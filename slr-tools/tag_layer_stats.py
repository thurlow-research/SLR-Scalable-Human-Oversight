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
# NOTE (2026-08-28): the merged "04 - Calibration (Adjudicated)" collection [46QVUN7N] is NOT
# Set A u Set B -- it drops Momcilovic (M74M3RFJ, Set A) and adds Otten (ZUM76CCG, a Set C pilot
# paper). It is also mislabelled "blind-first": only Set B was tagged blind. Using it produced an
# uninterpretable blended figure. Always use the two source collections, split.
BANDS = {
    "UIN658B7": "01 Accept",
    "WTKULZ5U": "02 Light Read",
    "2WE2DX36": "03 Full Read",
    "JFN8693L": "04a Calibration Set A (model-first)",
    "IURU9UTA": "04b Calibration Set B (BLIND)",
}
# Only Set B is the anchoring control: the arbiter tagged it without seeing any model proposal.
# Set A was tagged with model tags present (blind first read + model-aware adjudication, §34).
BLIND_BAND = "IURU9UTA"
MERGED_CALIBRATION_DO_NOT_USE = "46QVUN7N"

MODELS = ("opus", "codex", "gemini", "fable")

# Anchored at ^cal: so SUPERSEDED runs renamed with a version prefix (e.g. v1_cal:opus:...)
# fall outside and are ignored automatically. Do not relax this anchor.
TAG_RE = re.compile(r"^cal:(\w+):(?:primary:)?(theme|facet):([a-z0-9-]+)$")
SUPERSEDED_RE = re.compile(r"^v\d+_cal:")
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


def split_layers(data: dict) -> dict:
    """Decompose one item's tag layers.

    Returns a dict so callers cannot silently mis-order the tuple, and so new
    signals (primary, demote, superseded) can be added without breaking callers.
    """
    votes: collections.Counter = collections.Counter()
    human, reject = set(), set()
    primary = None
    demoted = False
    superseded = 0
    for entry in data.get("tags", []):
        tag = entry["tag"]
        if SUPERSEDED_RE.match(tag):
            superseded += 1          # a prior instrument version, deliberately excluded
            continue
        if tag.startswith("demote:"):
            demoted = True
            continue
        m = TAG_RE.match(tag)
        if m:
            who, kind, slug = m.groups()
            if who == "human":
                human.add((kind, slug))
                if ":primary:" in tag:
                    primary = slug
            elif who in MODELS:
                votes[(kind, slug)] += 1
        m2 = REJECT_RE.match(tag)
        if m2:
            reject.add((m2.group(1), m2.group(2)))
    return {"votes": votes, "human": human, "reject": reject,
            "primary": primary, "demoted": demoted, "superseded": superseded}


def measure(items: dict, frozen: set) -> dict:
    """Origination, three-state and TIER figures for one band.

    Completeness predicate is a PRIMARY theme (or an explicit demote), not "any
    cal:human tag" -- a targeted single-axis write leaves a human tag behind
    without an adjudication, and the loose predicate counted those as done.
    """
    endorsed = originated = rejected = 0
    orig_reachable = 0            # arbiter added a tag the panel COULD have proposed
    orig_by_slug: collections.Counter = collections.Counter()
    modal_total = modal_end = modal_rej = modal_silent = 0
    nonmodal_endorsed = 0
    papers = partial = untouched = 0
    demoted = 0
    superseded_tags = 0
    # tier axis: the panel proposes demotes via flags that never reach Zotero, so
    # tier agreement is measured against the human demote tag only.
    tier_human_demote = 0

    for data in items.values():
        L = split_layers(data)
        superseded_tags += L["superseded"]
        adjudicated = L["primary"] is not None or L["demoted"]
        if not adjudicated:
            if L["human"] or L["reject"]:
                partial += 1       # tagged on one axis, never given a primary
            else:
                untouched += 1
            continue
        papers += 1
        if L["demoted"]:
            demoted += 1
            tier_human_demote += 1

        votes, human, reject = L["votes"], L["human"], L["reject"]
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
        "papers_adjudicated": papers,
        "papers_partial": partial,
        "papers_untouched": untouched,
        "papers_demoted": demoted,
        "surviving": papers - demoted,
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
        "superseded_tags_ignored": superseded_tags,
        "originations_by_slug": dict(orig_by_slug.most_common()),
    }


def instrument_check(items: dict, band: str, version_dir: str = "slr-phase4/data/tags-v213") -> dict:
    """Do this band's Zotero model tags match the CURRENT instrument's JSON?

    Guards the trap that produced the bogus 80.9% origination figure: Set A's
    Zotero layer still holds the v1 panel run, so any statistic computed from it
    compares a v1 panel against a v2.13-aligned human layer. A high mismatch rate
    means the band has not been written back from the current run.
    """
    checked = match = missing = 0
    for key, data in items.items():
        path = os.path.join(version_dir, "opus", f"{key}.json")
        if not os.path.exists(path):
            missing += 1
            continue
        with open(path) as fh:
            j = json.load(fh)
        expect = {("theme", t) for t in j.get("themes", [])} | \
                 {("facet", f) for f in j.get("facets", [])}
        got = set()
        for entry in data.get("tags", []):
            m = TAG_RE.match(entry["tag"])
            if m and m.group(1) == "opus":
                got.add((m.group(2), m.group(3)))
        if not got:
            continue
        checked += 1
        if got == expect:
            match += 1
    rate = round(match / checked * 100, 1) if checked else None
    return {"band": band, "items_checked": checked, "matching_current_instrument": match,
            "match_pct": rate, "no_json_on_disk": missing,
            "WARNING": (None if (rate is None or rate >= 50)
                        else "Zotero model layer does NOT match the current instrument -- "
                             "likely a superseded run not yet written back. Figures for this "
                             "band are NOT comparable to the others.")}


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

    checks = []
    for key, name in BANDS.items():
        items = fetch_band(library, lib_type, key, api_key)
        bands[name] = measure(items, frozen)
        bands[name]["items_in_band"] = len(items)
        checks.append(instrument_check(items, name))
        for data in items.values():
            L = split_layers(data)
            for kind, slug in set(L["votes"]) | L["human"] | L["reject"]:
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
        "instrument_checks": checks,
        "control": {
            "blind_band": BANDS[BLIND_BAND],
            "comparison": ("Set A vs Set B is the ONLY clean anchoring contrast: same "
                           "arbiter, same instrument, same exhaustive protocol, same era, "
                           "differing solely in whether model tags were visible. Compare "
                           "those two to each other -- NOT either to a supervised band."),
            "why_not_supervised_bands": ("Light Read is confounded three ways: it was "
                                         "deliberately non-exhaustive, the vocabulary grew "
                                         "under it, and the confirmation protocol drifted "
                                         "mid-band from a subset to all tags."),
            "merged_collection_not_used": MERGED_CALIBRATION_DO_NOT_USE,
        },
        "caveats": [
            "Silence over a modal proposal means 'scanned, nothing worth discussing' in "
            "bands that received a pass, and 'never examined' in partially-tagged papers. "
            "papers_partial is reported separately so the two are not conflated.",
            "Completeness = a PRIMARY theme or an explicit demote. 'Any cal:human tag' "
            "counts targeted single-axis writes as adjudicated and overstates coverage.",
            "Check instrument_checks before comparing bands: a band whose Zotero model "
            "layer predates the current instrument is not comparable to one that does not.",
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
        if not b["papers_adjudicated"]:
            continue
        print(f"  {name:36s} n={b['papers_adjudicated']:3d} "
              f"(surv {b['surviving']:3d} / dem {b['papers_demoted']:3d} / "
              f"part {b['papers_partial']:2d} / untouched {b['papers_untouched']:2d})  "
              f"orig {b['origination_pct'] or 0:5.1f}%  "
              f"override {b['override_rate_pct'] or 0:5.1f}%")
    for c in checks:
        if c.get("WARNING"):
            print(f"  !! {c['band']}: {c['match_pct']}% match to current instrument -- {c['WARNING']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
