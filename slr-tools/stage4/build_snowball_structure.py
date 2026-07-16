#!/usr/bin/env python3
"""Set up the Citation Snowballing collection structure (Zotero WRITE, structural).

Under Citation Snowballing (G7HHMK45), currently:
  01-Import (ITWCXPK6)
  02-Screening (V6C26LPJ) -> 01-Core,02-Core,03-Core,04-Core  (all empty)

Target:
  01-Import (unchanged)
  02-Screening -> 00-Queue, 01-Keep, 02-Maybe, 03-Discard, 04-Superceded
  03-Banding   -> 01-Cocite-5plus, 02-Cocite-3-4, 03-Cocite-2, 04-Cocite-1
                  (re-parent + rename the four empty *-Core collections)

Only touches empty collections; no items are moved. Idempotent-ish: skips a
create if a same-named child already exists.
"""
import json
import os
import sys
import urllib.request
import urllib.error

KEY = os.environ["ZOTERO_API_KEY"]
LIB = os.environ["ZOTERO_LIBRARY_ID"]
BASE = f"https://api.zotero.org/groups/{LIB}"
H = {"Zotero-API-Key": KEY, "Zotero-API-Version": "3"}

SNOWBALL = "G7HHMK45"
SCREENING = "V6C26LPJ"
CORE_COLS = {  # existing key -> new (name, parent placeholder 'BANDING')
    "44FKSEL9": "01-Cocite-5plus",
    "6UXZLUS6": "02-Cocite-3-4",
    "QPJMYDIX": "03-Cocite-2",
    "WDVCMBZW": "04-Cocite-1",
}
SCREEN_CHILDREN = ["00-Queue", "01-Keep", "02-Maybe", "03-Discard", "04-Superceded"]


def api(method, path, body=None, headers=None):
    hs = dict(H)
    if headers:
        hs.update(headers)
    data = json.dumps(body).encode() if body is not None else None
    if data:
        hs["Content-Type"] = "application/json"
    req = urllib.request.Request(f"{BASE}{path}", data=data, headers=hs, method=method)
    with urllib.request.urlopen(req) as r:
        raw = r.read()
        return (json.loads(raw) if raw else None), dict(r.headers)


def get_col(key):
    obj, _ = api("GET", f"/collections/{key}")
    return obj


def children_names(parent):
    out, start = {}, 0
    while True:
        d, h = api("GET", f"/collections/{parent}/collections?limit=100&start={start}")
        for c in d:
            out[c["data"]["name"]] = c["key"]
        tot = int(h.get("Total-Results", len(out)))
        start += 100
        if start >= tot or not d:
            break
    return out


def create_children(parent, names):
    existing = children_names(parent)
    todo = [n for n in names if n not in existing]
    made = {}
    if todo:
        body = [{"name": n, "parentCollection": parent} for n in todo]
        res, _ = api("POST", "/collections", body)
        succ = res.get("success", {})
        for idx, key in succ.items():
            made[todo[int(idx)]] = key
        if res.get("failed"):
            print("  FAILED creates:", res["failed"])
    for n in names:
        k = made.get(n) or existing.get(n)
        print(f"  child {n:<16} -> {k}")
    return {**existing, **made}


def rename_reparent(key, new_name, new_parent):
    obj = get_col(key)
    ver = obj["version"]
    api("PATCH", f"/collections/{key}",
        {"name": new_name, "parentCollection": new_parent},
        {"If-Unmodified-Since-Version": str(ver)})
    print(f"  {key}: -> '{new_name}' under {new_parent}")


def main():
    print("== 02-Screening dispositions ==")
    create_children(SCREENING, SCREEN_CHILDREN)

    print("== 03-Banding (create parent) ==")
    banding = create_children(SNOWBALL, ["03-Banding"])["03-Banding"]

    print("== re-parent + rename the *-Core collections into 03-Banding ==")
    for key, newname in CORE_COLS.items():
        rename_reparent(key, newname, banding)

    print("\nDone. Verifying tree ...")
    for label, parent in [("02-Screening", SCREENING), ("03-Banding", banding)]:
        print(f"  {label}:")
        for n, k in sorted(children_names(parent).items()):
            print(f"    {n:<18} {k}")
    print(f"\n03-Banding key = {banding}")


if __name__ == "__main__":
    if not KEY:
        sys.exit("ZOTERO_API_KEY not set")
    main()
