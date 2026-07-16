#!/usr/bin/env python3
"""Tag every item in the 04-Superceded collections with its ORIGINAL item type
AND original publication date, so both survive when the record is later converted
to the keeper's type and merged (Zotero unions tags on merge; field values of the
merged-away record are discarded).

Adds additive tags:
  orig-type:<kebab-itemType>   (e.g. journalArticle -> orig-type:journal-article)
  orig-date:<parsedDate>       (ISO where available, e.g. orig-date:2024-03)
Existing tags are preserved. Idempotent: only adds an orig-* tag that is missing.

Usage:
  python3 tag_superseded_orig_type.py --dry-run   # preview scope, no writes
  python3 tag_superseded_orig_type.py             # apply
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error

KEY = os.environ["ZOTERO_API_KEY"]
LIB = os.environ["ZOTERO_LIBRARY_ID"]
BASE = f"https://api.zotero.org/groups/{LIB}"
H = {"Zotero-API-Key": KEY, "Zotero-API-Version": "3"}
SKIP_TYPES = {"attachment", "note", "annotation"}


def kebab(s):
    return re.sub(r"(?<!^)(?=[A-Z])", "-", s).lower()


def api(method, path, body=None, headers=None):
    hs = dict(H)
    if headers:
        hs.update(headers)
    data = json.dumps(body).encode() if body is not None else None
    if data:
        hs["Content-Type"] = "application/json"
    req = urllib.request.Request(f"{BASE}{path}", data=data, headers=hs, method=method)
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req) as r:
                raw = r.read()
                return (json.loads(raw) if raw else None), dict(r.headers)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(int(e.headers.get("Retry-After", "3")) + attempt)
                continue
            raise


def get_all(path):
    out, start = [], 0
    while True:
        d, h = api("GET", f"{path}{'&' if '?' in path else '?'}limit=100&start={start}")
        out.extend(d)
        tot = int(h.get("Total-Results", len(out)))
        start += 100
        if start >= tot or not d:
            break
    return out


def superseded_collections():
    cols = get_all("/collections")
    return [c for c in cols if c["data"]["name"] == "04-Superceded"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    scols = superseded_collections()
    print(f"Found {len(scols)} '04-Superceded' collections.")

    items = {}  # key -> item object (dedupe across collections)
    for c in scols:
        for it in get_all(f"/collections/{c['key']}/items/top"):
            d = it["data"]
            if d.get("itemType") in SKIP_TYPES:
                continue
            items[it["key"]] = it
    print(f"{len(items)} unique bibliographic items across those collections.\n")

    def desired(it):
        """orig-* tags that SHOULD exist on this item (type + publication date)."""
        d = it["data"]
        out = [f"orig-type:{kebab(d['itemType'])}"]
        date = (it.get("meta", {}).get("parsedDate") or d.get("date") or "").strip()
        if date:
            out.append(f"orig-date:{date}")
        return out

    def missing(it):
        have = {t.get("tag", "") for t in it["data"].get("tags", [])}
        return [t for t in desired(it) if t not in have]

    need = [it for it in items.values() if missing(it)]
    print(f"{len(need)} items need one or more orig-* tags "
          f"({len(items)-len(need)} already complete).")
    for it in need[:14]:
        print(f"  {it['key']} [{it['data']['itemType']}] += {missing(it)}")

    if args.dry_run:
        print("\n(dry-run - no writes)")
        return

    todo = need[:args.limit] if args.limit else need
    tagged = 0
    for it in todo:
        key = it["key"]
        cur, _ = api("GET", f"/items/{key}")   # fresh version + tags (avoid clobber)
        ver = cur["version"]
        have = {t.get("tag", "") for t in cur["data"].get("tags", [])}
        add = [t for t in desired(it) if t not in have]
        if not add:
            continue
        newtags = cur["data"].get("tags", []) + [{"tag": t} for t in add]
        try:
            api("PATCH", f"/items/{key}", {"tags": newtags},
                {"If-Unmodified-Since-Version": str(ver)})
            tagged += 1
            print(f"  {key} += {add}")
        except urllib.error.HTTPError as e:
            print(f"  FAIL {key}: HTTP {e.code}")
            continue
        time.sleep(0.3)
    print(f"\nDone. Updated {tagged} items with missing orig-* tags.")


if __name__ == "__main__":
    if not KEY:
        sys.exit("ZOTERO_API_KEY not set")
    main()
