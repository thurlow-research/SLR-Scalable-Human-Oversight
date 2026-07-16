#!/usr/bin/env python3
"""Snowball items that turned out to be duplicates of already-screened corpus items
(merged during client dedupe) carry the corpus record's phase-1 votes. Rather than
re-screen them, apply their prior phase-1 decision: file each into the Citation
Snowballing 02-Screening keep/maybe/discard bucket and keep it out of 00-Queue.

Decision priority (phase 1): human vote > Claude (calibrated primary) > any other
s1 model > s2 machine > maybe.

Additive (existing collections preserved). Usage: --dry-run | (apply).
"""
import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from collections import Counter

KEY = os.environ["ZOTERO_API_KEY"]
LIB = os.environ["ZOTERO_LIBRARY_ID"]
BASE = f"https://api.zotero.org/groups/{LIB}"
H = {"Zotero-API-Key": KEY, "Zotero-API-Version": "3"}
IMPORT_COL = "ITWCXPK6"
QUEUE = "44ZQVX6R"
BUCKET = {"keep": "I8ERWQU4", "maybe": "R5P2NLSN", "discard": "QVSP4TJW"}


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


def decide(tags):
    s1 = [t for t in tags if t.startswith("s1:")]
    s2 = [t for t in tags if t.startswith("s2:")]
    for src in (["human"], ["claude"], ["gemini", "chatgpt"]):
        for t in s1:
            if any(f":{who}:" in t for who in src):
                return t.rsplit(":", 1)[1]
    if s2:
        return s2[0].rsplit(":", 1)[1]
    return "maybe"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    items = [it for it in get_all(f"/collections/{IMPORT_COL}/items/top")
             if it["data"].get("itemType") not in ("attachment", "note")]

    def tg(it):
        return [t["tag"] for t in it["data"].get("tags", [])]

    merged = [it for it in items
              if any(t.startswith(("s1:", "s2:", "s3:")) or (t.startswith("source:") and t != "source:snowball")
                     for t in tg(it))]
    plan = []
    for it in merged:
        d = decide(tg(it))
        if d not in BUCKET:
            d = "maybe"
        plan.append((it, d))
    print(f"{len(merged)} merged (duplicate) snowball items.")
    print("decision distribution:", dict(Counter(d for _, d in plan)))
    for it, d in plan:
        hv = [t for t in tg(it) if t.startswith("s1:")]
        print(f"  {it['key']} -> {d:<8} '{(it['data'].get('title','') or '')[:40]:<40}' {hv}")

    if args.dry_run:
        print("\n(dry-run - no writes)")
        return

    done = 0
    for it, d in plan:
        key = it["key"]
        cur, _ = api("GET", f"/items/{key}")
        ver = cur["version"]
        cols = [c for c in cur["data"].get("collections", []) if c != QUEUE]
        bucket = BUCKET[d]
        if bucket not in cols:
            cols.append(bucket)
        try:
            api("PATCH", f"/items/{key}", {"collections": cols},
                {"If-Unmodified-Since-Version": str(ver)})
            done += 1
        except urllib.error.HTTPError as e:
            print(f"  FAIL {key}: HTTP {e.code}")
        time.sleep(0.3)
    print(f"\nDone. Filed {done}/{len(plan)} into snowball keep/maybe/discard (removed from queue).")


if __name__ == "__main__":
    if not KEY:
        sys.exit("ZOTERO_API_KEY not set")
    main()
