#!/usr/bin/env python3
"""Build the screening input for the non-duplicate snowball items.

Pulls items from Citation Snowballing/01-Import, EXCLUDES the 45 already-decided
duplicates (those already filed into a snowball keep/maybe/discard bucket), and
writes item_key,title,abstract,cocite,has_abstract for the screening harness.

Output: work/stage4/snowball_screen_input.csv
"""
import csv
import json
import os
import urllib.request
from pathlib import Path

KEY = os.environ["ZOTERO_API_KEY"]
LIB = os.environ["ZOTERO_LIBRARY_ID"]
BASE = f"https://api.zotero.org/groups/{LIB}"
H = {"Zotero-API-Key": KEY, "Zotero-API-Version": "3"}
IMPORT_COL = "ITWCXPK6"
BUCKETS = {"I8ERWQU4", "R5P2NLSN", "QVSP4TJW"}  # keep/maybe/discard (already decided)
OUT = Path(__file__).parent / "work" / "stage4" / "snowball_screen_input.csv"


def get_all(path):
    out, start = [], 0
    while True:
        req = urllib.request.Request(f"{BASE}{path}?limit=100&start={start}", headers=H)
        with urllib.request.urlopen(req) as r:
            d = json.load(r)
            h = dict(r.headers)
        out += d
        tot = int(h.get("Total-Results", len(out)))
        start += 100
        if start >= tot or not d:
            break
    return out


def main():
    items = [it for it in get_all(f"/collections/{IMPORT_COL}/items/top")
             if it["data"].get("itemType") not in ("attachment", "note")]
    rows, with_abs = [], 0
    for it in items:
        d = it["data"]
        if set(d.get("collections", [])) & BUCKETS:
            continue  # already decided (merged duplicate)
        cocite = next((t["tag"].split(":")[1] for t in d.get("tags", [])
                       if t["tag"].startswith("cocite:")), "")
        ab = (d.get("abstractNote") or "").strip()
        if ab:
            with_abs += 1
        rows.append({"item_key": it["key"], "title": (d.get("title") or "").strip(),
                     "abstract": ab, "cocite": cocite, "has_abstract": int(bool(ab))})
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["item_key", "title", "abstract", "cocite", "has_abstract"])
        w.writeheader()
        w.writerows(rows)
    print(f"{len(items)} in 01-Import; {len(rows)} to screen (excluded {len(items)-len(rows)} decided dups).")
    print(f"  with abstract: {with_abs}  title-only: {len(rows)-with_abs}")
    from collections import Counter
    band = Counter(">=5" if r["cocite"] and int(r["cocite"]) >= 5 else
                   "3-4" if r["cocite"] and int(r["cocite"]) >= 3 else
                   "2" if r["cocite"] == "2" else "1" for r in rows)
    print("  by cocite band:", dict(band))
    print(f"-> {OUT}")


if __name__ == "__main__":
    main()
