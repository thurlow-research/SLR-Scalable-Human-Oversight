#!/usr/bin/env python3
"""Print the F2 review step-2 confirmation queue (Phase 6 only) as reviewer-ready batches.

Open decision = a panel proposal at >=2/3 on a Phase 6 paper with no human ruling: F2-family slugs
(F2, F2b, F2c runs), plus the §150a implicit-confirmation residue (frozen vocabulary, surviving papers).
For each, shows panel support and the models' own one-line reason. Read-only.

Usage:  python3 slr-tools/f2_step2_batch.py [--batch N] [--size 10]
"""
import argparse, collections, glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import tag_layer_stats as T
R = os.path.join(os.path.dirname(HERE), "slr-phase4", "data")
ALIAS = {"3Z45M3V3": "U3IQJ4VK"}
F2 = set(json.load(open(os.path.join(R, "f2_census.json")))) | {"deterministic-orchestration-v2", "rules-based-checks-v3"}
DEP = {"counterpoint"}

def reasons():
    out = collections.defaultdict(lambda: collections.defaultdict(list))
    for d in ("tags-f2", "tags-f2b", "tags-f2c", "tags-v213"):
        for f in glob.glob(os.path.join(R, d, "*", "*.json")):
            if f.endswith(".meta.json") or re.search(r"\.r\d+\.json$", f): continue
            v = f.split(os.sep)[-2]; k = os.path.basename(f)[:-5]; k = ALIAS.get(k, k)
            j = json.load(open(f))
            rats = j.get("rationales")
            if not isinstance(rats, dict) and isinstance(j.get("rationale"), dict):
                rats = j["rationale"]
            if isinstance(rats, dict):
                for s, r in rats.items(): out[k][s].append((v, r if isinstance(r, str) else json.dumps(r)))
            elif isinstance(j.get("rationale"), str):
                for s in set(j.get("themes") or []) | set(j.get("facets") or []):
                    sent = [x for x in re.split(r"(?<=[.;])\s+", j["rationale"]) if s in x]
                    if sent: out[k][s].append((v, sent[0]))
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--batch", type=int, default=1); ap.add_argument("--size", type=int, default=10)
    a = ap.parse_args()
    p6 = T.fetch_band(os.environ["ZOTERO_LIBRARY_ID"], "group", "R9ZHDXMN", os.environ["ZOTERO_API_KEY_RO"])
    frozen = set(T.FROZEN_THEMES) | set(T.FROZEN_FACETS); RS = reasons()
    q = {}
    for k, d in p6.items():
        L = T.split_layers(d); ruled = {s for _, s in L["human"]} | {s for _, s in L["reject"]}
        open_ = [(kind, s, n) for (kind, s), n in L["votes"].items()
                 if n >= 2 and s not in ruled and s not in DEP and (s in F2 or (s in frozen and not L["demoted"]))]
        if open_: q[k] = (d, L, sorted(open_, key=lambda x: (-x[2], x[1])))
    order = sorted(q, key=lambda k: (len(q[k][2]), ((q[k][0].get("creators") or [{}])[0].get("lastName") or "")))
    chunk = order[(a.batch - 1) * a.size: a.batch * a.size]
    print(f"open: {sum(len(v[2]) for v in q.values())} decisions on {len(q)} papers · batch {a.batch}: {len(chunk)} papers\n")
    for k in chunk:
        d, L, items = q[k]; c = d.get("creators") or [{}]
        au = c[0].get("lastName") or c[0].get("name", "?")
        print(f"### {au} `{k}` — {d['title'][:90]}  (primary: {L['primary']})")
        for kind, s, n in items:
            rs = RS[k].get(s, [])
            print(f"   [{kind}] {s}  {n}/3" + (f"  — {rs[0][0]}: {rs[0][1][:260]}" if rs else ""))
        print()
if __name__ == "__main__": main()
