#!/usr/bin/env python3
"""
Generate two complementary verification samples from a decisions CSV.

Produces THREE output files:

  trust_check.csv        — Stratified sample for trust verification (unblinded).
                           Contains AI decisions, rationale, title, abstract together.
                           Used to debug: does the AI's reasoning match the abstract?

  validation_blind.csv   — Pure random sample for methodology validation (blinded).
                           Contains ONLY item_key, title, abstract, and empty
                           human_decision/human_rationale columns. AI decision is
                           withheld to avoid anchoring bias during independent coding.

  validation_key.csv     — Corresponding AI decisions for the blind sample,
                           kept separate. Used only AFTER blind coding is complete,
                           merged on item_key for kappa calculation.

Usage:
    python3 generate_verification_samples.py \\
        --input apply_all.csv \\
        --output-dir verification/ \\
        --trust-per-stratum 20 \\
        --validation-size 100 \\
        [--seed 42]

After blind coding, merge with:
    python3 -c "
    import csv
    blind = {r['item_key']: r for r in csv.DictReader(open('validation_blind.csv'))}
    key   = {r['item_key']: r for r in csv.DictReader(open('validation_key.csv'))}
    merged = []
    for k, b in blind.items():
        m = {**b, **{f'ai_{kk}':vv for kk,vv in key[k].items() if kk!='item_key'}}
        merged.append(m)
    with open('validation_merged.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(merged[0].keys()))
        w.writeheader()
        w.writerows(merged)
    "
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
ZOTERO_API_KEY = os.environ.get("ZOTERO_API_KEY", os.environ.get("ZOTERO_API_KEY_RO", ""))
LIB = os.environ.get("ZOTERO_LIBRARY_ID", "6505702")
BASE = f"https://api.zotero.org/groups/{LIB}"
RATE_LIMIT_SEC = 0.3


def zot_get(path, retries=5):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(f"{BASE}{path}")
            req.add_header("Zotero-API-Key", ZOTERO_API_KEY)
            req.add_header("Zotero-API-Version", "3")
            with urllib.request.urlopen(req, timeout=30) as r:
                return True, json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return False, None
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            return False, f"HTTP {e.code}"
        except Exception:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            return False, "fetch_error"
    return False, "max_retries"


def fetch_details(item_key):
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


def stratified_sample(rows, per_stratum, stratify_col, seed):
    random.seed(seed)
    strata = defaultdict(list)
    for r in rows:
        key = (r.get(stratify_col) or "").strip().lower() or "unknown"
        strata[key].append(r)
    out = []
    for key, items in sorted(strata.items()):
        n = min(per_stratum, len(items))
        out.extend(random.sample(items, n))
    return out, {k: len(v) for k, v in strata.items()}


def random_sample(rows, n, seed):
    random.seed(seed + 1)  # different seed namespace so trust + validation don't overlap by coincidence
    n = min(n, len(rows))
    return random.sample(rows, n)


def enrich(rows, key_col="item_key", label=""):
    """Fetch title/abstract for each row. Returns enriched rows + missing keys."""
    enriched = []
    missing = []
    for i, r in enumerate(rows, 1):
        key = (r.get(key_col) or "").strip()
        details = fetch_details(key)
        out = dict(r)
        if details:
            out.update(details)
        else:
            out.update({"title": "", "abstract": "", "year": "",
                        "authors": "", "item_type": ""})
            missing.append(key)
        enriched.append(out)
        if i % 25 == 0 or i == len(rows):
            print(f"  [{label}] {i}/{len(rows)} fetched ({len(missing)} missing)")
        time.sleep(RATE_LIMIT_SEC)
    return enriched, missing


def write_csv(path, rows, fieldnames):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", required=True,
                        help="Input CSV (e.g. apply_all.csv)")
    parser.add_argument("--output-dir", default="verification",
                        help="Output directory (default: verification/)")
    parser.add_argument("--trust-per-stratum", type=int, default=20,
                        help="Items per decision category for trust check (default: 20)")
    parser.add_argument("--validation-size", type=int, default=100,
                        help="Total items for blinded methodology sample (default: 100)")
    parser.add_argument("--stratify-col", default="decision",
                        help="Column to stratify on for trust check (default: decision)")
    parser.add_argument("--decision-col", default="decision",
                        help="AI decision column to blind out of validation (default: decision)")
    parser.add_argument("--confidence-col", default="confidence",
                        help="AI confidence column to blind out (default: confidence)")
    parser.add_argument("--rationale-col", default="rationale",
                        help="AI rationale column to blind out (default: rationale)")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed (default: 42)")
    parser.add_argument("--trust-only", action="store_true",
                        help="Only generate the trust check sample (skip validation)")
    parser.add_argument("--validation-only", action="store_true",
                        help="Only generate the validation samples (skip trust check)")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"ERROR: input not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(args.output_dir, exist_ok=True)

    # Read input
    with open(args.input, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        original_fields = list(reader.fieldnames or [])
        rows = list(reader)

    # Filter to valid keys
    rows = [r for r in rows
            if (r.get("item_key") or "").strip()
            and len((r["item_key"] or "").strip()) == 8]
    print(f"Loaded {len(rows)} rows with valid item keys from {args.input}\n")

    # ----- Trust check sample (stratified, unblinded) -----
    if not args.validation_only:
        print(f"=== TRUST CHECK SAMPLE ===")
        print(f"Stratified by '{args.stratify_col}', {args.trust_per_stratum} per stratum")
        trust_rows, strata_pop = stratified_sample(
            rows, args.trust_per_stratum, args.stratify_col, args.seed)
        print(f"Population by stratum: {strata_pop}")
        print(f"Sampled: {len(trust_rows)} items")
        print(f"Fetching title/abstract...")
        trust_enriched, trust_missing = enrich(trust_rows, label="trust")
        trust_fields = original_fields + ["title", "abstract", "year",
                                          "authors", "item_type"]
        # Dedupe field list while preserving order
        trust_fields = list(dict.fromkeys(trust_fields))
        trust_path = os.path.join(args.output_dir, "trust_check.csv")
        write_csv(trust_path, trust_enriched, trust_fields)
        print(f"Wrote {trust_path} ({len(trust_enriched)} rows, "
              f"{len(trust_missing)} missing from Zotero)\n")

    # ----- Validation sample (pure random, BLINDED) -----
    if not args.trust_only:
        print(f"=== VALIDATION SAMPLE (BLINDED) ===")
        val_rows = random_sample(rows, args.validation_size, args.seed)
        print(f"Pure random sample: {len(val_rows)} items")
        # Show distribution so user knows roughly what to expect during coding
        val_dist = defaultdict(int)
        for r in val_rows:
            val_dist[(r.get(args.decision_col) or "").strip().lower()] += 1
        print(f"  Underlying AI decision distribution (DO NOT consult during coding): "
              f"{dict(val_dist)}")
        print(f"Fetching title/abstract...")
        val_enriched, val_missing = enrich(val_rows, label="validation")

        # Split into blind + key
        blind_fields = ["item_key", "title", "abstract", "year", "authors", "item_type",
                        "human_decision", "human_confidence", "human_rationale"]
        key_fields = ["item_key", args.decision_col, args.confidence_col,
                      args.rationale_col]
        # Dedupe
        blind_fields = list(dict.fromkeys(blind_fields))
        key_fields = list(dict.fromkeys(key_fields))

        blind_rows = []
        key_rows = []
        for r in val_enriched:
            blind_rows.append({
                "item_key":         r.get("item_key", ""),
                "title":            r.get("title", ""),
                "abstract":         r.get("abstract", ""),
                "year":             r.get("year", ""),
                "authors":          r.get("authors", ""),
                "item_type":        r.get("item_type", ""),
                "human_decision":   "",
                "human_confidence": "",
                "human_rationale":  "",
            })
            key_rows.append({
                "item_key":              r.get("item_key", ""),
                args.decision_col:       r.get(args.decision_col, ""),
                args.confidence_col:     r.get(args.confidence_col, ""),
                args.rationale_col:      r.get(args.rationale_col, ""),
            })

        blind_path = os.path.join(args.output_dir, "validation_blind.csv")
        key_path   = os.path.join(args.output_dir, "validation_key.csv")
        write_csv(blind_path, blind_rows, blind_fields)
        write_csv(key_path,   key_rows,   key_fields)
        print(f"Wrote {blind_path}  ← code human_decision in this file")
        print(f"Wrote {key_path}    ← DO NOT OPEN until blind coding is complete")
        if val_missing:
            print(f"  ({len(val_missing)} items missing from Zotero)")

    print("\nDone.")


if __name__ == "__main__":
    main()
