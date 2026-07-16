#!/usr/bin/env python3
"""Dump key|version|title for the two singleton review collections -> JSON + readable list."""
import json, urllib.request, os, sys, socket
socket.setdefaulttimeout(30)
KEY = os.environ['ZOTERO_API_KEY']; LIB = os.environ['ZOTERO_LIBRARY_ID']
BASE = f'https://api.zotero.org/groups/{LIB}'
H = {'Zotero-API-Key': KEY, 'Zotero-API-Version': '3'}
COLLS = {'TJTE4QWX': 'Title-Only', '4WMXV36M': 'Low-Confidence'}


def get_all(c):
    o, s = [], 0
    while True:
        with urllib.request.urlopen(urllib.request.Request(
                f'{BASE}/collections/{c}/items/top?limit=100&start={s}', headers=H), timeout=30) as r:
            d = json.load(r)
        o += d
        if len(d) < 100:
            break
        s += 100
    return [it for it in o if it['data'].get('itemType') not in ('attachment', 'note')]


rows, seen = [], set()
for c, name in COLLS.items():
    for it in get_all(c):
        if it['key'] in seen:
            continue
        seen.add(it['key'])
        rows.append({'key': it['key'], 'version': it['version'], 'coll': name,
                     'title': it['data'].get('title', ''), 'url': it['data'].get('url', ''),
                     'itemType': it['data'].get('itemType', '')})

out = 'work/stage4/titles_dump.json'
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump(rows, open(out, 'w'), indent=1)
for i, r in enumerate(rows, 1):
    print(f"{i:3} [{r['key']}] {r['title']}")
print(f"\n{len(rows)} unique items -> {out}", file=sys.stderr)
