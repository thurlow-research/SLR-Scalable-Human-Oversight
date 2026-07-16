#!/usr/bin/env python
"""Stage 3 build step — pull the 983 eligible items from Zotero (READ-ONLY),
enrich them for relevance triage + full-text fetching, and split into batches.

Outputs (into --outdir, default ./work):
  stage3_input.csv    one row per unique item, all metadata (join key = item_key)
  batches/batch_NNN.csv   model-input slices (item_key,title,year,item_type,abstract)

Read-only: uses the Zotero read key. No writes, no tags. Safe to re-run.

Sources of the pool:
  Phase 2 Keep         3D8XR6AP  (~924)
  Phase 2 Maybe->Keep  ZB6R4G9H  (~59)
"""
import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

API = "https://api.zotero.org"
KEEP_COLLECTIONS = {"3D8XR6AP": "phase2-keep", "ZB6R4G9H": "phase2-maybe-keep"}

# Top-level source folder names we care about, matched against a collection's
# ancestor-name chain to label each item's origin stream.
SOURCE_HINTS = [
    ("IEEE", "ieee"), ("ACM", "acm"), ("SCOPUS", "scopus"), ("Scopus", "scopus"),
    ("Web of Science", "wos"), ("WoS", "wos"), ("arXiv", "arxiv"), ("arVix", "arxiv"),
    ("SSRN", "ssrn"), ("Practitioner", "practitioner"), ("Chapters", "chapters"),
    ("Hancheng Cao", "committee"), ("Linda Naimi", "committee"), ("Coursework", "coursework"),
]
# Query-prefix fallback (collection names like "Q-arXiv-06", "Q-SCO-07").
QPREFIX = {"IEX": "ieee", "ACM": "acm", "SCO": "scopus", "WoS": "wos",
           "arXiv": "arxiv", "arVix": "arxiv", "SSRN": "ssrn", "CW": "coursework"}

# Structural (non-source) collection names to skip while resolving origin —
# e.g. "a - non-SSRN Screening" must NOT match the "SSRN" source hint.
STRUCTURAL_SKIP = ("screening", "phase", "dups", "supersed", "queue",
                   "01-keep", "02-maybe", "03-discard", "04-", "import",
                   "references", "linkedin", "01-imports")

RETRIEVAL = {
    "arxiv": "arxiv-auto",            # export.arxiv.org/pdf/{id}
    "ssrn": "ssrn-manual (likely not-retrievable)",
    "ieee": "library-pull (Purdue)",
    "acm": "library-pull (Purdue)",
    "scopus": "library-pull (Purdue)",
    "wos": "library-pull (Purdue)",
    "coursework": "grey-lit (have/manual)",
    "chapters": "grey-lit (have/manual)",
    "committee": "grey-lit (have/manual)",
    "practitioner": "grey-lit (have/manual)",
}


def load_env():
    """Populate ZOTERO_* from environment, or fall back to the project .envrc."""
    if os.environ.get("ZOTERO_API_KEY") and os.environ.get("ZOTERO_LIBRARY_ID"):
        return
    envrc = Path("/Users/scott/Library/CloudStorage/OneDrive-purdue.edu/"
                 "Systemic Literature Review/.envrc")
    if envrc.exists():
        for line in envrc.read_text().splitlines():
            m = re.match(r"\s*export\s+(ZOTERO_[A-Z_]+)=(.*)", line)
            if m:
                os.environ.setdefault(m.group(1), m.group(2).strip().strip('"\''))


def api_get(path, params=None):
    lib = os.environ["ZOTERO_LIBRARY_ID"]
    ltype = os.environ.get("ZOTERO_LIBRARY_TYPE", "group")
    key = os.environ["ZOTERO_API_KEY"]
    base = f"{API}/{'groups' if ltype == 'group' else 'users'}/{lib}{path}"
    qs = "&".join(f"{k}={urllib.request.quote(str(v))}" for k, v in (params or {}).items())
    url = base + ("?" + qs if qs else "")
    req = urllib.request.Request(url, headers={"Zotero-API-Key": key,
                                               "Zotero-API-Version": "3"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode()), r.headers


def paged(path, params=None):
    params = dict(params or {})
    params.setdefault("limit", 100)
    start = 0
    while True:
        params["start"] = start
        batch, headers = api_get(path, params)
        if not batch:
            break
        yield from batch
        total = int(headers.get("Total-Results", 0))
        start += len(batch)
        if start >= total:
            break
        time.sleep(0.12)  # <= 10 req/s Zotero courtesy


def build_collection_map():
    """key -> (name, parentKey)."""
    m = {}
    for c in paged("/collections"):
        d = c["data"]
        m[c["key"]] = (d.get("name", ""), d.get("parentCollection") or None)
    return m


def resolve_sources(coll_keys, cmap):
    found = set()
    for k in coll_keys:
        # walk ancestor chain collecting names
        seen, cur = [], k
        while cur and cur in cmap and cur not in seen:
            seen.append(cur)
            name = cmap[cur][0]
            cur_parent = cmap[cur][1]
            if any(s in name.lower() for s in STRUCTURAL_SKIP):
                cur = cur_parent
                continue
            for needle, tag in SOURCE_HINTS:
                if needle.lower() in name.lower():
                    found.add(tag)
            mq = re.match(r"Q-([A-Za-z]+)-", name)
            if mq and mq.group(1) in QPREFIX:
                found.add(QPREFIX[mq.group(1)])
            cur = cmap[cur][1]
    return sorted(found)


def year_of(date):
    m = re.search(r"(19|20)\d{2}", date or "")
    return m.group(0) if m else ""


def authors_of(creators, limit=3):
    names = []
    for c in creators or []:
        if c.get("creatorType") not in (None, "author"):
            continue
        if c.get("lastName"):
            names.append(c["lastName"])
        elif c.get("name"):
            names.append(c["name"])
    if not names:
        return ""
    if len(names) > limit:
        return "; ".join(names[:limit]) + " et al."
    return "; ".join(names)


def arxiv_id_of(data):
    for field in (data.get("url", ""), data.get("archiveID", ""),
                  data.get("extra", ""), data.get("archiveLocation", "")):
        m = re.search(r"(\d{4}\.\d{4,5})", field or "")
        if m:
            return m.group(1)
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default="work")
    ap.add_argument("--batch-size", type=int, default=20)
    ap.add_argument("--limit", type=int, default=0, help="cap items (for testing)")
    args = ap.parse_args()

    load_env()
    for v in ("ZOTERO_API_KEY", "ZOTERO_LIBRARY_ID"):
        if not os.environ.get(v):
            sys.exit(f"missing {v} (export it or run from the project dir with direnv)")

    out = Path(args.outdir)
    (out / "batches").mkdir(parents=True, exist_ok=True)

    # Pattern 8: rebuilding the input invalidates any prior screening run —
    # clear stale batches, per-batch outputs, and the checkpoint so a re-screen
    # starts clean (no orphaned batch_049 from a different item set).
    stale = (list((out / "batches").glob("batch_*.csv"))
             + list(out.glob("batch_*_out.csv"))
             + ([out / "checkpoint.json"] if (out / "checkpoint.json").exists() else []))
    for f in stale:
        f.unlink()
    if stale:
        print(f"cleared {len(stale)} stale batch/output/checkpoint files", flush=True)

    print("fetching collection map...", flush=True)
    cmap = build_collection_map()

    items = {}
    for coll, label in KEEP_COLLECTIONS.items():
        print(f"fetching top items of {coll} ({label})...", flush=True)
        # attachments for has_pdf
        pdf_parents = set()
        for att in paged(f"/collections/{coll}/items",
                         {"itemType": "attachment"}):
            d = att["data"]
            if (d.get("contentType") == "application/pdf"
                    or (d.get("filename", "").lower().endswith(".pdf"))):
                if d.get("parentItem"):
                    pdf_parents.add(d["parentItem"])
        for it in paged(f"/collections/{coll}/items/top"):
            key = it["key"]
            d = it["data"]
            if key in items:
                items[key]["pool"] += f"+{label}"
                continue
            sources = resolve_sources(d.get("collections", []), cmap)
            src = ",".join(sources) if sources else "unknown"
            has_pdf = key in pdf_parents
            primary = sources[0] if sources else ""
            route = "have-pdf (skip)" if has_pdf else RETRIEVAL.get(primary, "manual")
            items[key] = {
                "item_key": key,
                "title": (d.get("title") or "").replace("\n", " ").strip(),
                "authors": authors_of(d.get("creators")),
                "year": year_of(d.get("date")),
                "item_type": d.get("itemType", ""),
                "source": src,
                "has_pdf": "yes" if has_pdf else "no",
                "doi": d.get("DOI", "") or "",
                "arxiv_id": arxiv_id_of(d),
                "retrieval_route": route,
                "pool": label,
                "abstract": (d.get("abstractNote") or "").replace("\r", " ").replace("\n", " ").strip(),
            }
            if args.limit and len(items) >= args.limit:
                break
        if args.limit and len(items) >= args.limit:
            break

    rows = list(items.values())

    # Flag content duplicates that Zotero never merged (WoS-Duplicates residue).
    # Never delete (per the always-merge-never-delete rule) — just mark, so we
    # screen the primary once and propagate its decision to the dups downstream.
    TYPE_RANK = {"journalArticle": 0, "conferencePaper": 1, "preprint": 2,
                 "report": 3, "thesis": 4, "webpage": 5}

    def norm_title(t):
        return re.sub(r"[^a-z0-9]", "", (t or "").lower())

    groups = {}
    for r in rows:
        gkey = ("doi:" + r["doi"].lower()) if r["doi"] else ("ti:" + norm_title(r["title"]))
        groups.setdefault(gkey, []).append(r)
    dup_groups = 0
    for gkey, members in groups.items():
        if len(members) == 1:
            members[0]["dup_group"], members[0]["is_primary"] = "", "yes"
            continue
        dup_groups += 1
        members.sort(key=lambda r: (r["has_pdf"] != "yes",
                                    TYPE_RANK.get(r["item_type"], 9), r["item_key"]))
        gid = members[0]["item_key"]
        for j, r in enumerate(members):
            r["dup_group"] = gid
            r["is_primary"] = "yes" if j == 0 else "no"

    cols = ["item_key", "title", "authors", "year", "item_type", "source",
            "has_pdf", "doi", "arxiv_id", "retrieval_route", "pool",
            "dup_group", "is_primary", "abstract"]
    with open(out / "stage3_input.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)

    # batch slices — only primaries. authors is carried for human reference in
    # the batch files but is deliberately NOT rendered into the screening prompt
    # (see render_batch in stage3_screen.py) to keep the relevance call author-blind.
    # Duplicates inherit the primary's decision at consolidation time.
    primaries = [r for r in rows if r["is_primary"] == "yes"]
    bcols = ["item_key", "title", "authors", "year", "item_type", "abstract"]
    for i in range(0, len(primaries), args.batch_size):
        chunk = primaries[i:i + args.batch_size]
        bnum = i // args.batch_size
        with open(out / "batches" / f"batch_{bnum:03d}.csv", "w",
                  newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=bcols, extrasaction="ignore")
            w.writeheader()
            w.writerows(chunk)

    n_batches = (len(primaries) + args.batch_size - 1) // args.batch_size
    no_abs = sum(1 for r in primaries if not r["abstract"])
    have_pdf = sum(1 for r in rows if r["has_pdf"] == "yes")
    print(f"\n{len(rows)} items ({len(primaries)} primaries + "
          f"{len(rows)-len(primaries)} dups in {dup_groups} groups) "
          f"-> {n_batches} batches of {args.batch_size} (primaries only)")
    print(f"  has_pdf: {have_pdf} ({100*have_pdf//max(len(rows),1)}%)   "
          f"missing abstract (primaries): {no_abs}")
    from collections import Counter
    print("  by source:", dict(Counter(r["source"] for r in rows)))
    print(f"  wrote {out/'stage3_input.csv'} and {out/'batches'}/")


if __name__ == "__main__":
    main()
