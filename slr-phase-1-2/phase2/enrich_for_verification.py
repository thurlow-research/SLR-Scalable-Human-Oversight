#!/usr/bin/env python3
"""
Enrich a decisions CSV with title and abstract from Zotero for verification sampling.

Reads any CSV with an item_key column (apply_all.csv, human_review.csv, etc.),
optionally samples a subset, fetches each item's title and abstract from Zotero,
and writes an enriched CSV ready for manual review.

Usage:
    # Full sample (100% — typical for human_review.csv)
    python3 enrich_for_verification.py \\
        --input human_review.csv --output human_review_enriched.csv

    # Stratified 5% sample of apply_all.csv (by decision column)
    python3 enrich_for_verification.py \\
        --input apply_all.csv --output sample_5pct.csv \\
        --sample-rate 0.05 --stratify decision

    # Fixed-N sample per stratum
    python3 enrich_for_verification.py \\
        --input apply_all.csv --output sample.csv \\
        --per-stratum 10 --stratify decision --seed 42

    # Random sample without stratification
    python3 enrich_for_verification.py \\
        --input apply_all.csv --output sample.csv --sample-rate 0.01

Notes:
- Uses read-only Zotero API key. No writes happen, ever.
- Sampling is deterministic when --seed is set; default seed is 42.
- Original columns are preserved; title, abstract, year, authors, item_type
  are appended.
"""
import argparse
import csv
import json
import os
import random
import sys
import time
import urllib.request
import urllib.error
from collections import defaultdict

# ============================================================
# CONFIG
# ============================================================
ZOTERO_API_KEY_RO = os.environ.get(
    "ZOTERO_API_KEY",
    os.environ.get("ZOTERO_API_KEY_RO", "")  # read-only fallback
)
LIB = os.environ.get("ZOTERO_LIBRARY_ID", "6505702")
BASE = f"https://api.zotero.org/groups/{LIB}"
RATE_LIMIT_SEC = 0.3

ENRICHED_FIELDS = ["title", "abstract", "year", "authors", "item_type"]


# ============================================================
# ZOTERO API
# ============================================================
def zot_get(path, retries=5):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(f"{BASE}{path}")
            req.add_header("Zotero-API-Key", ZOTERO_API_KEY_RO)
            req.add_header("Zotero-API-Version", "3")
            with urllib.request.urlopen(req, timeout=30) as r:
                return True, json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return False, None  # item missing — not retryable
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            return False, f"HTTP {e.code}"
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            return False, str(e)
    return False, "max retries"


def fetch_item_details(item_key):
    """Return dict with title, abstract, year, authors, item_type, or None on failure."""
    ok, data = zot_get(f"/items/{item_key}")
    if not ok or not data:
        return None
    d = data.get("data", {})
    authors = []
    for c in d.get("creators", [])[:5]:
        last = c.get("lastName") or c.get("name") or ""
        if last:
            authors.append(last)
    return {
        "title":     (d.get("title") or "").strip(),
        "abstract":  (d.get("abstractNote") or "").strip(),
        "year":      (d.get("date") or "")[:4],
        "authors":   "; ".join(authors),
        "item_type": d.get("itemType") or "",
    }


# ============================================================
# SAMPLING
# ============================================================
def sample_rows(rows, sample_rate, per_stratum, stratify_col, seed):
    """
    Sample rows. Modes:
      - per_stratum N + stratify_col → N per stratum (random within each)
      - sample_rate R + stratify_col → ceil(R * len(stratum)) per stratum
      - sample_rate R, no stratify   → R fraction across whole set
      - sample_rate 1.0              → all rows
    """
    if sample_rate >= 1.0 and not per_stratum:
        return list(rows)

    random.seed(seed)

    # Stratified sampling
    if stratify_col:
        strata = defaultdict(list)
        for r in rows:
            key = (r.get(stratify_col) or "").strip().lower() or "unknown"
            strata[key].append(r)
        sampled = []
        for key, items in sorted(strata.items()):
            if per_stratum:
                n = min(per_stratum, len(items))
            else:
                n = max(1, int(round(sample_rate * len(items))))
                n = min(n, len(items))
            sampled.extend(random.sample(items, n))
        return sampled

    # Random sample, no stratification
    n = max(1, int(round(sample_rate * len(rows))))
    n = min(n, len(rows))
    return random.sample(list(rows), n)


# ============================================================
# MAIN
# ============================================================
def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--input",  required=True, help="Input CSV with item_key column")
    parser.add_argument("--output", required=True, help="Output CSV path")
    parser.add_argument("--sample-rate", type=float, default=1.0,
                        help="Fraction of rows to sample (0.0-1.0). Default: 1.0 (all)")
    parser.add_argument("--per-stratum", type=int, default=None,
                        help="Fixed N per stratum. Overrides --sample-rate if set. "
                             "Requires --stratify.")
    parser.add_argument("--stratify", default=None,
                        help="Column name to stratify on (e.g. 'decision'). "
                             "When set, sampling preserves the column distribution.")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for reproducibility (default: 42)")
    parser.add_argument("--key-column", default="item_key",
                        help="Name of the item_key column (default: item_key)")
    args = parser.parse_args()

    if args.per_stratum and not args.stratify:
        print("ERROR: --per-stratum requires --stratify", file=sys.stderr)
        sys.exit(2)
    if not (0.0 < args.sample_rate <= 1.0):
        print("ERROR: --sample-rate must be in (0.0, 1.0]", file=sys.stderr)
        sys.exit(2)

    # Read input
    if not os.path.exists(args.input):
        print(f"ERROR: input not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    with open(args.input, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        original_fields = list(reader.fieldnames or [])
        rows = list(reader)

    if args.key_column not in original_fields:
        print(f"ERROR: column '{args.key_column}' not found. "
              f"Available: {original_fields}", file=sys.stderr)
        sys.exit(1)

    # Filter to rows with valid 8-char keys
    rows = [r for r in rows
            if (r.get(args.key_column) or "").strip()
            and len((r[args.key_column] or "").strip()) == 8]
    print(f"Loaded {len(rows)} rows with valid item keys from {args.input}")

    # Sample
    if args.stratify and args.stratify not in original_fields:
        print(f"WARNING: stratify column '{args.stratify}' not in input — "
              f"falling back to random sampling", file=sys.stderr)
        args.stratify = None

    sampled = sample_rows(rows, args.sample_rate, args.per_stratum,
                          args.stratify, args.seed)
    print(f"Sampled {len(sampled)} rows "
          f"(rate={args.sample_rate}, "
          f"per_stratum={args.per_stratum}, "
          f"stratify={args.stratify}, "
          f"seed={args.seed})")

    if args.stratify:
        counts = defaultdict(int)
        for r in sampled:
            counts[(r.get(args.stratify) or "").strip().lower()] += 1
        print(f"  Stratum distribution: {dict(counts)}")

    # Enrich
    print(f"\nFetching item details from Zotero...")
    out_fields = original_fields[:]
    for ef in ENRICHED_FIELDS:
        if ef not in out_fields:
            out_fields.append(ef)

    enriched = []
    missing = []
    for i, row in enumerate(sampled, 1):
        key = row[args.key_column].strip()
        details = fetch_item_details(key)
        out_row = dict(row)
        if details:
            out_row.update(details)
        else:
            for ef in ENRICHED_FIELDS:
                out_row.setdefault(ef, "")
            missing.append(key)
        enriched.append(out_row)
        if i % 25 == 0 or i == len(sampled):
            print(f"  {i}/{len(sampled)} fetched ({len(missing)} missing)")
        time.sleep(RATE_LIMIT_SEC)

    # Write output
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_fields)
        w.writeheader()
        w.writerows(enriched)

    print(f"\nWrote {len(enriched)} enriched rows → {args.output}")
    if missing:
        print(f"WARNING: {len(missing)} items not found in Zotero:")
        for k in missing[:10]:
            print(f"  {k}")
        if len(missing) > 10:
            print(f"  ... and {len(missing) - 10} more")


if __name__ == "__main__":
    main()
