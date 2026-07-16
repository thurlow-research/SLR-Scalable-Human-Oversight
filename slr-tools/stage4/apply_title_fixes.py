#!/usr/bin/env python3
"""Apply hand-authored OCR title corrections (title_fixes.json) to Zotero.
Versions come from titles_dump.json; PATCH is no-clobber (If-Unmodified-Since-Version).
Usage: python3 apply_title_fixes.py [--dry-run]
"""
import json, urllib.request, urllib.error, os, sys, time, socket
socket.setdefaulttimeout(30)
KEY = os.environ['ZOTERO_API_KEY']; LIB = os.environ['ZOTERO_LIBRARY_ID']
BASE = f'https://api.zotero.org/groups/{LIB}'
H = {'Zotero-API-Key': KEY, 'Zotero-API-Version': '3'}
DRY = '--dry-run' in sys.argv

dump = {r['key']: r for r in json.load(open('work/stage4/titles_dump.json'))}
fixes = json.load(open('title_fixes.json'))

ok = skip = fail = 0
for k, new in fixes.items():
    r = dump.get(k)
    if not r:
        print(f"  {k}: NOT in dump — skip"); skip += 1; continue
    old = r['title']
    if old == new:
        print(f"  {k}: already correct — skip"); skip += 1; continue
    print(f"  {k}\n    OLD: {old}\n    NEW: {new}")
    if DRY:
        ok += 1; continue
    try:
        hs = dict(H); hs['Content-Type'] = 'application/json'
        hs['If-Unmodified-Since-Version'] = str(r['version'])
        urllib.request.urlopen(urllib.request.Request(
            f"{BASE}/items/{k}", data=json.dumps({'title': new}).encode(),
            headers=hs, method='PATCH'), timeout=30).read()
        ok += 1
    except urllib.error.HTTPError as e:
        print(f"    FAIL {e.code} (version changed? re-dump)"); fail += 1
    time.sleep(0.15)
print(f"\n{'(dry-run) ' if DRY else ''}fixed {ok}, skipped {skip}, failed {fail} of {len(fixes)}")
