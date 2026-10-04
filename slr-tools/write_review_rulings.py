#!/usr/bin/env python3
"""Write the arbiter's F2-review rulings (slr-phase4/data/f2_review_rulings.json) into Zotero.

endorse -> cal:human:<kind>:<slug>        reject -> cal:human:reject:<kind>:<slug>

ADDITIVE ONLY: never removes a tag. A QA correction keeps the original endorsement and adds the reject
alongside it (§142a precedent) — final:* = modal ∪ endorsements − rejections drops it.

Guards: reads with the RO key, writes with the RW key (least privilege); version-guarded PATCH
(If-Unmodified-Since-Version); re-reads every item after writing and verifies; only entries whose
'written' is null are attempted; on success the ledger entry is stamped with the date.

DRY RUN BY DEFAULT. Pass --commit to write. Back up the library first.
Usage:  python3 slr-tools/write_review_rulings.py [--commit]
"""

from __future__ import annotations

import argparse
import collections
import datetime
import json
import os
import sys
import urllib.error
import urllib.request

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(R, "slr-phase4", "data", "f2_review_rulings.json")
LIB = os.environ.get("ZOTERO_LIBRARY_ID")
LT = os.environ.get("ZOTERO_LIBRARY_TYPE", "group")


def req(key, path, data=None, method="GET", extra=None):
    h = {"Zotero-API-Version": "3", "Authorization": f"Bearer {key}"}
    if data is not None:
        h["Content-Type"] = "application/json"
    h.update(extra or {})
    return urllib.request.urlopen(urllib.request.Request(
        f"https://api.zotero.org/{LT}s/{LIB}{path}", data=data, headers=h, method=method))


def tag_for(r):
    return (f"cal:human:{r['kind']}:{r['slug']}" if r["action"] == "endorse"
            else f"cal:human:reject:{r['kind']}:{r['slug']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--commit", action="store_true")
    a = ap.parse_args()
    ro = os.environ.get("ZOTERO_API_KEY_RO")
    rw = os.environ.get("ZOTERO_API_KEY_RW")
    if a.commit and not rw:
        sys.exit("refusing to --commit without ZOTERO_API_KEY_RW")

    L = json.load(open(LEDGER))
    pending = [r for r in L["rulings"] if not r.get("written")]
    by_item = collections.defaultdict(list)
    for r in pending:
        by_item[r["key"]].append(r)

    plan, already = {}, 0
    for k, rs in by_item.items():
        with req(ro, f"/items/{k}") as resp:
            d = json.load(resp)["data"]
        have = {t["tag"] for t in d["tags"]}
        add = sorted({tag_for(r) for r in rs} - have)
        already += len({tag_for(r) for r in rs} & have)
        plan[k] = (d["version"], d["tags"], add, rs)

    n_add = sum(len(p[2]) for p in plan.values())
    print(f"{len(pending)} pending rulings on {len(plan)} items · {n_add} tags to add · "
          f"{already} already present")
    for k, (_, _, add, rs) in sorted(plan.items(), key=lambda x: x[1][3][0]["author"]):
        if add:
            print(f"   {rs[0]['author']:14s} {k}  + " + ", ".join(add))
    if not a.commit:
        print("\nDRY RUN — nothing written. Re-run with --commit (back up the library first).")
        return 0

    ok = fail = 0
    today = datetime.date.today().isoformat()
    for k, (ver, tags, add, rs) in plan.items():
        try:
            if add:
                body = json.dumps({"tags": tags + [{"tag": t} for t in add]}).encode()
                req(rw, f"/items/{k}", data=body, method="PATCH",
                    extra={"If-Unmodified-Since-Version": str(ver)}).close()
            with req(ro, f"/items/{k}") as resp:
                now = {t["tag"] for t in json.load(resp)["data"]["tags"]}
            if all(tag_for(r) in now for r in rs):
                for r in rs:
                    r["written"] = today
                ok += 1
            else:
                fail += 1
                print(f"   VERIFY FAILED {k}")
        except urllib.error.HTTPError as e:
            fail += 1
            print(f"   HTTP {e.code} on {k} — {e.reason}")
    json.dump(L, open(LEDGER, "w"), indent=1, ensure_ascii=False)
    print(f"\nwritten+verified {ok} items · failed {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
