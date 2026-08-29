#!/usr/bin/env python3
"""Supersede a model run on a set of items: RENAME the old tags, write the new ones.

Implements the rule in `Methodology/SLR_Methodology_Bootstrap.md` §3:

    Superseded MODEL RUNS are provenance too -- NEVER delete them.
    Rename, don't remove: prefix superseded tags with the INSTRUMENT VERSION that
    produced them (cal:opus:theme:X -> v1_cal:opus:theme:X), then write the new
    run in the bare cal: form.

The prefix names the *instrument version*, not an ordinal -- ordinals break at the
second supersession (a second superseded run would be "v2_", colliding with
instrument v2.13). Superseding the current run later gives `v213_cal:...`.

Why a dedicated tool: the Zotero CLI has `tag-add` but no rename and no remove, so
this needs a version-guarded PATCH of the whole tags array. The same operation
recurs at EVERY future instrument revision.

Guarantees:
  * cal:human:* is never touched -- human decisions are not a model run.
  * Already-prefixed tags are left alone (idempotent; safe to re-run).
  * Refuses to write if the new run's JSON is missing for any item, so a partial
    write cannot leave a band half-superseded.
  * If-Unmodified-Since-Version on every PATCH; a concurrent edit aborts the item.

DRY RUN BY DEFAULT. Pass --commit to write. Back up the library first.

Usage:
    python3 slr-tools/supersede_model_run.py --collection JFN8693L \
        --prefix v1 --new-run slr-phase4/data/tags-v213
    python3 slr-tools/supersede_model_run.py --collection JFN8693L \
        --prefix v1 --new-run slr-phase4/data/tags-v213 --commit
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

API = "https://api.zotero.org"
MODELS = ("opus", "codex", "gemini", "fable")   # vendors we WRITE; renaming is not limited to these
# Vendor may contain hyphens (e.g. "gemini-fast", a vendor from an early run).
# A (\w+) class silently misses those, leaving them in the bare cal: namespace while
# their siblings get prefixed -- a mixed-instrument record, which is the exact
# corruption this tool exists to prevent.
CAL_RE = re.compile(r"^cal:([\w.-]+):(?:primary:)?(theme|facet):[a-z0-9-]+$")
PREFIXED_RE = re.compile(r"^v\d+_cal:")


def _req(cfg, path, data=None, method="GET", extra_headers=None):
    headers = {"Zotero-API-Version": "3", "Authorization": f"Bearer {cfg['key']}"}
    if data is not None:
        headers["Content-Type"] = "application/json"
    headers.update(extra_headers or {})
    url = f"{API}/{cfg['lib_type']}s/{cfg['library']}{path}"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    return urllib.request.urlopen(req)


def fetch_collection(cfg, key):
    items, start = {}, 0
    while True:
        with _req(cfg, f"/collections/{key}/items/top?limit=100&start={start}") as r:
            page = json.load(r)
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


def new_run_tags(run_dir: str, item_key: str, vendors: tuple) -> tuple[list[str], list[str]]:
    """(tags to write, vendors found) for one item from the new run's JSON."""
    tags, found = [], []
    for vendor in vendors:
        path = os.path.join(run_dir, vendor, f"{item_key}.json")
        if not os.path.exists(path):
            continue
        with open(path) as fh:
            d = json.load(fh)
        found.append(vendor)
        primary = d.get("primary_theme")
        if primary:
            tags.append(f"cal:{vendor}:primary:theme:{primary}")
        for t in d.get("themes", []):
            tags.append(f"cal:{vendor}:theme:{t}")
        for f in d.get("facets", []):
            tags.append(f"cal:{vendor}:facet:{f}")
    return sorted(set(tags)), found


def plan_item(data: dict, prefix: str, run_dir: str, vendors: tuple) -> dict:
    key = data["key"]
    existing = [t["tag"] for t in data.get("tags", [])]
    renames, keeps, already = [], [], []
    for tag in existing:
        if PREFIXED_RE.match(tag):
            already.append(tag)
            keeps.append(tag)
            continue
        m = CAL_RE.match(tag)
        # Supersede EVERY non-human vendor, not a fixed allow-list: an unrecognised
        # vendor from an old run must still be carried out of the live namespace.
        if m and m.group(1) != "human":
            renames.append((tag, f"{prefix}_{tag}"))
        else:                                    # cal:human:*, demote:*, source:*, ...
            keeps.append(tag)
    additions, found = new_run_tags(run_dir, key, vendors)
    final = sorted(set(keeps + [new for _, new in renames] + additions))
    return {"key": key, "version": data["version"], "renames": renames,
            "additions": additions, "vendors": found, "already_prefixed": already,
            "final_tags": final, "n_before": len(existing), "n_after": len(final)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--collection", required=True, help="collection key to operate on")
    ap.add_argument("--prefix", required=True,
                    help="instrument version that produced the OLD tags, e.g. v1")
    ap.add_argument("--new-run", required=True,
                    help="directory holding the new run, with <vendor>/<itemKey>.json")
    ap.add_argument("--vendors", default="opus,codex,gemini",
                    help="vendors to WRITE from the new run (default: the uniform 3). "
                         "fable is excluded by default -- panel composition must be uniform "
                         "across the corpus, and fable covers only part of it.")
    ap.add_argument("--commit", action="store_true", help="actually write (default: dry run)")
    args = ap.parse_args()

    if not re.fullmatch(r"v\d+", args.prefix):
        print(f"--prefix must look like v1 / v213 (got {args.prefix!r})", file=sys.stderr)
        return 2

    key = os.environ.get("ZOTERO_API_KEY_RW") or os.environ.get("ZOTERO_API_KEY")
    if args.commit and not os.environ.get("ZOTERO_API_KEY_RW"):
        print("refusing to --commit without ZOTERO_API_KEY_RW (least privilege)", file=sys.stderr)
        return 2
    cfg = {"key": key,
           "library": os.environ.get("ZOTERO_LIBRARY_ID"),
           "lib_type": os.environ.get("ZOTERO_LIBRARY_TYPE", "group")}
    if not cfg["key"] or not cfg["library"]:
        print("need ZOTERO_API_KEY(_RW) and ZOTERO_LIBRARY_ID", file=sys.stderr)
        return 2

    vendors = tuple(v.strip() for v in args.vendors.split(",") if v.strip())
    items = fetch_collection(cfg, args.collection)
    plans = [plan_item(d, args.prefix, args.new_run, vendors) for d in items.values()]

    # Non-uniform coverage silently corrupts a band: one item on a 4-vendor panel
    # and the rest on 3 makes modal thresholds mean different things per paper.
    coverage = {p["key"]: set(p["vendors"]) for p in plans}
    shapes = {frozenset(v) for v in coverage.values()}
    if len(shapes) > 1:
        print(f"ABORT: vendor coverage is NOT uniform across the band: "
              f"{ {k: sorted(v) for k, v in coverage.items()} }", file=sys.stderr)
        print("Narrow --vendors so every item has the same panel.", file=sys.stderr)
        return 1

    missing = [p["key"] for p in plans if not p["vendors"]]
    if missing:
        print(f"ABORT: no new-run JSON for {len(missing)} item(s): {missing}", file=sys.stderr)
        print("Refusing to half-supersede a band.", file=sys.stderr)
        return 1

    print(f"collection {args.collection}: {len(plans)} items · new run {args.new_run}")
    print(f"old tags will be prefixed '{args.prefix}_'  ·  writing vendors: {','.join(vendors)}\n")
    tot_r = tot_a = 0
    for p in sorted(plans, key=lambda x: x["key"]):
        tot_r += len(p["renames"]); tot_a += len(p["additions"])
        note = "  (already prefixed - idempotent)" if p["already_prefixed"] else ""
        print(f"  {p['key']}  rename {len(p['renames']):3d}  add {len(p['additions']):3d}  "
              f"vendors {','.join(p['vendors'])}  tags {p['n_before']}->{p['n_after']}{note}")
    print(f"\nTOTAL  rename {tot_r}  add {tot_a}")
    if plans:
        s = sorted(plans, key=lambda x: x["key"])[0]
        print(f"\nsample ({s['key']}):")
        for old, new in s["renames"][:3]:
            print(f"    {old}\n      -> {new}")
        for a in s["additions"][:3]:
            print(f"    + {a}")

    if not args.commit:
        print("\nDRY RUN — nothing written. Re-run with --commit (back up the library first).")
        return 0

    ok = fail = 0
    for p in plans:
        body = json.dumps({"tags": [{"tag": t} for t in p["final_tags"]]}).encode()
        try:
            _req(cfg, f"/items/{p['key']}", data=body, method="PATCH",
                 extra_headers={"If-Unmodified-Since-Version": str(p["version"])})
            ok += 1
        except urllib.error.HTTPError as e:
            fail += 1
            print(f"  FAIL {p['key']}: HTTP {e.code} {e.reason}", file=sys.stderr)
    print(f"\nwritten {ok}, failed {fail}")
    return 0 if not fail else 1


if __name__ == "__main__":
    raise SystemExit(main())
