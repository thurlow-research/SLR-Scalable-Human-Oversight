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

**If your AI code review runs several models and takes the majority vote, the evidence says you built
the weaker design.**

I spent the last several months reading everything I could find on keeping human oversight of
AI-generated code from collapsing under volume. 9,518 papers screened. 147 read in full. 72 survived.

Here is the finding I did not expect.

**"Multiple AI reviewers" describes two opposite things.**

*Redundancy* — several models answering the same question, then aggregating — is the intuitive design.
The evidence is unkind to it. In one study, cross-model convergence improved acceptance by **2.4
percentage points**. Model errors turn out to be correlated, so agreement largely measures shared blind
spots rather than correctness.

*Adjudication* — a second stage asking a **different** question, checking the first stage's output —
behaves nothing like it. The same study's arbitration phase cut code-change surface by **83–90%**.
Another dropped a false-positive rate from **88.7% to 40.0%** by validating verdicts against executable
evidence rather than asking a second model whether it agreed.

Same "multi-agent" label. Opposite results. Most papers don't separate them — and neither did my own
taxonomy until three weeks ago.

**The second finding is about the problem itself, not the solutions.**

That AI-generated code is riskier yet gets less scrutiny is now repeated as settled. Some of the
evidence is real: one study found **79% of merged human+AI pull requests received no external review or
comment at all**. But most papers reach for *volume* as proof — and volume is not the same claim.
Reviewer overload is not evidence that defects got through. Those need different measurements, and the
second one is rarely done.

**One caveat I have to state.** I used a three-model panel to help tag this corpus. On the contested
calls — where the models proposed something I hadn't — they were right **about half the time**. In a
review partly *about* the limits of machine agreement, that applies to my instrument too.

If you're running multiple models over the same diff today: are they answering the same question, or
different ones? I'd genuinely like to know what's working in practice.

---

## Structure rationale — driven by Post 01's analytics

Post 01 measured: **118,615 impressions · 97,668 members reached · 98% out-of-network · 221 social
engagements (149 reactions, 31 comments, 5 reposts) · 483 article views · 318 profile viewers · 63
followers gained.**

Four readings, each of which changed this draft:

1. **98% out-of-network.** Almost every reader is a stranger with no context. **The first line carries
   the entire post.** Post 02 therefore opens on a claim that is immediately useful to a practitioner
   and mildly arguable, not on the funnel statistic. "9,518 papers" is a *credibility* line, so it now
   sits in the second paragraph where it does that job instead.
2. **0.19% engagement against enormous reach.** It travelled but didn't provoke — 31 comments on 118k
   impressions. The post informed rather than invited. Hence the **closing question**, and hence
   leading with the finding people can disagree with.
3. **483 article views = 0.4% click-through.** Readers do not leave the post. **All substance stays
   inline; never put the argument behind a link.**
4. **63 followers and 318 profile views from one post.** The credibility signal worked. Keep the
   self-implicating caveat — the "my panel was right about half the time" line is what makes the rest
   trustworthy, and it costs nothing.

**Cut from the earlier draft:** the "solution-heavy, evidence-thin" finding. True and central to the
dissertation, but the least surprising of the three to a practitioner audience, and the post was long.
It belongs in Post 03.

**Ordering:** contrarian-and-useful → credibility → the problem claim → self-implicating caveat →
question.

## Notes for revision

- Numbers are rounded for readability (88.7/40.0). Exact figures in Sources above.
- No participant recruitment, per the content plan — that holds until after candidacy.
- The opener is deliberately a little combative. If it reads as too much, the softer version is:
  *"If your AI code review runs several models and takes the majority vote, the evidence is not on
  your side."*
- Consider posting mid-week morning US time, matching whatever Post 01 used.
