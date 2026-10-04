#!/usr/bin/env python3
"""Compute the PRISMA screening funnel from a read-only snapshot of the Zotero library.

Every count in Methodology/PRISMA_Funnel.md comes from this script. It replaces the
hand-carried snapshot figures (9,518 / 983 / 149 / 148 / 147) that drifted as dedupes landed.

Rules applied (Methodology/SLR_Methodology_Bootstrap.md §3; Selection_Criteria_By_Phase.md):
  * Phases 1-3 made SINGLE-valued calls -> the decision of record is collection membership.
  * Phase 4+ decisions are TAGS: tier = `demote:context` if present, else the Phase-3 call.
  * A record is one study. A record is a removed duplicate only if its `superseded-by:<key>`
    names a DIFFERENT key that still exists. Client-side Zotero merges union tags, so a merge
    survivor can carry `superseded-by:` pointing at itself or at a key the merge deleted
    (24 self + 20 dangling of 56 at snapshot 169153); counting the bare tag over-removes.
  * A record filed in both Final/Core and Final/Context (merged query+snowball records) counts
    as Core: it entered full-text reading, which is where its tier was finally decided.
  * Stream: a record in any query/other-methods import belongs to the QUERY stream (the query
    record is master); the snowball stream is snowball-only records. A record is scored only
    against its own stream's buckets.

Usage:
    python3 slr-tools/prisma_funnel.py --dump  /path/lib.json   # fetch snapshot (RO key)
    python3 slr-tools/prisma_funnel.py --snapshot /path/lib.json [--json out.json]
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import sys
import urllib.request

API = "https://api.zotero.org"

SLR_ROOT = "AEQEL2RI"          # System LIterature Review
PHASE1 = "CJQBAJ4V"
QUERY_SOURCES = ["ACM", "IEEE Xplore", "SCOPUS", "SSRN", "Web of Science", "arXiv"]
OTHER_SOURCES = ["Coursework", "Practitioner Network", "Committee Recommendations"]
SNOWBALL = "Citation Snowballing"

# Phase 2 / 01-Queries: <Phase-1 bucket> / <Phase-2 bucket>
P2_QUERY = {
    ("keep", "keep"): "3D8XR6AP", ("keep", "maybe"): "5VHKIH5W", ("keep", "discard"): "9A2LGHUT",
    ("maybe", "keep"): "ZB6R4G9H", ("maybe", "maybe"): "LR6EXWQB", ("maybe", "discard"): "TA8JUISM",
}
P3_QUERY = {"core": "539H8RBQ", "context": "85JVIR9X", "discard": "JIMGLVAL"}
P3_SNOW = {"core": "UPTNJTIS", "context": "WX9WW6A7", "discard": "3GZZNLAR"}   # subtrees
FINAL = {"core": "3S9B658S", "context": "QE8TWEJQ", "discard": "72SVYQMU"}
PHASE6 = "R9ZHDXMN"
BUCKET = {"00": "queue", "01": "keep", "02": "maybe", "03": "discard", "04": "superseded"}


def dump(path: str) -> None:
    gid, key = os.environ["ZOTERO_LIBRARY_ID"], os.environ["ZOTERO_API_KEY_RO"]

    def get(p):
        out, start = [], 0
        while True:
            sep = "&" if "?" in p else "?"
            req = urllib.request.Request(
                f"{API}/groups/{gid}/{p}{sep}limit=100&start={start}",
                headers={"Zotero-API-Key": key, "Zotero-API-Version": "3"})
            with urllib.request.urlopen(req) as r:
                total = int(r.headers["Total-Results"])
                ver = r.headers.get("Last-Modified-Version")
                out += json.load(r)
            start += 100
            if start >= total:
                return out, total, ver

    cols, ct, _ = get("collections")
    items, it, ver = get("items/top")
    assert len(cols) == ct and len(items) == it, "pagination mismatch vs Total-Results"
    json.dump({"version": ver, "collections": [c["data"] for c in cols],
               "items": [i["data"] for i in items]}, open(path, "w"))
    print(f"snapshot v{ver}: {ct} collections, {it} top-level items -> {path}")


class Lib:
    def __init__(self, snap):
        self.version = snap["version"]
        self.cols = {c["key"]: c for c in snap["collections"]}
        self.items = {i["key"]: i for i in snap["items"] if i["itemType"] not in ("note", "attachment")}
        self.kids = collections.defaultdict(list)
        for c in self.cols.values():
            if c["parentCollection"]:
                self.kids[c["parentCollection"]].append(c["key"])
        self.by_col = collections.defaultdict(set)
        for k, it in self.items.items():
            for c in it["collections"]:
                self.by_col[c].add(k)

    def sub(self, k):
        out = {k}
        for ch in self.kids[k]:
            out |= self.sub(ch)
        return out

    def members(self, root, deep=True):
        return set().union(*(self.by_col[c] for c in (self.sub(root) if deep else {root})))

    def tags(self, k):
        return {t["tag"] for t in self.items[k]["tags"]}

    def source(self, name):
        return next(k for k in self.kids[PHASE1] if self.cols[k]["name"] == name)

    def imports(self, src):
        roots = [c for c in self.sub(src) if self.cols[c]["name"].startswith("01-Import")]
        return set().union(set(), *(self.members(r) for r in roots))

    def buckets(self, src):
        out = collections.defaultdict(set)
        for c in self.sub(src):
            p = self.cols[c]["parentCollection"]
            if p and self.cols[p]["name"].startswith("02-Screening"):
                out[BUCKET[self.cols[c]["name"][:2]]] |= self.members(c)
        return out


def superseded(lib):
    out = set()
    for k in lib.items:
        for t in lib.tags(k):
            if t.startswith("superseded-by:"):
                tgt = t.split(":", 1)[1]
                if tgt != k and tgt in lib.items:
                    out.add(k)
    return out


def p1_decision(lib, k, bk):
    hit = [b for b in ("keep", "maybe", "discard") if k in bk[b]]
    human = [t.split(":")[2] for t in lib.tags(k) if t.startswith("s1:human:")]
    if len(hit) > 1 and len(set(human)) == 1:
        return human[0], True
    return (hit[0] if hit else None), len(hit) > 1


def funnel(lib):
    R = {"snapshot_version": lib.version}
    sup = superseded(lib)
    tree = lib.members(SLR_ROOT)

    per_src, Q, O = {}, set(), set()
    for name in QUERY_SOURCES + OTHER_SOURCES:
        imp = lib.imports(lib.source(name))
        per_src[name] = {"records": len(imp), "superseded": len(imp & sup)}
        (Q if name in QUERY_SOURCES else O).update(imp)
    SB = lib.imports(lib.source(SNOWBALL))
    per_src[SNOWBALL] = {"records": len(SB), "superseded": len(SB & sup)}
    qstream = (Q | O) - sup
    sstream = SB - Q - O - sup
    cross = (SB & (Q | O)) - sup
    R["identification"] = {
        "items_in_slr_tree": len(tree),
        "per_source_records_overlapping": per_src,
        "records_any_import": len(Q | O | SB),
        "removed_as_duplicate_superseded": len((Q | O | SB) & sup),
        "non_record_items_in_tree": len(tree - Q - O - SB),
        "unique_records": len((Q | O | SB) - sup),
        "query_stream": len(qstream),
        "  of_which_database": len((Q - sup)),
        "  of_which_other_methods_only": len((O - Q) - sup),
        "snowball_stream": len(sstream),
        "snowball_hits_already_in_query_stream": len(cross),
    }

    # ---- Phase 1 (recall screen) ------------------------------------------------------
    qb = collections.defaultdict(set)
    for name in QUERY_SOURCES + OTHER_SOURCES:
        for b, m in lib.buckets(lib.source(name)).items():
            qb[b] |= m
    sb = lib.buckets(lib.source(SNOWBALL))

    def p1(stream, bk):
        dec, conflicts, unscreened = {}, [], []
        for k in stream:
            d, c = p1_decision(lib, k, bk)
            if c:
                conflicts.append(k)
            if d is None:
                unscreened.append(k)
            else:
                dec[k] = d
        return dec, conflicts, unscreened

    qd, qconf, qun = p1(qstream, qb)
    sd, sconf, sun = p1(sstream, sb)
    held = {k for k in sstream if "hold:no-abstract" in lib.tags(k)}
    cnt = lambda d: dict(collections.Counter(d.values()))
    un_by_coll = collections.Counter(
        "/".join(lib.cols[c]["name"] for c in lib.items[k]["collections"] if c in lib.cols) for k in qun)
    R["phase1"] = {
        "query": cnt(qd), "query_conflicts": len(qconf), "query_unscreened": len(qun),
        "query_unscreened_by_collection": dict(un_by_coll),
        "snowball": cnt(sd), "snowball_conflicts": len(sconf), "snowball_unscreened": len(sun),
        "snowball_held_no_abstract": len(held),
        "snowball_held_by_p1_bucket": dict(collections.Counter(sd.get(k) for k in held)),
    }

    # ---- Phase 2 (operationalizability screen) ---------------------------------------
    p2 = {}
    for (a, b), c in P2_QUERY.items():
        for k in lib.members(c) & qstream:
            p2[k] = (a, b)
    eligible_q = {k for k, (a, b) in p2.items() if b == "keep"}
    passed = {k for k, d in qd.items() if d in ("keep", "maybe")}
    s2 = {k: [t.split(":")[2] for t in lib.tags(k) if t.startswith("s2:opus:")] for k in sstream}
    R["phase2"] = {
        "query_input_p1_keep_maybe": len(passed),
        "query_cells": {f"{a}->{b}": sum(1 for v in p2.values() if v == (a, b)) for a, b in P2_QUERY},
        "query_eligible": len(eligible_q),
        "query_p1_pass_missing_from_p2": len(passed - set(p2)),
        "query_in_p2_but_p1_discard": len(set(p2) - passed),
        "snowball_s2opus": dict(collections.Counter(v[0] for v in s2.values() if v)),
    }

    # ---- Phase 3 (relevance triage, provisional eligibility) -------------------------
    def tri(spec, stream):
        out = {}
        for b, c in spec.items():
            for k in lib.members(c) & stream:
                out.setdefault(k, []).append(b)
        return out
    t3q, t3s = tri(P3_QUERY, qstream), tri(P3_SNOW, sstream | qstream)
    fin = tri(FINAL, qstream | sstream)
    one = lambda d: dict(collections.Counter(v[0] if len(v) == 1 else "+".join(v) for v in d.values()))
    human = lambda ks: dict(collections.Counter(
        "/".join(sorted(t.split(":")[2] for t in lib.tags(k) if t.startswith("s3:human:"))) or "(none)"
        for k in ks))
    R["phase3"] = {
        "query_triage": one(t3q),
        "query_eligible_not_triaged": len(eligible_q - set(t3q)),
        "query_triaged_not_eligible": len(set(t3q) - eligible_q),
        "snowball_triage": one({k: v for k, v in t3s.items() if k in sstream}),
        "snowball_triage_records_in_query_stream": len(set(t3s) & qstream),
        "final_merged": one(fin),
        "final_by_stream": {b: {"query": len(lib.members(c) & qstream), "snowball": len(lib.members(c) & sstream)}
                            for b, c in FINAL.items()},
        "final_superseded_still_filed": {b: len(lib.members(c) & sup) for b, c in FINAL.items()},
        "triaged_not_in_final": len((set(t3q) | (set(t3s) & sstream)) - set(fin)),
        "final_core_s3human": human(k for k, v in fin.items() if v == ["core"]),
    }

    # ---- Phases 4-6 (full-text eligibility, finalized) --------------------------------
    core = {k for k, v in fin.items() if "core" in v}
    demoted = {k for k in core if "demote:context" in lib.tags(k)}
    reviewed = {k for k in core if any(t.startswith("cal:human:primary:") for t in lib.tags(k))}
    p6 = lib.members(PHASE6, deep=False)
    surv = (core - demoted) & reviewed
    R["fulltext"] = {
        "core_entering_fulltext": len(core),
        "demoted_to_context": len(demoted),
        "not_demoted": len(core - demoted),
        "not_demoted_with_human_primary": len(surv),
        "not_demoted_without_human_primary": sorted(core - demoted - reviewed),
        "demoted_but_have_primary": len(demoted & reviewed),
        "phase6_collection": len(p6),
        "phase6_superseded": sorted(p6 & sup),
        "phase6_minus_predicate": sorted(p6 - surv),
        "predicate_minus_phase6": sorted(surv - p6),
        "phase6_from_stream": {"query": len(p6 & qstream), "snowball": len(p6 & sstream)},
        "phase6_not_from_final_core": sorted(p6 - core),
    }
    return R


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump")
    ap.add_argument("--snapshot")
    ap.add_argument("--json")
    a = ap.parse_args()
    if a.dump:
        dump(a.dump)
    if a.snapshot:
        R = funnel(Lib(json.load(open(a.snapshot))))
        s = json.dumps(R, indent=2)
        print(s)
        if a.json:
            open(a.json, "w").write(s + "\n")


if __name__ == "__main__":
    sys.exit(main())
