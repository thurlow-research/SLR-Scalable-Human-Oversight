#!/usr/bin/env python
"""Split Stage-3 results into human-review buckets for the core double-down pass.

Sample-validated edges (from the Trust Check 50): Opus 'core' held up at centrality
>=75, but demoted ~6/7 of the time below 75; and the human found 'hidden cores' sitting
in Opus's context tier at centrality 45-55. So the review is banded by centrality across
both bins, each bucket a separate sheet:

  A_core_confirm_75plus   bin=core,    cent>=75      -> SKIM / fast-confirm (top band held up)
  B_core_review_70-74     bin=core,    70<=cent<=74  -> REVIEW (demote-risk cliff)
  C_core_review_60-69     bin=core,    60<=cent<=69  -> REVIEW (demote-risk, some discard)
  D_context_recall_55-69  bin=context, 55<=cent<=69  -> HIDDEN-CORE check (promote-risk)

Each sheet: sorted centrality-desc, review columns + blank human_bin / human_note.
human_bin: core (full extraction) | context (abstract-level) | discard.
Primaries only (dups inherit). Output -> work/review/<bucket>.csv

Usage:  python stage3_review_buckets.py --outdir work
"""
import argparse
import csv
from pathlib import Path

COLS = ["item_key", "opus_bin", "centrality", "title", "authors", "year", "item_type",
        "source", "has_pdf", "doi", "arxiv_id", "opus_rationale", "abstract",
        "human_bin", "human_note"]

BUCKETS = [
    ("A_core_confirm_75plus",  "core",    75, 100, "SKIM / fast-confirm"),
    ("B_core_review_70-74",    "core",    70, 74,  "REVIEW (demote-risk)"),
    ("C_core_review_60-69",    "core",    60, 69,  "REVIEW (demote-risk)"),
    ("D_context_recall_55-69", "context", 55, 69,  "HIDDEN-CORE check"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default="work")
    args = ap.parse_args()
    work = Path(args.outdir)
    rows = [r for r in csv.DictReader(open(work / "stage3_results.csv", encoding="utf-8"))
            if r.get("is_primary") == "yes"]

    def cent(r):
        v = (r.get("centrality") or "").strip()
        return int(v) if v.lstrip("-").isdigit() else -1

    outdir = work / "review"
    outdir.mkdir(exist_ok=True)
    print(f"buckets -> {outdir}")
    total = 0
    for name, b, lo, hi, note in BUCKETS:
        sel = sorted([r for r in rows if r["bin"] == b and lo <= cent(r) <= hi],
                     key=lambda r: -cent(r))
        with open(outdir / f"{name}.csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(COLS)
            for r in sel:
                w.writerow([r["item_key"], r["bin"], r.get("centrality", ""),
                            r.get("title", ""), r.get("authors", ""), r.get("year", ""),
                            r.get("item_type", ""), r.get("source", ""), r.get("has_pdf", ""),
                            r.get("doi", ""), r.get("arxiv_id", ""), r.get("rationale", ""),
                            r.get("abstract", ""), "", ""])
        nf = sum(1 for r in sel if r.get("has_pdf") == "no")
        total += len(sel)
        print(f"  {name}.csv  n={len(sel):>3}  (no-PDF {nf:>3})  — {note}")
    print(f"total across buckets: {total}")


if __name__ == "__main__":
    main()
