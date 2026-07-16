#!/usr/bin/env python3
"""Load rescreen Phase-1 results: re-file each item into Citation Snowballing/02-Screening
Keep/Maybe/Discard per new decision, add s1:sonnet:<decision> (replacing any prior s1:sonnet:*),
preserve all other tags/collections. Resumable via rescreen_p1_loaded.json."""
import csv, json, os, time, urllib.request, urllib.error
from pathlib import Path
KEY=os.environ["ZOTERO_API_KEY"]; LIB=os.environ["ZOTERO_LIBRARY_ID"]
BASE=f"https://api.zotero.org/groups/{LIB}"; ZH={"Zotero-API-Key":KEY,"Zotero-API-Version":"3"}
BUCKET={"keep":"I8ERWQU4","maybe":"R5P2NLSN","discard":"QVSP4TJW"}
ALLB=set(BUCKET.values())
DONE=Path("work/stage4/rescreen_p1_loaded.json")

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

done=json.load(open(DONE)) if DONE.exists() else {}
rows=list(csv.DictReader(open("work/stage4/rescreen_p1.csv")))
n=0
for r in rows:
    k=r["item_key"]
    if k in done: continue
    dec=r["decision"]; tgt=BUCKET.get(dec,BUCKET["maybe"])
    it=api("GET",f"/items/{k}")
    d=it["data"]
    tags=[t for t in d.get("tags",[]) if not t["tag"].startswith("s1:sonnet:")]+[{"tag":f"s1:sonnet:{dec}"}]
    colls=[c for c in (d.get("collections") or []) if c not in ALLB]+[tgt]
    colls=list(dict.fromkeys(colls))
    api("PATCH",f"/items/{k}",{"tags":tags,"collections":colls},
        {"If-Unmodified-Since-Version":str(it["version"])})
    done[k]=dec; n+=1
    if n%50==0:
        json.dump(done,open(DONE,"w")); print(f"  {n} loaded")
    time.sleep(0.05)
json.dump(done,open(DONE,"w"))
from collections import Counter
print(f"loaded {n} (total {len(done)}) | dist:",dict(Counter(done.values())))
