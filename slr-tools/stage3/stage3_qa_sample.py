#!/usr/bin/env python
"""Stage 3 QA sampler — draw the cross-model + human verification samples.

From work/stage3_results.csv (the Opus verdicts) it draws:
  - a 250-item stratified-random sample (proportional across core/context/discard)
    given INDEPENDENTLY to Gemini Advanced and ChatGPT Pro (same 250 for both, so
    all three legs are comparable on a shared set), and
  - a 50-item stratified subset OF the 250 for blinded HUMAN review.

QA is on PRIMARIES only — flagged duplicates inherit the primary's verdict, so
re-judging them adds no signal.

Blinding, by design:
  - model input files carry NO Opus verdict and NO author (the Stage-3 rubric is
    deliberately author-blind) — each leg judges fresh.
  - the human sheet is also blinded to the Opus verdict (avoids anchoring) but
    keeps authors, since human adjudication is holistic.
  - work/qa/qa_master_250.csv holds the Opus verdicts + the in_human_50 flag; it is
    the SCORING KEY and is never handed to a model.

Everything is seeded (SEED below) so the draw is reproducible and documentable.

Usage:  python stage3_qa_sample.py --outdir work [--chunk 25]
"""
import argparse
import csv
import random
from collections import defaultdict
from pathlib import Path

SEED = 20260706                 # reproducible; = the sampling date (2026-07-06)
N_MODEL = 250
N_HUMAN = 50

# Fields shown to a model leg (blinded, author-withheld) + blanks for its verdict.
MODEL_IN = ["seq", "item_key", "title", "year", "item_type", "abstract"]
MODEL_OUT = ["bin", "centrality", "reason_code", "rationale"]   # they fill these
# Human sheet: same, plus authors (human review is not author-blind).
HUMAN_IN = ["seq", "item_key", "title", "authors", "year", "item_type", "abstract"]


def proportional(n_total, pools, universe_n):
    """Largest-remainder proportional allocation across strata."""
    raw = {b: n_total * len(v) / universe_n for b, v in pools.items()}
    alloc = {b: int(raw[b]) for b in pools}
    rem = n_total - sum(alloc.values())
    for b in sorted(pools, key=lambda b: raw[b] - alloc[b], reverse=True)[:rem]:
        alloc[b] += 1
    return alloc


def write_blinded(path, rows, cols):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cols + MODEL_OUT)
        for i, r in enumerate(rows, 1):
            base = [i if c == "seq" else (r.get(c) or "") for c in cols]
            w.writerow(base + ["", "", "", ""])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default="work")
    ap.add_argument("--chunk", type=int, default=25,
                    help="items per per-model chunk file (fresh-chat-per-chunk protocol)")
    args = ap.parse_args()

    work = Path(args.outdir)
    rows = list(csv.DictReader(open(work / "stage3_results.csv", encoding="utf-8")))
    prim = [r for r in rows if r.get("is_primary") == "yes"]
    N = len(prim)

    by_bin = defaultdict(list)
    for r in prim:
        by_bin[r["bin"]].append(r)

    # --- 250 stratified random ---
    random.seed(SEED)
    alloc250 = proportional(N_MODEL, by_bin, N)
    sample250 = []
    for b, v in by_bin.items():
        sample250 += random.sample(v, alloc250[b])
    # stable, reproducible presentation order (shuffle so bins are interleaved)
    random.seed(SEED + 2)
    random.shuffle(sample250)

    # --- 50 stratified subset of the 250 ---
    pools50 = defaultdict(list)
    for r in sample250:
        pools50[r["bin"]].append(r)
    alloc50 = proportional(N_HUMAN, pools50, len(sample250))
    random.seed(SEED + 1)
    human_keys = set()
    for b, v in pools50.items():
        for r in random.sample(v, alloc50[b]):
            human_keys.add(r["item_key"])
    human_rows = [r for r in sample250 if r["item_key"] in human_keys]

    qa = work / "qa"
    qa.mkdir(exist_ok=True)

    # Scoring key (never given to a model): Opus verdicts + flags + full metadata.
    master_cols = ["item_key", "bin", "centrality", "reason_code", "rationale",
                   "in_human_50", "title", "authors", "year", "item_type",
                   "source", "has_pdf", "doi", "arxiv_id", "abstract"]
    with open(qa / "qa_master_250.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=master_cols, extrasaction="ignore")
        w.writeheader()
        for r in sample250:
            w.writerow({**r, "in_human_50": "yes" if r["item_key"] in human_keys else "no"})

    # Blinded model input files (identical 250 for both legs).
    write_blinded(qa / "gemini_input_250.csv", sample250, MODEL_IN)
    write_blinded(qa / "chatgpt_input_250.csv", sample250, MODEL_IN)
    # Blinded human sheet (50), authors included.
    write_blinded(qa / "human_review_50.csv", human_rows, HUMAN_IN)

    # Per-model chunk files for the fresh-chat-per-chunk protocol.
    for leg in ("gemini", "chatgpt"):
        d = qa / f"{leg}_chunks"
        d.mkdir(exist_ok=True)
        for c in list(d.glob("chunk_*.csv")):
            c.unlink()
        for ci in range(0, len(sample250), args.chunk):
            chunk = sample250[ci:ci + args.chunk]
            write_blinded(d / f"chunk_{ci//args.chunk:02d}.csv", chunk, MODEL_IN)

    print(f"SEED={SEED}  universe(primaries)={N}")
    print(f"250 allocation: {alloc250}  (sum {sum(alloc250.values())})")
    print(f" 50 allocation: {alloc50}  (sum {len(human_keys)})")
    print(f"wrote {qa}/qa_master_250.csv  (scoring key)")
    print(f"      {qa}/gemini_input_250.csv / chatgpt_input_250.csv  (blinded, author-withheld)")
    print(f"      {qa}/human_review_50.csv  (blinded, authors kept)")
    n_chunks = (len(sample250) + args.chunk - 1) // args.chunk
    print(f"      {qa}/gemini_chunks/ + chatgpt_chunks/  ({n_chunks} chunks of ≤{args.chunk})")


if __name__ == "__main__":
    main()
