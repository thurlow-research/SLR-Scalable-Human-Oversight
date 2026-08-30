# LinkedIn Post 02 — "9,518 papers later"

**Status:** draft, not posted. **Drafted:** 2026-08-29.
**Angle:** solution-side findings from the SLR — the follow-up teased at the end of Post 01. Problem
was defined there; this is what the literature does and does not actually establish.
**Role: TEASER.** Pairs with `LinkedIn_Article_01_SLR_Findings_Draft.md`, which carries the evidence,
the method and the practical recommendations. This post names *what* was found; the article shows
*why it holds*. It must open a curiosity gap, not close one.

**Flow:** contrarian claim → credibility numbers → three findings named but not proved →
self-implicating caveat → article link → question.

**Sequence:** Post 01 (incident pattern, posted) → **Post 02 + Article 01 (this — SLR findings)** →
Post 03 (open questions → research questions) → later, after candidacy, the survey call.
**No recruitment in any of these.**

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

## Draft — TEASER (drives to Article 01)

**If your answer to “is this AI-generated code safe to merge?” is several models voting, the evidence
says you built the weaker design.**

AI writes code faster than anyone can read it. The interesting problem isn't making the machine
check better — it's **deciding what still needs a human, and making sure those things actually reach
one.**

I screened 9,518 papers looking for what's known about that. 147 read in full. 72 survived.

Three things came out of it:

→ **"Multi-agent review" describes two opposite designs**, and they don't perform remotely alike. One
is the intuitive one. It's the weaker one — and if it's the reason you've reduced human review, you've
removed the human and kept the error. Most papers don't separate the two. Neither did my own taxonomy
until three weeks ago.

→ **The problem everyone cites is far less measured than it sounds.** The strongest study I found is
genuinely alarming. Its authors also name an alternative explanation for their own headline result —
and say plainly they didn't test it.

→ **The field is solution-heavy and evidence-thin.** After 147 close reads I can describe dozens of
oversight mechanisms and almost no actual practices.

And one finding that turned back on me: I used a three-model panel to help tag the corpus. On the
contested calls, it was right about **half the time**. In a review partly about the limits of machine
agreement, that applies to my own instrument too.

I've written the whole thing up — the numbers, the two designs side by side, how the corpus was built,
and **five things the evidence actually supports doing** if you're building or buying AI coding tooling
right now: **[ARTICLE LINK]**

If you have AI writing code in your org today: when something checks it, is it answering the *same*
question the generator did, or a *different* one?

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

**Revised again once the article existed.** The first version summarised the findings *completely*,
which makes a good standalone post and a poor teaser — the arbiter's note was that the last one "didn't
tease enough." Findings are now **named without being proved**: the two designs are contrasted but the
numbers live in the article; the review-absence study is characterised but not quoted. The reader gets
real value and a specific reason to click.

**On the 0.4% click-through:** that is not evidence links fail. It is evidence the previous post closed
the gap it should have opened. The fix is a better gap, not fewer links.

**Ordering:** contrarian-and-useful → credibility → three named findings → self-implicating caveat →
article → question.

## Notes for revision

- Numbers are rounded for readability (88.7/40.0). Exact figures in Sources above.
- No participant recruitment, per the content plan — that holds until after candidacy.
- The opener is deliberately a little combative. If it reads as too much, the softer version is:
  *"If your answer to “is this AI-generated code safe to merge?” is several models voting, the evidence
  is not on your side."*
- Consider posting mid-week morning US time, matching whatever Post 01 used.
