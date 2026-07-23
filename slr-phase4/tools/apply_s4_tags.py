#!/usr/bin/env python3
"""Apply s4: machine-proposal tags to Zotero items (group 6505702).

Namespace-owned merge: the s4:* tag family is machine-owned — existing s4:* tags
on the item are replaced by the new proposal set; every other tag (human cal:*,
lineage s1/s2/s3, theme:/facet slugs) is left untouched. Never replace-mode
(write_tags.py is legacy for a reason).

Dry-run by default; --commit performs the write (RW key). Reads use RO key.
Standing rule: library backup before any --commit session.
"""
import argparse, json, os, pathlib, sys, time
import urllib.request

GROUP = "6505702"
API = f"https://api.zotero.org/groups/{GROUP}/items"


def req(url, key, method="GET", body=None, headers=None):
    h = {"Zotero-API-Key": key, "Zotero-API-Version": "3"}
    h.update(headers or {})
    r = urllib.request.Request(url, method=method, headers=h,
                               data=json.dumps(body).encode() if body is not None else None)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(r) as resp:
                return resp.status, resp.headers, resp.read()
        except urllib.error.HTTPError as e:
            if e.code in (502, 503) and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError("unreachable")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tagfile", help="JSON {itemKey: [s4: tags]} from triage --emit-tags")
    ap.add_argument("--commit", action="store_true", help="actually write (default: dry-run)")
    a = ap.parse_args()

    ro = os.environ.get("ZOTERO_API_KEY_RO") or os.environ.get("ZOTERO_API_KEY")
    rw = os.environ.get("ZOTERO_API_KEY_RW") or os.environ.get("ZOTERO_API_KEY")
    if not ro or (a.commit and not rw):
        sys.exit("missing ZOTERO_API_KEY_RO/RW (source .envrc)")

    payload = json.loads(pathlib.Path(a.tagfile).read_text())
    for key, new_s4 in payload.items():
        bad = [t for t in new_s4 if not t.startswith("s4:")]
        if bad:
            sys.exit(f"{key}: refusing non-s4 tags {bad}")
        _, headers, body = req(f"{API}/{key}", ro)
        item = json.loads(body)
        version = item["version"]
        current = [t["tag"] for t in item["data"]["tags"]]
        kept = [t for t in current if not t.startswith("s4:")]
        dropped = [t for t in current if t.startswith("s4:") and t not in new_s4]
        added = [t for t in new_s4 if t not in current]
        final = kept + list(new_s4)
        print(f"{key} (v{version}): +{len(added)} -{len(dropped)} "
              f"| add {added or '[]'} | drop {dropped or '[]'} | untouched non-s4: {len(kept)}")
        if not a.commit:
            continue
        status, _, _ = req(
            f"{API}/{key}", rw, method="PATCH",
            body={"tags": [{"tag": t} for t in final]},
            headers={"If-Unmodified-Since-Version": str(version),
                     "Content-Type": "application/json"})
        print(f"  PATCH -> {status}")
    if not a.commit:
        print("dry-run only; re-run with --commit to write")


if __name__ == "__main__":
    main()
