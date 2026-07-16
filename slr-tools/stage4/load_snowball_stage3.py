#!/usr/bin/env python3
"""Consolidate snowball Stage-3 _out.csv verdicts and file into Phase 3/02-Snowballing
band sub-collections, with s3:opus:<bin> + centrality:<n> tags (score-as-tag for tracking).
Filing by bin + centrality:
  core   >=75 -> Core/01-Confirm (75-100)      core <75 -> Core/02-Review (70-74)
  context>=55 -> Context/01-Recall (55-69)     context<55-> Context/02-Below-55 (30-54)
  discard     -> 03-Discard
Resumable via loaded.json."""
import csv, json, os, time, glob, urllib.request, urllib.error
from pathlib import Path
KEY=os.environ["ZOTERO_API_KEY"]; LIB=os.environ["ZOTERO_LIBRARY_ID"]
BASE=f"https://api.zotero.org/groups/{LIB}"; ZH={"Zotero-API-Key":KEY,"Zotero-API-Version":"3"}
CORE_CONFIRM="RZWBRF2T"; CORE_REVIEW="HFD75W94"; CTX_RECALL="ZUUGKPK2"; CTX_BELOW="MBSRBERI"; DISCARD="3GZZNLAR"
ALL_P3={CORE_CONFIRM,CORE_REVIEW,CTX_RECALL,CTX_BELOW,DISCARD}
DONE=Path("work/snowball_stage3/loaded.json")

def target(b,cent):
    try: c=int(float(cent))
    except: c=0
    if b=="core":    return CORE_CONFIRM if c>=75 else CORE_REVIEW
    if b=="context": return CTX_RECALL   if c>=55 else CTX_BELOW
    return DISCARD

def api(method,path,body=None,headers=None):
    hs=dict(ZH)
    if headers: hs.update(headers)
    data=json.dumps(body).encode() if body is not None else None
    if data: hs["Content-Type"]="application/json"
    req=urllib.request.Request(f"{BASE}{path}",data=data,headers=hs,method=method)
    for a in range(6):
        try:
            with urllib.request.urlopen(req,timeout=30) as r:
                raw=r.read(); return (json.loads(raw) if raw else None)
        except urllib.error.HTTPError as e:
            if e.code in (429,500,502,503): time.sleep(int(e.headers.get("Retry-After","3"))+a); continue
            raise

verdicts={}
for f in glob.glob("work/snowball_stage3/batch_*_out.csv"):
    for r in csv.DictReader(open(f)):
        verdicts[r["item_key"]]={"bin":r["bin"],"centrality":r["centrality"]}
done=json.load(open(DONE)) if DONE.exists() else {}
n=0
from collections import Counter
dist=Counter()
for k,v in verdicts.items():
    tgt=target(v["bin"],v["centrality"]); dist[tgt]+=1
    if k in done: continue
    it=api("GET",f"/items/{k}"); d=it["data"]
    tags=[t for t in d.get("tags",[]) if not (t["tag"].startswith("s3:opus:") or t["tag"].startswith("centrality:"))]
    tags+=[{"tag":f"s3:opus:{v['bin']}"},{"tag":f"centrality:{v['centrality']}"}]
    colls=[c for c in (d.get("collections") or []) if c not in ALL_P3]+[tgt]
    api("PATCH",f"/items/{k}",{"tags":tags,"collections":list(dict.fromkeys(colls))},
        {"If-Unmodified-Since-Version":str(it["version"])})
    done[k]=f"{v['bin']}:{v['centrality']}"; n+=1
    if n%40==0: json.dump(done,open(DONE,"w")); print(f"  {n}")
    time.sleep(0.05)
json.dump(done,open(DONE,"w"))
names={CORE_CONFIRM:"Core/Confirm",CORE_REVIEW:"Core/Review",CTX_RECALL:"Ctx/Recall",CTX_BELOW:"Ctx/Below",DISCARD:"Discard"}
print(f"loaded {n} (total {len(done)})")
print("by sub-collection:",{names[k]:c for k,c in dist.items()})
