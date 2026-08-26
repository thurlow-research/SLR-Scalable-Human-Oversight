#!/usr/bin/env python3
"""Measure the human arbitration layer against the machine panel layer.

Produces the numbers §11 of Methodology/Theme_Tagging_Calibration.md reports:

  * the live tag vocabulary, and how it differs from the frozen v2.13 instrument
  * how often the arbiter ORIGINATED a tag no model proposed (the anchoring measure)
  * the three-state distribution over panel-modal proposals (endorse / reject / silent)

Run it at each measurement point and keep the JSON:

    T0  now, frozen instrument                     (baseline)
    T1  Light Read + Accept closed, still frozen
    T2  after the restricted re-run on the revised instrument

T1 -> T2 is the interesting comparison: if origination on the post-freeze slugs
collapses, the gap was the instrument rather than the panel.

Usage:
    python3 slr-tools/tag_layer_stats.py --label T0 --out slr-phase4/data/tags-v213/
    python3 slr-tools/tag_layer_stats.py --label T0 --date 2026-08-26   # reproducible stamp
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys
import urllib.request

API = "https://api.zotero.org"

# Phase 5 reading bands. The calibration band tagged blind-first, which makes it
# the control for the anchoring measurement -- same arbiter, same instrument,
# proposals not visible.
BANDS = {
    "WTKULZ5U": "02 Light Read",
    "2WE2DX36": "03 Full Read",
    "UIN658B7": "01 Accept",
    "46QVUN7N": "04 Calibration (blind-first)",
}
BLIND_FIRST = "46QVUN7N"

MODELS = ("opus", "codex", "gemini", "fable")

TAG_RE = re.compile(r"^cal:(\w+):(?:primary:)?(theme|facet):([a-z0-9-]+)$")
REJECT_RE = re.compile(r"^cal:human:reject:(theme|facet):([a-z0-9-]+)$")

# The frozen v2.13 instrument -- what the panel actually ran on. Anything the
# arbiter used beyond this list was unreachable by the models by construction.
FROZEN_THEMES = [
    "oversight-scaling-inversion", "ai-code-insecurity", "quality-debt",
    "automation-bias", "oversight-theater", "ai-review", "rules-based-checks",
    "formal-methods", "risk-routing", "remediation-gating", "hitl-workflow",
    "oversight-explanation", "agent-scope-drift", "org-governance",
    "regulatory-compliance", "tooling-supply-chain", "provenance-auditability",
]
FROZEN_FACETS = [
    "problem-statement-anchor", "survey-input", "intro-framing", "lit-review",
    "counterpoint", "framework", "design-only", "expert-validated",
    "built-system", "adopted", "assistive", "agentic", "general-ai", "steering",
    "metrics", "routing-signal", "non-developer", "general-code",
    "risk-security", "risk-quality", "risk-overreliance", "risk-ip", "risk-bias",
    "method-self-report", "method-mining", "method-experiment",
    "method-field-study",
]


def fetch_band(library: str, lib_type: str, key: str, api_key: str) -> dict:
    """All top-level items in one collection, keyed by item key."""
    items, start = {}, 0
    while True:
        url = (f"{API}/{lib_type}s/{library}/collections/{key}/items/top"
               f"?limit=100&start={start}")
        req = urllib.request.Request(url, headers={
            "Zotero-API-Version": "3",
            "Authorization": f"Bearer {api_key}",
        })
        with urllib.request.urlopen(req) as resp:
            page = json.load(resp)
        if not page:
            break
        for it in page:
            d = it["data"]
            if d["itemType"] in ("attachment", "note"):
                continue
            items[d["key"]] = d
        if len(page) < 100:
            break
        start += 100
    return items


def split_layers(data: dict) -> tuple[dict, set, set]:
    """(model votes per tag, human endorsements, human rejections) for one item."""
    votes: collections.Counter = collections.Counter()
    human, reject = set(), set()
    for entry in data.get("tags", []):
        tag = entry["tag"]
        m = TAG_RE.match(tag)
        if m:
            who, kind, slug = m.groups()
            if who == "human":
                human.add((kind, slug))
            elif who in MODELS:
                votes[(kind, slug)] += 1
        m2 = REJECT_RE.match(tag)
        if m2:
            reject.add((m2.group(1), m2.group(2)))
    return votes, human, reject


def measure(items: dict, frozen: set) -> dict:
    """Origination and three-state figures for one band."""
    endorsed = originated = rejected = 0
    orig_reachable = 0            # arbiter added a tag the panel COULD have proposed
    orig_by_slug: collections.Counter = collections.Counter()
    modal_total = modal_end = modal_rej = modal_silent = 0
    nonmodal_endorsed = 0
    papers = 0

    for data in items.values():
        votes, human, reject = split_layers(data)
        if not human and not reject:
            continue                       # no arbiter layer yet
        papers += 1
        proposed = set(votes)

        endorsed += len(human & proposed)
        rejected += len(reject)
        for kind, slug in human - proposed:
            originated += 1
            orig_by_slug[slug] += 1
            if slug in frozen:
                orig_reachable += 1

        modal = {k for k, v in votes.items() if v >= 2}
        modal_total += len(modal)
        modal_end += len(modal & human)
        modal_rej += len(modal & reject)
        modal_silent += len(modal - human - reject)
        nonmodal_endorsed += len((human - modal) & proposed)

    written = endorsed + originated
    pct = lambda n, d: round(n / d * 100, 1) if d else None
    return {
        "papers_with_arbiter_layer": papers,
        "human_tags_written": written,
        "endorsements": endorsed,
        "originations": originated,
        "origination_pct": pct(originated, written),
        # Originations of tags that existed in the frozen instrument. The rest
        # were unreachable -- the panel had no vocabulary for them.
        "originations_reachable": orig_reachable,
        "origination_pct_reachable_only": pct(orig_reachable, written),
        "rejections": rejected,
        "panel_modal_proposals": modal_total,
        "modal_endorsed": modal_end,
        "modal_rejected": modal_rej,
        "modal_silent": modal_silent,
        "override_rate_pct": pct(modal_rej, modal_total),
        "nonmodal_endorsed": nonmodal_endorsed,
        "originations_by_slug": dict(orig_by_slug.most_common()),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--label", required=True, help="measurement point, e.g. T0")
    ap.add_argument("--date", required=True, help="YYYY-MM-DD stamp for the filename")
    ap.add_argument("--out", default="slr-phase4/data/tags-v213",
                    help="directory to write the snapshot into")
    ap.add_argument("--note", default="", help="one line on what this point captures")
    args = ap.parse_args()

    api_key = os.environ.get("ZOTERO_API_KEY_RO") or os.environ.get("ZOTERO_API_KEY")
    library = os.environ.get("ZOTERO_LIBRARY_ID")
    lib_type = os.environ.get("ZOTERO_LIBRARY_TYPE", "group")
    if not api_key or not library:
        print("need ZOTERO_API_KEY(_RO) and ZOTERO_LIBRARY_ID in the environment",
              file=sys.stderr)
        return 2

    frozen = set(FROZEN_THEMES) | set(FROZEN_FACETS)
    bands, live_theme, live_facet = {}, set(), set()

    for key, name in BANDS.items():
        items = fetch_band(library, lib_type, key, api_key)
        bands[name] = measure(items, frozen)
        bands[name]["items_in_band"] = len(items)
        for data in items.values():
            votes, human, reject = split_layers(data)
            for kind, slug in set(votes) | human | reject:
                (live_theme if kind == "theme" else live_facet).add(slug)

    snapshot = {
        "label": args.label,
        "date": args.date,
        "note": args.note,
        "instrument": {
            "frozen_version": "v2.13",
            "frozen_themes": len(FROZEN_THEMES),
            "frozen_facets": len(FROZEN_FACETS),
            "frozen_total": len(frozen),
            "live_themes": len(live_theme),
            "live_facets": len(live_facet),
            "live_total": len(live_theme) + len(live_facet),
            # Vocabulary the arbiter used that the frozen panel could not propose.
            "post_freeze_themes": sorted(live_theme - set(FROZEN_THEMES)),
            "post_freeze_facets": sorted(live_facet - set(FROZEN_FACETS)),
            "frozen_but_never_used": sorted(frozen - live_theme - live_facet),
        },
        "bands": bands,
        "control": {
            "blind_first_band": BANDS[BLIND_FIRST],
            "comment": ("The calibration band tagged blind-first, so its origination "
                        "rate is the no-anchor baseline. Directional only: that pass "
                        "was an exhaustive coding, while the supervised bands are "
                        "deliberately non-exhaustive (silence = not considered)."),
        },
        "caveats": [
            "'Originated' means absent from every model's MODAL set; only modal tags "
            "are written to Zotero, so a 1-of-3-run proposal counts as originated. "
            "Origination is therefore an upper bound.",
            "The vocabulary was co-authored with the arbiter, so panel recall is "
            "measured against a shared instrument, not independent ground truth.",
            "The human is the criterion, so these figures cannot estimate human error. "
            "Only the blind-first Set B design speaks to that.",
        ],
    }

    os.makedirs(args.out, exist_ok=True)
    path = os.path.join(args.out, f"tag_layer_stats_{args.label}_{args.date}.json")
    with open(path, "w") as fh:
        json.dump(snapshot, fh, indent=2)
        fh.write("\n")

    inst = snapshot["instrument"]
    print(f"wrote {path}")
    print(f"  instrument: frozen {inst['frozen_total']} -> live {inst['live_total']}")
    for name, b in bands.items():
        if not b["papers_with_arbiter_layer"]:
            continue
        print(f"  {name:30s} n={b['papers_with_arbiter_layer']:3d} "
              f"originated {b['origination_pct']:5.1f}% "
              f"override {b['override_rate_pct'] or 0:5.1f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
