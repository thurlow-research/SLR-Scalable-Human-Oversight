#!/usr/bin/env python
"""Stage 3 QA scorer — agreement analysis across Opus / codex / gemini (+ human).

Joins the three model legs on the shared 250 sample and the blinded human 50, then:
  1. Validates coverage per leg (any missing item_key is reported).
  2. TRUST CHECK (gate): Opus vs human on the 50 — Cohen's κ (3-way bin) + confusion
     matrix + core↔discard CROSSOVERS (a real false-negative/positive). Any crossover
     blocks auto-apply and lands in adjudicate.csv.
  3. CROSS-MODEL: pairwise Cohen's κ on the 250 (3-way bin) for every model pair, plus
     Spearman rank correlation on centrality (this is an ordinal pass).
  4. Writes qa/adjudicate.csv = every item the three legs don't unanimously agree on,
     plus the Context↔Discard border band — the human-decision worklist. Where all
     three agree, the item auto-classifies (not written to the worklist).

Pure stdlib (κ and Spearman implemented inline) — matches the stdlib-only venv.
Human sheet is optional: if human_review_50.csv has no filled bins yet, the Trust
Check is skipped with a notice and the cross-model analysis still runs.

Usage:  python stage3_qa_score.py --outdir work
"""
import argparse
import csv
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

BINS = ["core", "context", "discard"]
BORDER_LO, BORDER_HI = 25, 40   # Context↔Discard border band (centrality), human-reviewed


def cohen_kappa(pairs):
    """pairs = list of (label_a, label_b). Returns (kappa, Po, n)."""
    pairs = [(a, b) for a, b in pairs if a and b]
    n = len(pairs)
    if not n:
        return None, None, 0
    po = sum(1 for a, b in pairs if a == b) / n
    ma, mb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum((ma[c] / n) * (mb[c] / n) for c in set(ma) | set(mb))
    kappa = (po - pe) / (1 - pe) if pe != 1 else 1.0
    return kappa, po, n


def _ranks(xs):
    """Average (fractional) ranks, tie-aware."""
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(xs):
        j = i
        while j + 1 < len(xs) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2 + 1
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def spearman(pairs):
    pairs = [(a, b) for a, b in pairs if a is not None and b is not None]
    n = len(pairs)
    if n < 2:
        return None, 0
    ra, rb = _ranks([a for a, _ in pairs]), _ranks([b for _, b in pairs])
    mra, mrb = sum(ra) / n, sum(rb) / n
    num = sum((ra[i] - mra) * (rb[i] - mrb) for i in range(n))
    da = sum((r - mra) ** 2 for r in ra) ** 0.5
    db = sum((r - mrb) ** 2 for r in rb) ** 0.5
    return (num / (da * db) if da and db else None), n


def load(path, keycol="item_key"):
    if not Path(path).exists():
        return {}
    return {r[keycol]: r for r in csv.DictReader(open(path, encoding="utf-8"))}


def interp(k):
    if k is None:
        return "n/a"
    for thr, lbl in [(.81, "almost perfect"), (.61, "substantial"), (.41, "moderate"),
                     (.21, "fair"), (0, "slight"), (-1, "poor")]:
        if k >= thr:
            return lbl


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default="work")
    args = ap.parse_args()
    qa = Path(args.outdir) / "qa"

    master = load(qa / "qa_master_250.csv")
    codex = load(qa / "codex_out_250.csv")
    gemini = load(qa / "gemini_out_250.csv")
    human = load(qa / "human_review_50.csv")

    legs = {"opus": master, "codex": codex, "gemini": gemini}
    keys = list(master)
    print(f"master 250: {len(master)}  |  codex: {len(codex)}  gemini: {len(gemini)}"
          f"  human: {sum(1 for r in human.values() if (r.get('bin') or '').strip())}"
          f"/{len(human)} filled")

    # 1. coverage
    for name, leg in (("codex", codex), ("gemini", gemini)):
        miss = [k for k in keys if k not in leg]
        if miss:
            print(f"  !! {name} missing {len(miss)} keys: {', '.join(miss[:8])}"
                  f"{' ...' if len(miss) > 8 else ''}")

    def b(leg, k):
        return (leg.get(k, {}).get("bin") or "").strip().lower()

    def c(leg, k):
        v = (leg.get(k, {}).get("centrality") or "").strip()
        return int(v) if v.lstrip("-").isdigit() else None

    # 2. Trust Check (gate) — Opus vs human on the 50
    hkeys = [k for k in human if (human[k].get("bin") or "").strip()]
    print("\n── TRUST CHECK (gate): Opus vs human on the 50 ──")
    crossovers = []
    if hkeys:
        pairs = [(b(master, k), (human[k]["bin"] or "").strip().lower()) for k in hkeys]
        k_th, po, n = cohen_kappa(pairs)
        print(f"  n={n}  Po={po:.1%}  κ={k_th:.3f} ({interp(k_th)})")
        print("  confusion (rows=Opus, cols=human):")
        conf = defaultdict(Counter)
        for o, h in pairs:
            conf[o][h] += 1
        print("            " + "".join(f"{x:>9}" for x in BINS))
        for o in BINS:
            print(f"    {o:>8}" + "".join(f"{conf[o][h]:>9}" for h in BINS))
        crossovers = [k for k in hkeys
                      if {b(master, k), (human[k]['bin'] or '').lower()} == {"core", "discard"}]
        print(f"  core↔discard crossovers (block auto-apply): {len(crossovers)}"
              + (f" -> {', '.join(crossovers)}" if crossovers else ""))
    else:
        print("  (human sheet not filled yet — skipping; fill human_review_50.csv then re-run)")

    # 3. Cross-model agreement on the 250
    print("\n── CROSS-MODEL: pairwise κ (bin) + Spearman (centrality) on the 250 ──")
    for a, bb in combinations(legs, 2):
        kp, po, n = cohen_kappa([(b(legs[a], k), b(legs[bb], k)) for k in keys])
        sp, ns = spearman([(c(legs[a], k), c(legs[bb], k)) for k in keys])
        sp_s = f"{sp:+.3f}" if sp is not None else "n/a"
        print(f"  {a:>6} vs {bb:<6}  κ={kp:.3f} ({interp(kp)}, Po={po:.1%})   ρ={sp_s}")

    # 4. Consensus + adjudication worklist
    print("\n── CONSENSUS across the 3 legs ──")
    rows_adj, tally = [], Counter()
    for k in keys:
        votes = [b(master, k), b(codex, k), b(gemini, k)]
        present = [v for v in votes if v]
        cnt = Counter(present)
        top, ntop = cnt.most_common(1)[0]
        if ntop == len(present) and len(present) == 3:
            agree = "3/3"
        elif ntop >= 2:
            agree = "2/3"
        else:
            agree = "split"
        tally[agree] += 1
        cent_o = c(master, k)
        border = cent_o is not None and BORDER_LO <= cent_o <= BORDER_HI
        # span==2 => at least one leg said core and another said discard (high severity)
        ords = [BINS[::-1].index(v) for v in present]  # discard=0,context=1,core=2
        model_crossover = present and (max(ords) - min(ords) == 2)
        reasons = []
        if agree != "3/3":
            reasons.append("disagreement")
        if border:
            reasons.append("border")
        if model_crossover or k in crossovers:
            reasons.append("crossover")
        if reasons:
            rows_adj.append({
                "item_key": k, "title": master[k].get("title", ""),
                "agreement": agree, "reason": "+".join(reasons),
                "opus_bin": b(master, k), "opus_cent": cent_o if cent_o is not None else "",
                "codex_bin": b(codex, k), "codex_cent": c(codex, k) if c(codex, k) is not None else "",
                "gemini_bin": b(gemini, k), "gemini_cent": c(gemini, k) if c(gemini, k) is not None else "",
                "human_bin": (human.get(k, {}).get("bin") or "").strip().lower(),
                "consensus": top if agree != "split" else "",
            })
    print(f"  {dict(tally)}  (3/3 auto-classify; 2/3 majority w/ flag; split -> adjudicate)")

    dst = qa / "adjudicate.csv"
    cols = ["item_key", "title", "agreement", "reason", "consensus",
            "opus_bin", "opus_cent", "codex_bin", "codex_cent",
            "gemini_bin", "gemini_cent", "human_bin"]
    # crossovers first (highest severity), then by disagreement breadth.
    rows_adj.sort(key=lambda r: (0 if "crossover" in r["reason"] else 1,
                                 {"split": 0, "2/3": 1, "3/3": 2}[r["agreement"]], r["reason"]))
    with open(dst, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows_adj)
    print(f"\nwrote {dst}  ({len(rows_adj)} items need human decision; "
          f"{len(keys) - len(rows_adj)} auto-classify on 3/3 agreement)")
    if not hkeys:
        print("NOTE: Trust Check gate not evaluated — fill human_review_50.csv and re-run before applying s3:* tags.")


if __name__ == "__main__":
    main()
