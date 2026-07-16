#!/usr/bin/env python3
"""Setup for snowball RE-screen on cleaned/enriched data:
 - create 'Held - No Abstract (review)' under Citation Snowballing
 - items in Keep(480)+Maybe(15) WITHOUT an abstract -> tag hold:no-abstract + file into Held (excluded from auto-screen)
 - items WITH abstract -> rescreen_input.csv (item_key,title,abstract,cocite,has_abstract)
"""
import csv, json, os, time, urllib.request, urllib.error
from pathlib import Path
KEY=os.environ["ZOTERO_API_KEY"]; LIB=os.environ["ZOTERO_LIBRARY_ID"]
BASE=f"https://api.zotero.org/groups/{LIB}"; ZH={"Zotero-API-Key":KEY,"Zotero-API-Version":"3"}
SNOWBALL_PARENT="G7HHMK45"; SRC={"keep":"I8ERWQU4","maybe":"R5P2NLSN"}
OUT=Path("work/stage4/rescreen_input.csv")

def api(method,path,body=None,headers=None):
    hs=dict(ZH)
    if headers: hs.update(headers)
    data=json.dumps(body).encode() if body is not None else None
    if data: hs["Content-Type"]="application/json"
    req=urllib.request.Request(f"{BASE}{path}",data=data,headers=hs,method=method)
    for a in range(6):
        try:
            with urllib.request.urlopen(req,timeout=30) as r:
                raw=r.read(); return (json.loads(raw) if raw else None),dict(r.headers)
        except urllib.error.HTTPError as e:
            if e.code in (429,500,502,503): time.sleep(int(e.headers.get("Retry-After","3"))+a); continue
            raise

def get_all(col):
    out,s=[],0
    while True:
        d,h=api("GET",f"/collections/{col}/items/top?limit=100&start={s}")
        out+=d
        if len(d)<100: break
        s+=100
    return [it for it in out if it["data"].get("itemType") not in ("attachment","note")]

# 1. create Held collection (idempotent: reuse if exists)
cols,_=api("GET","/collections?limit=100")
held=next((c["key"] for c in cols if c["data"]["name"]=="Held - No Abstract (review)"
           and c["data"].get("parentCollection")==SNOWBALL_PARENT),None)
if not held:
    res,_=api("POST","/collections",[{"name":"Held - No Abstract (review)","parentCollection":SNOWBALL_PARENT}])
    held=res["successful"]["0"]["key"]
    print("created Held collection",held)
else:
    print("reusing Held collection",held)

# 2. split keep+maybe by abstract
seen={}; rows=[]; held_items=[]
for disp,col in SRC.items():
    for it in get_all(col):
        k=it["key"]
        if k in seen: continue
        seen[k]=1
        d=it["data"]; ab=(d.get("abstractNote") or "").strip()
        cocite=next((t["tag"].split(":")[1] for t in d.get("tags",[]) if t["tag"].startswith("cocite:")),"")
        if ab:
            rows.append({"item_key":k,"title":(d.get("title") or "").strip(),"abstract":ab,
                         "cocite":cocite,"has_abstract":1})
        else:
            held_items.append(it)

# 3. tag + file held items
n=0
for it in held_items:
    d=it["data"]; k=it["key"]
    tags=[t for t in d.get("tags",[]) if t["tag"]!="hold:no-abstract"]+[{"tag":"hold:no-abstract"}]
    colls=list(dict.fromkeys((d.get("collections") or [])+[held]))
    api("PATCH",f"/items/{k}",{"tags":tags,"collections":colls},
        {"If-Unmodified-Since-Version":str(it["version"])})
    n+=1; time.sleep(0.05)
print(f"held (no-abstract): {n} tagged hold:no-abstract + filed into Held")

# 4. write rescreen input
OUT.parent.mkdir(parents=True,exist_ok=True)
with open(OUT,"w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=["item_key","title","abstract","cocite","has_abstract"]); w.writeheader(); w.writerows(rows)
print(f"rescreen_input.csv: {len(rows)} abstract-bearing items -> {OUT}")
