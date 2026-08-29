#!/usr/bin/env python3
"""Score the F2 calibration run against arbiter-settled answers.

Answers one question: DO THE NEW AND REVISED DEFINITIONS READ CORRECTLY?
It is a gate on the instrument, not a measurement of the panel.

Failure rule: a definition fails if a `must` is missed or a `must_not` fires at
**>=2/3 vendor agreement**. One dissenting vendor is noise; a majority means the
definition reads wrong and must be fixed before the other 63 papers are run.

Also enforces the OUTPUT CONTRACT — any slug outside the permitted ten, or an
unsuffixed v1 slug, is a validation failure rather than a proposal.

Usage:
    python3 slr-phase4/tools/score_f2_calibration.py
    python3 slr-phase4/tools/score_f2_calibration.py --run r2
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECTED = os.path.join(R, "data", "f2_calibration_expected.json")
RUNDIR = os.path.join(R, "data", "tags-f2")
VENDORS = ("opus", "codex", "gemini")

THEMES = {"evaluator-reliability", "oversight-scaling-inversion-v2", "rules-based-checks-v2"}
FACETS = {"agent-panel", "cross-model", "evaluated-real-data", "evaluated-synthetic",
          "evaluated-benchmark", "deterministic-orchestration", "survey-input-v2"}
PERMITTED = THEMES | FACETS
V1_LEAK = {"survey-input", "rules-based-checks", "oversight-scaling-inversion", "counterpoint",
           "scaling-dissent"}


def load(vendor: str, key: str, run: str) -> dict | None:
    sfx = "" if run == "r1" else f".{run}"
    p = os.path.join(RUNDIR, vendor, f"{key}{sfx}.json")
    if not os.path.exists(p) or os.path.getsize(p) == 0:
        return None
    try:
        with open(p) as fh:
            return json.load(fh)
    except json.JSONDecodeError:
        return {"_malformed": True}


def emitted(d: dict) -> set[str]:
    return set(d.get("themes") or []) | set(d.get("facets") or [])


def flagged(d: dict) -> set[str]:
    return {f.get("slug") for f in (d.get("flags") or []) if isinstance(f, dict)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", default="r1")
    args = ap.parse_args()

    with open(EXPECTED) as fh:
        spec = json.load(fh)
    cases = spec["cases"]

    print(f"F2 CALIBRATION — run {args.run} · {len(cases)} papers · {len(VENDORS)} vendors\n")

    contract, defects = [], []
    missing = 0
    per_slug = collections.defaultdict(lambda: {"hit": 0, "want": 0, "false": 0})

    for key, c in cases.items():
        outs = {v: load(v, key, args.run) for v in VENDORS}
        have = {v: d for v, d in outs.items() if d}
        if len(have) < len(VENDORS):
            missing += len(VENDORS) - len(have)
        print(f"── {key}  {c['author']}   ({len(have)}/{len(VENDORS)} vendors returned)")

        votes, flags = collections.Counter(), collections.Counter()
        for v, d in have.items():
            if d.get("_malformed"):
                contract.append(f"{key}/{v}: MALFORMED JSON")
                continue
            e = emitted(d)
            for s in e - PERMITTED:
                contract.append(f"{key}/{v}: illegal slug {s!r}"
                                + ("  (V1 LEAK)" if s in V1_LEAK else ""))
            # namespace check
            for s in set(d.get("themes") or []) & FACETS:
                contract.append(f"{key}/{v}: {s!r} emitted as THEME, is a facet")
            for s in set(d.get("facets") or []) & THEMES:
                contract.append(f"{key}/{v}: {s!r} emitted as FACET, is a theme")
            for s in e & PERMITTED:
                if s not in (d.get("rationales") or {}):
                    contract.append(f"{key}/{v}: {s!r} emitted with NO RATIONALE (discardable)")
            votes.update(e & PERMITTED)
            flags.update(flagged(d))

        n = max(len(have), 1)
        for s in c.get("must", []):
            per_slug[s]["want"] += 1
            ok = votes[s] >= 2
            per_slug[s]["hit"] += 1 if ok else 0
            print(f"     must      {s:<32} {votes[s]}/{n}  {'OK' if ok else '** MISS **'}")
            if not ok:
                defects.append(f"{key} ({c['author']}): MISSED {s} — only {votes[s]}/{n}")
        for s in c.get("must_not", []):
            bad = votes[s] >= 2
            if bad:
                per_slug[s]["false"] += 1
            print(f"     must_not  {s:<32} {votes[s]}/{n}  {'** FIRED **' if bad else 'OK'}")
            if bad:
                defects.append(f"{key} ({c['author']}): FALSE POSITIVE {s} — {votes[s]}/{n}")
        for s in c.get("flag", []):
            ok = flags[s] >= 2
            print(f"     flag      {s:<32} {flags[s]}/{n}  {'OK' if ok else '** NOT FLAGGED **'}")
            if not ok:
                defects.append(f"{key} ({c['author']}): expected a flag on {s}, got {flags[s]}/{n}")
        print()

    print("=" * 74)
    if contract:
        print(f"\nOUTPUT-CONTRACT VIOLATIONS ({len(contract)}) — these are bugs, not proposals:")
        for c_ in contract:
            print("   ", c_)
    else:
        print("\nOutput contract: clean.")

    if missing:
        print(f"\n⚠ {missing} vendor/paper outputs missing or empty — rerun before trusting the score.")

    print("\nPER-SLUG:")
    for s in sorted(per_slug):
        d = per_slug[s]
        print(f"   {s:<34} recall {d['hit']}/{d['want']}   false-positives {d['false']}")

    print()
    if defects:
        print(f"❌ CALIBRATION FAILED — {len(defects)} defect(s). Fix the instrument before the full run:")
        for d in defects:
            print("   ", d)
        return 1
    print("✅ CALIBRATION PASSED — definitions read correctly. Cleared for the remaining papers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
