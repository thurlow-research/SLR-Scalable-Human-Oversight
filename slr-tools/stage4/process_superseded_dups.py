#!/usr/bin/env python3
"""Prep every duplicate so Zotero client dedupe can merge each group.

Scope (MODIFIABLE) = items in 01-Dups + 00-Dups + the 6 04-Superceded collections.
Rule: group all dups by normalized TITLE (pulling in any `superseded-by:` keeper
even if it lives in the main corpus), and promote every group to its highest-ranked
item type — journalArticle > conferencePaper > bookSection > preprint. This handles
clean pairs, chains, circular refs, AND untagged dups uniformly.

For each item whose type is changed:
  - add `orig-type:<kebab>` + `orig-date:<parsedDate>` tags (lineage preserved onto
    the surviving keeper when Zotero unions tags on merge)
  - convert its type via Zotero-schema field mapping (unmappable fields -> Extra)
Keepers (already the group's top type) and untagged orphans (no title match) are
left untouched. superseded-by/supersedes tags are NOT altered (merge keeps
collection memberships and unions tags).

Usage:
  python3 process_superseded_dups.py --dry-run
  python3 process_superseded_dups.py --limit 3
  python3 process_superseded_dups.py
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from collections import Counter, defaultdict

KEY = os.environ["ZOTERO_API_KEY"]
LIB = os.environ["ZOTERO_LIBRARY_ID"]
BASE = f"https://api.zotero.org/groups/{LIB}"
H = {"Zotero-API-Key": KEY, "Zotero-API-Version": "3"}
SKIP_TYPES = {"attachment", "note", "annotation"}
PRESERVE = {"itemType", "key", "version", "creators", "tags", "collections",
            "relations", "dateAdded", "dateModified", "extra"}
DUP_COLLECTIONS = ["T6RUELNJ", "BIRBU25N"]   # 01-Dups, 00-Dups
RANK = {"journalArticle": 4, "conferencePaper": 3, "bookSection": 2, "preprint": 1}


def kebab(s):
    return re.sub(r"(?<!^)(?=[A-Z])", "-", s).lower()


def norm_title(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def api(method, path, body=None, headers=None):
    hs = dict(H)
    if headers:
        hs.update(headers)
    data = json.dumps(body).encode() if body is not None else None
    if data:
        hs["Content-Type"] = "application/json"
    req = urllib.request.Request(f"{BASE}{path}", data=data, headers=hs, method=method)
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req) as r:
                raw = r.read()
                return (json.loads(raw) if raw else None), dict(r.headers)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(int(e.headers.get("Retry-After", "3")) + attempt)
                continue
            raise


def get_all(path):
    out, start = [], 0
    while True:
        d, h = api("GET", f"{path}{'&' if '?' in path else '?'}limit=100&start={start}")
        out.extend(d)
        tot = int(h.get("Total-Results", len(out)))
        start += 100
        if start >= tot or not d:
            break
    return out


def load_schema():
    with urllib.request.urlopen("https://api.zotero.org/schema") as r:
        sch = json.load(r)
    fields, base2field, creators, primary = {}, {}, {}, {}
    for it in sch["itemTypes"]:
        t = it["itemType"]
        fmap, b2f = {}, {}
        for f in it.get("fields", []):
            fmap[f["field"]] = f.get("baseField", f["field"])
            b2f[f.get("baseField", f["field"])] = f["field"]
        fields[t], base2field[t] = fmap, b2f
        cts = [c["creatorType"] for c in it.get("creatorTypes", [])]
        creators[t] = set(cts)
        primary[t] = next((c["creatorType"] for c in it.get("creatorTypes", [])
                           if c.get("primary")), cts[0] if cts else "author")
    return fields, base2field, creators, primary


CACHE = {}


def get_item(key):
    if key not in CACHE:
        try:
            obj, _ = api("GET", f"/items/{key}")
            CACHE[key] = obj
        except urllib.error.HTTPError:
            CACHE[key] = None
    return CACHE[key]


def superseded_keys(it):
    return [t["tag"].split(":", 1)[1] for t in it["data"].get("tags", [])
            if t["tag"].startswith("superseded-by:")]


def orig_tags(it):
    d = it["data"]
    out = [f"orig-type:{kebab(d['itemType'])}"]
    date = (it.get("meta", {}).get("parsedDate") or d.get("date") or "").strip()
    if date:
        out.append(f"orig-date:{date}")
    return out


def convert_data(old, target, fields, base2field, creators, primary):
    fmap_old = fields[old["itemType"]]
    b2f_tgt = base2field[target]
    valid_tgt = set(fields[target].keys())
    new, moved = {"itemType": target}, []
    for f, v in old.items():
        if f in PRESERVE or not v:
            continue
        tf = b2f_tgt.get(fmap_old.get(f, f))
        if tf:
            new[tf] = v
        elif f in valid_tgt:
            new[f] = v
        else:
            moved.append((f, v))
    extra = old.get("extra", "")
    if moved:
        extra = (extra + "\n" if extra else "") + "\n".join(f"{f}: {v}" for f, v in moved)
    if extra:
        new["extra"] = extra
    vct, prim = creators[target], primary[target]
    ncre = []
    for c in old.get("creators", []):
        nc = {"creatorType": c.get("creatorType") if c.get("creatorType") in vct else prim}
        if "name" in c:
            nc["name"] = c["name"]
        else:
            nc["firstName"] = c.get("firstName", "")
            nc["lastName"] = c.get("lastName", "")
        ncre.append(nc)
    new["creators"] = ncre
    return new, [f for f, _ in moved]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    fields, base2field, creators, primary = load_schema()

    scols = [c["key"] for c in get_all("/collections")
             if c["data"]["name"] == "04-Superceded"] + DUP_COLLECTIONS
    mod = {}
    for ck in scols:
        for it in get_all(f"/collections/{ck}/items/top"):
            if it["data"].get("itemType") in SKIP_TYPES:
                continue
            mod[it["key"]] = it
            CACHE[it["key"]] = it
    # universe = modifiable + referenced keepers (for grouping/target type)
    universe = dict(mod)
    for it in list(mod.values()):
        for kk in superseded_keys(it):
            ko = get_item(kk)
            if ko and ko["data"].get("itemType") not in SKIP_TYPES:
                universe[kk] = ko

    groups = defaultdict(list)
    for k, it in universe.items():
        groups[norm_title(it["data"].get("title", ""))].append(k)

    target = {}
    for title, keys in groups.items():
        types = [universe[k]["data"]["itemType"] for k in keys]
        target[title] = max(types, key=lambda t: RANK.get(t, 0))

    plans, orphans = [], []
    for k, it in mod.items():
        title = norm_title(it["data"].get("title", ""))
        tt = target[title]
        cur = it["data"]["itemType"]
        grp_size = len(groups[title])
        if cur == tt:
            continue  # already top type / keeper
        if grp_size <= 1 and not superseded_keys(it):
            orphans.append((k, cur))   # no title match, no lineage -> can't safely act
            continue
        plans.append({"key": k, "cur": cur, "target": tt, "it": it})

    print(f"{len(mod)} modifiable dup items; {len(universe)-len(mod)} referenced keepers pulled in.")
    print(f"CONVERT: {len(plans)}   already-top-type: "
          f"{sum(1 for it in mod.values() if it['data']['itemType']==target[norm_title(it['data'].get('title',''))]) }"
          f"   orphans (left): {len(orphans)}")
    print("  conversions:", dict(Counter(f"{p['cur']}->{p['target']}" for p in plans)))
    if orphans:
        print("  orphans (no title match + no superseded-by, untouched):")
        for k, t in orphans[:20]:
            print(f"     {k} [{t}] '{(mod[k]['data'].get('title','') or '')[:50]}'")

    if args.dry_run:
        print("\n(dry-run - no writes)")
        return

    todo = plans[:args.limit] if args.limit else plans
    done = 0
    for p in todo:
        key = p["key"]
        cur, _ = api("GET", f"/items/{key}")
        ver = cur["version"]
        have = {t["tag"] for t in cur["data"].get("tags", [])}
        newtags = cur["data"].get("tags", []) + [{"tag": t} for t in orig_tags(p["it"]) if t not in have]
        new, moved = convert_data(cur["data"], p["target"], fields, base2field, creators, primary)
        new["tags"] = newtags
        new["collections"] = cur["data"].get("collections", [])
        new["relations"] = cur["data"].get("relations", {})
        try:
            api("PUT", f"/items/{key}", new, {"If-Unmodified-Since-Version": str(ver)})
            done += 1
            mv = f" (Extra+={','.join(moved)})" if moved else ""
            print(f"  converted {key} {p['cur']}->{p['target']}{mv}")
        except urllib.error.HTTPError as e:
            print(f"  FAIL {key}: HTTP {e.code} {e.read()[:150]}")
        time.sleep(0.35)
    print(f"\nDone. Converted {done}/{len(todo)}.")


if __name__ == "__main__":
    if not KEY:
        sys.exit("ZOTERO_API_KEY not set")
    main()
