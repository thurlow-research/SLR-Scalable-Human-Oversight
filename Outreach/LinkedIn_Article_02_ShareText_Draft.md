# LinkedIn Article 02 — share text ("9,518 papers later")

**Status:** draft, not posted. **Drafted:** 2026-08-29.
**Angle:** solution-side findings from the SLR — the follow-up teased at the end of Article 01. Problem
was defined there; this is what the literature does and does not actually establish.
**Role: SHARE COMMENTARY** for Article 02 — the text that appears in the feed above the article
card. Pairs with `LinkedIn_Article_02_SLR_Findings_Draft.md`, which carries the evidence,
the method and the practical recommendations. This post names *what* was found; the article shows
*why it holds*. It must open a curiosity gap, not close one.

**Flow:** contrarian claim → credibility numbers → three findings named but not proved →
self-implicating caveat → article link → question.

**Sequence:** **Article 01** (incident pattern — PUBLISHED) → **Article 02 (this — SLR findings)** →
**Post 03** (open questions → research questions) → later, after candidacy, the survey call.
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

## Draft — SHARE TEXT (drives to Article 02)

**If your answer to "is this AI-generated code safe to merge?" is several models voting, the evidence
says you built the weaker design.**

I spent the last several months screening 9,518 papers on how organisations keep human oversight of AI
coding from collapsing under volume. 147 read in full. 72 survived.

Three things worth your time:

**1. "Multi-agent" describes three different designs, and they don't perform alike.**
Agents voting on the same question. A critic judging another agent's output. Agents genuinely
challenging each other. The first is the intuitive one and the weakest — model errors correlate, so
agreement mostly measures shared blind spots. The second is where the measurable wins are. The third is
rare, and it's the only one that hands a human a *disagreement* to judge rather than a verdict to
rubber-stamp.

**2. Rubber-stamping is the default setting, not a discipline problem.**
One study watched engineers working with a coding agent and found their attention *declined as the task
went on*, narrowing to the "happy path" where everything works. The uncomfortable part: familiarity with
the tool appeared to make it worse, not better. Careful review is expensive. Skimming is free. Under
deadline, free wins — and no amount of telling people to try harder changes that.

**3. Which makes routing the whole game.**
You cannot review everything carefully; that's the arithmetic we started with. So the real question
isn't "how do we get people to review properly," it's **"which changes get the expensive kind of
attention, and what decides that?"** Of the 72 studies I kept, **four** were primarily about that. The
mechanism the entire problem turns on is one of the least-studied areas in the field.

And one finding that turned back on me. I used three models to screen this corpus. They agreed with
*each other* at Cohen's κ 0.49–0.64. They agreed with *me* at **κ = 0.30** — below the floor usually
considered acceptable for a systematic review. And where they disagreed with each other, that
disagreement predicted my judgment at **chance**. Models converging on each other is not the same as
models converging on the truth — which is Finding 1, arriving from inside my own method.

I've written the whole thing up: the numbers, the three designs side by side, and six things the
evidence actually supports doing if you're building or buying this right now — **[ARTICLE LINK]**

If you have AI writing code in your org today: what actually reaches a human, and who decided that?

## Structure rationale — driven by Article 01's analytics

Article 01 measured: **118,615 impressions · 97,668 members reached · 98% out-of-network · 221 social
engagements (149 reactions, 31 comments, 5 reposts) · 483 article views · 318 profile viewers · 63
followers gained.**

Four readings, each of which changed this draft:

1. **98% out-of-network.** Almost every reader is a stranger with no context. **The first line carries
   the entire post.** The share text therefore opens on a claim that is immediately useful to a practitioner
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

**Length: ~400 words**, per the arbiter's "long enough to make a point and tease, but under 500." An
earlier 219-word cut went too far — it named the findings without landing any of them, which buys a
click but leaves nothing if the click doesn't happen. Each finding now gets a claim plus the evidence
that makes it stick, and stops before it starts explaining.

**The signal I initially under-read: 32 SAVES against 5 reposts.** Saves mean *"useful to me, I'll come
back to this"* — high intent, low broadcast. Combined with 31 comments on 118k impressions, the picture
is: this audience treats the content as **reference material rather than conversation**. That argues
for concrete, specific, re-readable claims (numbers, named mechanisms, things you can act on) over
provocation — and it makes a six-recommendation article very saveable. The closing question stays,
because comments are the one metric that didn't move and it costs a line.

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
- Consider posting mid-week morning US time, matching whatever Article 01 used.
