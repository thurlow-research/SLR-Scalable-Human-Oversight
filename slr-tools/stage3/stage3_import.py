#!/usr/bin/env python
"""Stage 3 import — file the triaged corpus into Phase-3 collections + apply s3: tags.

Consolidates the human bucket decisions (work/review/*.csv) over Opus's triage
(work/stage3_results.csv), drops superseded duplicates, and for each surviving primary:
  - ADDS it to the matching Phase-3 sub-collection (01-Core/02-Context/03-Discard)
    *additively* — existing collection memberships are never touched;
  - adds tags: s3:opus:<opus_bin> (all), s3:human:<final> (bucket-reviewed items),
    lit-review (secondary literature).

Disposition per primary:
  - in a review bucket & not a duplicate -> effective bin (human override or per-bucket
    default: A/B blank=core, C/D blank=context);
  - not in a bucket -> Opus bin (the un-reviewed context<55 band and Opus discards);
  - the 7 superseded dup records -> excluded (already moved to 04-Superceded in Zotero).

Writes: per-item PATCH with If-Unmodified-Since-Version (no clobber), resumable via a
checkpoint. Run --dry-run first to review counts + the plan CSV before --apply.

Usage:
  python stage3_import.py --dry-run
  python stage3_import.py --apply
"""
import argparse, csv, json, os, re, time, urllib.request, urllib.error
from collections import Counter
from pathlib import Path

KEY=os.environ.get("ZOTERO_API_KEY"); LIB=os.environ.get("ZOTERO_LIBRARY_ID")
BASE=f"https://api.zotero.org/groups/{LIB}"
COLL={"core":"539H8RBQ","context":"85JVIR9X","discard":"JIMGLVAL"}
BUCKETS={"A":"A_core_confirm_75plus.csv","B":"B_core_review_70-74.csv",
         "C":"C_core_review_60-69.csv","D":"D_context_recall_55-69.csv"}
DEFAULT={"A":"core","B":"core","C":"context","D":"context"}
DROP={"BZDX5Z8B","EB9D98W5","AEB37KGC","CWUPRIIQ","XVWJ5J6J","B7APR28B","6UKF6TT2"}
LITREV_FALSEPOS={"G3FISG9I"}   # primary grounded-theory study, not a literature review
EXTRA_TAGS={"E9RAWBDT":["framing"],"B56YY529":["theme:oversight"]}   # per-item manual tags
LITREV_RX=re.compile(r'(a survey (of|on)|systematic literature review|literature review|'
                     r'scoping review|meta[- ]?analysis|mapping study|a review of|technical survey)',re.I)

def readcsv(f):
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:
            with open(f,encoding=enc) as fh: return list(csv.DictReader(fh))
        except UnicodeDecodeError: continue
    raise RuntimeError(f"cannot decode {f}")

def build(work):
    rev=work/"review"
    bucket={}   # item_key -> (final_bin, opus_bin_from_bucket, is_litrev)
    for bk,f in BUCKETS.items():
        for r in readcsv(rev/f):
            hb=(r.get("human_bin") or "").strip().lower()
            if hb=="duplicate": continue
            final=hb if hb in ("core","context","discard") else DEFAULT[bk]
            t=r.get("title","")
            litrev=bool(LITREV_RX.search(t)) and not re.search(r'code review|peer review',t,re.I) \
                   and r["item_key"] not in LITREV_FALSEPOS
            bucket[r["item_key"]]={"final":final,"opus":(r.get("opus_bin") or "").strip().lower(),
                                   "litrev":litrev,"reviewed":True}
    results={r["item_key"]:r for r in readcsv(work/"stage3_results.csv")}
    plan={}
    for k,r in results.items():
        if k in DROP or r.get("is_primary")!="yes": continue
        opus=(r.get("bin") or "").strip().lower()
        if k in bucket:
            b=bucket[k]; plan[k]={"final":b["final"],"opus":b["opus"] or opus,
                                  "reviewed":True,"litrev":b["litrev"],"title":r.get("title","")}
        else:
            plan[k]={"final":opus,"opus":opus,"reviewed":False,"litrev":False,"title":r.get("title","")}
    return plan

def tags_for(k,p):
    t=[f"s3:opus:{p['opus']}"] if p["opus"] else []
    if p["reviewed"]: t.append(f"s3:human:{p['final']}")
    if p["litrev"]: t.append("lit-review")
    t+=EXTRA_TAGS.get(k,[])
    return t

def api_get(path):
    req=urllib.request.Request(f"{BASE}/{path}",headers={"Zotero-API-Key":KEY,"Zotero-API-Version":"3"})
    with urllib.request.urlopen(req) as r: return json.load(r), dict(r.headers)

def cmd(args):
    work=Path(args.outdir)
    plan=build(work)
    print(f"primaries to file: {len(plan)}  (excluded {len(DROP)} superseded dups)")
    print("  disposition:", dict(Counter(p["final"] for p in plan.values())))
    print("  reviewed(human) vs machine-only:",
          dict(Counter("human" if p["reviewed"] else "machine" for p in plan.values())))
    print("  lit-review tags:", sum(1 for p in plan.values() if p["litrev"]))
    # sanity: any Opus-core not reviewed? (should be zero)
    anom=[k for k,p in plan.items() if p["opus"]=="core" and not p["reviewed"]]
    if anom: print(f"  !! {len(anom)} Opus-core items not in any bucket:", anom[:8])
    # plan CSV
    with open(work/"stage3_import_plan.csv","w",newline="",encoding="utf-8") as fh:
        w=csv.writer(fh); w.writerow(["item_key","final","target_collection","reviewed","tags","title"])
        for k,p in sorted(plan.items(),key=lambda kv:kv[1]["final"]):
            w.writerow([k,p["final"],COLL[p["final"]],p["reviewed"],"|".join(tags_for(k,p)),p["title"][:80]])
    print(f"  wrote {work/'stage3_import_plan.csv'}")
    if args.dry_run:
        print("\nDRY-RUN — no writes. Review the plan, then run --apply.")
        for k,p in list(plan.items())[:5]:
            print(f"    {k} -> {p['final']} ({COLL[p['final']]})  tags={tags_for(k,p)}")
        return
    # APPLY
    ckpt=work/"import_checkpoint.json"
    done=set(json.loads(ckpt.read_text())) if ckpt.exists() else set()
    n=0; fail=[]
    for k,p in plan.items():
        if k in done: continue
        target=COLL[p["final"]]
        try:
            it,_=api_get(f"items/{k}"); ver=it["version"]; d=it["data"]
            cols=list(d.get("collections",[]))
            if target not in cols: cols.append(target)      # ADDITIVE
            have={t["tag"] for t in d.get("tags",[])}
            tags=list(d.get("tags",[]))+[{"tag":t} for t in tags_for(k,p) if t not in have]
            body=json.dumps({"version":ver,"collections":cols,"tags":tags}).encode()
            req=urllib.request.Request(f"{BASE}/items/{k}",data=body,method="PATCH",
                headers={"Zotero-API-Key":KEY,"Zotero-API-Version":"3","Content-Type":"application/json",
                         "If-Unmodified-Since-Version":str(ver)})
            with urllib.request.urlopen(req) as r:
                if r.status not in (200,204): fail.append((k,r.status)); continue
            done.add(k); n+=1
            if n%50==0:
                ckpt.write_text(json.dumps(sorted(done))); print(f"  ...{n} filed",flush=True)
            time.sleep(args.sleep)
        except urllib.error.HTTPError as e:
            if e.code==429:
                time.sleep(int(e.headers.get("Retry-After","10"))); continue
            fail.append((k,e.code))
    ckpt.write_text(json.dumps(sorted(done)))
    print(f"\nfiled {n} items. failures: {fail if fail else 0}")
    for b,c in COLL.items():
        _,h=api_get(f"collections/{c}/items/top?limit=1")
        print(f"  {b} ({c}): {h.get('Total-Results')} items")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--outdir",default="work")
    ap.add_argument("--dry-run",action="store_true")
    ap.add_argument("--apply",action="store_true")
    ap.add_argument("--sleep",type=float,default=0.15)
    a=ap.parse_args()
    if not a.apply: a.dry_run=True
    cmd(a)

if __name__=="__main__":
    main()
