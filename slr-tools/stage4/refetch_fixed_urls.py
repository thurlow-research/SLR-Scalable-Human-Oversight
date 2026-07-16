#!/usr/bin/env python3
"""Re-fetch URLs for the 34 OCR-fixed records specifically (keys from title_fixes.json).
Reports per-record: already has URL / filled now / still no match. PATCHes Zotero.
"""
import json, urllib.request, urllib.error, os, sys, time, socket, difflib, re
socket.setdefaulttimeout(30)
sys.path.insert(0, os.path.expanduser('~/.claude/skills/openalex/scripts'))
import openalex
KEY = os.environ['ZOTERO_API_KEY']; LIB = os.environ['ZOTERO_LIBRARY_ID']
BASE = f'https://api.zotero.org/groups/{LIB}'
H = {'Zotero-API-Key': KEY, 'Zotero-API-Version': '3'}


def norm(x):
    return re.sub(r'[^a-z0-9]', '', (x or '').lower())


def get_item(k):
    with urllib.request.urlopen(urllib.request.Request(f'{BASE}/items/{k}', headers=H), timeout=30) as r:
        return json.load(r)


keys = list(json.load(open('title_fixes.json')).keys())
have = filled = nomatch = 0
still = []
for k in keys:
    it = get_item(k); d = it['data']; title = d.get('title', '')
    url = (d.get('url') or '').strip()
    if url and 'semanticscholar' not in url:
        have += 1
        print(f"  {k}  HAS URL   {title[:52]}")
        continue
    rec = openalex.normalize(openalex.get_work(title))
    if not rec or difflib.SequenceMatcher(None, norm(title), norm(rec['title'])).ratio() < 0.5:
        nomatch += 1; still.append((k, title))
        print(f"  {k}  no match  {title[:52]}")
        continue
    body = {}
    if rec['url']:
        body['url'] = rec['url']
    if rec['doi'] and not d.get('DOI'):
        body['DOI'] = rec['doi']
    if rec['abstract'] and not (d.get('abstractNote') or '').strip():
        body['abstractNote'] = rec['abstract']
    if rec['authors'] and not d.get('creators'):
        body['creators'] = [{'creatorType': 'author', 'lastName': n.split()[-1],
                             'firstName': ' '.join(n.split()[:-1])} for n in rec['authors']]
    if not body.get('url'):
        nomatch += 1; still.append((k, title))
        print(f"  {k}  matched but no URL  {title[:44]}")
        continue
    hs = dict(H); hs['Content-Type'] = 'application/json'; hs['If-Unmodified-Since-Version'] = str(it['version'])
    urllib.request.urlopen(urllib.request.Request(f"{BASE}/items/{k}", data=json.dumps(body).encode(),
                           headers=hs, method='PATCH'), timeout=30).read()
    filled += 1
    print(f"  {k}  FILLED +{'+'.join(sorted(body))}  {rec['url'][:40]}")
    time.sleep(0.15)

print(f"\n=== of {len(keys)} fixed records: {have} already had URL, {filled} filled now, {nomatch} still no URL ===")
if still:
    print("still URL-less (likely not in OpenAlex — new/grey):")
    for k, t in still:
        print(f"  {k}  {t[:70]}")
