# Emerging Themes — cross-cutting patterns surfacing during triage/extraction

**Vibe Coding Governance SLR · synthesis source document**
**Started:** 2026-07-13 · Updated 2026-07-14 (full theme catalogue added) · Grows as themes recur across the corpus

Themes that span multiple items and warrant a dedicated synthesis section in the review /
dissertation. Each names its anchor + the corpus cluster (Zotero item keys) so it is traceable.

---

## Tag reference — full working vocabulary (2026-07-14)

Derived **bottom-up** from open-coding all 149 Core abstracts (4 parallel coders, identical frame)
→ merged emergent clusters → cross-checked against the 76 HOS experiential findings. Grouped by the
review question's own structure. `theme:<slug>` is the tag applied; the cross-doc **T-label** (T0–T3)
ties back to the handoff / `Problem_Statement_Evidence.md`. Example keys are **illustrative members**
surfaced during coding, not final rosters — the systematic sweep confirms/completes each. Counts (~N)
are approximate, for sizing. **Two themes have full write-ups below** (`tooling-supply-chain`,
`oversight-explanation`).

### How tagging works (read before applying)

Tags live in **three independent layers**; a paper normally carries several across them:
- **Lineage layer** (screening ground truth, every paper): `source:` · `s3:human:<bin>` · `centrality:<n>`.
- **Facet layer** (functional role in the write-up): `problem-statement-anchor` / `survey-input` /
  `intro-framing` / `lit-review` — zero or more.
- **Theme layer** (`theme:<slug>`): cross-cutting membership — **apply liberally**; a core paper
  typically belongs to 1–3 themes.

- **Multiple tags: expected.** The layers answer different questions ("where from / is it core?",
  "what role?", "what argument does it feed?"), so they stack. A paper can also hold several *themes*
  (e.g. a system that reviews, risk-scores, and escalates tags all three stages).
- **Mutual exclusivity: only one dimension.** Disposition `core`/`context`/`discard` (lineage layer)
  is exactly one per paper. **Among synthesis tags, nothing is mutually exclusive** — they are built
  to overlap; the Detect pair (`ai-review`/`rules-based-checks`) *expects* dual-tagging on gray-zone
  systems (rubric-grounded LLM-judge; "LLM writes tests then runs them"). Theme tags are **orthogonal
  to disposition** — a *context* paper can still carry `survey-input` or a `theme:`.
- **Membership, not mention.** Tag a theme only where the paper *contributes to that theme's argument*
  (with a one-line rationale), never because the abstract name-drops the topic. Keeps a `theme:` filter
  returning a real roster, not keyword noise.
- **Plumbing ≠ membership (systems papers, 2026-07-18).** A built system *uses* many mechanisms —
  its agents run tests, sandbox code, retry fixes — but tag only the mechanisms the paper
  *contributes an argument about*. (Calibration: three models tagged `rules-based-checks` on
  `UB2EVUFU` because its agents run test suites — instrumental plumbing; the paper's contribution is
  the agentic verification architecture → `ai-review`.)
- **Steering exclusion (apply before any solution theme).** Contributions that shape *what gets
  generated* — better prompts, specs, fine-tuning, and **controlling the AI's inputs/context** — are
  *steering*, not oversight; only a paper's inspection/comprehension/gating remainder earns solution
  themes. (Calibration: all four models missed the input-side case on Lumen `VG6CIDQW`, whose
  "context control" lever is steering — see decision log 2026-07-18.)
- **"Transparency" is never tagged as such — route it by object:** artifact/provenance *record* →
  `provenance-auditability` · reviewer comprehension (live view or handoff) → `oversight-explanation`
  · agent-behavior monitoring → `agent-scope-drift` · institutional evidence/audit trails →
  `org-governance` / `regulatory-compliance`.
- **Primary theme (one per paper) — tie-breaker.** The paper's *home*, where it'd be written up in
  depth. When a paper spans **adjacent** themes (`risk-routing`↔`hitl-workflow` = route vs. control-surface;
  `ai-review`↔`hitl-workflow` = the AI check vs. the human's gate), the primary is the theme carrying the
  paper's **distinctive contribution / novelty**, *not* the standard scaffolding. (Hedwig `T72TU8B5`:
  novelty = the dynamic-autonomy classifier → `risk-routing`, not the check-in surface.)
  **Altitude refinement (Scott, 2026-07-18 late, F9JM9CI6):** when a broader and a more specific
  theme both fit, primary = the most specific theme that still captures **where the paper's main
  effort lives** (F9JM9CI6: an AI-review vision whose energy goes into explanation design →
  `oversight-explanation` primary). Guard: a specific mechanism that is one *component* of a broader
  contribution does NOT outrank the broader theme (UB2EVUFU: budget-halving inside the verification
  architecture → primary stays `ai-review` — the exact codex/gemini v2 retag error).

---

### FACET TAGS (functional role; orthogonal to theme)

**`problem-statement-anchor`** — a single "committee-sit-up" empirical statistic strong enough to anchor
the problem statement. Feeds `Problem_Statement_Evidence.md`; also gets a child note. *Selective — few papers.*
**Bar (sharpened 2026-07-18):** the stat must anchor the **overall** problem statement (the
oversight-scaling inversion / two-part frame) — not a sub-argument's headline number (e.g. LLM-judge
unreliability) or a population-specific finding, however vivid. Models over-apply this facet by
*salience* (any impressive number); the calibration human applied it zero times in 10 papers on this
bar. **Never on a `lit-review` paper** — its stats are secondhand; chase and anchor the primaries.
- `59KP8GTP` — ~80% of AI-co-authored PRs merged with no explicit review.
- `3Z45M3V3` — 29.5% of Python / 24.2% of JS Copilot snippets carry security weaknesses.

**`survey-input`** — empirical adoption / preference / RAI-priority findings that inform the **org survey
design** (what practitioners want, prioritize, or limit). *Valuable even at context tier — that's the point.*
- `29NBUJWT` — developer AI-adoption appraisals and RAI priorities by task type.

**`dissertation-input`** (added 2026-08-15) — findings or theory the **dissertation** must engage with
directly (research questions, survey constructs, discussion), beyond the paper's role in the SLR corpus.
**HUMAN-ONLY synthesis tag** — never in the model instrument (v2.13 frozen mid-sweep; models can't judge
dissertation relevance anyway); arbiter-applied, sparse by design. Bar: substantive contribution to a
dissertation-level question; a **child note is required** stating which question and why (mirrors the
`problem-statement-anchor` capture convention). Orthogonal to tier — expected mostly on context items.
Tier ≠ importance: context is a scope judgment; this tag carries the value judgment separately.
- `UTTJ5N93` (seed) — cognitive forcing functions reduce AI overreliance: the oversight-*effectiveness*
  dimension (oversight quality as a manipulable design variable, not a fixed human property), feeding the
  "effective as well as scalable" dissertation question; stays context per the `7BMFG5IK` precedent.

**`intro-framing`** — position / agenda / definitional papers that *name the gap* but don't operationalize
a mechanism; cite in the Introduction. Usually context-tier (+ often `lit-review`).
- `4TUNZ7FU` — position/agenda paper establishing the need.

**`lit-review`** — secondary literature (survey / review / meta-analysis); default context + reference-
snowball source. **Structure not required (2026-07-18):** systematic *or* narrative — the test is
whether the evidence is *synthesized from other papers rather than produced*. A casual stat-assembly
needs this facet *most* (marks the evidence derivative → cite the underlying primaries, don't
double-count). **Primary convention for lit-review papers — binding:** if this facet applies, the primary MUST be
the "biggest-tent" theme covering the synthesis *overall* — never the most vivid/quantified section
(the models' salience bias on `2CKL96B8`; the dry-run showed a non-imperative wording gets ignored).
**A framing related-work section ≠ this facet (2026-07-20, Set B consultation):** the facet marks
the PAPER's role — a paper producing its own results (study/system/design) with a literature review
as framing/input is primary literature; both facet jobs (derivative-evidence marker, biggest-tent
convention) would misfire on it. Hybrid edge: tag only if the review component is itself a citable
contribution ("would you send someone to this paper *for the review*?").
- `5I2W8IC6` — systematic review mapping trust/distrust concepts for LLMs in SE.

**`counterpoint`** (role facet, added 2026-07-18) — the paper **argues against a prevailing position**
in the AI-coding/oversight discourse: full-automation maximalism, the value of HITL, oversight
scaling — any direction. **Direction-agnostic**: record *what it opposes* in the rationale (a paper
can be contrarian toward automation yet aligned with this review's thesis, or vice versa). Two jobs:
(a) the Discussion's alternative-views roster / confirmation-bias defense; (b) operationalizes the
earmarked "contrarian hunt" — the roster accumulates during tagging rather than a separate later
hunt. Often co-occurs with `intro-framing`; absence = no counter-position staked.
- `F9JM9CI6` — against review-automation maximalism (note the polarity: *pro*-human-oversight).

**Artifact / evidence cluster** (added 2026-07-15; `design-only` added 2026-07-19) — four composable
facets capturing the *form and maturity* of the contribution, powering the **proposed-vs-adopted**
adoption story (esp. formal-methods aspirational-vs-niche). Maturity ladder: `design-only` →
`built-system` → `adopted`; `framework` marks the *form* and composes at any rung.

**`framework`** — a **technical framework / reference architecture / integratable design** — a concrete,
adoptable structure you could plug into a build/dev pipeline (whether or not yet implemented). **Not** an
org-policy apparatus (that's `theme:org-governance`) and **not** a one-off point tool. The distinction is
*altitude/integratability*: `facet:framework` = a pipeline-integratable technical framework;
`theme:org-governance` = the org-level governance apparatus that pulls oversight together. A purely
*conceptual* framework that's neither (a bare taxonomy/decision model) does **not** get this facet —
it's captured by its theme. Composes freely (e.g. `lit-review` + `framework`).
- **Breadth is NOT the criterion.** A *focused, single-concern* architecture still qualifies (VibeGuard's
  security gate, Hedwig's autonomy-control layer). What's excluded is a **point result** — a bare
  algorithm, benchmark, or measurement with no adoptable/reusable structure. Test: *"would someone adopt
  this as a reusable design into their pipeline?"* → framework; *"is it a one-off result?"* → not.
- `T8E8SCCG` — VibeGuard's security-gate framework (drops into publish/CI). *(A policy-as-code engine is
  the gray zone: `org-governance` topic **and** `framework` form — both.)*

**`design-only`** (form facet, added 2026-07-19 mid-Set-B under the §10 additive precedent) — the paper
**specifies a mechanism/architecture in buildable detail** (components, formulas, thresholds,
architecture) **but never credibly runs it**: no working implementation and no evaluation on the
intended object. The *positive* marker for "proposed, not built" — a missing `built-system` alone is
ambiguous three ways (facet not applicable vs tagger miss vs genuinely unbuilt); this disambiguates
and powers the synthesis claim "N of the solution papers exist only on paper."
- **A mock demo does not count as building.** A demonstration that fabricates the mechanism's core
  outputs — random/synthetic stand-ins for the very values the mechanism is supposed to compute — is
  still design-only. Worked example: `R4WJZBSF`, whose "production-ready Google Colab implementation"
  computes two of its four metrics as literal `np.random` draws, whose results table reproduces the
  mock's hard-coded probabilities, and whose claimed validation (κ=0.72, 90% precision, three
  institutions) has no corresponding artifact in the paper.
- **Applies only to papers that propose something.** An empirical study with no proposed mechanism
  gets neither this facet nor `built-system` — the facet marks the *presence of an unbuilt design*,
  not the absence of building.
- **Boundaries.** ≠ `intro-framing` (which specifies NO mechanism — the discriminator is *buildable
  detail*; carrying both on one paper is a contradiction). Mutually exclusive with `built-system` and
  `adopted`; composes with `framework` (a proposed reference architecture = `framework` +
  `design-only`). Completes the maturity spectrum: `intro-framing` (gap named) → `design-only`
  (mechanism designed) → `built-system` (running) → `adopted` (in real use).
  **Inclusive-side ruling (Scott, 2026-07-20, §23):** a *stated architectural-design contribution*
  (F9JM9CI6's AI-OS review-platform architecture) meets buildable detail even when the authors
  defer realization to a research agenda — F9JM9CI6 is the worked example on this side; genuinely
  mechanism-free gap-naming papers remain `intro-framing`.
- **Disposition tripwire** (parallel to steering-only and `general-ai`): a design-only *solution*
  paper meets the "proposes an unevaluated methodology/framework → context" discriminator — check
  the core bar / `demote:context` candidate. Not automatic: a novel central framework can stay core
  by the promote exception, **and the what+how carve-out (arbiter ruling 2026-07-20, §23) keeps a
  paper core when it names the elements to track AND defines operationalizable metrics for tracking
  them — instrumentation specification clears bar (2) as measurement even unevaluated (R4WJZBSF).**
- **Slug rationale:** chosen over `proposal` — every solution paper "proposes" something, so that
  slug invites over-firing (the `ai-review` slug-connotation lesson, §13); the exclusion lives in
  the name. Re-run regression pair: `R4WJZBSF` (design-only) vs the built Set A systems
  (`T8E8SCCG` VibeGuard, `T72TU8B5` Hedwig, `VG6CIDQW` Lumen — `built-system`, never design-only).

**`expert-validated`** (form facet, staged 2026-07-20, **promoted 2026-07-21** on its first genuine
instance — `UW2R6BBJ`, changelog §28) — the contribution was **evaluated by documented expert
judgment**: expert panel, Delphi rounds, structured practitioner review, with the process
described as method (who, how many, what protocol). The middle rung of evidence strength:
unvalidated design < expert-validated design < built prototype < adopted.
- **The panel judges the *contribution*, not produces the *data*.** Experts shaping requirements
  or filtering lit-review inputs (input-side — the dissolved 6DXZGHD9-era probe) don't count;
  experts as study *subjects* = `method-self-report`, not this; ≠ peer review (every published
  paper); ≠ undocumented collegial feedback. The same panel can do both jobs — provide data AND
  validate the design → `method-self-report` + this facet co-hold.
- Composes with `design-only` (the common case: specified, never run, expert-vetted) or with
  `built-system` (a running system additionally panel-reviewed).

**`built-system`** — the authors *implemented* the approach as a working system / tool / prototype
("…and they built it"), beyond describing it.
- `T8E8SCCG` — VibeGuard, a built pre-publish security gate.

**`adopted`** — evidence the system is used **outside the research context** — commercial / production /
real organizational use (by the authors' own company or third parties), **beyond a lab prototype or
benchmark**. The scarce, high-signal adoption bit; absence = prototype / proposal / study. Usually
co-occurs with `built-system`.
- **Pilot rule (2026-07-20, Set B consultation — applied same day by the arbiter):** "outside the
  research *context*" ≠ "outside the research *organization*". The discriminator is **study site vs
  user**: a pilot/multi-org case study run *as the paper's field evaluation* (authors deploy,
  instrument, observe — remove the study and the use ends) is the research context extended to a
  field site → strong `built-system` evidence, NOT adoption. `adopted` = use for the org's **own
  operational purposes** — integrated, org-initiated, or continuing beyond the study window.
  Textual cues: "we deployed at X for a 3-month pilot and measured…" → evaluation; "X has
  integrated it into their CI pipeline" / "in use at X since…" → adopted.
- `CTGGMIX9`, `V4IRKSFI` — industrially deployed review systems.

**`general-ai`** (scope flag, added 2026-07-15) — the governance/oversight contribution is **general
AI/LLM, not coding-specific** (transferable from the broader AI-governance space: model adversarial-
robustness, general RAI frameworks, general model-assurance). A *scope* flag; default (untagged) =
coding-specific (the SLR's core focus). Two jobs: (a) **scope audit** — surface cores that are
general-rather-than-coding-specific → candidates to demote to **context** (per the "broader governance
that transfers → context" rule); (b) **synthesis separation** — keep borrowed general-AI governance
distinct from coding-specific governance. Object-of-governance = the *model*, not the produced code.
- `M74M3RFJ` — assurance cases for LLM adversarial robustness + EU AI Act compliance (general-AI;
  **demoted core → context** 2026-07-15). The models all tagged it `regulatory-compliance` (theme-level,
  in-scope-looking); the human scoped it out — the flag is the tripwire for that.
- **Kept-core exception (arbiter, 2026-07-21 — adjudication-layer rule, changelog §30):** a deep
  regulatory-operationalization dive in a general-AI paper triggers a **look-at-keeping review —
  not an automatic keep**; the arbiter then weighs whether it is the corpus's **sole
  operationalization exemplar for a review-question limb**. `UW2R6BBJ` kept on that weighing (the
  only deep dive applying regulatory frameworks to engineering controls; evaluated deployment +
  expert-validated), serving the RQ's governance/policy limb. Parallel to the one-framing-anchor principle and `general-code`'s
  kept-core transfers; the flag stays on as audit trail. **Taggers/models still flag
  `demote:context` on general-AI objects** — the flag proposes, the human disposes; M74M3RFJ's
  demote stands (unevaluated, robustness-focused, not sole).

**`assistive` / `agentic`** (generation-mode scope pair, added 2026-07-18) — which *generation setting*
the paper studies. The cut is **who initiates + the reviewable unit**, NOT tool location — "in the IDE"
is the wrong axis, since agents live in IDEs too (Cursor, Copilot agent mode):
- **`assistive`** — human-initiated, **suggestion-granularity** generation (inline completion,
  *snippet-level* chat-paste): the human authors in the flow and accepts piece-by-piece (a chat task
  returning a *complete artifact* is the tie-rule case: reviewable unit dominates → `agentic`). Oversight surface = the
  *acceptance moment* (`automation-bias` territory).
- **`agentic`** — **AI-initiated / AI-planned multi-step work** delivered at **artifact/PR granularity**
  for review. Oversight surface = the *gate* (`oversight-scaling-inversion` territory; the setting the
  Detect→Triage→Fix→Escalate pipeline mostly presupposes).

Apply either or **both** (a paper that compares or spans modes); **neither** = the paper doesn't
specify, or mode is irrelevant to its claim (same absence convention as `adopted`).
**Clarifier (2026-07-18, F9JM9CI6):** the pair describes the **generation** studied — "uses agents"
≠ `agentic`, and "AI assists the human" ≠ `assistive`. A paper whose AI sits only on the
*review/oversight* side studies no AI generation → tag **neither**, and consider `general-code`.
**Tie-rule (2026-07-18, 22JBEZNK):** when the two criteria disagree — e.g. a *human-initiated* chat
task returning a *complete artifact* — **the reviewable unit dominates**: the facet's job is to
identify the oversight surface, and a wholesale-delivered artifact puts the human at the gate
(→ `agentic`) regardless of who initiated. Two jobs:
(a) **synthesis separation** — which oversight evidence/mechanisms belong to which mode; (b) **survey
stratification** — mode-specific items in the org survey.
- Illustrative: `3Z45M3V3` / `YBHHYR4P` — assistive (Copilot-snippet CWEs / users trust insecure code
  more); `SHK6KAX6` / `UIXCRBQX` — agentic (agentic-PR merge & maintenance studies); `T72TU8B5`
  (Hedwig autonomy tiers) — agentic.

**`steering`** (contribution-type flag, added 2026-07-18; amended same day; materiality qualifier added
after the dry-run) — the paper's proposed solution **or the practice it documents** operates on
**generation** as a **substantive part of the contribution** (not any incidental prompt-shaping
component — every AI system shapes a prompt somewhere) — better
prompts, specs/executable requirements, fine-tuning, shaping model inputs — rather than
inspecting/gating the produced artifact. **Contribution, not topic**: every AI-coding paper touches
generation; the flag applies only when steering is *offered as the solution* or is *the documented
practice under study* (empirical amendment from `Z8TPRNEU`: the "control" professional devs exercise
is largely generation-directing — the facet explains the thin solution-theme roster). Three jobs: (a) **audit trail** for the steering exclusion — documents why a solution
component earned no solution theme; (b) explains sparse theme rosters on hybrid steer-and-check
systems in the sweep; (c) **tripwire**: a *steering-only* solution is a demote-to-context candidate
(the `spec-driven-guardrails` resolution, now enforceable — parallel to `general-ai` for object
scope). Illustrative: `VG6CIDQW` (Lumen — context control over the assistant's inputs, confirmed
steering 2026-07-18, a big part of the system; its oversight remainder is `oversight-explanation`
pull); `DPKKMXSA` (prompt-enhancement as the fix); the spec-driven cluster (`C88VGWMI` `7SH86C2W`
`JCTP8VXP`, context-tier).

**`metrics`** (contribution flag, added 2026-07-20) — the paper **defines metrics / scores / indices**
(risk, quality, oversight, compliance) **as a deliverable** — not merely *uses* metrics to evaluate
something (every empirical paper has an evaluation apparatus; that earns nothing). The
**defines-vs-uses test is the guardrail** — "metrics" is as collision-prone a word as "framework."
**Contribution, not apparatus.** The metrics' **object comes from the co-tagged themes**
(+`regulatory-compliance` = compliance-risk metrics · + an oversight theme = oversight metrics ·
+`quality-debt` = quality metrics · +`risk-routing` = metrics that *drive* allocation, VTDG995V-class).
Composes with `design-only` (metrics defined, never run on real data — R4WJZBSF) or with problem
themes (defined AND applied → the findings earn theme membership; the facet marks the reusable
instrument).
- **Rationale MUST name the measurand** — *what* the metrics measure ("regulatory/ethical risk
  exposure," "defect likelihood," "review coverage"), not just the domain. The tag layer records the
  domain via themes; the risk-ness (or other nature) of the measurand lives in the rationale. A
  saturating `risks` facet was considered and **rejected** (2026-07-20): "talks about risk" is a
  mention-level criterion in a governance corpus — near-100% base rate, zero discrimination.
- **Boundary with `risk-routing`:** defining the signal without the allocation decision is NOT
  routing (see that theme's Boundary); papers that define AND route get theme + facet.
- Genesis: `R4WJZBSF` — four regulatory-risk indices, no allocation decision; the human's blind
  `risk-routing` primary was the stretch that exposed the gap (changelog §20). Staged kin:
  risk-quantification instrument family (`HOS_Seeded_Theme_Candidates.md`, sweep-cluster tripwire).

**`routing-signal`** (contribution flag, added 2026-07-21 §29) — the paper contributes a
**computed, producer-independent signal framed for review-attention allocation** (which artifacts
deserve human scrutiny) **without operationalizing the selection/gating logic** — no threshold,
tier, or engagement decision. The `steering`-grammar audit trail for the **signal-without-
allocation boundary**, which caught the arbiter blind twice in two days (R4WJZBSF `risk-routing`
primary; E95T8E88 `risk-routing` primary) — the instrument's most human-catching line gets its
positive marker.
- **Framing test:** the paper itself must frame the signal as review-attention input (E95T8E88:
  "allow reviewers to prioritize their attention"). Signals framed for other purposes get
  `metrics` only (R4WJZBSF's org-risk score) — keeps generic defect predictors out.
- **Mutually exclusive with `theme:risk-routing`** by construction: operationalized selection →
  the theme (+`metrics`); signal-only → this flag (+`metrics`, usually).
- **Synthesis job:** the Triage supply chain — "N papers supply routing signals vs M operationalize
  routing" is a field-maturity finding the review question predicts. Seed: `E95T8E88`
  (deletion-likelihood at PR creation, AUC 87.1, selection logic absent).

**`general-code`** (scope flag, object axis, added 2026-07-18) — the paper's oversight/review
mechanism targets **code generally, not AI-generated code specifically**; the AI (if any) sits on
the *oversight side* (review support), not the producing side. Such work *transfers* to the AI-code
setting but wasn't developed or evaluated there — keep it distinguishable so synthesis doesn't
overclaim (mechanisms *built for* AI code vs mechanisms *imported from* general review practice).
Default (untagged) = the overseen object is AI-generated code. Completes the wrong-object tripwire
family: `general-ai` (object = the model) · `general-code` (object = any code) · `non-developer`
(population) · `steering` (contribution type). Doubles as the audit trail for the "broader-setting
oversight that transfers" triage rule when such a paper is kept core.
- `F9JM9CI6` — AI-supported review prep (agents generate higher-level descriptions for the reviewer)
  for code review *in general*; kept core (augment-vs-replace), object = general code.

**`non-developer`** (scope flag, population axis, added 2026-07-18) — the generating/overseeing
human studied is **not a professional developer**: end-user, business user, citizen developer —
the "democratization" endgame of vibe coding. Default (untagged) = professional-developer context.
Completes the three scope axes: **mode** (`assistive`/`agentic`) · **object** (`general-ai`) ·
**population** (`non-developer`). Also the tripwire for the staged **oversight-competence-gap** theme
candidate (escalation presupposes a competent receiver; democratization removes it — see
`HOS_Seeded_Theme_Candidates.md`): if flagged papers accumulate making that argument, it promotes.
Illustrative: `22JBEZNK` — business users can't detect flaws in AI analyses even when warned.

**`risk-security` / `risk-quality` / `risk-overreliance` / `risk-ip` / `risk-bias`** (risk-type flag
family, added 2026-07-20 §21 as homeless-types-only, **extended to the uniform family same day §22**) —
**substantive treatment of the harm**, one bar for every flag: defines a metric for it ·
contributes/evaluates a mitigation for it · reports an empirical result about it · devotes focal
analysis to it. An intro risk-list sentence = mention, no tag; the rationale cites which clause fired.
Types: security · quality (incl. **code comprehensibility** — "explainability of the code," see the
routing note below) · over-reliance · IP/plagiarism/licensing · bias in generated code.
- **A deliberate, bounded exception to membership-not-mention**, justified by the synthesis
  deliverable it powers: the **risk×mitigation matrix** — which harms the corpus identifies vs which
  have actual mechanisms; the gap cells (identified-but-unmitigated) are Discussion findings.
- **Flag ≠ theme — the co-occurrence grammar:** the flag marks substantive *engagement*
  (define-level suffices); the matching theme (`ai-code-insecurity` / `quality-debt` /
  `automation-bias`) still requires the paper to *do the lift* (study/evidence/argue). Heavy-lift
  papers carry **both** — expected, not double-counting: the matrix reads flags for the
  identified/measured axis and themes/mechanisms for the evidenced/mitigated axis. **Matrix
  reconstruction = one query per column, one bar** (the uniform family replaced §21's asymmetric
  design — themed columns no longer depend on rationale text-matching).
- **Explainability routes by object** (word-collision list entry): support for the human *judging
  the AI/its output* → `oversight-explanation`; **comprehensibility of the code itself** (unclear
  logic, undocumented sections) → quality territory (`risk-quality`, `theme:quality-debt` if the
  lift is done); model-XAI → `general-ai`.
- **Source-agnostic (arbiter ruling 2026-07-20, CodeAgent `7V7SRG43`):** the flags track the
  **harm**, regardless of the overseen code's source — a `general-code` mechanism that mitigates
  security/quality harms earns the flags plus `general-code`, and the matrix segments transferable
  mechanisms via that flag (parallel to `lit-review` segmenting secondhand rows). The `general-ai`
  exclusion stands (M74M3RFJ: object = the *model*, not code).
- **Lit-review interplay (arbiter ruling 2026-07-20, reversing an initial lean):** focal secondhand
  synthesis CAN fire these flags — `2CKL96B8` (narrative review; focal security-stats + quality
  synthesis) carries `risk-security` + `risk-quality`. The matrix segments secondhand engagement
  via the `lit-review` facet; passing enumeration ("need quality metrics") still never fires; and
  `problem-statement-anchor` remains never-on-lit-review (different facet, different bar — the
  anchor requires a citable headline stat, chase the primaries).
- **Extensible on the same bar** if the sweep surfaces a new type (privacy the likely next).
  **Promotion path** (for the homeless types `risk-ip`/`risk-bias`): a cluster at contribution
  level converts flag → theme, definition ready-made.
- Genesis: `R4WJZBSF` (defines PRS/BPI/EG/ADS → earns all four applicable flags: risk-ip,
  risk-bias, risk-quality, risk-overreliance); informal corpus recurrence of IP risk observed by
  the arbiter; HOS's IP scanner = experiential corroboration (kin, not driver — the HOS guardrail
  holds). Changelog §21–§22.

**`method-self-report` / `method-mining` / `method-experiment` / `method-field-study`**
(data-collection method family, added 2026-07-20 §25) — the standard SLR study-characteristics
axis: **how the paper's own evidence was produced.** `method-self-report` = humans tell you
(questionnaires, interviews, focus groups, diaries — perception/attitude data); `method-mining` =
artifacts measured (repos, PRs, commits, forum posts, logs, telemetry — behavior/artifact data);
`method-experiment` = controlled tasks with manipulation (lab or crowdsourced);
`method-field-study` = deployment/case study observed in a real setting. **Apply all that fit**
(mixed methods expected: `Z8TPRNEU` = self-report + field observation).
- **Own evidence only:** `lit-review` papers get none (their evidence is synthesized — the methods
  live in the primaries); absence = no empirical evidence produced (position papers, pure designs).
- **World-or-tool test (2026-07-20, systems-paper consultation):** results describing the *world*
  → method facet; results describing only the *tool* (benchmarks, self-run tests over constructed
  corpora) → no facet — that evaluation is carried by `built-system`. A detector run over real
  repos earns `method-mining` only if the findings characterize the repos, not just the detector's
  precision. **Humans using the artifact always fires one:** assigned tasks / controlled
  conditions → `method-experiment`; real work in the org's own setting, natural use →
  `method-field-study` (the adopted pilot rule's study-site pilots and case-study evaluations land
  here); a lab study plus a deployment gets both.
- **Subjects may be systems (2026-07-20, calibration backfill audit):** controlled studies of
  **third-party** tools/models whose findings characterize those systems = `method-experiment`
  (UDVHQ5HR probing external LLM verifiers — the findings are about the world's tooling). Running
  **your own** system on a benchmark — even a standardized third-party one (UB2EVUFU on
  ProjDevBench, retry-on-fail conditions prescribed) — is still tool-results: no facet, by the
  whose-properties test; parity with VibeGuard's untagged "controlled experiments on synthetic
  projects." The triangle: VibeGuard (own tool, synthetic) none · UB2EVUFU (own tool, standardized
  bench) none · UDVHQ5HR (others' tools studied) experiment. Benchmark-grade evidence for own
  systems = evidence-strength within `built-system` — staged `evaluated-benchmark` candidate.
- **Slug rationale:** `method-self-report`, not `method-survey` — avoids colliding with
  `survey-input`, whose slug already misled the arbiter once (B644HQFS probe: the facet tests the
  finding's *utility to the org survey*, method-independent; a mined study can be survey-input).
- **Jobs:** (a) evidence-weight separation in synthesis — perception vs artifact evidence disagree
  routinely in this corpus (users *believe* insecure code is more secure, YBHHYR4P); (b) the
  methods chapter's study-designs table, collected free during the sweep; (c) matrix provenance
  (identified-by-perception vs identified-by-measurement). Single-home note: if the Stage-4
  extraction codebook gains a data-collection field, reconcile — these tags are now the home.

---

### THEME TAGS

Each entry: **Captures** (what earns the tag) · **Boundary** (include/exclude, where it helps) · **Examples**.

#### Family 1 — QUANTIFY THE PROBLEM (why oversight must scale)

**`theme:oversight-scaling-inversion`** (T0) · ~8
- **Captures:** the spine — AI code is *riskier yet less inspected*; PRs auto-merged unreviewed;
  review becomes the bottleneck; burden concentrates on a shrinking pool of maintainers.
- **Boundary:** measures the *oversight gap itself* (the gating act, or its absence / cost). Not a
  generic "AI is buggy" measurement (that's the two below).
- **Examples:** `59KP8GTP` — ~80% of AI PRs merged unreviewed; `SHK6KAX6` — 61% of agentic PRs merge
  with minimal human intervention; `F2C2DWSI` — Copilot shifts rework/review burden onto core devs;
  `B644HQFS` — "AI slop" externalizes review cost onto maintainers.

**`theme:ai-code-insecurity`** · ~7
- **Captures:** empirical evidence AI-generated code carries **security** vulnerabilities (CWE rates,
  security benchmarks, insecure-but-confident).
- **Boundary:** security/vulnerability specifically. Non-security quality issues → `quality-debt`.
- **Examples:** `3Z45M3V3` — real-repo Copilot CWE prevalence; `4PSM6ZCD` — agent code only 10.5%
  secure, hint-based mitigations fail; `YBHHYR4P` — users write less secure code yet believe it *more* secure.

**`theme:quality-debt`** · ~7
- **Captures:** **non-security** quality degradation — technical debt, complexity, code smells,
  maintainability, breaking changes — accumulating from AI code.
- **Boundary:** maintainability/debt, not vulnerabilities (→ `ai-code-insecurity`). **Code
  comprehensibility ("explainability of the code") lives here** — unclear logic, undocumented
  sections, code lacking human-understandable rationale is a maintainability/review-burden attribute
  (2026-07-20; NOT `oversight-explanation`, which is judging-support for the human). Define-only
  measurement of quality attributes → `metrics` + `risk-quality`, no theme (membership = the lift).
- **Examples:** `9H6FWJME` — AI commits introduce persistent smells surviving to HEAD; `REZGA5WF` —
  causal ↑ in complexity/warnings (Cursor); `UIXCRBQX` — agentic PRs riskier in *maintenance* (confidence trap).

#### Family 2 — LIMITS OF CURRENT OVERSIGHT (the insufficiency layer)

**`theme:automation-bias`** · ~7
- **Captures:** the *human* fails at oversight — over-reliance, complacency, skill erosion, cognitive
  disengagement; people miss flaws even when warned/prompted.
- **Boundary — the failing human must be CAPABLE (2026-07-18):** automation-bias is an attention/trust
  failure by someone who *could have caught it* (over-reliance, complacency). If the failure persists
  despite priming, distrust instructions, and incentives — or the human *lacks the ability/support to
  evaluate at all* (typically `non-developer` settings) — that is the **oversight-competence gap**
  (staged candidate, `HOS_Seeded_Theme_Candidates.md`), NOT bias. Counter-example: `22JBEZNK` — the
  study *controls for* over-reliance (primed distrust, prompts, pay) and its Discussion explicitly
  rejects overconfidence: "the difficulty is rooted in applying domain expertise or critical thinking
  to unfamiliar technical contexts." All four models mis-tagged it automation-bias primary on the
  surface phrase "missed flaws even when warned" — the warning was the *control*, not the finding.
  Process failure (hollow/unenforced review) → `oversight-theater`.
- **Examples:** `E689ZAXC` — adding a review step makes workers *less* likely to revise; `5BAZZWHG` —
  cognitive engagement declines with agentic assistants.

**`theme:oversight-theater`** · ~5
- **Captures:** oversight that exists on paper but lacks authority/time/information to change the
  outcome — rubber-stamp, token HITL, "meaningful vs. checkbox", moral-crumple-zone. *Enforcement, not
  knowledge* (HOS).
- **Boundary:** about the *structure/authority* of the review being empty. Human cognitive failure → `automation-bias`.
- **Examples:** `9MV2IVNU` — names "Rubber-Stamp Risk"; `JVWUYDME` — "Human-in-Command" replacing
  token HITL with an enforced operating envelope; `ZGST9CY6` — designing *meaningful* oversight vs. automation-in-disguise.

#### Family 3 — CHARACTERIZE THE SOLUTION · organized on the **Detect → Triage → Fix → Escalate** pipeline

The solution themes are stages of one loop. A single system often spans stages → multi-tag it.
Cross-cutting: `agent-scope-drift`.

**— DETECT (is there a problem?) — two *kinds of detector*, split by signal epistemics —**

**`theme:ai-review`** (**probabilistic detector**) · ~16
- **Captures:** AI/LLM/agentic review that *judges* the produced artifact — fallible, can hallucinate.
  Single-reviewer, multi-agent panels, and **independent / cross-model review** (one agent validating
  another). **Also carries the reliability limits** of agent-checks-agent review.
- **Boundary:** the output is a *judgment/opinion* ("this looks wrong"). Grounded/checkable output →
  `rules-based-checks`. *Deciding which findings matter* → `risk-routing`. *Making the fix* → remediation.
- **Examples:** `CTGGMIX9` — spec-grounded LLM review, industrially deployed; `5RKMGRNA` — multi-agent
  PR review (bug/security/perf specialists); `A6ZE2A26` — unanimous LLM jury as accept/reject gate.
  *Limits:* `BAWCBT9R` — LLM-judge prompt-bias; `UDVHQ5HR` — LLMs misjudge NL-spec conformance;
  `TA6GIUK2` — AI-reviewing-AI is circular without an executable spec.

**`theme:rules-based-checks`** (**deterministic detector**) · ~8
- **Captures:** grounded, checkable verdicts — can't hallucinate, but blind outside their spec.
  Static analysis / lint, type-checkers, **tests**, symbolic-execution & **classical formal-methods
  engines** (CBMC, theorem provers), sandboxed execution, rubric checks.
- **Boundary:** a *computed/executable* verdict against a spec/test/oracle. Note: value as *oversight*
  depends on the oracle's independence — AI code passing AI-written tests is near-circular. A classical
  formal verifier here **also** carries the composable `formal-methods` tag (see below).
- **Examples:** `PR4GS7SP` — symbolic execution assesses correctness at near-human accuracy; `9R6TGN82`
  — program-analysis + test signals train toward secure code; `QWHE9EXH` — sandboxed transpiler/executor;
  `72W6R4JG` — automated verification via fine-grained constraint-violation feedback.

**`theme:formal-methods`** (**composable technique tag** — annotates the performer, not a pipeline stage) · ~4–6
- **Captures:** the paper uses/proposes *formal methods* — theorem proving, model checking, symbolic
  execution, deductive verification, formal specification / autoformalization. **Orthogonal to the
  performer**: always pair it with the theme that says *who* does the formal reasoning.
- **Compose:**
  - AI/LLM does the formal reasoning → `ai-review` + `formal-methods` (e.g. `5DI9B43K` verified LLM
    reasoning; `6ZW9QNQH` autoformalization).
  - Classical engine (CBMC, theorem prover, symbolic executor) → `rules-based-checks` + `formal-methods`
    (e.g. `PR4GS7SP`; TF56EPIP's surveyed CBMC/theorem-proving).
  - Pure advocacy / position, no performer → `formal-methods` + `intro-framing`.
- **Why a tag, not a solution section:** only ~4/149 cores foreground it (`PR4GS7SP` `E5SQKRH7`
  `6ZW9QNQH` `5DI9B43K`), one a *position* paper — a minor, largely aspirational academic thread.
  A standalone section would read as a recommendation that won't land with practitioners.
- **Adoption-gap framing (synthesis point):** the barrier is the *human expertise/effort to author
  specs & proofs*, **not** the value of the guarantees — practitioners reject *doing* formal methods,
  not its output. So the composed tags predict uptake:
  - `formal-methods` + `rules-based-checks` (classical, human-authored) → **niche / high-assurance only**
    (lives-on-the-line exceptions), near-zero mainstream uptake; vibe coding's speed ethos won't change it.
  - `formal-methods` + `ai-review` (AI-automated / autoformalization) → **the plausible adoption path**:
    if AI removes the authoring burden, practitioners accept it as just another pipeline check.
  - **Economics caveat:** that uptake still hinges on the AI-driven check being cheap/fast/quiet —
    formal methods' compute cost doesn't vanish, and correct-but-uneconomical oversight gets turned off
    (cf. `three-tier-review-cost-model`, `cost-gating`). A testable hypothesis for the org survey.

**— TRIAGE (what matters / what to do / escalate?) —**

**`theme:risk-routing`** · ~12
- **Captures:** the **allocation / triage decision** — compute a signal → decide *which* AI actions/
  artifacts reach a human, *whether* to escalate, at *what* priority/autonomy tier. The contribution is
  the **smarts of surfacing** (signal + selection/prioritization/tiering logic). *Gate on a **computed,
  producer-independent** signal* (HOS); model self-confidence is disqualified. **Mnemonic: risk-routing = WHAT**
  (what gets surfaced, at what priority) vs. `hitl-workflow` = *how & when* the human then acts.
- **Boundary:** the contribution is the *selection/prioritization/escalation logic* (which/whether/when
  a human is engaged). The review that *produced* the finding → `ai-review`/`rules-based-checks`; the
  interface the human then uses → `hitl-workflow`. **Error-condition handback is NOT risk-routing
  (2026-07-18, UB2EVUFU):** "agent stuck / can't converge → hand back to the human" is an *exception
  path*, not a discretionary triage decision — no computed signal selects among items. The handback
  mechanism, if contributed, → `hitl-workflow`; oversight of the failed-fix loop → `remediation-gating`.
  **Defining a risk metric/score without the allocation decision is NOT routing (2026-07-20,
  R4WJZBSF):** routing = signal *plus* selection/tiering logic; a paper that contributes only the
  signal (metrics, scores, composite indices) with no which/whether/when decision built on it gets
  the `metrics` facet, not this theme. Papers that define AND route get both.
- **Examples:** `BU73N7PC` — Meta diff-risk-score gates risky diffs; `74GE3TF7` — creation-time
  circuit-breaker predicts high-maintenance PRs for gated triage; `VTDG995V` — calibration → *computed*
  review intensity; `T72TU8B5` — autonomy tier adjusts by earned developer trust.

**— FIX (remediate the problem) —**

**`theme:remediation-gating`** · ~3 (thin — populate in sweep)
- **Captures (D3 ruling, 2026-07-18): governance of AUTONOMOUS fixing** — the system fixes *without
  per-fix human involvement* (Jidoka: autonomation that stops/corrects itself), kept safe by
  machinery: **content** gates (filter/arbitrate *which* fix candidates are acceptable) and
  **process** gates (bounded retries, budget-decay, convergence rules, stop-progression — fail-closed
  termination + handback when the fix won't converge). The *acting* step brought under control.
  Deciding when a **human** must engage on the fix path (risk tiers over fixes) = `risk-routing`
  layered on top — the andon cord, not the gate. **A human approving every fix is NOT this theme:**
  review-everything is the unscalable anti-pattern this review exists to move past (attention
  collapse → automation-bias territory); a paper *advocating* blanket per-fix human approval is a
  `counterpoint` candidate. Note the distinction: such a design *introduces* automation-bias risk —
  a rationale-level critique — whereas `automation-bias` *membership* requires the paper to
  study/evidence the human failure, not merely risk causing it.
- **Boundary:** the *gating/oversight of the fix*, **not** the repair technique itself (generating a
  fix is generation, outside the oversight frame). **Requires an autonomous fix/repair action being
  overseen** — a pure *detection or publish/quality gate* that blocks bad code with **no auto-fix** is
  NOT remediation-gating; that's the enforcement side of the detector (`rules-based-checks`/`ai-review`).
  Re-checking a landed fix → `rules-based-checks` / `ai-review`; deciding *which* fixes need sign-off →
  `risk-routing`. *(Calibration note: both a human and Opus over-tagged VibeGuard `T8E8SCCG` here — a
  publish gate, no auto-fix — which is why this exclusion is now explicit. **The same human repeated
  the same error on the same paper 2026-07-18** — root cause: this exclusion lived only in this doc,
  never in the compressed cheat-sheet the tagger works from. Now carried in every copy. Principle:
  every boundary that has ever caught a human must appear in the compressed instrument.)*
- **Examples:** `GAD5Z8PV` — multi-LLM ensemble filters harmful AI fix suggestions with minimal-edit
  arbitration before deployment (content gate); `UB2EVUFU` — budget-halving retry cycles with
  stop-progression when verification keeps failing (process gate); (sweep to add
  auto-repair-with-approval systems).

**— ESCALATE (human enters on disagreement / low-confidence / high-stakes) —**

**`theme:hitl-workflow`** · ~9
- **Captures:** the human's **control surface** — the mechanism an *already-engaged* human acts through:
  confirmation checkpoints, action guards, approval gates, human-as-director/orchestrator, bounded
  delegation. The contribution is the **design of the control point**, not the
  logic deciding what to surface. **Mnemonic: hitl-workflow = HOW + WHEN** the human acts (control
  mechanism + checkpoint placement/frequency) vs. `risk-routing` = *what* to surface.
- **Boundary:** *how the human exercises control* — **levers, not lenses**: comprehension/visibility
  tooling (the former "context transparency", relocated 2026-07-18) → `oversight-explanation`.
  Deciding *whether/what* to escalate → `risk-routing`. NB the steering exclusion: a lever over the
  AI's *inputs/context* is steering, not a control point over the artifact (the Lumen error).
  **Plan-gate rule (Scott, 2026-07-18 panel ruling):** a human gate over an AI-produced plan IS
  hitl-workflow when it is a *designed checkpoint in a lifecycle with checks and balances* (defined
  gate, authority to block, resumable process); the same approval act inside a conversational
  guide-then-"go do it" flow is steering.
- **Examples:** `XK3P9C96` — optimal placement of confirmation checkpoints; `U9VZQXGI` — HITL agent UI
  with action guards; `N7E3MR2V` — full-SDLC agent with human-approval guardrails + audit trails;
  `ID7IN65K` — 860-dev survey: demand for bounded delegation with authority scoping.

**`theme:oversight-explanation`** (T2) · ~5 — *full write-up below*
- **Captures (broadened 2026-07-18): helping the human understand what the AI is doing** — the
  *information* side of oversight, in either direction:
  - **push** — the system escalates and makes the handoff **comprehensible and decision-ready** to a
    reviewer not embedded in the code: background + options + recommendation + risks; uplevel from
    code detail to decision framing (the agentic-mode manifestation);
  - **pull** — tools the human *invokes* to understand what the AI is doing/using: context and
    dependency visibility, live "what is it drawing on" views (the assistive-mode manifestation;
    absorbs "context transparency", relocated here from `hitl-workflow`);
  - **standing** (added 2026-07-18, critique panel) — explanations *attached to AI output* that
    support the human's verdict (`7UB2MD8Z`'s patch explanations; 22JBEZNK's reformatted responses).
    The modes are **illustrative, not exhaustive** — the headline governs.
- **Boundary:** information/lens, never the lever — *acting* on the understanding (gates, checkpoints,
  approvals) → `hitl-workflow`; *where* to look → `risk-routing`; a **persistent auditable record**
  (vs a point-in-time view) → `provenance-auditability`.
- **Examples:** `7UB2MD8Z` — explanations improve human patch-correctness judgment (5/6 bugs);
  `KF5MGIBI` — fine-tuned LLM improves review-comment comprehensibility (localization/explanation/fix);
  `IM6DJDEE` — "Consultation Request / Merge-Readiness Packs" as structured handoff artifacts;
  `VG6CIDQW` (Lumen) — human-invoked context/dependency visibility in assistive mode (pull).

**— CROSS-CUTTING (keep the agent on-mandate) —**

**`theme:agent-scope-drift`** (HOS-A) · ~5
- **Captures:** agents range **beyond mandate** / make unreviewed architectural decisions / drift from
  intent; mechanisms that **detect or bound departure from intent** — intent telemetry, guardrails,
  earned-trust autonomy. (Tightened 2026-07-18 from "keep them in scope," which read as absorbing
  *any* control mechanism.)
- **Boundary — tag by the object of the mechanism, not the motivation of the actor (2026-07-18):**
  about *the agent departing from what was asked* (a distinct failure mode from producing buggy code).
  Applies when drift is the mechanism's **operand** — e.g., a multi-agent panel checking the code's
  scope against the spec's scope → `agent-scope-drift` + `ai-review` (object + performer, same
  composition grammar as `formal-methods`). Does NOT apply to generic retained control merely
  *motivated* by drift-worry — counter-example: `Z8TPRNEU` (devs deliberately retain control) →
  `hitl-workflow`, not here. Human-directed control → `hitl-workflow`.
- **Examples:** `95CPB7CF` — intent-level telemetry exposes drift from architectural intent; `8AW26GFK`
  — agents make unreviewed architectural decisions ("vibe architecting").

#### Family 4 — GOVERNANCE & POLICY LANDSCAPE

**`theme:org-governance`** (renamed from `governance-frameworks`, 2026-07-15) · ~9
- **Captures:** the **organizational governance apparatus** — how governance is applied *broadly* across
  the org, pulling oversight together: policy, **audit logging / audit trails**, accountability, roles,
  maturity models, responsible-adoption, runtime policy-as-code. The org's own rules for AI code.
- **Boundary:** the *holistic org-level* governance structure — **not** a single pipeline-integratable
  framework (that's `facet:framework`) and not external law (`regulatory-compliance`). Pairs as
  `org-governance` (internal) / `regulatory-compliance` (external).
- **Examples:** `B4TVIG5Y` — org maturity model for AI-assisted dev; `XJAXB98T` — 12 GenAI governance
  strategies across 67 OSS projects; `HBR7QZ2C` — policy engine → runtime enforcement for agentic AI.

**`theme:regulatory-compliance`** · ~10
- **Captures:** external regulation/standards and legal accountability — EU AI Act Art.14, NIST AI RMF,
  ISO 42001, liability, auditor-ready evidence.
- **Boundary:** driven by an *external* mandate/law/standard. Internal org governance → `org-governance`.
- **Examples:** `XZEHQYNZ` — operationalizing EU AI Act human-oversight for agentic SE; `UW2R6BBJ` —
  NIST AI RMF into lifecycle controls with evidence artifacts; `27YULT5I` — accountability/transparency
  in regulated-finance code migration.

#### Family 5 — SUPPLY CHAIN & PROVENANCE

**`theme:tooling-supply-chain`** (T1) · *full write-up below*
- **Captures:** provenance & vetting of the **AI tooling** that writes/touches code (agent *skills*,
  *MCP servers*, external agents) as its own oversight surface; poisoned/hallucinated dependencies;
  **+ attacks on the oversight layer** (framing attacks, evasion, spec-gaming — a supply-chain attack
  on the reviewer, absorbed from the dissolved T3).
- **Boundary:** governance of *what enters* (tools/deps) and *attacks on the reviewer*, distinct from
  reviewing the emitted code. **D4 ruling (Scott, 2026-07-18, final):** dependency risk
  *in generated code* — hallucinated/poisoned packages the AI writes in — → `ai-code-insecurity`,
  NOT here; this theme keeps the AI *tooling* (skills/MCP/agents entering the toolchain) and attacks
  on the reviewer. Excludes keyword false-positives (hardware
  trojans, classic SolarWinds-class incidents).
- **Examples:** `6ZC3H7AF` — 26% of scanned agent skills carry ≥1 vulnerability, minimal vetting;
  *attacks:* `X7EN6DXZ` — PR-metadata framing biases LLM review, 100% attack success; `T3XTXIXW` —
  obfuscation reliably bypasses CoT LLM review.

**`theme:provenance-auditability`** · ~7
- **Captures:** traceability/provenance of AI *changes* so a human **can** review them — an auditable
  record of what changed and why; IP/licensing vetting; certified components.
- **Boundary:** restoring *reviewability/auditability of the output*, and it **requires a persistent
  record/trace** — a *point-in-time* "what is it using right now" view that captures nothing is
  `oversight-explanation` (pull), not provenance (sharpened 2026-07-18, Lumen). Vetting the *tools* →
  `tooling-supply-chain`.
- **Examples:** `2KPHQ5IV` — AI code leaves no auditable record; typed-graph consensus layer restores it;
  `RG4A4D6K` — provenance-tracking given 20–30% enterprise code is GenAI; `VCI88UZD` — human-certified
  module repositories with provenance + interface contracts.

### Decision log & scoping calls (2026-07-14)
- **`untrusted-overseer` (T3) — DISSOLVED, papers redistributed (Scott, 2026-07-14).** The original T3
  conflated two strands; rather than a standalone theme (scope-expansion risk), its papers were absorbed
  into existing themes:
  - **Attacks on the oversight mechanism** (framing attacks flipping verdicts, obfuscation evading the
    reviewer, spec-gaming/evaluation-evasion: `X7EN6DXZ` `T3XTXIXW` `WBS9U5N7` `T8E8SCCG`) →
    **`theme:tooling-supply-chain`** (an attack on the reviewer is a supply-chain attack on the oversight layer).
  - **Independent / cross-model verification and its reliability limits** — what Scott had called
    "adversarial agents" (one agent validating another): LLM-judge bias, over-rejection, spec-conformance
    misjudgment, AI-reviewing-AI circularity (`BAWCBT9R` `A5WDGC7J` `UDVHQ5HR` `TA6GIUK2` `5NZ2EDEK`) →
    **`theme:ai-review`** (its reliability-limits dimension).
  - No `theme:overseer-reliability` / no standalone T3. **Terminology:** call the agent-checks-agent case
    *independent / cross-model verification*, not "adversarial" — reserve "adversarial" for the attack sense.
- **`spec-driven-guardrails` — RESOLVED → context, NOT a theme (Scott, 2026-07-14).** Secure-by-
  construction / spec-as-gate / executable-requirements / active-rules (`C88VGWMI` `TA6GIUK2` `7SH86C2W`
  `JCTP8VXP` `6ZW9QNQH` `WRXR2VTP`) constrain *what gets generated* — by the oversight-vs-steering
  discriminator this is **steering, not oversight**, so it does not get a solution theme (consistent with
  `DPKKMXSA` and other steering papers). Such a paper still gets tagged by any *oversight* facet it does
  carry (e.g. `TA6GIUK2`'s AI-reviewing-AI point → `ai-review` limits); the steering contribution itself
  is context.
- **`theme:remediation-gating` — ADDED (Scott, 2026-07-14).** Fills the **Fix** slot in the
  Detect→Triage→Fix→Escalate pipeline; scoped to *oversight of autonomous fixes* (gating/filtering/
  escalating the fix), not the repair technique. Thin at present (seed `GAD5Z8PV`) — populate in the sweep.
- **HOS axes thin at the core tier** (kept as HOS-side design findings, not themes): context-window
  assembly ("less is more"), cost-tiered review economics.
- **Detect-stage naming (Scott, 2026-07-14):** the two detector themes are named for legibility to a
  non-specialist reader — `theme:ai-review` (**probabilistic** detector — AI judges, can hallucinate)
  and `theme:rules-based-checks` (**deterministic** detector — grounded/checkable, incl. tests & formal
  methods). Kept **separate** (retracting the earlier fold idea): the judgment-vs-grounded distinction is
  the load-bearing "gate on a computed, producer-independent signal" axis and `TA6GIUK2`'s
  "AI-reviewing-AI is circular without an executable spec." Both sit under **Detect** in the
  Detect→Triage→Fix→Escalate pipeline.
- **`theme:formal-methods` — ADDED as a composable technique tag (Scott, 2026-07-15).** Resolves the
  "is formal methods really rules-based?" question without splitting a standalone solution theme.
  Formal methods is a *technique* orthogonal to the *performer*: pair `formal-methods` with `ai-review`
  (AI does it) or `rules-based-checks` (classical engine does it). This makes the **rename of
  `rules-based-checks` unnecessary** (the technique is now tagged separately) and **encodes the adoption
  hypothesis** in the taxonomy: classical+human-authored = niche/high-assurance; **AI-automated
  (autoformalization) = the plausible uptake path** because it removes the spec/proof-authoring burden
  practitioners actually object to — gated on the check being cheap/fast (economics caveat). Added
  **now** because it is *additive* (doesn't redefine existing themes) and no Set A paper involves formal
  methods, so it doesn't disturb the frozen calibration.
- **Open pruning question:** Family 1's three problem themes could collapse toward one
  `theme:problem-evidence` if the problem side should be smaller. Left expanded pending review.
- **`oversight-explanation` BROADENED + freeze lifted → human vetting pass (Scott, 2026-07-18).**
  Reading Lumen `VG6CIDQW` (Set A), the human overturned all four models' **unanimous** primary
  `hitl-workflow` — a category error, not a ranking call: Lumen's "context control" lever is
  *input-side steering*, and its oversight contribution is comprehension. `provenance-auditability`
  was also rejected (point-in-time view, no persistent record). Resolution: `oversight-explanation`
  = **helping the human understand what the AI is doing** — *push* (decision-ready escalation
  handoff) or *pull* (human-invoked visibility); "context transparency" relocated out of
  `hitl-workflow` (now levers-only); steering exclusion extended to input-side control; transparency
  routing rule added to the preamble. **Process change:** the instrument freeze is lifted — Scott is
  human-tagging the calibration papers as a *vocabulary-vetting pass*; the human-vs-model experiment
  then runs on the vetted instrument (models re-run both sets; Set A human tags are model-informed,
  Set B is the clean comparison). See `Taxonomy_Changelog.md` §11.
- **Set A audit decisions (Scott, 2026-07-18 EOD; changelog §16–§17).** `automation-bias` requires a
  **capable** human (capability discriminator; `22JBEZNK` example → counter-example; the
  oversight-competence-gap candidate is now arbiter-validated). `problem-statement-anchor` bar =
  the **overall** problem statement only; **never on `lit-review`**. `lit-review` = systematic OR
  narrative (synthesized-not-produced test); lit-review primary = **biggest-tent** theme. Mode
  **tie-rule**: reviewable unit dominates initiator. Workflow: **struggle signal** (primary struggle /
  definition-stretching → check the core bar). VibeGuard `remediation-gating` recurrence →
  **compression-gap principle**: every boundary that has ever caught a human must appear in the
  compressed instrument, not just this reference.
- **`steering` + `non-developer` facets — ADDED (Scott, 2026-07-18, vetting pass).** `steering` =
  contribution-type flag (solution operates on generation; audit trail for the steering exclusion;
  steering-only → demote candidate). `non-developer` = population scope flag (end-user/business-user/
  citizen-developer settings; the democratization endgame), completing the mode/object/population
  scope axes and serving as tripwire for the staged *oversight-competence-gap* theme candidate
  (22JBEZNK seed). Facet count 10 → 12. Changelog §12.
- **`assistive` / `agentic` generation-mode facet pair — ADDED (Scott, 2026-07-18).** The oversight
  problem differs qualitatively by mode — acceptance-moment micro-decisions (automation-bias evidence)
  vs artifact-level gating (the scaling inversion + the solution pipeline) — and the axis is not
  recoverable from existing tags. Added **mid-Set-B** under the `formal-methods` precedent: purely
  *additive* scope facets (no theme redefined), so Set A model outputs are undisturbed; the 20
  calibration papers get backfilled in the post-Set-B iteration; TF56EPIP's human tags predate the
  pair. Logged as `Taxonomy_Changelog.md` §10.
- **`design-only` form facet — ADDED (Scott, 2026-07-19, Set B pass).** Positive marker for
  "mechanism specified in buildable detail but never credibly run" (mock demos that fabricate their
  own outputs don't count as building — R4WJZBSF worked example). Motivated by the human stretching
  `intro-framing` to record proposal-ness on R4WJZBSF — evidence the vocabulary had a hole; absence
  of `built-system` was the only carrier and absence is ambiguous. Completes the maturity spectrum
  intro-framing → design-only → built-system → adopted; design-only solution = demote tripwire
  (unevaluated-framework discriminator). Mid-Set-B under the §10 additive precedent. Facet count
  14 → 15; menu 32 → 33. Changelog §19.
- **`metrics` contribution facet — ADDED (Scott, 2026-07-20, Set B pass).** Defines-vs-uses
  guardrail; measurand-rationale rule; object supplied by co-tagged themes (a separate `risks`
  facet was considered and rejected — mention-saturation). Paired with the `risk-routing` boundary
  line: signal-without-allocation ≠ routing (the R4WJZBSF stretch). Risk-quantification instrument
  family staged with a sweep-cluster tripwire. Facet count 15 → 16; menu 33 → 34. Changelog §20.
- **`risk-ip` + `risk-bias` risk-type flags — ADDED (Scott, 2026-07-20, Set B pass).** Bounded
  membership-exception flags for risk types with no theme home, powering the synthesis
  risk×mitigation matrix; substantive-treatment bar (metric / mitigation / empirical result / focal
  analysis — never intro-lists); themed risks excluded (their themes are the columns). Facet count
  16 → 18; menu 34 → 36; facet checklist five → six questions. Changelog §21.
- **`routing-signal` contribution flag — ADDED (Scott, 2026-07-21, E95T8E88 probe; landed
  same-conversation on two-catch evidence).** Signal-framed-for-review-attention without
  operationalized selection; audit trail for the signal-without-allocation boundary (steering
  grammar); mutually exclusive with theme:risk-routing; Triage supply-chain roster. Facet count
  26 → 27; menu 44 → 45. Changelog §29.
- **Data-collection method family — ADDED (Scott, 2026-07-20, B644HQFS probe).**
  `method-self-report` / `method-mining` / `method-experiment` / `method-field-study` — the SLR
  study-characteristics axis; own-evidence-only; multi-apply; lit-reviews get none. Facet count
  21 → 25; menu 39 → 43; checklist six → seven questions. Changelog §25.
- **Risk-flag family made UNIFORM — `risk-security` + `risk-quality` + `risk-overreliance` ADDED
  (Scott, 2026-07-20, same day).** The §21 homeless-only scoping made matrix columns depend on
  rationale text-matching for themed risks (heterogeneous inclusion bars — a methods-validity
  problem the arbiter flagged three ways). Now one bar for all five flags; flag = engagement,
  theme = lift, co-occurrence expected. Also: explainability three-way routing (judging-support →
  oversight-explanation · code comprehensibility → quality · model-XAI → general-ai); measurand
  fixed vocabulary; define-only ≠ theme-membership line (first catch: R4WJZBSF automation-bias +
  oversight-explanation over-tags). Facet count 18 → 21; menu 36 → 39. Changelog §22.

⚠️ **Namespace note:** a *legacy* topical `theme:*` set already exists at scale (`theme:governance` 170,
`theme:oversight` 163, `theme:risk` 104, `theme:orgs` 105, …) from an earlier bulk pass. Exact-slug
filtering on the synthesis slugs above is unambiguous; decide separately whether to re-prefix synthesis
themes (e.g. `syn:<slug>`) or leave them.

---

## Theme 1 — The AI-tooling supply chain as an under-governed oversight surface

**One line:** software supply-chain governance is a mature, largely *solved* discipline for
open-source dependencies (allowlists, provenance/SLSA, review gates) — but it has **not** been
extended to the AI tooling that now writes and touches code (agent *skills*, *MCP servers*,
externally-sourced agents), which install and execute with *implicit trust and minimal vetting*.
Governing the **provenance and vetting of the tools** is an oversight surface in its own right,
distinct from reviewing the code they emit.

**Origin:** Scott's practitioner observation — Microsoft (and mature orgs) enforce strict OSS
supply-chain security (approved-package allowlists, restrict-to-vetted, SLSA provenance, review
processes). The same discipline *should* apply to externally-sourced skills/agents, but the
evidence shows it currently doesn't — so the analysis must scope the supply chain **broadly**.

**Three layers to scope:**
- **Layer 0 — the established discipline to inherit from:** `7S24HQUN` (accountability in
  algorithmic supply chains), `2WGHN2NR` (reproducible builds), the SLSA/provenance cluster
  (`3PZZ4ADM`, `NTVE3RS8`, `P2KI2BFW`, `T49KME27`…), `CMNVQ7CX` (code provenance).
- **Layer 1 — the code the AI *generates* (poisoned/hallucinated dependencies):** `2KQ93JHX`
  (package hallucination / slopsquatting), `QKWS7WF4` + `TA8IPAW4` (trojan-trigger detection in
  code LLMs). *(Numerous model-poisoning studies exist but were mostly discarded as model-internals
  without an org-oversight angle: `7FKKZFHN`, `PK3MHVVN`, `GUR6XUU2`, `W49WX6KP`, `HUVIWYNF`.)*
- **Layer 2 — the AI *tooling* itself, sourced externally (the new surface):**
  - **Anchor:** `6ZC3H7AF` "Agent Skills in the Wild" — 26.1% of 31,132 scanned skills carry ≥1
    vulnerability (prompt injection, data exfiltration, privilege escalation, supply-chain), 5.2%
    high-severity; skills "execute with implicit trust and minimal vetting."
  - Defenses/architecture: `RMRMXUT4` (skill-poisoning attack taxonomies + defense architectures),
    `CIP9FBM3` (MCP-server security, empirical), `7ECA3PNE` (MCP guardian), `CJ6UBWCX`
    (authorization boundary / AI gateways), `Z6RB7NDA` (secure tool-integration patterns),
    `33HNWZ53` (AgentClick — skill-based human-in-the-loop review), `LZPAIXTQ` (model supply-chain
    security).

**Why it's core-relevant (not just security trivia):** it is *oversight of what enters the
codebase* — the provenance/vetting gate for the tools, mirroring the code-review gate for the
output. It connects to the oversight-scaling inversion (`Problem_Statement_Evidence.md`): the same
"install and run with minimal vetting" reflex that merges AI PRs unreviewed also installs agent
skills unvetted.

**Research angle:** treat externally-sourced agent tooling as a **new dependency class** requiring
the same — or adapted — software-supply-chain governance (allowlists, provenance, vetting/review
gates); characterize where that governance exists, where it's absent, and what adaptation the
agentic setting demands.

**Scope note — keyword false positives excluded:** hardware trojans (`DMLNDC2K`, `TPRVD7RL`,
`GNN4TJ`, `SPICED`), classic/general supply-chain incidents (`2DWGC5EB` SolarWinds/Kaseya, the xz
news items, `SH5GMI78` Industry-5.0, `TQ9696RG` logistics), and MCP-labelled off-topic items
(`I9RZSX7J` Llama-3, `RBI76C2G` MCP marketplace commerce) matched the sweep but are out of scope.

---

## Theme 2 — Explanation comprehensibility: the last mile of oversight

**One line:** an accurate escalation or finding is **inert if the human can't act on it**.
Effective oversight requires the AI's *handoff explanation* to be comprehensible and
decision-ready to a reviewer who is **not already embedded in the code** — which means
**upleveling** from code-level detail to a decision framing: *context → the problem →
options/tradeoffs*. Routing the human's attention (see `VTDG995V`) is only half the job; the
handoff explanation is the other half, and it is where oversight silently fails.

**Scope broadened (2026-07-18):** the theme now covers the *information side of oversight*
generally — not only the **push** handoff this write-up describes, but **pull** comprehension
tooling the human invokes to see what the AI is doing/using (Lumen `VG6CIDQW`: context/dependency
visibility in assistive mode). The write-up below is the push/agentic manifestation; the Tag
reference above is the operative definition.

**Anchor — `7UB2MD8Z`** (Explainable automated debugging / AutoSD): empirical — participants
*with* explanations judged AI-generated patch correctness **more accurately in 5 of 6 bugs**, and
the tool signals *when it is confident*. The unstated corollary (and the design crux): the
explanation only helps if it is comprehensible — an accurate escalation with an opaque rationale
does not improve the human's gate decision.

**Corpus cross-refs:**
- `IM6DJDEE` — its "Consultation Request Packs" / "Merge-Readiness Packs" are exactly structured
  escalation/handoff artifacts for this; the vocabulary for a decision-ready explanation.
- `VTDG995V` — attention-routing (confidence → review intensity) is the complement: *where* to look
  vs *what to understand once you look*.

**Practitioner instance (HOS field note).** In HOS, raw model-generated explanations assumed the
reader was already embedded in the code, so they were **unusable to the very reviewer being
escalated to** (escalated *because* they are not in the weeds). Fix: force structure — explicit
instructions to supply **context, articulate the problem, and lay out options/tradeoffs** — and
**uplevel the discussion** from implementation minutiae to the decision level. This is the
real-world validation of the theme; recorded in HOS `Improvements/ENHANCEMENT_IDEAS.md`.

**Why core-relevant:** the explanation is the **interface between the AI's finding and the human's
gate decision** — an oversight mechanism (core Part-2), with empirical support. It is the design
dimension the tool-capability/eval papers miss.

**Research angle:** characterize what makes an oversight/escalation explanation *actionable* —
abstraction level (upleveling), required context, and explicit options/tradeoffs — as a first-class
design requirement of scalable human oversight, not an afterthought.

---

## Synthesis / theme-tag vocabulary (for the theme-tagging pass)

**→ The operative reference is the [Tag reference — full working vocabulary](#tag-reference--full-working-vocabulary-2026-07-14)
section at the top of this doc** (facet tags + all theme tags, each with what it captures, boundaries,
and example keys, plus how the three tag layers stack and what's mutually exclusive). This section is
kept only as a pointer so there is a single source of truth.

Synthesis tags are distinct from the screening-lineage tags (`source:`, `s1:`, `s2:`, `s3:`,
`centrality:`, `superseded-by:`, `cocite:`): they mark *why an item matters to the argument*,
independent of core/context disposition, and are applied liberally (an item can carry several).

---

## Candidate corpus-level finding — "where to look" is well covered; "does looking work" is not (2026-08-24)

**Status: UNVERIFIED. Do not use until counted.** Recorded during the Light Read pass so it is not
rediscovered at synthesis.

**The claim:**

> The literature is rich in deciding **where to look** and poor in measuring **whether looking works**.

**Where it came from.** Langer et al. (`5DCQDB4C`, Context) imports Signal Detection Theory into the
human-oversight setting, which supplies vocabulary the corpus otherwise lacks:

- **Response criterion (`c`)** — how readily the overseer accepts. Set optimally by the *prior
  probability of a defect* and the *cost of a miss*.
- **Sensitivity (`d′`)** — whether the overseer, once looking, actually *detects* the defect.

Under that frame, **risk-routing is criterion-setting**. "This file is historically buggy, review it
harder" is adjusting `c` by base rate — the same mechanism, in operational rather than SDT language.
(Noted by the arbiter of HOS's own risk rating, which does this without using SDT terms.)

**The apparent asymmetry:**

| Half of SDT | Corpus coverage |
|---|---|
| **Criterion-setting** — where to look, what to prioritise, how to route | Heavily populated: `risk-routing` is among the largest themes; `TJH7QFAX` (Borg), `BU73N7PC` (Abreu), `6F3S8IB7` (HAIF), `3ZVMBGPB` (Kamalı) all contribute allocation machinery |
| **Sensitivity-measuring** — whether the reviewer catches what they are shown | Apparently scarce: `9MV2IVNU` (Eze) operationalizes it as override rate (*"an extremely low OR may indicate rubber-stamping"*) and was **2 of 128** on the `oversight-theater`+`metrics` scarcity count (§53) |

**How to verify (do this at synthesis, not now):** classify Core papers into criterion-setting
(contributes a routing/prioritisation signal or allocation logic) vs sensitivity-measuring
(measures whether human review actually detects defects), and count. Beware double-counting papers
that do both, and beware treating *proposing* a gate as *measuring* its effectiveness.

**Why it matters if it holds.** It is a gap statement of the kind an SLR exists to produce, and it
converts into a direct survey question for the dissertation: *do organizations know whether their
reviewers catch what gets routed to them?* Most likely do not — which would make the gap both a
literature finding and an empirical one.

**Caveat.** The asymmetry may be an artifact of the instrument rather than the literature:
`risk-routing` is a theme with a facet family behind it, while "measured detection effectiveness"
has no tag at all. Check whether the absence is in the papers or in the vocabulary before reporting
it.

## Synthesis thread — OVERSIGHT EFFECTIVENESS as the outcome variable (SQ2, opened 2026-08-25)

**Arbiter framing (2026-08-25):** *"Oversight effectiveness … that is really 'is the human oversight
actually working'. Factors that feed into that are automation bias, oversight theatre, etc."*

That sentence reorganises a whole theme group. The corpus's *Limits of current oversight* themes are
all **determinants**; effectiveness is the **outcome** they determine, and it has no home:

| Existing theme | What fails | Role |
|---|---|---|
| `automation-bias` | the human checker | determinant |
| `oversight-theater` | the process / authority to act | determinant |
| `evaluator-reliability` (staged) | the AI checker | determinant |
| **— none —** | **whether oversight actually caught anything** | **outcome** |

**This is NOT `evaluator-reliability`, and the boundary is the arbiter's** (2026-08-25):
*"Not evaluator reliability. That would apply to this LLM compared to that LLM."* That candidate is
scoped to an **AI evaluator audited against another model or ground truth** — three anchors, all
`demote:context` (`WBS9U5N7` Alami, `BAWCBT9R` Zhao, `UDVHQ5HR` Jin), all also carrying
`primary-proposed:`. Two earlier notes of mine wrongly stretched it: `ZGST9CY6` (Zhu) was filed there
as a "converse instance," and `84D2AMVM` (McKay) was read as firing its promotion tripwire. **Both
were out of scope** and are relocated here. The `evaluator-reliability` entry in
`HOS_Seeded_Theme_Candidates` §E needs those two passages struck.

**Why a synthesis thread and not a tag.** A tag marks what a paper is *about*; these papers are not
about the same thing. McKay surveys determinants, Zhu prescribes signals to track, Langer supplies a
formalism. What unites them is that they bear on **SQ2 — "how and why is current oversight
insufficient"** — which is a synthesis axis, not a subject. Promotion to a tag stays available and is
cheap; un-tagging a wrong candidate across items is not.

**Instances.**
- **`84D2AMVM` McKay (ANCHOR, read 2026-08-25).** The only paper so far whose subject is oversight
  effectiveness itself. Surveys a century of human-factors work for determinants — conformity,
  complacency, persuasion, workload, unequal treatment of active vs passive error, and
  *"organisational policies and norms which may deter thorough review and human challenge of AI
  recommendations."* Names the measurement gap outright: *"an urgent need for evaluation approaches
  useful in selecting promising overseer candidates"*, *"robust measurement methodologies"*,
  *"performance measurement approaches which support incentives for active oversight."* Also supplies
  the proportionality principle (§3.2) that oversight requirements should scale with the risk of
  oversight *failure*.
- **`ZGST9CY6` Zhu.** Prescriptive, machine + human: every pattern closes with "Signals to track" —
  veto precision, audit reversal rate, inter-rater agreement against a golden set, incidence of
  "right answer, wrong reasons", disagreement rate with rules baseline.
- **`5DCQDB4C` Langer, Baum & Schlicker (2024) — ALREADY ADJUDICATED, `demote:context`.**
  *Effective human oversight of AI-based systems: a signal detection perspective on the detection of
  inaccurate and unfair outputs.* Tagged `primary:theme:automation-bias` + `general-ai` +
  `intro-framing` + `risk-bias` + `risk-overreliance`. No verbal definition of oversight; it
  **operationalises** effectiveness via signal detection theory — d′ (sensitivity) separated from
  criterion (threshold), which is exactly the distinction the risk-routing argument needs and which
  nothing else in the corpus supplies. **Its Context tier does not diminish its value to this thread:
  tier ≠ dissertation value (§55c), and this is the thread's formal backbone.** Worth revisiting at
  synthesis specifically for the d′/criterion framing.
- **`TW4I6DU6` Sterz et al. — UNREAD, check on arrival.** *On the Quest for Effectiveness in Human
  Oversight: Interdisciplinary Perspectives.* Contains an explicit definition — *"We understand human
  oversight to be the supervision of a system…"* Six authors across dependable systems, DFKI and law.
  **Corrects a provisional claim:** McKay is the only definitional paper *so far*, not in the corpus.
- **`9HPPSFM6` Green — UNREAD.** *The flaws of policies requiring human oversight of government
  algorithms* — argues oversight policies assume humans can reliably correct AI errors, an assumption
  unsupported by evidence. The strongest counterweight in the corpus to any permissive reading.

**Relationship to the "where to look vs does looking work" finding (§ above).** Same observation one
level up. That entry contrasts *criterion-setting* against *sensitivity-measuring* at the level of
**mechanisms**; this thread is the same asymmetry at the level of **the oversight system as a whole**.
If both hold, they reinforce: the corpus is populated with allocation machinery and with named failure
modes, and thin on evidence that any of it demonstrably works. **Verify them together at synthesis** —
they share a counting method and would share a caveat, since either could be an artifact of an
instrument built to capture mechanisms rather than outcomes.

**Regulatory hook (worth carrying into the discussion).** EU AI Act Art. 14(4)(a) requires the
overseer *"remain aware of the possible tendency of automatically relying or over-relying on the
output."* Automation bias is therefore not merely a quality concern but a **compliance** one — which
gives the determinants above legal salience and makes the absent outcome measure harder to excuse.

## FOLLOW-UP — `6ZW9QNQH` (Mitchell) flagged DEMOTE CANDIDATE, contingent on the formal-methods cluster (2026-08-25)

**Not demoted.** Kept Core provisionally; revisit once the `formal-methods` cluster is fully read.

**Why flagged:** a 5,300-word workshop position paper (LMPL '25) whose prototype under-delivers its
own thesis — it advocates autoformalization plus formal verification and implements syntactic checks
plus compilation success. `design-only`, no ladder rung, no method facets.

**Why not demoted now:** the §53 scarcity test cannot be run. `formal-methods` is 7 of 149, and
**three are unread** — `E5SQKRH7` (Sharma, *Assessing correctness in LLM-based code generation*),
`5DI9B43K` (Sistla, *Towards verified code reasoning by LLMs*), `72W6R4JG` (Töpfer, *Vibe-coding:
feedback-based automated verification*). `FZK2QB5A` (Alshahwan, *Assured offline LLM-based software
engineering*) is also unread. Töpfer's title in particular describes Mitchell's proposal implemented.

**Decision rule at revisit:**
- If Töpfer / Sistla / Alshahwan deliver autoformalization-plus-feedback for vibe coding → Mitchell is
  **dominated** (advocacy for what another corpus paper built — the Marri-vs-Zoro pattern, §61) →
  **demote to Context.**
- If none of them covers that ground → Mitchell is the corpus's **position statement of the gap** →
  **keep Core.**

**Preserve regardless of tier** — a causal claim not seen elsewhere in the corpus: *"LLMs prioritize
user commands over code consistency"*, so accumulated natural-language constraints silently
contradict one another and developers do not notice. A specific mechanism for long-run vibe-coding
degradation, adjacent to Casserini's agentic entropy (`95CPB7CF`) and Maes's reviewability decline
(`59ZW4R58`, §A watch item). Cite it for the mechanism even from Context.

## Synthesis thread — INDEPENDENCE OF THE CHECK: why the checker cannot be the producer (opened 2026-08-25)

**Arbiter framing:** *"The score comes from the thing being checked, which is the disqualifier — and
the paper's numbers back it up. This could be important to explaining the importance of having
something else do the checking, and checks and balances."*

**The claim.** An oversight signal is informative only to the extent it is **produced independently of
the artifact's producer**. A model's assessment of its own output is not a check; it is the same
computation reporting on itself. This is a *structural* property, not a quality-of-model property —
it does not improve as models improve.

**What makes this thread unusually strong: the corpus supplies all four legs of the argument.**

**1. The instrument already asserts it (design rule).** `risk-routing` requires *"a computed &
**producer-independent** signal — **model self-confidence is disqualified**."* Recorded as a design
judgement, before any evidence.

**2. The literature prescribes it (design side).**
- `ZGST9CY6` **Zhu et al.** (*AI and Ethics* 2026), mechanism catalogue: *"Divergence detection and
  independent checker — comparison against **a second AI/system**, heuristic, or ruleset with
  alerting… flags cases needing verification when solvers disagree; **avoids blind trust**."*
- `R9CDT9KB` **Mahmud et al.** (ACSAC 2025) build it: three vendors (GPT-4 Turbo, Claude Sonnet 4.5,
  Gemini 2.0 Flash), routing on **inter-model disagreement**, with the rationale stated —
  *"different models exhibit **different blind spots** across vulnerability categories."*
- `5DI9B43K` **Sistla et al.** (Google DeepMind/Google/Meta) use an **external formal verifier** over
  the agent's extracted reasoning — independence by construction, not by ensemble.

**3. The measurement confirms it (evidence side) — this is the new leg.**
`VTDG995V` **Gros, Spiess et al.** (ICSE 2025) test four *producer-internal* confidence measures
(average token probability, sequence probability, verbalized self-ask, QA logit) and find
**ECE 0.09–0.73**; *"intrinsic LLM confidences are **poor predictors of code correctness**."*
Local Platt rescaling against real correctness labels moves ECE **0.46 → 0.04** — which shows the
signal carries *some* information, but only once fitted against an **external** ground truth
(they use test outcomes). **The rescue comes from outside the model.**

**4. Practice violates it (observed side).**
`E9RAWBDT` **Pimenova et al.**: developers, overwhelmed by review volume, *"recommend **delegating
review back to the AI by asking it to audit its own code**"* — with the authors noting *"it is unclear
how effective these strategies are compared to traditional code review."* So the field's default
adaptation to the scaling problem is **exactly the move the design literature forbids and the
measurement shows fails.**

**Why this is the strongest argument shape available in the corpus.** Rule → prescription →
measurement → observed deviation, with independent sources at each step, and no step resting on the
dissertation's own reasoning. The prescription and the deviation were found in separate papers by
separate groups; the measurement was not sought to support either.

**Extension — the checker is not merely dependent but attackable.** `X7EN6DXZ` **Mitropoulos et al.**
demonstrate **100% success** re-introducing CVEs past LLM reviewers via crafted PR metadata, and name
the asymmetry that makes it structural: *"attackers can iteratively refine attacks against a local
clone of the review pipeline, while defenders have only one chance to detect them."* Independence is
therefore necessary but not sufficient — see the §B candidate in `HOS_Seeded_Theme_Candidates`
(*the overseer is itself an untrusted, attackable component*), which `VFNJSZD9` (Hjazeen) asserts and
Mitropoulos demonstrates.

**Caveat to carry.** "Independent" admits degrees, and the corpus shows at least four:
same-model self-report < same-model rescaled against external labels < different-vendor ensemble <
external deterministic verifier. **Do not flatten these into a binary** in the write-up; the
interesting claim is that the gradient exists and that practice sits at the weakest end of it.

**Survey hook.** Ask what produces the signal that decides review depth — the assistant itself, a
different model, or a deterministic tool — and whether that choice was deliberate. The expected answer
is "the assistant," unexamined.

## Analytical frame — THE TWO GATES OF RISK ROUTING (SQ5, opened 2026-08-26)

**Arbiter framing:** *"HOS as 'risk assessment' — and only the thing identified as high risk gets that
enforcement."* Drawn while comparing HOS's rule (human approval of **all high-risk changes, period**)
with VARI's (`5RLPIA3K`), which requires human review of **everything** in its domain and varies only
the depth.

**The distinction.** Risk routing operates at two levels, and papers differ in which they address:

| | **Gate 1 — ACCESS** | **Gate 2 — DEPTH** |
|---|---|---|
| Question | Does this need human review **at all**? | Given that it does, **how much**? |
| Requires | a computed risk assessment | a prioritisation signal |
| Effect on load | **reduces the count of human touches** | reallocates a **fixed** workload |
| Scaling | **this is where scaling lives** | no scaling effect |

**Why it matters: only gate 1 scales.** Gate 2 makes oversight better-targeted, not cheaper. A system
with no gate 1 has a human-attention cost that grows linearly with output no matter how good its
prioritisation is.

**The worked contrast that produced the frame.**
- **HOS** computes the classification, and enforcement applies **only** to what it identifies as
  high-risk. Gate 1 + gate 2.
- **`5RLPIA3K` VARI** *inherits* its classification: EU AI Act **Annex III Point 4(a)** declares
  employment AI high-risk before the system sees anything, so gate 1 is answered "yes, always." Its
  escalation triggers — *"adversary flags moderate or severe bias risk · arbitrator confidence falls
  below threshold · advocate and adversary reach irreconcilable positions · data quality is
  insufficient"* — are genuine computed signals, but they allocate **depth only**.
  It is therefore **the corpus's only gate-2-only design**, and a useful contrast case rather than a
  weak instance of routing.

**Correction this frame supplies.** VARI first read as "anti-scaling," and it deliberately *increases*
per-decision human cost (forced viewing of all three agent outputs before the decision buttons unlock,
time-on-task tracking, random engagement audits). But that is not a design flaw — **given a classifier
that returns "high" for everything, 100% review is the correct policy, identical to HOS's.** The
absence of scaling is inherited from the domain, not chosen.

**Consequences worth testing at synthesis.**
1. **Count gate-1 vs gate-2 contributions across the corpus.** First read: most routing papers are
   gate 1 — Mahmud (`R9CDT9KB`) routes uncertain cases *to* humans, Abreu (`BU73N7PC`) risk-classifies
   which releases get scrutiny, Zhu (`ZGST9CY6`) uses risk-weighted sampling to select what is reviewed
   at all. If that holds, gate 2 is thinly covered and VARI is near-unique.
2. **If all scaling leverage is at gate 1, the quality of the risk assessment is the whole game** —
   everything downstream allocates a budget already set. That is a thesis-shaped claim and it is
   testable against the corpus.
3. **A classifier that over-assigns "high risk" fails expensive, not safe.** VARI-level cost applied to
   work that did not need it: productivity collapses while safety holds. This is the **fail-closed**
   harm (§52 / the Ehsani ruling) arriving through the classifier rather than through reviewer
   saturation.

**Bearing on the Article 14 argument.** The corpus now holds **two opposed readings of the same
Article**: the permissive one (Art. 14 mandates oversight *capability*, not per-item review; 14(5)'s
two-person rule for biometric ID is the carve-out that proves the general case) and VARI's conservative
one (per-item human interpretation required). **Both can be right** — they answer different questions.
The permissive reading is about what the Act requires *in general*; VARI's is about what it requires
*once a system is already inside Annex III*. **The disagreement is over the scope of the high-risk
class, not over the review rule** — which is exactly the gate-1/gate-2 split. Sterz et al.
(`TW4I6DU6`) critique Art. 14 directly and should be read alongside both.

## Exogenous corroboration — the volume→over-reliance shape outside AI coding (`EB49Q8QM`, 2026-08-26)

**Framing material, not a tag.** Tilbury & Flowerday (2024), *The rationality of automation bias in
security operation centers*, was ruled **Context** — the object is SOC alert triage, not AI-generated
code (`general-ai` 2/3, `demote:context` 3/3). Its value is to the **framing**, not the corpus.

**Why it is worth citing anyway.** The paper's motivating chain is the inversion shape, in a domain
with a decade of prior literature and no connection to this thesis:

> *"a commonly discussed challenge is the volume of alerts that need to be assessed"* → SOCs adopt
> automated decision aids to triage → analysts become over-reliant, suffer cognitive skill
> degradation, and **miss flaws despite contradictory information being present**.

Volume exceeds human review capacity → automate the triage → the human check degrades. That is
`oversight-scaling-inversion` feeding `automation-bias`, established **outside** software
engineering.

**How it earns its place in the argument.** It is evidence the dynamic is **not novel to AI coding** —
which pre-empts the obvious objection that this review has found a temporary artifact of an immature
tooling generation. A reviewer who doubts the mechanism in a code-review context has to contend with
it being documented where the alert volumes have been overwhelming for years.

**Connects to:** the oversight-effectiveness thread (SQ2) — Tilbury's four critical success factors
are conditions under which automated triage *retains* a working human check, which is the same
outcome variable that thread is organized around.

**Caution on transfer.** SOC triage is a *detection* task with a ground-truth outcome (the alert was
real or it was not); code review is not. Use the paper for the **shape of the failure**, not for
effect sizes or for its CSFs as portable controls.

## Independence thread — a design that gets it half right (`DJMBHHZN`, 2026-08-26)

Feeds the **INDEPENDENCE OF THE CHECK** thread. MOSAICO (Tisi et al.) is the first corpus design that
**instantiates producer-independence architecturally** and then partially undercuts it.

**Right:** two levels. First-level *solution agents* propose; separate second-level *supervision
agents* evaluate. The checker is structurally not the producer — which is the thread's normative
claim rendered as an architecture rather than an exhortation.

**Wrong:** the governance language admits *"the uncertainty agents can have about their own answers"*
as an input to the decision. That is **self-reported producer confidence**, the anti-pattern §74
names. A design can be independent at the layer that matters and still readmit the producer's own
signal through a side channel.

**Why it earns a place in the thread:** most corpus papers either violate independence without
noticing or assert it without mechanism. This one shows the failure is not binary — independence is a
property of *each signal*, not of the architecture as a whole. Any org-survey question about
"independent review" needs to ask what the reviewer *sees*, not just who the reviewer is.

**Second contribution — oversight as configuration.** MOSAICO relocates the human from inspecting
artifacts to **authoring policy** (agreement type, minimum votes, deadlines, confidence thresholds).
This is a distinct answer to **gate 1** of the two-gate frame: not "route risky artifacts to humans"
but "let humans set the conditions under which machine agreement suffices." Directly convertible into
survey instrument: *does your org define, in writing, what agreement level is required before AI
output is accepted?* Almost nothing else in the corpus generates that question.

## OPEN DESIGN NOTE — the dissertation bucketing schema is doing two jobs (2026-08-26)

Parked for the schema work, recorded now while the reasoning is fresh. **Dissertation
Primary/Supporting currently conflates two independent axes:**

- **evidential weight** — how much the paper's findings can support a claim
- **construct value** — how much it shapes the argument, vocabulary, or survey instrument

Three papers already adjudicated make a natural **test set**, because they sit at different points and
cannot be ordered on one axis:

| Paper | Evidential weight | Construct value | Ruled |
|---|---|---|---|
| **MOSAICO** (`DJMBHHZN`) | **none** — design-only, month 3 of 36, nothing measured | **high** — governance policy language, agent repository w/ KPIs, oversight-as-configuration | SLR Core · Diss **Primary** |
| **Kim & Yegge** | low — self-report, authors' own anecdotes | moderate — practitioner framing | SLR Core · Diss **Supporting** |
| **Sidney** | low — vendor whitepaper, no study | moderate — risk-tiered review depth | SLR Core · Diss **Primary** |

**Consequence to carry:** if MOSAICO stays Primary, it must be flagged **construct-source** so nothing
downstream cites it as *support* for a claim. A one-bit evidential marker on the dissertation buckets
would remove the ambiguity — worth deciding when the schema is built, not per paper.

## UPDATE to the Mitchell demote decision — Töpfer read; domination is PARTIAL (2026-08-26)

`72W6R4JG` (Töpfer) is now adjudicated. Against the decision rule recorded above:

**Delivered:** formal-constraint-driven feedback for vibe coding, implemented and evaluated. The
constraint verifier checks FCL formulas over execution traces and emits repairable counterexamples;
the LLM repairs autonomously within a bounded 10-iteration gate. This *is* Mitchell's proposal built —
for the **feedback** half.

**Not delivered — autoformalization.** Töpfer's constraints are **hand-authored by the domain expert**.
The paper names reducing *"the manual effort of 'constraint engineering'"* as future work. Mitchell's
specific advocacy was autoformalization *plus* verification; the automatic derivation of formal specs
from natural language remains unclaimed by any read paper.

**Status: RESOLVED 2026-08-27 — Mitchell KEEPS Core.** `FZK2QB5A` (Alshahwan) was the last candidate
and does **not** close the gap: its twin guarantees are *"does not regress the properties of the
original code"* — **regression against existing behaviour, not specifications derived from intent**.
No corpus paper delivers autoformalization plus feedback, so **Mitchell survives as the corpus's
position statement of that gap** (§105a). Decision closed.

**Coupling to watch (§77).** If the `formal-methods` definition is ever narrowed to proof-grade work,
the cluster shrinks below 7 of 149 and the §53 scarcity test moves in Mitchell's favour — a *smaller*
cluster makes Mitchell more likely to survive as the corpus's position statement of the gap. The
definition call and the tier call are coupled; resolve the definition first.

## The scaling problem stated from the REGULATORY side (`XZEHQYNZ`, 2026-08-26)

Tuape et al. is Context (secondhand, preliminary) but sits in **Dissertation Supporting** because it is
one of the few corpus papers treating the EU AI Act as **subject** rather than motivation — and because
it engages it correctly (§78), which makes it citable as framing rather than as evidence *about* the
field's misreadings.

**Two extracts worth carrying.**

**1. The inversion, arrived at from regulation rather than from practice:**

> *"This creates a reinforcing cycle where the desire for greater AI automation in software development
> is directly challenged by the absence of frameworks that support human understanding, intervention,
> and ethical alignment **at scale**."*

Same shape as `oversight-scaling-inversion`, reached from a completely different direction: not "review
capacity is exceeded so bad code ships," but "the compliance obligation cannot be discharged at the
volumes automation produces." Useful because it means the scaling claim does not rest solely on
practitioner-reported review capacity — a regulatory-analysis paper reaches it independently.

**2. A two-tiered adoption hypothesis — and a survey question:**

> *"while basic automation using AI in software development is emerging (e.g., code suggestions), the
> more complex and high-risk applications of Agentic AI necessitate a profound re-architecture of
> development methodologies… This suggests a **two-tiered adoption scenario**."*

This is a **risk-routing-shaped claim at the adoption level** — routing not individual artifacts but
whole *modes of use* into different governance regimes. Directly testable in the org survey: **do orgs
actually bifurcate their governance between assistive and agentic use, or apply one policy to both?**
If they bifurcate, the two gates (§SQ5) are operating at organizational rather than artifact
granularity — which is the altitude question the ZUM76CCG ruling raised, arriving here from the
regulatory side.

**Bucketing note:** third data point for the schema — high construct value, low evidential weight, and
unlike MOSAICO also *secondhand*. See the open design note above.

## TRIPWIRE on the two-gate frame — the UN-ROUTED REMAINDER (staged 2026-08-26, `ZBF86IJM`)

**Status: staged, not adopted.** One instance, out of scope, token granularity. Do not carry into the
argument until a second instance lands at artifact granularity.

**The claim being watched.** Risk-routed oversight is the thesis's answer to scaling: send the risky
things to humans, let the rest through. Gate 1 therefore always produces an **un-routed remainder** —
and the open question is whether that remainder receives *the same* reduced scrutiny it would have got
under no routing at all, or **less**, because the absence of a routing signal is read as an
endorsement.

**First instance — Vasconcelos et al. (`ZBF86IJM`, Context).** Token-level uncertainty highlighting in
AI code completions, n=30, within-subjects:
- *"several participants mentioned that they **interpreted a lack of highlights as signal that the code
  was correct**."*
- *"By editing **only the tokens highlighted**… participants would be able to pass the provided unit
  tests… **but their code would improperly handle an edge case**."*
- The authors' own caution: *"we may find that we are simply **shifting** the automation bias such that
  people are applying an insufficient level of skepticism to the highlights, where before they were
  insufficiently skeptical of the code completion itself."*

**Why it matters if it replicates.** It would mean risk routing does not merely *reallocate* scrutiny
but **destroys** some — the routed items gain attention while the un-routed lose more than they had.
That converts an efficiency mechanism into a net-negative one at some ratio, and it is the empirical
form of the concern raised against Sidney (requiring inspection of everything but varying depth — the
shallow path acquires a false clean bill of health).

**Why it is NOT yet usable.** Assistive mode, token granularity, three puzzle tasks, and the accuracy
effect was not significant (p = 0.145). At PR granularity the human faces a different task entirely.
**Promote on:** any paper observing reduced scrutiny of un-flagged *artifacts* (not tokens) in an
agentic or PR-review setting.

**Related but distinct:** the independence thread's measurement leg stays with `VTDG995V` — that is
about whether the *signal* is any good; this is about what humans do with the *absence* of one.

## Inversion mechanism — DIMENSION COLLAPSE, or why capacity is not the only story (`2KPHQ5IV`, 2026-08-26)

Wang et al. supply an `oversight-scaling-inversion` instance whose **mechanism differs from every
other instance in the corpus**, and the difference is worth preserving in the write-up.

**The standard account (capacity).** Volume of AI-generated change exceeds the time humans have to
review it; review degrades; bad code ships. `E9RAWBDT`, Pimenova, and the practitioner-reported
accounts all run this way.

**Wang's account (representation).** The bottleneck is not time but **the artifact itself**:

> *"the dominant artifact of AI-assisted development (code plus chat history) performs **dimension
> collapse**, flattening complex system topology into low-dimensional text and making systems opaque
> and fragile under change."*
> *"Reviewers cannot determine what invariants were assumed, what changed, or why a regression
> occurred. **This is not a generation failure but a control failure.**"*

On this account, **more review time would not fix it** — the information required to review was never
recorded. Scaling makes it worse because *"opacity accumulates faster than humans can inspect it"*,
degrading into **"scaled opacity."**

**Why it matters to the argument.** It splits the inversion into two mechanisms with **different
remedies**:

| Mechanism | Bottleneck | Remedy implied |
|---|---|---|
| **Capacity** | reviewer time vs. change volume | routing, prioritisation, more reviewers, better tooling |
| **Representation** | the artifact cannot carry the commitments | change the primary artifact so review is *possible* |

Routing — the thesis's main scaling answer — **only addresses the first.** If representation is the
binding constraint, routing a reviewer to the right diff still leaves them unable to determine what
was assumed. This is a real limit on the two-gate frame and should be stated rather than glossed.

**Connects to:** the reviewability-decline watch item (Maes, §A in `HOS_Seeded_Theme_Candidates`) and
Mitchell's degradation mechanism (`6ZW9QNQH` — accumulated natural-language constraints silently
contradicting one another). All three describe *review getting harder*, independent of volume.
**Watch for a fourth; if the cluster holds, "reviewability decay" is a finding distinct from the
capacity inversion.**

**Survey hook.** Ask whether reviewers of AI-generated changes can determine *what was assumed* — not
whether they have time. The two constraints have different fixes and orgs likely conflate them.

## CANDIDATE FINDING — the inspection point may be absent, not merely degraded (opened 2026-08-26)

**Status: two instances, tripwire set at three.** This is the sharpest form the thesis's problem can
take, and the instrument currently cannot express it (§81).

**The claim.** The review's framing assumes oversight *degrades* under scale — reviewers get less
time, less context, less authority. A stronger possibility is visible in the corpus: a mode of
development in which **no human inspects the generated artifact at any point**. Not rubber-stamping a
diff nobody understands, but never opening it.

**Where it lives in the instrument.** Not in the generation-mode pair — that was the first attempt and
it was wrong (§81). Modes describe how code is *produced*; whether anyone reads it is an *oversight*
property, so it belongs on its own axis. **`no-inspection` is staged as an orthogonal flag** (§81a),
composable with either mode: `agentic` + `no-inspection` says what neither says alone. Arbiter, ruling
on `T2EG4BE2`: *"Not assistive. **Human likely not even looking at the code.**"* — the observation was
right; the channel was not.

**Instance 1 — observed practice.** `T2EG4BE2` (Waseem et al.): *"a single 'fix this' prompt can
rewrite large parts of the codebase **before architects or testers have seen the previous version**."*
Their industry teams treat VC as *"unsafe by default for customer-facing systems"* — an admission that
the default path has no inspection in it.

**Instance 2 — deliberate design.** `72W6R4JG` (Töpfer et al.), titled *"…with **no human code
inspection**"*: the human authors formal constraints and never reads the generated adaptation manager.
Here the absence is **engineered and defended**, on the argument that a formal checker substitutes.

**The two instances are the interesting part.** The same absence arrives from opposite directions —
one as a practice that emerged without anyone deciding it, one as an explicit engineering position
with a compensating mechanism. That contrast is the argument: **the question is not whether humans
inspect less, but whether the inspection point exists at all, and if not, what stands in for it.**

**How it reframes the two gates.** Gate 1 asks *does this need human review?* Both instances answer
"no" — but only Töpfer answers it *deliberately*, with a replacement. Waseem's teams answer it by
default, with nothing. **An org can arrive at zero-inspection by design or by drift, and those look
identical in the artifact.** That distinction is exactly what an org survey can detect and a code
audit cannot.

**Survey hook.** Not *"how thoroughly is AI-generated code reviewed?"* but **"is there a point in your
process where a human is required to read it — and if not, what replaced that?"** The expected finding
is that some orgs cannot answer the second half.

**Promote on:** a third instance. See §81 for the vocabulary options (a `no-inspection` scope flag vs.
an explicit third mode); do not graft mid-measurement (§41).

## SQ5 REFINEMENT — risk routing has two purposes, and only one of them scales (2026-08-26)

**Arbiter, ruling on `RG4A4D6K`:** *"I can buy detection as risk routing. **It isn't tackling scaling at
all, just ensuring review.**"* That distinction should be carried into the two-gate frame, because it
changes what a count of routing papers means.

**Gate 1 asks *does this need human review?* — but papers reach that gate from opposite directions:**

| | Question asked | Human load | Corpus examples |
|---|---|---|---|
| **Load-reducing** | what can safely **skip** review? | **down** | the risk-tiered review-depth designs; `ZUM76CCG`; Sidney |
| **Coverage-ensuring** | what must **not** skip review? | **up** | `RG4A4D6K` (detect AI-authored code → targeted review) |

**Only the load-reducing kind is a scaling mechanism.** The coverage-ensuring kind is a *quality*
mechanism that happens to use the same machinery — it finds work that was escaping oversight and adds
it back. **A corpus count of `risk-routing` cannot be read as a count of scaling mechanisms without
separating these.**

**Why this is more than bookkeeping.** The two have opposite relationships to the inversion. A
load-reducing router is a *response* to the inversion — it exists because review capacity is
exhausted. A coverage-ensuring router *deepens* the capacity problem: it adds review load in exchange
for catching what was slipping through. **An org adopting both is pulling in two directions**, and
whether the net effect relieves or worsens the inversion is an empirical question about the ratio —
one the survey could actually ask.

**Shared failure mode, in both directions.** The absence of a routing signal gets read as a clean bill
of health:
- load-reducing — un-flagged artifacts read as safe (`ZBF86IJM` tripwire: *"interpreted a lack of
  highlights as signal that the code was correct"*)
- coverage-ensuring — **detector false negatives make AI-authored code read as human-authored**, and
  human-authored code attracts ordinary, unheightened review

So the un-routed-remainder problem is not a quirk of one design; it is **structural to routing as
such**, and it strengthens the case for promoting that tripwire if a second instance lands.

**Survey hook.** Ask both halves separately: *what lets a change skip review* and *what forces a change
into review* — and whether the same signal drives both. Orgs likely have one and not the other.

## MECHANISM — SUBSTITUTION: when oversight holds, senior building capacity pays for it (`F2C2DWSI`, 2026-08-26)

Xu et al. supply something no other corpus paper does: **a price tag on oversight that does not fail.**

**The finding.** A difference-in-differences study over a monthly GitHub panel (July 2020–July 2022)
following Copilot's introduction. Productivity rises — but the gain is concentrated in
**less-experienced (peripheral)** contributors, whose code *"requires more rework to satisfy repository
standards."* The rework lands on **core** developers, who **review 6.5% more code** and show a
**19% drop in their own original code productivity**.

**Why it is not `oversight-scaling-inversion` (§83).** Nothing here shows review being skipped. Review
*holds* — the contributions get revised before integration. What gives way is something else.

**Two release valves under the same pressure.** Rising AI code volume plus falling per-unit quality has
to go somewhere, and the corpus now documents two distinct outlets:

| | What gives way | Observable | Corpus |
|---|---|---|---|
| **Inversion** | the review itself | bad code ships; PRs merged unreviewed; rubber-stamping | `2KPHQ5IV`, `T2EG4BE2`, `E9RAWBDT` |
| **Substitution** | senior *building* capacity | experts stop producing; review load rises | `F2C2DWSI` |

**An organization can be in either state and not know which** — and the two call for opposite
responses. The inversion needs review capacity added; substitution means capacity is already being
paid for, out of a budget nobody is looking at.

**The measurement trap, and why this matters for the survey.** Aggregate throughput went **up**. The
peripheral developers' gains and the core developers' losses **net out**, so an org watching commit
volume sees AI working exactly as advertised while its most experienced people quietly stop producing
anything new. **The cost is real, large, and invisible to the metric most orgs actually track.**

Arbiter's framing: *"as it increases in volume, the focus on the experienced team members is shifting
from building to fixing."* The harm is a **substitution**, not an overtime bill — which is why it does
not show up as a capacity complaint until the pool of experts thins.

**Survey hooks.**
- *Has the share of senior engineers' time spent reviewing versus authoring changed since AI adoption?*
- *Do you measure senior original output separately, or only team throughput?* — the expected answer is
  the latter, which is precisely why the substitution would go unnoticed.

**Connects to:** the reviewability-decay cluster (Wang §80, Maes §A, Mitchell) — those describe review
getting *harder*; this describes who *absorbs* that difficulty and what they stop doing instead.

## FINDING CANDIDATE — when review saturates, communities RESTRICT INTAKE rather than scale review (`XJAXB98T`, 2026-08-26)

Yang et al. is the first corpus paper documenting, at scale and from observed practice rather than
proposal, **what organisations actually do when AI contribution volume exceeds review capacity.**
Multi-stage qualitative analysis of governance materials from **67 highly visible OSS projects**.
Dissertation Primary.

**The answer is not "scale oversight." It is "reduce what arrives."**

Twelve strategies in four functional groups: **entry admissibility and input qualification**;
**responsibility and evidence restoration**; **review burden and workflow protection**; and
**infrastructure and institutional adjustment**. Three of the four operate on the *input side*.

**Practitioners state the thesis themselves, which is rare and citable:**

> Oh My Zsh: ***"review is the bottleneck. Not code generation."***
> FastAPI: low-effort AI submissions are ***"a Denial-of-service attack on our human effort."***
> typescript-eslint: maintainers do not want review to become ***"effectively babysitting someone's
> Claude instance via the code review process."***
> curl: *"fake and otherwise made up security problems effectively **prevent us from doing real project
> work** and make us waste time and resources."*
> Jaeger: *"Code review is a discussion between people, not bots."*

**How this reframes gate 1 (SQ5).** The two-gate frame assumed gate 1 asks *does this need human
review?* — a triage question applied to arriving work. These communities are operating gate 1 by
**exclusion instead of triage**: ban AI-assisted contributions, require disclosure, demand evidence
before review, cap newcomer queues. **The gate is placed before the work exists, not after.**

| Gate-1 posture | Mechanism | Corpus |
|---|---|---|
| **Triage** | assess arriving work, route by risk | the risk-tiered designs; `ZUM76CCG` |
| **Exclusion** | restrict who/what may submit at all | `XJAXB98T` — bans, disclosure mandates, evidence gates, queue caps |

**Why the distinction earns its keep.** Exclusion needs no assessment capacity, which is exactly why
saturated projects reach for it — triage costs reviewer attention, and reviewer attention is the
exhausted resource. **A community with no spare review capacity cannot afford to triage; it can only
afford to refuse.** That predicts a specific organisational pattern: risk-based routing should appear
in orgs with *slack*, and blanket restriction in orgs without it.

**Note this is fail-CLOSED** (§86a): safety holds, throughput collapses, and the harm is productivity.
It is therefore **not** `oversight-scaling-inversion` — and its presence alongside the fail-open cases
(Wang, Waseem, Pimenova) shows the same pressure resolving in opposite directions depending on **who
controls intake**. OSS maintainers can refuse a PR; an employed reviewer facing their own team's output
usually cannot. **That asymmetry is worth testing in the survey.**

**Survey hooks.**
- *When AI-generated contributions exceeded review capacity, did you add reviewers, route by risk, or
  restrict what could be submitted?*
- *Do contributors have to disclose AI assistance? Is anything required before review begins?*
- The 12 strategies are a ready-made response menu — use them as closed options rather than
  free-texting the question.

## ARGUMENT STRUCTURE — "X fails, therefore Y and Z" is OUR synthesis, not the literature's (`PPMTM4DG`, 2026-08-26)

Yu et al., *Fight fire with fire: how much can we trust ChatGPT on source code-related tasks?*
(**IEEE TSE**, Dec 2024). Core + Dissertation Primary. This entry records the **shape of the argument**
it participates in, because the shape needs declaring before the chapter uses it.

**The arbiter's formulation:** *"X doesn't work, need to look for other solutions. Y and Z (which
aren't discussed by X) but address the issues in X's failure."*

### The measurement — the weakest rung, quantified
Yu tests ChatGPT verifying **its own** output across generation, completion, and repair. Missing-report
rates for its own defects:

| Task | Own errors it fails to report |
|---|---|
| incorrect code generation | **67%** |
| failed program repairs | **59%** |
| vulnerabilities in completed code | 23% |

Plus **75% of the explanations** in its self-generated test reports are **inaccurate** for incorrect
code and failed repairs — the artifact a human would read *to check the check* is mostly wrong. And
self-contradictory hallucination: code called correct at generation, incorrect at verification, with
nothing changed in between.

**Stronger in kind than `VTDG995V`.** Gros/Spiess showed model confidence is *poorly calibrated* — a
noisy signal. Yu shows the check **does not work**. Noise versus failure.

**Placement on the independence gradient** (which the thread warns not to flatten):

> **same-model self-report ← Yu** · same-model rescaled against external labels ← `VTDG995V` ·
> different-vendor ensemble ← Mahmud · external deterministic verifier ← Sistla

**Scope caveat — this is a LOWER BOUND.** The self-check runs in the **same session**, so the model has
its own prior output in context: the most degenerate configuration available. A fresh-session same-model
check might do better, and **the corpus does not test that**. Do not present 67% as the general
self-check rate; present it as the worst case, which is what makes it decisive against *"just have it
review itself."*

### The structural point — declare the synthesis
**Yu proposes no fix.** It concludes that human judgement remains essential; it never mentions agent
panels or cross-model checking. **Mahmud and Zhu propose those without citing Yu.** So the chain
*"self-check fails → therefore diverse checkers"* is **assembled by this review**.

**Stated carelessly that is a weakness; stated properly it is the stronger shape** — independent groups,
neither writing to support the other, cf. the independence thread's rule → prescription → measurement →
deviation structure. **But it must be labelled as synthesis in the chapter**, or a committee will read
it as a finding one of these papers reported. It is not.

**The half-claim to avoid.** Yu establishes that **self-verification fails**. It does **not** establish
that **cross-model verification succeeds** — no different-model checker is tested. Cited alone as the
case for panels, it is vulnerable to *"you have shown self-check is bad, not that panels are good."*
The positive half must come from Mahmud (*"different models exhibit different blind spots"*), and even
that is routing on **disagreement** rather than a head-to-head comparison.

### GAP TO VERIFY AT CLOSEOUT
What would close the chain is a study comparing, on the same artifacts:

> model A generates → **A checks** &nbsp;versus&nbsp; model A generates → **B checks**

**I do not believe the corpus contains this** — but that is a claim to verify against the full set
before asserting, not to assume. If confirmed absent, it is a **named research gap** the dissertation
can claim, and a cheap experiment to run given Yu's published setup and datasets. **Action: check the
`ai-review` and `agent-panel` sets explicitly at closeout.**

## PRESERVE FROM CONTEXT — accountability pressure INCREASES AI deference (`E689ZAXC`, 2026-08-26)

Zhou & Zhao, *Review makes workers less likely to revise AI output* (SSRN, 2026). **Ruled Context** —
the task domain is writing social media posts, not code (`general-ai` 3/3, panel demote 3/3). **The
domain is orthogonal; the mechanism is not.** Recorded here because it contradicts a premise the rest
of the corpus assumes.

**The finding.** Seven experiments, **N = 2,895**:

> *"Can review — a cornerstone of organizational accountability — encourage workers to collaborate
> with AI rather than outsource their work entirely to it? … we find that review has the **opposite
> effect**: participants who expected their work to be evaluated [were **less** likely to revise AI
> output] … than risk introducing errors through modification."*

**Telling someone their work will be reviewed makes them defer MORE to the AI.** Editing means owning
the edits; passing the AI's output through unmodified is defensible. Accountability pressure converts
into deference rather than scrutiny.

**Why it matters to this review.** Most of the corpus's solution literature assumes the opposite —
that adding a reviewer, a sign-off, or an approval gate increases the care taken with AI output. This
supplies an **empirically grounded reason the assumption can invert**, and with unusual statistical
power for a behavioural result.

**It explains three things already on record:**
- **Jessee**, *Scapegoat-as-a-service* — if the human's role is blame-absorption, the rational move is
  to change nothing, which is exactly what these experiments observe.
- **`oversight-theater`** — the arbiter's own worked example (a junior developer assigned to approve
  AI-generated PRs) now has a mechanism: the reviewer's incentive is to pass it through.
- **§85's enforcement gap** — prescribed-but-unenforced checkpoints may be worse than neutral if the
  act of assigning a reviewer *reduces* revision.

**The uncomfortable implication for the thesis.** Human oversight is the review's proposed answer to
the scaling problem, and this says the answer can be **self-defeating in the direction of its own
mechanism**: formalising accountability may buy less scrutiny, not more. That belongs in the
limitations discussion whether or not it is ever cited as evidence.

**Scope caveat.** General-AI task (social media posts), student and crowdworker participants, no code.
Do **not** present it as a finding about code review; present it as a mechanism that *would* need
testing in a code-review setting — which is a **concrete survey/experiment hook**: does formal
sign-off on AI-generated PRs reduce the rate at which reviewers modify them?

**Not exercised: §30.** This is structurally the Eze case (`9MV2IVNU`, §53) — `general-ai`, panel
demote, transferable controls — where the sole-exemplar exception was exercised. Here the arbiter
ruled demote, so the mechanism is preserved as framing rather than promoted to Core. **If a code-domain
replication appears later, revisit.**

## CANDIDATE MECHANISM — the DECISION SURFACE: what the human engages when they cannot read the artifact (2026-08-26)

**Staged, 3 instances.** Companion to the `no-inspection` staging (§81a): that records *the human does
not read the code*; this records **what they engage instead**.

**The claim.** In a growing set of designs the human's oversight object is **not an artifact but a
decision** — curated, structured, and presented for a choice. The artifact may never be shown at all.

| Paper | Tier | Decision surface | Traceable to code? |
|---|---|---|---|
| **Kasibatla**, *Decision-Oriented Programming with Aporia* (`ZH6QIU8A`) | Core · Diss Supporting | decisions explicit and structured as *"the shared medium between the programmer and the agent"*, elicited proactively | **yes** |
| **González**, *HiLDE* (`CI93QRUH`) | Context · Diss Supporting | decision points in a completion, alternatives explained, human picks | yes (within-turn) |
| **Zhou**, *Steering LLMs via scalable interactive oversight* (`XRTVITVP`) | Core · Diss Supporting | recursive tree of low-burden decisions, pre-generation | **no** — stops at the PRD |

Aporia names the problem the cluster answers: *"developers **cede decision-making authority to
agents**, often without realizing that important design decisions are being made without them."*

### The two design variables — from the arbiter's HOS experience
Neither is named by any of the three papers, and both are what separate a usable decision surface from
an unusable one:

1. **Altitude.** Escalations pitched at code level are unreadable to anyone not already deep in the
   codebase — *"anyone who was 'new' to the code (e.g. everyone) would struggle to follow."* The
   decision must be raised to the level at which a non-expert can grasp *what is at stake*, not *what
   changed*.
2. **Options with analysis.** Not "here is a problem" but "here are the choices and what each costs."
   A decision surface without alternatives is a notification; with alternatives and their consequences
   it becomes an actual locus of control.

> *Provenance note:* these come from the arbiter's own system-building experience, offered as
> comprehension of the papers. **They are a lens for reading the corpus, not evidence in it** — the
> claim that altitude and options matter needs corpus or survey support before it enters findings.

### Why it matters
If oversight increasingly happens at the decision layer rather than the artifact layer, then **the
quality of oversight is a property of interface design, not of reviewer diligence.** That relocates
the whole question: a diligent reviewer facing a bad decision surface cannot oversee well, and the
governance literature's focus on *who reviews* and *whether they signed off* misses it entirely.

**Distinguish from `oversight-explanation`.** That facet covers explaining an artifact *post hoc* so a
human can judge it. This is *ante hoc* — the choice is presented before the artifact exists. The two
co-occur in practice (Aporia carries `oversight-explanation` as primary **and** `steering`), which is
why a separate tag is staged rather than assumed.

**Promote on:** a fourth instance, or any paper that measures decision-surface quality rather than
merely proposing one. **Survey hook:** when an AI agent needs a human decision, what does the human
actually see — a diff, a summary, or a choice with alternatives?

## INDEPENDENCE THREAD — REFINEMENT: diversity and ground truth are two axes, not one (`TA6GIUK2`, 2026-08-26)

Zietsman, *The specification as quality gate: three hypotheses on AI-assisted code review* (arXiv
2026-03). Core · Dissertation Supporting. **This corrects something in our own framing.**

**What the thread has said until now.** Independence admits degrees, and we listed them as a single
gradient: same-model self-report < same-model rescaled against external labels < different-vendor
ensemble < external deterministic verifier. **That treats vendor diversity as *the* axis.**

**Zietsman splits it:**

> *"A cross-family pipeline, Grok reviewing Claude-generated code for instance, has more independence
> than a same-family pipeline. Different organisations, different training corpora, different reward
> signals. Errors are partially independent in ways that same-family models are not. **But model
> diversity does not supply ground truth. A cross-family reviewer without an external specification is
> still checking code against code, not code against intent.**"*

**Two axes, not one:**

| | Low | High |
|---|---|---|
| **Decorrelation** | same model, same session | different vendors, different training corpora |
| **Reference** | no external spec — checking the artifact against itself | executable specification, tests, formal constraints |

**You can max out one and have none of the other.** A four-vendor panel with no specification is highly
decorrelated and still has no ground truth: it produces *agreement*, which we may mistake for
*correctness*. That is a different failure from the one Yu (§91) documents, and our gradient conflated
them.

**Consequences worth carrying:**
- **Agreement is not validation.** `agent-panel` and `cross-model` mechanisms buy decorrelated error;
  they do not buy a reference. Anything reported about panel effectiveness should say which axis it
  moved.
- **It qualifies the arbiter's HOS observation** (cross-model panel review of specs and architecture
  proved useful) without contradicting it: diversity helped, *and* the specification was present as the
  reference. Both were doing work.
- **It links the two clusters.** The specification-side papers (Töpfer, Zhou `XRTVITVP`, this) supply
  the *reference* axis; the panel papers (Mahmud, Swidey, Zhu) supply the *decorrelation* axis. They are
  complementary answers, not competing ones.

**Supporting evidence, weak but pointed** — Experiment 2, planted domain-convention bugs, neutral
docstrings: **BDD caught 5/5; AI review ranged 0%–100%**, collapsing exactly where domain knowledge was
not inferable from the code (`interpolate_rate` 0%). And a self-caught confound that is itself a
finding: *"the original docstrings stated the domain convention explicitly… **A docstring that encodes
the convention is a specification.**"* Much informal evidence that "AI review works fine" may be
**spec-assisted without anyone noticing**.

**Caveat to carry:** single author, preprint, five functions per experiment, planted bugs, and the
author's own framing — *"directional evidence, not a controlled demonstration."* **Cite for the
distinction, not for the numbers.**

**Also worth noting for §91:** Zietsman constructs the same argument chain we assembled — AI reviewing
AI is circular, therefore an external reference is required — **independently**. That partly answers
the concern that the chain is our own synthesis.

## INDEPENDENCE THREAD — a SECOND AXIS: independent of generation vs independent of intent (`P837LJWE`, 2026-08-27)

Arising from the arbiter's question on Bhatnagar: *"the oversight is really the same oversight that a
human gets — someone else reviews the code. Right?"* **Nearly — and the gap is the finding.**

Bhatnagar describes *"asynchronous collaboration between **a senior domain expert** and an LLM"* —
singular. The human lead **sets the constraints, prompts the AI, and performs the Strategic
Rollbacks.** Single-author paper; no second reviewer anywhere in it.

**Ordinary code review has two degrees of separation:** the reviewer did not write the code, and
usually did not write the ticket. **Here there is one.**

**The thread's existing gradient covers the checker's *substrate*** — same-model self-report <
rescaled against external labels < different-vendor ensemble < external deterministic verifier. **This
is the human-side axis, and it is orthogonal:**

| Configuration | Independent of **generation**? | Independent of **intent**? |
|---|---|---|
| AI writes, AI checks (`PPMTM4DG`, §91) | ✗ | ✗ |
| **AI writes, the human who specified it checks** (`P837LJWE`; and the default IDE workflow) | ✓ | **✗** |
| AI writes, a different human checks (ordinary peer review) | ✓ | ✓ |

### The implication is about the field, not this paper

**The default AI coding workflow — developer prompts, developer accepts — has LESS independence than
the peer review it displaces.** We have been treating human-reviews-AI as the baseline against which
AI-reviews-AI is degraded (§91). But human-reviews-own-prompted-output is *itself* a degraded form of
peer review, because **the same person owns the request and the acceptance**.

**This compounds with `E689ZAXC` (§95):** expecting review makes workers *less* likely to revise AI
output, because editing means owning the change. **If they already own the request, that pressure is
stronger, not weaker.** Two independent mechanisms pointing the same way.

**Why it matters for the survey.** An organisation can truthfully answer *"yes, a human reviews all
AI-generated code"* while having **less** separation than its pre-AI process had — and nobody involved
would experience that as a reduction in oversight. It is invisible from inside.

**Survey hook (banked as #13):** *Is the person who reviews AI-generated output the same person who
prompted it? If so, what else in the loop is independent?*

**Also preserved from `P837LJWE` — a failure mode we do not otherwise have.** Strategic Rollbacks
caught *"AI-generated configurations that, **while syntactically correct, failed to adhere to** [the
enterprise's security guardrails]"*, and the paper names the general propensity: *"syntactically
plausible but **architecturally flawed** code."* That is Zhao's tests-pass/security-fails gap (§93)
**one level up** — syntax passes, **compliance and architecture** fail — and what caught it was human
architectural judgement, not any automated check. Cite for the failure mode, not for the effect sizes.

## THE INVERSION IS BIMODAL — two studies, one population, opposite tails (`JQPPKSFQ` + `NZJST99D`, 2026-08-27)

**The most consequential pairing in the corpus so far**, because it changes the question the
dissertation should be asking.

| | Paper | Tail studied | Outcome |
|---|---|---|---|
| `JQPPKSFQ` | Branco et al., *LGTM!* | **auto-merged** agentic PRs | **fail-OPEN** — review skipped, code ships |
| `NZJST99D` | Ehsani et al., *Where Do AI Coding Agents Fail?* | **not-merged** agentic PRs | **fail-CLOSED** — PRs abandoned, throughput collapses |

**Same population (AIDev, ~33k agent-authored PRs), opposite halves of the distribution.** §52's
definition already cited `NZJST99D` as the fail-closed exemplar; Branco supplies the fail-open half.

**And Branco reports the distribution is bimodal, with a discriminator:**

> *"agentic PR acceptance is **bimodally distributed**, typically either fully accepted or rejected.
> Auto-merged agentic PRs are notably smaller and more focused, and **less common in more mature,
> well-governed projects**."*

Repositories *"tend to either auto-merge all or none"* — and **governance maturity predicts which.**

### Why this reframes the research question

The review has been implicitly asking *"does the oversight inversion happen?"* — and the tagging pass
kept answering *"not in this paper"* (four consecutive §88 rejections). **The bimodality explains why
both answers kept appearing: the inversion is real, and it is not universal.** It is a property of
**ungoverned repositories**, not of agentic coding as such.

> **The right question is not *whether* the inversion happens but *in which organisations*, and what
> distinguishes them.** That is an empirical question about org characteristics — precisely what a
> survey can answer and a code audit cannot.

**Two further findings worth carrying:**
- **Maintainers auto-merge agentic PRs *more* often than human-authored ones** — AI code receiving
  *less* scrutiny than human code, stated as a measured differential rather than an inference.
- **They show caution toward PRs that delete existing code.** A risk signal operating in the wild:
  deletion triggers scrutiny where addition does not. Not a contributed mechanism (§107e), but a
  revealed heuristic, and a good survey probe.

**Survey implications.** Ask for the *shape*, not the average: **is auto-merge all-or-nothing in your
org, or conditional?** If bimodality holds outside OSS, the interesting variable is what moves a team
from one mode to the other — and Branco's answer, governance maturity, is testable.

**Caveat.** Both papers are OSS repository mining. Whether the bimodality survives in commercial
settings — where maintainers are employees and cannot simply abandon a PR — is **untested**, and the
asymmetry noted at §86 (OSS maintainers can refuse; employed reviewers often cannot) suggests it may
not transfer cleanly.

## MECHANISM — ENGAGEMENT DECAY: oversight quality falls as the session proceeds (`5BAZZWHG`, 2026-08-27)

**The fifth distinct mechanism by which oversight fails, and the only one that is temporal and
intra-session.** Core + Dissertation Primary.

> **EVIDENCE GRADE — hypothesis, not established.** `5BAZZWHG` is a **formative study with four
> participants**, one code-generation task each, engagement measured by **self-report** plus think-aloud.
> That is a *suggestive probe*, not a demonstration. **The theoretical weight is carried by
> `ING3D89M` (Parasuraman & Manzey) and the wider vigilance-decrement literature; Catalan is the
> software-engineering instance pointing the same way.** Do not cite the N=4 study for the mechanism —
> cite it for *domain* relevance and cite Parasuraman for the effect. **Promote on replication at scale.**

**The finding.** A formative study of software engineers working with an agentic coding assistant:

> *"**cognitive engagement consistently declines as tasks progress**, and current ACA designs provide
> limited affordances for reflection, verification, and meaning-making."*

Arbiter's reading: *"people start strong with oversight, and then their mind numbs and quality / depth
of the oversight lags."*

### Where it sits among the mechanisms

| Mechanism | What fails | Kind |
|---|---|---|
| **Inversion** (§107, Branco) | review is skipped | structural — volume |
| **Substitution** (Xu §83) | senior building capacity is spent | structural — cost |
| **Intake restriction** (Yang §86) | work is refused rather than triaged | structural — policy |
| **Reviewability decay** (Wang §80) | the artifact cannot be reviewed | structural — representation |
| **Engagement decay** (Catalan) | **the reviewer's attention declines while reviewing** | **temporal — intra-session** |

**The consequence the others do not have:** *oversight quality is not a constant per reviewer — it is a
decreasing function of time-on-task.* Every organisational control we have seen assumes a reviewer is
either present or absent. **None accounts for a reviewer who is present and progressively less
effective.**

### It has a theoretical anchor already in the corpus
`ING3D89M` — **Parasuraman & Manzey**, *Complacency and bias in human use of automation* (Context,
`dissertation-input`). Catalan is the **software-engineering empirical instance** of that classical
vigilance-decrement result. **Theory and domain evidence from independent literatures**, neither
written to support the other — the same argument shape the independence thread relies on.

### Two links worth carrying
- **To the decision-surface cluster (§96e).** Aporia / HiLDE / Zhou ask *what the human should engage
  with*; Catalan asks *whether they engage at all*. **A well-designed decision surface presented to a
  disengaged reviewer is still unread** — which means decision-surface quality and engagement are
  independent failure points, and fixing one does not fix the other.
- **To accountability deference (§95, Zhou & Zhao).** Two mechanisms, same outcome: the reviewer does
  not meaningfully revise. One because attention decays, one because ownership discourages editing.
  **They would compound.**

### The dissertation opening
The paper names **cognitive-forcing mechanisms** as the design response and operationalises none — and
the arbiter independently arrived at the same question (System 1 vs System 2 triggers, alternate checks
and balances, effective escalation). **That is an identified-but-unfilled opening**, not a gap needing
to be argued into existence.

### The arbiter's causal chain — stated as a hypothesis, only the first link demonstrated

> **engagement decays → attention lapses → defects pass unreviewed → the inversion**

Arbiter: *"it is a consequence of humans tuning out in later cycles, as described in the paper."*
**Plausible, and worth testing — but Catalan demonstrates only the first link.** Nothing in the study
is merged, shipped or gated; there is no review step in the design, so no defect can escape one.
`oversight-scaling-inversion` was therefore declined (§108c): tagging the last link would import the
conclusion from the mechanism, and **"could lead to leakage" would fire the tag on every
automation-bias paper**, which is the discriminating-power collapse §87 exists to prevent.

**The chain is testable, and that is its value.** It predicts review quality should degrade measurably
*across a session* — a prediction no corpus paper has tested and an organisation could.

**Survey hooks:**
- *Does review quality differ between the first and last change reviewed in a session?* — most orgs
  will not know, and **not knowing is itself the finding**.
- *Is there anything in your process that deliberately interrupts a reviewer's flow to force
  re-engagement — batch size limits, mandatory breaks, forced justification?*

## MISALLOCATION, NOT OVERLOAD — the norm inversion (`59KP8GTP`, 2026-08-27)

A **sixth** mechanism, and the first where reviewers are **present, responsive, and pointed the wrong
way**.

**The finding.** Gao et al. expand the AIDev dataset with contributor code-ownership data and a
human-authored baseline:

> *"In contrast to human-created PRs where **non-owner developers receive the most feedback**,
> AI-co-authored PRs from non-owners receive the **least**, with approximately **80% merged without any
> explicit review**."*

Plus: **67.5%** of AI-co-authored PRs come from contributors with **no prior code ownership**, and
**86.9%** of repositories have **no AI-agent guidelines at all**.

### Why this is not the capacity inversion

| | Reviewers | Failure |
|---|---|---|
| **Capacity inversion** (Branco §107) | overwhelmed, absent | volume exceeds review capacity |
| **Misallocation** (Gao) | **present and responding** | attention aimed **away** from the higher-risk population |

Branco's repositories skip review because they cannot keep up. Gao's reviewers **are** reviewing — they
are simply giving least scrutiny to newcomers using AI, which is **the reversal of a long-standing OSS
norm**. Onboarding scrutiny for unfamiliar contributors is one of the few oversight practices open
source reliably does well, and AI co-authorship appears to switch it off.

**Why it might happen** (untested, and worth stating as hypotheses rather than conclusions):
- **Attribution laundering** — an AI co-author reads as a competence signal, so the human contributor is
  treated as vouched-for.
- **Diffusion of responsibility** — nobody owns a review of code nobody wrote.
- **Surface plausibility** — AI-generated PRs *look* more polished (cf. Wang's *"approve based on
  vibes"*, §80), and polish substitutes for provenance.

### Why it matters more than the headline number

The 80% figure is a capacity story anyone would predict. **The inversion is not predictable and runs
against the field's own norms** — which makes it the more interesting finding, and one an organisation
would never detect from inside, because every individual review decision looks locally reasonable.

**Connects to:** §106's second independence axis — a newcomer's AI-co-authored PR has *neither*
independence (the AI generated it, the newcomer prompted it, and no owner reviews it). This is the
weakest configuration in the corpus, and it is the **most common** one at 67.5%.

**Survey hooks:**
- *Do contributions involving AI receive more, less, or the same review as comparable contributions
  without it? How would you know?*
- *Does your onboarding scrutiny for unfamiliar contributors change when the contribution is
  AI-assisted?*

## PRESCRIPTION vs VIOLATION — the literature says more scrutiny, practice gives less (2026-08-27)

**The dissertation-grade pairing from the Accept band**, assembled from two independent datasets whose
authors were not writing in response to one another.

| | Claim | Evidence |
|---|---|---|
| **Prescription** — `REZGA5WF` (He et al.) | AI-generated code *"requir[es] **extra scrutiny** during review"* | DiD + matched controls + panel GMM: complexity **+41%**, warnings **+30%**, persistent; a *"comprehension tax… regardless of functional correctness"* |
| **Violation** — `59KP8GTP` (Gao et al.) | AI-co-authored PRs from non-owners receive **the least** feedback; **~80%** merged without explicit review | AIDev mining with a human-authored baseline |

**The literature prescribes more scrutiny for AI code on measured grounds; practice supplies less, also
measured.** Neither paper cites the other. That is the same argument shape the independence thread
relies on — **prescription and observed deviation from independent sources** — and it is stronger than
either finding alone.

**Why it matters:** it converts "organisations should review AI code more carefully" from an assertion
into a **documented gap between recommendation and behaviour**, which is precisely what an
organisational survey is positioned to explain.

### Framing consequence — the productivity defence does not hold
He's temporal result defuses the standard counter-argument to investing in oversight. *"Accept the
quality cost as the price of speed"* assumes the speed persists. It does not:

> **3–5× velocity gain in month one; gains dissipate after two months. Warnings +30% and complexity
> +41% persist — and drive the long-term slowdown.**

**The gain is transient and the cost is permanent**, so the trade being invoked is not the trade on
offer.

### SELF-THROTTLING — a gate upstream of generation (staged)
> *"tools might implement **self-throttling: automatically reducing suggestion volume or aggressiveness
> when project-level complexity or debt exceeds healthy thresholds**, forcing developers to consolidate
> before generating more code."*

**Every other gate in the corpus sits between generation and merge. This one sits before generation.**
It is a proposal, not a built mechanism, and appears in a discussion section — but it is a distinct
answer to gate 1: *do not route the artifact for review; prevent the artifact from existing while debt
is high.*

**Connects to** the intake-restriction finding (Yang §86) — communities refuse work rather than triage
it. Self-throttling is the same move applied to the tool rather than the contributor. **Watch for a
second instance;** if the pattern holds, "restrict production" is a third gate-1 posture alongside
triage and exclusion.

## SHIFT-LEFT PAST THE SDLC — the gate-placement spectrum, extended upstream (`YA7XNWYE`, 2026-08-28)

Arbiter, on Ji's accountability argument: *"This is **shift left** — if the model makers do a better job,
there will be less left for individuals to pick up and better security overall. Same as detecting and
fixing problems earlier in SDLC."*

**That completes a spectrum the corpus has been building piecemeal.** Every mechanism we have catalogued
places a gate somewhere; ordering them by *how early* reveals a dimension no single paper names:

| Position | Mechanism | Corpus |
|---|---|---|
| **Before the model exists** | curate training data; evaluate models on security benchmarks, not only functional ones | **`YA7XNWYE`** (Ji) |
| **Before the artifact exists** | self-throttling — reduce suggestion volume when project debt is high | `REZGA5WF` (He, §117) |
| **Before the work arrives** | intake restriction — bans, disclosure, evidence gates, queue caps | `XJAXB98T` (Yang, §86) |
| **Before the artifact is specified** | decision elicitation; formal constraints authored up front | Aporia, `XRTVITVP`, `72W6R4JG` |
| **Between generation and merge** | review, filters, gates — where nearly everything sits | most of the corpus |
| **After merge** | debt measurement, refactoring sprints triggered by metrics | `REZGA5WF` |

**The insight the ordering produces:** the field's attention is concentrated almost entirely at
*between generation and merge* — the position where oversight is **most expensive and least
leveraged**, because every artifact must be handled individually by a human whose attention is the
scarce resource. **The upstream positions are structurally cheaper** (one intervention affects all
downstream output) and are occupied by **one paper each**.

**Why that matters for the dissertation.** If the scaling problem is that per-artifact human review does
not scale, then **the answer may not be better review — it may be fewer artifacts needing it.** Ji makes
this argument at the model layer, He at the tool layer, Yang at the contribution layer. **None of the
three cites the others; none names the pattern.** Naming it is available to the review.

**Caution.** Shift-left is a *reallocation* of accountability, not an elimination of it. Ji is explicit
that responsibility should move toward *"organizations best positioned to reduce systemic risk at
scale"* — which for an org survey raises: **does your organisation treat AI code security as something
it can influence upstream (tooling, model choice, procurement) or only downstream (review)?** Most will
answer downstream, and that answer is the finding.

## GAP TO FILL — one technology, two settings (recorded 2026-08-28)

**The dissertation will need to establish that the same underlying technology powers both assistive and
agentic scenarios.** Our own mode-pair rulings treat them as distinct *settings* (§81, §108b, §117e),
and the tie-rule exists precisely because the boundary is contested — but the *technology* is one thing
in two configurations, and the argument depends on that.

**No corpus paper currently supports the claim.** `R2QMVNXI` (Chang, §109) comes closest — its Figure 2
presents a practitioner-recognised **spectrum** of AI-based coding from assistive through agentic — but
it is Context, an MLR of YouTube discourse, and not strong enough to carry the point alone.

**Options:** find a source (a technical survey of code-assistant architectures would serve), or **argue
it as the review's own position** and mark it as such. **Flagged now so it is not discovered late.**

## Conformance review vs defect review — a distinction the corpus conflates (`A5WDGC7J`, 2026-08-28)

Raised by the arbiter on Jin, whose framing is that the paper applies code review **against the
V-model** — checking the implementation against the *specification* rather than scanning for bugs or
poor structure. That separates two activities the corpus has been treating as one:

| | Question | Needs a referent? | How it fails |
|---|---|---|---|
| **Defect review** | *Is this code bad?* | no — judge the artifact alone | **omission** — misses what it did not look for |
| **Conformance review** | *Did it build what was asked?* | **yes** — a spec to check against | **overcorrection** — rejects conformant work, invents faults |

**Why the distinction earns a place in the findings.** Most oversight mechanisms in the corpus are
defect review — linters, scanners, security gates, quality checks. But the failure practitioners
describe with agentic coding is usually **conformance**: the agent produced clean, well-structured,
passing code that *is not what was asked for*. A gate made entirely of defect review cannot see that
failure, because the artifact is not defective.

**The evidence chain this completes.** Three corpus papers now make a single argument about LLM
reviewers that none makes alone:

1. **Yu (`PPMTM4DG`)** — a model cannot reliably catch its own defects (**false negatives**). Implied
   fix: give the reviewer an independent referent.
2. **Zietsman (`TA6GIUK2`)** — review without an external referent is **circular**. Reinforces the fix.
3. **Jin (`A5WDGC7J`)** — supplying the referent produces a **different failure**, not no failure:
   systematic **overcorrection**, FPR up to **88.74%**.

**So "give the reviewer the spec" is necessary and not sufficient.** The escape route the first two
papers point at is closed by the third. This is the strongest form of the review's scaling argument
available so far, because it does not rest on models being weak — it rests on the **review task itself
being two-sided**, where fixing one error direction moves cost into the other.

**Open question for the dissertation:** overcorrection is the *expensive* failure for scalable
oversight. A reviewer that misses defects degrades quality silently; a reviewer that rejects
conformant work **consumes the scarce resource oversight is trying to conserve** — human attention —
and trains the human toward dismissal, which is `automation-bias` arriving from the opposite
direction than usual (§118). Whether that dismissal reflex is observed empirically anywhere in the
corpus is **not yet checked**; flagged for the closeout sweep.

## The tagging procedure as a worked instance of its own subject (2026-08-28)

Recorded because the arbiter raised it as a findings-relevant observation, and bounded because it is
self-observation. Full statement in `Theme_Tagging_Calibration.md` §11.6b.

**The observation:** the tag taxonomy (44 slugs frozen / 50 live, seven checklist questions per paper)
exceeds what the arbiter can hold in working memory, so tagging is **mediated** rather than direct —
*"human suggests, machine helps validate. Machine suggests more,"* with the arbiter adjudicating. This
held for **every** supervised paper, including those where the arbiter named tags first.

**Why it is interesting:** it is the review's own subject running at n=1 — `hitl-workflow` over
`ai-review`, adopted not for speed but because **recall over a large vocabulary is the specific thing
human attention fails at**, which is the same premise the corpus's oversight tooling runs on.

**Guardrail (§11.8).** This is a **worked illustration, not evidence.** Its home is the methods chapter
as procedure and limitation, plus at most a paragraph in the discussion. It does **not** enter the
findings, is **not** citable as a result about oversight in general, and the assistant is **not** an
independent rater — its checks are correlated with the arbiter's by construction.

## Certified registries — vetting the SUPPLY rather than the output (`VCI88UZD` + `6ZC3H7AF`, 2026-08-28)

Surfaced by the arbiter while ruling Liu, *Agent Skills in the Wild*: *"There was a paper a while back
about having a list of trusted repository / packages. That concept could apply to Liu as well.
Trusted skills."*

**The pairing:**
- **Enyedi (`VCI88UZD`)** — *Human-certified module repositories for the AI age.* The mechanism:
  a curated registry whose contents carry a **human certification**, so consumers inherit vetting they
  did not perform.
- **Liu (`6ZC3H7AF`)** — *Agent Skills in the Wild.* The empirical case for needing one: **26.1% of
  31,132 marketplace skills contain at least one vulnerability**, and skills bundling executable
  scripts are **2.12× more likely** to be vulnerable (OR=2.12, p<0.001). The paper's own conclusion
  calls for *"capability-based permission systems and mandatory security vetting."*

**Why this is a distinct oversight shape, and worth naming.** Everything else in the corpus oversees
**what the AI produces**. This oversees **what the AI consumes** — the skills, modules and packages an
agent pulls in at run time. Certification moves the human review **once, upstream, to the artifact**,
and every downstream use inherits it. That is a genuinely different scaling economics from reviewing
each output: pay once per package rather than once per generation.

**The catch, and why it is not a free win.** It relocates the bottleneck rather than removing it —
someone must certify 42,447 skills, and Liu's own detector runs at 86.7% precision / 82.5% recall, so
an automated gate over that volume admits a meaningful error rate. The unresolved question is
**who certifies, at what cadence, and what happens when a certified artifact is later found
vulnerable** — a revocation problem the corpus does not address anywhere.

**Status:** neither paper is at core for this (Liu demoted 2026-08-28 — the object is human-authored
third-party packages, not AI-generated code; supply-chain security of agent *inputs*). The arbiter
explicitly ruled **no dissertation role**. Recorded because the *shape* — upstream certification as an
alternative to per-output review — is a real point on the oversight design space and may return if
the scope ever widens to agent tooling.

## Quality scaling vs THROUGHPUT scaling — two things "scalable oversight" is being used to mean (2026-08-28)

Forced by the arbiter's devil's-advocate question on McAleese (`NRVQT89E`, CriticGPT): *"Wouldn't this
say that scaling human oversight isn't possible since you still need a human (in partnership with AI)
to look at everything?"*

The question exposes a **term collision** that has to be resolved before the corpus is synthesised:

| | meaning | the question it answers |
|---|---|---|
| **Quality scaling** | more **accurate** oversight per human-hour | *how good is the review a human gives?* |
| **Throughput scaling** | more **code overseen** per human-hour | *how much can get reviewed at all?* |

**This review's premise is the second.** In the arbiter's words: *"the human doesn't have to look at
everything. We can figure out what AI can review on its own and what really needs human eyes."*
Allocation, not augmentation.

**OpenAI's "scalable oversight" is the first**, and the papers say so plainly: *"The ultimate goal of
scalable oversight is to **help humans evaluate model output in order to train** [better models]"* ·
*"methods that can **help humans to correctly evaluate** model output."* Their human never leaves any
sample — **cannot** leave, because in an RLHF labelling regime the human's judgment *is* the product.

**The diagnostic that settles which a paper supports:** does it measure **time or volume**, or only
**accuracy**? McAleese reports contractors taking *"fifty minutes per example"* and **never claims the
critic makes them faster** — only more correct. A method that is better-but-not-faster does not scale
throughput at all, however much it improves quality.

**Consequences for reading the corpus:**
- **Do not cite quality-scaling results as throughput evidence.** McAleese, Kang and Zhou all
  demonstrate the first; none demonstrates the second.
- **The genuinely throughput-relevant finding in McAleese is different from its headline:** critics
  found *"hundreds of errors in ChatGPT training data rated as **flawless**"* — recovering coverage that
  human review at volume had **already lost**. That is about what humans miss when they cannot look
  properly, which is the allocation problem.
- **Routing evidence is what the review is actually short of.** Papers keep supplying configuration
  performance (which arrangement reviews best) and almost never supply allocation rules (which items
  need which arrangement). Karakaya recommends triage but does not build it (§122d); McAleese has a
  deployment-time precision/recall knob but never evaluates routing on it.

## The idealised reviewer — why human-arm baselines are optimistic (`NRVQT89E`, 2026-08-28)

Arbiter, on McAleese's human contractors: *"the human in this paper is likely less distracted and will
do a better job. Reality is an ugly thing."*

The human arm is **a best-case human** — a contractor paid to spend *"fifty minutes per example"*, no
release pressure, no competing work, reviewing as the task rather than around it. That biases the two
headline findings in **opposite** directions, and both directions matter:

- **"AI catches more bugs than human contractors" gets STRONGER.** The model beat an *idealised*
  reviewer, not a distracted one. Against a real maintainer the margin should widen.
- **"Human+AI is best" gets WEAKER.** The human contribution to the team was measured from an
  attentive partner. A real maintainer under Karakaya's *"release pressure, ownership boundaries, or
  timing"* (§122a) contributes less, so the team advantage over AI-alone is an **upper bound**.

**General rule for the corpus:** whenever a study's human arm is a *paid, unhurried, single-tasked*
reviewer, its human-alone baseline is optimistic and its human-in-the-loop benefit is an upper bound.
Catalan's engagement decay is the mechanism that erodes it in practice. Worth checking against every
paper reporting a human-vs-AI or human+AI comparison.

## The authoring-side limit — why swapping in an agent reviewer does not close the loop (`74GE3TF7`, 2026-08-28)

Raised by the arbiter as a prediction, then found in the paper as its own limitation: *"Even if agents
are doing the reviewing, we could end up in the same sad state of abandoned PRs because the coder agent
couldn't deal with the feedback."*

> *"a pattern of '**silent abandonment**': small PRs that look safe (no CI touches) but **stall because
> the agent cannot handle subjective feedback**. This implies that while we can catch the 'explosive'
> failures, the '**silent' failures require behavioral monitoring**."*

**Why this is a distinct failure and not a variant of the others.** Almost every oversight mechanism in
the corpus watches the **artifact** — scanners, tests, review bots, complexity gates. This failure is
invisible to all of them, because **the artifact is fine**. The defect is in the agent's capacity to
**iterate under feedback**: it produces something plausible, receives a subjective critique, and
cannot converge. Minh's own structural router — AUC 0.958 on cost prediction — **misses these as false
negatives**.

**The consequence for delegation.** Automating the *reviewer* side does not help, because the
bottleneck is on the *authoring* side. An agent reviewer would issue the same subjective feedback the
coder agent already cannot absorb — faster, and at greater volume. Feedback throughput rises;
convergence does not. **This is a limit on full delegation that no amount of better reviewing fixes**,
and it pairs with §126's finding that the human+AI team beats AI alone on precision.

**What it implies is needed:** signals about the *interaction*, not the artifact — Minh calls it
*"behavioral monitoring"*, and proposes *"semantic risk models to catch subtle logic bugs that
structural gates miss"* plus *"cryptographic identity to enable **reputation tracking**."* Per-agent
reputation as a routing input appears nowhere else in the corpus.

**Open question for the dissertation:** the corpus measures agents as *producers* (quality, security,
debt) and as *reviewers* (Yu, Jin, McAleese). It does not measure them as **negotiators** — the ability
to take critique and converge. If oversight is a loop rather than a gate, that capacity is the one that
determines whether delegation terminates.
