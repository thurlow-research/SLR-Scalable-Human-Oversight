#!/usr/bin/env python3
"""One-off: rename cal:human:facet:benchmark-evaluated -> evaluated-benchmark and
cal:human:facet:synthetic-evaluated -> evaluated-synthetic across all affected items
(group 6505702), so both sort adjacently in the tag-selector menu.

Usage: python3 rename_eval_facets.py [--commit]
"""
import json, os, sys, urllib.request

GROUP_ID = "6505702"
API_BASE = f"https://api.zotero.org/groups/{GROUP_ID}"
RENAMES = {
    "cal:human:facet:benchmark-evaluated": "cal:human:facet:evaluated-benchmark",
    "cal:human:facet:synthetic-evaluated": "cal:human:facet:evaluated-synthetic",
}

KEYS = [
    "T3XTXIXW", "7UB2MD8Z", "A5WDGC7J", "ZH6QIU8A", "CI93QRUH", "WRXR2VTP",
    "VZ27QUPQ", "MFSZPSPU", "HBR7QZ2C", "A6ZE2A26", "96XE669R", "WBS9U5N7",
]


def get_item(api_key, key):
    req = urllib.request.Request(f"{API_BASE}/items/{key}", headers={"Zotero-API-Key": api_key, "Zotero-API-Version": "3"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def main():
    commit = "--commit" in sys.argv
    ro_key = os.environ.get("ZOTERO_API_KEY_RO") or os.environ.get("ZOTERO_API_KEY")
    rw_key = os.environ.get("ZOTERO_API_KEY_RW") or ro_key

    for key in KEYS:
        item = get_item(ro_key, key)
        data = item["data"]
        version = data["version"]
        tags = [t["tag"] for t in data["tags"]]
        changed = []
        new_tags = []
        for t in tags:
            if t in RENAMES:
                new_tags.append(RENAMES[t])
                changed.append((t, RENAMES[t]))
            else:
                new_tags.append(t)
        if not changed:
            print(f"{key}: no matching tag, skipped")
            continue
        for old, new in changed:
            print(f"{key}: {old} -> {new}")
        if not commit:
            continue
        body = json.dumps({"tags": [{"tag": t} for t in new_tags]}).encode()
        req = urllib.request.Request(
            f"{API_BASE}/items/{key}", data=body, method="PATCH",
            headers={
                "Zotero-API-Key": rw_key,
                "Zotero-API-Version": "3",
                "Content-Type": "application/json",
                "If-Unmodified-Since-Version": str(version),
            },
        )
        try:
            with urllib.request.urlopen(req) as resp:
                print(f"  -> HTTP {resp.status}")
        except urllib.error.HTTPError as e:
            print(f"  -> ERROR {e.code}: {e.read()}")

    if not commit:
        print("\nDRY RUN. Pass --commit to write.")


if __name__ == "__main__":
    main()
