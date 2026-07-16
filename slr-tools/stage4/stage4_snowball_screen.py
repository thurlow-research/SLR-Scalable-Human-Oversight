#!/usr/bin/env python3
"""Snowball screening — two-phase, mirroring the main corpus.

Phase 1: Sonnet title/abstract screen (slr-phase-1-2/phase2/pass2_sonnet_prompt.md)
         over the non-dupe candidates -> keep/maybe/discard.
Phase 2: Opus deep review (pass2_opus_prompt.md) over the Phase-1 MAYBES -> keep/discard.

Batched, resumable (skips item_keys already in the output CSV). CSV model output is
parsed tolerantly. Human review of exceptions + loading into Zotero are separate steps.

Usage:
  python3 stage4_snowball_screen.py --phase 1 --model sonnet
  python3 stage4_snowball_screen.py --phase 2 --model opus
"""
import argparse
import csv
import io
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
WORK = HERE / "work" / "stage4"
PROMPTS = HERE.parent.parent / "slr-phase-1-2" / "phase2"
P1_PROMPT = PROMPTS / "pass2_sonnet_prompt.md"
P2_PROMPT = PROMPTS / "pass2_opus_prompt.md"
INPUT = WORK / "snowball_screen_input.csv"
P1_OUT = WORK / "snowball_screen_p1.csv"
P2_OUT = WORK / "snowball_screen_p2.csv"
BATCH = 20


def call_model(prompt, model, timeout=600):
    p = subprocess.run(["claude", "-p", "--model", model], input=prompt,
                       capture_output=True, text=True, timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError(f"claude exit {p.returncode}: {(p.stderr or '')[:300]}")
    return p.stdout or ""


def parse_csv_block(text, keys):
    """Pull rows out of the model's CSV output; keep only known item_keys."""
    text = re.sub(r"^```(?:csv)?|```$", "", text.strip(), flags=re.M).strip()
    # find the header line
    lines = text.splitlines()
    start = next((i for i, ln in enumerate(lines) if ln.lower().startswith("item_key")), 0)
    rdr = csv.DictReader(io.StringIO("\n".join(lines[start:])))
    out = {}
    for row in rdr:
        k = (row.get("item_key") or "").strip()
        if k in keys:
            out[k] = row
    return out


def load_done(path):
    if not path.exists():
        return {}
    return {r["item_key"]: r for r in csv.DictReader(open(path))}


def append_rows(path, rows, header):
    new = not path.exists()
    with open(path, "a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=header)
        if new:
            w.writeheader()
        for r in rows:
            w.writerow(r)


def render(rows, cols):
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(cols)
    for r in rows:
        w.writerow([r.get(c, "") for c in cols])
    return buf.getvalue()


def phase1(model):
    rubric = P1_PROMPT.read_text()
    done = load_done(P1_OUT)
    rows = [r for r in csv.DictReader(open(INPUT)) if r["item_key"] not in done]
    print(f"Phase 1 (Sonnet): {len(rows)} pending, {len(done)} done")
    for i in range(0, len(rows), BATCH):
        batch = rows[i:i + BATCH]
        keys = {r["item_key"] for r in batch}
        csv_in = render([{"item_key": r["item_key"], "title": r["title"],
                          "abstract": r["abstract"] or "(no abstract available)"}
                         for r in batch], ["item_key", "title", "abstract"])
        prompt = rubric.replace("[PASTE BATCH CSV HERE]", csv_in)
        got = {}
        for _ in range(3):
            try:
                got = parse_csv_block(call_model(prompt, model), keys)
            except Exception as e:  # noqa: BLE001
                time.sleep(3)
                continue
            if len(got) >= len(keys) * 0.8:
                break
        out = []
        for r in batch:
            g = got.get(r["item_key"], {})
            out.append({"item_key": r["item_key"], "cocite": r["cocite"],
                        "decision": (g.get("decision") or "maybe").strip().lower(),
                        "confidence": (g.get("confidence") or "low").strip().lower(),
                        "rationale": (g.get("rationale") or "MISSING-from-model").strip(),
                        "title": r["title"]})
        append_rows(P1_OUT, out, ["item_key", "cocite", "decision", "confidence", "rationale", "title"])
        print(f"  {min(i+BATCH,len(rows))}/{len(rows)}")
    from collections import Counter
    allrows = list(csv.DictReader(open(P1_OUT)))
    print("Phase-1 distribution:", dict(Counter(r["decision"] for r in allrows)))


def phase2(model, decisions=("maybe",)):
    rubric = P2_PROMPT.read_text()
    p1 = list(csv.DictReader(open(P1_OUT)))
    inp = {r["item_key"]: r for r in csv.DictReader(open(INPUT))}
    maybes = [r for r in p1 if r["decision"] in decisions]
    done = load_done(P2_OUT)
    pending = [r for r in maybes if r["item_key"] not in done]
    print(f"Phase 2 (Opus): {len(maybes)} maybes, {len(pending)} pending")
    for i in range(0, len(pending), BATCH):
        batch = pending[i:i + BATCH]
        keys = {r["item_key"] for r in batch}
        csv_in = render([{"item_key": r["item_key"], "title": r["title"],
                          "abstract": inp.get(r["item_key"], {}).get("abstract") or "(no abstract available)",
                          "prior_decision": r["decision"], "prior_confidence": r["confidence"],
                          "prior_rationale": r["rationale"]} for r in batch],
                        ["item_key", "title", "abstract", "prior_decision", "prior_confidence", "prior_rationale"])
        prompt = (rubric.replace("[PASTE BATCH CSV HERE]", csv_in)
                        .replace("[PASTE REVIEW CSV HERE]", csv_in))
        if "[PASTE" not in rubric:
            prompt = rubric + "\n\n" + csv_in
        got = {}
        for _ in range(3):
            try:
                got = parse_csv_block(call_model(prompt, model), keys)
            except Exception:
                time.sleep(3)
                continue
            if len(got) >= len(keys) * 0.8:
                break
        out = []
        for r in batch:
            g = got.get(r["item_key"], {})
            out.append({"item_key": r["item_key"], "cocite": r["cocite"],
                        "decision": (g.get("decision") or "discard").strip().lower(),
                        "confidence": (g.get("confidence") or "low").strip().lower(),
                        "rationale": (g.get("rationale") or "MISSING-from-model").strip()})
        append_rows(P2_OUT, out, ["item_key", "cocite", "decision", "confidence", "rationale"])
        print(f"  {min(i+BATCH,len(pending))}/{len(pending)}")
    from collections import Counter
    print("Phase-2 distribution:", dict(Counter(r["decision"] for r in csv.DictReader(open(P2_OUT)))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", type=int, required=True, choices=[1, 2])
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--input", help="override input CSV")
    ap.add_argument("--p1out", help="override phase-1 output CSV")
    ap.add_argument("--p2out", help="override phase-2 output CSV")
    ap.add_argument("--rescreen", default="maybe",
                    help="comma-list of phase-1 decisions to re-screen in phase 2 (default: maybe)")
    a = ap.parse_args()
    global INPUT, P1_OUT, P2_OUT
    if a.input:
        INPUT = Path(a.input)
    if a.p1out:
        P1_OUT = Path(a.p1out)
    if a.p2out:
        P2_OUT = Path(a.p2out)
    if a.phase == 1:
        phase1(a.model)
    else:
        phase2(a.model, tuple(d.strip() for d in a.rescreen.split(",")))


if __name__ == "__main__":
    main()
