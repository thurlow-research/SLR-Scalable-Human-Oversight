#!/usr/bin/env python3
"""Write per-model cal:<model>:* tags to all 128 sweep items in Zotero.

Per model (opus/codex/gemini), computes the MODAL primary/themes/facets across
that model's available runs (base + r2/r3 replication runs where they exist) —
a tag counts if asserted in >=50% of that model's runs for the paper. Additive
write (never removes existing tags); processes in batches, verifies each item
against the API immediately after writing, logs everything.

Usage: write_sweep_model_tags.py [--batch-size N] [--limit N] [--start-at KEY]
"""
import json, os, sys, glob, time, argparse, urllib.request, urllib.error
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HERE, "..", "data", "tags-v213")
MODELS = ["opus", "codex", "gemini"]
LIB_ID = "6505702"
RO_KEY = os.environ.get("ZOTERO_API_KEY_RO") or os.environ["ZOTERO_API_KEY"]
RW_KEY = os.environ.get("ZOTERO_API_KEY_RW") or os.environ["ZOTERO_API_KEY"]


def load_runs(model, key):
    base = os.path.join(DATA_DIR, model)
    files = sorted(glob.glob(os.path.join(base, f"{key}.json"))) + \
            sorted(glob.glob(os.path.join(base, f"{key}.r*.json")))
    files = [f for f in files if not f.endswith(".meta.json")]
    runs = []
    for f in files:
        try:
            runs.append(json.load(open(f)))
        except Exception as e:
            print(f"WARN: failed to parse {f}: {e}", file=sys.stderr)
    return runs


def modal_set(runs, field):
    n = len(runs)
    if n == 0:
        return []
    counts = Counter()
    for r in runs:
        for v in r.get(field) or []:
            counts[v] += 1
    threshold = n / 2.0
    return sorted([v for v, c in counts.items() if c >= threshold])


def modal_primary(runs):
    if not runs:
        return None
    counts = Counter(r.get("primary_theme") for r in runs if r.get("primary_theme"))
    if not counts:
        return None
    top = counts.most_common()
    maxcount = top[0][1]
    tied = [v for v, c in top if c == maxcount]
    if len(tied) == 1:
        return tied[0]
    r1_primary = runs[0].get("primary_theme")
    return r1_primary if r1_primary in tied else tied[0]


def build_tags_for_model(model, key):
    runs = load_runs(model, key)
    if not runs:
        return []
    primary = modal_primary(runs)
    themes = modal_set(runs, "themes")
    facets = modal_set(runs, "facets")
    tags = []
    if primary:
        tags.append(f"cal:{model}:primary:theme:{primary}")
    for t in themes:
        tags.append(f"cal:{model}:theme:{t}")
    for f in facets:
        tags.append(f"cal:{model}:facet:{f}")
    return tags


def build_tags_for_key(key):
    tags = []
    for model in MODELS:
        tags.extend(build_tags_for_model(model, key))
    return tags


def api_get(key):
    req = urllib.request.Request(
        f"https://api.zotero.org/groups/{LIB_ID}/items/{key}",
        headers={"Zotero-API-Version": "3", "Zotero-API-Key": RO_KEY},
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def write_key(key, new_tags, retries=3):
    if not new_tags:
        return {"key": key, "status": "no-data"}
    for attempt in range(retries):
        try:
            item = api_get(key)
            version = item["data"]["version"]
            existing = {t["tag"] for t in item["data"]["tags"]}
            to_add = [t for t in new_tags if t not in existing]
            if not to_add:
                return {"key": key, "status": "skip-present", "added": 0}
            all_tags = sorted(existing | set(new_tags))
            body = json.dumps({"tags": [{"tag": t} for t in all_tags]}).encode()
            req = urllib.request.Request(
                f"https://api.zotero.org/groups/{LIB_ID}/items/{key}",
                data=body, method="PATCH",
                headers={
                    "Zotero-API-Version": "3",
                    "Zotero-API-Key": RW_KEY,
                    "Content-Type": "application/json",
                    "If-Unmodified-Since-Version": str(version),
                },
            )
            with urllib.request.urlopen(req):
                pass
            # verify
            item2 = api_get(key)
            after = {t["tag"] for t in item2["data"]["tags"]}
            missing = [t for t in new_tags if t not in after]
            return {
                "key": key, "status": "added", "added": len(to_add),
                "verified": len(missing) == 0, "missing": missing,
            }
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code == 412:
                wait = int(e.headers.get("Retry-After", "2")) if e.code == 429 else 1
                time.sleep(wait + attempt)
                continue
            return {"key": key, "status": "error", "error": f"{e.code} {e.read().decode()[:200]}"}
        except Exception as e:
            return {"key": key, "status": "error", "error": str(e)}
    return {"key": key, "status": "error", "error": "exhausted retries"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-size", type=int, default=5)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--start-at", type=str, default=None)
    args = ap.parse_args()

    keys = json.load(open(os.path.join(DATA_DIR, "sweep_keys.json")))
    if args.start_at:
        idx = keys.index(args.start_at)
        keys = keys[idx:]
    if args.limit:
        keys = keys[: args.limit]

    log = []
    total = len(keys)
    for i in range(0, total, args.batch_size):
        batch = keys[i : i + args.batch_size]
        batch_results = []
        for key in batch:
            tags = build_tags_for_key(key)
            result = write_key(key, tags)
            batch_results.append(result)
            log.append(result)
            time.sleep(0.15)
        statuses = [f"{r['key']}:{r['status']}" for r in batch_results]
        print(f"[{min(i+args.batch_size, total)}/{total}] {statuses}", flush=True)
        errors = [r for r in batch_results if r["status"] == "error"]
        unverified = [r for r in batch_results if r.get("verified") is False]
        if errors:
            print(f"  ERRORS: {errors}", flush=True)
        if unverified:
            print(f"  VERIFY-FAILED: {unverified}", flush=True)

    log_path = os.path.join(DATA_DIR, "sweep_model_tag_write_log.json")
    json.dump(log, open(log_path, "w"), indent=2)
    summary = Counter(r["status"] for r in log)
    print("\n=== SUMMARY ===")
    print(dict(summary))
    print("errors:", [r for r in log if r["status"] == "error"])
    print("verify-failed:", [r for r in log if r.get("verified") is False])
    print(f"log written: {log_path}")


if __name__ == "__main__":
    main()
