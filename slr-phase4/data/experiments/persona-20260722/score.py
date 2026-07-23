#!/usr/bin/env python3
"""Score the persona-variant gemini run vs human gold, side-by-side with the v2.13 baseline."""
import json, pathlib

SP = pathlib.Path(__file__).parent
R = pathlib.Path("/Users/scott/Code/SLR/slr-phase4")
gold = json.load(open(R / "data/tags-v213/human_gold.json"))

def jac(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a | b else 1.0

def load(p):
    try:
        return json.loads(p.read_text())
    except Exception:
        return None

rows, agg = [], {"persona": {"prim": 0, "tj": [], "fj": [], "dem_ok": 0, "n": 0},
                 "baseline": {"prim": 0, "tj": [], "fj": [], "dem_ok": 0, "n": 0}}
for k, g in gold.items():
    row = {"key": k, "gold": g["primary"]}
    for arm, path in (("persona", SP / f"gemini/{k}.json"),
                      ("baseline", R / f"data/tags-v213/gemini/{k}.json")):
        d = load(path)
        if not d:
            row[arm] = None
            continue
        a = agg[arm]
        a["n"] += 1
        a["prim"] += d["primary_theme"] == g["primary"]
        a["tj"].append(jac(d["themes"], g["themes"]))
        a["fj"].append(jac(d["facets"], g["facets"]))
        a["dem_ok"] += any(f.startswith("demote:") for f in d.get("flags", [])) == g["demote"]
        row[arm] = {"primary": d["primary_theme"], "themes": sorted(d["themes"]),
                    "facets": sorted(d["facets"]), "flags": d.get("flags", [])}
    rows.append(row)

print(f"{'key':10} {'gold primary':28} {'baseline':28} {'persona':28}")
for r in rows:
    b = r["baseline"]["primary"] if r["baseline"] else "MISSING"
    p = r["persona"]["primary"] if r["persona"] else "MISSING"
    mb = "=" if b == r["gold"] else "X"
    mp = "=" if p == r["gold"] else "X"
    hilite = " <-- changed" if b != p else ""
    print(f"{r['key']:10} {r['gold']:28} {mb} {b:26} {mp} {p:26}{hilite}")

print()
for arm in ("baseline", "persona"):
    a = agg[arm]
    if a["n"]:
        print(f"{arm:9}: primaries {a['prim']}/{a['n']}  theme-J {sum(a['tj'])/a['n']:.2f}  "
              f"facet-J {sum(a['fj'])/a['n']:.2f}  demote-correct {a['dem_ok']}/{a['n']}")

# the confusion Scott cares about: hitl-workflow <-> risk-routing
print("\nhitl-workflow / risk-routing involvement (gold, baseline, persona):")
for r in rows:
    trio = [r["gold"],
            r["baseline"]["primary"] if r["baseline"] else "-",
            r["persona"]["primary"] if r["persona"] else "-"]
    if any(t in ("hitl-workflow", "risk-routing") for t in trio):
        print(f"  {r['key']:10} gold={trio[0]:26} base={trio[1]:26} persona={trio[2]}")

json.dump(rows, open(SP / "scored.json", "w"), indent=1)
print("\nwrote", SP / "scored.json")
