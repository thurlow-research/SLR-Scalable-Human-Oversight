#!/usr/bin/env python3
"""Clean OCR/citation-mangled stub titles in a Zotero collection (LOCAL, no network):
  - pull a leading 'YYYY.' out of the title into the date field
  - split CamelCase and dictionary word-break spaceless runs into spaced words
Run the URL fetch separately afterward (titles are now searchable).

Usage: python3 clean_mangled_titles.py COLLECTION_KEY [--dry-run] [--limit N]
"""
import argparse
import json
import os
import re
import time
import urllib.request
import urllib.error
from functools import lru_cache

KEY = os.environ["ZOTERO_API_KEY"]
LIB = os.environ["ZOTERO_LIBRARY_ID"]
BASE = f"https://api.zotero.org/groups/{LIB}"
H = {"Zotero-API-Key": KEY, "Zotero-API-Version": "3"}

WORDS = set()
if os.path.exists("/usr/share/dict/words"):
    WORDS = {w.strip().lower() for w in open("/usr/share/dict/words", errors="ignore")
             if len(w.strip()) >= 2}
WORDS |= {"a", "an", "of", "to", "in", "on", "by", "is", "as", "at", "we", "our", "ai",
          "llm", "llms", "ml", "api", "id", "vibe", "github", "copilot", "chatgpt", "pre",
          "co", "de", "re", "gpt", "se", "mcp", "rag", "devops", "sql", "io", "ui", "ux"}


@lru_cache(maxsize=None)
def wordbreak(s):
    s = s.lower()
    n = len(s)
    INF = float("inf")
    dp = [(0, [])] + [(INF, None)] * n
    for i in range(1, n + 1):
        for j in range(max(0, i - 22), i):
            if dp[j][0] == INF:
                continue
            chunk = s[j:i]
            cost = dp[j][0] + (0 if chunk in WORDS else len(chunk) ** 2) + 1
            if cost < dp[i][0]:
                dp[i] = (cost, dp[j][1] + [chunk])
    return " ".join(dp[n][1]) if dp[n][1] else s


def clean_title(raw):
    m = re.match(r"^\s*[\"'“”]*\.?\s*(\d{4})[.,]?\s*", raw)
    year = m.group(1) if m else ""
    t = (raw[m.end():] if m else raw).strip().lstrip(".").strip()
    t = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", t)        # CamelCase
    t = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", t)
    parts = []
    for tok in t.split(" "):
        core = tok.replace("-", "")
        if len(core) >= 16 and core.isalpha():           # spaceless run -> word-break
            parts.append(" ".join(wordbreak(x) for x in tok.split("-") if x))
        else:
            parts.append(tok)
    t = re.sub(r"\s+", " ", " ".join(parts)).strip()
    return year, t


def get_all(coll):
    out, start = [], 0
    while True:
        d = json.load(urllib.request.urlopen(urllib.request.Request(
            f"{BASE}/collections/{coll}/items/top?limit=100&start={start}", headers=H)))
        out += d
        if len(d) < 100:
            break
        start += 100
    return [it for it in out if it["data"].get("itemType") not in ("attachment", "note")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("collection")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    items = get_all(a.collection)

    def mangled(it):
        t = it["data"].get("title", "")
        yr = re.match(r"^\s*[\"'“”]*\.?\s*\d{4}[.\s]", t)
        maxtok = max((len(w.replace("-", "")) for w in t.split(" ")), default=0)
        return bool(yr) or maxtok >= 16

    targets = [it for it in items if mangled(it)]
    if a.limit:
        targets = targets[:a.limit]
    print(f"{len(items)} items; {len(targets)} to clean")
    n = 0
    for it in targets:
        raw = it["data"].get("title", "")
        year, cleaned = clean_title(raw)
        body = {}
        if cleaned and cleaned != raw:
            body["title"] = cleaned
        if year and not (it["data"].get("date") or "").strip():
            body["date"] = year
        if not body:
            continue
        n += 1
        print(f"  {it['key']}: '{raw[:40]}'\n     -> title='{body.get('title', raw)[:56]}' date={body.get('date','-')}")
        if not a.dry_run:
            try:
                hs = dict(H); hs["Content-Type"] = "application/json"
                hs["If-Unmodified-Since-Version"] = str(it["version"])
                urllib.request.urlopen(urllib.request.Request(f"{BASE}/items/{it['key']}",
                                       data=json.dumps(body).encode(), headers=hs, method="PATCH"), timeout=30).read()
            except urllib.error.HTTPError as e:
                print("    FAIL", e.code)
            time.sleep(0.08)
    print(f"\n{'(dry-run) ' if a.dry_run else ''}cleaned {n}")


if __name__ == "__main__":
    main()
