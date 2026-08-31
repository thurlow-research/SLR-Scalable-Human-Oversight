#!/usr/bin/env python3
"""Write the F2 restricted re-run's per-vendor proposals into Zotero.

Writes `cal:<vendor>:theme:<slug>` / `cal:<vendor>:facet:<slug>` for the 11 F2
slugs only. ADDITIVE — never removes a tag, never touches `cal:human:*`, never
proposes a primary or a disposition.

Guards, each from a real failure earlier in this project:
  * SLUG WHITELIST — anything outside the 11 is a validation failure, not a
    proposal. Catches v1 leakage (`survey-input` vs `survey-input-v2`).
  * NAMESPACE CHECK — a theme emitted as a facet (or vice versa) is refused.
    A slug split across namespaces yields two half-populated constructs in
    `final:*` (§146a, evaluator-reliability).
  * RATIONALE REQUIRED — a slug emitted without one is discarded, matching the
    instrument's own output contract.
  * ABORTS if any vendor/paper output is missing or malformed, so a partial run
    cannot half-populate the band.
  * If-Unmodified-Since-Version on every PATCH; verifies each item after write.

DRY RUN BY DEFAULT. Pass --commit to write. Back up the library first.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.dirname(HERE)
RUNDIR = os.path.join(R, "data", "tags-f2")
KEYS = os.path.join(R, "data", "f2_phase6_keys.json")
VENDORS = ("opus", "codex", "gemini")

THEMES = {"evaluator-reliability", "oversight-scaling-inversion-v2", "rules-based-checks-v2"}
FACETS = {"agent-panel", "peer-critique", "cross-model", "evaluated-real-data",
          "evaluated-synthetic", "evaluated-benchmark", "deterministic-orchestration",
          "survey-input-v2"}
PERMITTED = THEMES | FACETS

LIB = os.environ.get("ZOTERO_LIBRARY_ID")
LT = os.environ.get("ZOTERO_LIBRARY_TYPE", "group")


def _req(key, path, data=None, method="GET", extra=None):
    h = {"Zotero-API-Version": "3", "Authorization": f"Bearer {key}"}
    if data is not None:
        h["Content-Type"] = "application/json"
    h.update(extra or {})
    return urllib.request.urlopen(urllib.request.Request(
        f"https://api.zotero.org/{LT}s/{LIB}{path}", data=data, headers=h, method=method))


def plan_item(key: str) -> tuple[list[str], list[str]]:
    """(tags to add, problems) for one paper across all vendors."""
    tags, problems = [], []
    for v in VENDORS:
        p = os.path.join(RUNDIR, v, f"{key}.json")
        if not os.path.exists(p) or os.path.getsize(p) == 0:
            problems.append(f"{v}/{key}: MISSING")
            continue
        try:
            d = json.load(open(p))
        except Exception:
            problems.append(f"{v}/{key}: MALFORMED")
            continue
        rats = d.get("rationales") or {}
        for kind, slugs, valid in (("theme", d.get("themes") or [], THEMES),
                                   ("facet", d.get("facets") or [], FACETS)):
            for s in slugs:
                if s not in PERMITTED:
                    problems.append(f"{v}/{key}: illegal slug {s!r}")
                    continue
                if s not in valid:
                    problems.append(f"{v}/{key}: {s!r} emitted as {kind}, wrong namespace")
                    continue
                if s not in rats:
                    problems.append(f"{v}/{key}: {s!r} has no rationale — discarded")
                    continue
                tags.append(f"cal:{v}:{kind}:{s}")
    return sorted(set(tags)), problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--commit", action="store_true", help="actually write (default: dry run)")
    args = ap.parse_args()

    ro = os.environ.get("ZOTERO_API_KEY_RO") or os.environ.get("ZOTERO_API_KEY")
    rw = os.environ.get("ZOTERO_API_KEY_RW")
    if args.commit and not rw:
        print("refusing to --commit without ZOTERO_API_KEY_RW (least privilege)", file=sys.stderr)
        return 2
    if not ro or not LIB:
        print("need ZOTERO_API_KEY(_RO) and ZOTERO_LIBRARY_ID", file=sys.stderr)
        return 2

    keys = json.load(open(KEYS))
    plans, all_problems = {}, []
    for k in keys:
        t, p = plan_item(k)
        plans[k] = t
        all_problems += p

    hard = [p for p in all_problems if "MISSING" in p or "MALFORMED" in p or "illegal" in p
            or "wrong namespace" in p]
    if hard:
        print(f"ABORT: {len(hard)} hard problem(s) — refusing to half-populate the band:",
              file=sys.stderr)
        for p in hard[:20]:
            print("   ", p, file=sys.stderr)
        return 1
    soft = [p for p in all_problems if p not in hard]
    if soft:
        print(f"discarded {len(soft)} slug(s) lacking a rationale:")
        for p in soft:
            print("   ", p)
        print()

    total = sum(len(v) for v in plans.values())
    tagged = sum(1 for v in plans.values() if v)
    print(f"{len(keys)} papers · {total} tags to add · {tagged} papers receive at least one")
    print(f"{len(keys) - tagged} papers get nothing (a valid and expected result)\n")
    for k in sorted(plans, key=lambda x: -len(plans[x]))[:8]:
        if plans[k]:
            print(f"   {k}  {len(plans[k]):2d}  {', '.join(s.split(':',2)[2] for s in plans[k][:3])}…")

    if not args.commit:
        print("\nDRY RUN — nothing written. Re-run with --commit (back up the library first).")
        return 0

    ok = fail = skipped = 0
    for k, add in plans.items():
        if not add:
            skipped += 1
            continue
        d = json.load(_req(ro, f"/items/{k}"))["data"]
        have = {t["tag"] for t in d.get("tags", [])}
        new = sorted(have | set(add))
        if new == sorted(have):
            skipped += 1
            continue
        body = json.dumps({"tags": [{"tag": t} for t in new]}).encode()
        try:
            _req(rw, f"/items/{k}", data=body, method="PATCH",
                 extra={"If-Unmodified-Since-Version": str(d["version"])})
            after = {t["tag"] for t in json.load(_req(ro, f"/items/{k}"))["data"].get("tags", [])}
            missing = set(add) - after
            if missing:
                print(f"  VERIFY FAILED {k}: {missing}", file=sys.stderr)
                fail += 1
            else:
                ok += 1
        except urllib.error.HTTPError as e:
            print(f"  FAIL {k}: HTTP {e.code} {e.reason}", file=sys.stderr)
            fail += 1
    print(f"\nwritten+verified {ok} · failed {fail} · unchanged {skipped}")
    return 0 if not fail else 1


if __name__ == "__main__":
    raise SystemExit(main())
