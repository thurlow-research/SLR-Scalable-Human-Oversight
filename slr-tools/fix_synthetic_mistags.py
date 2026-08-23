#!/usr/bin/env python3
"""One-off: fix evaluated-synthetic/method-experiment mistags found during the
05 - Synthetic-Eval Check rescan (2026-08-22), per the corrected ladder-vs-method-*
exclusivity rule (Taxonomy_Changelog.md #34).

Usage: python3 fix_synthetic_mistags.py [--commit]
"""
import json, os, sys, urllib.request

GROUP_ID = "6505702"
API_BASE = f"https://api.zotero.org/groups/{GROUP_ID}"

# key -> (tags to remove, tags to add)
FIXES = {
    "ZBF86IJM": (["cal:human:facet:evaluated-synthetic"], ["cal:human:facet:method-experiment"]),
    "CI93QRUH": (["cal:human:facet:evaluated-synthetic"], ["cal:human:facet:method-experiment"]),
    "ZH6QIU8A": (["cal:human:facet:evaluated-synthetic"], ["cal:human:facet:method-experiment"]),
    "JCTP8VXP": (["cal:human:facet:evaluated-synthetic"], []),
    "7UB2MD8Z": ([], ["cal:human:facet:method-experiment"]),
    "U9VZQXGI": ([], ["cal:human:facet:method-experiment"]),
    "A5WDGC7J": (["cal:human:facet:evaluated-synthetic"], []),
}


def get_item(api_key, key):
    req = urllib.request.Request(f"{API_BASE}/items/{key}", headers={"Zotero-API-Key": api_key, "Zotero-API-Version": "3"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def main():
    commit = "--commit" in sys.argv
    ro_key = os.environ.get("ZOTERO_API_KEY_RO") or os.environ.get("ZOTERO_API_KEY")
    rw_key = os.environ.get("ZOTERO_API_KEY_RW") or ro_key

    for key, (remove, add) in FIXES.items():
        item = get_item(ro_key, key)
        data = item["data"]
        version = data["version"]
        tags = [t["tag"] for t in data["tags"]]

        removed = [t for t in remove if t in tags]
        tags = [t for t in tags if t not in remove]
        added = [t for t in add if t not in tags]
        tags += added

        print(f"{key}: -{removed} +{added}")
        if not removed and not added:
            print("  (no change, skipped)")
            continue
        if not commit:
            continue

        body = json.dumps({"tags": [{"tag": t} for t in tags]}).encode()
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
