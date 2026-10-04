#!/usr/bin/env python3
"""Build the F2 review queue: every (paper, tag) decision the arbiter still owes on the F2 vocabulary.

Four parts, from the 2026-08-29 handoff §7 items 1–2:
  A  strong panel signal (>=2/3 vendors), no human ruling
  B  human tag present, weak panel signal (<=1/3)
  C  sweep of the -v2 slugs on every paper where the v1 tag was used or the v2 tag was proposed,
     plus the agent-panel / peer-critique split
  D  a model flag on the tag, no human ruling
Plus the §150a implicit-confirmation residue (frozen vocabulary), so each paper is visited once.

Reads the F2 run files (and F2b, if present) from disk, and the human layer live from Zotero (RO key).
Writes nothing to Zotero.

Usage:  python3 slr-tools/f2_review_queue.py [--json out.json] [--by-paper]
"""

from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tag_layer_stats as T  # noqa: E402

R = os.path.join(os.path.dirname(HERE), "slr-phase4")
VENDORS = ("opus", "codex", "gemini")
# Record keys that changed after the F2 run (Zotero dedupe merges). Changelog §151d.
ALIAS = {"3Z45M3V3": "U3IQJ4VK"}
V1_OF = {"oversight-scaling-inversion-v2": "oversight-scaling-inversion",
         "survey-input-v2": "survey-input", "rules-based-checks-v2": "rules-based-checks"}
DEPRECATED = {d["slug"] for d in json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "slr-phase4", "data", "deprecated_vocabulary.json")))["deprecated"]}  # §101a


def load_runs(rundir):
    runs, flags = {}, collections.defaultdict(set)
    for v in VENDORS:
        for f in glob.glob(os.path.join(R, "data", rundir, v, "*.json")):
            if f.endswith(".meta.json"):
                continue
            k = os.path.basename(f)[:-5]
            k = ALIAS.get(k, k)
            j = json.load(open(f))
            runs[(v, k)] = set(j.get("themes") or []) | set(j.get("facets") or [])
            for fl in j.get("flags") or []:
                flags[(k, fl.get("slug"))].add(v)
    return runs, flags


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    ap.add_argument("--by-paper", action="store_true")
    a = ap.parse_args()
    lib, key = os.environ["ZOTERO_LIBRARY_ID"], os.environ["ZOTERO_API_KEY_RO"]

    vocab = set(json.load(open(os.path.join(R, "data", "f2_census.json"))))
    runs, flags = load_runs("tags-f2")
    if os.path.isdir(os.path.join(R, "data", "tags-f2b")):
        r2, f2 = load_runs("tags-f2b")
        for (v, k), s in r2.items():
            runs[(v, k)] = runs.get((v, k), set()) | s
        for k_, vs in f2.items():
            flags[k_] |= vs
        vocab.add("deterministic-orchestration-v2")
    frozen = set(T.FROZEN_THEMES) | set(T.FROZEN_FACETS)

    p6 = T.fetch_band(lib, "group", "R9ZHDXMN", key)
    queue = collections.defaultdict(dict)       # paper -> slug -> set(reasons)
    for k, d in p6.items():
        L = T.split_layers(d)
        human = {s for _, s in L["human"]}
        ruled = human | {s for _, s in L["reject"]}
        votes = collections.Counter(s for v in VENDORS for s in runs.get((v, k), ()))

        def add(slug, why):
            if slug not in ruled:
                queue[k].setdefault(slug, set()).add(why)

        for s in vocab:
            if votes[s] >= 2:
                add(s, "A strong signal")
            if s in human and votes[s] <= 1:
                queue[k].setdefault(s, set()).add("B human tag, weak signal")
            if flags.get((k, s)):
                add(s, f"D flagged ({'/'.join(sorted(flags[(k, s)]))})")
        for v2, v1 in V1_OF.items():
            if v1 in human or votes[v2]:
                add(v2, "C -v2 sweep")
        if ("agent-panel" in human or votes["agent-panel"] or votes["peer-critique"]) \
                and not ({"agent-panel", "peer-critique"} & ruled):
            add("agent-panel/peer-critique", "C split sweep")
        # §150a residue: frozen-vocabulary panel-modal proposals left silent on a surviving paper
        if not L["demoted"]:
            for (kind, s), n in L["votes"].items():
                if n >= 2 and s in frozen and s not in DEPRECATED and (kind, s) not in L["human"] \
                        and (kind, s) not in L["reject"]:
                    add(s, "E §150a implicit confirmation")

    items = [(k, s, r) for k, v in queue.items() for s, rs in v.items() for r in rs]
    print(f"queue: {sum(len(v) for v in queue.values())} decisions on {len(queue)} papers "
          f"({len(items)} reason-rows)")
    for r, n in sorted(collections.Counter(r.split(' (')[0] for _, _, r in items).items()):
        print(f"   {r:34s} {n}")
    if a.by_paper:
        name = lambda k: ((p6[k].get("creators") or [{}])[0].get("lastName")
                          or (p6[k].get("creators") or [{}])[0].get("name", "?"))
        for k in sorted(queue, key=lambda k: -len(queue[k])):
            print(f"\n{name(k)} {k}  ({len(queue[k])})")
            for s, rs in sorted(queue[k].items()):
                print(f"   {s:34s} {'; '.join(sorted(rs))}")
    if a.json:
        json.dump({k: {s: sorted(r) for s, r in v.items()} for k, v in queue.items()},
                  open(a.json, "w"), indent=1)


if __name__ == "__main__":
    main()
