#!/usr/bin/env python3
"""Backfill thin snowball Zotero records from OpenAlex — FAST version.

Only calls OpenAlex for items that actually have a CONTENT gap (missing
authors/abstract/venue/date, or missing url with no DOI). Weak
semanticscholar.org URLs are fixed directly from the existing DOI (no network).
OpenAlex lookups for gap-items are BATCHED by DOI (OR-filter, 50/call); title-only
items with no DOI fall back to individual title search.

Only fills gaps (never overwrites good data). Recovered abstracts drop the
`snowball:title-only` tag. Resumable via work/stage4/backfill_done.json.
"""
import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from pathlib import Path

sys.path.insert(0, os.path.expanduser("~/.claude/skills/openalex/scripts"))
import openalex  # noqa: E402

KEY = os.environ["ZOTERO_API_KEY"]
LIB = os.environ["ZOTERO_LIBRARY_ID"]
BASE = f"https://api.zotero.org/groups/{LIB}"
ZH = {"Zotero-API-Key": KEY, "Zotero-API-Version": "3"}
IMPORT_COL = "ITWCXPK6"
HERE = Path(__file__).parent / "work" / "stage4"
DONE = HERE / "backfill_done.json"
VENUE_FIELD = {"journalArticle": "publicationTitle", "conferencePaper": "proceedingsTitle",
               "preprint": "repository", "bookSection": "bookTitle"}
OA = "https://api.openalex.org/works"
MAILTO = os.environ.get("OPENALEX_MAILTO", "")


def zget_all(path):
    out, start = [], 0
    while True:
        req = urllib.request.Request(f"{BASE}{path}?limit=100&start={start}", headers=ZH)
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.load(r); h = dict(r.headers)
        out += d
        tot = int(h.get("Total-Results", len(out)))
        start += 100
        if start >= tot or not d:
            break
    return out


def zpatch(key, body, ver):
    data = json.dumps(body).encode()
    hs = dict(ZH); hs["Content-Type"] = "application/json"; hs["If-Unmodified-Since-Version"] = str(ver)
    urllib.request.urlopen(urllib.request.Request(f"{BASE}/items/{key}", data=data, headers=hs, method="PATCH"), timeout=30).read()


def split_name(n):
    p = n.split()
    return ({"creatorType": "author", "lastName": p[0], "firstName": ""} if len(p) == 1
            else {"creatorType": "author", "lastName": p[-1], "firstName": " ".join(p[:-1])})


def arxiv_of(d):
    for line in (d.get("extra") or "").splitlines():
        if line.lower().startswith("arxiv:"):
            return line.split(":", 1)[1].strip()
    return ""


def oa_batch(dois):
    """Fetch many works by DOI (OR-filter); fault-tolerant. -> {doi_lower: rec}."""
    out = {}
    uniq = list(dict.fromkeys(d.lower() for d in dois if d))
    i, size = 0, 25
    while i < len(uniq):
        chunk = [c for c in uniq[i:i + size] if c and "/" in c and not c.endswith(("/", "."))]
        if not chunk:
            i += size
            continue
        filt = "|".join(chunk)   # DOIs are URL-safe for OpenAlex; DO NOT url-encode the |/:
        url = (f"{OA}?filter=doi:{filt}&per-page={size}"
               f"&select={openalex.SELECT}" + (f"&mailto={MAILTO}" if MAILTO else ""))
        d = openalex._fetch(url)
        if d is None:  # bad chunk -> resolve individually so one bad DOI can't sink it
            for one in chunk:
                rec = openalex.normalize(openalex.get_work(f"doi:{one}"))
                if rec and rec["doi"]:
                    out[rec["doi"].lower()] = rec
        else:
            for w in d.get("results", []):
                rec = openalex.normalize(w)
                if rec and rec["doi"]:
                    out[rec["doi"].lower()] = rec
        i += size
        time.sleep(0.15)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--title-search", action="store_true",
                    help="also title-search no-DOI items (slow, mostly grey-lit; default off)")
    args = ap.parse_args()
    done = set(json.load(open(DONE))) if DONE.exists() else set()

    items = [it for it in zget_all(f"/collections/{IMPORT_COL}/items/top")
             if it["data"].get("itemType") not in ("attachment", "note")]
    pending = [it for it in items if it["key"] not in done]
    if args.limit:
        pending = pending[:args.limit]
    print(f"{len(items)} items; {len(pending)} pending")

    # classify: which need OpenAlex (content gap) vs url-only-fix vs complete
    need_oa, url_only = [], []
    for it in pending:
        d = it["data"]
        vf = VENUE_FIELD.get(d["itemType"], "publicationTitle")
        gaps = (not d.get("creators") or not (d.get("abstractNote") or "").strip()
                or not d.get(vf) or not d.get("date"))
        curl = d.get("url", "") or ""
        weak_url = (not curl) or ("semanticscholar.org" in curl)
        if gaps or (weak_url and not d.get("DOI")):
            need_oa.append(it)
        elif weak_url and d.get("DOI"):
            url_only.append(it)
        else:
            done.add(it["key"])
    print(f"  complete: {len(pending)-len(need_oa)-len(url_only)}  url-only-fix: {len(url_only)}  need-openalex: {len(need_oa)}")

    # batch OpenAlex for the DOI-having gap items
    dois = [it["data"].get("DOI", "") for it in need_oa if it["data"].get("DOI")]
    dois += [f"10.48550/arxiv.{arxiv_of(it['data'])}" for it in need_oa
             if not it["data"].get("DOI") and arxiv_of(it["data"])]
    print(f"  batch-fetching {len(dois)} DOIs from OpenAlex ...")
    doimap = oa_batch(dois)

    stat = {"authors": 0, "doi": 0, "url": 0, "venue": 0, "date": 0, "abstract": 0}
    updated = nomatch = 0

    def apply(it, rec):
        d = it["data"]
        body, tags_changed = {}, []
        if not d.get("creators") and rec and rec["authors"]:
            body["creators"] = [split_name(n) for n in rec["authors"]]; stat["authors"] += 1
        doi = d.get("DOI") or (rec["doi"] if rec else "")
        if not d.get("DOI") and rec and rec["doi"]:
            body["DOI"] = rec["doi"]; doi = rec["doi"]; stat["doi"] += 1
        curl = d.get("url", "") or ""
        if (not curl or "semanticscholar.org" in curl):
            newurl = (f"https://doi.org/{doi}" if doi else (rec["url"] if rec else ""))
            if newurl:
                body["url"] = newurl; stat["url"] += 1
        vf = VENUE_FIELD.get(d["itemType"], "publicationTitle")
        if not d.get(vf) and rec and rec["venue"]:
            body[vf] = rec["venue"]; stat["venue"] += 1
        if not d.get("date") and rec and (rec["date"] or rec["year"]):
            body["date"] = rec["date"] or str(rec["year"]); stat["date"] += 1
        if not (d.get("abstractNote") or "").strip() and rec and rec["abstract"]:
            body["abstractNote"] = rec["abstract"]; stat["abstract"] += 1
            body["tags"] = [t for t in d.get("tags", []) if t.get("tag") != "snowball:title-only"]
        return body

    work = [(it, None) for it in url_only]
    for it in need_oa:
        d = it["data"]
        doi = (d.get("DOI") or "").lower()
        arx = arxiv_of(d)
        rec = doimap.get(doi) or (doimap.get(f"10.48550/arxiv.{arx}".lower()) if arx else None)
        if rec is None and not doi and not arx and args.title_search:  # optional title fallback
            rec = openalex.normalize(openalex.get_work(d.get("title", "")))
        work.append((it, rec))

    for n, (it, rec) in enumerate(work, 1):
        body = apply(it, rec)
        if body:
            try:
                zpatch(it["key"], body, it["version"]); updated += 1
            except urllib.error.HTTPError as e:
                print(f"  FAIL {it['key']}: {e.code}")
        elif rec is None and it in [w[0] for w in work if w[1] is None] and it not in url_only:
            nomatch += 1
        done.add(it["key"])
        if n % 200 == 0:
            DONE.write_text(json.dumps(sorted(done)))
            print(f"  {n}/{len(work)} updated={updated}")
    DONE.write_text(json.dumps(sorted(done)))
    print(f"\nDone. updated {updated}. fields: {stat}")


if __name__ == "__main__":
    main()
