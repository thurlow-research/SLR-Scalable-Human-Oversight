#!/usr/bin/env python3
"""Record-level reconciliation behind Methodology/Appendix_A_Count_Reconciliation_2026-11-02.md.

prisma_funnel.py reports counts; this script names the records behind the residues those counts
leave (the 3 unbucketed query records, the 1,208 -> 1,213 gap, human involvement in the
title/abstract exclusions, and the Stage-3 below-floor false-negative evidence). Read-only.

Usage (from the repo root):
    python3 slr-tools/prisma_funnel.py --dump /path/lib.json        # RO key
    python3 slr-tools/appendix_a_recon.py /path/lib.json
"""
import collections
import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prisma_funnel as P  # noqa: E402

STAGE3 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stage3", "work")
FLOOR = 55

lib = P.Lib(json.load(open(sys.argv[1])))
sup = P.superseded(lib)
Q, O = set(), set()
for n in P.QUERY_SOURCES + P.OTHER_SOURCES:
    (Q if n in P.QUERY_SOURCES else O).update(lib.imports(lib.source(n)))
SB = lib.imports(lib.source(P.SNOWBALL))
qs, ss = (Q | O) - sup, SB - Q - O - sup

qb = collections.defaultdict(set)
for n in P.QUERY_SOURCES + P.OTHER_SOURCES:
    for b, m in lib.buckets(lib.source(n)).items():
        qb[b] |= m
qd, qun = {}, []
for k in qs:
    d, _ = P.p1_decision(lib, k, qb)
    (qun.append(k) if d is None else qd.__setitem__(k, d))
p2 = {}
for (a, b), c in P.P2_QUERY.items():
    for k in lib.members(c) & qs:
        p2[k] = (a, b)
elig = {k for k, v in p2.items() if v[1] == "keep"}


def tri(spec, stream):
    out = {}
    for b, c in spec.items():
        for k in lib.members(c) & stream:
            out.setdefault(k, []).append(b)
    return out


t3q, t3s, fin = tri(P.P3_QUERY, qs), tri(P.P3_SNOW, ss | qs), tri(P.FINAL, qs | ss)
p6 = lib.members(P.PHASE6, deep=False)


def tags(k, *pfx):
    return sorted(t for t in lib.tags(k) if t.startswith(pfx))


def row(k):
    return f"  {k}  final={fin.get(k)}  p6={k in p6}  {tags(k, 's1:', 's2:', 's3:', 's4:', 'source:', 'superseded-by:')}  {lib.items[k].get('title', '')[:70]}"


print(f"snapshot v{lib.version}")

print("\n== Q1a: query records with no Phase-1 bucket that reached a later stage ==")
for k in sorted(k for k in qun if k in p2 or k in t3q or k in t3s or k in fin or k in p6):
    print(row(k))

print("\n== Q1b: 1,208 advanced vs 1,213 triaged ==")
adv_s = {k for k in ss if k in t3s}
s2keep = {k for k in ss if "s2:opus:keep" in lib.tags(k)}
print(f"query eligible {len(elig)} + snowball triaged {len(adv_s)} = {len(elig) + len(adv_s)}; in 03-Final {len(fin)}")
print("in 03-Final (query stream) but not Phase-2 eligible:")
for k in sorted((set(fin) & qs) - elig):
    print(row(k))
print("Phase-2 eligible but never triaged:")
for k in sorted(elig - set(fin)):
    print(row(k))
print("snowball s2:opus:keep never triaged:")
for k in sorted(s2keep - adv_s):
    print(row(k))

print("\n== Q2: human involvement in title/abstract exclusions ==")


def single(k, p):
    v = {t.split(":")[2] for t in lib.tags(k) if t.startswith(p)}
    return next(iter(v)) if len(v) == 1 else None


c = collections.Counter()
for k in set(qd) - elig:
    if qd[k] == "discard":
        c[("query P1 discard", "human" if tags(k, "s1:human:") else "model only")] += 1
    else:
        c[("query P2 not advanced", "human" if tags(k, "s2:human:") else "model only")] += 1
held = {k for k in ss if "hold:no-abstract" in lib.tags(k)}
ex_s = ss - held - adv_s
c[("snowball", "human" if any(tags(k, "s1:human:", "s2:human:") for k in ex_s) else "model only")] += len(ex_s)
for kv in sorted(c.items()):
    print(" ", kv)
ag = collections.Counter((single(k, "s1:claude:"), single(k, "s1:human:")) for k in qs)
cd = {h: n for (cl, h), n in ag.items() if cl == "discard" and h}
print(f"  Claude P1 discards also human-coded: {sum(cd.values())}; human agreed {cd.get('discard', 0)}")
rev = sorted(k for k in set(qd) - elig if qd[k] != "discard" and "s1:human:keep" in lib.tags(k)
             and p2.get(k, ("", ""))[1] == "discard" and not tags(k, "s2:human:"))
print(f"  s1:human:keep -> Pass-2 discard bucket, no s2:human: {len(rev)} "
      f"({sum(1 for k in rev if tags(k, 's4:'))} re-adjudicated in F6)")

print(f"\n== Q3: Stage-3 floor (centrality >= {FLOOR}) ==")
res = [r for r in csv.DictReader(open(os.path.join(STAGE3, "stage3_results.csv"))) if r["is_primary"] == "yes"]
print(" ", sorted(collections.Counter((r["bin"], int(r["centrality"]) >= FLOOR) for r in res).items()))
opus = {r["item_key"]: r for r in csv.DictReader(open(os.path.join(STAGE3, "qa", "qa_master_250.csv")))}
print("  human-50 sample, human core or retained with Opus centrality below floor:")
for r in csv.DictReader(open(os.path.join(STAGE3, "qa", "human_review_50.csv"))):
    o = opus[r["item_key"]]
    if int(o["centrality"]) < FLOOR and (r["bin"] == "core" or o["bin"] == "discard" != r["bin"]):
        k = r["item_key"]
        print(f"   {k} human={r['bin']} opus={o['bin']}/{o['centrality']} "
              f"library={fin.get(k)} {tags(k, 's3:human:') if k in lib.items else 'NOT IN LIBRARY'}")
