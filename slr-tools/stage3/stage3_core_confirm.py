#!/usr/bin/env python
"""Build the core-confirmation worklist — all Opus 'core' primaries for human review.

Stage-3 QA showed Opus 'core' precision vs the human is ~30% (human demotes most to
context), the error is mostly extraction-DEPTH (core->context, still kept), and no model
can triage it (codex/agy push the opposite direction). So every core is human-confirmed
before it earns full extraction. Centrality RANKING is the one reliable signal
(cross-model Spearman ~0.69), so the sheet is sorted centrality-descending: confirm
top-down and stop when yield drops.

Output work/core_confirm.csv columns:
  rank, item_key, centrality(opus), title, authors, year, item_type, source, has_pdf,
  doi, arxiv_id, opus_rationale, abstract, + blank human_bin / human_note.
human_bin: core (confirm -> full extraction) | context (demote -> abstract-level) | discard.

Usage:  python stage3_core_confirm.py --outdir work
"""
import argparse
import csv
from collections import Counter
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default="work")
    args = ap.parse_args()
    work = Path(args.outdir)
    rows = list(csv.DictReader(open(work / "stage3_results.csv", encoding="utf-8")))
    cores = [r for r in rows if r["bin"] == "core" and r.get("is_primary") == "yes"]

    def cent(r):
        v = (r.get("centrality") or "").strip()
        return int(v) if v.lstrip("-").isdigit() else -1
    cores.sort(key=lambda r: -cent(r))

    cols = ["rank", "item_key", "centrality", "title", "authors", "year", "item_type",
            "source", "has_pdf", "doi", "arxiv_id", "opus_rationale", "abstract",
            "human_bin", "human_note"]
    dst = work / "core_confirm.csv"
    with open(dst, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for i, r in enumerate(cores, 1):
            w.writerow([i, r["item_key"], r.get("centrality", ""), r.get("title", ""),
                        r.get("authors", ""), r.get("year", ""), r.get("item_type", ""),
                        r.get("source", ""), r.get("has_pdf", ""), r.get("doi", ""),
                        r.get("arxiv_id", ""), r.get("rationale", ""),
                        r.get("abstract", ""), "", ""])

    need_fetch = sum(1 for r in cores if r.get("has_pdf") == "no")
    bands = Counter(f"{(cent(r)//10)*10}s" for r in cores)
    print(f"wrote {dst}  ({len(cores)} core primaries, sorted centrality-desc)")
    print(f"  need PDF fetch for full extraction (has_pdf=no): {need_fetch}")
    print("  centrality bands:", dict(sorted(bands.items(), key=lambda kv: -int(kv[0][:-1]))))


if __name__ == "__main__":
    main()
