#!/usr/bin/env python3
"""Stage 4 — research-method SEED pass (emergent, full multi-label).

Purpose: produce an *actual* method/design distribution over the 114 cores so a
vocabulary can be chosen bottom-up. Open-vocabulary, multi-label. This is a seed
for vocabulary selection, not the locked classification; every label is
human-reviewable afterward.

Cheap by design: feeds only the abstract+intro slice (first ~9k chars, where
research design is declared) plus the already-extracted evidence_type signals,
not the full text. Resumable per-doc.

Outputs (work/stage4/):
  perdoc_method/<item_key>.json
  core_methods_seed.csv   (methods joined ' | ')
"""
import argparse
import csv
import json
import re
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).parent
MAP = HERE / "work" / "stage4" / "core_txt_map.csv"
PERDOC = HERE / "work" / "stage4" / "perdoc"
OUTDIR = HERE / "work" / "stage4" / "perdoc_method"
OUTCSV = HERE / "work" / "stage4" / "core_methods_seed.csv"
# full text, head+tail capped for the long tail (matches stage4_extract.py) —
# method/design is often stated in a deep methods section, not the abstract.
HEAD_CHARS = 105_000
TAIL_CHARS = 35_000
CAP = HEAD_CHARS + TAIL_CHARS


def load_doc(path):
    text = Path(path).read_text(errors="replace")
    if len(text) <= CAP:
        return text
    return text[:HEAD_CHARS] + "\n\n[...TRUNCATED FOR LENGTH...]\n\n" + text[-TAIL_CHARS:]

RUBRIC = """You are classifying the RESEARCH METHOD / STUDY DESIGN of one primary
document in a systematic literature review on human oversight of AI-generated code.

Return exactly one JSON object (no prose, no code fences):
{
  "item_key": "<echo>",
  "methods": ["<open, descriptive multi-labels for EVERY research method/design the paper actually uses>"],
  "empirical": true/false,        // does it collect or analyze data / evaluate an artifact empirically?
  "human_subjects": true/false,   // does it survey, interview, or run a user study with human participants?
  "primary_hint": "<the single most central method, for optional later use>",
  "notes": "<caveat or null>"
}

Guidance for `methods` labels (use the paper's own reality; invent labels if needed;
DO NOT force into a fixed list):
  design-science / prototype / tool-build, controlled-experiment, benchmark-evaluation,
  repository-mining/MSR (observational analysis of public/OSS repos, PRs, commits, issues),
  measurement-study, case-study, field-study, survey/questionnaire, interviews,
  qualitative-analysis, grounded-theory, simulation, formal-analysis/proof,
  literature-review/mapping, multivocal/grey-literature-review, conceptual/position/framework,
  dataset-contribution, ablation-study.
- repository-mining/MSR = observational mining of real-world repositories; it is NOT a
  controlled-experiment (no manipulation), NOT a case-study (large-scale quantitative,
  not one in-depth context), and NOT a benchmark (mines real repos, not a curated task set).
- Multi-label: a paper that builds a tool AND benchmarks it gets both.
- A pure argument/roadmap with no data = ["conceptual/position"], empirical=false.
- human_subjects=true ONLY for real participant data (survey/interview/user-study),
  NOT for using human-written code as a baseline.
"""


def call_model(prompt, model, timeout=600):
    proc = subprocess.run(["claude", "-p", "--model", model],
                          input=prompt, capture_output=True, text=True, timeout=timeout)
    if proc.returncode != 0:
        raise RuntimeError(f"claude exit {proc.returncode}: {(proc.stderr or '')[:300]}")
    return proc.stdout or ""


def extract_json_obj(text):
    text = re.sub(r"^```(?:json)?|```$", "", (text or "").strip(), flags=re.M).strip()
    start = text.find("{")
    if start < 0:
        raise ValueError("no JSON object")
    depth, instr, esc = 0, False, False
    for i in range(start, len(text)):
        ch = text[i]
        if instr:
            esc = (ch == "\\" and not esc)
            if ch == '"' and not esc:
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
    raise ValueError("unterminated JSON")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="claude-opus-4-8")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(open(MAP)))

    pending = [r for r in rows if not (OUTDIR / f"{r['item_key']}.json").exists()]
    if args.limit:
        pending = pending[:args.limit]
    print(f"{len(rows)} docs; {len(pending)} pending (model={args.model})")

    fails = []
    for i, r in enumerate(pending, 1):
        key = r["item_key"]
        pj = PERDOC / f"{key}.json"
        et = []
        if pj.exists():
            et = json.load(open(pj)).get("evidence_type", [])
        body = load_doc(r["txt_path"])
        prompt = (RUBRIC + f"\n\nitem_key: {key}\ncitation: {r['citation']}\n"
                  f"title: {r.get('title','')}\n"
                  f"prior evidence_type signals: {et}\n"
                  f"\n----- FULL TEXT BEGINS -----\n{body}\n----- FULL TEXT ENDS -----\n"
                  "Return one JSON object. Base the method on what the paper ACTUALLY "
                  "does in its methods/evaluation, not just the abstract.")
        ok = False
        for _ in range(3):
            try:
                rec = extract_json_obj(call_model(prompt, args.model))
                rec["item_key"] = key
                rec["citation"] = r["citation"]
                if isinstance(rec.get("methods"), str):
                    rec["methods"] = [rec["methods"]]
                rec.setdefault("methods", [])
                (OUTDIR / f"{key}.json").write_text(json.dumps(rec, indent=2))
                hs = "H" if rec.get("human_subjects") else " "
                em = "E" if rec.get("empirical") else " "
                print(f"  [{i}/{len(pending)}] {key} {r['citation']:<22} {em}{hs} "
                      f"{' | '.join(rec['methods'])[:70]}")
                ok = True
                break
            except Exception as e:  # noqa: BLE001
                time.sleep(2)
                last = str(e)
        if not ok:
            print(f"  FAIL {key}: {last[:80]}")
            fails.append(key)

    # assemble csv
    recs = [json.load(open(p)) for p in sorted(OUTDIR.glob("*.json"))]
    with open(OUTCSV, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["item_key", "citation", "methods", "empirical",
                    "human_subjects", "primary_hint", "notes"])
        for r in recs:
            w.writerow([r["item_key"], r.get("citation", ""),
                        " | ".join(r.get("methods", [])),
                        int(bool(r.get("empirical"))),
                        int(bool(r.get("human_subjects"))),
                        r.get("primary_hint", ""), r.get("notes", "")])
    print(f"\n{len(recs)} records -> {OUTCSV}; {len(fails)} failed")


if __name__ == "__main__":
    main()
