#!/usr/bin/env python3
"""F1 — compute the reportable tag set `final:*` for Phase 6 (the 72 kept articles).

    final:* = panel modal ∪ human endorsements − human rejections − deprecated vocabulary   (§101a)

* panel modal  = proposed by >= 2 DISTINCT vendors (opus, codex, gemini). Counted by vendor, not by tag (§173).
* human        = cal:human:<kind>:<slug>;  rejections = cal:human:reject:<kind>:<slug>.
* deprecated   = slr-phase4/data/deprecated_vocabulary.json (never emitted — §101a).
* primary      = the arbiter's cal:human:primary:theme:X → final:primary:theme:X (+ final:theme:X).
* ALL non-deprecated versions are emitted (v1 / -v2 / -v3 coexist); which one the synthesis reads is resolved by
  slr-phase4/data/governing_versions.json, not by dropping tags (arbiter, 2026-10-04).

final:* is a DERIVED layer: a recompute replaces an item's final:* tags wholesale. The cal:* layers it is
computed from are never touched. Checks enforced (closeout F1): no deprecated slug in final:*; Phase 6 only;
every item has exactly one final primary; no slug emitted in both namespaces.

DRY RUN BY DEFAULT: prints the plan and writes a JSON snapshot. --commit writes to Zotero (back up first).
Usage:  python3 slr-tools/compute_final.py [--commit] [--snapshot PATH]
"""

from __future__ import annotations

import argparse
import collections
import datetime
import json
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tag_layer_stats as T  # noqa: E402

R = os.path.join(os.path.dirname(HERE), "slr-phase4", "data")
PHASE6 = "R9ZHDXMN"
LIB = os.environ.get("ZOTERO_LIBRARY_ID")


def compute(d, deprecated):
    L = T.split_layers(d)
    modal = {ks for ks, n in L["votes"].items() if n >= 2}
    final = (modal | L["human"]) - L["reject"]
    final = {(k, s) for k, s in final if s not in deprecated}
    prim = L["primary"]
    if prim:
        final.add(("theme", prim))
    return L, modal, final, prim


def tagset(final, prim):
    tags = {f"final:{k}:{s}" for k, s in final}
    if prim:
        tags.add(f"final:primary:theme:{prim}")
    return tags


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--commit", action="store_true")
    ap.add_argument("--snapshot", default=os.path.join(R, f"final_tags_{datetime.date.today().isoformat()}.json"))
    a = ap.parse_args()
    ro, rw = os.environ.get("ZOTERO_API_KEY_RO"), os.environ.get("ZOTERO_API_KEY_RW")
    deprecated = {x["slug"] for x in json.load(open(os.path.join(R, "deprecated_vocabulary.json")))["deprecated"]}
    p6 = T.fetch_band(LIB, "group", PHASE6, ro)

    snap, problems, kinds = {}, [], collections.defaultdict(set)
    src = collections.Counter()
    for k, d in sorted(p6.items()):
        L, modal, final, prim = compute(d, deprecated)
        if not prim:
            problems.append(f"{k}: no human primary — not adjudicated")
        for kind, s in final:
            kinds[s].add(kind)
            src["modal+human" if (kind, s) in modal and (kind, s) in L["human"]
                else "modal only (silent)" if (kind, s) in modal else "human only"] += 1
        snap[k] = {"title": d.get("title", ""), "primary": prim, "final": sorted(tagset(final, prim))}
    both = sorted(s for s, ks in kinds.items() if len(ks) > 1)
    if both:
        problems.append(f"slug(s) in both namespaces: {both}")
    leaked = [k for k, v in snap.items() if any(t.split(":")[-1] in deprecated for t in v["final"])]
    if leaked:
        problems.append(f"deprecated slug leaked into final:* on {leaked}")

    n = sum(len(v["final"]) for v in snap.values())
    print(f"Phase 6: {len(snap)} items · {n} final:* tags · sources: {dict(src)}")
    print("final:* tags per item:", dict(sorted(collections.Counter(len(v['final']) for v in snap.values()).items())))
    per_slug = collections.Counter(t.split(":", 2)[2] for v in snap.values() for t in v["final"] if not t.startswith("final:primary"))
    print("most frequent:", per_slug.most_common(12))
    print("deprecated excluded:", sorted(deprecated), "| leaked:", len(leaked))
    json.dump({"computed": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
               "formula": "final = panel modal (>=2 distinct vendors) ∪ human endorsements − human rejections − deprecated (§101a, §173)",
               "deprecated": sorted(deprecated), "items": snap}, open(a.snapshot, "w"), indent=1, ensure_ascii=False)
    print("snapshot:", os.path.relpath(a.snapshot))
    if problems:
        print("\nCHECKS FAILED:"); [print("  ", p) for p in problems]
        return 1
    print("checks: OK (one primary per item · no deprecated · no namespace collisions · Phase 6 only)")
    if not a.commit:
        print("\nDRY RUN — nothing written. Re-run with --commit (back up the library first).")
        return 0
    if not rw:
        sys.exit("refusing to --commit without ZOTERO_API_KEY_RW")

    ok = fail = 0
    for k, v in snap.items():
        url = f"https://api.zotero.org/groups/{LIB}/items/{k}"
        with urllib.request.urlopen(urllib.request.Request(url, headers={"Zotero-API-Key": ro})) as r:
            d = json.load(r)["data"]
        keep = [t for t in d["tags"] if not t["tag"].startswith("final:")]  # derived layer replaced wholesale
        body = json.dumps({"tags": keep + [{"tag": t} for t in v["final"]]}).encode()
        urllib.request.urlopen(urllib.request.Request(url, data=body, method="PATCH", headers={
            "Zotero-API-Key": rw, "Content-Type": "application/json",
            "If-Unmodified-Since-Version": str(d["version"])})).close()
        with urllib.request.urlopen(urllib.request.Request(url, headers={"Zotero-API-Key": ro})) as r:
            now = {t["tag"] for t in json.load(r)["data"]["tags"] if t["tag"].startswith("final:")}
        if now == set(v["final"]):
            ok += 1
        else:
            fail += 1; print("   VERIFY FAILED", k)
    print(f"\nwritten+verified {ok} · failed {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
