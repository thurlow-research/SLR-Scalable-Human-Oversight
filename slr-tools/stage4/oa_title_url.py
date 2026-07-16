#!/usr/bin/env python3
"""Fill missing/weak URLs (and canonicalize rough titles) for the two singleton
review collections, from OpenAlex. PATCHes Zotero per item (resumable — already-good
items are skipped on rerun).

Logging: timestamped, per-item, to BOTH stdout and work/stage4/oa_title_url.log.
Throttle-aware: a get_work that takes >20s is almost certainly an OpenAlex 429
backoff (not a real miss); N consecutive such hits trips a circuit-breaker that
backs off exponentially rather than grinding silently.
"""
import json, urllib.request, os, sys, time, re, difflib, socket, logging
socket.setdefaulttimeout(30)  # global safety net: no urllib read blocks forever
sys.path.insert(0, os.path.expanduser('~/.claude/skills/openalex/scripts'))
import openalex  # prefers IPv4 + honors OPENALEX_MAILTO (polite pool) from env

LOG_PATH = os.path.join('work', 'stage4', 'oa_title_url.log')
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s %(levelname)-7s %(message)s',
    datefmt='%H:%M:%S',
    handlers=[logging.FileHandler(LOG_PATH), logging.StreamHandler(sys.stdout)])
log = logging.getLogger('oa')

KEY = os.environ['ZOTERO_API_KEY']; LIB = os.environ['ZOTERO_LIBRARY_ID']
BASE = f'https://api.zotero.org/groups/{LIB}'
H = {'Zotero-API-Key': KEY, 'Zotero-API-Version': '3'}
COLLECTIONS = ['4WMXV36M', 'TJTE4QWX']  # Low-Confidence (review) + Title-Only (fetch)

THROTTLE_SECS = 20      # a get_work slower than this = presumed 429 backoff
BREAKER_TRIP = 3        # consecutive throttle-hits before we back off
mailto = os.environ.get('OPENALEX_MAILTO') or os.environ.get('OPENALEX_EMAIL') or '(none)'


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


def norm(x):
    return re.sub(r'[^a-z0-9]', '', (x or '').lower())


def rough_title(t):
    return max((len(w.replace('-', '')) for w in (t or '').split(' ')), default=0) >= 16


def main():
    log.info('=== OpenAlex URL/title pass START | polite-pool mailto=%s ===', mailto)
    items = []
    for c in COLLECTIONS:
        got = get_all(c)
        log.info('collection %s: %d items', c, len(got))
        items += got
    seen = set()
    items = [it for it in items if not (it['key'] in seen or seen.add(it['key']))]
    need = [it for it in items if not (it['data'].get('url') or '').strip()
            or 'semanticscholar' in (it['data'].get('url') or '')
            or rough_title(it['data'].get('title', ''))]
    log.info('%d unique items; %d need OpenAlex upgrade (missing/weak URL or rough title)',
             len(items), len(need))

    url_f = title_f = matched = nomatch = 0
    consec_throttle = 0
    for i, it in enumerate(need, 1):
        d = it['data']; title = d.get('title', '')
        t0 = time.time()
        rec = openalex.normalize(openalex.get_work(title))
        dt = time.time() - t0

        if dt > THROTTLE_SECS:               # slow call == OpenAlex throttling us
            consec_throttle += 1
            log.warning('[%d/%d] THROTTLE (%.0fs, no result) consec=%d :: %.50s',
                        i, len(need), dt, consec_throttle, title)
            if consec_throttle >= BREAKER_TRIP:
                backoff = min(60 * consec_throttle, 600)
                log.warning('circuit-breaker: %d consecutive throttle hits — backing off %ds',
                            consec_throttle, backoff)
                time.sleep(backoff)
            continue
        consec_throttle = 0

        if not rec:
            nomatch += 1
            log.info('[%d/%d] no OpenAlex match (%.1fs) :: %.55s', i, len(need), dt, title)
            continue
        if difflib.SequenceMatcher(None, norm(title), norm(rec['title'])).ratio() < 0.5:
            nomatch += 1
            log.info('[%d/%d] match rejected (title mismatch) :: %.45s != %.30s',
                     i, len(need), title, rec['title'])
            continue

        matched += 1
        body = {}
        if rec['title'] and norm(rec['title']) != norm(title):
            body['title'] = rec['title']; title_f += 1
        cu = d.get('url', '') or ''
        if rec['url'] and (not cu or 'semanticscholar' in cu):
            body['url'] = rec['url']; url_f += 1
        if rec['doi'] and not d.get('DOI'):
            body['DOI'] = rec['doi']
        if rec['authors'] and not d.get('creators'):
            body['creators'] = [{'creatorType': 'author', 'lastName': n.split()[-1],
                                 'firstName': ' '.join(n.split()[:-1])} for n in rec['authors']]
        if rec['abstract'] and not (d.get('abstractNote') or '').strip():
            body['abstractNote'] = rec['abstract']
        if rec['year'] and not (d.get('date') or '').strip():
            body['date'] = str(rec['year'])
        if not body:
            log.info('[%d/%d] matched, nothing to fill :: %.55s', i, len(need), title)
            continue
        try:
            hs = dict(H); hs['Content-Type'] = 'application/json'
            hs['If-Unmodified-Since-Version'] = str(it['version'])
            urllib.request.urlopen(urllib.request.Request(
                f"{BASE}/items/{it['key']}", data=json.dumps(body).encode(),
                headers=hs, method='PATCH'), timeout=30).read()
            log.info('[%d/%d] PATCHED %s: %s (%.1fs) :: %.45s', i, len(need), it['key'],
                     '+'.join(sorted(body)), dt, title)
        except Exception as e:
            log.error('[%d/%d] PATCH FAILED %s: %s', i, len(need), it['key'], e)
        time.sleep(0.2)

    log.info('=== DONE: URLs filled %d, titles canonicalized %d | matched %d, no-match %d, of %d ===',
             url_f, title_f, matched, nomatch, len(need))


if __name__ == '__main__':
    main()
