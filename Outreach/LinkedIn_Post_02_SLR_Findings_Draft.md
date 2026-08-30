# LinkedIn Post 02 — "9,518 papers later"

**Status:** draft, not posted. **Drafted:** 2026-08-29.
**Angle:** solution-side findings from the SLR — the follow-up teased at the end of Post 01. Problem
was defined there; this is what the literature does and does not actually establish.
**Flow:** funnel stat as hook → one-line method → three findings, strongest last → honest limitation →
what's next.

**Sequence note:** Post 01 (incident pattern) → **Post 02 (this, SLR findings)** → Post 03 (HOS
insights). **No call for survey participants** — that stays held until after candidacy.

---

## Sources (fact-check before posting)

All figures verified 2026-08-29 against the live Zotero library and `slr-phase4/data/f2_census.json`.

- Funnel: 9,518 unique records → 4,061 (recall screen) → 983 eligible (precision screen) → 147 studies
  at full text → 72 retained. `Knowledge Xfer/SLR_CONTEXT.md` §6; Phase 6 = `R9ZHDXMN`.
- **79.0%** of merged Human+AI PRs received no external review or comment — Gao et al. (2026), MSR '26,
  pp. 777–781, DOI 10.1145/3793302.3793573. *Verified in the published version.*
- **88.74% → 39.96%** false-positive rate after a verification filter — Jin & Chen (2026), *Automated
  Software Engineering* 33:90, DOI 10.1007/s10515-026-00638-5. *Verified in the published version.*
- **2.4 percentage points** acceptance gain from cross-model convergence, vs **83–90%** reduction in
  code-change surface from the arbitration phase — Vargas (2025), SLEAN, arXiv:2510.10010.
- Panel precision on contested tags: 7 of 14 — own measurement, Set A/B residual, 2026-08-29.
- ⚠ **Do not publish** the "1 of 72" inversion figure as settled — it rests on one strict definition
  and 144 flags are still unadjudicated. Phrased below as "rarely measured," which is defensible.

---

## Draft

**9,518 papers on AI code review. 72 that survived a close read.**

I've spent the last several months on a systematic review of how organizations keep human oversight of
AI-generated code from collapsing under volume. Search across five databases, two screening passes,
then full-text reading of what was left — 147 studies, of which 72 held up.

Three things stand out, and the third is the one I did not expect.

**1. The field is solution-heavy and evidence-thin.**
There is no shortage of proposed mechanisms — gates, panels, rubrics, risk scores. There is very little
account of what any organization actually *does*. Mechanisms get demonstrated in research settings and
almost never observed in a firm.

**2. The problem is widely asserted and rarely measured.**
The premise — that AI-generated code is riskier yet gets less scrutiny — is repeated constantly. The
strongest evidence is real: one study found **79% of merged human+AI pull requests received no external
review or comment at all**. But most papers reach for *volume* as proof, and volume is not the same
thing. Pressure on reviewers isn't evidence that defects got through. Those are different claims and
they need different measurements.

**3. "Multiple AI reviewers" describes two opposite things.**
This is the finding I'd hand to anyone building these systems today.

*Redundancy* — several models answering the same question, then aggregating — reads as the obvious
design. The evidence is unkind to it. In one study, cross-model convergence improved acceptance by
**2.4 percentage points**. Model errors turn out to be correlated, so agreement mostly measures shared
blind spots.

*Adjudication* — a second stage asking a **different** question, checking the first stage's output —
performs very differently. The same study's arbitration phase cut code-change surface by **83–90%**.
Another cut a false-positive rate from **88.7% to 40.0%** by validating verdicts against executable
evidence.

Same "multi-agent" label. Opposite results. Most papers don't distinguish them — and neither did my own
taxonomy until three weeks ago.

**A caveat I have to state.** I used a three-model panel to help tag this corpus. On the contested
calls — where the models proposed something I hadn't — they were right **about half the time**. That is
a useful reminder in a review partly *about* the limits of machine agreement: it applies to my
instrument too.

Next up: what this implies for actually building oversight that scales.

---

## Notes for revision

- Consider trimming finding 1 — it's the least surprising and the post runs long for LinkedIn.
- The "neither did my own taxonomy" line is the credibility move; keep it.
- Numbers are rounded for readability (88.7/40.0). Exact figures in Sources above.
- No participant recruitment, per the content plan.
