#!/usr/bin/env python3
"""Second-chance URL fetch for the fixed records OpenAlex's strict top-1 title search
missed: use the RELEVANCE search endpoint (top-5) + pick best fuzzy title match >=0.72.
Grey-lit simply won't match (not in OpenAlex) — no harm trying. PATCHes Zotero.
"""
import json, urllib.request, os, sys, time, socket, difflib, re
socket.setdefaulttimeout(30)
sys.path.insert(0, os.path.expanduser('~/.claude/skills/openalex/scripts'))
import openalex
KEY = os.environ['ZOTERO_API_KEY']; LIB = os.environ['ZOTERO_LIBRARY_ID']
BASE = f'https://api.zotero.org/groups/{LIB}'
H = {'Zotero-API-Key': KEY, 'Zotero-API-Version': '3'}

# the 12 stragglers (real papers worth a second try; grey-lit will just no-match)
KEYS = ['WNGFVRN9', 'QEF4XCQS', 'B8DJBDXS', '644HUTI8', 'A292H27R', 'WITZNUF9',
        'HFZBEEQX', 'UMSNBE5P', '756MF8RP', '52DNSEVS', 'FAUAQCSZ', 'CNN7GGG2']


def norm(x):
    return re.sub(r'[^a-z0-9]', '', (x or '').lower())


def get_item(k):
    with urllib.request.urlopen(urllib.request.Request(f'{BASE}/items/{k}', headers=H), timeout=30) as r:
        return json.load(r)


def best_match(title):
    q = urllib.parse.quote(re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', title.lower())).strip()[:250])
    d = openalex._fetch(f"{openalex.BASE}/works?search={q}&per-page=5&select={openalex.SELECT}")
    best, bestr = None, 0.0
    for w in (d or {}).get('results', []):
        rec = openalex.normalize(w)
        r = difflib.SequenceMatcher(None, norm(title), norm(rec['title'])).ratio()
        if r > bestr:
            best, bestr = rec, r
    return (best, bestr) if bestr >= 0.72 else (None, bestr)


import urllib.parse
filled = 0
for k in KEYS:
    it = get_item(k); d = it['data']; title = d.get('title', '')
    rec, r = best_match(title)
    if not rec or not rec.get('url'):
        print(f"  {k}  no match (best ratio {r:.2f})  {title[:48]}")
        continue
    body = {'url': rec['url']}
    if rec['doi'] and not d.get('DOI'):
        body['DOI'] = rec['doi']
    if rec['abstract'] and not (d.get('abstractNote') or '').strip():
        body['abstractNote'] = rec['abstract']
    if rec['authors'] and not d.get('creators'):
        body['creators'] = [{'creatorType': 'author', 'lastName': n.split()[-1],
                             'firstName': ' '.join(n.split()[:-1])} for n in rec['authors']]
    hs = dict(H); hs['Content-Type'] = 'application/json'; hs['If-Unmodified-Since-Version'] = str(it['version'])
    urllib.request.urlopen(urllib.request.Request(f"{BASE}/items/{k}", data=json.dumps(body).encode(),
                           headers=hs, method='PATCH'), timeout=30).read()
    filled += 1
    print(f"  {k}  FILLED (ratio {r:.2f}) +{'+'.join(sorted(body))}\n      -> {rec['title'][:60]}\n      -> {rec['url']}")
    time.sleep(0.15)
print(f"\n=== second-chance: filled {filled} of {len(KEYS)} ===")
