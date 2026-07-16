#!/usr/bin/env python
"""Stage 3 cross-model QA — run the ChatGPT (codex) and Gemini (agy) legs.

Independent second/third opinions on the 250-item QA sample, judged with the SAME
instrument as the Opus run. The Opus verdicts are already in qa/qa_master_250.csv and
are NOT re-run — they are the thing being checked.

Each leg screens the identical blinded 250 (author-withheld) in chunks, with the same
hardening as stage3_screen.py: JSON-array extraction, item-key hallucination/omission
guard (>5% invented or any missing → reject + retry), per-chunk checkpoint, sleep
between calls. Writes qa/{leg}_out_250.csv for the scorer to join.

Legs (each pinned to that vendor's Opus-tier reasoning model, never the fast tier):
  codex   -> ChatGPT via `codex exec` (prompt on stdin), model gpt-5 @ reasoning=high
  gemini  -> Gemini via `agy -p` (prompt as ARG), model "Gemini 3.1 Pro (High)"

agy resets the shell cwd and takes the prompt as a positional arg, not stdin — both
handled here. Neither leg needs an API key: codex uses the ChatGPT login, agy its own.

Usage:
  python stage3_qa_screen.py --leg codex  run [--chunk N] [--limit-chunks K] [--override]
  python stage3_qa_screen.py --leg gemini run
  python stage3_qa_screen.py --leg codex  consolidate      # merge chunk outs -> {leg}_out_250.csv
"""
import argparse
import csv
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

# One source of truth for the instrument — reuse the Opus run's rubric + helpers.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from stage3_screen import RUBRIC, render_batch, extract_json  # noqa: E402

# Per-leg config. `model` is the Opus-equivalent top-reasoning tier for that vendor.
LEGS = {
    "codex":  {"src": "chatgpt_input_250.csv", "model": "gpt-5.5"},
    "gemini": {"src": "gemini_input_250.csv",  "model": "Gemini 3.1 Pro (High)"},
}


def call_codex(prompt, model, timeout):
    """ChatGPT leg via `codex exec` — prompt on stdin, answer captured from a file.

    read-only sandbox + skip-git-repo-check so it never touches the workspace; the
    task is pure classification, so no tools are needed."""
    with tempfile.NamedTemporaryFile("r+", suffix=".txt", delete=True) as out:
        cmd = ["codex", "exec", "--skip-git-repo-check", "--sandbox", "read-only",
               "-m", model, "-c", "model_reasoning_effort=high",
               "--output-last-message", out.name, "-"]
        proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                              timeout=timeout)
        if proc.returncode != 0:
            raise RuntimeError(f"codex exit {proc.returncode}: {(proc.stderr or '')[:400]}")
        out.seek(0)
        text = out.read()
    return text or proc.stdout or ""


def call_gemini(prompt, model, timeout):
    """Gemini leg via `agy -p` — prompt is a POSITIONAL arg (not stdin).

    subprocess list form avoids any shell quoting issues with the large prompt. agy
    resets cwd on exit, which doesn't matter here since we use absolute paths."""
    cmd = ["agy", "-p", prompt, "--model", model]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if proc.returncode != 0:
        raise RuntimeError(f"agy exit {proc.returncode}: {(proc.stderr or '')[:400]}")
    return proc.stdout or ""


CALLERS = {"codex": call_codex, "gemini": call_gemini}


def screen_chunk(rows, leg, model, timeout, retries=2):
    """Returns (verdicts_by_key, err). Retries on hallucinated/missing keys."""
    keys = {r["item_key"] for r in rows}
    prompt = RUBRIC + "\n\nITEMS TO SCREEN:\n\n" + render_batch(rows)
    last = ""
    for _ in range(retries + 1):
        try:
            objs = extract_json(CALLERS[leg](prompt, model, timeout))
        except Exception as e:  # noqa: BLE001
            last = str(e)
            time.sleep(3)
            continue
        by_key, halluc = {}, 0
        for o in objs:
            k = (o.get("item_key") or "").strip()
            if k in keys:
                by_key[k] = o
            else:
                halluc += 1
        missing = keys - set(by_key)
        if halluc / max(len(objs), 1) > 0.05 or missing:
            last = f"hallucinated={halluc} missing={len(missing)}"
            time.sleep(3)
            continue
        return by_key, ""
    return {}, last


def chunks_of(rows, n):
    for i in range(0, len(rows), n):
        yield i // n, rows[i:i + n]


def cmd_run(args):
    qa = Path(args.outdir) / "qa"
    leg = args.leg
    cfg = LEGS[leg]
    model = args.model or cfg["model"]
    rows = list(csv.DictReader(open(qa / cfg["src"], encoding="utf-8")))
    out_dir = qa / f"{leg}_out"
    out_dir.mkdir(exist_ok=True)

    ran = 0
    for ci, chunk in chunks_of(rows, args.chunk):
        if args.only_chunk is not None and ci != args.only_chunk:
            continue
        cout = out_dir / f"chunk_{ci:02d}.csv"
        if not args.override and cout.exists():
            continue
        if args.limit_chunks and ran >= args.limit_chunks:
            break
        print(f"[{leg} chunk_{ci:02d}] screening {len(chunk)} items via {model} ...", flush=True)
        verdicts, err = screen_chunk(chunk, leg, model, args.timeout)
        if err:
            print(f"[{leg} chunk_{ci:02d}] FAILED ({err}); leaving unset for re-run.", flush=True)
            time.sleep(args.sleep)
            continue
        with open(cout, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["item_key", "bin", "centrality", "reason_code", "rationale", "title"])
            for r in chunk:
                o = verdicts[r["item_key"]]
                w.writerow([r["item_key"], (o.get("bin") or "").lower(),
                            o.get("centrality", ""), o.get("reason_code", ""),
                            (o.get("rationale") or "").replace("\n", " ").strip(),
                            r.get("title", "")])
        ran += 1
        print(f"[{leg} chunk_{ci:02d}] ok ({len(verdicts)} verdicts).", flush=True)
        time.sleep(args.sleep)
    total = (len(rows) + args.chunk - 1) // args.chunk
    have = len(list(out_dir.glob("chunk_*.csv")))
    print(f"\n{leg}: {have}/{total} chunks complete.")
    if have == total:
        _consolidate(args)


def _consolidate(args):
    qa = Path(args.outdir) / "qa"
    leg = args.leg
    out_dir = qa / f"{leg}_out"
    merged, seen = [], set()
    for c in sorted(out_dir.glob("chunk_*.csv")):
        for r in csv.DictReader(open(c, encoding="utf-8")):
            if r["item_key"] not in seen:
                merged.append(r)
                seen.add(r["item_key"])
    dst = qa / f"{leg}_out_250.csv"
    with open(dst, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["item_key", "bin", "centrality",
                                           "reason_code", "rationale", "title"])
        w.writeheader()
        w.writerows(merged)
    print(f"wrote {dst}  ({len(merged)} verdicts)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--leg", required=True, choices=list(LEGS))
    ap.add_argument("--outdir", default="work")
    ap.add_argument("--model", default=None, help="override the leg's default model")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run"); r.set_defaults(fn=cmd_run)
    r.add_argument("--chunk", type=int, default=25)
    r.add_argument("--only-chunk", type=int, default=None, help="run just one chunk (calibration)")
    r.add_argument("--limit-chunks", type=int, default=0)
    r.add_argument("--override", action="store_true", help="re-run chunks even if their out exists")
    r.add_argument("--sleep", type=float, default=3.0)
    r.add_argument("--timeout", type=int, default=600)
    c = sub.add_parser("consolidate"); c.set_defaults(fn=_consolidate)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
