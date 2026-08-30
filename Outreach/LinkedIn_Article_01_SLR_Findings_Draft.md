# LinkedIn Article 01 — "What 9,518 Papers Say About Overseeing AI-Generated Code"

**Status:** draft, not posted. **Drafted:** 2026-08-29.
**Pairs with:** `LinkedIn_Post_02_SLR_Findings_Draft.md` (the teaser that drives here).
**Images:** `assets/funnel.png` (after the methodology paragraph) · `assets/two-mechanisms.png`
(inside Finding 1). Both 2400×1350.

**Sources / fact-check:** see the Sources block in the Post 02 draft — same figures, same verification,
all confirmed 2026-08-29 against the live library and the published versions of each paper.

⚠ **Do not publish** the "1 of 72 papers clears the strict leakage test" figure as settled. It rests on
one strict definition with 144 panel flags still unadjudicated. Phrased below as *"rarely measured to a
standard that would survive scrutiny,"* which is defensible now.

---

## Draft

# What 9,518 Papers Say About Overseeing AI-Generated Code

Code production now scales with compute. Code *inspection* still scales with the number of qualified
engineers and the hours they can spend reading diffs.

In ordinary engineering practice, riskier work attracts more scrutiny. With AI-generated code the
curves appear to cross: the artifact is measurably riskier, and it receives *less* attention. I've
spent the last several months trying to establish what is actually known about that — not what people
assert, but what has been demonstrated.

Here is what the literature does and does not support.

### How I got here

Five databases, plus backward citation snowballing. A deliberately loose recall screen first, then a
tighter precision screen on titles and abstracts, then full-text reading of everything that survived.
Tagging used a fixed instrument with a three-model panel proposing labels and me adjudicating every
one — model proposals are evidence, not decisions. 9,518 unique records went in; 147 studies were read
in full; **72 survived close reading**.

> **[IMAGE: assets/funnel.png]**

That attrition is worth pausing on. Roughly half the full-text corpus was cut once I read it properly,
and consistently more aggressively than the model panel recommended. A great deal of published work on
"AI coding oversight" turns out, on inspection, to be about something narrower — usually a review tool.

### Finding 1: "Multi-agent" describes two opposite designs

This is the one I'd hand to anyone building these systems today.

The intuitive design is **redundancy**: run several models over the same diff, and treat agreement as
confidence. It feels like a second opinion. The evidence is unkind to it. In one study, convergence
between models improved acceptance by **2.4 percentage points**. Another benchmarked unanimous
committees of one to six LLM judges and found their errors were *correlated* — so agreement largely
measures shared blind spots rather than correctness.

The design that works is **adjudication**: a second stage that asks a *different* question — not "do
you also think this is a bug?" but "is this finding actually valid?" In the same study, the arbitration
phase cut code-change surface by **83–90%**, enforcing minimal fixes over scope-expanding ones. A
production system at ByteDance added a validation stage in front of developers specifically because the
first stage hallucinated, and reached 75% precision with 12,000+ weekly users. Another paper dropped a
false-positive rate from **88.7% to 40.0%** by validating verdicts against executable evidence instead
of a second model's opinion.

> **[IMAGE: assets/two-mechanisms.png]**

Same label. Opposite results. Most papers don't separate them — and neither did my own taxonomy until
three weeks ago, which is how I know the distinction is easy to miss.

There's a second-order version of this worth naming. Among systems that do use a checking stage, almost
all use **one-directional** critique: a dedicated critic reviewing a producer's output. Agents actually
checking *each other* — mutual critique — is rare in the literature. Whether that's a gap or a signal
is exactly what I'd like to find out.

### Finding 2: The problem is widely asserted and rarely measured

The premise — riskier code, less scrutiny — is now repeated as settled. Some of the evidence is real
and specific. One study of open source repositories found **79% of merged human+AI pull requests
received no external review or comment at all**, and that the usual pattern inverts: contributors
without prior ownership normally attract the *most* feedback, but for AI-assisted work they attract the
*least*.

That is a genuine finding. But much of the surrounding literature reaches for *volume* as proof, and
volume is a different claim. Reviewer overload is not evidence that defects reached production. To show
oversight is failing you need either observed absence of review, or defects in merged code with review
failure as the cause — and the second is rarely done. Even the strongest study above stops short: the
authors note that the unreviewed pull requests may simply be targeting easier work, and say plainly
that they did not test it.

So the problem is real, and the evidence for it is thinner than its confidence suggests. That gap is
not a reason to dismiss the concern. It's a reason to go measure it properly.

### Finding 3: The field is solution-heavy and evidence-thin

There is no shortage of proposed mechanisms — gates, panels, rubrics, risk scores, provenance
tracking. What is nearly absent is any account of what organizations actually *do*. Mechanisms get
built and demonstrated in research settings; very few are observed inside a firm, under production
pressure, with real reviewers who have other work.

That's the gap my own research is aimed at, so I'm not neutral about it. But it held up: after reading
147 studies closely, I can describe dozens of designs and almost no practices.

### What the evidence actually supports doing

Five things I'd act on if I were building or buying AI coding tooling tomorrow. Each is grounded in the
studies above rather than in my own preferences — which is also why the list is shorter than you might
expect.

**1. Make the second stage ask a different question.** If your pipeline's answer to "is this reliable?"
is *more models voting*, you are paying for the mechanism with the weakest evidence behind it. A
validation stage that asks "is this finding valid?" is the one that keeps showing measurable results.

**2. Stop treating agreement as confidence.** Unanimity across models is not independent
confirmation when the models share training data, prompt framing, and failure modes. If you use
convergence as a quality gate, you are measuring consensus, not correctness.

**3. Choose complementary checkers, not more of them.** The committee study found conservatism hits
diminishing returns as size grows, and that *composition* mattered more than count. If you run three
models, you should be able to say how they fail *differently* — and ideally have measured it. Adding a
third model that fails like the first two buys nothing.

**4. Let code make the decision; let the model produce the evidence.** Several of the better-performing
designs have models emit findings or scores while deterministic code decides accept / reject /
escalate. A threshold can be moved, tested and explained; a model's verdict cannot. It also means the
check can't be skipped — instruction-following is probabilistic, a state transition isn't.

**5. Use the boring tools where they apply.** Linters, scanners, type checkers and test suites have
knowable, stable error profiles. Don't spend an LLM call on something a deterministic check already
does reliably — and don't call a rubric "rules-based" if a model is the one scoring it. Those two have
very different failure behaviour, and conflating them is how a pipeline ends up less predictable than
it looks.

And one decision to make explicitly rather than by accident: **what is your gate protecting?**
Protecting the codebase means blocking more and interrupting people more. Protecting attention means
letting more through. Those are opposite tunings of the same architecture. The most successful
deployment I found chose precision over recall deliberately, and accepted that it would miss things.
Choosing by default is how teams end up with a gate nobody trusts and everybody routes around.

### One caveat I have to state

I used a three-model panel to help tag this corpus. On the *contested* calls — the ones where the
models proposed something I hadn't — they were right about **half the time**.

In a review partly about the limits of machine agreement, that finding applies to my own instrument.
It's also the practical argument for the adjudication pattern above: the panel was useful precisely
because a human asked a different question of its output, rather than counting how many models agreed.

### What I'd like to know

If you're running AI review over real diffs today: are your models answering the **same** question, or
**different** ones? And does anyone check whether the flagged issues were real?

I'll be writing next about what this implies for building oversight that actually scales.

---

## Notes

- Target length ~1,050 words. LinkedIn articles hold attention to roughly 1,200; don't grow it.
- Both images are essential, not decorative — the funnel carries credibility, the two-mechanism diagram
  carries the argument. Place them exactly where marked.
- No participant recruitment, per the content plan — that holds until after candidacy.
- Paper names are deliberately omitted from the body to keep it readable; add a short "sources" note at
  the end of the LinkedIn article if comments ask, or link the eventual preprint.
