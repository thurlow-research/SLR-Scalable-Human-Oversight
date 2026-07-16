#!/usr/bin/env python3
"""Change each superseded item's item-type to match its keeper's type.

Scope: items in the 04-Superceded collections that carry an `orig-type:` tag
(added by tag_superseded_orig_type.py). For each, the keeper is resolved from the
`superseded-by:<key>` tag; the item is converted to the keeper's itemType with
proper Zotero base-field mapping (e.g. proceedingsTitle/bookTitle -> publicationTitle).
Any field not valid for the target type is appended to `Extra` (no data loss).
Creators with an invalid creatorType for the target are remapped to its primary.
Tags, collections, and relations are preserved.

Usage:
  python3 convert_superseded_types.py --dry-run
  python3 convert_superseded_types.py --limit 1
  python3 convert_superseded_types.py
"""
import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error

KEY = os.environ["ZOTERO_API_KEY"]
LIB = os.environ["ZOTERO_LIBRARY_ID"]
BASE = f"https://api.zotero.org/groups/{LIB}"
H = {"Zotero-API-Key": KEY, "Zotero-API-Version": "3"}
SKIP_TYPES = {"attachment", "note", "annotation"}
PRESERVE = {"itemType", "key", "version", "creators", "tags", "collections",
            "relations", "dateAdded", "dateModified", "extra"}


def api(method, path, body=None, headers=None, base=BASE):
    hs = dict(H)
    if headers:
        hs.update(headers)
    data = json.dumps(body).encode() if body is not None else None
    if data:
        hs["Content-Type"] = "application/json"
    req = urllib.request.Request(f"{base}{path}", data=data, headers=hs, method=method)
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
    req = urllib.request.Request("https://api.zotero.org/schema")
    with urllib.request.urlopen(req) as r:
        sch = json.load(r)
    fields, base2field, creators, primary = {}, {}, {}, {}
    for it in sch["itemTypes"]:
        t = it["itemType"]
        fmap = {}          # field -> baseField (or itself)
        b2f = {}           # base -> field (for THIS type)
        for f in it.get("fields", []):
            fn = f["field"]
            bf = f.get("baseField", fn)
            fmap[fn] = bf
            b2f[bf] = fn
        fields[t] = fmap
        base2field[t] = b2f
        cts = [c["creatorType"] for c in it.get("creatorTypes", [])]
        creators[t] = set(cts)
        primary[t] = next((c["creatorType"] for c in it.get("creatorTypes", [])
                           if c.get("primary")), cts[0] if cts else "author")
    return fields, base2field, creators, primary


def convert(old, target, ver, fields, base2field, creators, primary):
    oldtype = old["itemType"]
    fmap_old = fields[oldtype]
    b2f_tgt = base2field[target]
    valid_tgt = set(fields[target].keys())
    new = {"itemType": target}
    moved = []
    for f, v in old.items():
        if f in PRESERVE or not v:
            continue
        base = fmap_old.get(f, f)
        tf = b2f_tgt.get(base)
        if tf:
            new[tf] = v
        elif f in valid_tgt:
            new[f] = v
        else:
            moved.append((f, v))
    extra = old.get("extra", "")
    if moved:
        add = "\n".join(f"{f}: {v}" for f, v in moved)
        extra = (extra + "\n" + add) if extra else add
    if extra:
        new["extra"] = extra
    vct, prim = creators[target], primary[target]
    ncre = []
    for c in old.get("creators", []):
        ct = c.get("creatorType")
        nc = {"creatorType": ct if ct in vct else prim}
        if "name" in c:
            nc["name"] = c["name"]
        else:
            nc["firstName"] = c.get("firstName", "")
            nc["lastName"] = c.get("lastName", "")
        ncre.append(nc)
    new["creators"] = ncre
    new["tags"] = old.get("tags", [])
    new["collections"] = old.get("collections", [])
    new["relations"] = old.get("relations", {})
    return new, [f for f, _ in moved]


def keeper_key(tags):
    for t in tags:
        tag = t.get("tag", "")
        if tag.startswith("superseded-by:"):
            return tag.split(":", 1)[1]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    fields, base2field, creators, primary = load_schema()
    scols = [c for c in get_all("/collections") if c["data"]["name"] == "04-Superceded"]
    items = {}
    for c in scols:
        for it in get_all(f"/collections/{c['key']}/items/top"):
            if it["data"].get("itemType") in SKIP_TYPES:
                continue
            items[it["key"]] = it
    # only items we tagged with orig-type
    scoped = [it for it in items.values()
              if any(t.get("tag", "").startswith("orig-type:") for t in it["data"].get("tags", []))]
    print(f"{len(scoped)} orig-type-tagged superseded items in scope.\n")

    plans, skips = [], []
    kcache = {}
    for it in scoped:
        d = it["data"]
        kk = keeper_key(d.get("tags", []))
        if not kk:
            skips.append((it["key"], d["itemType"], "no superseded-by tag"))
            continue
        if kk not in kcache:
            try:
                kobj, _ = api("GET", f"/items/{kk}")
                kcache[kk] = kobj["data"]["itemType"]
            except urllib.error.HTTPError:
                kcache[kk] = None
        ktype = kcache[kk]
        if not ktype:
            skips.append((it["key"], d["itemType"], f"keeper {kk} not found"))
            continue
        if ktype == d["itemType"]:
            skips.append((it["key"], d["itemType"], f"already matches keeper ({ktype})"))
            continue
        plans.append((it, kk, ktype))

    print(f"{len(plans)} to convert, {len(skips)} skipped.")
    for k, t, why in skips:
        print(f"  skip {k} [{t}] — {why}")
    print()
    for it, kk, ktype in plans:
        d = it["data"]
        new, moved = convert(d, ktype, it["version"], fields, base2field, creators, primary)
        mv = f"  (moved to Extra: {', '.join(moved)})" if moved else ""
        print(f"  {it['key']}: {d['itemType']} -> {ktype}  keeper={kk}{mv}")
        print(f"       '{(d.get('title','') or '')[:60]}'")

    if args.dry_run:
        print("\n(dry-run — no writes)")
        return

    todo = plans[:args.limit] if args.limit else plans
    ok = 0
    for it, kk, ktype in todo:
        new, _ = convert(it["data"], ktype, it["version"], fields, base2field, creators, primary)
        try:
            api("PUT", f"/items/{it['key']}", new,
                {"If-Unmodified-Since-Version": str(it["version"])})
            ok += 1
            print(f"  converted {it['key']} -> {ktype}")
        except urllib.error.HTTPError as e:
            print(f"  FAIL {it['key']}: HTTP {e.code} {e.read()[:200]}")
        time.sleep(0.4)
    print(f"\nDone. Converted {ok}/{len(todo)}.")


if __name__ == "__main__":
    if not KEY:
        sys.exit("ZOTERO_API_KEY not set")
    main()
