#!/usr/bin/env python3
"""
Build cross-model validation workbook from non_ssrn_llm_screen.py decisions.csv.

Usage:
    # Build full workbook (all decisions):
    python3 build_validation_sheet.py

    # Build stratified random sample of N items:
    python3 build_validation_sheet.py --sample 500

    # Sample with fixed seed for reproducibility:
    python3 build_validation_sheet.py --sample 500 --seed 42

Output:
    decisions_validation.csv   — full or sampled workbook, ready for:
                                  1. You to fill in human_decision column
                                  2. Uploading to ChatGPT (cols: item_key, title, abstract)
                                  3. Uploading to Gemini  (cols: item_key, title, abstract)
                                  4. Merging back chatgpt_decision and gemini_decision columns

Columns in output:
    item_key          — Zotero item key
    source            — source database (ieee, scopus, acm, arxiv, wos)
    title             — paper title
    authors           — author list
    year              — publication year
    url               — URL if available
    abstract          — full abstract
    claude_decision   — Claude Sonnet 4.6 decision (keep/maybe/discard)
    claude_category   — Claude category tag (for discards)
    claude_rationale  — Claude one-line rationale
    human_decision    — BLANK — fill in manually for your 100-item spot-check
    chatgpt_decision  — BLANK — fill in from ChatGPT validation run
    gemini_decision   — BLANK — fill in from Gemini validation run

Sampling strategy (--sample N):
    Proportionally stratified by claude_decision so the sample reflects
    the actual keep/maybe/discard distribution. Within each stratum,
    items are randomly selected.
"""

import csv, os, sys, random, argparse
from collections import defaultdict

WORKDIR = os.path.expanduser("~/slr/non-ssrn")
INPUT_CSV  = os.path.join(WORKDIR, "decisions.csv")
OUTPUT_CSV = os.path.join(WORKDIR, "decisions_validation.csv")

# Input columns from non_ssrn_llm_screen.py
IN_COLS = ["item_key", "decision", "category", "title", "authors", "year", "url", "rationale", "abstract"]

# Output columns
OUT_COLS = [
    "item_key", "source", "title", "authors", "year", "url", "abstract",
    "claude_decision", "claude_category", "claude_rationale",
    "human_decision", "chatgpt_decision", "gemini_decision"
]


def load_decisions(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def stratified_sample(rows, n, seed=None):
    """
    Proportionally stratified random sample of n rows by claude_decision.
    Preserves keep/maybe/discard distribution from full corpus.
    """
    rng = random.Random(seed)

    # Group by decision
    strata = defaultdict(list)
    for row in rows:
        strata[row["decision"]].append(row)

    total = len(rows)
    sampled = []

    # Calculate proportional allocation, rounding carefully
    alloc = {}
    remainder = {}
    allocated = 0
    for decision, group in strata.items():
        exact = n * len(group) / total
        alloc[decision] = int(exact)
        remainder[decision] = exact - int(exact)
        allocated += int(exact)

    # Distribute remaining slots to strata with largest remainders
    shortfall = n - allocated
    for decision in sorted(remainder, key=remainder.get, reverse=True)[:shortfall]:
        alloc[decision] += 1

    # Sample from each stratum
    for decision, count in alloc.items():
        group = strata[decision]
        count = min(count, len(group))  # can't sample more than available
        sampled.extend(rng.sample(group, count))

    # Shuffle final sample so decisions aren't grouped
    rng.shuffle(sampled)
    return sampled


def build_output_row(row):
    """Map input row to output row schema.

    Accepts both raw decisions.csv and enriched decisions_enriched.csv.
    - source: populated by enrich_decisions.py; blank if raw input used
    - human_decision: populated by enrich_decisions.py from Zotero bucket
      membership; blank if raw input used or item was still in Queue
    """
    return {
        "item_key":         row.get("item_key", ""),
        "source":           row.get("source", ""),
        "title":            row.get("title", ""),
        "authors":          row.get("authors", ""),
        "year":             row.get("year", ""),
        "url":              row.get("url", ""),
        "abstract":         row.get("abstract", ""),
        "claude_decision":  row.get("decision", ""),
        "claude_category":  row.get("category", ""),
        "claude_rationale": row.get("rationale", ""),
        "human_decision":   row.get("human_decision", ""),
        "chatgpt_decision": "",
        "gemini_decision":  "",
    }


def write_output(rows, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUT_COLS)
        writer.writeheader()
        for row in rows:
            writer.writerow(build_output_row(row))


def print_summary(rows, label=""):
    from collections import Counter
    counts = Counter(r.get("decision", r.get("claude_decision", "")) for r in rows)
    total = sum(counts.values())
    print(f"\n{label}Decision distribution ({total} items):")
    for d in ["keep", "maybe", "discard"]:
        n = counts.get(d, 0)
        pct = 100 * n / total if total else 0
        print(f"  {d:8s}: {n:5d}  ({pct:.1f}%)")


def main():
    parser = argparse.ArgumentParser(
        description="Build cross-model validation workbook from non-SSRN decisions.csv"
    )
    parser.add_argument("--sample", type=int, default=None,
                        help="Number of items to sample (default: all)")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for reproducibility (default: 42)")
    parser.add_argument("--input", default=INPUT_CSV,
                        help=f"Input CSV path (default: {INPUT_CSV})")
    parser.add_argument("--output", default=OUTPUT_CSV,
                        help=f"Output CSV path (default: {OUTPUT_CSV})")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"ERROR: Input file not found: {args.input}")
        print("Has the screening run completed? Check ~/slr/non-ssrn/progress.log")
        sys.exit(1)

    print(f"Reading: {args.input}")
    rows = load_decisions(args.input)
    print(f"Loaded {len(rows)} decisions")
    print_summary(rows, "Full corpus — ")

    if args.sample:
        if args.sample > len(rows):
            print(f"WARNING: Requested {args.sample} but only {len(rows)} available. Using all.")
            sampled = rows
        else:
            sampled = stratified_sample(rows, args.sample, seed=args.seed)
            print_summary(sampled, f"Sampled (n={len(sampled)}, seed={args.seed}) — ")
    else:
        sampled = rows

    write_output(sampled, args.output)
    print(f"\nOutput written: {args.output}")
    print(f"Rows: {len(sampled)}")
    print(f"\nNext steps:")
    print(f"  1. Open {args.output}")
    print(f"  2. human_decision already populated from Zotero (via enrich_decisions.py)")
    print(f"     Items still in Queue will have blank human_decision — fill those in manually")
    print(f"  3. Extract item_key, title, abstract columns → upload to ChatGPT (50 rows/batch)")
    print(f"     Use: chatgpt_validation_prompt.md")
    print(f"  4. Extract item_key, title, abstract columns → upload to Gemini (50 rows/batch)")
    print(f"     Use: gemini_validation_prompt.md")
    print(f"  5. Paste chatgpt_decision and gemini_decision columns back into this file")
    print(f"  6. Run kappa analysis")


if __name__ == "__main__":
    main()
