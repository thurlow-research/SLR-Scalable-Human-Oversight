#!/usr/bin/env python3
import os
"""
Post-process non_ssrn_llm_screen.py decisions.csv.

Adds two columns by looking up each item_key in Zotero:
  source          — which database the item came from (ieee, scopus, acm, arxiv, wos)
  human_decision  — the human screening decision already in Zotero
                    (keep / maybe / discard / blank if still in Queue)

All screening done prior to the AI run was human, so existing bucket
membership (01-Keep, 02-Maybe, 03-Discard) is treated as human_decision.
Items still in 00-Queue have no prior human decision → blank.

Usage:
    cd ~/slr/non-ssrn
    python3 enrich_decisions.py

    # Custom paths:
    python3 enrich_decisions.py --input decisions.csv --output decisions_enriched.csv

Output:
    decisions_enriched.csv  — original columns + source + human_decision

Then run build_validation_sheet.py against the enriched file:
    python3 build_validation_sheet.py --input decisions_enriched.csv --sample 500
"""

import csv, json, os, sys, time, random, argparse, urllib.request, urllib.error
from collections import defaultdict

# ── Config ────────────────────────────────────────────────────────────────────
ZOTERO_API_KEY = os.environ.get("ZOTERO_API_KEY_RO", "")   # read-only
LIB            = "6505702"
BASE           = f"https://api.zotero.org/groups/{LIB}"

WORKDIR    = os.path.expanduser("~/slr/non-ssrn")
INPUT_CSV  = os.path.join(WORKDIR, "decisions.csv")
OUTPUT_CSV = os.path.join(WORKDIR, "decisions_enriched.csv")

ZOTERO_RATE_LIMIT_SEC = 0.3
BATCH_SIZE = 50   # items per Zotero API call (/items?itemKey=A,B,C,...)

# ── Source parent keys → short name ──────────────────────────────────────────
# Only the five non-SSRN sources that non_ssrn_llm_screen.py covers.
SOURCE_PARENTS = {
    "7XHWH8NM": "ieee",
    "2RWBC7QH": "scopus",
    "G4IIYGV6": "acm",
    "YK2CHQLN": "arxiv",
    "E7AS4HD4": "wos",
}

# Bucket name prefix → human_decision value
# 00-Queue → blank (no human decision yet)
BUCKET_MAP = {
    "01-": "keep",
    "02-": "maybe",
    "03-": "discard",
    "04-": None,   # superseded — treat as blank (edge case)
}

# ── Zotero API ────────────────────────────────────────────────────────────────
def zot_get(path, retries=5):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(f"{BASE}{path}")
            req.add_header("Zotero-API-Key", ZOTERO_API_KEY)
            req.add_header("Zotero-API-Version", "3")
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                wait = 2 ** attempt + random.uniform(0, 1)
                print(f"  Zotero HTTP {e.code}, retry in {wait:.1f}s", flush=True)
                time.sleep(wait)
                continue
            raise
        except Exception:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise
    return None


def build_collection_map():
    """
    Fetch all collections in the library and build two lookup dicts:
      col_to_source:  collection_key → source short name (ieee/scopus/etc.)
                      for any collection that is a descendant of a source parent
      col_to_bucket:  collection_key → human_decision (keep/maybe/discard/None)
                      for 01-Keep, 02-Maybe, 03-Discard, 04-Superseded collections
    """
    print("Fetching collection tree from Zotero...", flush=True)
    all_cols = []
    start = 0
    while True:
        batch = zot_get(f"/collections?limit=100&start={start}")
        if not batch:
            break
        all_cols.extend(batch)
        if len(batch) < 100:
            break
        start += 100
        time.sleep(ZOTERO_RATE_LIMIT_SEC)

    print(f"  Loaded {len(all_cols)} collections", flush=True)

    # Build parent → children map
    children_of = defaultdict(list)
    col_data = {}
    for c in all_cols:
        d = c.get("data", {})
        key = d.get("key", c.get("key"))
        name = d.get("name", "")
        parent = d.get("parentCollection") or None
        col_data[key] = {"name": name, "parent": parent}
        if parent:
            children_of[parent].append(key)

    # Walk descendants of each source parent to build col_to_source
    col_to_source = {}
    col_to_bucket = {}

    def walk(key, source_name):
        col_to_source[key] = source_name
        name = col_data.get(key, {}).get("name", "")
        # Determine bucket
        for prefix, decision in BUCKET_MAP.items():
            if name.startswith(prefix):
                col_to_bucket[key] = decision
                break
        for child in children_of.get(key, []):
            walk(child, source_name)

    for parent_key, source_name in SOURCE_PARENTS.items():
        if parent_key in col_data:
            walk(parent_key, source_name)
        else:
            print(f"  WARNING: source parent {parent_key} ({source_name}) not found in library",
                  flush=True)

    return col_to_source, col_to_bucket


def fetch_item_collections_batch(item_keys):
    """
    Fetch collection memberships for a batch of item keys.
    Uses /items?itemKey=A,B,C&include=data endpoint.
    Returns dict: item_key → list of collection keys.
    """
    key_str = ",".join(item_keys)
    data = zot_get(f"/items?itemKey={key_str}&limit=100&include=data")
    if not data:
        return {}
    result = {}
    for item in data:
        k = item.get("key", "")
        cols = item.get("data", {}).get("collections", [])
        result[k] = cols
    return result


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Enrich non-SSRN decisions.csv with source and human_decision from Zotero."
    )
    parser.add_argument("--input",  default=INPUT_CSV,  help=f"Input CSV (default: {INPUT_CSV})")
    parser.add_argument("--output", default=OUTPUT_CSV, help=f"Output CSV (default: {OUTPUT_CSV})")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"ERROR: Input not found: {args.input}")
        print("Has the screening run completed? Check ~/slr/non-ssrn/progress.log")
        sys.exit(1)

    # Load decisions
    print(f"Reading {args.input}...", flush=True)
    rows = []
    with open(args.input, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)
    print(f"  {len(rows)} decisions loaded", flush=True)

    # Build collection maps
    col_to_source, col_to_bucket = build_collection_map()

    # Batch-fetch collection memberships for all item keys
    print(f"\nFetching collection memberships ({len(rows)} items, "
          f"~{len(rows)//BATCH_SIZE + 1} API calls)...", flush=True)

    item_cols = {}   # item_key → list of collection keys
    keys = [r["item_key"] for r in rows]
    for i in range(0, len(keys), BATCH_SIZE):
        batch = keys[i:i + BATCH_SIZE]
        result = fetch_item_collections_batch(batch)
        item_cols.update(result)
        done = min(i + BATCH_SIZE, len(keys))
        print(f"  {done}/{len(keys)} items fetched", end="\r", flush=True)
        time.sleep(ZOTERO_RATE_LIMIT_SEC)
    print(f"  {len(keys)}/{len(keys)} items fetched", flush=True)

    # Resolve source and human_decision for each row
    source_counts  = defaultdict(int)
    bucket_counts  = defaultdict(int)
    missing_counts = 0

    for row in rows:
        k = row["item_key"]
        cols = item_cols.get(k, [])

        if not cols:
            missing_counts += 1
            row["source"]         = ""
            row["human_decision"] = ""
            continue

        # Source: first collection that maps to a known source
        source = ""
        for col_key in cols:
            if col_key in col_to_source:
                source = col_to_source[col_key]
                break
        row["source"] = source
        source_counts[source or "(unknown)"] += 1

        # Human decision: highest-priority bucket across all collections
        # Priority: keep > maybe > discard > superseded > blank
        priority = {"keep": 3, "maybe": 2, "discard": 1, None: 0}
        best = None
        for col_key in cols:
            if col_key in col_to_bucket:
                candidate = col_to_bucket[col_key]
                if priority.get(candidate, 0) > priority.get(best, 0):
                    best = candidate
        row["human_decision"] = best if best else ""
        bucket_counts[best if best else "(queue/blank)"] += 1

    # Write enriched CSV
    out_fieldnames = list(fieldnames) + ["source", "human_decision"]
    # Avoid duplicate columns if re-running
    seen = set()
    deduped = []
    for f in out_fieldnames:
        if f not in seen:
            deduped.append(f)
            seen.add(f)
    out_fieldnames = deduped

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=out_fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    # Summary
    print(f"\nOutput written: {args.output}")
    print(f"\nSource breakdown:")
    for src, count in sorted(source_counts.items()):
        print(f"  {src:12s}: {count}")
    if missing_counts:
        print(f"  (no collection): {missing_counts}")

    print(f"\nHuman decision breakdown:")
    for bucket, count in sorted(bucket_counts.items()):
        print(f"  {str(bucket):12s}: {count}")

    print(f"\nNext step:")
    print(f"  python3 build_validation_sheet.py --input {args.output} --sample 500")


if __name__ == "__main__":
    main()
