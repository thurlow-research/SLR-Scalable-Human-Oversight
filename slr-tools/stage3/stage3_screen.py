#!/usr/bin/env python
"""Stage 3 screen step — relevance triage of the 976 primaries via Claude (Opus).

Runs each batch through `claude -p`, forcing a strict JSON verdict per item:
  { item_key, bin (core|context|discard), centrality (0-100), reason_code, rationale }

Follows the slr-pipeline-patterns hardening:
  - per-batch checkpoint (only failed/unrun batches re-execute)
  - header/JSON-anchored extraction from model output
  - item-key hallucination validation (drop unknown keys; retry if >5% or any missing)
  - sleep between calls; checkpoint only set after a clean batch
  - None-guards on all string ops

Subcommands:
  run          process all pending batches (resumable). --limit-batches N, --batch NNN
  consolidate  join verdicts with stage3_input.csv, propagate dup decisions,
               write stage3_results.csv + print the bin distribution

Model call is isolated in call_model(); adjust there if your `claude` invocation differs.
"""
import argparse
import csv
import json
import re
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# The instrument. Edit this rubric only deliberately — it defines the Stage-3 cut.
# ─────────────────────────────────────────────────────────────────────────────
RUBRIC = """\
You are a screening assistant for a PRISMA systematic literature review. You apply \
the reviewer's criteria consistently; you do NOT make the final scholarly judgment. \
Judge each item independently and on its own merits — do not default to keeping.

REVIEW TOPIC / CORE RESEARCH QUESTION
How do organizations practice and scale HUMAN OVERSIGHT of AI-GENERATED CODE ("vibe \
coding") so that oversight keeps pace with code volume WITHOUT sacrificing quality — \
including the governance/policy landscape and the strengths/limitations of current \
oversight practices.

TASK
These items already passed two abstract-level screens (recall, then operationalizability). \
Your job is a RELEVANCE TRIAGE: assign each to one bin and a 0-100 centrality score \
(how central it is to the core RQ). Score drives ranking; the bins are:

CORE (centrality 70-100): Directly addresses scalable human oversight / governance of \
AI-generated code in an organizational or software-engineering pipeline context, WITH an \
operationalizable mechanism, measurement, framework, or empirical finding. Examples: \
vibe-coding governance; AI-code risk recognition/measurement in orgs; code-review \
scalability under AI volume; human-in-the-loop / LLM-as-judge / adversarial-agent \
oversight triggers; developer overtrust/over-reliance in AI coding; org governance \
responses specific to AI-generated code.

CONTEXT (centrality 30-69): Adjacent BUT methodologically strong and transferable — the \
volume/risk problem, or human oversight / AI governance in a broader setting (other AI \
application domains, general DevSecOps, automation-bias theory, non-code-specific \
regulatory frameworks) where the finding plausibly transfers to AI-code oversight. Must \
have an evidence base or a concrete framework — NOT opinion.

DISCARD (centrality 0-29): Weak AND off-core. Keyword-only matches; descriptive-only with \
no operationalizable/transferable angle; non-software domain with no transfer; LLM \
capability benchmarks with no governance link; opinion/position without an evidence base; \
or known false-positive classes: blockchain, classroom/educational scenarios, pure \
developer-productivity studies with no oversight angle.
For DISCARD only, set reason_code to ONE of: out-of-scope | wrong-level | wrong-type | \
too-old | quality-threshold-not-met. For CORE/CONTEXT leave reason_code "".

If the abstract is missing or too thin to judge, use your best estimate and set a \
centrality near the CONTEXT/DISCARD border (25-40) with rationale noting the thin abstract \
(these get human review).

OUTPUT — STRICT
Return ONLY a JSON array, one object per input item, no prose, no markdown fences:
[{"item_key":"XXXXXXXX","bin":"core|context|discard","centrality":0-100,"reason_code":"","rationale":"one sentence"}]
Echo item_key EXACTLY as given. Include every item. rationale = one short sentence.
"""


def call_model(prompt, model, timeout=300):
    """Invoke the Claude Code CLI headlessly, prompt via stdin. Returns stdout text.
    Adjust this function if your local `claude` invocation differs."""
    proc = subprocess.run(
        ["claude", "-p", "--model", model],
        input=prompt, capture_output=True, text=True, timeout=timeout,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"claude exit {proc.returncode}: {(proc.stderr or '')[:400]}")
    return proc.stdout or ""


def render_batch(rows):
    lines = []
    for i, r in enumerate(rows, 1):
        ab,ti = (r.get("abstract") or "").strip(), (r.get("title") or "").strip()
        lines.append(
            f'--- ITEM {i} ---\nitem_key: {r["item_key"]}\ntitle: {ti}\n'
            f'year: {r.get("year","")}  type: {r.get("item_type","")}\n'
            f'abstract: {ab if ab else "(no abstract available)"}'
        )
    return "\n\n".join(lines)


def extract_json(text):
    """Pull the first JSON array out of the model output (tolerates fences/preamble)."""
    text = re.sub(r"^```(?:json)?|```$", "", (text or "").strip(), flags=re.M).strip()
    start = text.find("[")
    if start < 0:
        raise ValueError("no JSON array in output")
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "[":
            depth += 1
        elif text[i] == "]":
            depth -= 1
            if depth == 0:
                return json.loads(text[start:i + 1])
    raise ValueError("unterminated JSON array")


def screen_batch(rows, model, retries=2):
    """Returns (verdicts_by_key, problems). Retries on hallucination/missing."""
    batch_keys = {r["item_key"] for r in rows}
    prompt = RUBRIC + "\n\nITEMS TO SCREEN:\n\n" + render_batch(rows)
    last_err = ""
    for attempt in range(retries + 1):
        try:
            objs = extract_json(call_model(prompt, model))
        except Exception as e:  # noqa: BLE001
            last_err = str(e)
            time.sleep(3)
            continue
        by_key, hallucinated = {}, 0
        for o in objs:
            k = (o.get("item_key") or "").strip()
            if k in batch_keys:
                by_key[k] = o
            else:
                hallucinated += 1
        missing = batch_keys - set(by_key)
        # Pattern 7: reject the attempt if the model invented keys or dropped items.
        if hallucinated / max(len(objs), 1) > 0.05 or missing:
            last_err = f"hallucinated={hallucinated} missing={len(missing)}"
            time.sleep(3)
            continue
        return by_key, ""
    return {}, last_err


def cmd_run(args):
    work = Path(args.outdir)
    bdir = work / "batches"
    batch_files = sorted(bdir.glob("batch_[0-9][0-9][0-9].csv"))
    if args.batch is not None:
        batch_files = [bdir / f"batch_{args.batch:03d}.csv"]
    ckpt_path = work / "checkpoint.json"
    ckpt = json.loads(ckpt_path.read_text()) if ckpt_path.exists() else {"done": []}
    done = set(ckpt["done"])

    ran = 0
    for bf in batch_files:
        name = bf.stem
        out_path = work / f"{name}_out.csv"
        # Skip already-done batches unless --override forces a re-screen.
        if not args.override and name in done and out_path.exists():
            continue
        if args.limit_batches and ran >= args.limit_batches:
            break
        rows = list(csv.DictReader(open(bf, encoding="utf-8")))
        print(f"[{name}] screening {len(rows)} items via {args.model} ...", flush=True)
        verdicts, err = screen_batch(rows, args.model)
        if err:
            print(f"[{name}] FAILED ({err}); leaving unset for re-run.", flush=True)
            time.sleep(args.sleep)
            continue
        with open(out_path, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            # Verdict fields come from the model; title/authors/abstract are joined
            # locally from the batch input (r) so each _out is directly reviewable
            # during calibration — the model never sees or re-emits them.
            w.writerow(["item_key", "bin", "centrality", "reason_code", "rationale",
                        "title", "authors", "abstract"])
            for r in rows:  # preserve batch order
                o = verdicts[r["item_key"]]
                w.writerow([r["item_key"], (o.get("bin") or "").lower(),
                            o.get("centrality", ""), o.get("reason_code", ""),
                            (o.get("rationale") or "").replace("\n", " ").strip(),
                            r.get("title", ""), r.get("authors", ""),
                            r.get("abstract", "")])
        done.add(name)                                   # checkpoint AFTER success
        ckpt_path.write_text(json.dumps({"done": sorted(done)}, indent=2))
        ran += 1
        print(f"[{name}] ok ({len(verdicts)} verdicts).", flush=True)
        time.sleep(args.sleep)
    print(f"\ndone. {len(done)}/{len(sorted(bdir.glob('batch_[0-9][0-9][0-9].csv')))} "
          f"batches complete.")


def cmd_consolidate(args):
    work = Path(args.outdir)
    meta = {r["item_key"]: r for r in csv.DictReader(open(work / "stage3_input.csv", encoding="utf-8"))}
    verdicts = {}
    for out in sorted(work.glob("batch_[0-9][0-9][0-9]_out.csv")):
        for r in csv.DictReader(open(out, encoding="utf-8")):
            verdicts[r["item_key"]] = r

    # Propagate each primary's verdict to its flagged duplicates.
    for k, m in meta.items():
        if m.get("is_primary") == "no" and m.get("dup_group") in verdicts:
            v = dict(verdicts[m["dup_group"]])
            v["item_key"] = k
            verdicts[k] = v

    missing = [k for k in meta if k not in verdicts]
    cols = ["item_key", "bin", "centrality", "reason_code", "title", "authors",
            "year", "item_type", "source", "has_pdf", "doi", "arxiv_id",
            "retrieval_route", "is_primary", "dup_group", "rationale", "abstract"]
    out_csv = work / "stage3_results.csv"
    with open(out_csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for k, m in sorted(meta.items(),
                           key=lambda kv: -int(verdicts.get(kv[0], {}).get("centrality") or 0)):
            v = verdicts.get(k, {})
            w.writerow({**m, **{c: v.get(c, "") for c in
                                ("bin", "centrality", "reason_code", "rationale")}})
    print(f"wrote {out_csv}  ({len(meta)} items; {len(missing)} unscreened)")
    if missing:
        print("  UNSCREENED (re-run those batches):", ", ".join(missing[:10]),
              "..." if len(missing) > 10 else "")
    bins = Counter((verdicts.get(k, {}).get("bin") or "?") for k in meta)
    print("  bins:", dict(bins))
    core = [k for k in meta if (verdicts.get(k, {}).get("bin") == "core")]
    core_fetch = [k for k in core if meta[k]["has_pdf"] == "no" and meta[k]["is_primary"] == "yes"]
    print(f"  CORE={len(core)}  (of which {len(core_fetch)} need fetching, "
          f"{len(core)-len(core_fetch)} already have PDF/are dups)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default="work")
    ap.add_argument("--model", default="opus")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run"); r.set_defaults(fn=cmd_run)
    r.add_argument("--sleep", type=float, default=5.0)
    r.add_argument("--limit-batches", type=int, default=0)
    r.add_argument("--batch", type=int, default=None)
    r.add_argument("--override", action="store_true",
                   help="Re-screen in-scope batches even if already checkpointed "
                        "(ignores checkpoint + existing _out). Respects --batch/--limit-batches.")
    c = sub.add_parser("consolidate"); c.set_defaults(fn=cmd_consolidate)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
