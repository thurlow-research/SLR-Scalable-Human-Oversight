#!/usr/bin/env python3
"""Load snowball screening results into Zotero (combined disposition + phase tags).

Final decision = Phase-1 decision, except Phase-1 'maybe' -> Phase-2 decision.
Files each item into Citation Snowballing/02-Screening 01-Keep or 03-Discard
(additive), tags s1:sonnet:<p1> and, for items that went to Phase 2, s2:opus:<p2>,
and removes it from 00-Queue. Resumable via work/stage4/load_done.json.
"""
import csv
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

KEY = os.environ["ZOTERO_API_KEY"]
LIB = os.environ["ZOTERO_LIBRARY_ID"]
BASE = f"https://api.zotero.org/groups/{LIB}"
ZH = {"Zotero-API-Key": KEY, "Zotero-API-Version": "3"}
HERE = Path(__file__).parent / "work" / "stage4"
QUEUE = "44ZQVX6R"
BUCKET = {"keep": "I8ERWQU4", "maybe": "R5P2NLSN", "discard": "QVSP4TJW"}
DONE = HERE / "load_done.json"


def api(method, path, body=None, headers=None):
    hs = dict(ZH)
    if headers:
        hs.update(headers)
    data = json.dumps(body).encode() if body is not None else None
    if data:
        hs["Content-Type"] = "application/json"
    req = urllib.request.Request(f"{BASE}{path}", data=data, headers=hs, method=method)
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read()
                return (json.loads(raw) if raw else None), dict(r.headers)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503):
                time.sleep(int(e.headers.get("Retry-After", "3")) + attempt)
                continue
            raise


def main():
    p1 = {r["item_key"]: r for r in csv.DictReader(open(HERE / "snowball_screen_p1.csv"))}
    p2 = {r["item_key"]: r for r in csv.DictReader(open(HERE / "snowball_screen_p2.csv"))}
    done = set(json.load(open(DONE))) if DONE.exists() else set()

    plan = []
    for k, r in p1.items():
        if k in done:
            continue
        p1d = r["decision"]
        final = p2.get(k, {}).get("decision", "discard") if p1d == "maybe" else p1d
        tags = [f"s1:sonnet:{p1d}"]
        if k in p2:
            tags.append(f"s2:opus:{p2[k]['decision']}")
        plan.append((k, final if final in BUCKET else "discard", tags))
    print(f"{len(plan)} to load ({len(done)} already done)")

    n = 0
    for k, final, newtags in plan:
        try:
            cur, _ = api("GET", f"/items/{k}")
        except urllib.error.HTTPError as e:
            print(f"  GET FAIL {k}: {e.code}")
            continue
        ver = cur["version"]
        d = cur["data"]
        cols = [c for c in d.get("collections", []) if c != QUEUE]
        b = BUCKET[final]
        if b not in cols:
            cols.append(b)
        have = {t["tag"] for t in d.get("tags", [])}
        tags = d.get("tags", []) + [{"tag": t} for t in newtags if t not in have]
        try:
            api("PATCH", f"/items/{k}", {"collections": cols, "tags": tags},
                {"If-Unmodified-Since-Version": str(ver)})
            n += 1
            done.add(k)
        except urllib.error.HTTPError as e:
            print(f"  PATCH FAIL {k}: {e.code}")
        if n % 200 == 0:
            DONE.write_text(json.dumps(sorted(done)))
            print(f"  loaded {n}/{len(plan)}")
        time.sleep(0.12)
    DONE.write_text(json.dumps(sorted(done)))
    print(f"\nDone. Loaded {n}.")


if __name__ == "__main__":
    if not KEY:
        sys.exit("ZOTERO_API_KEY not set")
    main()
