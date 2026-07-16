#!/usr/bin/env python3
"""Stage 4 snowball — enrich candidate references with full metadata (READ-ONLY).

Reads the co-citation table (core_cocitation.json) and pulls authors + abstract +
venue + externalIds + url from Semantic Scholar so the works can be imported as
real, screenable Zotero items. NO writes.

Output: work/stage4/core_snowball_enriched.json
"""
import json
import os
import time
import urllib.request
import urllib.error
from pathlib import Path

KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
S2 = "https://api.semanticscholar.org/graph/v1"
HERE = Path(__file__).parent
INP = HERE / "work" / "stage4" / "core_cocitation.json"
OUT = HERE / "work" / "stage4" / "core_snowball_enriched.json"
FIELDS = ("title,abstract,year,authors,venue,publicationVenue,externalIds,"
          "publicationTypes,url,openAccessPdf,journal")


def post(path, params, body):
    url = f"{S2}{path}{params}"
    headers = {"Content-Type": "application/json"}
    if KEY:
        headers["x-api-key"] = KEY
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers=headers, method="POST")
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(int(e.headers.get("Retry-After", "3")) + attempt)
                continue
            raise
        except urllib.error.URLError:
            time.sleep(2 + attempt)
    return None


def main():
    rows = json.load(open(INP))
    with_id = [r for r in rows if r.get("s2_id")]
    no_id = [r for r in rows if not r.get("s2_id")]
    print(f"{len(rows)} refs; {len(with_id)} have s2_id, {len(no_id)} do not")

    meta = {}
    for i in range(0, len(with_id), 400):
        chunk = with_id[i:i + 400]
        res = post("/paper/batch", f"?fields={FIELDS}", {"ids": [r["s2_id"] for r in chunk]})
        if res:
            for r, obj in zip(chunk, res):
                if obj:
                    meta[r["s2_id"]] = obj
        print(f"  enriched {min(i+400,len(with_id))}/{len(with_id)}")
        time.sleep(1)

    out = []
    n_abs = 0
    for r in rows:
        m = meta.get(r.get("s2_id")) or {}
        abstract = m.get("abstract") or ""
        if abstract:
            n_abs += 1
        authors = [a.get("name", "") for a in (m.get("authors") or [])]
        ext = m.get("externalIds") or {}
        oa = (m.get("openAccessPdf") or {}) or {}
        out.append({
            "ref_key": r["ref_key"],
            "s2_id": r.get("s2_id", ""),
            "title": m.get("title") or r.get("title", ""),
            "abstract": abstract,
            "authors": authors,
            "year": m.get("year") or r.get("year", ""),
            "venue": m.get("venue") or r.get("venue", ""),
            "publication_types": m.get("publicationTypes") or [],
            "doi": (ext.get("DOI") or r.get("doi", "") or "").lower(),
            "arxiv": (ext.get("ArXiv") or r.get("arxiv", "") or "").lower(),
            "url": m.get("url") or "",
            "oa_pdf": oa.get("url", ""),
            "cocite_count": r["cocite_count"],
            "citing_keys": r["citing_keys"],
            "in_corpus": r["in_corpus"],
            "has_abstract": bool(abstract),
        })
    json.dump(out, open(OUT, "w"), indent=1)
    print(f"\nWrote {len(out)} enriched -> {OUT}")
    print(f"  with abstract: {n_abs}/{len(out)}  (rest = title-only screen)")
    # coverage by band
    from collections import Counter
    for floor in [5, 3, 2]:
        band = [r for r in out if r["cocite_count"] >= floor and not r["in_corpus"]]
        wa = sum(1 for r in band if r["has_abstract"])
        print(f"  cocite>={floor} not-in-corpus: {len(band)}  ({wa} w/ abstract)")


if __name__ == "__main__":
    main()
