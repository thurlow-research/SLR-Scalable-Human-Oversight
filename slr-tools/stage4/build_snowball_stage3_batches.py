#!/usr/bin/env python3
"""Build Stage-3 triage batches from the snowball Phase-2 (Opus) KEEPS.
Final keep set = rescreen_p2.csv decision==keep. Pulls title+abstract from rescreen_input.csv.
Writes work/snowball_stage3/batches/batch_NNN.csv (item_key,title,abstract)."""
import csv, os
from pathlib import Path
WORK=Path("work/stage4"); OUT=Path("work/snowball_stage3/batches"); OUT.mkdir(parents=True,exist_ok=True)
inp={r["item_key"]:r for r in csv.DictReader(open(WORK/"rescreen_input.csv"))}
p2=list(csv.DictReader(open(WORK/"rescreen_p2.csv")))
keeps=[r["item_key"] for r in p2 if r["decision"]=="keep"]
BATCH=20; n=0
for i in range(0,len(keeps),BATCH):
    n+=1
    with open(OUT/f"batch_{n:03d}.csv","w",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=["item_key","title","abstract"]); w.writeheader()
        for k in keeps[i:i+BATCH]:
            r=inp.get(k,{}); w.writerow({"item_key":k,"title":r.get("title",""),"abstract":r.get("abstract","")})
print(f"{len(keeps)} Opus-keeps -> {n} batches in {OUT}")
