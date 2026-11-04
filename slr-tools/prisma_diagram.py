#!/usr/bin/env python3
"""PRISMA 2020 flow diagram (Figure A1, Appendix A), APA 7 figure style, from prisma_funnel.py JSON.

Port of the Assignment 6 `prisma_flow.py` layout; the only change is that every count is read from
the funnel JSON rather than typed in, so the figure cannot drift from the source of record.
APA 7 (Sec. 7.26): sans serif within the image, 8-14 pt at final size; rendered at its printed width
(6.5 in). Figure notes go in the caption, not inside the image.

Usage (needs matplotlib):
    python3 slr-tools/prisma_diagram.py Methodology/PRISMA_Funnel_vNNN.json OUTDIR
Writes OUTDIR/PRISMA_Flow_Diagram.{png,svg} and PRISMA_Flow_Diagram_adaptive.svg.
"""
import json
import os
import re
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

R = json.load(open(sys.argv[1]))
OUT = sys.argv[2]
idn, p1, p2, p3, ft = R["identification"], R["phase1"], R["phase2"], R["phase3"], R["fulltext"]
n = "{:,}".format

held = p1["snowball_held_no_abstract"]
unscreened_q = p1["query_unscreened"] - len(p3["query_unscreened_progressed"])
screened = sum(p1["query"].values()) + sum(p1["snowball"].values()) - held
advanced = p2["query_eligible"] + p2["snowball_s2opus"].get("keep", 0)
fm = p3["final_merged"]
C = {
    "identified": idn["identified_before_dedup"], "database": idn["  before_dedup_by_group"]["database"],
    "other": idn["  before_dedup_by_group"]["other_methods"], "snowball": idn["  before_dedup_by_group"]["snowball"],
    "dups": idn["duplicates_removed"], "unique": idn["unique_records"], "not_screened": held + unscreened_q,
    "held": held, "unscreened_q": unscreened_q, "screened": screened, "excluded": screened - advanced,
    "advanced": advanced, "triaged": sum(fm.values()), "context": fm.get("context", 0),
    "discard": fm.get("discard", 0), "triage_core": sum(v for k, v in fm.items() if "core" in k),
    "fulltext": ft["core_entering_fulltext"], "demoted": ft["demoted_to_context"],
    "pending": len(ft["not_demoted_without_human_primary"]), "included": ft["phase6_collection"],
}

FONT = ["Arial", "Liberation Sans", "Helvetica", "DejaVu Sans"]  # Arial-metric fallback
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = FONT
plt.rcParams["svg.fonttype"] = "none"   # editable text in SVG; Word renders it as Arial

BODY = 9      # pt, printed
STAGE = 9.5   # pt, printed

fig, ax = plt.subplots(figsize=(6.5, 8.0))
ax.set_xlim(0, 101)
ax.set_ylim(0, 118)
ax.axis("off")


def box(x, y, w, h, text):
    ax.add_patch(Rectangle((x, y), w, h, linewidth=0.9, edgecolor="black", facecolor="white"))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=BODY, linespacing=1.3)


def arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", lw=0.9, color="black",
                                shrinkA=0, shrinkB=0, mutation_scale=9))


def stage(y, h, label):
    ax.add_patch(Rectangle((0, y), 7, h, linewidth=0, facecolor="#d9d9d9"))
    ax.text(3.5, y + h / 2, label, ha="center", va="center", fontsize=STAGE,
            rotation=90, fontweight="bold")


LX, LW = 10, 47
RX, RW = 61, 39.5
lcx = LX + LW / 2

# Identification
stage(84, 33, "Identification")
box(LX, 87, LW, 28,
    f"Records identified\n(n = {n(C['identified'])})\n\n"
    f"Database searches (n = {n(C['database'])})\n"
    f"Other methods: committee,\ncoursework, practitioner\nnetwork (n = {n(C['other'])})\n"
    f"Citation snowballing (n = {n(C['snowball'])})")
box(RX, 95, RW, 12, f"Duplicate records\nremoved (n = {n(C['dups'])})\nUnique records\n(n = {n(C['unique'])})")
arrow(LX + LW, 101, RX, 101)

# Screening
stage(52, 30, "Screening")
box(RX, 69, RW, 13,
    f"Records not screened (n = {n(C['not_screened'])})\n"
    f"No abstract after\nenrichment (n = {n(C['held'])})\n"
    f"Query records (n = {n(C['unscreened_q'])})")
ax.plot([lcx, RX], [75.5, 75.5], color="black", lw=0.9)
arrow(lcx + 0.01, 75.5, RX, 75.5)
box(LX, 55, LW, 10, f"Records screened on title\nand abstractᵃ (n = {n(C['screened'])})")
arrow(lcx, 87, lcx, 65)
box(RX, 55, RW, 10, f"Records excluded\n(n = {n(C['excluded'])})")
arrow(LX + LW, 60, RX, 60)

# Eligibility
stage(19, 31, "Eligibility")
box(LX, 37, LW, 10, f"Records assessed in\nrelevance triageᵇ (n = {n(C['triaged'])})")
arrow(lcx, 55, lcx, 47)
box(RX, 35, RW, 14, f"Classified at abstract level\nContext (n = {n(C['context'])})\nDiscarded (n = {n(C['discard'])})")
arrow(LX + LW, 42, RX, 42)
box(LX, 21, LW, 10, f"Core studies assessed\nin full textᶜ (n = {n(C['fulltext'])})")
arrow(lcx, 37, lcx, 31)
right = f"Reclassified as context after\nfull-text review (n = {n(C['demoted'])})"
if C["pending"]:
    right += f"\nDecision pending (n = {C['pending']})"
box(RX, 21, RW, 10, right)
arrow(LX + LW, 26, RX, 26)

# Included
stage(2, 15, "Included")
box(LX, 4.5, LW, 10, f"Studies included in review\n(n = {n(C['included'])})")
arrow(lcx, 21, lcx, 14.5)

os.makedirs(OUT, exist_ok=True)
fig.savefig(f"{OUT}/PRISMA_Flow_Diagram.png", dpi=300, bbox_inches="tight", pad_inches=0.05)
fig.savefig(f"{OUT}/PRISMA_Flow_Diagram.svg", bbox_inches="tight", pad_inches=0.05, metadata={"Date": None})

# Light/dark adaptive SVG (web, GitHub, Markdown viewers). Colors stay literal (light) so renderers
# without CSS support (Quick Look, Word) show black-on-white; browsers override in dark mode.
STYLE = """<style>
  @media (prefers-color-scheme: dark) {
    [style*="fill: #ffffff"] { fill: #1e1e1e !important; }
    [style*="fill: #d9d9d9"] { fill: #3a3a3a !important; }
    [style*="stroke: #000000"] { stroke: #e6e6e6 !important; }
    [style^="stroke: #000000"] { fill: #e6e6e6 !important; }
    text { fill: #e6e6e6 !important; }
  }
</style>"""
svg = open(f"{OUT}/PRISMA_Flow_Diagram.svg").read()
svg = re.sub(r"(<svg[^>]*>)", r"\1\n" + STYLE, svg, count=1)
open(f"{OUT}/PRISMA_Flow_Diagram_adaptive.svg", "w").write(svg)
print(json.dumps(C))
