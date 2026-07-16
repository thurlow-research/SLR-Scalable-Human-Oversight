#!/usr/bin/env python3
"""Recover missing abstracts for title-only snowball items via OpenAlex.

OpenAlex stores abstracts as an inverted index with broad coverage (incl. arXiv
preprints). Lookup order per item: DOI -> arXiv-DOI (10.48550/arXiv.x) -> title
search. Recovered abstracts are written back to the Zotero item (abstractNote) and
the `snowball:title-only` tag removed.

Usage:
  python3 recover_abstracts.py --limit 60 --dry-run   # sample hit-rate, no writes
  python3 recover_abstracts.py --limit 60             # apply to first 60
  python3 recover_abstracts.py                        # all title-only items
"""
import argparse
import csv
import json
import os
import time
import urllib.parse
import urllib.request
import urllib.error
from pathlib import Path

KEY = os.environ["ZOTERO_API_KEY"]
LIB = os.environ["ZOTERO_LIBRARY_ID"]
ZBASE = f"https://api.zotero.org/groups/{LIB}"
ZH = {"Zotero-API-Key": KEY, "Zotero-API-Version": "3"}
OA = "https://api.openalex.org/works"
MAILTO = "scott.a.thurlow@gmail.com"
HERE = Path(__file__).parent / "work" / "stage4"


def oa_get(url):
    req = urllib.request.Request(url, headers={"User-Agent": f"mailto:{MAILTO}"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503):
                time.sleep(2 + attempt)
                continue
            return None
        except Exception:
            return None
    return None


def reconstruct(inv):
    if not inv:
        return ""
    pos = sorted((p, w) for w, ps in inv.items() for p in ps)
    return " ".join(w for _, w in pos)


def lookup(doi, arxiv, title):
    for u in filter(None, [
        f"{OA}/doi:{doi}?select=abstract_inverted_index&mailto={MAILTO}" if doi else None,
        f"{OA}/doi:10.48550/arXiv.{arxiv}?select=abstract_inverted_index&mailto={MAILTO}" if arxiv else None,
    ]):
        d = oa_get(u)
        ab = reconstruct((d or {}).get("abstract_inverted_index"))
        if ab:
            return ab
    if title:
        q = urllib.parse.quote(title[:200])
        d = oa_get(f"{OA}?filter=title.search:{q}&per-page=1"
                   f"&select=abstract_inverted_index,title&mailto={MAILTO}")
        res = (d or {}).get("results") or []
        if res:
            return reconstruct(res[0].get("abstract_inverted_index"))
    return ""


def zpatch(key, abstract):
    o = urllib.request.Request(f"{ZBASE}/items/{key}", headers=ZH)
    with urllib.request.urlopen(o) as r:
        cur = json.load(r)
    ver = cur["version"]
    tags = [t for t in cur["data"].get("tags", []) if t.get("tag") != "snowball:title-only"]
    body = json.dumps({"abstractNote": abstract, "tags": tags}).encode()
    hs = dict(ZH); hs["Content-Type"] = "application/json"; hs["If-Unmodified-Since-Version"] = str(ver)
    urllib.request.urlopen(urllib.request.Request(f"{ZBASE}/items/{key}", data=body, headers=hs, method="PATCH")).read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--cocite-min", type=int, default=0)
    args = ap.parse_args()

    # item_key -> ref_key
    imap = json.load(open(HERE / "snowball_import_map.json"))
    rev = {v: k for k, v in imap.items()}
    enr = {r["ref_key"]: r for r in json.load(open(HERE / "core_snowball_enriched.json"))}
    rows = list(csv.DictReader(open(HERE / "snowball_screen_input.csv")))
    todo = [r for r in rows if r["has_abstract"] == "0"
            and (not args.cocite_min or (r["cocite"] and int(r["cocite"]) >= args.cocite_min))]
    if args.limit:
        todo = todo[:args.limit]
    print(f"{len(todo)} title-only items to try (cocite-min={args.cocite_min})")

    hit = 0
    for i, r in enumerate(todo, 1):
        rk = rev.get(r["item_key"])
        e = enr.get(rk, {})
        ab = lookup(e.get("doi", ""), e.get("arxiv", ""), r["title"])
        if ab:
            hit += 1
            if not args.dry_run:
                try:
                    zpatch(r["item_key"], ab)
                except urllib.error.HTTPError as ex:
                    print(f"  zotero FAIL {r['item_key']}: {ex.code}")
        if i % 25 == 0:
            print(f"  {i}/{len(todo)}  recovered {hit}")
        time.sleep(0.15)
    print(f"\nRecovered abstracts for {hit}/{len(todo)} ({100*hit//max(len(todo),1)}%)"
          + ("  (dry-run)" if args.dry_run else ""))


if __name__ == "__main__":
    main()
