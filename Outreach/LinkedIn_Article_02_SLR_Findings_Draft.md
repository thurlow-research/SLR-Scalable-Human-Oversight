# LinkedIn Article 02 — "What 9,518 Papers Say About Overseeing AI-Generated Code"

**Status:** draft, not posted. **Drafted:** 2026-08-29.
**Pairs with:** `LinkedIn_Article_02_ShareText_Draft.md` — the feed commentary that drives here.
**Images:** `assets/funnel.png` (after the methodology paragraph) · `assets/mechanisms.png`
(inside Finding 1). Both 2400×1350. *Superseded, kept as provenance: `two-mechanisms.png` collapsed
mutual critique into adjudication; `three-mechanisms.png` lacked the orchestration axis.*

**Screening reliability figures** (added 2026-08-29), all from `Methodology/`: cross-model pairwise
Cohen's κ **0.49–0.64** and Spearman ρ ≈ 0.69 on a 250-item sample (`SLR_Status_Update_2026-07-08.md`);
blinded human Trust Check n=50, binary keep/discard **κ = 0.30**, reproducing the Pass-1 pilot at
**κ = 0.27**, both below the **0.4** IRR floor (same file, and `screening_multimodel_results.md`:
"all human/LLM pairs fell below κ=0.4"); model dissent vs human **κ ≈ 0.01–0.04**
(`Selection_Criteria_By_Phase.md` §210). **Note for accuracy:** the κ = 0.79 figure elsewhere in the
methodology is the *unblinded human Pass-2 trust check*, NOT model-human agreement — do not mix them.

**Sources / fact-check:** see the Sources block in `LinkedIn_Article_02_ShareText_Draft.md` — same figures, same verification,
all confirmed 2026-08-29 against the live library and the published versions of each paper. **Added
2026-08-29:** the System 1 / System 2 material is Catalan et al. (`5BAZZWHG`), *"I'm Not Reading All of
That"* — engagement "consistently declines as tasks" progress; attention centres on the "happy path";
explicitly framed against "the dual-process cognitive theory of System 1 thinking"; prior tool
experience "may have encouraged them to stay on System 1 thinking"; cognitive forcing designs proposed
as the remedy. **Routing count: four of the 72 retained studies** carry risk-routing as their primary
theme — re-verify at closeout.

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

The question underneath all of it isn't how to make machine checking better. It's **how a human stays
meaningfully in control of work they can no longer read all of.** Telling reviewers to try harder
doesn't survive the arithmetic, and it doesn't survive the psychology either — automation complacency
shows up precisely under these conditions, in experts and novices alike, and resists training.

So the real design problem is allocation: **what can be safely handed to a machine, so that human
attention lands where it actually changes the outcome?** Every finding below is a partial answer to
that, or a warning about answering it wrong.

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

### Finding 1: "Multi-agent" describes three different designs

This is the one I'd hand to anyone building these systems today.

**Redundancy** is the intuitive design: run several agents over the same diff and treat agreement as
confidence. It feels like a second opinion. The evidence is unkind to it. In one study, convergence
between models improved acceptance by **2.4 percentage points**. Another benchmarked unanimous
committees of one to six LLM judges and found their errors were *correlated* — so agreement largely
measures shared blind spots rather than correctness.

**One-way critique** asks a *different* question: not "do you also think this is a bug?" but "is this
finding actually valid?" This is where the measurable results are. A production system at ByteDance put
a validation stage in front of developers specifically because the first stage hallucinated, and
reached 75% precision with 12,000+ weekly users. Another paper dropped a false-positive rate from
**88.7% to 40.0%** by validating verdicts against executable evidence rather than a second model's
opinion. This is the common shape in the literature.

**Mutual critique** is the third, and the rarest: agents that read *each other's* work and challenge
it, converging or escalating rather than voting. One pipeline I looked at runs all three in sequence —
independent audits, then cross-critique where each provider reads the other's assessment, then
arbitration. Its arbitration phase cut code-change surface by **83–90%**, though that figure belongs to
the whole downstream stack, not to any single stage. In the corpus overall, nearly all critique is
one-way; mutual designs are scarce enough that I'd call the space largely unstudied.

> **[IMAGE: assets/mechanisms.png]**

And none of the three answers a separate question: **who decides whether any of it runs?** If a model
controls the flow, it can skip the check or ignore the result — instruction-following is probabilistic.
If code controls it, the check happens whether the model would have chosen it or not. About one in
seven of the studies I kept build that way. It's orthogonal to the topologies above, and the stronger
systems combine them: a fixed sequence of phases, with agents critiquing each other inside it.

Same label. Very different mechanisms. Most papers don't separate them — and neither did my own
taxonomy until three weeks ago, which is how I know the distinction is easy to miss.

**Why this matters for human oversight specifically.** Which design you built determines *what you can
stop looking at*. If you reduce human review because three models agreed, you reduced it on the basis
of correlated blind spots — you removed the human and kept the error. If you reduce it because a
validation stage suppressed false positives, you removed work that was genuinely noise. **One buys you
scale; the other buys you the appearance of it.**

And mutual critique changes something else — not how much reaches a human, but *what*. A voting system
hands a person a verdict to accept or override, which is exactly the situation where rubber-stamping
takes over. A system where agents genuinely disagree hands a person a **disagreement**: two positions,
the reasoning behind each, and a decision that actually requires judgment. One paper does precisely
this, presenting the full debate to a human decision-maker rather than a conclusion.

That's a much better use of a scarce reviewer than asking them to confirm what the machine already
decided. It is also the design the literature has least to say about.

### Finding 2: Human attention has two modes, and the cheap one is rubber-stamping

The most useful thing I read wasn't about AI at all. It was about how people read.

One study watched software engineers work with an agentic coding assistant and found their **cognitive
engagement consistently declined as the task went on**. What attention remained went to the "happy
path" — the sequence where everything works. Edge cases, failure modes and the assistant's reasoning
got progressively less.

The authors connect this to dual-process theory: **System 1** is fast, heuristic and cheap; **System 2**
is analytical, comprehensive and expensive. Reviewing a diff properly is System 2 work. Skimming it for
obvious breakage is System 1. And under time pressure, with an assistant that is usually right, System
1 is what you get. Rubber-stamping isn't a character flaw — it's the predictable equilibrium.

The detail that should worry anyone rolling these tools out: **familiarity made it worse.**
Participants' prior experience with the assistant appeared to *encourage* them to stay in System 1.
The longer a team uses the tool, the cheaper their reading of its output is likely to get.

**This is why routing is the whole problem.** You cannot run System 2 on everything — that's the
arithmetic we started with. But you also can't leave allocation to chance, because the default is the
shallow mode and it decays with familiarity. So the design question isn't "how do we get people to
review carefully?" It's **"which changes get the expensive kind of attention, and how does anything
decide that?"**

That reframes what a good oversight system is for. Its job isn't to review everything, or to replace
the reviewer. Its job is to **spend a scarce, decaying resource well** — and to make sure the small
number of things that genuinely need deliberate human judgment actually arrive in front of someone
still capable of giving it.

Which makes it striking how little the literature has to say about it. Of the 72 studies I retained,
**four** are primarily about risk-based routing — deciding what needs a person. The mechanism the whole
problem turns on is one of the thinnest clusters in the field.

*(There is a proposed remedy worth knowing: **cognitive forcing designs** — interventions that
deliberately interrupt the AI's flow to push the user into analytical thinking. Promising, and as far
as I can tell not yet tested at production scale.)*

### Finding 3: The problem is widely asserted and rarely measured

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

### What the evidence actually supports doing

Six things I'd act on if I were building or buying AI coding tooling tomorrow. Each is grounded in the
studies above rather than in my own preferences — which is also why the list is shorter than you might
expect.

Read them all against one question: **does this protect scarce human attention, or just consume it
differently?**

**1. Decide explicitly what gets a human — don't let it default.** If nothing in your pipeline routes,
then attention is being allocated by whoever happens to be on call and how tired they are. Pick a
signal — blast radius, security surface, unfamiliar subsystem, low-confidence generation — and make it
decide what escalates. A crude explicit rule beats an implicit one, because you can argue with it and
measure it.

**2. Make the second stage ask a different question.** If your pipeline's answer to "is this reliable?"
is *more models voting*, you are paying for the mechanism with the weakest evidence behind it. A
validation stage that asks "is this finding valid?" is the one that keeps showing measurable results.

**3. Stop treating agreement as confidence.** Unanimity across models is not independent
confirmation when the models share training data, prompt framing, and failure modes. If you use
convergence as a quality gate, you are measuring consensus, not correctness.

**4. Choose complementary checkers, not more of them.** The committee study found conservatism hits
diminishing returns as size grows, and that *composition* mattered more than count. If you run three
models, you should be able to say how they fail *differently* — and ideally have measured it. Adding a
third model that fails like the first two buys nothing.

**5. Let code make the decision; let the model produce the evidence.** Several of the better-performing
designs have models emit findings or scores while deterministic code decides accept / reject /
escalate. A threshold can be moved, tested and explained; a model's verdict cannot. It also means the
check can't be skipped — instruction-following is probabilistic, a state transition isn't. **And it is
the only version where a human can meaningfully set policy**: you can argue about where to put a
threshold, and be overruled about it. You cannot argue with a model's mood.

**6. Use the boring tools where they apply.** Linters, scanners, type checkers and test suites have
knowable, stable error profiles. Don't spend an LLM call on something a deterministic check already
does reliably — and don't call a rubric "rules-based" if a model is the one scoring it. Those two have
very different failure behaviour, and conflating them is how a pipeline ends up less predictable than
it looks.

And one decision to make explicitly rather than by accident: **what is your gate protecting?**
Protecting the codebase means blocking more and interrupting people more. Protecting attention means
letting more through. Those are opposite tunings of the same architecture. The most successful
deployment I found chose precision over recall deliberately, and accepted that it would miss things.
Choosing by default is how teams end up with a gate nobody trusts and everybody routes around.

### One caveat I have to state — and it's the same finding again

I used three models throughout: to screen, and later to help tag. The reliability numbers are the
sharpest version of everything above, because they happened to me rather than to someone I read about.

**The models agreed with each other reasonably well** — pairwise Cohen's κ of **0.49–0.64** across a
250-item sample, Spearman ρ ≈ 0.69. **They agreed with me much less.** On a blinded 50-item check,
model-versus-human keep/discard agreement came in at **κ = 0.30** — "fair," and below the **0.4** floor
usually treated as acceptable for inter-rater reliability in a systematic review. It reproduced almost
exactly in a second round (κ = 0.27), so it wasn't a bad sample.

The part that settled it: **model *dissent* carried no signal about human judgment either.** Where two
models disagreed — the obvious place to look for hard cases — agreement with my eventual call ran at
**κ ≈ 0.01–0.04**. Chance. So there was no shortcut available: not "trust the consensus," and not even
"only review the ones they argue about." Every record still needed a human decision.

Later, at the tagging stage, the same shape appeared: on *contested* calls — where the panel proposed
something I hadn't — it was right about **half the time**.

**Models converging on each other is not the same as models converging on the truth**, and my own
screening measured the gap. That is the redundancy finding from Finding 1, arriving from inside the
method rather than from the literature — and it's the practical argument for the adjudication pattern:
the panel was useful precisely because a human asked a *different* question of its output, rather than
counting how many models agreed.

### What I'd like to know

None of this is an argument for taking humans out. It's an argument about **where to put them.** The
scaling problem isn't solved by a better reviewer or a better model — it's solved, if at all, by
deciding what genuinely needs a person and then making sure those things reliably reach one.

And the literature is far better at proposing mechanisms than at showing how allocation actually works
in a real organisation under deadline. After 147 close reads I can describe dozens of designs and
almost no practices. That's the gap I'm spending my PhD on.

If you have AI writing code in your org today: **what actually reaches a human, and who decided that?**

I'll write next about the questions this raised that nobody has answered.

---

## Notes

- **Length: ~2,150 words.** This grew well past the original 1,050 target as the practical section, the
  System 1/2 finding and the three-mechanism rewrite went in. It is a genuine long-read now. If it
  needs to come down, in order of least damage: (a) tighten Finding 3 — Post 03 covers "does anything
  actually go wrong" anyway; (b) drop recommendations 3 and 6, the two least surprising; (c) compress
  the mutual-critique paragraph in Finding 1 and let the graphic carry it. **Do not cut Finding 2** —
  it is the bridge that makes routing the crux rather than one mechanism among many.
- Both images are essential, not decorative — the funnel carries credibility, the two-mechanism diagram
  carries the argument. Place them exactly where marked.
- No participant recruitment, per the content plan — that holds until after candidacy.
- Paper names are deliberately omitted from the body to keep it readable; add a short "sources" note at
  the end of the LinkedIn article if comments ask, or link the eventual preprint.
