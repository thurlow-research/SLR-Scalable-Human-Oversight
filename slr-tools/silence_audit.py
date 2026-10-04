#!/usr/bin/env python3
"""Split the arbiter's silence by what it means, and list the implicitly confirmed set.

Silence over a panel-modal proposal (>=2 of 3 vendors) means different things by context
(Taxonomy_Changelog.md §150; Post_Accept_Closeout.md C4):

  * surviving paper -> IMPLICITLY CONFIRMED. Early Light Read worked by scanning the full list and
                       querying only doubtful tags; later papers were confirmed tag by tag, so on those
                       silence does not occur.
  * demoted paper   -> UNVERIFIED. §42: a demote short-circuits tag verification (no consumer).

Production bands only (Light Read, Accept, Full Read). Frozen v2.13 vocabulary only, so proposals
written by the F2 restricted re-run (2026-08-30 on) do not leak in. Reads the live library with the
RO key; writes nothing.

Usage:  python3 slr-tools/silence_audit.py [--list]
"""

from __future__ import annotations

import argparse
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tag_layer_stats as T  # noqa: E402

BANDS = {"WTKULZ5U": "Light Read", "UIN658B7": "Accept", "2WE2DX36": "Full Read"}
DEPRECATED = {"counterpoint"}          # §56; removed by closeout sweep B3, not by confirmation
VENDOR_RE = re.compile(r"^cal:(opus|codex|gemini):(?:primary:)?(theme|facet):([a-z0-9-]+)$")


def vendors(data, kind, slug):
    return sorted({m.group(1) for t in data["tags"]
                   if (m := VENDOR_RE.match(t["tag"])) and m.group(2) == kind and m.group(3) == slug})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="print the implicitly confirmed set")
    a = ap.parse_args()
    lib, key = os.environ["ZOTERO_LIBRARY_ID"], os.environ["ZOTERO_API_KEY_RO"]
    frozen = set(T.FROZEN_THEMES) | set(T.FROZEN_FACETS)

    c = collections.Counter()
    implicit = []
    for coll, band in BANDS.items():
        for k, d in T.fetch_band(lib, "group", coll, key).items():
            L = T.split_layers(d)
            cat = "demoted" if L["demoted"] else "surviving"
            modal = {x for x, v in L["votes"].items() if v >= 2 and x[1] in frozen}
            silent = modal - L["human"] - L["reject"]
            c[cat, "papers"] += 1
            c[cat, "modal"] += len(modal)
            c[cat, "endorsed"] += len(modal & L["human"])
            c[cat, "rejected"] += len(modal & L["reject"])
            c[cat, "silent"] += len(silent)
            if cat == "surviving":
                for kind, slug in sorted(silent):
                    implicit.append((band, k, (d.get("creators") or [{}])[0].get("lastName", "?"),
                                     d.get("title", ""), L["primary"], kind, slug, vendors(d, kind, slug)))

    print(f"{'':10s} {'papers':>6s} {'modal':>6s} {'endorsed':>14s} {'rejected':>12s} {'silent':>13s}")
    for cat in ("surviving", "demoted"):
        m = c[cat, "modal"] or 1
        print(f"{cat:10s} {c[cat, 'papers']:6d} {c[cat, 'modal']:6d} "
              f"{c[cat, 'endorsed']:5d} ({c[cat, 'endorsed'] / m:5.1%}) "
              f"{c[cat, 'rejected']:4d} ({c[cat, 'rejected'] / m:5.1%}) "
              f"{c[cat, 'silent']:4d} ({c[cat, 'silent'] / m:5.1%})")
    live = [r for r in implicit if r[6] not in DEPRECATED]
    print(f"\nimplicitly confirmed: {len(implicit)} tags on {len({r[1] for r in implicit})} papers; "
          f"{len(implicit) - len(live)} deprecated (B3 sweep) -> "
          f"{len(live)} to confirm on {len({r[1] for r in live})} papers")
    if a.list:
        for band, k, au, title, prim, kind, slug, v in live:
            print(f"  {band:10s} {k} {au:12s} primary={prim or '-':26s} {kind:5s} {slug:26s} {len(v)}/3 {','.join(v)}"
                  f"  | {title[:70]}")


if __name__ == "__main__":
    main()
