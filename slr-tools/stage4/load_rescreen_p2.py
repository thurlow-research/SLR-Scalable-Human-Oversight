#!/usr/bin/env python3
"""Load rescreen Phase-2 (Opus) results. Opus is a binary keep/discard arbiter.
 keep  -> file into Phase 2/02-Snowballing/01-Keep (BB4XPCTU) + tag s2:opus:keep
 discard-> tag s2:opus:discard (lineage); not filed into the P2 keep set.
Resumable via rescreen_p2_loaded.json."""
import csv, json, os, time, urllib.request, urllib.error
from pathlib import Path
KEY=os.environ["ZOTERO_API_KEY"]; LIB=os.environ["ZOTERO_LIBRARY_ID"]
BASE=f"https://api.zotero.org/groups/{LIB}"; ZH={"Zotero-API-Key":KEY,"Zotero-API-Version":"3"}
P2_KEEP="BB4XPCTU"
DONE=Path("work/stage4/rescreen_p2_loaded.json")
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
rows=list(csv.DictReader(open("work/stage4/rescreen_p2.csv")))
n=0
from collections import Counter
for r in rows:
    k=r["item_key"]
    if k in done: continue
    dec=r["decision"]
    it=api("GET",f"/items/{k}"); d=it["data"]
    tags=[t for t in d.get("tags",[]) if not t["tag"].startswith("s2:opus:")]+[{"tag":f"s2:opus:{dec}"}]
    colls=list(d.get("collections") or [])
    if dec=="keep" and P2_KEEP not in colls: colls=colls+[P2_KEEP]
    api("PATCH",f"/items/{k}",{"tags":tags,"collections":list(dict.fromkeys(colls))},
        {"If-Unmodified-Since-Version":str(it["version"])})
    done[k]=dec; n+=1
    if n%40==0: json.dump(done,open(DONE,"w")); print(f"  {n}")
    time.sleep(0.05)
json.dump(done,open(DONE,"w"))
print(f"loaded {n} (total {len(done)}) | dist:",dict(Counter(done.values())))
