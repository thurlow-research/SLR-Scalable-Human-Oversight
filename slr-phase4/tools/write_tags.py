#!/usr/bin/env python3
"""Write source-encoded calibration tags to Zotero. REPLACE mode for the given models.
Scheme: cal:<model>:theme:<slug> / cal:<model>:primary:<slug> / cal:<model>:facet:<slug>
Usage: write_tags.py <A|B> <model1[,model2,...]>
"""
import json,sys,os,urllib.request
KEY=os.environ.get('ZOTERO_API_KEY_RW') or os.environ['ZOTERO_API_KEY']  # writes need RW
GID='6505702'
S=os.path.dirname(os.path.abspath(__file__))
sets=json.load(open(f'{S}/calib_sets.json'))
which=sys.argv[1].upper(); models=sys.argv[2].split(',')
keys=sets['setA'] if which=='A' else sets['setB']

def req(method,url,data=None,headers=None):
    h={'Zotero-API-Key':KEY}; h.update(headers or {})
    if data is not None: data=json.dumps(data).encode(); h['Content-Type']='application/json'
    r=urllib.request.Request(url,data=data,headers=h,method=method)
    with urllib.request.urlopen(r) as resp:
        b=resp.read(); return resp.status,(json.loads(b) if b else None)

def tags_for(model,k):
    f=f'{S}/tags/{model}/{k}.json'
    if not os.path.exists(f) or os.path.getsize(f)==0: return None
    d=json.load(open(f)); out=set()
    for t in d.get('themes',[]) or []: out.add(f'cal:{model}:theme:{t}')
    pt=d.get('primary_theme')
    if pt: out.add(f'cal:{model}:primary:theme:{pt}'); out.add(f'cal:{model}:theme:{pt}')
    for fc in d.get('facets',[]) or []: out.add(f'cal:{model}:facet:{fc}')
    return out

for k in keys:
    want=set(); missing=[]
    for m in models:
        t=tags_for(m,k)
        if t is None: missing.append(m); continue
        want|=t
    if missing: print(f'{k}: MISSING {missing}')
    _,item=req('GET',f'https://api.zotero.org/groups/{GID}/items/{k}')
    ver=item['data']['version']; existing=item['data'].get('tags',[])
    # REPLACE: drop existing cal:<model>: tags for target models, keep everything else
    kept=[t for t in existing if not any(t['tag'].startswith(f'cal:{m}:') for m in models)]
    newlist=kept+[{'tag':t} for t in sorted(want)]
    if {t['tag'] for t in newlist}=={t['tag'] for t in existing}:
        print(f'{k}: no change'); continue
    st,_=req('PATCH',f'https://api.zotero.org/groups/{GID}/items/{k}',
             {'tags':newlist},{'If-Unmodified-Since-Version':str(ver)})
    print(f'{k}: [{st}] models={models} tags-written={len(want)}')
print('WRITE_DONE')
