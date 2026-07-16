#!/usr/bin/env python3
"""Detect snowball records that duplicate an ORIGINAL triaged (query-stream) record,
by DOI / arXiv id / normalized title. Reports matches with the master's disposition.
Read-only."""
import json, os, re, socket, urllib.request
socket.setdefaulttimeout(30)
LIB=os.environ["ZOTERO_LIBRARY_ID"]; H={"Zotero-API-Key":os.environ["ZOTERO_API_KEY"],"Zotero-API-Version":"3"}
BASE=f"https://api.zotero.org/groups/{LIB}"
MASTER={"539H8RBQ":"core","85JVIR9X":"context","JIMGLVAL":"discard"}      # Phase3/01-Queries
SNOW={"BB4XPCTU":"p2-keep","TVXU94Q4":"held"}                             # live snowball set

def get_all(c):
    o,s=[],0
    while True:
        with urllib.request.urlopen(urllib.request.Request(f"{BASE}/collections/{c}/items/top?limit=100&start={s}",headers=H),timeout=30) as r:
            d=json.load(r)
        o+=d
        if len(d)<100: break
        s+=100
    return [it for it in o if it["data"].get("itemType") not in ("attachment","note")]

def norm_title(t): return re.sub(r"[^a-z0-9]","",(t or "").lower())
def ids_of(d):
    out=set()
    doi=(d.get("DOI") or "").lower().replace("https://doi.org/","").strip()
    if doi: out.add(("doi",doi))
    blob=" ".join([d.get("url") or "", d.get("extra") or "", doi])
    for m in re.findall(r"(\d{4}\.\d{4,5})",blob): out.add(("arxiv",m))
    for m in re.findall(r"arxiv[:/ ]*([a-z\-]+/\d{7}|\d{4}\.\d{4,5})",blob.lower()): out.add(("arxiv",m))
    return out

# build master index
midx={}; mtitle={}
for c,disp in MASTER.items():
    for it in get_all(c):
        d=it["data"]
        for i in ids_of(d): midx[i]=(it["key"],disp)
        nt=norm_title(d.get("title"))
        if len(nt)>=12: mtitle[nt]=(it["key"],disp)
print(f"master index: {len(midx)} ids, {len(mtitle)} titles")

# scan snowball
seen=set(); matches=[]
for c,tag in SNOW.items():
    for it in get_all(c):
        k=it["key"]
        if k in seen: continue
        seen.add(k)
        d=it["data"]
        hit=None
        for i in ids_of(d):
            if i in midx: hit=("id "+i[0],midx[i]); break
        if not hit:
            nt=norm_title(d.get("title"))
            if len(nt)>=12 and nt in mtitle: hit=("title",mtitle[nt])
        if hit:
            same = (k==hit[1][0])
            matches.append((k,tag,hit[1][0],hit[1][1],hit[0],same,(d.get("title") or "")[:55]))
print(f"\n{len(matches)} snowball records overlap the original triaged set:\n")
from collections import Counter
print("by master disposition:",dict(Counter(m[3] for m in matches)))
print("same-key (one record in both):",sum(1 for m in matches if m[5]),"| different-key (true dup):",sum(1 for m in matches if not m[5]))
print()
for k,tag,mk,mdisp,how,same,title in sorted(matches,key=lambda m:m[3]):
    print(f"  snow {k} ({tag}) -> master {mk} [{mdisp}] via {how} {'SAME-KEY' if same else 'DUP'} :: {title}")
