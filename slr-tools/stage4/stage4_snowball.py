#!/usr/bin/env python3
"""Stage 4 — backward snowballing via Semantic Scholar (READ-ONLY compute).

For the 114 Core documents: resolve each to a Semantic Scholar paperId, pull its
references, and aggregate a co-citation table — how many of our cores cite each
referenced work. Frequency is a prioritization/importance signal, NOT a scope
criterion; screening + any Zotero load happen later, gated.

NO writes to Zotero. Outputs under work/stage4/:
  core_s2_resolution.csv     which cores resolved to an S2 id (and how)
  core_cocitation.csv/.json  the co-citation table (source of truth for counts)

Env: SEMANTIC_SCHOLAR_API_KEY (from .envrc). Uses the keyed batch + references
endpoints (off the unauthenticated ~1 rps pool).
"""
import csv
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path
from collections import defaultdict

KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
S2 = "https://api.semanticscholar.org/graph/v1"
HERE = Path(__file__).parent
STAGE3 = HERE.parent / "stage3" / "work"
IMPORT_PLAN = STAGE3 / "stage3_import_plan.csv"
RESULTS = STAGE3 / "stage3_results.csv"
OUTDIR = HERE / "work" / "stage4"


def norm_title(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def req(method, path, params="", body=None):
    url = f"{S2}{path}{params}"
    data = json.dumps(body).encode() if body is not None else None
    headers = {"Content-Type": "application/json"}
    if KEY:
        headers["x-api-key"] = KEY
    r = urllib.request.Request(url, data=data, headers=headers, method=method)
    for attempt in range(6):
        try:
            with urllib.request.urlopen(r) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                wait = int(e.headers.get("Retry-After", "3")) + attempt
                time.sleep(wait)
                continue
            if e.code == 404:
                return None
            raise
        except urllib.error.URLError:
            time.sleep(2 + attempt)
    return None


def load_cores():
    core_keys = {r["item_key"] for r in csv.DictReader(open(IMPORT_PLAN))
                 if r["final"] == "core"}
    meta = {}
    for r in csv.DictReader(open(RESULTS)):
        if r["item_key"] in core_keys:
            meta[r["item_key"]] = r
    return meta


def build_corpus_index():
    """Sets to test whether a referenced work is already in our 983-item pool."""
    dois, arxivs, titles = set(), set(), set()
    for r in csv.DictReader(open(RESULTS)):
        if (r.get("doi") or "").strip():
            dois.add(r["doi"].strip().lower())
        if (r.get("arxiv_id") or "").strip():
            arxivs.add(r["arxiv_id"].strip().lower().replace("arxiv:", ""))
        if (r.get("title") or "").strip():
            titles.add(norm_title(r["title"]))
    return dois, arxivs, titles


def resolve(meta):
    """Resolve each core to an S2 paperId via DOI/ARXIV batch, then title search."""
    ids_in, keys_order = [], []
    for k, r in meta.items():
        doi = (r.get("doi") or "").strip()
        arx = (r.get("arxiv_id") or "").strip().replace("arXiv:", "").replace("arxiv:", "")
        if doi:
            ids_in.append(f"DOI:{doi}")
        elif arx:
            ids_in.append(f"ARXIV:{arx}")
        else:
            ids_in.append(None)
        keys_order.append(k)

    resolved = {}  # item_key -> {paperId, how, title}
    # batch resolve the non-null DOI/ARXIV ids
    batch_ids = [i for i in ids_in if i]
    got = {}
    for i in range(0, len(batch_ids), 400):
        chunk = batch_ids[i:i + 400]
        res = req("POST", "/paper/batch",
                  "?fields=paperId,title,year,externalIds", {"ids": chunk})
        if res:
            for inp, obj in zip(chunk, res):
                if obj and obj.get("paperId"):
                    got[inp] = obj
        time.sleep(1)
    for k, idin in zip(keys_order, ids_in):
        if idin and idin in got:
            resolved[k] = {"paperId": got[idin]["paperId"],
                           "how": idin.split(":")[0], "title": got[idin].get("title", "")}

    # title-search fallback for the unresolved
    for k in meta:
        if k in resolved:
            continue
        title = (meta[k].get("title") or "").strip()
        if not title:
            continue
        res = req("GET", "/paper/search",
                  f"?query={urllib.parse.quote(title[:250])}&limit=1"
                  "&fields=paperId,title,year,externalIds")
        time.sleep(1.1)
        data = (res or {}).get("data") or []
        if data and data[0].get("paperId"):
            # guard: require decent title overlap
            if norm_title(data[0].get("title", ""))[:30] and \
               norm_title(title)[:20] in norm_title(data[0].get("title", "")):
                resolved[k] = {"paperId": data[0]["paperId"], "how": "title",
                               "title": data[0].get("title", "")}
            else:
                resolved[k] = {"paperId": data[0]["paperId"], "how": "title-weak",
                               "title": data[0].get("title", "")}
    return resolved


def fetch_refs(paper_id):
    out, offset = [], 0
    while True:
        res = req("GET", f"/paper/{paper_id}/references",
                  f"?fields=paperId,title,year,externalIds,venue,citationCount"
                  f"&limit=1000&offset={offset}")
        if not res:
            break
        data = res.get("data") or []
        out.extend(cp.get("citedPaper") for cp in data if cp.get("citedPaper"))
        if len(data) < 1000 or res.get("next") is None:
            break
        offset += 1000
        time.sleep(0.5)
    return out


def main():
    if not KEY:
        print("WARNING: SEMANTIC_SCHOLAR_API_KEY not set — running on the "
              "unauthenticated pool (slow/rate-limited).", file=sys.stderr)
    OUTDIR.mkdir(parents=True, exist_ok=True)
    meta = load_cores()
    print(f"Cores: {len(meta)}")
    dois, arxivs, titles = build_corpus_index()

    print("Resolving cores to S2 ids ...")
    resolved = resolve(meta)
    hows = defaultdict(int)
    for v in resolved.values():
        hows[v["how"]] += 1
    print(f"  resolved {len(resolved)}/{len(meta)}: {dict(hows)}")
    with open(OUTDIR / "core_s2_resolution.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["item_key", "paperId", "how", "s2_title", "our_title"])
        for k, r in meta.items():
            rv = resolved.get(k)
            w.writerow([k, rv["paperId"] if rv else "", rv["how"] if rv else "UNRESOLVED",
                        rv["title"] if rv else "", (r.get("title") or "")[:120]])

    print("Fetching references + aggregating co-citations ...")
    agg = {}  # ref_key -> record
    for n, (k, rv) in enumerate(resolved.items(), 1):
        refs = fetch_refs(rv["paperId"])
        for cp in refs:
            ext = cp.get("externalIds") or {}
            doi = (ext.get("DOI") or "").lower()
            arx = (ext.get("ArXiv") or "").lower()
            pid = cp.get("paperId") or ""
            ref_key = pid or doi or norm_title(cp.get("title"))
            if not ref_key:
                continue
            rec = agg.get(ref_key)
            if not rec:
                in_corpus = bool((doi and doi in dois) or (arx and arx in arxivs)
                                 or norm_title(cp.get("title")) in titles)
                rec = {"ref_key": ref_key, "s2_id": pid, "doi": doi, "arxiv": arx,
                       "title": (cp.get("title") or "").replace("\n", " "),
                       "year": cp.get("year") or "", "venue": cp.get("venue") or "",
                       "global_citations": cp.get("citationCount") or 0,
                       "cocite_count": 0, "citing_keys": [], "in_corpus": in_corpus}
                agg[ref_key] = rec
            rec["cocite_count"] += 1
            rec["citing_keys"].append(k)
        time.sleep(0.6)
        if n % 20 == 0:
            print(f"  {n}/{len(resolved)} cores processed, {len(agg)} unique refs so far")

    rows = sorted(agg.values(), key=lambda r: -r["cocite_count"])
    with open(OUTDIR / "core_cocitation.json", "w") as fh:
        json.dump(rows, fh, indent=1)
    with open(OUTDIR / "core_cocitation.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["cocite_count", "in_corpus", "title", "year", "venue",
                    "global_citations", "doi", "arxiv", "s2_id", "citing_keys"])
        for r in rows:
            w.writerow([r["cocite_count"], int(r["in_corpus"]), r["title"], r["year"],
                        r["venue"], r["global_citations"], r["doi"], r["arxiv"],
                        r["s2_id"], "|".join(r["citing_keys"])])

    # distribution
    from collections import Counter
    dist = Counter(r["cocite_count"] for r in rows)
    notincorpus = [r for r in rows if not r["in_corpus"]]
    print(f"\nUnique referenced works: {len(rows)}")
    print(f"Not already in our corpus: {len(notincorpus)}")
    print("co-citation distribution (count : #refs / #refs-not-in-corpus):")
    for c in sorted(dist, reverse=True):
        nic = sum(1 for r in rows if r["cocite_count"] == c and not r["in_corpus"])
        if c >= 2 or dist[c] < 30:
            print(f"  cited by {c:2d} cores : {dist[c]:5d} refs  ({nic} not-in-corpus)")
    print(f"\nOutputs -> {OUTDIR}/core_cocitation.csv (+ .json), core_s2_resolution.csv")


if __name__ == "__main__":
    import urllib.parse  # noqa: E402
    main()
