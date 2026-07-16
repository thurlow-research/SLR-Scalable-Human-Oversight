#!/usr/bin/env python3
"""Stage 4 snowball — import enriched candidate refs into Zotero (WRITE).

Creates Zotero items for the not-in-corpus snowball references, filing each into
01-Import + its 03-Banding bucket, tagged source:snowball + cocite:<n>
(+ snowball:title-only when no abstract). Resumable: a ref already recorded in
the mapping file is skipped.

Usage:
  python3 stage4_snowball_import.py --limit 10   # test batch
  python3 stage4_snowball_import.py              # full run (resumes)
"""
import argparse
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
H = {"Zotero-API-Key": KEY, "Zotero-API-Version": "3"}

HERE = Path(__file__).parent
INP = HERE / "work" / "stage4" / "core_snowball_enriched.json"
MAP = HERE / "work" / "stage4" / "snowball_import_map.json"  # ref_key -> item_key

IMPORT_COL = "ITWCXPK6"           # 01-Import
BAND = {"5plus": "44FKSEL9", "3-4": "6UXZLUS6", "2": "QPJMYDIX", "1": "WDVCMBZW"}


def band_key(c):
    if c >= 5:
        return BAND["5plus"]
    if c >= 3:
        return BAND["3-4"]
    if c == 2:
        return BAND["2"]
    return BAND["1"]


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


def item_type(r):
    pts = [p.lower() for p in (r.get("publication_types") or [])]
    if r.get("arxiv") or "arxiv" in (r.get("venue", "") or "").lower():
        return "preprint"
    if any("conference" in p for p in pts):
        return "conferencePaper"
    return "journalArticle"


def creators(authors):
    out = []
    for a in authors:
        a = (a or "").strip()
        if not a:
            continue
        parts = a.split()
        if len(parts) == 1:
            out.append({"creatorType": "author", "lastName": parts[0], "firstName": ""})
        else:
            out.append({"creatorType": "author", "lastName": parts[-1],
                        "firstName": " ".join(parts[:-1])})
    return out


def build_item(r):
    it = item_type(r)
    tags = [{"tag": "source:snowball"}, {"tag": f"cocite:{r['cocite_count']}"}]
    if not r.get("has_abstract"):
        tags.append({"tag": "snowball:title-only"})
    d = {
        "itemType": it,
        "title": r.get("title", "") or "(untitled)",
        "creators": creators(r.get("authors") or []),
        "abstractNote": r.get("abstract", "") or "",
        "date": str(r.get("year") or ""),
        "url": r.get("url", "") or "",
        "tags": tags,
        "collections": [IMPORT_COL, band_key(r["cocite_count"])],
    }
    venue = r.get("venue", "") or ""
    if it == "conferencePaper":
        d["proceedingsTitle"] = venue
    elif it == "journalArticle":
        d["publicationTitle"] = venue
    else:  # preprint
        d["repository"] = venue or "arXiv"
    if r.get("doi"):
        if it in ("journalArticle", "conferencePaper", "preprint"):
            d["DOI"] = r["doi"]
    extra = [f"cocite:{r['cocite_count']}"]
    if r.get("s2_id"):
        extra.append(f"S2:{r['s2_id']}")
    if r.get("arxiv"):
        extra.append(f"arXiv:{r['arxiv']}")
    d["extra"] = "\n".join(extra)
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    rows = [r for r in json.load(open(INP)) if not r["in_corpus"]]
    done = json.load(open(MAP)) if MAP.exists() else {}
    pending = [r for r in rows if r["ref_key"] not in done]
    if args.limit:
        pending = pending[:args.limit]
    print(f"{len(rows)} not-in-corpus refs; {len(done)} already imported; "
          f"{len(pending)} this run")

    created = 0
    for i in range(0, len(pending), 50):
        chunk = pending[i:i + 50]
        body = [build_item(r) for r in chunk]
        res, _ = api("POST", "/items", body)
        succ = res.get("success", {})
        for idx, ikey in succ.items():
            done[chunk[int(idx)]["ref_key"]] = ikey
            created += 1
        if res.get("failed"):
            print("  FAILED:", json.dumps(res["failed"])[:300])
        MAP.write_text(json.dumps(done, indent=1))
        print(f"  {min(i+50,len(pending))}/{len(pending)} (created {created})")
        time.sleep(1)
    print(f"\nDone. {created} items created this run; {len(done)} total mapped -> {MAP}")


if __name__ == "__main__":
    if not KEY:
        sys.exit("ZOTERO_API_KEY not set")
    main()
