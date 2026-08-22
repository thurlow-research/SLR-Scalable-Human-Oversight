# HOS-Seeded Theme Candidates (staging — graft before classifying cores)

**Canonical citation:** Thurlow, S. (2026). HumanOversightSystem (Version 0.5.0) [Computer software]. Purdue University. https://doi.org/10.5281/zenodo.21347272
**Status:** staging / not yet grafted. Source: synthesis of ~76 HOS research findings
(`~/Code/HumanOversightSystem/Human/research/`) against the SLR themes, 2026-07-13.
**Do not treat as finalized themes.** Graft the corpus-grounded ones into
`Emerging_Themes.md` / `Problem_Statement_Evidence.md` / `slr-conventions` *before* the
core-article classification pass.

## Guardrail — how HOS may and may not inform the SLR

HOS is the **learning vehicle, not an SLR data source**. Two kinds of HOS findings, neither
is direct SLR evidence:
1. **Pass-through corpus reading-notes** — HOS's notes on *corpus papers* (Mitropoulos 2026
   framing attack; Ferdous 2026 confidence/refactor-risk; Charoenwet/AgenticSCR 2026
   corroboration-ranking; Parris/AIRA 2026 scanner-masking; Kumar/SWE-PRBench single-reviewer
   recall; Watanabe 2026 agentic-PR size; Loker/CodeRabbit 2025 the "1.7×" claim). These point
   to *papers* — ground themes on those, don't double-count as HOS corroboration.
2. **HOS-original experience** — HOS's own design lessons. These are **theme hypotheses to
   validate against the corpus**, never self-validating (avoid the reflexivity trap).

**Action before grafting:** cross-check the pass-through papers against the library (some are
likely already cores/contexts; missing ones are retrieval/snowball candidates), so each grafted
theme stands on corpus evidence.

## A. Sharpeners for T0 — the oversight-scaling inversion (graft into Problem_Statement_Evidence)

- ⭐ **"The gap is enforcement, not knowledge."** A governance audit found ~21 fail-opens,
  nearly every one violating a principle already *written down*. Reframes the insufficiency
  layer: orgs don't lack oversight *policy* — the policy is **documented but not mechanically
  enforced**. Upgrades the problem statement from "do orgs oversee AI code?" to "**is their
  oversight enforced or merely advisory?**" (HOS: `unenforceable-rules-need-verification-mechanisms`.)
- **Task-class, not touched-content, is the agentic risk axis.** Refactor/chore break most yet
  read as "maintenance" and get lightest review → a concrete mechanism for *why* the riskiest AI
  output is least inspected. (Pass-through: Ferdous 2026, Watanabe 2026.)
- **Citation-hygiene caveat for the T0 anchor:** the "AI code ~1.7× buggier" premise traces to
  ONE source (Loker/CodeRabbit 2025, 470 PRs, AI-*co-authored* ≠ autonomous). Cite the chain
  precisely or the premise is attackable.
- **Unit of analysis:** AI-code quality is a *session* property, not a single-PR one — errors
  interlock across steps ("house of cards"). (HOS-original: `working-state-invariant`.)

## B. New theme candidate — T3: "The overseer is itself an untrusted, attackable component"

*Thesis:* AI reviewers/scanners are not a trusted oracle — they emit confident false signal, can
be socially engineered, and can suppress true signal — so the oversight layer needs its own
verification before its output drives action. This is the **strengths/limits-of-current-oversight**
limb of the RQ, and it cross-links T1 (a framing attack *is* a supply-chain attack on the
oversight layer).
- Confident non-reproducing reports (3/4). (HOS-original: `reviewer-agents-file-confident-non-reproducing-reports`.)
- 100% success flipping reviewer verdicts via PR-prose framing. (Corpus: Mitropoulos 2026.)
- LLM synthesis layer masks a real scanner FAIL as "this is fine." (Corpus: Parris/AIRA 2026.)
- Guard that records-but-doesn't-halt executes the refused action. (HOS: `a-guard-that-doesnt-halt-is-not-a-guard`.)
**Graft plan:** anchor on the *corpus* papers (Mitropoulos/Parris/…); check they're in the library first.

## C. Core-criteria refinement (graft into slr-conventions §criteria)

- **Gate on a computed/independent signal, never the model's self-report.** Model confidence is
  saturated (99.9% at 8–10) and flat vs defect rate; a reviewer's own "approve" can't override its
  own findings list. **Bounds the SNR-driving-attention discriminator:** the routing signal must be
  independent of the producer. This is exactly why `VTDG995V` (calibration → *computed*
  review-intensity) is core, but "route review by the model's own confidence" is disqualified.
  (HOS/corpus: `agent-confidence-is-uninformative…`, `gate-on-computed-signal-not-self-reported-verdict`,
  `self-classification-cannot-gate-the-human-boundary`, Ferdous 2026.)

## D. Corroborations of existing themes (fold as supporting points)

- **T1 (tooling supply chain)** extends from *installed* tooling to *invoked* tooling: oversight
  instruments that shell out to vendor CLIs **fail open** (removed flag, changed output, auth lapse
  → "ran, found nothing"); CI is a generous superset so absence-failures are invisible until field
  install ("green can mean the gate never ran"). (`tooling-drift-in-validation-pipelines`,
  `ci-is-blind-to-consumer-environment-failures`, `oversight-gate-must-declare-its-deps-and-fail-loud`.)
- **T2 (explanation)**: near-verbatim support — an escalation drives action only with three layers
  (descriptive/contextual/actionable) and project-calibrated thresholds
  (`structured-fault-explanation-drives-developer-action`, corpus Adejumo & Johnson 2025); review
  *volume* is itself a failure mode → rank by corroboration strength, not LLM plausibility
  (`corroboration-ranked-review…`); and for *review*, more context degrades detection
  (`more-context-makes-llm-review-worse-not-better`).

## E. Backlog — strong lenses, HOS-design-heavy, validate against corpus before promoting

- **Decorrelated / cross-vendor ensemble review** as load-bearing coverage (single-reviewer recall
  15–31%). (`cross-vendor-review-finds-real-bugs`, `gates-and-review-are-complementary`,
  `oversight-blindspot-documentation-discoverability` — the "N-dimension overseer is blind to
  dimension N+1 and to its own blindness" point is distinctive.)
- **Tiered, cost-aware review economics — "deployability = correctness"**: oversight that is correct
  but uneconomical or unforced *gets turned off*; gate expensive review by transition significance
  (inner-loop/pre-PR/release) with a cheap deterministic trigger. (`three-tier-review-cost-model`,
  `cost-gating-autonomous-oversight-loops`.)
- **Governance invariants** (governance/policy limb): only automation-tightens / human-relaxes
  (`ratchet-principle`); an override with no expiry becomes the policy (`an-override-must-expire…`);
  the recorder must not be in the recorded set; the oversight-*disabling* valve must be more
  auditable than the gates; forge-proof human gate needs identity-separation + server-side
  enforcement (`human-gate-enforcement-limits`); two-key enable.
- **Silent non-execution = clean result**: bypassed/skipped/never-invoked oversight is
  indistinguishable from "reviewed and clean" → force unskippable execution + loud, distinct N/A
  (`orchestrator-absorbs-roles-pipeline-bypassed-by-default`, `explicit-na-audit-entries`). *(Closely
  related to the T0 "enforcement not knowledge" reframe.)*
- **Non-deterministic reviewer convergence** ("pass = zero-NEW, feed it its own issue tracker,
  allow an accept disposition").
- **Interactive vs autonomous = one role, two modes** (governance boundary, not code boundary);
  specify the post-action handoff or the agent bypasses the review loop.
- **(Corpus-seeded, 2026-07-18; ARBITER-VALIDATED same day) Oversight-competence gap — escalation
  without a competent receiver.** The Escalate stage presupposes a human *capable* of judging what's
  escalated; the democratization endgame (non-programmers generating code) removes that
  presupposition. Distinct from `automation-bias` (attention/trust failure of a *capable* human),
  `oversight-theater` (hollow authority), and the scaling inversion (volume vs. inspection): here the
  gap is **capability absence**. **Anchor: `22JBEZNK`** — and the distinction is now
  author-corroborated: the study *controls for* over-reliance (primed distrust, prompts, incentives)
  and its Discussion explicitly rejects overconfidence ("difficulty is rooted in applying domain
  expertise or critical thinking to unfamiliar technical contexts"). All four calibration models
  conflated the two failure modes (unanimous automation-bias primary — Taxonomy_Changelog §16); the
  human separated them. Tripwire: the `non-developer` facet — promote to a theme iff flagged papers
  accumulate *making this argument*; otherwise it's a Discussion point. Don't name it
  "democratization" (phenomenon-name; would keyword-attract adoption papers that belong in
  `survey-input`).
- **(Corpus-seeded, 2026-07-18) Authority-allocation spectrum — "human in absolute control."** A
  recurring *stance*, not yet a tag: not human-in-the-loop of an AI-driven flow but AI-as-tool inside
  a human-commanded flow; the spectrum runs absolute control → bounded delegation → tiered autonomy →
  autonomous+gates. Corpus cluster: Lumen `VG6CIDQW` (developer agency), `JVWUYDME` (Human-in-Command),
  `Z8TPRNEU` (devs deliberately retain control), `ID7IN65K` (authority scoping), Hedwig `T72TU8B5`
  (earned-trust tiers). HOS kin: interactive-vs-autonomous above; ratchet-principle. Likely a
  Discussion *axis* reconstructed from `hitl-workflow` + `oversight-theater` + the `assistive`/`agentic`
  facets rather than a new tag — decide after the sweep.
- **(Corpus-seeded, 2026-07-20) Risk-quantification instrument family.** If the sweep surfaces a
  *cluster* of `metrics` papers whose measurand is prospective risk (vs compliance status, quality,
  coverage) and the Discussion needs them as a roster the tags can't reconstruct, promote a
  dedicated tag then — with the evidence in hand. **Tripwire: `metrics` facet + rationale-measurand
  = risk accumulating.** Until then the family is retrievable as `metrics` + rationale text; the
  object is carried by co-tagged themes (Taxonomy_Changelog §20 — same staging logic as the
  competence gap: tripwire first, tag only on recurrence). Seeds: `R4WJZBSF` (regulatory/ethical
  risk indices, Set B), `ZUM76CCG` (LRF autonomy×impact risk levels, Set C).
- **(Corpus-seeded, 2026-07-20) `expert-validated` form facet — PROMOTED 2026-07-21 (changelog
  §28): first genuine contribution-validation instance found (UW2R6BBJ, Set B — arbiter reached
  for the facet while tagging). Definition below moved into the instrument verbatim.** Original
  staging record: Definition ready-made
  (Taxonomy_Changelog §24): contribution **evaluated by documented expert judgment** (panel /
  Delphi / structured practitioner review, process described as method). **Discriminator: the
  panel judges the *contribution*, not produces the *data*** — experts shaping requirements or
  filtering lit-review findings (input-side, the 6DXZGHD9-era probe) don't count; experts as study
  subjects don't count; ≠ peer review; ≠ undocumented collegial feedback. Would slot between
  `design-only` and `built-system` on the evidence-strength ladder (unvalidated design <
  expert-validated design < built prototype < adopted). **Tripwire: papers where a documented
  panel validates the contribution itself accumulate** — the motivating instance dissolved on
  closer read (its panel was input-side), so the facet waits for a genuine first instance.
- **(Corpus-seeded, 2026-07-20; renamed 2026-08-22) `evaluated-benchmark` form facet — STAGED.**
  (Renamed from `benchmark-evaluated` purely for tag-menu sort adjacency with `evaluated-synthetic`
  — no definitional change; all prior Zotero tags updated to the new slug, see rename note below.)
  Own system evaluated **under a standardized third-party benchmark's prescribed conditions**
  (UB2EVUFU on ProjDevBench = first genuine instance) — an evidence-strength rung *within*
  `built-system`: self-tests < standardized benchmark < field study < adopted. Deliberately NOT a
  `method-*` value (that would reverse the world-or-tool cut — the results still describe the
  tool). **Tripwire: built-system papers with standardized-benchmark evaluations accumulate** such
  that the Discussion wants the roster ("N of M systems have benchmark-grade evidence") — likely
  fast, given agentic-systems papers' benchmark habits; promote then. ≠ the paper *being* a
  benchmark study of third-party systems (that's `method-experiment`, subjects-may-be-systems
  rule). **Second instance (2026-08-21): Y4TIF9KW** (Code Prism) — benchmarks detection coverage
  against DVNA (Damn Vulnerable Node Application), a standardized third-party vulnerable-app
  benchmark, with findings mapped to OWASP Top Ten; caught during the Full Read pass after the
  sweep panel's automated scan had initially flagged it as an `evaluated-synthetic` candidate
  (mixed-signal Bucket B) — full-text check distinguished "own self-constructed workload" from
  "standardized third-party benchmark."
  **Boundary sharpened (2026-08-22), worked example ZBF86IJM** (uncertainty-highlighting study):
  its coding tasks were *sourced from* a well-known platform (LeetCode, "easy" tier), but that
  alone does not confer `evaluated-benchmark` — the authors hand-picked 15 candidates, generated
  their own Codex completions, piloted with 3 participants, and pruned to a final 3 by their own
  criteria (10-minute completion time, diversity of error types). **"Standardized" means
  administering a recognized third-party benchmark's own fixed protocol** — its established task
  set *and* its established scoring methodology, as DVNA/ProjDevBench are — not "sourced from a
  platform that happens to have difficulty tiers." Curating raw material from a well-known pool is
  authored curation, not benchmark administration. (ZBF86IJM doesn't land on this ladder at all in
  the end — see the `evaluated-synthetic` entry below for why.)
- **(Corpus-seeded, 2026-08-20; renamed 2026-08-22) `evaluated-synthetic` form facet — STAGED.**
  (Renamed from `synthetic-evaluated`, same sort-adjacency rationale as above.) Own system
  evaluated against **self-constructed, non-standardized scenarios/workloads** (constructed
  tasks, mock data) rather than a standardized third-party benchmark or a real deployment — an
  evidence-strength rung *within* `built-system`, below `evaluated-benchmark`: self-tests <
  `evaluated-synthetic` < `evaluated-benchmark` < field study < adopted. Motivating instance:
  **HBR7QZ2C** (policy engine for agentic AI) — Section 10 evaluation runs the authors' own system
  over three self-constructed workloads (document automation / financial analysis / knowledge
  assistant, 200–300 tasks each), outcomes scored by human reviewers post-hoc; no real users, no
  field deployment, no standardized benchmark. Machine panel had proposed `method-experiment` here
  — wrong per the world-or-tool test (results describe the tool, not the world); human read caught
  it on full-text check. Deliberately NOT a `method-*` value, same reasoning as
  `evaluated-benchmark`. Deliberately NOT named with "mock" — that word is already reserved
  (`design-only`'s "mock demo ≠ built": fabricated *outputs*, keeps a paper OFF `built-system`
  entirely). `evaluated-synthetic` presumes the system really runs and produces real (unfabricated)
  outputs — only the *workload* is constructed, not the mechanism's results. **Tripwire already
  fired at staging time:** a scan of the sweep panel's votes found `built-system` +
  `method-experiment` co-proposed by at least one model on **21 of 128 sweep papers** (7 in
  01-Accept, 13 in 02-Light-Review, 1 in the Full Read bucket) — 38% of the sweep's 55
  built-system papers. Zero such co-occurrence survived in the 20 human-verified calibration gold
  papers, consistent with this being a real, recurring machine-only confusion that resolves
  correctly only on a full-text check. Candidate list for spot-checking as the arbiter works the
  workbook: 7SH86C2W, 7UB2MD8Z, 96XE669R, A5WDGC7J, A6ZE2A26, C88VGWMI, CI93QRUH, I6FZ5GD2,
  JCTP8VXP, MFSZPSPU, NRVQT89E, T3XTXIXW, U9VZQXGI, VZ27QUPQ, WBS9U5N7, X7EN6DXZ, XK3P9C96,
  XRTVITVP, Y4TIF9KW, ZBF86IJM, ZH6QIU8A. Not yet grafted into the live
  `Tag_Prompt.md`/`Tag_Cheatsheet.md` v2.13 instrument (frozen for gauge constancy); available now
  as a `cal:human:facet:` override on individual items ahead of a formal graft decision.
  **7SH86C2W resolved (2026-08-22):** full-read check — single self-selected, non-repeated
  scenario (one web-app project, one journal of observations), explicitly self-labeled
  "exploratory"/"preliminary" — falls below `evaluated-synthetic` on the ladder, at the plain
  `self-tests` (untagged) rung. Considered and rejected a separate `ad-hoc-evaluated` tier between
  `self-tests` and `evaluated-synthetic` (bare-smoke-test vs. real-if-single-case empirical
  exercise): no worked example yet exists of a *weaker* case than 7SH86C2W's real data-collection
  effort, so there is nothing to split against, and it wouldn't change any synthesis claim either
  way (proposed-vs-adopted maturity story doesn't distinguish the two). Ladder stays 4 rungs;
  revisit only if a genuinely weaker (bare existence-proof, no data collected) instance turns up.
  **Tag-rename note (2026-08-22):** all live Zotero tags updated
  `cal:human:facet:benchmark-evaluated` → `cal:human:facet:evaluated-benchmark` and
  `cal:human:facet:synthetic-evaluated` → `cal:human:facet:evaluated-synthetic` (12 items,
  `slr-tools/rename_eval_facets.py`); `slr_human_tags_actions.yml` menu entries renamed to match.
  **Ladder-vs-`method-*` exclusivity rule, sharpened (2026-08-22)** after a pressure-test against
  ZBF86IJM (uncertainty-highlighting study, LeetCode-derived tasks, 30 real programmers). The
  earlier phrasing "no real users, no field deployment, no standardized benchmark" was a
  description of the HBR7QZ2C worked example, not a general criterion, and reads as arbitrary
  without the reasoning: **the rung a paper's evaluation lands on is governed by the instrument's
  own pre-existing world-or-tool test** (§ method family) — *"results describing the world (real
  users, real deployment, real behavior) → method facet; results describing only the tool
  (self-run tests over constructed corpora) → built-system evaluation."* That is a **fork, not two
  independently-composable properties**: a given evaluation event lands on the tool side
  (`self-tests`/`evaluated-synthetic`/`evaluated-benchmark`) **or** the world side
  (`method-experiment`/`method-field-study` as a method facet) — never both for the *same*
  evaluation. Plainly: **`evaluated-synthetic` = the authors invented their own test data and test
  cases and measured their own system's performance against that self-made material** — no real
  subject performs the task in that evaluation event. The instant a real subject performs the task
  and their behavior/outcomes are what's measured, that evaluation event is `method-experiment` (a
  defined task set + a manipulated condition, investigating a specific question) or
  `method-field-study` (real work, natural setting, closer to "and what did you think?") instead —
  **not additionally `evaluated-synthetic`,** even though the task material itself was authored/
  curated (curating stimuli is inherent to running *any* controlled experiment, so treating that as
  sufficient for `evaluated-synthetic` would make it fire on nearly every `method-experiment` paper
  and erase its discriminating power — the same failure mode already rejected once this session for
  the `risks` facet). **Worked contrast: ZBF86IJM stays `method-experiment` only** — real
  programmers used the Edit Model live, so results describe the world, not the tool; it does
  **not** also get `evaluated-synthetic` despite the LeetCode-derived tasks being author-curated.
  **A single paper can still land on both sides**, just via *separate* evaluation events, not the
  same one twice — see NRVQT89E: the critic model runs alone and a contractor grades its output
  after the fact (tool side → `method-field-study` rung, real production-sourced material) **and**
  the contractors' own tampering/rating task is a real controlled human-subjects exercise (world
  side → `method-experiment` facet) — two distinct measurements in one paper, not one measurement
  double-tagged.
  **`method-field-study` vs. `adopted` boundary sharpened (2026-08-22), worked example
  NRVQT89E** (LLM Critics Help Catch LLM Bugs / CriticGPT): evaluated on real ChatGPT production
  RLHF data (real user interactions, real production contractor-labeling infrastructure) — not a
  benchmark, not self-constructed/synthetic. The one-line discriminator: **validated *with*
  production data → `method-field-study`; used/operating *in* production → `adopted`.**
  NRVQT89E's critic model was evaluated offline against real production-sourced data and never
  itself deployed to real ChatGPT users, so it lands at `method-field-study` (one rung below
  `adopted`), not `adopted` itself. Same discriminator the `adopted` pilot rule already draws
  (study-site pilot vs. the org's own operational use) — this just names the production-data-source
  case explicitly, since "production" language in a paper (baseline model, labeling pipeline) can
  otherwise read as if the paper's own system were deployed when it wasn't.

- **(Corpus-seeded, 2026-08-22) `agent-panel` + `cross-model` facets — STAGED.** Two new
  orthogonal, composable structural facets, motivated by a naming ambiguity in `theme:ai-review`'s
  own text ("single-reviewer, multi-agent panels, and independent/cross-model review" conflates
  *structure* — is more than one agent involved — with *function* — is checking/judging actually
  happening). `theme:ai-review` itself is **unchanged**: it fires whenever an AI judges/checks a
  produced artifact, regardless of whether that's one agent, a same-model panel, or a cross-vendor
  panel underneath. The two new facets separate out the structural questions:
  - **`agent-panel`** — multiple distinct agents are involved in the workflow, in *any* capacity
    (generation, review, or both). A PM-agent/Architect-agent/Tech-Design-agent panel
    collaboratively producing a design gets this facet but NOT `theme:ai-review` (no judging of a
    produced artifact — generation/steering territory). A three-agent review committee gets both.
  - **`cross-model`** — of those agents, they are different underlying vendors/models, not
    multiple instances of one — a modifier *on* `agent-panel` (panel composition), not on
    `ai-review` (so it never presupposes review is happening).
  Corpus check before staging (2026-08-22, grep for named model vendors — not exhaustive, some
  entries may be baseline-comparison mentions rather than the paper's own cooperating architecture,
  full-text confirm still needed): of the strongest `ai-review`-tagged multi-agent candidates,
  **10 of 13 checked show genuine cross-vendor composition** (A6ZE2A26 — claude/codellama/
  deepseek/gemini/gpt/llama/mistral; GAD5Z8PV — claude/gpt; UB2EVUFU — claude/deepseek/gpt/llama;
  Y4TIF9KW — claude/gemini/gpt; 5RKMGRNA — gemini/gpt; 7V7SRG43 — gpt/llama; S7FPFUT8 —
  gemini/gpt/llama/palm; U9VZQXGI — claude/deepseek/gemini/gpt; XK3P9C96 — claude/gpt; V4IRKSFI —
  deepseek/gpt/llama), **1 is clearly same-vendor** (HBR7QZ2C — gpt only, multiple personas/roles
  — the `agent-panel`-without-`cross-model` worked example), 2 inconclusive (F9JM9CI6, CTGGMIX9 —
  single incidental vendor mention, likely a baseline citation rather than the paper's own
  architecture). Preliminary read: cross-vendor composition is the dominant, not the exceptional,
  pattern among this corpus's multi-agent review solutions — a genuinely citable prevalence claim
  for the dissertation once the inconclusive/baseline-vs-architecture distinction is confirmed by a
  full read, not left as a grep artifact.
  **Naming decision trail (2026-08-22):** considered "adversarial-review" (broad) — rejected as
  conflating structure+function, same problem as `ai-review`'s own text. Considered
  "cross-examination" — checked against the corpus directly: appears exactly once, in *Measuring
  Progress on Scalable Oversight for LLMs*, meaning a **human** cross-examining a **single** AI
  (not agent-checks-agent) — adopting it would import a term the corpus already uses for a
  different concept, so rejected. "Adversarial" on its own *is* corpus-native (recurs in UB2EVUFU,
  U9VZQXGI, HBR7QZ2C for close to this exact broad concept) but was dropped in favor of splitting
  structure (`agent-panel`) from function (`ai-review`, unchanged) rather than one compound name.
  "Cross-model" is corpus-native (A6ZE2A26, 2 occurrences, describing multi-vendor composition
  directly) and was kept. **HOS guardrail note:** HOS's own decorrelation design (Claude=author,
  Codex=adversary, Gemini=correctness/architecture, Copilot=CI baseline) motivated *asking* this
  question but is explicitly not corpus evidence for it (per the guardrail above) — the corpus
  check above, not HOS, is what grounds staging this. Not yet in the live v2.13 instrument; apply
  by hand as `cal:human:facet:agent-panel` / `cal:human:facet:cross-model` ahead of a formal graft
  decision.

## Grafting checklist (do before classifying cores)
1. Cross-check pass-through corpus papers (Mitropoulos, Ferdous, Charoenwet, Parris, Kumar,
   Watanabe, Loker) against the library → in-corpus? retrieval/snowball candidates?
2. Ground **T3 (untrusted overseer)** on those corpus papers → add to `Emerging_Themes.md`.
3. Fold **A** (enforcement-not-knowledge, task-class-risk, 1.7× caveat) into `Problem_Statement_Evidence.md`.
4. Add **C** (computed-signal-not-self-report) to `slr-conventions` core criteria.
5. Decide which **E** backlog lenses have corpus support → promote or drop.
