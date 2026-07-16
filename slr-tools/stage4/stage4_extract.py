#!/usr/bin/env python3
"""Stage 4 — per-document signal extraction for emergent codebook derivation.

For each Core document (from core_txt_map.csv) this reads the full text and
invokes the Claude Code CLI headlessly with the rubric in
`stage4_extract_rubric.md`, producing one structured JSON record per document.

- Model: Opus (the calibrated primary from Stage 3) by default.
- Long-tail docs are capped head+tail so the intro/methods/framework and the
  conclusion/limitations both survive (mechanism + insufficiency signals live
  at both ends), with an explicit [...TRUNCATED...] marker.
- Resumable: a document whose perdoc/<item_key>.json already exists is skipped.
- Descriptive extraction only — NOT an inclusion or classification decision.
  The AI is a consistency aid; every record is human-reviewable and traceable.

Outputs (under work/stage4/):
  perdoc/<item_key>.json     one raw validated record per document
  core_theme_signals.csv     flattened table (lists joined with ' | ')

Usage:
  source .envrc  # not required (no network), but keeps parity with other tools
  python3 stage4_extract.py            # run all pending
  python3 stage4_extract.py --limit 10 # first 10 pending (validation batch)
  python3 stage4_extract.py --only ITEMKEY1,ITEMKEY2
  python3 stage4_extract.py --model claude-opus-4-8
"""
import argparse
import csv
import json
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
MAP = HERE / "work" / "stage4" / "core_txt_map.csv"
RUBRIC = HERE / "stage4_extract_rubric.md"
PERDOC = HERE / "work" / "stage4" / "perdoc"
OUTCSV = HERE / "work" / "stage4" / "core_theme_signals.csv"

# char budget for the document body (~ head + tail). ~140k chars ≈ ~35k tokens.
HEAD_CHARS = 105_000
TAIL_CHARS = 35_000
CAP = HEAD_CHARS + TAIL_CHARS

LIST_FIELDS = ["evidence_type", "risk_types", "solution_mechanisms",
               "mechanism_keywords", "oversight_locus", "key_constructs",
               "governance_refs"]
SCALAR_FIELDS = ["item_key", "citation", "problem_statement",
                 "magnitude_evidence", "insufficiency_evidence",
                 "human_role", "scope_fit", "notes"]
ALL_FIELDS = ["item_key", "citation", "evidence_type", "problem_statement",
              "magnitude_evidence", "risk_types", "insufficiency_evidence",
              "solution_mechanisms", "mechanism_keywords", "oversight_locus",
              "human_role", "key_constructs", "governance_refs", "scope_fit",
              "notes"]


def load_doc(path, nbytes):
    text = Path(path).read_text(errors="replace")
    if len(text) <= CAP:
        return text, False
    head = text[:HEAD_CHARS]
    tail = text[-TAIL_CHARS:]
    return head + "\n\n[...TRUNCATED FOR LENGTH...]\n\n" + tail, True


def call_model(prompt, model, timeout=600):
    proc = subprocess.run(
        ["claude", "-p", "--model", model],
        input=prompt, capture_output=True, text=True, timeout=timeout,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"claude exit {proc.returncode}: {(proc.stderr or '')[:400]}")
    return proc.stdout or ""


def extract_json_obj(text):
    """Pull the first balanced JSON object out of the model output."""
    text = re.sub(r"^```(?:json)?|```$", "", (text or "").strip(), flags=re.M).strip()
    start = text.find("{")
    if start < 0:
        raise ValueError("no JSON object in output")
    depth, instr, esc = 0, False, False
    for i in range(start, len(text)):
        ch = text[i]
        if instr:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                instr = False
            continue
        if ch == '"':
            instr = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start:i + 1])
    raise ValueError("unterminated JSON object")


def normalize(rec, item_key, citation):
    """Coerce to the schema; force item_key/citation to the known-good values."""
    rec["item_key"] = item_key
    rec["citation"] = citation
    for f in LIST_FIELDS:
        v = rec.get(f)
        if v is None:
            rec[f] = []
        elif isinstance(v, str):
            rec[f] = [v] if v.strip() else []
        elif not isinstance(v, list):
            rec[f] = [str(v)]
    for f in SCALAR_FIELDS:
        if f not in rec:
            rec[f] = None
    return rec


def build_prompt(rubric, item_key, citation, title, body):
    header = (f"item_key: {item_key}\ncitation: {citation}\ntitle: {title}\n")
    return (rubric + "\n\n---\n\nDOCUMENT TO EXTRACT:\n\n" + header +
            "\n----- FULL TEXT BEGINS -----\n" + body +
            "\n----- FULL TEXT ENDS -----\n\n"
            "Return exactly one JSON object per the schema. No prose.")


def extract_one(row, rubric, model, retries=2):
    item_key = row["item_key"]
    citation = row["citation"]
    title = row.get("title", "")
    body, truncated = load_doc(row["txt_path"], int(row["bytes"]))
    prompt = build_prompt(rubric, item_key, citation, title, body)
    last_err = ""
    for attempt in range(retries + 1):
        try:
            raw = call_model(prompt, model)
            rec = extract_json_obj(raw)
            rec = normalize(rec, item_key, citation)
            rec["_truncated"] = truncated
            return rec, None
        except Exception as e:  # noqa: BLE001
            last_err = str(e)
            time.sleep(3)
    return None, last_err


def flatten(rec):
    out = {}
    for f in ALL_FIELDS:
        v = rec.get(f)
        if isinstance(v, list):
            out[f] = " | ".join(str(x) for x in v)
        else:
            out[f] = "" if v is None else str(v)
    out["_truncated"] = int(bool(rec.get("_truncated")))
    return out


def write_csv(records):
    cols = ALL_FIELDS + ["_truncated"]
    with open(OUTCSV, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in records:
            w.writerow(flatten(r))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="claude-opus-4-8")
    ap.add_argument("--limit", type=int, default=0, help="cap pending docs (0=all)")
    ap.add_argument("--only", default="", help="comma-separated item_keys")
    ap.add_argument("--force", action="store_true", help="re-extract even if perdoc exists")
    args = ap.parse_args()

    PERDOC.mkdir(parents=True, exist_ok=True)
    rubric = RUBRIC.read_text()
    rows = list(csv.DictReader(open(MAP)))
    if args.only:
        want = {k.strip() for k in args.only.split(",") if k.strip()}
        rows = [r for r in rows if r["item_key"] in want]

    pending = []
    for r in rows:
        pj = PERDOC / f"{r['item_key']}.json"
        if pj.exists() and not args.force:
            continue
        pending.append(r)
    if args.limit:
        pending = pending[:args.limit]

    print(f"{len(rows)} mapped docs; {len(pending)} pending this run "
          f"(model={args.model}, cap={CAP} chars)")
    problems = []
    t0 = time.time()
    for i, row in enumerate(pending, 1):
        rec, err = extract_one(row, rubric, args.model)
        tag = f"[{i}/{len(pending)}] {row['item_key']} {row['citation']}"
        if rec is None:
            print(f"  FAIL {tag}: {err[:120]}")
            problems.append((row["item_key"], err))
            continue
        (PERDOC / f"{row['item_key']}.json").write_text(json.dumps(rec, indent=2))
        trunc = " (trunc)" if rec.get("_truncated") else ""
        nm = len(rec.get("mechanism_keywords", []))
        print(f"  ok   {tag}{trunc}  scope={rec.get('scope_fit')} mech_kw={nm}")

    # (re)assemble the full CSV from all perdoc json on disk
    allrecs = []
    for pj in sorted(PERDOC.glob("*.json")):
        allrecs.append(json.loads(pj.read_text()))
    write_csv(allrecs)
    dt = time.time() - t0
    print(f"\nDone. {len(allrecs)} total records -> {OUTCSV}")
    print(f"This run: {len(pending)-len(problems)} ok, {len(problems)} failed, {dt:.0f}s")
    if problems:
        print("Failures (re-run to retry — resumable):")
        for k, e in problems:
            print(f"   {k}: {e[:100]}")


if __name__ == "__main__":
    main()
