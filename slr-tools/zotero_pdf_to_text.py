#!/usr/bin/env python
"""Attach extracted plain text to Zotero items that have a PDF.

For every item in a collection (recursing into subcollections), find its PDF
attachment, run `pdftotext` on it, and upload the result as a `text/plain`
attachment on the same parent item — so models can read cheap text instead of
parsing PDFs.

Zotero group library via the Web API (env: ZOTERO_API_KEY, ZOTERO_LIBRARY_ID).
Writes use the full three-step Zotero file-upload protocol. Idempotent: items
that already have a `.txt` attachment are skipped unless --overwrite.

Safety: DRY-RUN by default (reports what it would do). Pass --apply to write.
This is a Zotero write with the write key — back up the library first.

Usage:
  python zotero_pdf_to_text.py --collection Y4DVYPA4                 # dry-run
  python zotero_pdf_to_text.py --collection Y4DVYPA4 --apply         # do it
  python zotero_pdf_to_text.py --collection Y4DVYPA4 --apply --limit 5
"""
import argparse, hashlib, json, os, re, subprocess, sys, tempfile, time
import urllib.parse, urllib.request, urllib.error
from pathlib import Path

KEY=os.environ.get("ZOTERO_API_KEY"); LIB=os.environ.get("ZOTERO_LIBRARY_ID")
BASE=f"https://api.zotero.org/groups/{LIB}"
H={"Zotero-API-Key":KEY,"Zotero-API-Version":"3"}

def req(method, path_or_url, data=None, headers=None, absolute=False):
    url=path_or_url if absolute else f"{BASE}/{path_or_url}"
    r=urllib.request.Request(url, data=data, method=method, headers={**H, **(headers or {})})
    return urllib.request.urlopen(r)

def get_json(path):
    with req("GET", path) as r: return json.load(r), dict(r.headers)

def all_subcollections(coll):
    """coll + every descendant collection key."""
    out=[coll]; stack=[coll]
    while stack:
        c=stack.pop(); start=0
        while True:
            data,h=get_json(f"collections/{c}/collections?limit=100&start={start}")
            for d in data: out.append(d["key"]); stack.append(d["key"])
            if len(data)<100: break
            start+=100
    return out

def top_items(coll):
    """top-level item keys directly in a collection (excludes child attachments)."""
    keys=[]; start=0
    while True:
        data,h=get_json(f"collections/{coll}/items/top?limit=100&start={start}")
        keys+=[d["key"] for d in data]
        if len(data)<100: break
        start+=100
    return keys

def children(item):
    data,_=get_json(f"items/{item}/children")
    return data

def find_pdf(kids):
    # imported_file (added from disk) and imported_url (saved via connector) are both
    # stored in Zotero and downloadable via /items/{key}/file; linked_file is a local
    # path not in group storage, so we skip it.
    pdfs=[k for k in kids if k["data"].get("itemType")=="attachment"
          and k["data"].get("contentType")=="application/pdf"
          and k["data"].get("linkMode") in ("imported_file","imported_url")]
    return pdfs[0] if pdfs else None

def text_atts(kids):
    return [k for k in kids if k["data"].get("itemType")=="attachment"
            and (k["data"].get("contentType")=="text/plain"
                 or (k["data"].get("filename","") or "").lower().endswith(".txt"))]

def has_file(att):
    """A real uploaded file has a non-empty md5; an empty/broken attachment doesn't."""
    return bool(att["data"].get("md5"))

def delete_item(att):
    with req("DELETE",f"items/{att['key']}",
             headers={"If-Unmodified-Since-Version":str(att["version"])}) as r:
        return r.status

def download_pdf(att_key):
    with req("GET", f"items/{att_key}/file") as r: return r.read()

def pdf_to_text(pdf_bytes):
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/"in.pdf"; t=Path(d)/"out.txt"; p.write_bytes(pdf_bytes)
        subprocess.run(["pdftotext","-enc","UTF-8",str(p),str(t)],check=True,
                       capture_output=True,timeout=300)
        return t.read_bytes()

def create_text_attachment(parent, filename):
    body=[{"itemType":"attachment","parentItem":parent,"linkMode":"imported_file",
           "title":filename,"filename":filename,"contentType":"text/plain","charset":"utf-8",
           "url":"","note":"","tags":[],"relations":{}}]
    with req("POST","items",data=json.dumps(body).encode(),
             headers={"Content-Type":"application/json"}) as r:
        resp=json.load(r)
    ok=resp.get("successful",{})
    if not ok: raise RuntimeError(f"create attachment failed: {resp.get('failed')}")
    return ok["0"]["key"]

def upload_file(att_key, filename, blob):
    md5=hashlib.md5(blob).hexdigest(); mtime=int(time.time()*1000)
    form=urllib.parse.urlencode({"md5":md5,"filename":filename,"filesize":len(blob),"mtime":mtime}).encode()
    # step 1: authorization
    try:
        with req("POST",f"items/{att_key}/file",data=form,
                 headers={"Content-Type":"application/x-www-form-urlencoded","If-None-Match":"*"}) as r:
            auth=json.load(r)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"upload-auth {e.code}: {e.read()[:200]}")
    if auth.get("exists"): return "exists"
    # step 2: upload to storage (prefix + file + suffix, raw body)
    payload=auth["prefix"].encode()+blob+auth["suffix"].encode()
    up=urllib.request.Request(auth["url"],data=payload,method="POST",
                              headers={"Content-Type":auth["contentType"]})
    with urllib.request.urlopen(up) as r:
        if r.status not in (200,201): raise RuntimeError(f"storage upload {r.status}")
    # step 3: register
    reg=urllib.parse.urlencode({"upload":auth["uploadKey"]}).encode()
    with req("POST",f"items/{att_key}/file",data=reg,
             headers={"Content-Type":"application/x-www-form-urlencoded","If-None-Match":"*"}) as r:
        if r.status not in (200,204): raise RuntimeError(f"register {r.status}")
    return "uploaded"

def sanitize(name):
    return re.sub(r"[^A-Za-z0-9._-]+","_",name)[:120] or "extracted"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--collection",required=True)
    ap.add_argument("--apply",action="store_true",help="actually write (default: dry-run)")
    ap.add_argument("--overwrite",action="store_true",help="add text even if a .txt attachment exists")
    ap.add_argument("--limit",type=int,default=0)
    ap.add_argument("--sleep",type=float,default=0.4)
    a=ap.parse_args()
    if not (KEY and LIB): sys.exit("ZOTERO_API_KEY / ZOTERO_LIBRARY_ID not set")

    colls=all_subcollections(a.collection)
    items=[]; seen=set()
    for c in colls:
        for k in top_items(c):
            if k not in seen: seen.add(k); items.append(k)
    print(f"collections (incl. subs): {len(colls)}   unique parent items: {len(items)}")

    stat={"txt_added":0,"skip_has_text":0,"no_pdf":0,"healed_empty":0,"err":0,"processed":0}
    for i,item in enumerate(items):
        if a.limit and stat["processed"]>=a.limit: break
        try:
            kids=children(item)
            tatts=text_atts(kids)
            valid=[t for t in tatts if has_file(t)]
            empty=[t for t in tatts if not has_file(t)]   # created but file never uploaded
            # a VALID text attachment means "done" (unless overwrite); an empty one is
            # a broken remnant to re-do so re-runs self-heal without duplicates.
            if valid and not a.overwrite:
                stat["skip_has_text"]+=1; continue
            pdf=find_pdf(kids)
            if not pdf: stat["no_pdf"]+=1; continue
            stat["processed"]+=1
            to_delete=empty+(valid if a.overwrite else [])   # clear before re-adding
            fn=sanitize((pdf["data"].get("filename") or item).rsplit(".",1)[0])+".txt"
            if not a.apply:
                tag=" [re-do empty]" if empty else (" [overwrite]" if (a.overwrite and valid) else "")
                print(f"  [DRY] {item}: would extract {pdf['key']} -> {fn}{tag}")
                continue
            for t in to_delete:
                delete_item(t); stat["healed_empty"]+= (1 if not has_file(t) else 0)
            blob=pdf_to_text(download_pdf(pdf["key"]))
            att=create_text_attachment(item,fn)
            res=upload_file(att,fn,blob)
            stat["txt_added"]+=1
            print(f"  {item}: {fn} ({len(blob)} bytes) -> {res}"
                  + (f" [healed {len(empty)} empty]" if empty else ""),flush=True)
            time.sleep(a.sleep)
        except Exception as e:  # noqa: BLE001
            stat["err"]+=1; print(f"  {item}: ERROR {e}",flush=True)
    print(f"\n{'APPLIED' if a.apply else 'DRY-RUN'} — {stat}")

if __name__=="__main__":
    main()
