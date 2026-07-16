#!/usr/bin/env python3
"""Stage 4 — build the txt -> item_key map for the 114 Core documents.

READ-ONLY against the Zotero group API. Lists every item in the Core
collection (539H8RBQ), pairs each child text/* attachment with its parent
item, resolves the on-disk storage path (storage/<attachKey>/<filename>),
and writes a join table the extraction harness uses.

Output: work/stage4/core_txt_map.csv
  columns: item_key, attach_key, citation, year, filename, txt_path, bytes
"""
import csv
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

KEY = os.environ.get("ZOTERO_API_KEY")
LIB = os.environ.get("ZOTERO_LIBRARY_ID", "6505702")
CORE_COLL = "539H8RBQ"
BASE = f"https://api.zotero.org/groups/{LIB}"
STORAGE = Path.home() / "Zotero" / "storage"
OUT = Path(__file__).parent / "work" / "stage4" / "core_txt_map.csv"


def api_get(path, params=""):
    url = f"{BASE}/{path}{params}"
    req = urllib.request.Request(
        url, headers={"Zotero-API-Key": KEY, "Zotero-API-Version": "3"}
    )
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req) as r:
                return json.load(r), dict(r.headers)
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                wait = int(e.headers.get("Retry-After", "5"))
                time.sleep(wait)
                continue
            raise
    raise RuntimeError(f"giving up on {url}")


def get_all(path):
    """Paginate a Zotero list endpoint fully."""
    out, start = [], 0
    while True:
        data, hdr = api_get(path, f"?limit=100&start={start}")
        out.extend(data)
        total = int(hdr.get("Total-Results", len(out)))
        start += 100
        if start >= total or not data:
            break
        time.sleep(0.2)
    return out


def citation(d):
    creators = d.get("creators", []) or []
    if creators:
        c = creators[0]
        name = c.get("lastName") or c.get("name") or "?"
    else:
        name = "?"
    yr = (d.get("date", "") or "")[:4]
    # pull a 4-digit year if date is messy
    for tok in (d.get("date", "") or "").replace("-", " ").split():
        if tok.isdigit() and len(tok) == 4:
            yr = tok
            break
    return name, yr


def main():
    if not KEY:
        sys.exit("ZOTERO_API_KEY not set (source .envrc)")
    print(f"Fetching Core collection {CORE_COLL} items ...")
    items = get_all(f"collections/{CORE_COLL}/items")
    print(f"  {len(items)} raw items (parents + children)")

    parents, attachments = {}, []
    for it in items:
        d = it.get("data", {})
        itype = d.get("itemType")
        if itype == "attachment":
            attachments.append(d)
        elif itype not in ("note",):
            parents[d["key"]] = d
    print(f"  {len(parents)} parent items, {len(attachments)} attachments")

    rows = []
    seen_parents = set()
    for a in attachments:
        ctype = a.get("contentType", "")
        fname = a.get("filename", "") or ""
        parent = a.get("parentItem")
        if not parent or parent not in parents:
            continue
        if not (ctype == "text/plain" or fname.lower().endswith(".txt")):
            continue
        akey = a["key"]
        txt_path = STORAGE / akey / fname
        pdata = parents[parent]
        name, yr = citation(pdata)
        nbytes = txt_path.stat().st_size if txt_path.exists() else 0
        rows.append({
            "item_key": parent,
            "attach_key": akey,
            "citation": f"{name} {yr}".strip(),
            "year": yr,
            "title": (pdata.get("title", "") or "").replace("\n", " ").strip(),
            "filename": fname,
            "txt_path": str(txt_path),
            "exists": int(txt_path.exists()),
            "bytes": nbytes,
        })
        seen_parents.add(parent)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    cols = ["item_key", "attach_key", "citation", "year", "title",
            "filename", "txt_path", "exists", "bytes"]
    with open(OUT, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)

    missing_txt = [k for k in parents if k not in seen_parents]
    print(f"\nWrote {len(rows)} txt mappings -> {OUT}")
    print(f"Parents with a .txt attachment: {len(seen_parents)}/{len(parents)}")
    onmissing = [r for r in rows if not r["exists"]]
    if onmissing:
        print(f"WARNING: {len(onmissing)} mapped txt paths do not exist on disk:")
        for r in onmissing:
            print(f"   {r['item_key']}  {r['filename']}")
    if missing_txt:
        print(f"WARNING: {len(missing_txt)} core parents have NO .txt attachment:")
        for k in missing_txt:
            print(f"   {k}  {parents[k].get('title','')[:70]}")


if __name__ == "__main__":
    main()
