#!/usr/bin/env python3
"""Stage per-paper prompts for the F2 restricted re-run.

Each prompt = the F2 instrument verbatim + the paper's full text. The instrument
(`Tag_Prompt_F2_restricted.md`) is the record of what was asked; nothing is
paraphrased here, so the file in the repo IS what the panel saw.

Writes to $PANEL_S/prompts/<key>.txt, matching the sweep runner's layout.

Usage:
    PANEL_S=<scratchpad> python3 slr-phase4/tools/build_f2_prompts.py --calibration
    PANEL_S=<scratchpad> python3 slr-phase4/tools/build_f2_prompts.py --phase6
"""

from __future__ import annotations

import argparse
import json
import os
import sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INSTRUMENT = os.path.join(R, "Tag_Prompt_F2_restricted.md")
TXT = os.path.join(R, "txt")

# The calibration set: papers whose answers are already settled by the arbiter,
# chosen to exercise every NEW or REVISED definition in both directions.
CALIBRATION = [
    "GAD5Z8PV",  # Vargas   — deterministic-orchestration YES (fixed phases, AI verdicts)
    "UB2EVUFU",  # Lyu      — deterministic-orchestration YES (MIXED: code phases, agent staffing)
    "72W6R4JG",  # Töpfer   — rules-based-checks-v2 YES / det-orch NO
    "3SU9QZ6F",  # Parris   — rules-based-checks-v2 YES / det-orch NO
    "UDVHQ5HR",  # Jin      — rules-based-checks-v2 NO + hybrid FLAG
    "7UB2MD8Z",  # Kang     — survey-input-v2 YES (stated preference, reported)
    "T72TU8B5",  # Shukla   — survey-input-v2 NO (formative, §145a)
    "B644HQFS",  # Baltes   — survey-input-v2 NO (no instrument, §116a)
    "A6ZE2A26",  # Ullah    — agent-panel + cross-model + evaluator-reliability YES
    "R9CDT9KB",  # Mahmud   — evaluated-real-data YES / synthetic NO (§148b contrast)
    "74GE3TF7",  # Minh     — oversight-scaling-inversion-v2 NO (§127b 3/3 false positive)
    "NRVQT89E",  # McAleese — peer-critique ONE-DIRECTIONAL / cross-model NO / agent-panel NO
]


def phase6_keys() -> list[str]:
    """Read the Phase 6 roster from the sidecar the run writes, or fail loudly."""
    p = os.path.join(R, "data", "f2_phase6_keys.json")
    if not os.path.exists(p):
        sys.exit(f"missing {p} — generate it from Phase 6 - Kept Core (R9ZHDXMN) first")
    with open(p) as fh:
        return json.load(fh)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--calibration", action="store_true", help="the 9 known-answer papers")
    g.add_argument("--phase6", action="store_true", help="all 72 survivors")
    args = ap.parse_args()

    S = os.environ.get("PANEL_S")
    if not S:
        sys.exit("set PANEL_S to the scratchpad panel dir")
    out = os.path.join(S, "prompts")
    os.makedirs(out, exist_ok=True)

    with open(INSTRUMENT) as fh:
        instrument = fh.read()

    keys = CALIBRATION if args.calibration else phase6_keys()
    missing = [k for k in keys if not os.path.exists(os.path.join(TXT, f"{k}.txt"))]
    if missing:
        sys.exit(f"ABORT: no TXT for {len(missing)} key(s): {missing}")

    for k in keys:
        with open(os.path.join(TXT, f"{k}.txt")) as fh:
            body = fh.read()
        with open(os.path.join(out, f"{k}.txt"), "w") as fh:
            fh.write(instrument)
            fh.write(f"\n\n---\n\n# THE PAPER TO TAG — key {k}\n\n")
            fh.write(body)

    print(f"staged {len(keys)} prompts in {out}")
    print(f"instrument: {os.path.relpath(INSTRUMENT, R)} ({len(instrument):,} chars)")
    with open(os.path.join(S, "f2_keys.json"), "w") as fh:
        json.dump(keys, fh)
    print(f"key list:   {os.path.join(S, 'f2_keys.json')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
