# Tagging instrument — F2 RESTRICTED RE-RUN (new vocabulary only)

**Instrument of record for the F2 run.** Implements `Restricted_Rerun_Spec.md`. Do not use this for
general tagging — it is deliberately partial.

**Population:** the 72 papers in `Phase 6 - Kept Core` (`R9ZHDXMN`). All have full text.
**Panel:** 3 vendors × k=3 = 9 runs per paper. Fable excluded (uniform composition).

---

## 0. WHAT THIS RUN IS, AND WHAT IT MUST NOT DO

You are applying **ten new vocabulary items** to a corpus whose **existing tags are already settled by
a human arbiter**. Those existing tags are **not under review**. You are not being asked whether the
paper's primary theme is right, whether it should have been kept, or whether its other facets hold.

**You may emit only the ten slugs in §2.** Everything else in the taxonomy is unreachable by
construction. If you find yourself wanting to propose an existing slug, that is out of scope — say
nothing.

**Why the restriction is on the OUTPUT and not on your reading:** every one of these ten slugs is
defined by a **boundary against an existing slug**. You cannot apply `agent-panel` without knowing
division of labour; you cannot apply `rules-based-checks-v2` without knowing `ai-review`. So this
prompt *tells you about* the neighbouring concepts — you need them to draw the line — but you may
**not emit them**.

**Default to silence.** These slugs are narrow. Nine of ten have a documented history of
over-application: the boundary corrections in §5 were each written after a panel fired a slug that did
not hold. **A slug you are unsure about is a slug you do not emit.** Under-proposing costs one missed
tag; over-proposing costs arbiter time and pollutes a measurement point.

---

## 1. INPUT

You receive the paper's **full text**. Read it before judging. Where a slug turns on *what a system
actually does* (`agent-panel`, `cross-model`, `rules-based-checks-v2`), the abstract is systematically
misleading — see the traps in §5.

---

## 2. OUTPUT CONTRACT

Return **exactly one JSON object**, no prose around it:

```json
{
  "themes":  ["..."],
  "facets":  ["..."],
  "rationales": { "<slug>": "1-2 sentences: which clause of the definition fired, and the evidence" },
  "flags":   [ { "slug": "<slug>", "issue": "why this is a boundary case the arbiter should rule on" } ]
}
```

**The only permitted values.**

| `themes` (3) | `facets` (7) |
|---|---|
| `evaluator-reliability` | `agent-panel` |
| `oversight-scaling-inversion-v2` | `cross-model` |
| `rules-based-checks-v2` | `evaluated-real-data` |
| | `evaluated-synthetic` |
| | `evaluated-benchmark` |
| | `scaling-dissent` |
| | `survey-input-v2` |

Any other string is a **validation failure**, not a proposal. Emitting `survey-input` or
`rules-based-checks` **without** the `-v2` suffix is a validation failure — the unsuffixed forms are the
frozen v1 tags and must not be touched.

**Rules.**
- **A rationale is required for every emitted slug.** No rationale = the slug is discarded.
- **Empty output is a valid and common result.** Most papers will get zero or one of these.
- **No primary theme.** Primaries are settled. Never propose one.
- **No disposition.** Never propose keep, demote, or tier.
- **`flags` is for genuine boundary cases** — emit the flag *instead of* guessing when a definition
  half-fits. A flagged non-emission is more useful than a confident wrong tag.

---

## 3. ENTAILMENT

**`evaluated-real-data` ⇒ the paper built something.** If no tool, system, pipeline or prototype was
built by the authors, `evaluated-real-data` **cannot** fire, whatever data was used. This is the single
hard entailment in the set; check it before emitting.

---

## 4. THE TEN SLUGS

### `agent-panel` *(facet)*

**Fires when:** multiple agents answer **the same question** about the same artifact, and their outputs
are combined by an **explicit aggregation rule** — vote, consensus, unanimity, majority.
**This is redundancy, not specialisation.**

**Discriminator — "loses a job or loses a vote?"** Remove one agent from the system. If **coverage**
disappears (nobody is checking security any more) it is **division of labour** → do not fire. If a
**vote** disappears (the same question now has two answers instead of three) it is a **panel** → fire.

**Positive:** Ullah `A6ZE2A26` — unanimous committees of 1–6 judges, all ruling on the same SQL query,
with committee size and composition varied as experimental variables.

**Negatives:**
- Nimraka `5RKMGRNA` — parallel specialists on **distinct** categories (division of labour)
- Rasheed `DJHG9BBS` — **relay**: sequential agents, each consuming the previous one's output
- P `N7E3MR2V` — PM / coordination roles (different functions, not different votes)
- David `6NTZ85CW` · Dutta `399HN438` — same pattern

> **TRAP.** The phrase *"multi-agent"* in a title or abstract **predicts nothing**. At least five
> distinct topologies in this corpus use it: panel · parallel division · relay · precision filter ·
> conjunctive gate. Read the architecture, not the label.

---

### `cross-model` *(facet)*

**Fires when:** **distinct models** check the same artifact **so that their errors can differ** — mutual
checking. The point is error decorrelation, not model count.

**Positive:** Ullah `A6ZE2A26` — committees of distinct models, with **composition measured as a
variable**.

**Negatives — all four are real corrections, not hypotheticals:**
- Karakaya `5NZ2EDEK` — models **compared** as judges (they are the *subject*, not checkers of each other)
- Lipsanen `7SH86C2W` — **task allocation**: Codex implements, Claude handles non-functional requirements
- McAleese `NRVQT89E` — **one** fine-tuned critic in a checking role
- Liu `9H6FWJME` — five tools studied; none checks another

> **TRAP.** More than one model being *present* is not `cross-model`. Ask: does model B's output act as
> a **check on** model A's output?

---

### `evaluator-reliability` *(theme — namespace fixed §146a)*

**Fires when:** the paper's subject matter is **how reliable the evaluator is** — whether an LLM judge,
critic, reviewer or metric can be trusted, and under what conditions it fails.

Consolidated to the **theme** namespace 2026-08-29 (§146a); the former facet form is retired. It names
what the paper is *about*, not a property of its evidence.

**Positives:** Jin `UDVHQ5HR` (systematic overcorrection in conformance judgement) · Zhao `BAWCBT9R`
(auditing LLM-as-a-judge for bias) · Spiess `VTDG995V` (calibration and correctness) · Karakaya
`5NZ2EDEK` (limits of automated evaluation) · Ullah `A6ZE2A26` (operating characteristics of juries) ·
Sollenberger `GCZQTNBD` (LLM-as-a-judge for validation).

**Does not fire** merely because a paper *uses* an LLM evaluator. It must **interrogate** that
evaluator's reliability.

---

### `evaluated-real-data` *(facet)*

**Definition (arbiter, F2a):** *"a **tool is developed** and that tool is **evaluated using real data**.
Tool could be a pipeline. In mining, pre-existing data is mined for insights. **No new tool is being
evaluated.**"*

**Two conditions, both required:**
1. The authors **built** something (⇒ see §3);
2. They **evaluated it** on **real-world** data — production repos, real commits, real issues, real
   incidents — as opposed to synthetic or benchmark material.

**Negative:** Liu `9H6FWJME` — 302.6k real commits, but **pure mining**. Nothing was built, so nothing
was evaluated. Real data alone never suffices.

**Candidate positives to assess on their merits:** Minh `74GE3TF7` · Karakaya `5NZ2EDEK` ·
Liu `6ZC3H7AF` · Lipsanen `7SH86C2W`. *(No confirmed instance existed when the definition was settled —
this slug may legitimately come back empty.)*

---

### `evaluated-synthetic` · `evaluated-benchmark` *(facets)*

Carry the §34/§35 wording unchanged.

- **`evaluated-synthetic`** — evaluated on **generated or constructed** material (injected faults,
  synthesised tasks, model-authored test cases) rather than material drawn from real practice.
- **`evaluated-benchmark`** — measured **against a recognised third-party benchmark run as-is**
  (SWE-bench, Defects4J, HumanEval and similar). **Not** contributing a benchmark; **not**
  author-curated material merely *sourced* from a well-known pool (§119b).

> **TRAP.** Running your own system on a standardised third-party benchmark is still **tool results**
> and produces no method facet — but it does fire `evaluated-benchmark`. These are different questions;
> do not conflate "what kind of evidence" with "what was it run on."

---

### `scaling-dissent` *(facet)*

**Fires when:** the paper argues that **delegating oversight is unworkable or impermissible as a general
matter** — a principled objection to the scaling project itself.

**Does NOT fire when** the paper reports that *a particular* delegation is unreliable, or that a
specific tool underperforms. **That is the review's own thesis, not dissent from it.**

> **POLARITY TRAP — assume it is live.** The predecessor slug `counterpoint` was deprecated (§56)
> because the panel tagged a thesis-**supporting** paper as opposition **9/9 — unanimously wrong.**
> The failure mode is reading *"AI review has problems"* as *"oversight cannot be scaled."* Almost
> every paper in this corpus reports problems; almost none dissents from the project.
>
> Before emitting, answer explicitly in the rationale: **what general claim does this paper make that
> the scaling thesis must answer?** If you cannot state one, do not emit.

**Negatives:** Karakaya `5NZ2EDEK` · Lipsanen `7SH86C2W`.

---

### `oversight-scaling-inversion-v2` *(theme — v1 tags remain untouched)*

**Leads with the leakage test (§88).** The claim is that **oversight capacity inverts** — that scaling
generation degrades the review that is supposed to catch its defects.

**Two satisfaction routes (§117d), either sufficient:**
1. **Observed review absence** — work merging without meaningful review;
2. **Defects measurably present in MERGED code, with review failure as the cause.**

**Explicitly insufficient — none of these fire it:** maintainer burden · queue growth · falling
throughput · displaced work · reviewer complaints.

> **Two failure modes, both found at 3/3 in the Accept band. Screen for both.**
>
> **§123a — volume-for-leakage substitution.** AIDev: agent PRs were accepted *less* often, yet the
> panel inferred inversion from a 3-days-vs-3-years volume figure. **Pressure is not leakage.**
>
> **§127b — population mismatch.** Minh: 28.3% merge instantly (absence), but those are the *trivial*
> PRs, while the overload symptom is *ghosting* — and ghosted PRs never merge. **Absence and overload
> must fall on the SAME population.** State in the rationale which population each half of your
> evidence describes.

Run as its **own slug**; v1 is not reused (§10.12), so the reclassification delta is measurable.

---

### `survey-input-v2` *(facet — v1 tags remain untouched)*

**THREE conditions, all required. Conjunctive.**

1. **Instrument test (§116a).** An actual **survey instrument** exists — Likert-type or structured
   questionnaire. **Semi-structured interviews alone fail this. Mined data fails this** (there is no
   instrument at all).
2. **Elicitation test (§121b).** The instrument elicits **stated preferences, adoption, or priorities**.
   An instrument measuring a **construct or performance** — cognitive load, engagement, comprehension,
   satisfaction, demographics — is `method-self-report` only.
3. **Reported-finding test (§145a, NEW).** The elicited preference is a **reported finding of the
   paper**, not **formative** material that motivated its design. *Location test:* does the preference
   appear in the **Results**, or in the **Motivation / Background**?

**Explicitly NOT criteria — both proposed and withdrawn, twice each (§121b, §124f, §145a):**
- **Centrality** — the survey need not be the paper's main method.
- **Usefulness to the reader's own research** — not a property of the paper.

**Positives:** Kang `7UB2MD8Z` — *"70% agreed"* explanations were wanted; a stated preference about
tooling, reported as a result · Salem `5Q4G4CQB` — five-point Likert on attitudes.

**Negatives, one per failed condition — use these to locate the boundary:**
- Baltes `B644HQFS` — **fails (1)**: 1,154 Reddit/HN posts, nobody surveyed
- Omidvar-Tehrani `4FGIVVTG` — **fails (1)**: interviews, no instrument (passes (2))
- Catalan `5BAZZWHG` — **fails (2)**: Likert exists but measures cognitive engagement, a construct
- Takerngsaksiri `5VTAJISY` (*HULA*) — **fails (2)**: 8 of 11 questions sit under the authors' own
  heading *"The performance of HULA"*
- Shukla `T72TU8B5` (*Hedwig*) — **fails (3)**: elicits *"evolving preferences for level of oversight"*,
  but the survey is formative and motivates the design

**Note:** `survey-input-v2` and `method-self-report` are **different axes** and co-occur freely.

---

### `rules-based-checks-v2` *(theme — v1 tags remain untouched)*

**Fires only when the EVALUATION is deterministic** — the verdict is **computed, reproducible, and
independent of any model's judgement**.

**Arbiter's rule (§139a):** ***"Rubrics that are LLM evaluated are not rules-based-checks."*** The theme
names **how the verdict is produced**, not how the criteria are written. **Rule-shaped criteria scored
by a model are `ai-review`**, however explicit, numbered or rule-like the rubric.

**Positives:** Parris `3SU9QZ6F` (15 deterministic checks) · Töpfer `72W6R4JG` (FCL constraint
verifier) · Xie `T8E8SCCG` (VibeGuard security gate) · Zhong `96XE669R` (30 deterministic verifiers) ·
Lipsanen `7SH86C2W` (executable acceptance tests, pass/fail).

**Negatives:** Sollenberger `GCZQTNBD` (LLM judge) · Raghavendra `8VBH957K` (LLM-scored rubrics) ·
Sun `V4IRKSFI` — **both** stages are fine-tuned LLMs; *"RuleChecker"* is a **name**, not a mechanism.

> **TRAP — do not tag from a component's name.** Ask what **computes the verdict**: code, or a model?
>
> **Also not this slug:** *deterministic orchestration* — a fixed state machine sequencing the steps —
> is not deterministic *checking*. Many systems have rigid control flow and an LLM judge at the end.
> The question is only about the **verdict**.

**Known hybrid — FLAG, do not force.** Deterministic **execution** over **model-generated** criteria
(e.g. running GPT-4o-authored tests): verdict computed, criteria model-authored. F2 has not settled
hybrids. **Emit a `flags` entry and let the arbiter rule.**

---

## 5. STANDING FAILURE MODES

Every item here is a **correction already made** in this project, not a hypothetical.

1. **Over-application when the contrast class is stripped.** Corrected five times in the Accept band
   (§110, §112a, §130b, §132a, §135c) and four times on `cross-model` alone (§122, §124d, §125d, §126c).
   The neighbours in §4 are there precisely because removing them causes over-firing.
2. **Tagging from vocabulary rather than mechanism.** *"Multi-agent"*, *"RuleChecker"*, *"rubric"*,
   *"benchmark"* — all appear in papers where the corresponding slug does **not** hold.
3. **Polarity inversion on dissent.** 9/9 unanimously wrong once already (§56).
4. **Unanimity is not correctness.** On the residual set — proposals the arbiter had not independently
   made — this panel has run at **50% precision (7 of 14)**. Three vendors agreeing is not evidence.
   **Your confidence should come from the definition fitting, never from expecting the others to agree.**

---

## 6. WORKED NON-EXAMPLE

A paper builds a multi-agent code review system. Four agents review each PR — one for security, one for
style, one for tests, one for performance. Their findings are merged and a fifth agent writes the final
comment. It is evaluated on 500 PRs from three open-source repos, scored against a rubric that a GPT-4
judge applies.

| Slug | Verdict | Why |
|---|---|---|
| `agent-panel` | **no** | Remove the security agent and *coverage* disappears, not a vote. Division of labour. |
| `cross-model` | **no** | One model in several roles; nothing checks anything else. |
| `rules-based-checks-v2` | **no** | The verdict comes from a GPT-4 judge. Rubric shape is irrelevant. |
| `evaluated-real-data` | **yes** | They built it, and evaluated on real PRs from real repos. |
| `evaluated-benchmark` | **no** | Author-curated PRs are not a third-party benchmark run as-is. |
| `evaluator-reliability` | **no** | It *uses* a judge; it does not interrogate the judge's reliability. |

**Correct output: one facet.** A panel that emitted four here would have made four separate documented
errors.
