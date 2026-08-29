# Taxonomy iteration log — v0 → current

How the theme-tagging taxonomy evolved through cross-model + human calibration. Each entry:
**disparity observed → diagnosis → change → outcome.** Companion to `Tag_Cheatsheet_v0.md` (the
starting point) and `Tag_Cheatsheet.md` / `Methodology/Emerging_Themes.md` (current).

Method: a 5-tagger panel (Claude **opus**, Claude **fable 5**, **codex** = gpt-5.6-sol, **gemini** =
Gemini 3.1 Pro, **gemini-fast** = Gemini 3.5 Flash) plus a **human**, each tagging the same papers'
full text against the taxonomy. Disagreements were treated as *signals about the instrument*, not noise.

---

## 1. Breadth divergence & "model consensus ≠ human"
- **Disparity (Set A, v0):** themes-per-paper ranged **opus 4.7 · codex 5.0 · fable 2.6 · gemini 2.7**.
  Primary theme was stable (9/10 unanimous), but *secondary* breadth split widely: ~half of all
  secondary tags were asserted by a single model. Only **Opus** reached the "limits-of-oversight"
  themes (`automation-bias`, `oversight-theater`, `tooling-supply-chain`).
- **Key finding:** adding **Fable** (a Claude model) showed it clustered with **Gemini** (Jaccard 0.86),
  *not* with Opus (0.49) — so tagging breadth is a **model disposition, not a vendor/family trait**.
  A naïve model-majority vote would have *dropped* exactly the subtle themes only Opus caught —
  reproducing the project's earlier screening finding that **model consensus ≠ human; Opus ≈ human.**
- **Change:** reinforced *membership-not-mention*; later boundary-sharpening (below) trimmed the long tail.
- **Outcome:** on the refined re-run, breadth converged (**opus 4.7 → 2.5**; all models ~2.3–2.5 except
  codex 4.2), and the "Opus outlier" pattern largely dissolved.

## 2. "Is formal methods really rules-based?"
- **Disparity:** `formal-methods` was lumped inside `rules-based-checks`, conflating *proof-based*
  guarantees with *heuristic* checks — and mislabeling who performs them (AI vs classical engine).
- **Change:** added a **composable `formal-methods` tag**, orthogonal to the *performer* (`ai-review`
  if an LLM does it, `rules-based-checks` if a classical engine does). The composition **encodes an
  adoption hypothesis**: classical+human-authored formal methods = niche; AI-automated (autoformalization)
  = the plausible uptake path.
- **Outcome:** corpus check — only ~4/149 cores foreground formal methods (one a position paper),
  confirming a minor, aspirational thread; the tag now segments it cleanly.

## 3. `framework` vs `governance-frameworks` collision + fuzzy `framework`
- **Disparity:** a human tagged `governance-frameworks` intending "it's a framework" — the two shared
  the word "framework." Separately, the `framework` facet split across taggers (VG6CIDQW 1/4; Hedwig
  human-vs-4-models).
- **Change:** renamed the theme **`governance-frameworks` → `org-governance`** (the org *apparatus* —
  policy, audit logging, accountability); sharpened the **`framework` facet** = a *pipeline-integratable
  technical framework/architecture*, **breadth not required**, excluding bare *point-results*.
- **Outcome:** the two stopped competing (form vs. topic); the VibeGuard/Hedwig consistency case
  clarified that a single-concern architecture still qualifies.

## 4. `remediation-gating` over-tagging
- **Disparity:** a human **and Opus** both tagged VibeGuard (`T8E8SCCG`) `remediation-gating` — but it's
  a *pre-publish gate with no auto-fix*.
- **Change:** sharpened the boundary — **requires an autonomous fix being overseen**; a pure
  detection/publish/quality gate is the enforcement side of the *detector*, not remediation.
- **Outcome:** both the human and Opus dropped it on re-read.

## 5. `risk-routing` ↔ `hitl-workflow` — the persistent primary split
- **Disparity:** the *only* recurring primary disagreements were on this adjacency (Hedwig `T72TU8B5`
  and `UB2EVUFU`), split ~2/3 across models.
- **Diagnosis:** not noise — a **definitional gap**. Both themes co-occur in systems that both *decide
  what to surface* and *provide the control point*.
- **Change:** sharpened the definitions to a mnemonic — **`risk-routing` = WHAT** (what gets surfaced,
  at what tier) vs **`hitl-workflow` = HOW + WHEN** (the human's control mechanism + checkpoint timing) —
  and added a **primary tie-breaker**: primary = the theme carrying the paper's *distinctive novelty*,
  not the standard scaffolding.
- **Outcome (measured):** re-running the four models on Hedwig collapsed the split from **2/3 → 5/5
  unanimous `risk-routing`** (both Opus and Fable *moved*, citing the tie-breaker verbatim), matching
  the human. A clean demonstration that a definitional fix can be *empirically verified* by re-run.

## 6. Scope: general-AI papers slipping into core
- **Disparity:** `M74M3RFJ` (assurance cases for *LLM adversarial robustness* + EU AI Act) was tagged
  `regulatory-compliance` by **all four models** — theme-level in-scope-looking — but its governance
  *object is the model*, not the produced code. The human scoped it out.
- **Change:** added a **`general-ai` scope flag** (governance is general-AI, not coding-specific) and a
  **`demote:context` workflow flag** for batch re-scoping.
- **Outcome:** `M74M3RFJ` demoted **core → context** (core count 149 → 148). Disposition is a human
  judgment the models are weak at — the flag is the tripwire.

## 7. Encoding-scheme consistency
- Made theme membership explicit (`theme:<slug>`) and standardized **primary = `primary:theme:<slug>`**
  (same tail as membership, `primary:` prepended) so calibration tags strip-map to the final convention.
- Menu labels prefixed `theme:` / `facet:` so theme-vs-facet is unmistakable in the tagging UI (which
  had caused the §3 mix-up).

## 8. Facet expansion (artifact / evidence axis)
- Added the composable **`framework` → `built-system` → `adopted`** cluster (form → maturity) to power a
  **proposed-vs-adopted** analysis, plus **`general-ai`**. In the refined Set A: `built-system` reached
  **10/10 all-model agreement**, `adopted` correctly **0/10** (nothing production-deployed) — high-signal,
  objective facets.

## 9. The PROMPT changed too — not only the definitions ⚠️
The full model prompt = **cheat-sheet (definitions) + `# YOUR TASK` block**. Both evolved. The task
block's key change was the **primary tie-breaker instruction**:
- **v0:** *"…choose **ONE primary theme**, and add any facet tags."*
- **current:** *"…choose **ONE primary theme (tie-breaker: the theme carrying the paper's DISTINCTIVE
  CONTRIBUTION/novelty, not standard scaffolding)**, and add any facet tags."*
  (also added: mentions of the `framework`/`built-system`/`adopted` facets and `formal-methods` composition.)

**Confound for the causal claim (§5).** The Hedwig **2/3 → 5/5** convergence combined *two* changes at
once: (a) the sharpened `risk-routing`/`hitl-workflow` **definitions** and (b) the new **tie-breaker
instruction** in the prompt. Because (b) directly instructs the primary choice, it is plausibly the
dominant driver. Accurate framing: *"the refined prompt (definitions + explicit tie-breaker) collapsed
the split"* — **not** "the definitions alone did it." A clean **isolation test** (defs-only vs
tie-breaker-only, factorial on one paper) would separate the two effects.
- v0 prompt preserved verbatim in `Tag_Prompt_v0.md`; current in `Tag_Prompt.md`.

## 10. Generation-mode axis missing (`assistive` vs `agentic`)
- **Gap (2026-07-18):** the corpus mixes two oversight settings — human-initiated,
  suggestion-granularity generation (Copilot-style: oversight = the acceptance moment) vs AI-initiated
  multi-step work at artifact/PR granularity (oversight = the gate) — and no tag separated them. The
  automation-bias evidence lives mostly in the first; the scaling inversion and the
  Detect→Triage→Fix→Escalate solution pipeline mostly presuppose the second. Not recoverable from
  existing tags (`agent-scope-drift` only catches it where drift is the topic).
- **Change:** added the **`assistive` / `agentic` scope-facet pair**, cut on *who initiates + the
  reviewable unit* — explicitly NOT "IDE vs not" (agents live in IDEs). Either / both / neither
  (= unspecified or mode-irrelevant). Additive (no theme redefined), so added **mid-Set-B** under the
  `formal-methods` precedent; Set A model outputs unaffected; calibration papers to be backfilled.
  At the same time the Set B human packet's embedded cheat-sheet was found **stale (v0-vintage:
  `governance-frameworks`, no `formal-methods`, 4 facets)** and refreshed to the current instrument —
  the Zotero Actions menu was already current, and the one paper tagged so far (TF56EPIP) used
  current slugs, so no human tags were affected.
- **Outcome:** pending — pilot on the 20 calibration papers in the post-Set-B iteration. Expected
  high agreement: near-factual property of the study, like `built-system` (10/10 in Set A).

## 11. The Lumen episode — unanimous-model category error; `oversight-explanation` broadened
- **Disparity (2026-07-18):** on Lumen (`VG6CIDQW`, Set A — "developer agency through transparent
  context control"), **all four models chose primary `hitl-workflow` unanimously, and the human
  overturned it.** First unanimity overturn in the calibration — it qualifies the "primary theme is
  essentially solved" finding: unanimity survived a boundary the oversight-vs-steering discriminator
  already covers.
- **Diagnosis:** (a) "context control" pattern-matched to *control surface*, but a lever over the
  AI's **inputs** is **input-side steering**, not oversight of an artifact — none of the four applied
  the steering exclusion there. (b) The human also rejected `provenance-auditability`: a point-in-time
  "what's in use now" view records nothing, so nothing is auditable after the fact. (c) The paper's
  real oversight contribution — human-invoked comprehension — had no sanctioned home:
  `oversight-explanation` was handoff-framed, and the lens-ish "context transparency" clause sat
  inside the otherwise lever-themed `hitl-workflow`.
- **Change:** `oversight-explanation` **broadened to "helping the human understand what the AI is
  doing"** with two manifestations — **push** (system escalates; decision-ready handoff:
  background + options + recommendation + risks) and **pull** (human-invoked visibility into what the
  AI is doing/using). "Context transparency" relocated out of `hitl-workflow` (now levers-only, with
  an explicit lens→`oversight-explanation` boundary); `provenance-auditability` gains the
  record-vs-live-view test; the **input-side steering cue** and a **transparency routing rule** added
  to the preamble and cheat-sheet. Human tags on Lumen: `oversight-explanation` (primary) +
  `assistive` + `built-system` — the day-old `assistive` facet did real work (it explains why no
  handoff exists for the old definition to bite on).
- **Process change:** the **freeze is lifted**. Scott human-tags the calibration papers as a
  *vocabulary-vetting pass*; the summative human-vs-model experiment then runs on the vetted
  instrument (models re-run Sets A+B in fresh contexts; Set A human tags are model-informed, Set B is
  the clean blind comparison). v1-instrument model outputs archived to `data/tags-v1/`.
- **Outcome:** pending the re-run — the decisive check is whether the broadened definition + steering
  cue flips the models' Lumen primary to `oversight-explanation`.

## 12. `steering` + `non-developer` facets (vetting pass, papers 2–3)
- **Gaps (2026-07-18):** (a) steering existed only as an *exclusion* — nothing marked a paper's
  steering component, so exclusion decisions left no audit trail and hybrid steer-and-check systems
  would read as under-tagged in the sweep; `assistive` cannot carry this (mode of the *setting* ≠
  type of the *contribution*). (b) Reading `22JBEZNK`: "non-programmers generating code" — the
  democratization endgame of vibe coding — had no population marker, though it up-ends the Escalate
  stage (escalation presupposes a competent receiver).
- **Change:** two facets. **`steering`** (contribution-type flag; contribution-not-topic guardrail;
  steering-*only* → demote candidate — makes the `spec-driven-guardrails` resolution enforceable,
  parallel to `general-ai`). **`non-developer`** (population scope flag; default = professional
  devs), completing the scope axes: mode (`assistive`/`agentic`) · object (`general-ai`) ·
  population (`non-developer`). The *argument* (oversight-competence gap) is staged in
  `HOS_Seeded_Theme_Candidates.md`, NOT made a theme (n=1; `non-developer` is its tripwire —
  promote if flagged papers accumulate making the argument). Facets 10 → 12; menu 28 → 30 actions.
- **Resolved (same day):** after weighing the ground-of-the-act test (quality knob = steering vs
  trust/risk input-gating = supply-chain-kin vs incidental control), Scott confirmed **controlling
  the input is steering, and it's a big part of Lumen** — Lumen is now the facet's worked example;
  the §11 "input-side steering" diagnosis stands unchanged. The ground-of-the-act test itself is the
  reusable rule: input *curation for output quality* = steering; input *vetting on trust/provenance
  grounds* = `tooling-supply-chain` territory.
- **Outcome:** pending the sweep (facet counts + whether the competence-gap candidate promotes).

## 13. The Z8TPRNEU probe — object-of-mechanism rule; drift boundary; steering amendment
- **Disparities (2026-07-18):** on "Professional Software Developers Don't Vibe, They Control":
  (a) 3 of 4 models tagged `agent-scope-drift`; the human rejected it — the paper documents *control
  practices*, with drift only the tangential *motivation*; the Tag reference itself was citing
  Z8TPRNEU as a drift **example**, encoding the over-broad reading. (b) The human applied `steering`
  to a *descriptive* practices paper, an unanticipated use (the facet was defined on *proposed*
  solutions). (c) The human initially read `ai-review` as "AI code review" — slug connotation
  narrower than the written scope (which covers agent-checks-agent by the locked §T3-dissolution
  decision); watch whether models repeat this in the re-run before adding a clarifier.
- **Change:** the **object-of-mechanism rule** — *tag by the object of the mechanism, not the
  motivation of the actor* — added to `agent-scope-drift`'s Boundary with a worked pair: positive
  (multi-agent panel checking code scope vs spec scope → drift + `ai-review`, the object+performer
  composition grammar) and negative (Z8TPRNEU's retained control → `hitl-workflow` only; removed from
  the drift example roster, converted to counter-example). Captures tail tightened: "keep them in
  scope" → "detect or bound departure from intent" (the old wording could absorb any control
  mechanism). `steering` facet amended: "proposed solution **or documented practice** operates on
  generation."
- **Outcome:** human tags on Z8TPRNEU: primary `hitl-workflow` (matches 4/4 models) + `ai-review`
  (sides with codex alone — breadth data point) + `agentic`/`steering`/`survey-input`. Re-run check:
  do fable/gemini/codex drop `agent-scope-drift` under the counter-example?

## 14. The UB2EVUFU probe — error-condition handback; process gates; plumbing rule; coder fatigue
- **Disparities (2026-07-18):** on "Self-organizing multi-agent systems for continuous software
  development": (a) the human's primary `ai-review` resolved Set A's original v1 split **3 models +
  human vs Opus** (`hitl-workflow`) — the tie-breaker's "distinctive novelty, not scaffolding" applied
  by the arbiter. (b) The human initially tagged `risk-routing` for "agent fails → escalates to
  human," then **self-corrected**: an error-condition handback is an exception path, not a
  discretionary triage decision. (c) Three models tagged `rules-based-checks`; a full-text scan
  confirmed tests appear only as the agents' *instruments* — pattern-matched plumbing. (d) The
  human's first-pass tag set had several oversights (facets missed), corrected on a second look —
  self-diagnosed **"dinner fatigue."** With 29 tags per paper, recall-based tagging degrades with
  coder fatigue; this is a *reliability factor of the human instrument*, not just an anecdote.
- **Change:** `risk-routing` boundary — **error-condition handback is NOT routing** (mechanism →
  `hitl-workflow`; failed-fix loop → `remediation-gating`). `remediation-gating` Captures — **two
  gate kinds**: content (filter fix candidates) and **process** (bounded retries / budget-decay /
  stop-progression, fail-closed; UB2EVUFU's budget-halving cycles = worked example). Preamble +
  cheat-sheet — **"plumbing ≠ membership"** rule for systems papers (UB2EVUFU's test-running agents
  as counter-example). Workflow — **five-question facet checklist** (role · form · scope · mode ·
  contribution) so facet coverage is mechanical, not recall-dependent; packet gains the same
  checklist + a second-look verification habit.
- **Outcome:** human final set: primary `ai-review` + `hitl-workflow`/`provenance-auditability`/
  `remediation-gating` + `agentic`/`built-system`/`framework`/`steering`. Re-run checks: do models
  stop tagging `rules-based-checks` here, and does Opus's primary move to `ai-review`?

## 15. The F9JM9CI6 probe — `counterpoint` + `general-code` facets; mode-pair clarifier
- **Gaps (2026-07-18):** on "Support, not automation" (AI-supported review *prep* — agents generate
  higher-level code descriptions for the reviewer): (a) nothing captured **stance polarity** — the
  paper argues *against* review-automation maximalism, and the earmarked "contrarian hunt" had no
  operationalization; (b) nothing captured the **object-of-oversight** — the mechanism targets code
  review *generally* (the reviewed code isn't AI-authored; the AI sits on the review side only), so
  on tags alone the paper reads broader than it is; (c) the human tagged mode twice, reversing
  (`assistive` → `agentic`), because both slugs invite readings the definition doesn't support
  ("uses agents", "AI assists the human").
- **Change:** **`counterpoint`** role facet (argues against a prevailing position; direction-agnostic,
  rationale records what's opposed; Discussion-balance + confirmation-bias defense).
  **`general-code`** scope flag (object = code generally, not AI code; transfers but wasn't
  developed/evaluated on AI code), completing the wrong-object family: `general-ai` (model) ·
  `general-code` (any code) · `non-developer` (population) · `steering` (contribution). Mode-pair
  **clarifier**: the pair describes the *generation* studied — AI only on the review/oversight side
  → tag *neither*. Facet checklist updated (role +counterpoint; scope +general-code). Facets 12 → 14;
  menu 30 → 32 actions.
- **Narrowness ruling:** the paper's thin scenario (review-prep only) is **extent, deliberately not
  tagged** — carried by primary, rationale, child note, and the withheld `framework`/`built-system`;
  a narrowness scalar would have poor reliability (every paper is narrow along some axis).
- **Outcome:** F9JM9CI6 expected final set: primary `ai-review` + `oversight-explanation`/
  `risk-routing`; facets `intro-framing` + `counterpoint` + `general-code`, **no mode facet**
  (`agentic` removed). Re-run check: do models apply `general-code` instead of a mode facet here?

## 16. The 22JBEZNK overturn — capability vs bias; the second unanimous-model error
- **Disparity (2026-07-18):** all four models tagged `automation-bias` as unanimous primary on the
  paper the Tag reference itself cited as the theme's example. The human tagged no automation-bias at
  all. Full-text read vindicated the human decisively: the study **controls for over-reliance**
  (primed distrust, explicit error-hunting prompts, monetary incentives) and its Discussion
  **explicitly rejects overconfidence** — "the difficulty is rooted in applying domain expertise or
  critical thinking to unfamiliar technical contexts." The models pattern-matched "missed flaws even
  when warned" — but the warning was the experimental *control*, not the finding.
- **Change:** `automation-bias` Boundary gains the **capability discriminator** (the failing human
  must be *capable*; can't-evaluate → the oversight-competence gap); 22JBEZNK moves from example to
  boundary counter-example; the **oversight-competence-gap candidate upgrades** to arbiter-validated
  + author-corroborated, 22JBEZNK its anchor. Mode-pair gains the **tie-rule** (initiator vs
  reviewable unit disagree → the reviewable unit dominates; human-prompted complete-artifact = the
  gate = `agentic`). Human also self-corrected `risk-routing` off ("how humans respond to raised
  risks," not triage).
- **Outcome:** second unanimity overturn (after Lumen), and the more damning: the models tagged the
  mechanism the paper explicitly rules out. Re-run check: does the discriminator flip them?

## 17. Set A audit — VibeGuard recurrence, demote signature, salience bias, anchor bar
- **VibeGuard (`T8E8SCCG`) recurrence — the compression-gap proof.** The human re-applied
  `remediation-gating` to VibeGuard — the *same documented error* (§4) whose exclusion was written
  from his own earlier mistake. Root cause is mechanical, not cognitive: the exclusion lived only in
  `Emerging_Themes.md`; the compressed cheat-sheet (what the tagger actually works from) never
  carried it, and the §14 process-gate broadening made the line *more* inclusive. **Principle now
  enforced: every boundary that has ever caught a human must appear in the compressed instrument.**
  Tag removed; exclusion added to all copies.
- **The demote signature, validated twice.** `2CKL96B8` (narrative stat-assembly; primary struggle)
  and `UDVHQ5HR` (LLM-judge capability benchmark; definition-stretching to `quality-debt`) both
  flagged `demote:context` — matching the `VP7TS6CX` worked call (tool-capability benchmark →
  context) and the secondary-lit rule. **Workflow cue added:** struggle to pick a primary /
  stretching a definition = check the core bar, don't force tags. With M74M3RFJ, the calibration
  sample has produced **3 demotes / 10 papers** — the sweep should expect a substantial demote tail
  (the tagging pass doubles as a scope audit).
- **Salience bias (models).** Models anchor on a paper's most vivid section: `2CKL96B8` primary
  ai-code-insecurity from its security-stats section (secondary-lit primary = **biggest-tent** theme
  now conventioned); 4 `problem-statement-anchor` applications by impressiveness rather than bar.
- **`problem-statement-anchor` bar set:** must anchor the OVERALL problem statement — not a
  sub-argument or population-specific stat, however vivid; never on `lit-review` (secondhand — chase
  primaries). Human's zero-anchors-in-10 recorded as the considered bar. `lit-review` clarified:
  structure not required (systematic OR narrative; test = synthesized-not-produced).
- **Outcome:** Set A human pass complete — all 10 papers tagged, verified, and adjudicated; ~20
  instrument products across §10–§17 from six probe papers + this audit.

## 18. Instrument-critique panel + known-answer dry-run → v2 revision
- **Dry-run (2026-07-18):** 5 blind fresh-context Fable taggers applied the instrument to the 10
  adjudicated Set A papers: **8/10 primary match; all four regression checks passed** (Lumen flip,
  VibeGuard exclusion, 22JBEZNK not-bias with the discriminator cited verbatim, tie-rule applied by
  name). Residual fixes: flags field, steering materiality, binding biggest-tent, ai-review practice
  clause. The two primary misses: 2CKL96B8 (biggest-tent non-binding) and F9JM9CI6 (the new
  ai-review↔oversight-explanation adjacency).
- **Panel (same day):** Fable 5 + GPT-5 Codex (high) + Gemini 3.1 Pro (High), fresh contexts, frozen
  input (instrument + Tag reference + Set A dev set with human tags only; input generator committed,
  artifact gitignored). ~40 findings; verdicts converge on "one revision cycle, then sweep." Full
  merged table: `data/critique/DISPOSITION.md`. Known-answer synthesis: theme-level calls are
  *forced* by the text; facet/flag-level calls mostly only *permitted* → divergence risk lives in
  facets/flags, mirroring Set A's breadth noise.
- **Applied (v2):** all A-group schema fixes (demote trigger list corrected — `general-code` is NOT
  a demote reason; criteria unified; bare-slug primary governs; flags vocabulary enumerated incl.
  `insufficient-input`); all B-group compression-gap restorations (computed-signal rule,
  framework point-tool exclusion + adoption test, dependencies clause, Detect dual-tagging,
  formal-methods third composition, intro-framing qualifier, Hedwig tie-break exemplar); all C-group
  sharpenings (oversight-explanation gains the **standing** mode — modes illustrative, headline
  governs; documented-practice clause generalized; biggest-tent operationalized; provenance record
  must serve *human* review; thin-input floor; insecurity evidence bar; vision-paper membership
  floor; survey-input substantiveness; competence-gap keep-core note); scope flags regrouped.
- **Arbiter rulings encoded:** **D1 plan-gate rule** (designed lifecycle checkpoint = hitl-workflow;
  conversational guide-then-go = steering). **D2 who-checks-what decomposition** with the HOS release
  cycle as worked example (HOS: Thurlow, S. (2026). HumanOversightSystem (Version 0.5.0) [Computer software]. Purdue University. https://doi.org/10.5281/zenodo.21347272) (producer self-checks = no theme; independent evaluation = detector by
  epistemics; severity + cross-model agreement = risk-routing on a computed producer-independent
  signal; fix approval/escalation + refix-loop governance = remediation-gating). **D4 (arbiter final, superseding the
  proposed split): dependency risk in generated code → ai-code-insecurity**; tooling-supply-chain
  keeps the AI tooling + attacks on the reviewer.
- **D3 RESOLVED (Scott, 2026-07-18) — the Jidoka ruling.** `remediation-gating` = the system fixes
  **autonomously, without per-fix human involvement**, kept safe by machinery (content/process
  gates, convergence, fail-closed stops); `risk-routing` **layers on top** to engage the human only
  when absolutely required — the andon cord. Risky-fix escalation to a human is therefore *routing*,
  not remediation (corrects a comingling in the first-draft worked example). **Human-approves-every-
  fix is NOT remediation-gating**: review-everything is the unscalable anti-pattern the review
  exists to move past (attention collapse); a paper *advocating* it is a `counterpoint` candidate —
  and *introducing* automation-bias risk by design is a rationale-level critique, distinct from
  `automation-bias` membership (which requires *studying* the failure). **Instrument FROZEN as v2**
  → Set A retag (improvement gate) → Set B.
- **Set A retag under v2 (2026-07-18, three fresh models):** improvement across every metric —
  primary fable 6/10→8/10, codex 6→7, gemini 6→7; theme Jaccard .50–.66 → .67–.78; **facet Jaccard
  roughly doubled** (.34–.42 → .61–.70); demote flags 8–9/10 correct. Both v1 unanimity errors
  (Lumen, 22JBEZNK) now called correctly by all three. Residual misses concentrate in 3 papers:
  2CKL96B8 (all three follow the *operationalized* biggest-tent to ai-code-insecurity — **resolved:
  human re-adjudicated to ai-code-insecurity**, conceding the original ai-review primary stretched
  that theme's definition; a case of the written rule out-performing the recorded intent), F9JM9CI6 (**resolved: human re-adjudicated to
  oversight-explanation** via the new **altitude refinement** — primary = most specific theme still
  capturing the paper's main effort; guard: a component mechanism doesn't outrank the broader
  contribution, so UB2EVUFU stays ai-review), UB2EVUFU
  (codex+gemini overcorrect to primary remediation-gating after the D2/D3 text raised its salience;
  gemini violated the then-unstated primary∈themes constraint).
- **Altitude-rule regression test (2026-07-18, latest):** 3 papers × 3 fresh taggers under the
  updated instrument — **8/9**. Flip-check UB2EVUFU: **codex flipped back to ai-review** (the guard
  worked; rationale decomposes per the rule); fable held correct. Hold-checks: F9JM9CI6
  oversight-explanation 3/3, Hedwig risk-routing 3/3 (nothing destabilized). Gemini's schema
  violation is gone (primary now in themes). **Residual: gemini kept remediation-gating on UB2EVUFU
  despite the compressed copy naming that exact case verbatim** — model non-compliance, not a
  wording gap; recorded as a gemini signature (v1 conservative floor → schema violation → ignores
  named worked example). Sweep implication: gemini primaries on multi-mechanism systems papers get
  the human check the design already prescribes.
- **Round-2 smoke test (fresh Fable, v2 text only): 10 revision-introduced defects found & fixed** —
  primary∈themes schema line added; best-effort-primary-when-demoting contradiction resolved;
  task-block demote copy restored the benchmark-evaluating-a-contributed-system carve-out; stale
  tag count; steering splice regrammared; formal-methods intro-framing marked as *facet*; rationale
  coverage specified; primary triple-definition cross-referenced; demote:discard given criteria;
  remediation-gating density split (anti-pattern note → sub-bullet). Cross-references verified clean.

## 19. `design-only` facet — positive marker for proposed-not-built (the R4WJZBSF probe) → v2.2
- **Gap (2026-07-19, Set B pass, paper 10):** R4WJZBSF proposes a four-metric ethical-risk framework
  whose "production-ready Google Colab implementation" fabricates its core outputs — EG and ADS are
  literal `np.random` draws, the results table reproduces the mock's hard-coded probabilities
  (ADS 60% = `p=[0.6, 0.4]`), BPI is substring matching despite the claimed BERT semantics, and the
  Methodology's validation claims (κ=0.72, 90% precision, three institutions) have no corresponding
  artifact. The human's blind read correctly saw "proposing, not building" but **reached for
  `intro-framing` to record it** — a definition stretch (intro-framing = names the gap, NO mechanism;
  this paper operationalizes formulas/thresholds/architecture) that also contradicted his own
  `framework` tag. Classified per §7 method step 2a: uncaptured concept, recurring (the
  unbuilt-proposal shape shows up repeatedly in the corpus), and no reasonable broadening holds it —
  broadening `intro-framing` would destroy its no-mechanism boundary, and absence of `built-system`
  is ambiguous three ways (not applicable vs tagger miss vs genuinely unbuilt).
- **Change:** added **`design-only`** form facet — mechanism **specified in buildable detail but
  never credibly run** (no working implementation, no evaluation on the intended object); **a mock
  demo that fabricates the mechanism's core outputs ≠ building** (R4WJZBSF worked example); applies
  only to papers that *propose* something; mutually exclusive with `built-system`/`adopted`,
  composes with `framework`; ≠ `intro-framing` (discriminator = buildable detail). Completes the
  maturity spectrum intro-framing → design-only → built-system → adopted. Disposition tripwire
  (parallel to steering-only / `general-ai`): design-only *solution* paper → the
  unevaluated-framework context discriminator → check the core bar. **Slug chosen over `proposal`**
  (every solution paper "proposes" — slug-connotation over-fire risk, the `ai-review` lesson §13).
  Facets 14 → 15; menu 32 → 33 (re-import pending); all four instrument copies updated in this
  commit (cheat-sheet, prompt, Set B packet, Tag reference). Additive mid-Set-B under the §10
  precedent — no theme redefined; Set B papers 1–9 untouched. **Instrument = v2.2.**
- **Comparability note:** R4WJZBSF's blind first-read human tags were snapshotted (Zotero v156638)
  *before* the audit dialogue that produced this facet — the paper is Set-A-style
  "blind first read + model-aware adjudication"; Set B papers 1–8 (untagged) remain fully clean.
- **Outcome:** pending — Set A backfill piloted post-Set-B (expected sparse: VibeGuard/Hedwig/
  Lumen/UB2EVUFU all built; F9JM9CI6 stays intro-framing unless its vision meets the
  buildable-detail bar). Re-run regression pair: R4WJZBSF design-only vs the built systems; watch
  codex for over-fire (breadth signature) and check the facet behaves like the near-factual
  `built-system` (10/10 in Set A). **2026-07-20 backfill:** `M74M3RFJ` confirmed the second
  design-only (GSN assurance-case framework, exemplars only, engine = future work) — design-only
  ON, intro-framing OFF per the contradiction rule; also reconciled: restored to the 01-AI
  Calibration collection (the calibration roster is frozen experiment infrastructure, orthogonal to
  disposition) + retroactive `demote:context` (its 2026-07-15 demotion predated the flag mechanism).
  F9JM9CI6: **RULED design-only (Scott, 2026-07-20 — overriding the assistant's stays-intro-framing
  assessment; §23)** — a stated architectural-design contribution meets buildable detail even with
  realization deferred to a research agenda; intro-framing off per the contradiction rule. The
  other seven calibration papers: four built, three propose nothing — facet correctly inapplicable.

## 20. `metrics` facet + risk-routing signal boundary (R4WJZBSF follow-on) → v2.3
- **Gap (2026-07-20, Set B pass):** R4WJZBSF defines four regulatory/ethical-risk indices with
  essentially no discussion of what to do with them — no allocation decision. The human's blind
  primary was `risk-routing`: with no home for a metric-definition contribution, the
  nearest-sounding theme absorbed it — and model salience bias will replicate that stretch at sweep
  scale (many papers define scores). Brainstorm considered a composable pair — `risks` ("talks
  about risks") + `metrics` — mixing to capture essences like "risk metrics" / "oversight metrics."
  **`risks` REJECTED:** a mention-level criterion in a governance corpus (near-100% base rate, zero
  discrimination; "risk" is a worse word-collision hazard than "framework"/"transparency," which
  get routing rules, not tags). The mixing falls out for free from `metrics` × the co-tagged
  themes: +`regulatory-compliance` = compliance-risk metrics, + an oversight theme = oversight
  metrics (Scott's own worked example), +`quality-debt` = quality metrics, +`risk-routing` =
  metrics that drive allocation.
- **Change:** **`metrics`** contribution flag — defines metrics/scores/indices **as a deliverable**
  (defines-vs-uses guardrail: an evaluation apparatus earns nothing; contribution, not apparatus);
  object supplied by co-tagged themes; composes with `design-only` (defined, never run on real
  data) or problem themes (defined AND applied → findings earn the theme, facet marks the
  instrument); **rationale must name the measurand** (the residual "measures *prospective risk*"
  nuance lives there — per the F9JM9CI6 narrowness precedent, below tag altitude).
  `risk-routing` Boundary += **defining a risk metric/score without the allocation decision is NOT
  routing** → `metrics` facet; define-AND-route gets both. Staged candidate:
  **risk-quantification instrument family** (`HOS_Seeded_Theme_Candidates.md`) — promote only if
  the sweep surfaces a cluster the tags can't reconstruct; tripwire = `metrics` + rationale-measurand
  = risk accumulating. Facets 15 → 16; menu 33 → 34 (re-import pending); all copies in lockstep.
  **Instrument = v2.3.**
- **Adjudication (Scott, 2026-07-20):** R4WJZBSF's measured risks are regulatory/ethical, so
  `regulatory-compliance` correctly carries the object — expected final set: primary
  `regulatory-compliance`, facets `metrics`+`framework`+`design-only`; Scott executes the toggles
  himself; §7 log updates on verification. If `risk-routing` drops there, the blind primary becomes
  the boundary's first logged catch.
- **Outcome:** pending — Set C's first member `ZUM76CCG` (LRF: autonomy×impact → oversight levels)
  exercises this boundary from the AI-first side (it plausibly routes, not just measures — a good
  contrast case); watch whether models stretch `risk-routing` on metric-definition papers in the
  Set B run.

## 21. `risk-ip` + `risk-bias` risk-type flags — the harms axis (→ v2.4)
- **Gap (2026-07-20, R4WJZBSF follow-on):** the synthesis needs a **risk-types ×
  identified/mitigated matrix** — which harms the corpus recognizes, which have actual mechanisms;
  the gap cells (identified-but-unmitigated) are Discussion findings. The theme spine organizes
  *mechanisms*, not *harms*; four risk types have theme columns (security / quality / over-reliance /
  explainability-deficit) but **IP/plagiarism and code-bias have no home**, and rationale free-text
  can't be queried into a matrix. Arbiter reports informal recurrence of IP risk across the corpus;
  HOS ships an IP scanner (experiential corroboration — kin, not driver). The §20 measurand
  tripwire was designed to wait for recurrence; the arbiter ruled it has effectively fired for
  these two types.
- **Change:** **`risk-ip` / `risk-bias`** risk-type flags. **Substantive-treatment bar** (defines a
  metric for it · contributes/evaluates a mitigation · reports an empirical result · focal
  analysis; an intro risk-list sentence = mention, no tag); **scoped to homeless types only** —
  themed risks get no flag (saturation guard; the same reason the generic `risks` facet was
  rejected in §20). A **deliberate, bounded exception to membership-not-mention**, justified by the
  synthesis axis it serves. Extensible on the same bar (privacy = likely third); promotion path:
  contribution-level cluster → theme, definition ready-made. Facet checklist gains a sixth
  question (**risk-types**); stale "31 tags" count corrected to 35. Facets 16 → 18; menu 34 → 36
  (re-import pending); all copies in lockstep. **Instrument = v2.4.**
- **Outcome:** pending — R4WJZBSF earns both flags (PRS/BPI are *defined metrics* for the two
  types — passes the bar via its first clause). Watch model compliance with the substantive bar in
  the Set B run: intro risk-lists are salience bait (codex breadth signature especially).
  **Superseded same day by §22** — the family went uniform.

## 22. Risk-flag family made uniform; explainability routed by object (→ v2.5)
- **Disparity (2026-07-20, same-day probe of §21):** the arbiter pressed the homeless-only scoping
  from three angles and it failed the smell test each time: (a) "measures IP risk" was
  tag-queryable but "measures quality debt" was not (rationale-text only); (b) matrix columns
  carried **heterogeneous inclusion bars** (flag columns = define-level; theme columns =
  study-level) — a methods-validity objection a committee could land; (c) the human's own
  R4WJZBSF over-tags (`automation-bias`, `oversight-explanation` off its ADS/EG metric definitions)
  showed taggers *will* reach for the theme when define-level treatment has no tag home. The §21
  parsimony argument (avoid theme/flag redundancy) lost to uniformity: the real saturation guard
  was always the substantive-treatment bar, not the scoping.
- **Change:** **`risk-security` + `risk-quality` + `risk-overreliance` added** → one five-flag
  family, one bar (metric · mitigation · empirical result · focal analysis; intro-lists never
  count; rationale cites the fired clause). **Co-occurrence grammar:** flag = substantive
  engagement, theme = the lift; heavy-lift papers carry both. Matrix = one query per column, one
  bar; §21's rationale-text reconstruction retired. **Explainability three-way routing** encoded
  (human-catch: the arbiter almost mapped EG → oversight-explanation): judging-support →
  `oversight-explanation` · **code comprehensibility → quality** (quality-debt Boundary + flag) ·
  model-XAI → `general-ai`; "explainability" joins the route-by-object word list. **Measurand
  vocabulary fixed** (security · quality · comprehensibility · over-reliance · ip-plagiarism ·
  bias · compliance · privacy). **Define-only ≠ theme-membership** stated explicitly in the
  compressed copies (compression-gap principle; first catch R4WJZBSF). Facets 18 → 21; menu
  36 → 39 (re-import pending); all copies in lockstep. **Instrument = v2.5.**
- **Adjudications encoded (Scott, 2026-07-20):** R4WJZBSF flags = risk-ip + risk-bias +
  risk-quality + risk-overreliance (all four metrics define-level); themes `automation-bias` and
  `oversight-explanation` come OFF (define-only; wrong object respectively). Both then-pending
  rulings (what+how core-bar carve-out; F9JM9CI6 design-only) were **confirmed by Scott the same
  day → §23**.
- **Outcome:** pending — the Set B model run tests bar compliance on five flags (risk-security =
  codex salience bait); Set C's ZUM76CCG tests define-vs-route from the AI-first side.

## 23. Two arbiter rulings: the what+how core-bar carve-out; F9JM9CI6 = design-only (→ v2.6)
- **Ruling 1 — what+how carve-out (Scott, 2026-07-20).** A paper that **names the risk/quality
  elements to track AND defines operationalizable metrics for tracking them** (full specification:
  formulas/thresholds/tools) **clears core bar (2) as measurement, even unevaluated**. Rationale
  (as pressure-tested): instrumentation *specification* is solution characterization — the Triage
  stage's computed producer-independent signals have to come from somewhere — not mere
  applicability; "value to the survey" is explicitly NOT the rationale (survey-input papers have
  value at context tier). This **amends the 2026-07-13 trap clause** ("do the measuring or the
  gating") — defining the instrumentation now counts as doing solution-work. Back-catalogue
  checked: no prior call flips (VP7TS6CX/DPKKMXSA/UDVHQ5HR/2CKL96B8/M74M3RFJ demote reasons all
  untouched). Class consequence accepted: what+how metric papers stay core with
  `design-only`+`metrics` as markers; what-only enumerations and borrowed-metrics papers remain
  context candidates; demote stays reserved for its listed triggers. Encoded in: `slr-conventions`
  quick discriminators, `SLR_Status_Update_2026-07-08.md` §3 (dated amendment), the `design-only`
  line in all compressed copies. First application: **R4WJZBSF kept core, no demote** (the paper's
  fabricated-evaluation problem is documented by `design-only`'s mock-demo clause; quality ≠ tier).
- **Ruling 2 — F9JM9CI6 = `design-only` (Scott, 2026-07-20, overriding the assistant's
  assessment).** A **stated architectural-design contribution** (F9JM9CI6 §3: AI-OS-based review
  platform architecture) **meets the buildable-detail bar even when the authors defer realization
  to a research agenda**; `intro-framing` comes off per the contradiction rule (`counterpoint` +
  `general-code` retained; no mode facet — unchanged). F9JM9CI6 becomes the *inclusive*-side
  worked example of the design-only/intro-framing boundary (R4WJZBSF = the mock-demo side;
  genuinely mechanism-free gap-naming papers remain intro-framing). Zotero updated (design-only
  added 2026-07-20 after a concurrent-edit check — Scott had removed intro-framing; the audit of
  all 10 calibration items found no other drift). **Instrument = v2.6** (text-only; menu unchanged
  at 39).
- **Outcome:** pending the re-run — watch whether models apply design-only to F9JM9CI6-class
  visions (stated-architecture clause) without over-firing on pure position papers.

## 24. Set B papers 2 & 10 closed; three boundary clarifiers; expert-validated staged (→ v2.7)
- **Set B consultation Q&A (2026-07-20, during blind tagging)** produced three near-catch
  clarifiers, all landed in every copy: (a) **lit-review framing rule** — a framing related-work
  section ≠ the facet (the facet is the paper's role; both facet jobs misfire otherwise); (b)
  **adopted pilot rule** — study-site vs user discriminator ("outside the research context" ≠
  "outside the research org"); a multi-org case-study *evaluation* is `built-system` evidence, not
  adoption — **the arbiter applied it correctly on first contact** the same hour; (c) **risk-flag ×
  lit-review interplay** — arbiter initially leaned "secondhand never fires," then reversed on
  2CKL96B8: **focal secondhand synthesis CAN fire the flags** (it now carries
  `risk-security`+`risk-quality`); matrix segments secondhand via `lit-review`; passing enumeration
  never fires; anchor stays never-on-lit-review.
- **`expert-validated` STAGED, not landed:** the motivating instance dissolved on closer read (its
  panel reviewed lit-review findings feeding requirements — input-side, judges-the-data not
  judges-the-contribution). Definition + tripwire parked in `HOS_Seeded_Theme_Candidates.md`.
- **Hedwig `T72TU8B5` + `metrics`** (arbiter): `change_pattern_risk` + the policy score are the
  argued novelty — the defines-AND-routes class (`metrics` + `theme:risk-routing`), the worked
  example the metrics entry names.
- **6DXZGHD9 closed (Set B paper 2) — the four-reads paper.** Blind primary `ai-code-insecurity`
  (sole theme) → final primary **`org-governance`** + `ai-code-insecurity` secondary; facets
  `built-system` · `metrics` (measurand: org-level security-risk exposure / practice maturity) ·
  `risk-security` · `risk-quality` (PA-2 consistency catch) · `risk-overreliance` (PA-5) ·
  `survey-input`; `framework` facet OFF (org apparatus ≠ pipeline framework — the §3-vintage
  boundary held). The home migrated across four arbiter reads (insecurity-detection → governance
  assessment); logged as diagnostic data — if models scatter on this primary, the human's
  difficulty predicted it. Template-family caution noted (ANN-ISM applied by the same author
  network to other domains).
- **R4WJZBSF closed (Set B paper 10)** at its §20–§23 adjudicated end-state (verified v156667).
  Both Set B closures are "blind first read + model-aware adjudication" (snapshots v156638 /
  v156680 preserve the blind records); Set B papers 1, 3–8 remain fully clean.
- **Instrument = v2.7** (text-only; menu stays 39). Facets 21 + two staged candidates.

## 25. Data-collection method family — the study-characteristics axis (B644HQFS probe → v2.8)
- **Gap (2026-07-20, Set B paper 1):** tagging B644HQFS (1,000 forum posts mined and coded), the
  arbiter asked whether mining "counts as survey" — exposing two things at once: (a) the
  `survey-input` slug invites a method reading its definition doesn't have (the facet tests the
  finding's *utility to the org survey*, method-independent — a mined study can absolutely be
  survey-input); (b) nothing anywhere tracks **how a paper's evidence was produced**, though
  perception vs artifact evidence disagree routinely in this corpus (YBHHYR4P: users *believe*
  insecure code is more secure) and the methods chapter needs a study-designs table regardless.
- **Change:** four-facet **data-collection method family** — `method-self-report` (humans tell
  you) · `method-mining` (artifacts measured) · `method-experiment` (controlled manipulation) ·
  `method-field-study` (real-setting deployment/observation). Own-evidence-only (lit-reviews get
  none — methods live in the primaries; absence = no empirical evidence); multi-apply for mixed
  methods. Slug deliberately `method-self-report`, NOT `method-survey` (the collision the probe
  itself demonstrated). Deliberately four values, no more: the full empirical-SE methods taxonomy
  is a rabbit hole; these cut exactly the evidence-weight distinctions synthesis uses.
  Single-home rule: if extraction codebook_v0 gains a data-collection field, reconcile — tags are
  the home. Facets 21 → 25; menu 39 → 43 (re-import pending); checklist six → seven questions
  (stale 35-count corrected to 42). **Instrument = v2.8.**
- **Outcome:** pending — backfill piloted post-Set-B with the other new facets; watch
  multi-apply compliance and the self-report/field-study boundary (observational studies at
  companies) in the model run.

## 26. Method-facet backfill audit → two boundary rules; `benchmark-evaluated` staged (→ v2.9)
- **Backfill (2026-07-20, Scott's quick scan of the 10 calibration items + assistant cross-check
  against full texts):** 7/10 correct at first pass, including two rule-holds under pressure —
  Hedwig `self-report` only (paper states "no formal user study"; synthetic-trace eval = tool) and
  VibeGuard untagged *despite* its "controlled experiments" wording (synthetic projects,
  precision/recall = tool results — the word didn't trap the tagger). Z8TPRNEU dual = the
  reference's own worked example. Adjudicated corrections: **22JBEZNK + `method-experiment`**
  (participants shown outputs, prompted to find flaws, primed + incentivized = assigned task with
  manipulation; "case study" framing ≠ field-study — not their own real work) and **UB2EVUFU
  − `method-experiment`** (initially tagged off its ProjDevBench benchmark run; arbiter agreed on
  the whose-properties test — the scores describe TheBotCompany, not the world).
- **Rules encoded:** (a) **whose-properties triangle** — VibeGuard (own tool, synthetic) none ·
  UB2EVUFU (own tool, standardized third-party bench) none · UDVHQ5HR (third-party tools studied)
  experiment; (b) **subjects may be systems** — controlled studies of *third-party* tools/models
  whose findings characterize those systems = `method-experiment`; own-system evals never earn a
  method facet regardless of harness. **`benchmark-evaluated` STAGED** (evidence rung within
  `built-system`; UB2EVUFU = first genuine instance; deliberately not a method value — would
  reverse the world-or-tool cut). **Instrument = v2.9** (text-only; menu stays 43).
- **Outcome:** the method axis survived its first 10-paper backfill with a 70% first-pass hit rate
  by a fatigued arbiter on day one — watch whether models beat that under the encoded rules.

## 27. Two Set B rulings: source-agnostic risk flags; carve-out tool-validation exclusion (→ v2.10)
- **Source-agnostic flags (Scott, 2026-07-20, CodeAgent `7V7SRG43`):** the risk flags track the
  **harm regardless of the overseen code's source** — CodeAgent detects security/quality issues in
  general (human-authored) code, and the arbiter ruled the flags fire ("they capture the risk
  regardless of the source") with `general-code` as the matrix's transfer-segmenter (parallel to
  `lit-review` segmenting secondhand rows). `general-ai` exclusion unchanged (M74M3RFJ: object =
  the model, not code). First instance of the general-code × risk-flag interaction.
- **Carve-out exclusion (encoding the arbiter's own BAWCBT9R demote):** metrics auditing a
  measurement tool's/judge's **own reliability** = the "validates which measurement tool"
  discriminator → context; the what+how carve-out does NOT reach them. Closes the soft edge a
  model could have walked through (BAWCBT9R names bias elements + defines sensitivity metrics —
  carve-out-shaped, but the object is the evaluator, not AI-code risk). Encoded in
  slr-conventions, Status_Update §3, and the compressed design-only lines.
- **Set B papers in flight:** B644HQFS closed pending one primary altitude ruling
  (quality-debt vs oversight-scaling-inversion); 7V7SRG43 audit delta pending toggles
  (+agent-scope-drift — the §13 worked-pair miss, +general-code, −method-experiment — the
  whose-properties repeat); BAWCBT9R audit delta pending toggles (+ai-review primary/theme,
  +method-experiment, −agentic, −risk-quality). §7 rows written when each closes.
  **Instrument = v2.10** (text-only; menu stays 43).

## 28. `expert-validated` PROMOTED from staging (UW2R6BBJ, first genuine instance → v2.11)
- **Trigger (2026-07-21):** tagging `UW2R6BBJ` (Set B, clean paper — consultation at rule level
  only), the arbiter hit a documented expert-panel validation and reached for the facet — the
  staged candidate's promotion condition. The two-day staging history is itself a validation
  arc: the facet was drafted 2026-07-20, its motivating instance *dissolved* on closer read
  (input-side panel), it was parked with the judges-the-contribution/produces-the-data
  discriminator, and the first genuine instance arrived within a day. Definition moved into the
  instrument verbatim from staging. Also clarified vs the method family: a surveyed expert panel
  is `method-self-report` on the *data* axis regardless (no `method-expert-panel` — sampling
  granularity stays in rationales); the same panel can provide data AND validate → both tags
  co-hold. Facets 25 → 26; menu 43 → **44** (re-import required). **Instrument = v2.11.**
- **Outcome:** pending — UW2R6BBJ's human set records the first application; watch the
  input-side/validation boundary in the model run (6DXZGHD9's panel = the negative example).

## 29. `routing-signal` facet — positive marker for the boundary that catches humans (→ v2.12)
- **Trigger (2026-07-21, E95T8E88 QA):** the signal-without-allocation boundary caught the arbiter
  blind for the SECOND time in two days (R4WJZBSF `risk-routing` primary → regulatory-compliance;
  E95T8E88 `risk-routing` primary → oversight-scaling-inversion). Twice-caught = the instrument's
  most human-catching line; per the compression-gap philosophy it gets maximum structural support:
  a positive marker, not just an exclusion.
- **Change:** **`routing-signal`** contribution flag, on the `steering` grammar (audit trail for a
  boundary exclusion): computed, producer-independent signal **framed for review-attention
  allocation** without operationalized selection/gating. Framing test keeps generic defect
  predictors out (other-purpose signals = `metrics` only, R4WJZBSF). Mutually exclusive with
  `theme:risk-routing` by construction. Synthesis job: the Triage supply-chain roster — signal
  suppliers vs operationalized routers is a field-maturity finding. Seed: E95T8E88
  (deletion-likelihood at PR creation; "allow reviewers to prioritize their attention"; AUC 87.1;
  no threshold/tier/engagement logic). Facets 26 → 27; menu 44 → **45** (re-import required).
  **Instrument = v2.12.**
- **Outcome:** pending — sweep expectation: the defect/PR-risk-prediction literature supplies
  recurrence fast; watch that models respect the framing test and the mutual exclusion. Sweep-time
  audit note: roster example 74GE3TF7 ("predicts high-maintenance PRs for gated triage") needs the
  same signal-vs-selection scrutiny on close read.

## 30. General-AI kept-core exception — the sole-exemplar rule (UW2R6BBJ → v2.13)
- **Ruling (Scott, 2026-07-21):** UW2R6BBJ kept core despite `general-ai` object — "the only one
  so far that did a deep dive into applying the regulatory frameworks." Encoded as the
  **sole-operationalization-exemplar exception** — with the trigger scoped by the arbiter same
  day: a deep compliance/regulatory-operationalization dive means **"look at keeping," not
  "keep"** — a candidate for the exception the arbiter weighs case-by-case; UW2R6BBJ passed the
  weighing (uniquely serves the regulatory limb: frameworks → engineering controls, evaluated +
  expert-validated). Grammar precedents: the one-framing-anchor
  principle; `general-code`'s kept-core transfers. **Adjudication-layer only** — compressed copies
  unchanged; models still flag `demote:context` on general-AI objects (flag proposes, human
  disposes). M74M3RFJ's demote unaffected (unevaluated, robustness-focused, not sole). If a second
  regulatory-operationalization deep-dive appears in the sweep, the "sole" premise lapses and both
  get re-adjudicated on ordinary criteria. **Instrument = v2.13** (reference-only; menu stays 45).

## 31. Prompt-design refinements evaluated and REJECTED — instrument unchanged (2026-07-22/23)
- **Persona framing** (assignment-derived technique): one-variable experiment, gemini-3.1-pro-high
  over the calibration 20 vs the v2.13 baseline and human gold. Primaries 13/20 vs 14/20;
  Jaccards ±.03; both regressions drifted toward themes named in the persona's research-interest
  list (interest-salience bias, the predicted failure mode, now observed). **v2.13 stays
  persona-free** — a defended design choice, consistent with the corpus's own framing-cue findings
  (BAWCBT9R, X7EN6DXZ). Confound disclosed: bundled with the hedwig-free vintage's worked-example
  substitutions (UB2EVUFU's flip to remediation-gating = anchoring suspect). Artifacts:
  `data/experiments/persona-20260722/`. Full writeup: calibration doc §8.1.
- **Theme/facet prompt split** (motivated by Flash-tier size-variance): declined — the rule mass
  couples the axes (metrics↔risk-routing, routing-signal exclusion, contradiction→demote logic);
  the testable premise was tested instead: **no length effect at panel tier** (r ≈ 0.0 between TXT
  size and disagreement/dispersion/accuracy, n=20). Lessons staged, not adopted: length as sweep
  covariate; sandwich-recap = v2.14 candidate (Flash-side test first); gauge-qualification probe
  required before any cheaper tier tags the context extension. Calibration doc §8.2.
- Gauge constancy hardened the same dates: panel models pinned in the runner (sol-high /
  3.1-pro-high / opus-4.8) + per-run provenance sidecars, after session-log audit confirmed all
  v2.13 runs used these tiers. Calibration doc §8.3. **Instrument remains v2.13; menu stays 45.**

## 32. Set C pilot CLOSED — the classification-framework altitude precedent (ZUM76CCG, 2026-08-15)
Arbiter adjudication of the ZUM76CCG packet (all five questions; full record in
`data/tags-v213/setC_pilot_dispositions.json`):
- **Altitude precedent (binding for the sweep): use-case/deployment-granularity classification
  frameworks that prescribe oversight *regimes* = `org-governance`; `theme:risk-routing` requires
  artifact-granularity selection driven by a computed, producer-independent signal.** The LRF's
  autonomy×impact matrix allocates governance regimes to deployments via human design-time
  judgment — no computed signal, no artifact selection → org apparatus (ASIL-classification-kin,
  6DXZGHD9-kin). Keeps Hedwig (dynamic per-artifact classifier) cleanly on the routing side.
  Confirms the replication-stage modal (org-governance 2/1) over the noise-built single-run
  consensus; codex's stable risk-routing dissent = its known drift-as-primary signature.
- **Contradiction pair**: `intro-framing` survives; `design-only` fails buildable-detail (no
  components/formulas/thresholds; the paper itself defers metrics to future work) — the arbiter's
  test "outlines a framework concept, not a buildable system" restates the discriminator.
  `metrics` correctly never fired (define-nothing, not define-only).
- **`risk-overreliance` dropped on arbiter reflection**: a background acknowledgment paragraph in
  a challenges catalog ≠ substantive treatment — the mention-vs-focal boundary is seductive at
  paragraph length (opus called it "focal"; the human initially leaned keep). Sweep note: audit
  eyes on paragraph-length risk-flag calls.
- **Demote:context confirmed**; §30 sole-exemplar exception not invoked (risk-classification
  dive, not regulatory operationalization; UW2R6BBJ holds the slot). Arbiter rationale — "useful
  for background and risk framing" — is the context tier's definition, worked as intended.
- **Mode = both confirmed** with an interpretation note: `agentic` == autonomy (AI-initiated,
  artifact-granularity reviewable unit) per the v2.13 definition — LRF levels 0–1 map to the
  assistive acceptance-moment, levels 2–3 to the agentic gate; assistive-alone would misstate the
  paper's span.
- **Pipeline validation**: one human delta vs the post-replication proposal (added
  `theme:hitl-workflow`, codex-aligned — the autonomy dimension argues human control modes as one
  of the framework's two axes). Everything else matched the ladder's pre-filled state.
  Instrument remains v2.13. Zotero gold written (v156854; pre-write snapshot in `Backups/`);
  the one malformed primary tag (`primary-theme:`) schema-fixed in the same write.

---

### Headline for the writeup
The taxonomy improved **measurably** as a *validated instrument*: disagreements were used diagnostically,
each fix was re-tested, and the sharpest result — the `risk-routing`/`hitl-workflow` definitional
refinement — converted a persistent **2/3 model split into 5/5 unanimity aligned with the human**.
Cross-model tagging behavior is a **model disposition, not a vendor trait** (Fable≈Gemini), and **model
consensus does not substitute for human judgment** on breadth and scope.

## 33. Staged-facet rename (sort adjacency) + `agent-panel`/`cross-model` staged + `7SH86C2W` resolved (2026-08-22)

**Rename, no definitional change.** `benchmark-evaluated` → `evaluated-benchmark` and
`synthetic-evaluated` → `evaluated-synthetic`, purely so the two sort adjacently in the Zotero
tag-selector menu. All 12 affected Zotero items re-tagged (`slr-tools/rename_eval_facets.py`);
`slr_human_tags_actions.yml` menu entries renamed to match; every doc reference updated
(`HOS_Seeded_Theme_Candidates.md`, `Synthetic_Eval_Check_Guide.md`, `Emerging_Themes.md`,
`Sweep_Reading_Guide.md`, `README.md`, `Tag_Prompt.md`/`Tag_Cheatsheet.md`'s parenthetical
mention). Historical entries (§26, `SETB_Human_Packet.md`) left under the old names as a record
of what the instrument said at the time.

**`7SH86C2W` resolved** (one of the `evaluated-synthetic` candidate-list papers): a single
self-selected, non-repeated scenario (one web-app build, journaled), explicitly self-labeled
exploratory/preliminary by its own authors — falls below `evaluated-synthetic` on the
evidence-strength ladder, at the plain `self-tests` (untagged) rung. A separate `ad-hoc-evaluated`
tier (bare smoke-test vs. a real-but-single-case empirical exercise) was considered and
**rejected**: no corpus instance yet exists that is genuinely *weaker* than 7SH86C2W's real
data-collection effort, so there's nothing to split against, and the split wouldn't change any
synthesis claim (proposed-vs-adopted maturity story doesn't distinguish the two). Ladder stays
4 rungs; revisit only if a bare-existence-proof instance turns up.

**`agent-panel` + `cross-model` facets — STAGED.** Motivated by a structure/function conflation
in `theme:ai-review`'s own text ("single-reviewer, multi-agent panels, and independent/cross-model
review"). `theme:ai-review` is **unchanged** — it fires whenever an AI judges/checks a produced
artifact, regardless of what's underneath. Two new orthogonal structural facets separate the
questions `theme:ai-review` was conflating:
- **`agent-panel`** — multiple distinct agents involved, in *any* capacity (generation, review, or
  both). A PM/Architect/Tech-Design agent panel producing a design gets this but not
  `theme:ai-review` (generation, not judging). A review committee gets both.
- **`cross-model`** — of those agents, they're different vendors, not multiple instances of one —
  a modifier *on* `agent-panel`'s composition, never on `ai-review` (so it never presupposes
  review is happening).

Corpus check before staging (grep for named model vendors across the strongest `ai-review`
multi-agent candidates — not exhaustive, some may be baseline-comparison mentions rather than the
paper's own architecture, full-text confirm still pending): **10 of 13 checked show genuine
cross-vendor composition** (A6ZE2A26, GAD5Z8PV, UB2EVUFU, Y4TIF9KW, 5RKMGRNA, 7V7SRG43, S7FPFUT8,
U9VZQXGI, XK3P9C96, V4IRKSFI); **1 clearly same-vendor** (HBR7QZ2C — gpt only, multiple personas —
the `agent-panel`-without-`cross-model` worked example); 2 inconclusive (F9JM9CI6, CTGGMIX9 —
single incidental mention, likely a baseline citation). Preliminary read: cross-vendor composition
looks like the dominant pattern among this corpus's multi-agent review solutions, not the
exception — a citable prevalence claim once confirmed by a full read.

**Naming trail:** "adversarial-review" (broad, compound) rejected as repeating `ai-review`'s own
structure/function conflation. "Cross-examination" rejected — checked against the corpus
directly: appears exactly once (*Measuring Progress on Scalable Oversight for LLMs*), meaning a
**human** cross-examining a **single** AI, not agent-checks-agent; adopting it would import a term
the corpus already uses for a different concept. "Adversarial" alone *is* corpus-native (recurs in
UB2EVUFU, U9VZQXGI, HBR7QZ2C for close to this concept) but was dropped in favor of the
structure/function split above rather than one compound name. "Cross-model" is corpus-native
(A6ZE2A26, describing multi-vendor composition directly) and was kept.

**HOS guardrail note:** HOS's own decorrelation design (Claude=author, Codex=adversary,
Gemini=correctness/architecture, Copilot=CI baseline) motivated *asking* this question but is
explicitly not corpus evidence for it, per the standing guardrail (`HOS_Seeded_Theme_Candidates.md`
§ intro) — the corpus check above, not HOS, is what grounds staging this.

Not yet in the live v2.13 instrument (frozen for gauge constancy); apply by hand as
`cal:human:facet:agent-panel` / `cal:human:facet:cross-model` ahead of a formal graft decision.

## 34. `evaluated-synthetic`/`evaluated-benchmark` boundary rules sharpened via pressure-testing (ZBF86IJM, NRVQT89E, 2026-08-22)

Arbiter pressure-tested both staged evidence-strength facets against two new worked examples
during full-read cleanup, surfacing two real gaps in the prior wording (§33's rename carried the
gaps forward unchanged; this entry fixes the substance).

**Gap 1 — "standardized" was underspecified.** ZBF86IJM's coding tasks were sourced from LeetCode
(a well-known platform, "easy" tier) — initially read as pushing toward `evaluated-benchmark`
("well-known dataset"). **Ruling: "standardized" means administering a recognized third-party
benchmark's own fixed protocol** (task set + scoring methodology, as DVNA/ProjDevBench are) — not
"sourced from a platform with difficulty tiers." The authors hand-picked 15 candidates from
LeetCode, generated their own completions, piloted, and pruned to 3 by their own criteria — that's
authored curation on top of a well-known raw-material pool, not benchmark administration.
`evaluated-benchmark` requires the real, fixed, field-recognized thing, run as-is.

**Gap 2 — the "no real users" phrasing in `evaluated-synthetic`'s HBR7QZ2C worked example had been
read as a general criterion, and wasn't justified as one.** Corrected ruling, grounded in the
instrument's pre-existing world-or-tool test rather than an ad hoc rule: **the evidence-strength
ladder (`self-tests`/`evaluated-synthetic`/`evaluated-benchmark`) and the method-* facets
(`method-experiment`/`method-field-study`) are a fork, not independently-composable properties.**
An evaluation event lands on the *tool* side (nobody real performs the task; the system runs and
something/someone grades the output after) or the *world* side (a real subject performs the task
and their behavior is measured) — never both for the same event. `evaluated-synthetic` = the
authors invented their own test data/cases and measured their own system against that self-made
material, tool side only. The moment a real subject performs the task, that event is
`method-experiment` (defined task set + manipulated condition) or `method-field-study` (real work,
natural setting) instead — **not additionally `evaluated-synthetic`**, even when the task material
was author-curated, because stimulus curation is inherent to any controlled experiment and treating
it as sufficient would make the facet fire on nearly every `method-experiment` paper (the same
near-100%-base-rate failure mode already rejected once this session for a `risks` facet proposal).

**Worked contrast, both directions:**
- **ZBF86IJM** — real programmers used the Edit Model live to complete tasks; results describe the
  world. `method-experiment` only. Does **not** also get `evaluated-synthetic`, despite the
  author-curated LeetCode-derived material.
- **NRVQT89E** — contains *two separate* evaluation events, one on each side, which is why it
  legitimately carries tags from both without violating the fork: the critic model runs alone and
  a contractor grades its output afterward (tool side → `method-field-study` *ladder rung*, on the
  strength of real production-sourced material) **and** the contractors' own tampering/rating task
  is itself a real controlled human-subjects exercise (world side → `method-experiment` *facet*).
  Two distinct measurements in one paper, not one measurement double-tagged.

Docs updated: `Methodology/HOS_Seeded_Theme_Candidates.md` (`evaluated-benchmark` and
`evaluated-synthetic` entries both carry the corrected reasoning + worked examples inline).

## 35. `05 - Synthetic-Eval Check` (21 items) — arbiter pass COMPLETE, retained as gold set (2026-08-22/23)

Arbiter worked all 21 candidates from the original tripwire scan (§ staging note in
`HOS_Seeded_Theme_Candidates.md`) to a final `cal:human:facet:*` disposition on the
`evaluated-synthetic`/`evaluated-benchmark`/`method-field-study`/`method-experiment`/plain
`self-tests` axis, applying the corrected exclusivity rule (§34) throughout. Several calls
surfaced mid-read as sharper edge cases than the original tripwire scan anticipated — recorded
here since they're reusable reasoning, not just this-paper trivia:

- **I6FZ5GD2** (visual analytics for AIDE coding agents) — `evaluated-benchmark`: Section 6 runs
  22/24 case-study competitions from **MLE-Bench (lite)**, a genuine established third-party
  benchmark, administered with its own real Kaggle tasks/metrics. Also carries a separate
  human-expert component (5 ML scientists) that the panel already proposed `expert-validated`
  for — plausibly correct for the right reason (panel judges the finished tool, not producing
  data), unlike MFSZPSPU below.
- **MFSZPSPU** (LLM-as-judge patch validity) — `method-field-study`, **not** `expert-validated`:
  real production-sourced bugs (Google sanitizer tools) support the field-study ladder rung, but
  neither human touchpoint clears the `expert-validated` bar — the rubric-refinement step is
  input-side shaping (excluded by definition) and the 3-rater ground truth is "experts as study
  subjects" (also explicitly excluded, routes to `method-experiment` instead, which stays as a
  separate co-occurring tag).
- **VZ27QUPQ** (API misuse detection/repair) — `evaluated-synthetic` **+ `method-mining`**: the
  qualitative-study dataset draws on The Stack (real, established GitHub corpus) but the authors
  build their own extraction/sampling pipeline on top of it (no prescribed protocol exists for
  "API misuse" on The Stack) — real raw material, author-invented methodology, so `method-mining`
  for the real-world-artifact characterization, not `evaluated-benchmark`. Dr.Fix (the repair
  system) separately stays `evaluated-synthetic` — self-labeled "our benchmark," release-upon-
  acceptance only, not yet adopted by anyone (the "wants to be a benchmark ≠ is one" distinction).
- **XRTVITVP** (scalable interactive oversight) — `evaluated-synthetic`, no `method-experiment`
  despite the panel proposing both: appendix read confirmed carefully-constructed prompts/tasks,
  system self-runs, LLM-judge scores it — no real human in the main-loop evaluation (a simulated
  non-expert user substitutes for one side of the "sandwich protocol," an LLM-judge substitutes
  for the other at scale).
- **96XE669R** — confirmed `evaluated-synthetic` (new instrument — VERICODE taxonomy + SWE-IF
  testbed — built on top of established benchmarks BigCodeBench/LiveCodeBench, substantial
  deviation, no release/availability language found). A leftover `evaluated-benchmark` tag from
  before this resolution was removed to avoid the two rungs co-existing on one evaluation event.

**Full final tag distribution (21 items):** `method-experiment` only — ZBF86IJM, JCTP8VXP,
WBS9U5N7*, CI93QRUH, ZH6QIU8A, XK3P9C96 (6, *WBS9U5N7's ladder side is `evaluated-synthetic`,
listed there). `evaluated-synthetic` only — A6ZE2A26, C88VGWMI, WBS9U5N7, 96XE669R, VZ27QUPQ,
XRTVITVP (6). `evaluated-benchmark` only — X7EN6DXZ, A5WDGC7J, T3XTXIXW, I6FZ5GD2 (4).
`method-field-study` only — MFSZPSPU (1). Two-event papers (ladder + separate `method-experiment`)
— U9VZQXGI, NRVQT89E, 7UB2MD8Z (3). Untagged/`self-tests` — Y4TIF9KW, 7SH86C2W (2, not
built-system-evaluation papers on this axis).

**Retained as the gold/validation set for these two facet pairs** — same role `human_gold.json`
plays for the main v2.13 instrument. If a future formal panel run ever extends
`evaluated-synthetic`/`evaluated-benchmark` coverage (Context tier, or a Core-tier panel-accuracy
check), this 21-item set is the reference to score the panel against, not a target for re-review.

## 36. Five discriminators sharpened during a Light Read full-record tag (BU73N7PC, 2026-08-23)

Arbiter tagged BU73N7PC ("Moving Faster and Reducing Risk: Using LLMs in Release Deployment")
against the panel's proposal (Opus/Codex primary `risk-routing`, Gemini primary `ai-review`;
Codex additionally proposed `hitl-workflow`+`oversight-explanation`; Opus/Codex also proposed
`framework`+`metrics`; no model proposed a method-* facet despite unanimous `built-system`+
`adopted`). Five real gaps surfaced resolving the disagreements — instrument definitions
unchanged in substance, discriminators made explicit:

**1. Primary-theme tie-breaker, goal vs. mechanism.** When a paper spans `risk-routing` and
`ai-review`, primary goes to whichever role the paper's own contribution occupies: is the AI
*judgment* itself the thing being contributed/evaluated (`ai-review`), or is the paper's
contribution the *allocation decision* that AI judgment feeds into (`risk-routing`)? BU73N7PC:
the risk-routing decision (which release changes get flagged for review) is the paper's stated
goal; the LLM classifier producing that signal is the mechanism serving it. Primary =
`risk-routing`, secondary theme `ai-review`. This sharpens (doesn't replace) the existing
altitude/novelty tie-breaker (§ Tag_Cheatsheet.md "Tie-breaker" bullet) with a concrete
goal-vs-mechanism framing for this specific theme pair.

**2. `hitl-workflow` requires a workflow built for human review of AI output — not any workflow
that happens to use AI.** BU73N7PC drops an LLM risk-classifier into Uber's pre-existing release
pipeline; no checkpoint/gate was *designed* to have a human review AI-generated code. Ruling:
"AI operating inside a pre-existing operational workflow" ≠ `hitl-workflow`. The direction also
matters — here the AI is reviewing/assessing **human-written** code changes, not AI output being
reviewed by a human, which is the inverse of what the theme covers and routes instead to the
`general-code` scope flag (the mechanism targets code generally, review-side AI, transferable to
our setting).

**3. `framework` negative worked example: a tool/stage bolted onto someone else's existing
pipeline fails the "reusable architecture" test.** BU73N7PC's classifier is one stage feeding an
existing deployment pipeline, not a pipeline design of its own — confirms the existing test
(*would someone adopt it as a reusable pipeline design?*) with a clean negative case, since the
paper's `built-system`+`adopted` pairing could otherwise read as `framework`-shaped at a glance.

**4. `adopted` does not imply `method-field-study` — check what the paper actually measured.**
A system can be in real production use (`adopted`) while the *evidence reported about it* still
comes from a controlled experiment (assigned/manipulated conditions) rather than observed
natural-use outcomes over time. BU73N7PC: `adopted`+`built-system` (real deployment) **+
`method-experiment`**, no `method-field-study` — the paper reports a controlled comparison, not
post-rollout incident-rate outcomes; had it reported the latter, `method-field-study` would apply
instead/additionally. Deployment status and evidence shape are independent axes.

**5. `metrics` requires the metric be a defined, reported deliverable — not the internal
apparatus a mechanism runs on.** Opus/Codex proposed `metrics` on BU73N7PC's risk score, but the
paper doesn't dwell on it: no formula, no reported detection-rate numbers, no discussion of the
metric's own properties — it's mostly inferred from what the routing decision implies. Ruling:
this is the apparatus feeding `risk-routing`'s allocation decision, not a separately-contributed
measurand the paper names and evaluates in its own right (the existing "contribution, not
apparatus" bar in the facet's definition, applied). Rejected. Worth flagging as a recurring
temptation specifically on `risk-routing` papers — nearly every one computes *some* internal
score, so treating that as sufficient would push `metrics` toward the same near-100%-base-rate
failure mode already rejected for other facets (§34).

Docs updated: `Tag_Cheatsheet.md` (`hitl-workflow`, `framework`, `metrics`, tie-breaker bullet —
inline worked-example additions).

## 37. `evaluator-reliability` theme STAGED + `primary-proposed:` convention + pass-scoping principle (2026-08-23)

Three things settled while working the Light Read pass. The theme candidate itself is recorded in
`Methodology/HOS_Seeded_Theme_Candidates.md` (§E, full definition/discriminator/anchors); this
entry carries the two *general* conventions that fell out of staging it, which apply to any future
staged tag, not just this one.

### 37a. `evaluator-reliability` staged (summary; full record in HOS_Seeded_Theme_Candidates §E)

Papers whose object is **whether an AI evaluator works** (LLM-as-judge, verifier, automated
reviewer audited as the subject) have no home in the instrument. Evidence: of 14 current
`demote:context` items (*demote = Core → **Context tier**; the paper is retained in the corpus,
just not carried into the Phase 6 core synthesis — it is not a discard*), **three** are this exact
class — `WBS9U5N7` (theme layer left *blank*
because nothing fit), `UDVHQ5HR` and `BAWCBT9R` (both forced into `primary:theme:ai-review` for
lack of an alternative). Fills the empty slot in *Limits of current oversight* alongside
`automation-bias` (human fails) and `oversight-theater` (process fails). Scoped narrowly to
evaluator-**auditing**; a broad `llm-eval` was considered and **rejected** as cannibalizing
`ai-code-insecurity`/`quality-debt`, core themes for which LLM evaluation is the *method*, not the
identity. Discriminator vs `ai-review` (whose text already claims "its reliability limits") is the
open question the sweep must settle, not assume.

### 37b. NEW CONVENTION — `cal:human:primary-proposed:theme:<slug>` during staging

**Problem:** a staged tag that would become a paper's *primary* can't be written as
`cal:human:primary:theme:<slug>` without destroying the record of what the primary was before —
and without silently changing the frozen instrument's output mid-corpus. Applying it at all
conflates "this was always the primary" with "this primary changed when a new theme arrived."

**Rule:** while a theme is staged, record displacement as
`cal:human:primary-proposed:theme:<slug>` and **leave the standing `cal:human:primary:theme:*`
untouched**. Membership still goes on normally as `cal:human:theme:<slug>`.

- Preserves gauge constancy — the frozen instrument's primary is undisturbed while the candidate
  is provisional.
- Preserves provenance — original vs. changed primary stays distinguishable, which
  `cal:human:primary:*` alone cannot express (the panel's `cal:<model>:primary:theme:*` tags are
  *machine* proposals, not the arbiter's prior human call).
- Clean cutover both ways — promotion converts `primary-proposed:` → `primary:` in one
  deterministic pass; rejection deletes the tag and disturbs nothing.

Generalizes to any staged tag capable of displacing a primary. Layers cleanly under the ratified
three-layer namespace (§ `Theme_Tagging_Calibration.md`): `cal:<model>:*` → `cal:human:*` →
`final:*`; `primary-proposed:` is a staging-only sublayer of the middle tier and never survives
into `final:*`.

### 37c. Pass-scoping principle — compartmentalize by mutual-exclusion group, not by tag count

> **DEFERRED — decide after screening completes.** Standing rule (2026-08-23): pass-design
> questions raised mid-screening are **parked, not resolved** — "we consider passes when done with
> the screening, that way we have the full picture." This section records the reasoning while it
> is fresh so the decision has something to start from; it is **not** a settled ruling and nothing
> here should drive a run before the Light Read pass is finished.

**Question raised:** at what point does asking one model to weigh 44 tags in a single pass hit a
lost-in-the-middle failure, versus splitting into narrow compartmentalized runs (as was done for
the evidence-ladder facets)?

**Answer adopted: split by whether the tags are mutually constraining or orthogonal — tag *count*
is the wrong axis.**

- **Mutually-exclusive / comparative decisions must stay in ONE pass.** Primary-theme selection is
  inherently comparative — "the theme carrying the distinctive novelty" is unanswerable from a
  two-theme menu. Same for the evidence-strength ladder (`self-tests` < `evaluated-synthetic` <
  `evaluated-benchmark` < `method-field-study` < `adopted`): one slot, competing fillers, one pass.
  This is *why* the eval-facet run worked — it happened to be exactly one mutual-exclusion group.
- **Orthogonal binaries can be split off freely.** `agent-panel`/`cross-model`,
  `evaluator-reliability` membership, the `risk-*` flags — independent judgments that don't compete
  for a slot. These are the safe candidates for a separate restricted run, and splitting them buys
  richer per-tag definitions and worked examples in the prompt.
- **Corroborating evidence that the current single pass is at/over capacity:** the instrument
  already concedes it — `Tag_Cheatsheet.md`'s facet block carries an explicit seven-question
  checklist with the note "*misses cluster here; 42 tags exceed recall*." An enumerated checklist
  is a mitigation for exactly this failure. The panel shows both failure modes in the sweep data:
  codex sprawl (8–12 themes proposed) and facet misses generally.
- **Cost of over-splitting (real, not hypothetical):** each pass re-reads the full text, and a
  paper judged in eight narrow passes can accumulate an *incoherent* tag set (facets contradicting
  the theme) that no single pass would have produced. Coherence is a property of joint judgment.

**Testable, no new runs required — QUEUED for post-screening:** the k=3 replication data already
measures decision quality directly via intra-model instability (the `unstable:<model>` tripwire).
If lost-in-the-middle is real, instability should rise with the number of themes a model proposes
— i.e. codex (8–12) should be measurably less self-consistent than opus (3–4) on the same papers.
Computable from the existing `data/tags-v213/{opus,codex,gemini}/*.r*.json` files; it converts this
principle from reasoning to measurement. **Run it when the screening is complete, not before** —
even zero-cost analysis is premature mid-pass, since a partial picture risks designing the next
pass around a pattern the remaining papers would have changed.

### 36a. Goal-vs-mechanism discriminator — mirror case confirming the rule (6F3S8IB7, 2026-08-23)

`6F3S8IB7` (HAIF) is the negative-image companion to BU73N7PC for the §36.1 discriminator, and
worth keeping as a pair since the rule is only testable if it lands both ways.

Both papers carry a genuine, non-token risk-tiering mechanism. They resolve **oppositely**:
- **BU73N7PC** — the allocation decision *is* the contribution; the LLM classifier serves it →
  primary `risk-routing`.
- **6F3S8IB7** — the tier matrix (Structuredness / Verifiability / Consequence of Error / AI
  Demonstrated Capability → Tier 1–4) is real and operational, but it is *one component* of a
  hybrid-team operating model (four principles, delegation protocol, estimation, retrospectives)
  → primary `hitl-workflow`, `risk-routing` retained as a secondary theme. The existing
  component-doesn't-outrank-the-broader-contribution rule decides it.

**Arbiter flipped the panel here** (modal `risk-routing`, 7 of 9 runs; gemini's base run alone
proposed `hitl-workflow`) — a case where the machine majority tracked the most *conspicuous*
mechanism rather than the contribution's altitude.

**Secondary ruling — routed *depth* is still routing.** HAIF states that *every* AI output has a
named human owner and that *all* outputs are "subject to validation," which reads at first like
the review-everything anti-pattern (which would make it a `counterpoint` candidate, not
`risk-routing`). It isn't: coverage and accountability are 100%, but **review depth is routed** —
Tier 2 full checklist review, Tier 3 post-hoc sampling at p% (default 20%, adjusted down on
evidence), Tier 4 monitoring plus exception handling; the owner "does not need to review every
output personally." **Rule: `risk-routing` is satisfied by allocating review *intensity*, not only
by allocating *whether* an item is seen at all.** Universal accountability coexists with routed
scrutiny; check which of the two a paper's "every output" language is actually claiming before
reaching for the anti-pattern.

*(Corpus note, not a tag: HAIF's tiering explicitly adapts **acceptance sampling** from statistical
quality control — AQL and lot sizes, cited as such — making it a direct corpus instance of the
SQC/Jidoka framing used in the project's own QA design.)*

### 36b. `design-only` tier discrimination — a Core/Context contrast pair (6F3S8IB7 vs VCI88UZD, 2026-08-23)

Two `design-only` papers, opposite tiers, discriminated by exactly one clause. Recorded as a pair
because the `design-only` core-bar carve-out is easy to read as a judgment call and isn't one.

**The carve-out (existing, `Tag_Cheatsheet.md` → `design-only`):** *names the elements to track AND
defines operationalizable metrics → clears the bar as measurement even unevaluated; what-only
enumerations / unevaluated frameworks without defined metrics → context candidates.*

- **`6F3S8IB7` (HAIF) → CORE.** What+how both present: elements to track (error rates, error types,
  review time, false acceptance rates) *and* operationalizable criteria (S/V/C/D decision matrix →
  Tier 1–4, 20% starting sample rate with adjustment rule, tier-transition mechanics). The paper
  claims the carve-out in its own framing — prior work converges on *what* teams should attend to
  (transparency, ownership, validation discipline, skill preservation); HAIF positions itself as
  the missing *how*.
- **`VCI88UZD` (human-certified module repositories) → CONTEXT.** What-only: asserts trusted
  repositories are needed without specifying how to operate one — no metrics, no criteria, no
  protocol. (Compounded by minimal AI involvement, but the what-only shortfall alone is
  sufficient.)

**Rule made explicit — uncalibrated ≠ unspecified.** HAIF concedes its thresholds are reasoned
estimates requiring empirical calibration, and identifies empirical validation as future work.
That does **not** cost it the carve-out: the reader must *calibrate* a supplied parameter, not
*invent* an absent one. Operational test for future cases: **could a team run it Monday without
inventing the missing piece?**

**Tier is not evidence strength.** The two axes are independent by design and must not be traded
against each other: tier (Core/Context) is a *scope* judgment; the form ladder (`design-only` →
`built-system` → `adopted`) plus the method-* facets carry *evidence strength*. A normative
"here is the right thing to do" contribution with no field evidence is a legitimate Core paper
sitting at the lowest evidence rung — that combination is reportable, not contradictory. Mirrors
the same separation already documented for `dissertation-input` ("tier ≠ importance").

**Stat this enables (compute at end-of-screening, not before):** proportion of solution-side Core
papers at `design-only` with no method-* facet. If that share is large it is a *finding*, not
corpus noise — it is the evidence-gap the dissertation's organizational survey exists to close.

## 38. `framework` facet RESOLVED — orthogonal to theme; covers process, not just pipeline (6F3S8IB7, 2026-08-23)

Raised as an open boundary question while tagging HAIF and **resolved same-session by arbiter
ruling** (not deferred — this is a definitional clarification of an existing tag, not a pass-design
question, so the park-until-end rule does not apply).

**The ruling, in the arbiter's words:** *"Org governance is: does it address org governance.
Framework is: whether it defines a mechanism / process."*

**Two axes, not one.** The theme answers **what subject the paper addresses**; the `framework`
facet answers **whether a definable mechanism/process is offered**. They are orthogonal, so
`framework` + `theme:org-governance` co-occur freely — and the corpus already shows this (8 of 128
papers in opus's base read; HBR7QZ2C carries both by prior arbiter hand). The old "≠
`theme:org-governance`" wording meant only *the facet is not a substitute for the theme*; it was
being misread as an exclusion.

**Scope widened to match the ruling:** `framework` is **not** restricted to technical/pipeline
artifacts. "Mechanism **or process**" includes organizational/team process designs. `6F3S8IB7`
(HAIF) is the grounding positive case — zero software (four principles, a tier decision matrix,
validation protocols, checklists, Scrum ceremony changes), yet a fully specified adoptable process
→ `framework` **+** `primary:theme:org-governance`. The old test ("*would someone adopt it as a
reusable **pipeline** design?*") returned the wrong answer on process frameworks and is replaced by
"*does it define a mechanism or process someone else could adopt?*"

**What survives unchanged:** the point-tool exclusion still does the real discriminating work. A
one-off tool or single stage bolted onto someone else's pipeline is not a defined mechanism/process
(BU73N7PC, §36 — ruling stands under the new wording, for the same reason). A bare
taxonomy/decision-model alone still earns neither.

**Correction to §36a reasoning.** In arguing 6F3S8IB7's primary I cited the *absence* of
`framework` as a confirming signal for `org-governance`. Under orthogonality that inference was
never valid — facet presence/absence carries no information about the theme. The primary ruling
itself is unaffected: it rests on the paper's self-description ("governing what happens after the
model produces output"; "accountability assignment") and on the component-doesn't-outrank rule,
both independent of the facet. Recorded here rather than silently amended so the bad inference
doesn't get reused.

## 39. `framework` scope-widening REVERTED — base-rate failure; narrow technical scoping restored (2026-08-23)

§38 widened `framework` from "technical framework / reference architecture integratable into a
build pipeline" to "defines a mechanism **or process**." **Reverted same session by arbiter
ruling:** *"Nearly everything would do that. Let's restrict framework to built scenarios —
something you integrate into a pipeline."*

**Measured, not asserted (opus base runs, n=128):**

| Scoping | Papers carrying `framework` |
|---|---|
| Technical / pipeline (original, restored) | **46 (36%)** — discriminating |
| "Defines a mechanism or process" (§38, reverted) | **≥72 (56%)** floor — and that floor is derived from facets the models assigned under the *narrow* reading, so the true figure is higher, approaching universal across the solution half of the corpus |

A facet that fires on most of the corpus carries no information. Same base-rate failure mode
already rejected for a proposed `risks` facet (§34) and guarded against for `metrics` on
`risk-routing` papers (§36.5). **Standing lesson: when widening a facet, compute the resulting
base rate before adopting the wording** — §38 was reasoned from a single hard case (HAIF) without
checking what the new wording would sweep in. One paper is enough to expose a gap; it is not
enough to size a fix.

**What "built scenarios" does and does not mean.** It does **not** require `built-system`: 12
corpus papers carry `framework`+`design-only`, and that composition is documented in the
`design-only` definition ("*mutually exclusive with `built-system`/`adopted`; composes with
`framework`*"). Requiring a build would invalidate all 12 and contradict the instrument. The
restriction is **buildable and pipeline-integratable — built or not.**

**What survives from §38:** the **orthogonality** clarification stands, unaffected by scope. Theme
answers *what subject*; facet answers *what form*. `framework`+`theme:org-governance` still
co-occur freely (8 corpus papers) **when the artifact is technical and the subject is governance** —
HBR7QZ2C, a policy engine, is the clean case. The legacy "≠ `theme:org-governance`" phrasing still
means "not a substitute for the theme," not an exclusion.

**Consequence for 6F3S8IB7 (HAIF):** it no longer qualifies — four principles, a tier decision
matrix, validation protocols, checklists and Scrum ceremony changes, but **zero technical
artifact** and nothing to integrate into a pipeline. Nothing is lost by dropping the facet: its
form is fully carried by `design-only` ("specifies a mechanism in buildable detail but never
credibly runs it" — tiers, thresholds, matrix all qualify) and its subject by
`primary:theme:org-governance`. **This reverses the arbiter's earlier same-session instance call
("definitely a framework") — flagged explicitly rather than silently applied.**

**§39 addendum — the decision line, in the arbiter's words (2026-08-23).** *"Proposing a framework
for a pipeline is a design-only framework. Process is governance."* Three-way resolution, now the
canonical form of this rule in `Tag_Cheatsheet.md`:

| What the paper offers | Tags |
|---|---|
| Pipeline architecture, built | `framework` + `built-system` (+ `adopted` if used outside research) |
| Pipeline architecture, proposed only | `framework` + `design-only` — *a proposed pipeline framework is a design-only framework*, not a non-framework (the 12 corpus papers) |
| Process / org practice, no technical artifact | `theme:org-governance` + `design-only` — **no `framework`** |

The middle row is the one that had been ambiguous and drove the §38 misstep: "not built" was being
conflated with "not a framework." Buildability, not build status, is the test.

**Applied to 6F3S8IB7 (HAIF):** `cal:human:facet:framework` **removed** (snapshot:
`Backups/zotero-item-snapshots/6F3S8IB7_pre-framework-removal_2026-08-23.json`; arbiter note added
to the item). Final human tag set: `primary:theme:org-governance`; themes `org-governance`,
`hitl-workflow`, `risk-routing`, `provenance-auditability`, `oversight-scaling-inversion`; facets
`design-only`, `risk-overreliance`, `risk-quality`. Core, `dissertation-input`, `s5:read`.

## 40. Was the agent prompt ambiguous on `framework`? — yes, but narrower than it looks; plus instrument drift found (2026-08-23)

Question raised after the §38→§39 reversal: *was the same ambiguity present in the tagging
instructions given to the panel?* Checked against the run data rather than reasoned about.

### 40a. Yes — and it is systematic, not noise

`Tag_Prompt.md` line 50 carried the **identical** pre-§39 wording ("technical framework /
reference architecture integratable into a build pipeline… ≠ `theme:org-governance`… *would
someone adopt it as a reusable pipeline design?*"). On 6F3S8IB7 (HAIF), the panel split **5 of 9
runs**, and the split is **model-systematic, not random**:

| model | r1 | r2 | r3 |
|---|---|---|---|
| codex | ✓ | ✓ | ✓ |
| gemini | ✓ | ✗ | ✓ |
| opus | ✗ | ✗ | ✗ |

Opus read the definition as technical-only (the reading §39 restored); codex read it as
any-framework; gemini was unstable with itself. A clean, reproducible disagreement on exactly the
pipeline-vs-process boundary — so the ambiguity was in the instrument, not only in the arbiter's
or assistant's reading of it.

### 40b. But `framework` is NOT an outlier — the facet layer is broadly contested

Split rate = share of papers (among those where ≥1 run proposed the facet) on which the 9 runs
disagreed. Computed over all 128 sweep papers:

| split % | facet | | split % | facet |
|---:|---|---|---:|---|
| 94% | problem-statement-anchor | | 53% | risk-ip · method-field-study |
| 87% | intro-framing | | 50% | assistive · lit-review |
| 85% | risk-bias | | 48% | general-code |
| 83% | counterpoint | | 45% | risk-quality |
| 81% | non-developer | | 44% | method-mining |
| 75% | steering | | 40% | method-experiment |
| 74% | metrics | | 36% | method-self-report |
| 70% | design-only | | 35% | risk-security |
| 68% | survey-input | | 27% | agentic |
| **59%** | **`framework` — rank 10 of 24** | | 20% | built-system |
| 56% | risk-overreliance | | 11% | general-ai |

**Nine facets are worse.** Singling out `framework` would have been a mistake — the honest finding
is that the *facet layer generally* carries high inter-run disagreement, with the role facets
(problem-statement-anchor, intro-framing, counterpoint) worst of all. Caveat: low-n facets inflate
the rate (risk-bias n=13, problem-statement-anchor n=17), but `steering` (n=63, 75%) and
`framework` (n=70, 59%) are large-n and still high.

**This is contained by design, not a crisis:** the triage ladder already routes non-unanimous
papers to LIGHT-REVIEW or HUMAN. High facet split is what the ladder exists to absorb. It does,
however, mean **facet counts from panel data alone are not reportable** — they need the human pass
behind them, which is what the Light Read is doing.

**Minor, don't overclaim:** the "≠ `theme:org-governance`" wording did mildly suppress
co-tagging — 8 observed co-occurrences vs 11.1 expected under independence (opus base, n=128).
Consistent with it being read as soft discouragement rather than hard exclusion. Small n.

### 40c. Instrument drift discovered — `Tag_Prompt.md` has separated from `Tag_Cheatsheet.md`

`Tag_Prompt.md` is the cheat-sheet body **plus** a 13-line task block, and the two have
historically been kept in lockstep (last joint update `05a8b35`). **This session's six refinements
landed in `Tag_Cheatsheet.md` only** — lines 28 `hitl-workflow`, 50 `framework`, 54 `adopted`,
64 `metrics`, 71 method-* facets, 78 primary tie-breaker.

So the drift is **accidental, not a deliberate gauge freeze**. That distinction matters: a future
session could reasonably "helpfully" sync them and thereby change the machine gauge mid-corpus
without anyone deciding to.

**DEFERRED to end-of-screening** (pass-design decision, per the standing rule): whether to (a) sync
the prompt and accept a changed gauge for any future run, (b) deliberately freeze `Tag_Prompt.md`
at v2.13 and document it as frozen, or (c) fork a v2.14 prompt for restricted re-runs only. **Until
that is decided, do not sync them** — the divergence is now recorded, which is what makes it safe
to leave.

### 40d. Feeds the deferred §37c question

The split rates above are the empirical face of the lost-in-the-middle question, and of the
instrument's own admission in the facet checklist ("*misses cluster here; 42 tags exceed recall*").
Data for that decision. Also deferred.

## 41. Versioning plan for the accumulated refinements — RATIFIED, executed at end of validation (2026-08-23)

Standing decision on what happens to §36–§40's refinements. Recorded now so a future session does
not act on them prematurely or lose the provenance.

**The plan (arbiter, 2026-08-23):**
1. **Implications are considered at the END of the validation exercise**, not during it. Refinements
   keep accumulating in `Tag_Cheatsheet.md` and this changelog as the Light Read proceeds; nothing
   is acted on mid-pass.
2. **A new, revised tagging definition is produced at the end** — a successor instrument
   incorporating the refinements.
3. **The original is kept for records.** v2.13-as-used must remain retrievable verbatim: it is the
   gauge that produced both the 128-paper panel data and the human Light Read pass, so every stat
   computed from that work is only interpretable against it.
4. **A second panel run is NOT committed to.** Whether the revisions warrant re-running the panel
   is decided at the end, once the revisions are known and their scope is visible.

**This supersedes the open question in §40c** — the answer is option (c), fork a successor, with
the timing fixed at end-of-validation and preservation of the original made an explicit
requirement. **The "do not sync `Tag_Prompt.md`" instruction from §40c therefore stands until the
revised instrument is cut.**

**Where v2.13-as-used currently lives (verified 2026-08-23):**
- `Tag_Cheatsheet.md` @ commit **`05a8b35`** — the last state before this session's edits.
- `Tag_Prompt.md` @ HEAD, lines 1–80 — **byte-identical** to the above (verified by diff). The
  §40c drift, which was accidental, has the incidental effect of preserving the original in the
  working tree. Note this is *luck, not design*: it survives only as long as nobody "fixes" the
  drift, which is precisely why §40c says not to.

**Recommended before the revised instrument is cut (not yet done, needs a go-ahead):** write an
explicit frozen copy — e.g. `slr-phase4/Tag_Cheatsheet_v2.13_AS-USED.md` — so the record does not
depend on git archaeology or on the drift persisting. Cheap insurance; the two preservation paths
above are both incidental rather than deliberate.

**Naming for the successor is deliberately not fixed here.** Whether it is v2.14 (revision) or
v3.0 (new gauge) depends on whether the refinements turn out to be clarifications or definitional
changes — §38→§39 showed that distinction is not always obvious in advance, and the gauge-constancy
consequences differ.

## 42. Light Read protocol — what the demote call short-circuits (methods record, 2026-08-23)

Clarified by the arbiter mid-pass, recorded because it determines how corpus statistics may be
scoped in the write-up.

**The protocol:** every Light Read paper receives a human read and an **independent human tier
call**. Panel unanimity does *not* cause the review to be skipped. What the demote call
short-circuits is **downstream tag verification** — once a paper is ruled Context, its remaining
theme/facet proposals are not verified against the instrument.

**Extended to the Accept band (arbiter, same session): the 44 `01 - Accept` papers also receive a
human demote review.** This goes beyond the `Sweep_Reading_Guide.md` protocol for that band
("*read for content; override only if something jumps out*", plus 4 mandatory audit papers) —
tier is now deliberately ruled on, not merely left undisturbed. Consequence: the human **tier**
judgment covers all three bands and is genuinely corpus-wide (6 Full Read + 78 Light Read + 44
Accept = 128), not Light-Read-only.

**Why this is methodologically sound rather than a shortcut:** the tier decision does not depend on
the unverified tags. It is made by the arbiter from the paper itself against the §3 core bar, so
there is no circularity (the earlier worry — "tier decided on impression because the tags that
would evidence it went unchecked" — does not arise). Context papers do not enter the Phase 6
synthesis, so their tag depth has no downstream consumer. Effort is proportional to what the tags
are used for.

**Consequence for reportable statistics — the two axes have different coverage:**

| Axis | Human coverage | What may be claimed |
|---|---|---|
| **Tier** (Core/Context) | **corpus-complete, all 128** — human demote review across Full Read (6), Light Read (78) **and Accept (44)** | tier-level human-vs-panel agreement may be reported corpus-wide |
| **Tags** (themes/facets) | **partial — Core only** — full adjudication on the 6 Full Reads; on Light Reads verification stops at a Context ruling; on Accepts only the 4 designated audit papers plus anything that jumps out | any human-vs-panel *tag* agreement statistic **must be scoped to Core**, and the Accept-band contribution is an audit sample rather than a census; stating it corpus-wide would overclaim, since the verified subset is non-randomly selected |

**Residual gaps (both pre-existing, neither caused by this protocol):**
- **Demote reasons are unstructured.** `demote:context` records *that* a paper was excluded, not
  *why*; reasons live in free-text arbiter notes where they exist at all. So "N excluded as
  secondary literature, M as general-AI object" is not currently computable. Detailed tag review
  would not have fixed this — it needs reason codes, a separate and smaller change. Same gap
  surfaced while staging `evaluator-reliability` (§37).
- **Rescue cost is bounded and known.** If a staged tag later moves a Context paper back to Core
  (the `evaluator-reliability` candidate is the live case), that paper's tags need a verification
  pass at that point.

**Superseded reasoning:** an earlier draft of this analysis recommended stratifying the skip by
panel unanimity and audit-sampling the demote pile. Both assumed unanimity was gating arbiter
effort. It is not — every paper is read — so neither applies. Recorded so the recommendations are
not resurrected from a stale premise.

## 43. WATCH TRIPWIRE — papers misstating the EU AI Act as motivation (first instance WUUDHL8R, 2026-08-23)

Not a tag. A corpus-observation tripwire: **count recurrences; if a cluster forms it is a reportable
finding about field maturity**, directly relevant to the dissertation's governance-landscape strand
("papers invoke the AI Act as motivation without engaging it correctly"). One instance is not a
pattern — log and move on.

**First instance — `WUUDHL8R`** (AI-driven refactoring for data clumps), §"Regulatory Compliance
and EU AI Act". Two distinct errors:

1. *"Unacceptable risk … Therefore AI-Driven Refactoring cannot be used here."* — category error
   **and** vacuity. The Act's tiers classify an AI system by **intended purpose**, not the dev
   tooling used to produce it; a refactoring tool takes no tier from the domain of the code it
   touches. Worse, Art. 5 practices are **banned outright**, so there is no "here" in which any
   tool is or isn't usable.
2. *"AI Systems **or which use AI generated code** fall in this [high-risk] category…"* — flatly
   false, and the more consequential of the two: high-risk classification turns on Annex I
   (product-safety components) or Annex III (enumerated use cases). **Code provenance is not a
   criterion.** A spam filter written entirely by an LLM stays minimal risk; a CV-screening tool
   hand-written in assembly is still high risk. This error would drive real behaviour — it implies
   "we used AI, therefore we are high-risk," a false compliance trigger.

**Correct mapping (arbiter's reframe, endorsed):** *"if refactor is done in a risky area, needs more
human review."* The driver is the classification of the **system being modified**, not of the tool:
a high-risk system's provider already carries risk-management, QMS, logging and Art. 14
human-oversight duties, and a *substantial modification* can trigger re-conformity assessment — so
automated refactoring in that codebase needs controlled change management and human sign-off. Note
this reframe is itself **risk-routing**: regulatory tier as a routing signal for review intensity,
structurally the same move HAIF (6F3S8IB7) makes.

**Diagnostic value for tagging:** the error is evidence for a **mention-vs-membership** call. This
paper *claims* AI Act engagement as a stated contribution, but the section recites the four tiers
with no mapping to its own pipeline — no gate, no criteria, nothing operationalized. A paper that
had genuinely engaged would not produce those two sentences. → **no `regulatory-compliance`
theme.**

*Caveat on this entry: the Act analysis above is from working knowledge, not a cited text. The core
points (Art. 5 as enumerated prohibitions; Art. 6 classification via Annex I/III; provenance
irrelevant to tier) are well established, but verify article numbers before any of this reaches the
dissertation.*

## 44. `regulatory-compliance` — justification/background ≠ compliance contribution; and a correlated-error caution (WUUDHL8R, 2026-08-23)

**Discriminator (arbiter, 2026-08-23):** *"It is not compliance. That was justification /
background."* Invoking a regulation to **motivate** the work is not contributing to the compliance
argument. `regulatory-compliance` requires the paper to *do the lift* — map its mechanism to
specific obligations, operationalize a control, produce audit evidence, or analyse the legal
requirement substantively. Reciting a regulation's structure in a background section is **mention**,
however long the section is (the mention-vs-focal rule at paragraph length, §ZUM76CCG lesson).

`WUUDHL8R` is the worked negative: a dedicated §"Regulatory Compliance and EU AI Act", the Act named
in the abstract, keywords and stated contributions — yet the section recites the four risk tiers
with **no mapping to its own pipeline** and gets two substantive facts wrong (§43). Background, not
contribution. Theme **not** applied.

### 44a. Correlated error — unanimity is not evidence of correctness

**All 9 panel runs proposed `regulatory-compliance` on WUUDHL8R.** The arbiter rejected it on solid
grounds. This is a clean instance of a failure mode the triage ladder does not otherwise surface:

> When the error lives in a **shared misreading of the instrument** (here: treating any substantive
> discussion of a regulation as membership), unanimity **amplifies** it rather than correcting it.
> Three models agreeing is only evidence of independence-adjusted correctness when their errors are
> uncorrelated — and models reading the same definition are not independent on definitional
> questions.

This matters because the ladder treats 3/3 consensus as the ACCEPT band, audited at ~10%. A
systematic definitional misreading would pass straight through.

**Exposure, measured:** `regulatory-compliance` is proposed by ≥1 run on **27 of 128** papers, and
**unanimously on 12**: `27YULT5I`, `34ELRWJH`, `5RLPIA3K`, `HBR7QZ2C`, `ID7IN65K`, `P837LJWE`,
`RG4A4D6K`, `TW4I6DU6`, `WPWF7A32`, `WUUDHL8R`, `XZEHQYNZ`, `ZSB2S59N`. WUUDHL8R is now 1 of 12
checked and 1 of 1 wrong — a sample far too small to generalize from, and several of the others
(e.g. `XZEHQYNZ`, `5RLPIA3K`, both EU-AI-Act-titled) are plausibly genuine compliance papers.

**Mitigation already in place, no new work proposed:** the arbiter is performing a demote review
across the Accept band (§42), so these do not sit unexamined. **Apply the justification-vs-
contribution discriminator when each is reached.** Whether the unanimous-12 warrant a targeted
check as a group is an end-of-screening question, deferred per the standing rule — flagged here so
the observation is not lost, not to prompt action now.

## 45. ⚠ CONVENTION CONFLICT — `cal:human:*` override semantics vs non-exhaustive arbiter tagging (2026-08-23)

**Open issue. Affects the eventual `final:*` write pass. Do not script that pass until resolved.**

**Arbiter's working practice (stated 2026-08-23):** *"I am not doing an exhaustive audit of tags. I
am giving tags that I feel are valid. My omission of a tag does not mean it isn't valid, it means it
wasn't something that jumped out at me. Exhaustive tagging would be 2 or 3× the effort."*

**Documented convention it contradicts** (`Sweep_Reading_Guide.md` §1.3): *"any `cal:human:*` tag is
read as an **arbiter override** that beats the machine proposal wholesale for that layer (if you set
any `cal:human:theme:*`, your theme set is THE theme set…)"*

**The defect:** the convention has two states where the work has three.

| State | Meaning | Encoded today |
|---|---|---|
| Endorsed | arbiter named it — valid | `cal:human:*` ✔ |
| **Rejected** | arbiter considered and ruled it out | ✗ conflated |
| **Not considered** | didn't jump out; may well be valid | ✗ conflated — silently read as rejection |

Under wholesale-override semantics, a scripted `final:*` pass would **strip valid themes** from every
paper where the arbiter named only one or two — which, under non-exhaustive tagging, is most of them.

**Live instance:** `WUUDHL8R`. `cal:human:theme:ai-review` was written, which under the convention
drops `regulatory-compliance` (9/9 panel) *and* `hitl-workflow` (8/9). The first is a genuine
arbiter rejection ("it is not compliance — that was justification/background", §44). The second was
an **assistant argument** (plumbing rule) that the arbiter never ruled on — so the record currently
encodes a rejection that was not made. **Flagged to the arbiter; awaiting a call on whether
`hitl-workflow` is restored.**

**Proposed resolution (assistant recommendation, NOT adopted):** make `cal:human:*` purely
**additive endorsements**, and give active rejections their own machine-readable marker —
`cal:human:reject:theme:<slug>` / `cal:human:reject:facet:<slug>`. The final pass then computes
**panel modal ∪ human endorsements − human rejections** instead of *endorsements alone*. Costs the
arbiter nothing (rejections are rare and deliberate — two today, both reasoned) and makes the
three states distinguishable. Layers under the ratified namespace (§`Theme_Tagging_Calibration.md`)
as a `cal:human:` sublayer that never survives into `final:*`.

**Interim assistant practice, effective immediately:** do not write `cal:human:theme:*` as if it were
a complete set; record arbiter-named tags as *additive endorsements* and note explicitly in the
arbiter note that the set is non-exhaustive. Any tag dropped on assistant reasoning must be raised
with the arbiter, not written as a silent rejection.

**Retrospective exposure to check before the final pass runs:** every paper already carrying
`cal:human:theme:*` or `cal:human:facet:*` was written under the old reading. Those need review
against this distinction — a bounded, enumerable set, and cheap to list from Zotero. Deferred to
end-of-screening with the other write-pass questions, but it is a **data-integrity** item, not a
refinement.

## 46. `cal:human:reject:*` RATIFIED — resolves the §45 convention conflict (2026-08-23)

Arbiter adopted the proposed fix. The `cal:human:*` layer now encodes **three** states instead of
two:

| State | Tag | Meaning |
|---|---|---|
| **Endorsed** | `cal:human:theme:<slug>` · `cal:human:facet:<slug>` | "This applies." **Additive** — does *not* imply the set is complete |
| **Rejected** | `cal:human:reject:theme:<slug>` · `cal:human:reject:facet:<slug>` | "I considered this and it does not apply" — overturns a panel proposal |
| **Not considered** | *silence* | Didn't jump out; the panel proposal **stands by default** |

**Final write pass computes: panel modal ∪ endorsements − rejections.** Not endorsements alone.

**Primary is exempt** — single-valued, so `cal:human:primary:theme:<slug>` simply replaces the
machine's primary; a reject marker there would be meaningless.

**Placement in the ratified namespace:** `reject:` is a sublayer of `cal:human:` and, like the rest
of that layer, is **permanent audit trail — never stripped**. Rejections do not themselves become
`final:*` tags; they *subtract* from what does.

**First instances — `WUUDHL8R`** (Baumgartner et al. 2024, *AI-driven refactoring: data clumps*):
- `cal:human:reject:theme:regulatory-compliance` (panel **9/9**) — *"It is not compliance. That was
  justification / background."*
- `cal:human:reject:theme:hitl-workflow` (panel **8/9**) — *"It didn't cover it."* Closes the §45
  open item: this was previously encoded as a silent drop resting on an *assistant* argument
  (plumbing rule); it is now an arbiter ruling with its own reason and marker.

Both are unanimous-or-near-unanimous panel proposals overturned by human review — the §44a
correlated-error pattern, now machine-countable rather than buried in note prose. That count is one
of the reportable outputs of the human pass.

**Docs updated:** `Sweep_Reading_Guide.md` §1.3 (the source of the defective wording — rewritten to
the three-state model), `Methodology/Theme_Tagging_Calibration.md` (namespace section).

**Still owed (deferred, §45):** items tagged *before* today were written under wholesale-override
semantics and need review against the endorsed-vs-rejected distinction before the `final:*` pass
runs. Bounded and enumerable from Zotero. **Data-integrity item.**

**Open, minor:** the Actions & Tags YAML has no `reject:` menu entries. Adding all 44 (17 themes +
27 facets) would bloat the menu for a rare action — recommend adding entries **on demand** as
rejections recur, or continuing to have them applied via the API. Not blocking.

## 47. `agentic`/`assistive` — apparatus-vs-object rule (WBS9U5N7, 2026-08-23)

**Arbiter ruling:** *"Agents as part of setting up the experiment, not agents as a core part of the
experiment."* Agents used to **stage** a study — manufacture stimulus, generate test material, drive
the harness — are **apparatus** and earn no mode facet. The pair fires only when the
agentic/assistive generation is the **phenomenon under study**.

Test: *is the agent the thing being examined, or the thing doing the examining/staging?*

**Worked negative — `WBS9U5N7`** (Alami, *Cognitive camouflage*): a Mutator agent synthesizes
deliberately-gamed code so a review committee can be tested on whether it catches the gaming. Agents
are everywhere in the design, but there is no developer, no pipeline, no production setting — the
paper studies **detection**, not agentic development. All 9 panel runs proposed `agentic`; arbiter
rejected → `cal:human:reject:facet:agentic`.

This **sharpens rather than changes** the existing clause ("*uses agents*" ≠ `agentic`) by naming
the specific confusion it was written to prevent: the earlier wording said what doesn't count but
not *why*, so a paper saturated with agents still reads as agentic on a fast pass. Apparatus-vs-
object gives the reason.

**Assistant-error note (pattern, not incident).** I recommended endorsing `agentic` here on
"there are agents," reading the facet name in its ordinary sense rather than its instrument-scoped
sense. Same class of error as §38, where I widened `framework` because HAIF "is a framework in plain
English." Both times the definition already excluded the case and I read past it. Flagged so the
pattern is visible in my recommendations — the instrument's scoping clauses are the operative text,
not the tag's name.

**Docs updated:** `Tag_Cheatsheet.md` mode-pair line only. **Not** propagated to `Tag_Prompt.md`,
per §41 — the panel prompt stays frozen at v2.13-as-used until the successor instrument is cut.

## 48. Correction — WBS9U5N7 is a two-event paper, not a method-experiment confusion exemplar (2026-08-23)

`WBS9U5N7` (Alami, *Cognitive camouflage*) had been characterized — in the Light Read prep sheet and
in my own advice — as a clean example of the machine-only `built-system`/`method-experiment`
confusion the §34 fork was written to catch. **That was wrong.** Arbiter endorsed
`method-experiment` on review.

**Why it holds:** the instrument's own carve-out covers it — *"**Subjects may be systems:**
controlled studies of **third-party** tools/models whose findings characterize those systems =
`method-experiment` (UDVHQ5HR)."* The paper reports a controlled comparison of Claude, GPT-4o and
Gemini whose findings characterize *those* models (Gemini missed 2/8, Claude 0/8; Gemini fooled 4/5
in the full-thesis condition; GPT-4o oscillates across all four domains). The "whose properties?"
test points at third parties, not at ZTARE.

So it is the **two-event pattern** (NRVQT89E, U9VZQXGI): ZTARE's own performance → the ladder rung
`evaluated-synthetic`; the third-party model comparison → `method-experiment`. Both stand; the fork
is not violated because they measure different events.

**Final human record on the item:** endorsed `theme:ai-review` (membership only — explicitly *not*
primary), `theme:rules-based-checks`, `facet:built-system`, `facet:method-experiment`,
`facet:evaluated-synthetic`. Rejected `facet:agentic` (§47). Primary deliberately empty, slot held
by `primary-proposed:theme:evaluator-reliability`. `demote:context`.

**Lesson worth keeping:** "no human subjects" is not sufficient for the machine-only diagnosis — the
question is *whose properties the findings describe*. A study with zero humans can still be
`method-experiment` when its subjects are third-party systems. The earlier reading collapsed
"no humans" into "tool-results," which the UDVHQ5HR clause explicitly rules out.

**Docs updated:** prep sheet entry for WBS9U5N7 rewritten with the resolution and a pointer here.

## 49. `framework` — span rule + mental model (WUUDHL8R, 2026-08-23)

Fourth `framework` refinement today. Arbiter rejected the facet on `WUUDHL8R` despite it being a
genuinely built, CI/CD-integrated pipeline — the case §39's wording did not cover.

**Arbiter rationale:** *"restriction to one part of overall lifecycle, one engineering task. It
identified code that should be refactored, facilitates it."*

**Span rule:** confinement to **one lifecycle stage / one engineering task** disqualifies, no matter
how many internal steps the thing has. **Frameworks govern the flow; tools do a job inside it.**

**Mental model (arbiter's formulation, now the primary test):**
> *"Can this be integrated into a CI/CD or code-building pipeline **to facilitate code generation at
> quality with oversight**?"*

Both halves must hold — integratable **and** in service of overseen generation.

**Reconciled with the calibration anchors** (this was the check that validated the rule rather than
just accepting it):

| | What it does | Verdict |
|---|---|---|
| VibeGuard `T8E8SCCG` | detect + **publish gate**, no auto-fix | governs the release boundary — spans the flow ✔ |
| Hedwig `T72TU8B5` | dynamic-autonomy classifier + check-in surface | routing + human interaction across the flow ✔ |
| `WUUDHL8R` | detect data clumps → refactor → validate → PR | many steps, **one maintenance task**, one phase ✘ |

**Wording defect this exposed and fixes:** the clause "*a focused **single-concern** architecture
qualifies*" was being read as "single-**task** qualifies" — which licenses precisely what the span
rule rejects, and is the likely reason **9 of 9** panel runs proposed `framework` here. Now stated
explicitly: **concern may be narrow; span may not.** VibeGuard is single-concern (one quality
dimension) yet spans detect→gate; WUUDHL8R is single-task.

**Known tension, flagged not resolved.** The mental model cleanly reproduces the HAIF (§39) and
WUUDHL8R rejections, but **does not obviously reproduce the BU73N7PC rejection** — that risk
classifier *is* CI/CD-integrated and *is* in service of overseen release, yet §39 excludes it as a
stage bolted onto someone else's pipeline. Mental model and point-tool exclusion may pull in
different directions there. Left open deliberately; candidate for resolution in the end-of-validation
revision (§41).

**Meta-observation for the revision.** `framework` has now been amended four times in one day
(§38 widen → §39 revert → §39 decision line → §49 span rule) and carries a **59% panel split rate**
(§40b, rank 10 of 24). Treat it as the instrument's most under-specified facet and rewrite it
wholesale in the successor rather than patching further.

**Docs updated:** `Tag_Cheatsheet.md` only. **Not** propagated to `Tag_Prompt.md` per §41.

## 50. METHOD ≠ CONTRIBUTION — the apparatus rule, promoted to a cross-cutting preamble rule (2026-08-23)

**Arbiter ruling:** *"For our tags, those elements must be in the proposed system / framework / etc,
not just used for analyzing data in the study."*

Promoted from a per-tag caveat to a **universal preamble rule** in `Tag_Cheatsheet.md`, because the
principle already existed in the instrument **four separate times under four different names** and
still failed to catch theme-level cases:

| Where it already lived | Wording |
|---|---|
| `metrics` | *"Contribution, not apparatus"* — every empirical paper has an evaluation apparatus; that gets nothing |
| method-\* facets | *"Applies to the paper's **own evidence production**"* + the world-or-tool test |
| `agentic`/`assistive` (§47) | apparatus-vs-object — agents that *stage* a study earn nothing |
| preamble | *"Plumbing ≠ membership"* — tag only mechanisms the paper *argues about* |

None of those reach a **theme** proposed off the methods section, which is the gap this closes.

**The test:** *is this candidate tag triggered by what the paper **studies**, or by how the authors
**did the study**?*

**Worked failure — `ID7IN65K`** (Choudhuri et al.): the paper codes open-ended survey responses with
three LLMs against an author-approved codebook and reports Krippendorff's α with pairwise Cohen's κ.
**All 3 panel runs proposed `theme:ai-review`** — reading the methods section as content. Arbiter
caught it: *"there is a lot of discussion of multiagent panel etc for analysis of the survey data, so
could yield false positive for those tags."*

**Why this error is high-frequency and worth a preamble slot:** it fires precisely when a paper's
*research design resembles the phenomenon under study* — and in a corpus about AI reviewing code,
papers that use AI to analyse data are common. The resemblance that makes the paper methodologically
interesting is the same resemblance that makes the tagger misfire.

**Reflexive note.** This is also the trap the SLR's own panel is most exposed to, since our method
*is* multi-model AI review. Papers worth citing for their method (see
`Theme_Tagging_Calibration.md` §9 and the new **Methodology Support** collection) are exactly the
papers most likely to be mistagged for it. **Cite for method; do not tag for it.**

**Docs updated:** `Tag_Cheatsheet.md` preamble. **Not** propagated to `Tag_Prompt.md` per §41 —
though note this one is a *machine* error, so it is a strong candidate for the successor prompt.

## 51. Reference-oracle exclusion — a checker needing ground truth is not an oversight mechanism (PR4GS7SP, 2026-08-23)

**Arbiter ruling:** *"Symbolic execution would be yes, but this is using symbolic execution to compare
against a 'known implementation' rather than assess correctness on its own."*

**Rule:** a checker that requires a **known-correct reference implementation** is a *measurement
instrument*, not a Detect-stage oversight mechanism — because in real oversight the reference does
not exist. If you had the correct implementation, you would not need the generated code. The
technique used internally is irrelevant to this test.

**Operational question:** *could this run on an artifact whose correct answer is unknown?* No → not
a Detect mechanism.

**Worked case — `PR4GS7SP`** (Cotroneo et al., *Automating the correctness assessment of AI-generated
code for security contexts*). ACCA genuinely uses symbolic execution, and both `rules-based-checks`
(which explicitly lists "symbolic exec") and `formal-methods` (ditto, with the documented
`rules-based-checks`+`formal-methods` pairing for a classical engine) appeared 9/9 in the panel.
By the letter of both definitions they fire. **Arbiter rejected both** — ACCA tests *equivalence to
a ground-truth implementation*, so it can only operate where correctness is already known. It is a
benchmarking oracle for comparing code generators, which the paper states plainly: assess
correctness *"without any human effort"*, validated by correlation against human evaluation.

**Why this needed stating:** the Detect definitions enumerate *techniques* (tests, static analysis,
symbolic exec, sandbox) and a technique list cannot distinguish a deployable check from a research
oracle using the same machinery. This is the missing condition.

**Naming hazard noted in passing.** `rules-based-checks` invites reading its *name* literally ("it
doesn't discuss any rules") when its definition is the deterministic-grounded-check bucket, symbolic
exec included. That is the mirror of the assistant's own errors today, which read `framework` and
`agentic` too *loosely* (§38, §47). **The tag names in this instrument are bucket labels, not
definitions — in both directions.** Worth a line in the successor instrument.

**Docs updated:** `Tag_Cheatsheet.md` Detect-group preamble. Not propagated to `Tag_Prompt.md` (§41).

## 52. `oversight-scaling-inversion` NARROWED to fail-open; fail-closed saturation logged as a gap (NZJST99D, 2026-08-23)

**Arbiter ruling:** *"One case (fail closed) impacts productivity, usefulness but is quite safe. Bad
code never ships. Fail open is truly a risk and scary — bad code ships. That is actually an
important distinction. If we bucketed this paper in with those that talk about all the maladies of
bad code shipping, this paper would be very out of place."*

**The narrowing.** The theme is **fail-open only**: capacity mismatch whose consequence is that
under-inspected AI code **reaches production**. Capacity mismatch that resolves **fail-closed** —
work abandoned, nothing merged — is a *productivity* failure, not an oversight failure, and does not
belong here.

**Why the old wording admitted both.** The definition was four clauses in a list: *"riskier yet less
inspected; PRs auto-merged unreviewed; review is the bottleneck; burden piles on maintainers."*
Clauses 1–2 are fail-open; clauses 3–4 are bare capacity language that fits either resolution. Read
as alternatives, any capacity paper qualified. The definition **conflated a cause (capacity
mismatch) with an effect (unsafe code ships)** — and only the effect defines the harm.

**The test that settled it — synthesis, not definition-matching.** A theme is *where a paper gets
written up*. Asked whether `NZJST99D` would sit naturally in a section on the maladies of bad code
shipping, the answer is no: **nothing shipped**. 33k agent-authored PRs, dominated by reviewer
abandonment, with no fail-open case found in the text. Safety held; throughput collapsed. Rejected
→ `cal:human:reject:theme:oversight-scaling-inversion`.

**Corpus exposure of the narrowing:** `oversight-scaling-inversion` is proposed by ≥1 run on **33 of
128** papers, **unanimously on 13**. Papers already tagged with it under the loose reading should be
re-checked against the fail-open condition before the `final:*` write — add to the §45 retrospective
list. Bounded; the synthesis test is quick to apply.

**SCOPE GUARD (added 2026-08-23, after an over-application).** The narrowing is **fail-open vs
fail-closed ONLY**. It does **not** restrict the theme to *code review*. Any oversight function that
fails to scale while output ships qualifies — legal/compliance capacity, security review, audit
capacity. The review question says "**human oversight** of AI-generated code… keeps pace with code
volume," not "code review." `34ELRWJH` (Goodhue) is the worked case: *"Traditional software companies
scale legal capacity alongside technical capability… AI-assisted development **breaks this coupling
entirely**"* — legal review is the bottleneck, the applications ship anyway, fail-open. The assistant
initially challenged it by inventing a second, unruled narrowing (code-review-only) and mis-ran the
synthesis test by pre-loading "bad code ships" as *defects* rather than *exposure*. Recorded so the
same over-application is not repeated across the other 32 affected papers.

### 52a. GAP — no theme for fail-closed review saturation (tripwire, 1 instance)

With the narrowing, `NZJST99D`'s headline finding has **no home**: review capacity exhausted, agent
contributions dropped on the floor. Distinct from `oversight-theater` (review exists but lacks
authority — here it does not happen at all) and from `oversight-scaling-inversion` (fail-open).

Conceptually interesting because the **remedy differs**: fail-open calls for gates; fail-closed
saturation calls for triage — i.e. this phenomenon is *motivation for* `risk-routing` rather than
membership in it.

**One instance is not enough to stage** (the `evaluator-reliability` candidate had three).
**Tripwire:** papers reporting that AI/agent output volume overwhelms review capacity **without**
unreviewed code shipping. Count recurrences; revisit at end of validation.

**Docs updated:** `Tag_Cheatsheet.md` theme definition. Not propagated to `Tag_Prompt.md` (§41).

## 53. §30 general-AI exception — second exercise, and what clears the bar (9MV2IVNU, 2026-08-23)

§30 established that a `general-ai` paper is a *context candidate*, and that the sole-exemplar
exception is **"look at keeping," not "keep."** `9MV2IVNU` (Eze, *Human-in-the-loop isn't a
checkbox*) is the second exercise of that exception and the first worked example of what actually
clears it.

**Facts:** the decision domain is loans / benefits / moderation, not code — `general-ai` proposed
9/9 and applied. All three models flagged the demote. **Kept Core anyway.**

**Arbiter's reasoning:** *"This is actually useful for coding scenarios even though not code. It
defines the controls, checks, etc which are applicable."* The four intervention controls (Override,
Escalate, Explain, Execution Boundary Control) and the ten-KPI suite transfer to a code-review
pipeline unchanged — override rate, escalation precision, review latency, disagreement tracking,
intervention drift are domain-agnostic oversight measurements.

**Corpus check that made it sole-exemplar rather than merely transferable** (this is the part worth
reusing): `oversight-theater` is modal on only **4 of 128** sweep papers, and only **2** of those
also carry `metrics` — this one and `2KPHQ5IV` (a consensus-layer architecture paper, not a
measurement one). So it is plausibly the **only** corpus paper that operationalizes
theater-detection *as measurement*: *"an extremely low override rate may indicate rubber-stamping;
an extremely high OR may suggest weak model performance."*

**Generalizable test for §30, extracted:** transferability alone is not enough — nearly any
general-AI governance paper "could apply to code." What clears the bar is **transferability +
scarcity**: run the corpus count for the theme/facet combination the paper uniquely supplies. If
something else already covers it, demote; if the corpus would lose the capability, keep.

**Scope flag is retained on a kept-core paper, deliberately.** `general-ai` here works the way
`general-code` is documented to — *"the audit trail for kept-core transfers."* It records that the
mismatch was seen and overridden, rather than missed. Reporting queries that need coding-specific
papers can still exclude on the flag.

**Also noted:** `design-only` applied with a caveat from the arbiter — *"It doesn't read like a
design, it is more of an enumeration of things to do / requirements than a pure design, but serves
as checklist."* It clears the buildable-detail bar via named controls plus metric definitions. A
reminder that `design-only`'s population includes requirement-enumerations, not only architectures.

## 54. Steering exclusion — the turn-over-turn rule (CI93QRUH, 2026-08-23)

**Arbiter ruling:** *"There is nothing that provides for the turn over turn behavior. It is more of
explaining what is being suggested in a turn."*

**Rule:** steering requires shaping the artifact **across turns** — an ongoing human↔AI loop that
develops the output. **Within-turn** explanation of, or selection among, what the model has already
produced is **not** steering.

This restores the arbiter's own working definition of steering (*"an ongoing interaction between
human and AI to develop the artifact rather than autonomous operation"*) into the instrument, which
previously described steering only in terms of *what* is controlled (inputs, prompts, specs,
context) and said nothing about **time**. The temporal condition is what discriminates the hard
cases.

**Worked case — `CI93QRUH` (HiLDE).** Highlights critical decision points in an LLM code completion,
displays local alternatives derived from top tokens at the current step, **explains the differences
between them**, and lets the programmer select one. **7 of 9 panel runs proposed `steering`** —
wrong. There is no iterative loop; the human reads an explanation and picks, within one suggestion.
Rejected → `cal:human:reject:facet:steering`.

Corroborating: the paper positions itself explicitly *against* steering — its stated motivation is
that *"programmers lack the agency to effectively control LLM behavior, relying on vague
prompt-tuning."* Prompt-tuning is the steering exclusion; HiLDE offers decision-point review as the
alternative to it.

**Consequence for disposition:** with steering off, the steering-only demote route closed, and the
paper was demoted on separate grounds — see below.

### 54a. §53 test reused, and it cut the other way (first negative application)

`CI93QRUH` was weighed for the §53 keep test: *transferability + scarcity*. The arbiter's
keep-argument was that the explanation mechanism "could be used in other, agentic contexts."

**Corpus check:** `oversight-explanation` is modal on **30 of 128** papers — one of the largest
themes. **13** are also `built-system` (so HiLDE is not unique even among built explanation tools),
and **19** are also `agentic` — the corpus already holds substantial explanation work *in agentic
contexts*, which is exactly the ground HiLDE would have to be extrapolated into.

**Demoted.** Nothing is lost. Contrast §53 (`9MV2IVNU`), where the equivalent count was **2 of 128**
and the corpus would have lost a capability.

**The asymmetry that makes the test principled:** "could be used in agentic contexts" is a claim
about **potential**; the 19 agentic explanation papers are **actual**. *Potential does not compete
with actual for scarcity.* Worth reusing — it is the sentence that resolved this cleanly.

Also notable: this is the first time the §53 test produced a **demote**. A keep-test that only ever
says keep is not a test.

**Docs updated:** `Tag_Cheatsheet.md` steering-exclusion preamble. Not propagated to
`Tag_Prompt.md` (§41) — but flagged as a **machine-error** fix (7/9 wrong), so it belongs in the
successor prompt alongside §50.

## 55. The directness / tangency test — what actually drives the Core/Context call (2026-08-23)

Articulated by the arbiter after a run of demotes that the written §3 bar did not cleanly explain.

**The test, in the arbiter's words:** *"Does it have to do about oversight, scaling oversight, or a
practice that directly applies? Then keep in core. If tangential to that, then context."*

**The specific weakening it names:** *"An empirical finding about underlying tech (LLM as code
review) doesn't directly contribute to the scalable human oversight. **Code review is a separate
topic we are taking as a given.**"*

That is the sentence the written bar was missing. §3 requires "(1) directly about scalable human
oversight… AND (2) an operationalizable mechanism, measurement, framework, or empirical finding."
A capability benchmark can satisfy **(2) completely** — sound method, real result — and still fail
(1). The bar named the ingredients but not the failure mode; **tangency** is the failure mode.

**The positive pole makes it usable.** Scaling oversight *is* **allocating finite human attention**,
so findings on **risk identification, prioritization, routing** are directly on-question. Arbiter:
*"A finding on risk identification or prioritization would tie in more directly."* Findings on
whether the underlying technology **can perform the task** are upstream — this review presupposes
code review rather than studying it.

| Directly on-question | Tangential |
|---|---|
| where to look · what to prioritize · how to allocate review · how the human exercises judgement | whether the underlying tech is *capable* of the task |

### 55a. NOT categorical — judge on coverage, not genre

**Arbiter's guard:** *"Consider as contribution to scalable human oversight is not a given. Case by
case based on what is covered. If the code reviews, for example, include risk ratings and oversight
explanation, then it might be a keeper. Just establishing LLM capability to do reviews, less so."*

This matters at scale: `ai-review` is modal on **33 of 128** papers, and a categorical
capability-exclusion would over-demote a large slice of them. A capability study that *also* carries
risk ratings, prioritization, or explanation support is core-eligible, because those bear on
allocating and exercising attention. **Same failure mode as the §38 `framework` widening in reverse:
do not convert a good discriminator into a blunt population-level rule.**

### 55b. Two failure modes of tangency

1. **Wrong topic — capability only.** The *evaluator family*, all demoted for the same reason:
   `WBS9U5N7` (spec-gaming evades holistic eval) · `UDVHQ5HR` (LLMs failing to verify against NL
   specs) · `BAWCBT9R` (auditing LLM-as-judge bias) · `PR4GS7SP` (ACCA correctness oracle) ·
   `8KJEKBGT` (LLM vulnerability/functionality assessment). Five papers, methodologically sound,
   collectively answering "does the evaluator work?" — a question upstream of the review.
2. **Right topic, peripheral treatment.** `TJH7QFAX` (Borg) contributes a genuine prioritization
   signal — CodeHealth predicting AI-modification success, framed by the authors as guiding "where
   additional human oversight is warranted" — but as a stated implication, not the paper's focus.
   Demoted. **The positive pole is not a keyword trigger: mentioning prioritization is not
   contributing to it.**

### 55c. Theme membership ≠ tier (third independent axis)

Earning a theme does not make a paper Core. `ai-review`'s definition explicitly includes *"its
reliability limits"*, so capability and reliability studies **are** `ai-review` by definition and
still fail the directness test. That is why it is simultaneously the corpus's **largest theme
(33/128)** and its **most demoted** — and why the panel keeps proposing keeps on this class.

Third such axis needing explicit separation, each of which caused real confusion today:

| Axis | Confusion prevented |
|---|---|
| tier vs **evidence strength** (§36b) | `design-only` is a rung, not a demerit |
| tier vs **dissertation value** | Context papers can be dissertation-central (`TJH7QFAX`, `RNDPW7VA`, `LGZXFLSJ`) |
| tier vs **theme membership** (§55c) | earning `ai-review` does not make it Core |

**Docs updated:** `Tag_Cheatsheet.md` — both rules inserted immediately **above** the demote-flag
list, since they gate it. Not propagated to `Tag_Prompt.md` (§41).

## 56. `counterpoint` DEPRECATED for polarity inversion; `scaling-dissent` created (JVWUYDME, 2026-08-24)

**The finding, in the arbiter's words:** *"What gets me is that this paper is arguing for our thesis,
yet we called it counterpoint."*

`JVWUYDME` (Jessee, *Scapegoat-as-a-service*) argues **for** the review's thesis — that oversight
should shift from per-item review to command authority over routed exceptions. **All 9 panel runs
tagged it `counterpoint`**, the opposition marker. Not a split, not a coin flip: unanimous and
confidently backwards.

### 56a. The defect is polarity inversion, not ambiguity

The written definition asked only *"does it argue against a prevailing position?"* — and Jessee
plainly does, against HITL-as-practiced. It **never asked which position**, so a paper opposing *bad
oversight* scored identically to one opposing *oversight itself*.

**This is worse than a noisy tag.** If the discussion ever reports "N papers dissent from the scaling
thesis," `counterpoint` as applied yields a **false claim** — papers arguing *for* better oversight
counted as arguing *against* scaling it. Reportable-statistics defect, not a tagging annoyance.

**Corroborating symptom:** proposed on **35 of 128** papers, only **6 unanimous**, **29 split — 82%
of touched papers**, among the worst agreement rates in the instrument (§40b). That is the signature
of a near-unfalsifiable predicate: almost every paper argues against *something*.

### 56b. Replaced, not redefined — the `dissertation-input` lesson applied

`counterpoint` is **deprecated**, not narrowed. Redefining a tag that already carries 35 applications
would leave old and new data meaning different things with no way to tell them apart — exactly the
collision that `dissertation-input` produced (177 items from an earlier `dissertation-*` pass
colliding with a new human-only definition). Legacy applications stay put and are explicitly marked
**never to be read as scaling dissent**.

### 56c. `scaling-dissent` — definition and the guard that makes it work

> The paper argues delegation of oversight is **unworkable or impermissible as a general matter**.

**Polarity guard (arbiter):** *"Our thesis is that many things can be delegated, some can't. That's
risk routing."* A risk-graded delegate/don't-delegate line **is the thesis**, however conservatively
drawn. This is the clause that stops `oversight-theater` papers flooding in and recreating
`counterpoint`'s 82% problem under a new name.

**Three calibration points, two from the corpus:**

| | Claim | Verdict |
|---|---|---|
| **Thesis** | delegate broadly, route exceptions to a human — a *graded* line | `risk-routing` — **`JVWUYDME`** |
| **Approaching dissent** | this class of work is *categorically* off-limits to AI | closer — **`WUUDHL8R`** ("Unacceptable risk… Therefore AI-Driven Refactoring cannot be used here") |
| **Dissent** | the line can't be drawn reliably · review-everything is the only defensible posture · oversight cannot scale | `scaling-dissent` |

**Discriminator: graded vs categorical.** `WUUDHL8R` stays a *boundary annotation* rather than an
instance on two counts — its bar derives from a **misreading** of Art. 5 rather than an argument,
and it concerns *tool usability*, not whether human oversight can scale. An artifact, not a position.

**`JVWUYDME` is the sophisticated near-miss** and the more valuable calibration point: asserting an
*irreducible human authority* reads like a limit on scaling but is in fact the routing claim.
Recorded as `cal:human:reject:facet:scaling-dissent` so the negative is machine-findable.

### 56d. Consequences

- **Standing review practice:** whenever the panel proposes `counterpoint`, **surface the
  `scaling-dissent` question for discussion** — it is a trigger, never a mapping.
- **Added to the deferred restricted panel re-run** (§37c/§41) alongside `agent-panel` /
  `cross-model` / the `evaluated-*` pair — `scaling-dissent` needs corpus-wide application to be
  countable.
- **The other 5 unanimous `counterpoint` papers** (`E689ZAXC`, `EB49Q8QM`, `ID7IN65K`, `P837LJWE`,
  `TA6GIUK2`) join the §45 retrospective list; same polarity risk on each.
- **Expect scarcity.** If the corpus-wide pass returns near-empty, *that is the finding* — "no
  substantive dissent from the scaling premise" is a legitimate result, not a failed tag.

**Docs updated:** `Tag_Cheatsheet.md` — `counterpoint` marked deprecated in place; `scaling-dissent`
added beside it. Not propagated to `Tag_Prompt.md` (§41).

### 49b. `framework` — conformance requirement ≠ architecture (Jessee, Eze; 2026-08-24)

Fifth `framework` refinement, and the one that explains the previous four misfires.

**Arbiter ruling:** *"He is enumerating principles of a system, but it hasn't been built… framework as
software ready or designed to be used, and defining process or principles informing process, are
different. I think this lands on the latter."*

**Rule:** a **conformance requirement** — a spec of what a system must *produce*, abstracted from how
it is built — is **not** a framework, however technical its vocabulary. Note this is *not* the
built/unbuilt axis (§39 already settled that a merely-proposed pipeline architecture **is** a
framework, +`design-only`). The axis here is **requirement vs design**.

**The tell: the paper declares its own platform-independence.** Jessee (`JVWUYDME`) states it
outright — *"In regulated environments, 'control' cannot depend on bespoke dashboards or idealized
tooling. **It must be definable independently of any specific UI, vendor, or platform.**"* MV-HIC
then lists four artifacts a system must be able to emit before acting (Intent · Inputs/Provenance ·
Constraints/Policy References · Action Preview as a deterministic dry-run payload), and §8.1 frames
it as *"a necessary but not sufficient condition."* That is a standard, not a design.
→ `design-only`, **`cal:human:reject:facet:framework`**.

**Applied identically to Eze (`9MV2IVNU`)**: the ten-KPI suite specifies *what must be measured*, not
an architecture. → `cal:human:reject:facet:framework` (panel had it 5/9).

**Assistant-error note, third of the same family.** I recommended *for* `framework` on Jessee after
grepping "technical evidence standard", "integration layer", "deterministic payload" — reading
**technical vocabulary as technical artifact**. Same shape as reading `framework` and `agentic` by
their names (§38, §47). The instrument's scoping clauses, not the paper's register, are the operative
text. **Guard: when a candidate `framework` paper uses architectural language, check whether it
specifies components or specifies obligations.**

**Consolidated `framework` decision path** (§39 · §49 · §49b): pipeline architecture, built →
`framework`+`built-system` · pipeline architecture, proposed → `framework`+`design-only` ·
**conformance requirement / obligations spec → `design-only`, no `framework`** · process or
org practice → theme only, no `framework` · single task at one lifecycle stage → no `framework`.

## 57. Method facets — instrumentation ≠ contribution; one event, one classification (Karuppuchamy, 2026-08-24)

**Arbiter:** *"Not sure about mining. They built a system and used it for building prod services.
Primary artifact was not from mining repos to see what types of changes were made. They did mine
CI/CD logs for before/after analysis."*

**Rule:** logs and telemetry used to **measure** something else are the *instrument*, not the
evidence event. `method-mining` requires the artifact analysis to **be** the finding.

The instrument already implied this — *"a detector run over real repos gets `method-mining` only if
the findings **characterize the repos**"* — but stated it only for detectors-over-repos, so it did
not reach a deployment measured via CI/CD telemetry.

| | Evidence event | Tag |
|---|---|---|
| **Instrumentation** | logs/telemetry measure a deployment's effect | `method-field-study` |
| **Contribution** | the artifact analysis *is* the result — `NZJST99D`, 33k PRs characterised | `method-mining` |

**Corollary — one evaluation event gets ONE method classification.** Two method facets require two
genuinely *separate* measurement events (§34's fork logic, `NRVQT89E`: a critic-model run graded by
contractors **and** a distinct human-subjects tampering task). Never one event measured by two
techniques.

**Worked failure — `8MXATG38`:** `method-field-study` **+** `method-mining` **+** `method-self-report`
all proposed **3/3** on what is a *single* longitudinal field deployment at one organisation, measured
via a telemetry dashboard. The panel read three *techniques* as three *methods*. Resolved to
`method-field-study` alone; the other two rejected. `method-self-report` fails for the same reason —
"resolving early feedback (prompt tuning, policy refinements)" is deployment iteration, not elicited
data.

**Why it matters beyond tidiness:** method facets are how the corpus will report its evidence base.
Triple-counting one deployment inflates the apparent volume of empirical work — "N papers with field
evidence, M with mining evidence" would double-count the same study.

**Also recorded from this paper:** `adopted` is one of the scarcest facets in the corpus — **5 of
128** (`8MXATG38`, `BU73N7PC`, `P837LJWE`, `RX9SICP9`, `V4IRKSFI`). Karuppuchamy clears the §36
pilot rule explicitly: the paper says *"prior to **adoption**"* and describes a phased rollout ending
in *"broad enablement through standard plugins, CI jobs, and issue-tracker automation"* — past the
study pilot into the organisation's own operational use.

**Docs updated:** `Tag_Cheatsheet.md` method-facet block. Not propagated to `Tag_Prompt.md` (§41) —
but this is a **machine error** (3/3), so it belongs in the successor prompt alongside §50 and §54.

## 58. Contributes-mechanisms vs organises-existing-mechanisms (Khoo vs Eze, 2026-08-24)

**Arbiter, on `5AVZQCVU` (Khoo):** *"E.g. Elgendy shape."*

**Test:** does the paper contribute **the mechanisms**, or **a structure for organising mechanisms
that already exist**? The latter is real work, but it lands Context unless the *structure itself* is
scarce.

**Worked contrast, both decided today:**

| | Contribution | Verdict |
|---|---|---|
| `9MV2IVNU` **Eze** | the **instruments themselves** — Override Rate, Override Directionality, Escalation Precision, Intervention Drift, each newly *defined* with a measurand | **Core** (§53: `oversight-theater`+`metrics` = 2 of 128) |
| `5AVZQCVU` **Khoo** | a **risk register + control catalogue** over controls that are borrowed security hygiene — *"implement input guardrails," "escape filtering before including web content in prompts," "use structured retrieval APIs rather than web scraping"* — and the paper calls its list *"tentative"* | **Context** |
| `WH2PIBNQ` **Elgendy** | Figure 1 workflow model, Table 1 modalities, Table 2 technical attributes — an arrangement of known practice | **Context** |

**Why this needed a separate test.** Khoo is *not* unactionable — it tiers controls by criticality
(Cardinal / Standard / Best Practice), maps capabilities to risks, and defines residual-risk
assessment. Judged on "is it operationalizable?" it passes. The demote turns on **whose mechanisms
they are**. Recording this so the audit trail does not say "not actionable," which the tiering would
falsify.

**Relationship to §55:** this is the *positive-pole* refinement. §55 says findings on risk
identification and prioritisation tie in directly — Khoo *does* prioritise. §58 adds that
prioritising **someone else's** controls is an organising contribution, and organising contributions
need the §53 scarcity test like any other transferable-but-crowded work. `org-governance` is modal
on **31 of 128**, so the structure is not scarce.

## 59. Panel failure mode — vocabulary matching, not mechanism reading (consolidated, 2026-08-24)

Scattered across §47, §49b, §50 and §57; consolidated here because it is **the single highest-value
input to the successor prompt** (§41) and because every instance is a *machine* error, not an
arbiter clarification.

**The pattern: the panel matches words in the paper to words in tag names, without checking what the
mechanism does.**

| Trigger word | Wrongly fired | Corpus instances |
|---|---|---|
| "agent" | `agentic` | `WBS9U5N7` (Mutator = apparatus, 9/9) · `ZH6QIU8A` (helper agents, assistive, 9/9) · `8MXATG38` (helper agents, 2/3) |
| "test suite" | `rules-based-checks` | `ZH6QIU8A` (tests are a *representation* of a decision, 9/9 — violates the plumbing rule's own worked example, "agents running test suites ≠ `rules-based-checks`") |
| "survey" | `survey-input` | conflates *the paper ran a survey* with *the finding is useful to the org survey* |
| multi-model panel in the **methods** | `ai-review` | `ID7IN65K` (3/3, reading the methods section as content — §50) |
| logs/telemetry as instrument | `method-mining` | `8MXATG38` (3/3 on a single field deployment — §57) |
| "framework" / "evidence standard" / "integration layer" | `framework` | `JVWUYDME` — *assistant* error, reading technical vocabulary as technical artifact (§49b) |

**Inverse failure — vocabulary absent, mechanism present:** `ZH6QIU8A` carries a **Decision Bank**,
explicitly *"a persistent, editable record"* with decisions *"traceable to code"*, and the panel
proposed `provenance-auditability` **0 of 9**. It reads labels, not function, in both directions.

**Concentration:** `ZH6QIU8A` alone produced three keyword misfires plus the inverse miss — four
vocabulary errors on one paper.

**Implication for the successor prompt:** the current prompt lists tag definitions. It does not
instruct the model to **identify the mechanism first and only then match it to a tag**. Every fix
above (§47 apparatus-vs-object, §50 method≠contribution, §57 instrumentation≠contribution, the
plumbing rule) is a special case of that one instruction. **Consider a single explicit step: "state
what the mechanism does in your own words before assigning any tag."**

## 60. `steering` — the three-case discriminator: contribution vs plumbing (2026-08-24/25)

Three papers in two days drew `steering` proposals from the panel and got three different arbiter
answers. The rulings are consistent, but only under a discriminator the instrument did not state:
**§54's temporal rule settles one case; "contribution, not topic" settles the other two.**

| Paper | Panel | Ruling | Operative reason |
|---|---|---|---|
| `CI93QRUH` HiLDE (Vasconcelos-adjacent) | 7/9 | **reject** | §54 — *within-turn* selection among what the model already produced |
| `JCTP8VXP` Zoro (Ma et al.) | **9/9** | **reject** | rule injection is **plumbing for enforcement**; the contribution is the CLI gate |
| `C88VGWMI` Marri | **9/9** | **ACCEPT** | strip the enforcement and injection **is** the contribution — nothing else is there |

**Why §54 does not decide the last two.** §54 excludes *within-turn* explanation/selection and
requires shaping "across turns." Both Zoro's constitution-style rules and Marri's constitution
persist across the whole development process, so both clear the temporal bar. The temporal rule was
written for HiLDE and does not discriminate the spec-driven cases at all.

**The rule that does — already in the facet text, never applied as the primary test:** steering
fires when generation-shaping is *"a **substantive part of the contribution** — NOT any incidental
prompt-shaping component every AI system has."* Applied:
- **Zoro** — arbiter: *"It describes a mechanism to set rules constraining what the LLM can do…
  In the scenario given, that was steering… but it could be enforcing a process, checklist, etc. too
  in pure agentic."* The rule *content* is user-supplied and arbitrary; the contributed machinery is
  `zoro-cli` refusing `update-step` until proofs exist. Steering is what the plumbing carries, not
  what was built. **Reject** — despite 9/9 and despite the paper's own §8.1 using the word
  ("**Steering** agent behavior through explicit, enforceable, and evolvable policies…"), which is
  almost certainly what drove the unanimity (§59 vocabulary matching).
- **Marri** — the Constitution is *"not prescriptive about implementation technology; it specifies
  what must hold, not how to achieve it."* No gate, no checker, no executable enforcement anywhere
  (see §61). What remains is a structured document injected into the generator's context. Arbiter:
  *"just injecting 'don't do that' to the prompts."* That is the contribution. **Accept.**

**Test to reuse:** *if the enforcement machinery were removed, would anything remain?* If yes, the
prompt-shaping was plumbing (reject). If the injection **is** what remains, it is the contribution
(accept). Expect this on every spec-driven / rules-file paper; the class is growing.

**Docs:** `Tag_Cheatsheet.md` steering entry needs the discriminator added at closeout — the current
text carries the "contribution, not topic" clause but buries it behind the §54 temporal preamble,
which is why all three cases had to be argued from scratch.

## 61. `framework` — §49b's second application, and the enforcement-gap observation (`C88VGWMI`, 2026-08-25)

**Panel 9/9 `framework`; arbiter rejected.** Second clean application of §49b
(conformance-requirement ≠ architecture), and the tell fired exactly as written — *the paper
declares its own platform-independence*:

> *"A constitution is **not prescriptive about implementation technology; it specifies what must
> hold, not how to achieve it**."* · *"The methodology is **domain-agnostic**."*

Same shape as Jessee/`JVWUYDME` MV-HIC. §49b is now two-for-two and can be treated as reliable.

**Full-text check on where enforcement lives — it doesn't.** Arbiter asked directly whether the
paper says *how* the guardrails are enforced. It does not:
- The **"Validator"** appears once, as a box in an ASCII architecture figure, never described in prose.
- **"Machine-readable"** means the constitution is *structured* (CWE mappings, MUST/SHOULD/MAY per
  RFC 2119). Nothing in the system machine-*reads* it.
- The **Compliance Traceability Matrix** is the strongest automation claim — *"principle to
  implementation artifacts at file and line-number granularity, **enabling** automated compliance
  verification."* Enabling, not doing; Table 1 is hand-authored and the stated purpose is
  *"Audit Support, where **auditors can verify**."*
- The only executable enforcement in the paper is **Pydantic field validators** in the demo app —
  ordinary input validation that happens to satisfy principle SEC-006, not a check of the constitution.

Actual pipeline: **constitution → context for the generator → human-authored matrix afterward.** The
paper's central claim, *"secure by construction rather than by post-hoc verification,"* is therefore
unearned: prevention here is better prompting, and there is no construction-time check.

**Disposition — Context (§53).** Not tangency: transferability is fine. **Scarcity fails.** Marri and
`JCTP8VXP` (Zoro) occupy the same axis — structured rules constraining AI generation — and Zoro ships
a CLI that rejects commands plus executable tests. On the shared axis Marri is dominated. Arbiter:
*"Not enough meat in the discussion for others to use."* Third negative application of §53 (after
§54a), which continues to make it a real test rather than a keep-rubber-stamp.

**Worth carrying forward — an unwitting instance of the §A enforcement gap.** `HOS_Seeded_Theme_Candidates`
§A records *"the gap is enforcement, not knowledge — orgs don't lack oversight policy, the policy is
documented but not mechanically enforced."* Marri writes policy in deliberately machine-readable form,
claims construction-time enforcement, and never builds it. That is the gap appearing **in the
literature** rather than in an audit. **Example-grade, not evidence-grade** — the paper does not
reflect on its own missing enforcement, so it instantiates the gap rather than reporting it; cite it
as an illustration, do not synthesise from it. This distinction is why Context is the right tier even
though the observation is valuable.

**Other calls:** primary `ai-code-insecurity` (arbiter: *"This one is all about improving security"*),
overriding a genuine 3-way panel split (`provenance-auditability` 4 / `ai-code-insecurity` 4 /
`org-governance` 1 — no modal winner, a tripwire in itself). `regulatory-compliance` **kept** (7/9)
against an initial §44 lean, on CWE/PCI-DSS/GDPR mapping plus audit support as a stated purpose.
`method-experiment` (5/9) rejected — the §35 gold pass already ruled `evaluated-synthetic`, and §34's
fork forbids both for one event.

## 62. `agent-scope-drift` — tag by the OBJECT of the drift (Zhu vs Zoro, 2026-08-24)

The panel proposed `agent-scope-drift` on two consecutive papers; the arbiter accepted one and
rejected the other. Same word, different object — and the definition already says *"tag by the
mechanism's **object**, not the actor's motivation."* Extended: **also not by the word.**

- **`ZGST9CY6` (Zhu) — REJECT.** Its drift machinery is *"versioning, drift detection, and abstain
  mechanisms"* over *"significant drifts in system behaviour that occur even without explicit
  re-training,"* with *"drift detection precision/recall"* as a sample metric. That is **model
  behavioural drift** — a statistical property of the system over time. Nothing wanders off-mandate.
- **`JCTP8VXP` (Zoro) — ACCEPT.** *"Codex **pauses mid-execution and asks** Johnny whether gray is
  an acceptable default colour… a rule that might normally **go unnoticed**,"* marked strict because
  the user *"does not want Codex **quietly choosing a colour**."* Plus the CLI halt on unproven
  rules. That is **an agent making unreviewed decisions outside its mandate**, and mechanisms that
  bound it — the theme as defined.

**Rule:** `agent-scope-drift` requires *an agent departing from intent*. Distribution/behaviour drift
of a model is **not** this theme, however prominent the word "drift" is in the paper. Panel proposed
it 1/3 on Zhu and 3/9 on Zoro — weak signals both times, so the tag is not reliably machine-detected
in either direction; expect to rule it by hand.

## 63. `remediation-gating` — §4 refined: a gate counts when it drives an autonomous fix (`JCTP8VXP`, 2026-08-24)

**Assistant recommended reject citing §4; arbiter overrode, and the override is correct.**

§4 records an over-tagging: VibeGuard (`T8E8SCCG`) drew `remediation-gating` from a human *and*
Opus and should not have. The assistant read §4 as a blanket caution against gates and applied it
to Zoro's CLI. §4's actual reason is narrower — VibeGuard is *"a detect/publish gate with **no
auto-fix**."*

Zoro differs on exactly that fact. The definition's process-gate list already includes
*"stop-progression, fail-closed,"* and there **is** an autonomous fix being governed:

> *"Codex is forced back to handle the migration. It **generates a backfill script** for all
> existing LogEntry records, **runs a unit test to verify it**, and submits proof."*

No human in that loop. **Accept.**

**Refinement to §4 (binding):** a fail-closed gate earns `remediation-gating` when it **drives an
autonomous remediation**; it does not when it merely blocks publication and hands back to a human.
The discriminating question is *what happens after the gate fires* — not whether a gate exists.
§4 should be read with this attached; on its own it reads as a blanket exclusion and was applied as
one.

## 64. `counterpoint` polarity inversion — second measured instance; and §52's first clean negative (`59ZW4R58`, 2026-08-24)

**§56 second instance.** Maes drew `counterpoint` **8/9** — another thesis-*supporting* paper read as
opposition, after Jessee/`JVWUYDME` at 9/9. Two independent high-consensus misfires on papers arguing
**for** engineered oversight promotes the failure mode from observed to **measured**. The panel is
reading *register* — "gotchas," "goes against the trend," a pessimistic tone — as *polarity*.

Maes's actual argument arc is the dissertation's own: generation scales → safety requires rigorous
human verification → verification erases the productivity gain and excludes non-programmers →
*"**Therefore, there would be value to now automate such frameworks**"*; §7.6: *"they are **not
automated yet**… In an upcoming paper, we will describe an **automated, and somehow autonomous,
implementation**."* Under §56's guard — dissent requires delegation being unworkable or impermissible
**as a general matter** — this fails the test exactly as Jessee did. Rejected.

### 64a. §52's first clean negative application

Maes was weighed for `oversight-scaling-inversion` (panel 4/9) and **declined**. The assistant
initially argued for it; the arbiter pushed back — *"indirectly acknowledging it… but I don't think
it is direct enough"* — and a full-text search settled it:

- *"huge amount of code"* appears **once**, in framing, never connected to review capacity.
- **No** bottleneck / backlog / throughput / keep-up language anywhere in ~7,000 words.
- "Scale" appears once more meaning the *built system* is unscalable — a different sense entirely.

What the assistant had read as the inversion — *"they now must perform rigorous code verifications"*
negating the productivity gain — is a claim about **cost per item**, not **volume exceeding
capacity**. §52's narrowing exists precisely to stop the tag firing on any paper observing that
oversight is expensive, and it worked. **This is the narrowing discriminating rather than merely
restricting** — worth recording next to §54a as evidence the fail-open scoping is load-bearing.

**Consequence — a second scaling mechanism logged, not tagged.** Maes argues AI code is *less
reviewable per unit*, so oversight cost rises at constant volume. Distinct from T0's volume
mechanism and multiplicative with it. Recorded as a WATCH ITEM in
`HOS_Seeded_Theme_Candidates` §A with a promotion tripwire (a second paper making per-item
reviewability decline its own mechanism), explicitly **not** as an `oversight-scaling-inversion`
instance. A third candidate mechanism surfaced the next day — detector false-positive volume
defeating triage (alert fatigue), with two instances already (`ZGST9CY6` Zhu, `R9CDT9KB` Mahmud) —
and belongs in the same watch item.

## 65. Lit-review themes require FOCAL synthesis — a mechanism inventory earns nothing (`4AXDVW7J`, 2026-08-25)

**Panel 9/9 `rules-based-checks`; arbiter rejected on a full-text check.** The largest unanimous
override of the Light Read pass, and the second 9/9 override in two papers (after `framework` on
`C88VGWMI`). Both were caught the same way: by reading past the vocabulary to what the paper does
with it.

Arbiter: *"No to rules based check. I didn't see anything. It was more of a design and what's
important to check."* Verification found the terms present but framed as survey material:

> *"**Recurring mechanisms.** At interaction time, typical SE pipelines combine a small set of
> mechanisms: prompt and response schemas, repository-grounded retrieval with scoped access, and
> **verification passes (for example, tests, linters, licence checks, or safety filters)**"*
> *"This is a **descriptive inventory of interaction-time mechanisms observed in SE practice**."*

Two occurrences, both inside an example list, inside an inventory of what other people already do.

**Rule (extends §58 to secondary literature).** A `lit-review` earns a **theme** only on **focal
secondary synthesis** — the review must gather, compare and draw conclusions from evidence *about
that theme*. **Enumerating a mechanism in a catalogue of practice is not focal synthesis.** The
existing instrument already says this for the `risk-*` flags (*"lit-reviews CAN earn these flags via
focal secondhand synthesis… passing enumeration still never fires"*); this entry states that the same
bar governs **themes**, which was implicit and had never been applied as a test.

**Why the panel missed it.** §59 vocabulary matching. "checks", "linters", "verification passes",
"safety filters" all appear; a label-reader sees the theme. The discriminator is *whose* mechanism
and *what the paper does with it* — the same object-vs-apparatus family as §47 and §50, here applied
to survey content rather than research machinery.

**Watch consequence:** inventory-style reviews are a recurring shape in this corpus (roadmaps,
capability models, SE2030-style agenda papers). Expect high-consensus theme proposals from them that
reflect the *inventory's* coverage rather than the *review's* argument. Check the framing sentence
around the term before endorsing.

## 66. `metrics` — naming what to report is not defining a metric (`4AXDVW7J` vs `59ZW4R58`, 2026-08-25)

**Panel 3/9 `metrics`; the assistant argued FOR it and the arbiter rejected.** Arbiter: *"it
enumerated things important to check, but not sure that it rose to the level of metrics."* Correct,
and the pair of papers gives the boundary a clean worked contrast.

- **`4AXDVW7J` (Migliarini) — NO.** Delivers *"harmonized evaluation constructs and a **reporting
  kit** that co-reports utility with ethical compliance, robustness to prompt perturbations,
  traceability from constraints to output spans/tool calls, and sustainability overhead with full
  configuration disclosure."* Every item names a **dimension to report**. Nothing is computed: no
  formula, no index, no threshold, no aggregation rule.
- **`59ZW4R58` (Maes) — YES.** Ships `CEI = α·C_cyclomatic + β·D_naming + γ·S_structural`, an
  `AGDV_Score` function with explicit weights (0.4 coverage / 0.3 readability / 0.3 consistency), and
  `M_understanding ≥ T_threshold`. Computable, with stated parameters.

**Rule:** `metrics` requires a **defined measurement procedure** — an index, formula, score,
threshold, or aggregation the reader could apply to produce a number. **A list of dimensions worth
reporting is a reporting framework, not a metric**, and belongs to the paper's theme(s) plus (where
the form fits) `design-only`. The existing definition's *"defines metrics/scores/indices as a
deliverable"* wording was read too loosely — "as a deliverable" was carrying the weight, when the
operative word is **defines**.

**Note the near-miss both ways.** A reporting kit is genuinely deliverable-side and genuinely
reusable, which is what makes it tempting; and Zhu's per-pattern "Signals to track" lists sit on the
same line — they were accepted there because Zhu pairs them with computed quantities (veto precision,
audit reversal rate, drift detection precision/recall) rather than with dimension names. Where a
paper offers only dimension names, the honest tag set is theme + `design-only`, with the reporting
guidance captured in the rationale.

## 67. `formal-methods` may be PRIMARY when the technique is the subject; `built-system` needs the core mechanism to run (`6ZW9QNQH`, 2026-08-25)

Two rulings on Mitchell & Shaaban, *Position: vibe coding needs vibe reasoning* (LMPL '25), plus an
assistant error worth recording because it repeats a pattern.

**(a) `formal-methods` as primary — the advocacy case.** The instrument reads
*"[technique, COMPOSABLE] … **Pair with the performer**: AI does it → `ai-review`+`formal-methods`;
classical engine → `rules-based-checks`+`formal-methods`; no performer (pure advocacy/position) →
`formal-methods` + the `intro-framing` facet."* The assistant applied the second clause and proposed
`rules-based-checks` primary, since Mitchell's verification is *"lightweight syntactic checks and
compilation success"* — a classical engine — and 4 of the corpus's other 6 `formal-methods` papers
sit under `rules-based-checks`.

**Arbiter overrode to `formal-methods` primary, correctly.** The pair-with-the-performer rule governs
papers that **use** the technique. Mitchell's **subject is the technique** — it argues formal methods
are the answer to vibe coding's constraint-contradiction problem, and the performer is a deliberate
stub with real verification deferred to *"future implementations."* That is the third clause's
advocacy case in all but name.
**Rule:** *pair with the performer when the paper **uses** formal methods; `formal-methods` may be
the home when the paper's **subject is the technique itself**.* The third clause is the tell — where
the performer is absent or placeholder, the technique is the subject.

**Correction to a scarcity claim made the same session.** The assistant reported Mitchell as "the
corpus's only paper with `formal-methods` as primary" and offered it as a §53 keep argument. That was
an artifact of reading panel output, not a property of the paper — and under the ruling above it is
no longer even anomalous. `formal-methods` is 7 of 149; three of those (`E5SQKRH7` Sharma,
`5DI9B43K` Sistla, `72W6R4JG` Töpfer) are **unread**, and Töpfer's title —
*Vibe-coding: feedback-based automated verification* — describes Mitchell's proposal implemented.
**The scarcity test cannot be run on this cluster yet.** See the follow-up item below.

**(b) `built-system` requires the CORE mechanism to run — extends the R4WJZBSF mock-demo rule.**
Panel 3/3 `built-system`; arbiter rejected. There *is* a real prototype: *"a small proof-of-concept
implementation written in TypeScript… we integrated our proposed side-car with Claude Code… via hooks
that run on code changes."* It genuinely executes. But the paper's thesis is **autoformalization plus
formal verification**, and what runs is LLM template instantiation plus *"lightweight syntactic checks
and compilation success."* **The hard part is stubbed.**

The instrument already holds the adjacent rule — *"a mock demo ≠ built: a demo that fabricates the
mechanism's core outputs … is still `design-only`"* (R4WJZBSF). **Extension:** substituting a
**placeholder for the mechanism's core** is the same failure as fabricating its outputs. Ruling:
`design-only` (+ `framework`, which composes for proposed-but-unrun architectures), **not**
`built-system`. Arbiter: *"not even a built system. It is incomplete."*
**Honest counter, recorded so the call is knowing:** the Claude Code hook integration is real and is
arguably the novel contribution, with verification as a swappable backend. Rejected because without
verification the side-car has nothing to say — but a future paper of this shape may deserve the
opposite call.
**Ladder consequence:** no rung. *"Results were promising; for example, the prototype system can emit
the lines in red in Listing 1"* on author-written toy functions is a **demonstration, not a
measurement**; `evaluated-synthetic` requires measuring against self-made material. Matches the
`7SH86C2W` precedent (single self-selected, non-repeated, exploratory scenario → below the rung).

**(c) Assistant error — a false negative reported as a verified finding.** The assistant grepped for
`we (implement|built|prototyp…)`, matched nothing, and stated "verified — it's a position paper with
no artifact and no evaluation." The paper says *"implementation written in TypeScript"* and *"the
prototype system"*, and has an **Experiments** section; the arbiter supplied the text. This is the
same failure as the Zhu `rules-based-checks` call (§65's family): **a pattern search that misses is
evidence of nothing, and must not be reported as a negative finding.** Standing correction: when
checking whether a paper contains X, read the structure — section headings, contribution list — before
concluding absence, and state the search's limits when reporting one.

## 68. Check the paper's OWN definition before tagging on its vocabulary (`RX9SICP9`, 2026-08-25)

**Both arbiter and assistant proposed `agent-panel` on Moreira; it does not apply.** The paper's
central construct is the *Verification Agent*, and it defines the term itself:

> *"**Verification Agent (VA): Any entity capable of evaluating an artifact's correctness.** Two
> types: **VA-automatic (unit tests, linters, compilers** — binary verdict on specific properties)
> and **VA-human (the operator)** — evaluates semantic adequacy, usability, domain correctness."*

The gate table then lists **VA-human** as the primary verifier for phases 0–4. So the paper's "agents"
are deterministic tools and people. `agent-panel` requires multiple distinct **AI** agents; nothing
here is one.

**Rule (generalises §47 and §59):** a term appearing in a paper is not evidence for the tag that
shares its name — **read the paper's own definition of the term first.** §47 covers apparatus vs
object (agents used to *run* a study ≠ `agentic`); §59 covers panel label-matching. **This is a third
case: the paper redefines a common word for its own construct.** The tag vocabulary and the paper's
vocabulary can collide without overlapping at all.

**Watch list — corpus terms known to be redefined by individual papers:** *agent* (Moreira: any
verifier, human or tool), *constitution* (Marri: a policy document, not a governance body),
*side-car* (Mitchell: a verification process, not deployment topology), *framing* (Mitropoulos: a
cognitive-bias attack vector, not problem statement). Expect more; the corpus is young and authors
are coining freely.

**Notable because it is the first tag error the arbiter and assistant made independently and
identically** — the shared cause is that both read a phrase (*"external verification agents"*) rather
than a definition. It is exactly the failure mode §59 attributes to the panel, occurring in humans.

### 68a. `adopted` without a method facet — deployed but never measured (`RX9SICP9`)

A clean worked example of the `adopted` ≠ `method-field-study` rule, and an unusual evidence profile
worth naming.

**`adopted` earned** (9/9, and rare — roughly 5 of 128 sweep papers reach the ladder's top):
> *"applied across **more than 20 projects involving multiple practitioners** at a single R&D
> institution… Internal records document consistent application across these projects."*

**`method-field-study` rejected** (6/9), on the paper's own limitations:
> *"does not establish superiority over alternatives or generalisability"* · *"**L2 — Property 4 not
> empirically tested.** The claim… is intuitive but **unmeasured**"* · *"**L3 — Gate cost not
> measured.**"*

**Ruling: no method facet at all.** Deployment is not measurement. Internal records documenting
*consistent application* evidence that the methodology was **used**, not that anything about it was
**observed or compared**. The method facets attach to an evidence-production event; there wasn't one.

**Why this profile matters for synthesis.** `adopted` + no method facet is the signature of
*practitioner methodology with real uptake and no evaluation* — high on the deployment ladder, absent
from the evidence base. Papers like this should not be counted as effectiveness evidence for SQ5 no
matter how mature their deployment status looks. The rung measures **maturity of use**, not
**strength of evidence**, and conflating the two would systematically overstate the corpus's
empirical footing.

### 68b. `adopted` qualified — deployment status vs verifiability of the deployment claim (`RX9SICP9`, 2026-08-25)

The tag **stands**: Moreira clears the pilot rule (*"outside the research **context**" ≠ "outside the
research **org**"*), because the 20+ projects are the organisation's own operational work, not a study
site — the paper ran no study at all. **What is qualified is the verifiability of the claim, not its
scope.** New tag `evidence:self-reported-unverified`, plus a child note carrying the reasoning.

**Why a scarce tag needs this.** `adopted` is **4 papers among the 48 adjudicated** (panel proposed it
on 8 of 149; the human layer roughly halved it). Ranked by inspectability:

| Paper | Org | Method facet |
|---|---|---|
| Abreu et al., *Moving Faster and Reducing Risk* (`BU73N7PC`) | **Meta**, ICSE-SEIP industrial track | `method-experiment` |
| Karuppuchamy, *AI-Augmented SE* (`8MXATG38`) | **eBay Inc.**, IEEE CCWC | `method-field-study` |
| Takerngsaksiri et al., *HITL SD Agents* (`5VTAJISY`) | Monash + **Atlassian**, ICSE-SEIP | `method-field-study` + `method-self-report` |
| **Moreira, *IACDM* (`RX9SICP9`)** | **name withheld**, records *"not publicly available"* | **NONE** |

The first three name an identifiable employer, publish in peer-reviewed practice tracks, and all
carry a method facet. Moreira is the only one with **neither** an identifiable deploying organisation
**nor** any measurement — and the methodology's author is the person reporting its use.

**So 25% of the corpus's `adopted` set rests on unverifiable self-report**, and it is the same
instance that §68a flags as deployed-but-never-measured. **The two weaknesses coincide**, which is
what makes it worth separating rather than absorbing.

**Rule:** deployment status and **evidential quality of the deployment claim** are a third
independent axis, alongside the two already recorded (tier vs evidence strength, §36b; deployment vs
evidence shape, §68a). Do not let a rung's scarcity substitute for its strength. **Any counted claim
of the form "N papers report production adoption" must exclude this instance or state the
distinction** — in a four-item set one soft member is a quarter of the evidence.

**Not a criticism of the paper.** Its limitations section is unusually candid: L1 names the
single-institution confound, L2 and L3 concede the central properties are unmeasured. The
qualification exists to keep the corpus statistic honest, not because the authors overclaimed.


## 69. `oversight-theater` presupposes a process to be hollow (`E9RAWBDT`, 2026-08-25)

**Arbiter, ruling out `oversight-theater` (panel 3/9):** *"There is no oversight, so there can't be
theatre."*

That is a cleaner statement of the boundary than the live definition carries. `oversight-theater` is
*"review exists on paper but lacks authority/time/info to change the outcome (rubber-stamp, token
HITL)"* — it presupposes **a process that exists and is hollow**. Where no review process exists at
all, the finding is **absence**, and absence belongs to `automation-bias` (over-trust) or
`oversight-scaling-inversion` (capacity), not here.

**Discriminator to reuse:** theater is a process performed **for someone else's benefit** — a
requirement, an auditor, a policy — that cannot change the outcome. A developer *choosing* a cheaper
check to preserve their own flow is **pragmatic substitution**, self-directed, and can still change
the outcome if it fires. Different mechanism, already covered by `automation-bias`.

**Assistant error, recorded because it is the third of its kind today.** I offered as evidence for
theater the line *"not read the original source beyond verifying its existence."* It is a **footnote
by the authors about their own citation practice** (*"Citation taken from Royal [64]; we have not
read the original source beyond verifying its existence"*) — scrupulous of them, and nothing to do
with how developers review code. Same family as §65 and §67(c): **a string matched out of context is
not evidence.** Read the surrounding sentence before quoting a grep hit as a finding.

## 70. First endorsement of `oversight-scaling-inversion` in the Light Read pass (`E9RAWBDT`, 2026-08-25)

Panel 7/9; **endorsed** — the first time the tag has survived arbiter review in this pass, after being
declined on `59ZW4R58` (Maes — cost per item, not volume), `R9CDT9KB` (Mahmud — detector false
positives), `VFNJSZD9` (Hjazeen — detection blindness) and `X7EN6DXZ` (Mitropoulos — subversion of a
working reviewer).

**What earned it — a documented practitioner adaptation, not an assertion:**

> *"extensive code review is itself a pain point: **'My 400-line code is now 3000 lines and neither
> of us can read it anymore'** (R63). Reviewing generated code can be tedious… **As a result, some
> vibe coders recommend delegating review back to the AI by asking it to audit its own code.**"*

Volume outstrips human review capacity → developers hand review **back to the generator** → nothing
human inspects the artifact → it ships. Fail-open, and it passes §52's synthesis test: it would read
naturally in a section on bad code shipping unreviewed.

**Methodological significance:** four rejections and one endorsement, all decided on the same
narrowing, is evidence that §52 **discriminates** rather than merely restricts. A test that never
fires is as useless as one that always does. Pair this entry with §64a (the first clean negative) when
defending the scoping in the write-up.

## 71. The independence failure — practitioners delegate review to the generator (`E9RAWBDT`, 2026-08-25)

Not a tag ruling; a corpus finding worth carrying into synthesis, and the sharpest thing in this paper
for the dissertation's thesis.

**The practice** (their §4.5, from mined posts and interviews):
> *"delegating review back to the AI by asking it to **audit its own code**… 'Once you have finished
> building, take your code and pass it through a leading reasoning model with the following prompt:
> Please review for production readiness: check for common vulnerabilities…' (R41). This strategy
> supports flow by preserving a sense of control while enabling effortless review. **However, it also
> signals high trust in model ability; it is unclear how effective these strategies are compared to
> traditional code review.**"*

**Why it matters.** The design literature in this same corpus prescribes the opposite. Zhu
(`ZGST9CY6`, Table 4) specifies *"divergence detection and independent checker — comparison against a
**second** AI/system, heuristic, or ruleset… flags cases needing verification when solvers disagree;
**avoids blind trust**."* Mahmud (`R9CDT9KB`) routes on **inter-model disagreement** across three
vendors precisely because *"different models exhibit different blind spots."*

**So: practitioners are doing the thing the design literature explicitly warns against** — using the
producer as its own checker, which destroys the producer-independence that makes the check
informative. The corpus contains both the prescription and the measured deviation from it, which is a
stronger claim than either alone.

**Cross-links:** strengthens §B (*the overseer is itself an untrusted, attackable component*) from the
practice side; supplies a mechanism for the `automation-bias` primary here; and is the practitioner
counterpart to `risk-routing`'s producer-independence requirement (*"model self-confidence is
disqualified"*), which turns out to be violated in the field by default.

## 72. §51's reference-oracle exclusion does NOT fire on migration/translation tasks (`27YULT5I`, 2026-08-25)

§51 excludes a checker that needs a known-correct reference implementation, on the stated ground that
*"in real oversight you do not have the reference (if you did, you would not need the generated
code)."* **That rationale fails for one whole task class.**

Sharma (Ronit) proposes *"**differential testing protocols that verify functional equivalence against
original systems**"* for LLM-driven legacy code migration in regulated finance. In migration the
reference is the **legacy codebase** — it exists, it is in production, and equivalence to it is the
actual acceptance criterion, not a research stand-in. The counterfactual §51 relies on ("if you had
the reference you would not need the generated code") is simply false here: you have the COBOL *and*
you need the Java.

**Rule:** §51 excludes reference-oracle checkers **when the reference would not exist in deployment**
(the case it was written for — `PR4GS7SP`/ACCA testing against ground-truth implementations). It does
**not** exclude them for **migration, translation, refactoring, or re-platforming**, where
equivalence-to-source is the oversight mechanism itself. `rules-based-checks` endorsed on that basis.

**Expect recurrence:** legacy modernisation is a major AI-coding use case, and every paper in it will
propose some form of differential/equivalence testing. Check the task class before applying §51.

## 73. `evaluated-real-data` — second instance, and the provenance-vs-curation test case arrives (`5DI9B43K`, 2026-08-25)

The staged rung (see `HOS_Seeded_Theme_Candidates` §E) had **one** confirmed instance and an open
question flagged as having **no test case**. Both change here.

**Second instance.** Sistla et al. (Google DeepMind / Google / Meta) evaluate on *"a **dataset of 20
problems, manually picked**, primarily from two [sources]"* — real MemorySanitizer-detected
uninitialized-variable bugs, plus 20 program-equivalence queries. Real-world-sourced; not a
recognized third-party protocol. Under the live instrument **no rung applies**: `evaluated-benchmark`
requires administering a recognized protocol as-is, `evaluated-synthetic` requires the authors to have
invented the material. Tool-side per §34's fork, so the ladder should apply and doesn't.

**And it is the missing test case.** The open question was whether **provenance** or **curation**
decides. Mahmud (`R9CDT9KB`) was real-sourced with no curation dispute — it did not discriminate.
Sistla is **real-sourced AND author-curated** ("manually picked"), which is exactly the contested cell.
`ZBF86IJM` could not settle it because it has no tool-side event at all.

**The question, stated precisely for the graft decision:** does `evaluated-real-data` require only that
the *material* be real-world-sourced (Sistla qualifies), or also that the *selection* be
protocol-driven rather than hand-picked (Sistla fails)? A curation bar would collapse the rung toward
`evaluated-benchmark`, since protocol-driven selection over real data largely *is* a benchmark. A
provenance-only bar admits hand-picked real bugs, which is weaker evidence than it looks — 20
manually chosen cases is not a sample.
**Provisional lean, not a ruling: provenance decides, and sample size is recorded in the rationale
rather than in the tag.** The rung's job is to say what the system ran *against*; how much and how
selected belongs in the write-up. Revisit at graft with both instances in hand.

**Corpus note:** two instances now, both from strong industrial-research groups, both hand-curated
from real defects. If that pattern holds the rung is describing a real and common evaluation style,
not an edge case.

## 74. `risk-routing`'s producer-independence clause gets empirical corroboration (`VTDG995V`, 2026-08-25)

The instrument disqualifies model self-confidence as a routing signal on principle:
*"Signal must be **computed & producer-independent** — model self-confidence is disqualified."*
Gros, Spiess et al. (ICSE 2025) **measure how badly it performs**, which turns a design judgement into
a supported one.

Their four measures are all producer-internal — average token probability, generated sequence
probability, verbalized self-ask, and QA logit. Result: **ECE 0.09–0.73** across settings; *"intrinsic
LLM confidences are poor predictors of code correctness."* Their own figures show
**ECE 0.46 → 0.04** once Platt rescaling is applied against local correctness labels.

**Two consequences for the instrument.**
1. **The clause is right, and now citable.** Where a rule previously rested on our reasoning, there is
   a peer-reviewed measurement behind it. Pair with §71 (practitioners delegating review to the
   generator) — the same axis from the practice side.
2. **Rescaling is a partial rescue, and the boundary matters.** A locally-calibrated confidence is
   *derived from* the model but *fitted against external outcomes*. It is still not
   producer-independent — the signal originates in the thing being checked — but it is materially
   better than raw. Contrast the genuinely independent cases: `R9CDT9KB` (Mahmud) routes on
   **inter-model disagreement** across three vendors; `5DI9B43K` (Sistla) routes on an **external
   formal verifier**. **Rule unchanged: self-confidence, rescaled or not, does not earn
   `risk-routing` or `routing-signal`.** Record rescaling in the rationale if a paper does it.

**Practical note for the survey.** Calibration is **not inheritable from the vendor** — it must be
fitted on the deploying organisation's own workload, using its own correctness labels (they use test
outcomes, chosen because *"tests are widely used, and are easily automated"*). That makes it an
org-side capability, and therefore a fair survey question rather than a vendor-side abstraction.

## 75. The confidence gate is gone — panel output is a suggestion, not a fact (2026-08-26)

Not a taxonomy refinement; a **procedural** one, recorded here because this changelog is the register
the methods chapter draws from. Full treatment in `Methodology/Theme_Tagging_Calibration.md` §11.

**What changed.** The original triage ladder (§5 of the calibration doc) auto-accepted 3/3 panel
consensus with only a 10% seeded random audit. That band is removed. **Every paper now gets a human
ruling on both tags and tier, regardless of agreement.** Sampling is not applicable — coverage is
total, so there is no sampling-error argument to make.

**Why, in principle.** Panel agreement is *the producer's own signal*. Gating review on it let the
thing being checked decide whether it needed checking — the failure §71 documents in practitioners
delegating review to the generator, and what §74's producer-independence clause forbids. The flaw was
present at design time; the errors below detected it.

**Why, in practice.** Unanimous panel error is measured, not hypothetical: `WUUDHL8R`
`regulatory-compliance` 9/9 (§44), `PR4GS7SP` `rules-based-checks`+`formal-methods` 9/9 (§51), Maes
`counterpoint` 8/9 with the polarity inverted (§64), and `9MV2IVNU` `demote:context` 9/9 overruled
(§53). Vendor decorrelation reduces correlated error; it does not remove **shared misreadings of the
instrument**, and those are invisible to agreement statistics.

**The number that settles it.** Across 515 panel-modal proposals on the 57 Light Read papers
adjudicated at T0: **72.6% endorsed · 8.3% rejected · 19.0% silent**, plus 29 non-modal proposals
rescued by human endorsement. **About one modal proposal in twelve is wrong.**

**What the panel is for.** Recall, not adjudication — it holds all 44 tags against every paper, which
is the thing human working memory fails at. Measured: panel recall on its *own* vocabulary is ~96%
(human origination 8.0% of written tags, ~4% once the post-freeze tags the panel could not propose
are excluded). It is a strong aid and not a substitute; the arbiter remains the criterion.

**Tagging is not fully automated *or* fully manual.** It is machine-proposed and human-validated —
supervision, not re-derivation. The vocabulary itself was likewise **co-authored** (emergent from the
corpus → machine-drafted → human-revised → human-locked before coding), which is what keeps the panel
from grading its own homework at the instrument level.

**Standing consequences:**
- Tripwires **rank attention**; they never **grant exemptions**.
- Depth of verification scales with **downstream consequence** (§42), never with agreement.
- `slr-tools/tag_layer_stats.py` regenerates these figures; T0 is frozen at
  `slr-phase4/data/tags-v213/tag_layer_stats_T0_2026-08-26.json`. T1 (corpus closed) and T2 (after
  the restricted re-run) are owed.
- **Instrument drift to date:** frozen v2.13 = 44 tags · cheatsheet now 45 · live in Zotero 50. All
  five post-freeze additions are human-originated. Every cheatsheet tag has fired at least once.

## 76. `metrics` — second application of §66; and MOSAICO's half-independence (`DJMBHHZN`, 2026-08-26)

Tisi et al., *MOSAICO: management, orchestration and supervision of AI-agent communities* — an EU
project proposal, month 3 of a 36-month span. Ruled **Core**, added to Dissertation Primary.

**(a) `metrics` rejected — §66 holds on its second case.** The agent repository specifies
*"quality attributes (KPIs), such as accuracy, failure rate, and latency."* Named dimensions, no
computable procedure. Same line as the Migliarini ruling: **naming what to report is not defining a
metric.** §66 now has a positive (Maes) and two negatives (Migliarini, MOSAICO).

**(b) `built-system` rejected despite an explicit prototype sentence.** The paper says *"We built
early prototypes to experiment ideas about the four technical solutions."* Prototypes built to
*explore ideas* in month 3 of 36, with every mechanism described in future tense and no evaluation,
do not clear §67's bar that the **core mechanism must run**. Codex proposed it 1/3; opus and gemini
both said `design-only`, and the arbiter agreed. **Worked rule:** a prototype sentence is not
self-certifying — check what the prototype *does* against the mechanism the paper claims.

**(c) `org-governance` declined as a vocabulary match (§59, and the panel got this one right).**
MOSAICO uses "governance" throughout, but the referent is a **technical policy language** for agent
communities (agreement type, minimum votes, deadlines, confidence thresholds) that the project owner
configures — not organizational policy or process for governing AI use. Test applied: *does the paper
describe governance of the org's AI use, or a mechanism the org configures?* Latter → `framework`,
which was already 3/3. **Notable:** 0 of 3 models proposed `org-governance`; the arbiter raised it and
withdrew it. The §59 failure mode usually runs the other way, so this is a useful converse instance.

**(d) `risk-routing` declined; human participation ≠ escalation.** The relevant sentence is *"Once
such a consensus is reached (potentially with the help of human evaluators **if they are also allowed
to participate according to the governance policy**)"* — humans are policy-permitted **participants**
in consensus, not a destination that disagreement escalates to. The confidence threshold routes to
**more agent discussion**, never to human attention. **Discriminator:** routing requires the signal to
allocate *human* review; a threshold that buys more machine deliberation is orchestration, not
routing.

**(e) `cross-model` declined — `agent-panel` without model heterogeneity.** The diversity claim is
*"specialisation of workers on tasks"*: role specialisation, not different models or vendors. Clean
worked case of the two facets coming apart — a panel can be many agents on one model.

**(f) Half-independence — a design that satisfies §74 at one layer and violates it at another.**
MOSAICO is architecturally producer-independent where it counts: first-level **solution agents**
propose, separate second-level **supervision agents** evaluate. But one of its two governance signals
is *"the uncertainty agents can have about their own answers"* — **self-reported producer
confidence**, the exact anti-pattern §74 names. Recorded because the corpus mostly offers designs
that ignore independence entirely; this is the first that gets it right structurally and then
undercuts it with a self-report channel.

**(g) Four correct tags proposed by one model only.** `tooling-supply-chain`, `agent-scope-drift`,
`oversight-explanation`, and `risk-quality` were codex-only (1/3) and all four were endorsed. Any
consensus rule would have discarded them — a single-paper instance of the effect quantified in
`Theme_Tagging_Calibration.md` §11.5 (29 non-modal proposals rescued across the pass).

## 77. `formal-methods` — membership tracks the technique used, not the technique invented (`72W6R4JG`, 2026-08-26)

Töpfer et al., *Vibe-coding: feedback-based automated verification with no human code inspection*.
Ruled **Core**; primary `rules-based-checks`; `formal-methods` kept as a theme.

**The finding that forced the question.** The abstract and the contributions list both present FCL
(Functional Constraint Logic) as *"a novel first-order temporal logic"*, but §4 says
*"Functional Constraint Logic (FCL), **introduced in [11]**"* and *"More examples and details on FCL
can be found in [11]."* **[11] is the authors' own companion paper** — Töpfer, Plášil, Bureš,
Hnětynka (2026), arXiv 2602.18607 — **already in the library as `2KDTRGRP`, sitting at Context**.
The formalism is borrowed; this paper contributes the feedback loop that uses it.

**Ruling — the two calls come apart:**
- **Primary: NO.** §67 lets `formal-methods` be primary *when the technique is the subject*. Here the
  technique is prior work, so the premise fails. Primary is `rules-based-checks` (panel 2/3).
- **Membership: YES.** **Theme membership tracks what the paper DOES, not what it INVENTS.** Novelty
  is a primary-selection criterion, never a membership bar — requiring it would strip mechanism tags
  off every paper that adopts machinery rather than inventing it.

**Why it clears the bar on the merits, not just by default:**
1. The formalism is **operative**. The central claim — *"diagnostic specificity is necessary"* — is a
   claim about FCL's properties: counting semantics localise failures where coarse metrics cannot.
   Remove FCL and there is no result (§67's core-mechanism-must-run test).
2. **§51's reference-oracle exclusion does not fire.** Constraints are authored *independently of the
   generated code*, so the checker runs on artifacts whose correct answer is unknown — the exact
   operational question §51 added, answered yes. Contrast `PR4GS7SP`, where it answered no.
3. It is the documented `rules-based-checks`+`formal-methods` pairing for a classical engine (§51).

**Strength vs kind — the distinction to keep.** The paper states *"The goal is not to prove properties
exhaustively, but to provide a detailed feedback message that supports repair."* Runtime trace-checking
over observed runs is weaker **evidence** than proof, but it is the same **kind** of technique. The tag
carries no proof-strength threshold. **If one is ever added — restricting `formal-methods` to
proof-grade work — it must be a written rule, not a per-paper call**, and it would shrink the cluster
(7 of 149), which feeds the §53 scarcity test on Mitchell (`6ZW9QNQH`). The definition call and the
Mitchell tier call are coupled.

**Also ruled on this paper:**
- **`agent-panel` REJECTED — tag by object (§62).** The "agents" are entities *inside the simulated
  system* (*"Villagers (agents) are farmers or…"*, ensembles in the Dragon Hunt CAS), i.e. the subject
  matter of the generated code. The architecture is one LLM plus one deterministic verifier — nothing
  reviews anything else. **Worked rule: the word "agent" in a paper's domain vocabulary is not
  evidence of an agent panel.**
- **`steering` REJECTED.** The domain expert states constraints once and exits; the turn-over-turn loop
  is **machine↔machine** (verifier → LLM). §54 requires an ongoing *human↔AI* loop. An automated repair
  loop is `remediation-gating`, not steering.
- **`method-experiment` REJECTED; `evaluated-synthetic` applied (§34 fork).** There is a real
  manipulation — three feedback-level variants, 10 independent attempts each — but it is an **ablation
  of the authors' own feedback design**, and the finding characterises *their tool*. Whose-properties
  test → tool-results. **Sharpest test case on record: a controlled ablation with replicates still
  earns no method facet.**
- **`provenance-auditability` REJECTED.** The counterexample report is *"rendered as a concise textual
  report… to provide a detailed feedback message that supports repair"* — it goes **to the LLM**. The
  definition requires a persistent record serving *human* reviewability; machine-to-machine persistence
  is plumbing. A human audit trail would also contradict the paper's own no-human-inspection thesis.
- **`evaluator-reliability` REJECTED — the evaluator is deterministic.** The FCL verifier is sound by
  construction; the LLMs here are *generators*, not evaluators. **The tag presupposes a probabilistic
  evaluator whose trustworthiness is in doubt** — the open question here is spec adequacy instead.

**New observation — the explanation channel runs backwards (`oversight-explanation` declined).** FCL is
explicitly designed for *legibility of failure*, argued against LTL: it yields *"attack happens 0 times
in steps 1–15"* rather than a generic *"globally"* / *"sometimes in the future"*. That is a genuine
explanation-design argument — but the stated audience is the model (*"counterexamples that can be
translated into **LLM-friendly feedback**"*), and **the human never sees AI output at all**: the domain
expert's surface is the constraint set they authored. `oversight-explanation` explains AI output *to a
human*; here a human-authored spec explains the failure *to the AI*. **First corpus instance of the
explanation channel pointing from the human's artifact toward the machine.** Recorded rather than
tagged; watch for a second instance before considering vocabulary.

**Follow-up owed at closeout:** `2KDTRGRP` (the FCL paper) sits at Context on a machine screening tag
(`s3:opus:context`) that was never human-confirmed, while a Core paper depends on it for its
formalism. Not a dedupe — genuinely different content — but the tier may be wrong. A third team paper,
`DU5B9CCK`, was discarded at s1.

## 78. §43 gets its first clean NEGATIVE — a paper that engages the AI Act correctly (`XZEHQYNZ`, 2026-08-26)

Tuape, Gabrielmichael & Kasurinen, *Architecting trust: designing human oversight and accountability
for AI-driven software engineering under the EU AI Act*. Ruled **Context** (`lit-review` 3/3,
self-described *"foundational step in a long-term research endeavor"* with *"preliminary findings"*),
added to **Dissertation Supporting**.

**Why it matters to §43.** `XZEHQYNZ` is one of the **12 papers on the EU-AI-Act watch tripwire**.
Checked against the two `WUUDHL8R` errors, it commits **neither**: no claim that dev tooling inherits
a risk tier, and no claim that AI-generated code makes a system high-risk. What it asserts is accurate:

- *"the Act strongly emphasizes 'effective oversight' for **high-risk AI systems**, its practical
  implementation for Agentic AI… lacks concrete guidance"* — correctly scoped
- *"the Act's expectation of human overseer competence"* — Art 14(4)(a), correct
- *"beyond a simple 'stop button' to real-time debugging"* — Art 14(4)(e), correctly characterised as
  insufficient for agentic systems

Only loose usage: *"high-risk applications of Agentic AI"* in the Discussion reads colloquially rather
than as the Act's term of art. Borderline, **not** a misstatement.

**Recorded as a CONTRAST CASE, not an instance.** §43 counts recurrences to test whether "papers invoke
the Act without engaging it correctly" is a reportable finding about field maturity. **A clean negative
is worth as much as a positive** — without negatives the tripwire measures only how many papers mention
the Act, not what share get it wrong. Watch count unchanged; denominator now has a confirmed correct
member.

**Also — the §44 converse.** §44 rejected `regulatory-compliance` on `WUUDHL8R` because the Act was
*justification*, not contribution. Here it **genuinely fires**: the Act is the **subject**, and the
paper's contribution is a taxonomy of implementation gaps in operationalizing Art 14 human oversight
for agentic SE. Panel proposed it as primary 3/3 and would have been right. **Not written** — §42
short-circuits tag verification on a Context ruling — but recorded so §44 has its positive pole.

**Discriminator worth keeping:** *does the paper's contribution change depending on what the Act says?*
`WUUDHL8R` — no, the refactoring tool is unaffected. `XZEHQYNZ` — yes, the entire gap taxonomy is
derived from Art 14's requirements. That is the line between motivation and contribution.

## 79. §53 worked NEGATIVE — a transferable finding does not earn Core when the thread already holds it (`ZBF86IJM`, 2026-08-26)

Vasconcelos et al., *Generation Probabilities Are Not Enough: Uncertainty Highlighting in AI Code
Completions* (ACM TOCHI 32(1), 2025). **Ruled Context.** Recorded because the assistant initially
argued for Core and the scarcity test reversed it — the reasoning is the reusable part.

**The tempting argument (rejected).** The paper's headline result reads as the producer-independence
clause proved: three within-subjects conditions over the **same completions**, differing only in what
was highlighted. Highlighting by **generation probability** — the producer's own signal — gave **no
benefit over no highlighting**; highlighting by a **separate edit model** gave faster completion and
more targeted edits. Mechanism-level, so it appears to transfer to agentic settings that route on
self-reported model confidence.

**Why it fails anyway — three counts of the §55 directness test:**
1. **Wrong mode.** `assistive`: human-initiated, snippet granularity, human authoring in the flow.
   The review's interest is agentic code.
2. **No scaling content.** No volume argument, no capacity argument, no delegation. The thesis's
   problem does not appear in the paper.
3. **Thin evidence for the transferable part.** n=30, three puzzle tasks, 10-minute cap, 38% baseline
   accuracy — and the accuracy hypothesis was **not supported** (p = 0.145). The significant effects
   were time, targeting, and preference; correctness did not move.

**The decisive check — the leg was already occupied.** The independence thread's *measurement* leg is
held by `VTDG995V` (Gros, Spiess et al., ICSE 2025), which tests four producer-internal confidence
measures directly against code correctness (ECE 0.09–0.73) and shows rescaling works only against
external ground truth. Same claim, **on code, at scale, no UI confound, and in scope.**

**Rule this establishes:** **§53 scarcity is tested against the ARGUMENT SLOT, not against the corpus
at large.** A finding is not scarce because it is unusual — it is scarce because *nothing else in the
corpus fills the role it would fill*. Before promoting on transferability, name the leg it would
occupy and check whether an in-scope paper already holds it. Contrast `9MV2IVNU` (Eze, §53), where the
slot was genuinely empty and the general-AI exception fired.

**What survives the demotion — one staged watch item.** Vasconcelos has something the rest of the
thread lacks: **human behavioural response to a routing signal** (`VTDG995V` is a calibration study
with no humans). Two observations, staged not adopted:
- *"several participants mentioned that they **interpreted a lack of highlights as signal that the code
  was correct**."*
- *"By editing **only the tokens highlighted**… participants would be able to pass the provided unit
  tests… **but their code would improperly handle an edge case** (because unit tests are not
  comprehensive)."*

This is the **un-routed remainder problem** — the failure mode of gate 1. Demonstrated only at token
granularity in assistive mode; extending it to PR-granularity agentic review is extrapolation.
**Tripwire: promote to a finding on a second instance at artifact granularity.**

## 80. `metrics` §66 — borrowed NOTATION without the mathematics (`2KPHQ5IV`, 2026-08-26)

Wang et al., *Scaling human-AI coding collaboration requires a governable consensus layer* (arXiv
2026-04-20). **Core.** Primary `provenance-auditability`.

**(a) `metrics` REJECTED at 3/3 — a correlated panel error, and a new §66 variant.** All three models
proposed it. The paper's §"Evaluation Framework" offers four measures; none clears the computable-
procedure bar, and **the authors disclaim the central one themselves**:

> *"Consensus entropy **H(𝐶 | 𝐼)** quantifies structural ambiguity given current intent; **we use
> conditional-entropy notation as conceptual shorthand rather than a literal Shannon quantity**."*

Alignment fidelity is *"**F(𝐼, 𝐶, 𝐴)** increases when…"* — function notation with no function,
*"can be estimated via human annotations, counterfactual questions, and post-hoc blame assignment."*
Cognitive load is a borrowed existing construct. Only *intervention distance* approaches it
(*"counts the number and complexity of human corrections"*) — the count is computable, "complexity"
and "correct consensus state" are not.

**The new variant:** §66's earlier negatives (Migliarini, MOSAICO) named *dimensions in prose*. This
one names them in **mathematical notation** — `H(·|·)`, `F(·,·,·)` — which creates an appearance of
formal content that the surrounding text explicitly withdraws. **Symbolic notation is a §59
vocabulary match at the symbolic level, and the panel fell for it 3/3.** Test to apply: *strip the
notation and restate in prose — is a procedure still described?* Here: no.

**(b) `oversight-scaling-inversion` — the cleanest §52 instance since `E9RAWBDT`.** Fail-open is
explicit; the approval happens anyway:

> *"Tests pass; **you click Merge**… you approve based on vibes: surface plausibility rather than
> structural understanding. Three months later a regression appears…"*
> *"As AI throughput scales, **opacity accumulates faster than humans can inspect it**… scaled
> AI-assisted engineering degrades into **scaled opacity**."*

Worth noting the *mechanism* is novel to the corpus: the inversion is driven not by diff **volume**
alone but by **dimension collapse** — the artifact (code plus chat history) cannot represent the
structural commitments, so inspection capacity fails for want of a reviewable representation rather
than for want of time. Complementary to the capacity-based accounts, not a duplicate of them.

**(c) `oversight-theater` applied — and the contrast with `E9RAWBDT` that sharpens §69.** On Pimenova
the arbiter refused theatre: *"There is no oversight, so there can't be theatre."* Here the process
**exists** — PR review, click Merge — and is hollow for want of **information**:
*"reviewers demoted to rubber-stamping opacity."* §69's presupposes-a-process condition is met.
**Discriminator: theatre needs a ritual to be empty. No ritual → no theatre; ritual without
information → theatre.**

**(d) `quality-debt` and `risk-routing` REJECTED at 2/3 each.** Both modal, both dropped on the
arbiter's read. Recorded because rejection was *required* — under §45/§46 a modal proposal survives
into `final:*` on silence, so "drop" is only effective as an explicit `cal:human:reject:*`.

**(e) `counterpoint` 2/3 — third measured polarity inversion (§56/§64).** The paper argues *better
models alone do not eliminate oversight needs*, which is thesis-**supporting**. Not `scaling-dissent`.
Left to the closeout deprecation sweep rather than rejected per-paper.

## 81. Mode tie-rule UPHELD; "nobody inspects" belongs on its own axis (`T2EG4BE2`, 2026-08-26)

Waseem et al., *Vibe coding in practice: flow, technical debt, and guidelines for sustainable use*.
**Core**, primary `quality-debt`. **`agentic` APPLIED** under the standing tie-rule.

**This entry was rewritten the same day.** It first recorded a *no mode facet* ruling, which was
reversed on review. **The reversal is the instructive part and is left visible.**

**What went wrong.** The arbiter reasoned *"Agentic means agents generating code autonomously. This
one focuses on vibe coding in iterative sessions with human directing"*, then on the fallback:
*"Not assistive. Human likely not even looking at the code."* The assistant agreed and wrote no mode
facet — **without checking the tie-rule that already governs exactly this case:**

> *"**Tie-rule:** initiator vs reviewable unit disagree (human-prompted chat task → complete artifact)
> → **the reviewable unit dominates** (wholesale artifact = the gate = `agentic`)."*

Waseem is that case verbatim: human-prompted, complete-artifact output. **A standing written rule was
overridden by an unwritten exception.**

**Two checks that caught it:**
1. **An internal contradiction in the data.** `72W6R4JG` (Töpfer, §77) — titled *"with no human code
   inspection"* — carries `agentic` (3/3, endorsed). Waseem carried no mode. **Same phenomenon,
   opposite tags, differing only in the order the two papers were discussed.**
2. **The no-mode bucket already means something else.** 22 of 66 adjudicated papers carry no mode, and
   they are there because *mode is irrelevant to the claim* — AI on the review side only, general-AI,
   or lit reviews (Migliarini, McKay, Sistla, Mitropoulos, Sterz…). Filing Waseem there **conflates
   "irrelevant" with "inexpressible"**, when mode is the paper's entire subject.

**The category error, stated for reuse.** The insight — *the human may never look at the code* — is
real, but it is an **oversight** property, not a **generation** property. Modes describe how code is
produced; inspection describes what happens to it afterwards. **Recording an oversight fact by
withholding a generation tag puts it on the wrong axis, and that is why it collided with the
tie-rule.** General rule: **when a tag feels wrong because of something the vocabulary cannot express,
do not encode the gap by omission — stage a new tag on the correct axis.**

**Ruling:** `agentic` applied. `assistive` not applied (0/3, and the human is not authoring in the
flow). The absence-of-inspection observation is **staged as a facet candidate**, not encoded here.

### 81a. STAGED CANDIDATE — `no-inspection` (2 instances, tripwire at 3)
An **orthogonal flag**, composable with either mode, marking that no human reads the generated
artifact at any point. `agentic` + `no-inspection` says what neither tag says alone.

| Instance | Character | Evidence |
|---|---|---|
| `T2EG4BE2` Waseem | **observed drift** | *"a single 'fix this' prompt can rewrite large parts of the codebase **before architects or testers have seen the previous version**"*; approval *"based on vibes"* |
| `72W6R4JG` Töpfer | **deliberate design** | titled *"…with **no human code inspection**"*; a formal checker is offered as the substitute |

**Do not graft mid-measurement (§41)** — accumulate to the next versioned cut. **Why it matters:** if a
mode exists in which no human inspects the artifact at any point, that is the scaling inversion at its
limit — not oversight degraded but oversight **absent** — and the instrument cannot currently say so.

**Other rulings on this paper:**
- **`agent-scope-drift` APPLIED** (codex 1/3 — a fourth non-modal rescue). The object is the agent
  departing from its mandate across regeneration cycles: *"one microservice **regenerated its
  authentication mechanism from JSON Web Tokens to session cookies**, causing authorization failures
  (HTTP 401) across dependent services"*, and the countermeasure is aimed squarely at it —
  *"Compare regenerated code semantically; highlight **intent-level changes** rather than line diffs
  to **prevent drift**."* Also *"reduces architectural drift"* and *"governance of architectural
  decisions (to prevent drift across iterations)."* §62 satisfied: the drifting thing is the agent,
  not the model.
- **`method-mining` KEPT over an initial arbiter instinct to drop it.** The concern was that the
  evidence base is *"authors' experiences, chats over coffee."* But the paper contains a discrete
  quantified measurement: *"We also **scanned seven early-stage vibe-coded MVPs**… **970 security
  issues were detected, including 801 high-severity**… unsafe input handling, insecure file
  operations, and exposed credentials accounted for **over 70% of all findings**."* Artifacts
  measured, findings characterising those artifacts — the `NZJST99D` shape at small scale. **Test
  that settled it: if the facet were dropped the paper would carry no method facet at all, asserting
  "no empirical evidence produced," which is false.**
- **`method-field-study` REJECTED at 3/3.** The experiential narrative (a microservice regenerating
  its auth from JWT to session cookies; API contracts with inconsistent field names) is **recounted,
  not observed as method**. **Discriminator: an experience report is not a field study — field study
  requires the observation to be conducted as method, not recalled as anecdote.**
- **`method-self-report` correctly absent (1/3).** No instrument: *"Surveying vibe-coded
  practitioners"* appears in the paper's **future work**, and the surveys it cites are other people's.
- **`org-governance` CONFIRMED after a challenge.** The assistant flagged over-tagging risk on the
  2/3 countermeasures cluster; checking it, the risk did not materialise. Table 1 is a **role-specific
  guideline matrix** with an explicit *"ʝ = guidance primarily for **CIO/CTO and organizational
  leadership**"* audience, whose rows define *"roles, approval gates, and audit trails"*,
  *"approval permissions"*, *"sign-off for high-impact code generations"*, and **"policy-as-code
  gates"** by name. Hits nearly the whole definition, and it is the paper's stated deliverable.
- **`regulatory-compliance` REJECTED at 2/3** — compliance appears as a *risk category to document*,
  not as an external-standard contribution (§44 discriminator: the contribution does not change
  depending on what any regulation says).

## 82. Routing to REDUCE load vs routing to ENSURE coverage — two mechanisms, one tag (`RG4A4D6K`, 2026-08-26)

Watson & Italie, *From black box to open book: an emerging transparency imperative in generative AI
codebases*. **Ruled Context** (`lit-review` 3/3, evidence is *"documented case studies and industry
data"*, recommendations only; `demote:context` 2/3). Tag verification short-circuited per §42; the
rulings below are recorded as reasoning-of-record rather than written to the arbiter layer.

**(a) The distinction the arbiter drew, which the vocabulary does not yet make.** Accepting detection
as a routing signal, the arbiter added: ***"It isn't tackling scaling at all, just ensuring review."***
That names two mechanisms currently sharing one tag:

| | Purpose | Effect on human load | Failure mode |
|---|---|---|---|
| **Routing to reduce load** | decide what *can safely skip* human review | **decreases** it | the un-routed remainder reads as endorsed (staged tripwire, `ZBF86IJM`) |
| **Routing to ensure coverage** | decide what *must not* skip review | **increases** it | false negatives read as *human-authored* and get ordinary review |

Watson is the second kind: AI-authored segments are detected and **selected for targeted human
review** — attention is *added* where there was none, not redirected away. **Both are `risk-routing`
mechanically, and they answer opposite questions.** This matters for SQ5: only the first is a scaling
mechanism. A corpus count of `risk-routing` papers therefore **cannot** be read as a count of scaling
mechanisms without separating the two.

**Symmetry worth noting:** the failure modes are the same shape. Vasconcelos showed un-highlighted
tokens read as correct; a detector's false negatives make AI code read as human-authored. **In both
directions, the absence of a routing signal is interpreted as a clean bill of health.**

**(b) Producer-independence satisfied by construction — second design instance.** The detector is
explicitly external to the generator: *"an **'outside-in' approach, analyzing the code itself without
requiring access to the AI tool's internal data or metadata from the generation process**."* Stronger
than MOSAICO's half-independence (§76f), which readmitted self-reported agent confidence. Feeds the
independence thread even from Context.

**(c) `regulatory-compliance` REJECTED at 3/3 — §78 discriminator applied.** *Does the contribution
change depending on what the regulation says?* No: the provenance-tracking recommendation stands
regardless, and compliance is one of four listed motivations alongside QA, security, and IP. Arbiter:
*"It is a motivation, but not deeply discussed."* Same pattern as `WUUDHL8R` (§44).

**(d) §43 watch tripwire — a THIRD category, and it may be the largest.** `RG4A4D6K` is one of the 12
flagged papers. It is neither correct (Tuape, §78) nor wrong (`WUUDHL8R`, §44) but **hedged to the
point of being unfalsifiable**: *"GDPR and the EU's AI Act **may require** organizations to disclose AI
use in their products"*, and *"regulatory bodies **increasingly mandate** transparency requirements for
AI systems in software development"* — the Act's transparency duties attach to specific system types,
not to AI use in software authoring, so the second overstates without asserting anything checkable.
**If several of the remaining 9 land here, the tripwire is measuring vagueness rather than error, and
the finding changes** from "the field misreads the Act" to "the field invokes it without engaging it."
Classify each of the 12 into correct / wrong / vague at closeout.

**(e) WATCH — risk flags may over-fire on risk-survey papers.** All five (`risk-security`,
`risk-quality`, `risk-ip`, `risk-bias`, `risk-overreliance`) came in 3/3. The arbiter's read of the
depth: *"It mentioned the various risks in the doc (**bullet points with explanations**)."* The bar is
substantive treatment — define a metric, contribute/evaluate a mitigation, report an empirical result,
or devote focal analysis — and bullet-with-explanation sits between "intro risk-list sentence" and
focal analysis. **Not adjudicated here (§42), but flagged: a lit review that surveys risks will trip
every flag, and risk-flag counts feed the identified/measured matrix.** Check at closeout whether
`lit-review` papers carry systematically more risk flags than primaries; if so the matrix needs to
segment by `lit-review` before counting.

**(f) Scarcity note supporting the demote.** Arbiter: *"there are several other papers I've seen that
have done detection of AI-gened code in GitHub repos."* Detection of AI-authored code is **not scarce**
in the corpus, and this paper contributes no detector of its own — it synthesizes the case for one.
§53 slot already occupied (cf. §79).

**(g) `problem-statement-anchor` NOT applied** despite the paper's committee-friendly opener —
*"GenAI tools… now generate an estimated **20-30% of code in many enterprise codebases**."* The rule is
**never on `lit-review`**: anchor the primary instead. **Action: chase citation [source of the 20–30%
figure] and evaluate the primary for the anchor.**

## 83. `oversight-scaling-inversion` REJECTED at 3/3 — silence is not evidence of fail-open (`F2C2DWSI`, 2026-08-26)

Xu, Medappa, Tunç, Vroegindeweij & Fransoo, *AI-assisted programming decreases the productivity of
experienced developers by increasing the technical debt and maintenance burden*. **Core**, primary
`quality-debt`.

**The rejection.** All three models proposed `oversight-scaling-inversion` and two made it **primary**.
Rejected. §52 requires **both** conditions affirmatively: AI code is riskier **yet less inspected**,
**and it ships anyway**. Xu supports neither — core contributors *"review more PRs"* (+6.5%), and
AI-generated contributions *"require more revisions **before integration**."*

**The rationale that survived arbiter correction, and it is the important part.** The assistant first
argued the reject on the ground that *"nothing ships unreviewed."* The arbiter corrected this:
*"Less that nothing ships unreviewed, as the core team is spending more time fixing stuff."* **The
paper never measures whether unreviewed code merges at all** — it measures rework volume and effort
allocation. The correct basis is therefore **silence, not contradiction**:

> **§52 requires affirmative evidence of fail-open. A paper that does not study inspection coverage
> cannot supply it, however strongly its other findings rhyme with the mechanism.**

This is a stronger and more portable rule than the one first offered, and it guards a real failure
mode: reading a paper's *adjacent* findings as though they established the specific claim a tag
requires. Cf. §59 — the panel matched "review burden" + "scaling" to the tag's vocabulary.

**What the paper supplies instead — the SUBSTITUTION mechanism.** Its own contribution statement:

> *"technical debt is increasingly an **outdated workload distribution phenomenon**: maintenance costs
> are concentrated among a **shrinking pool of core contributors, whose own productive output
> declines** as maintenance demands rise"* — and this holds *"even when the OSS repository workflow
> remains unchanged."*

Core developers review **6.5% more** and lose **19% of their own original output**. Oversight does not
fail; **senior building capacity** does. Recorded as a distinct mechanism in `Emerging_Themes.md`.

**`problem-statement-anchor` APPLIED (codex 1/3 — non-modal rescue).** The 6.5% / 19% pair quantifies
the overall two-part frame rather than a sub-argument, and this is a **primary study** — a
difference-in-differences design over a monthly GitHub panel (July 2020–July 2022, treatment/control
at project and contributor level) — so the never-on-`lit-review` bar does not bite (contrast §82g,
where Watson's 20–30% figure was refused for exactly that reason).

**`intro-framing` NOT applied** despite an initial arbiter instinct toward it. Panel 0/3, and the
paper is econometric causal inference, not a position paper. **Discriminator restated: `intro-framing`
marks papers that name a gap *instead of* operationalizing; it never applies to a study that produces
primary evidence, however framing-relevant its conclusions are.**

**Others:** `assistive` 3/3 (Copilot), `method-mining` 3/3 (mined repos/PRs/commits/review activity),
`risk-quality` 3/3. `metrics` (2/3, PR rework operationalized as a debt measure — likely clears §66,
unlike `2KPHQ5IV`) and `risk-overreliance` (1/3) left to stand or fall on modality. `counterpoint`
(2/3) is a **fourth** polarity inversion — the paper opposes AI *productivity maximalism*, which is
thesis-**supporting**, not `scaling-dissent`; deferred to the closeout deprecation sweep.

## 84. `metrics` §66 — the OFFERED-FOR-REUSE test, and the facet's first two-condition positive (`F2C2DWSI`, 2026-08-26)

Follows §83. `metrics` **APPLIED** to Xu et al. after a challenge from both directions — the arbiter
doubted it fit (*"I'm not sure that this fits our definition"*) and the assistant expected to agree.
**The text overruled both.**

**What decided it:**

> *"**A key contribution of our study is to operationalize technical debt at its point of entry.** We
> conceptualize extensive PR rework as realized technical debt…"*

and the measure is positioned **against existing measurement work**, not merely used —
*"Measurement approaches for technical debt have evolved along two complementary axes… PR rework
provides a **direct operationalization** of [it]."*

**Why this matters: it is the facet's first instance satisfying BOTH conditions in this pass.**

| Paper | Claimed as deliverable | Computable procedure | Ruling |
|---|---|---|---|
| `2KPHQ5IV` Wang (§80) | yes | **no** — *"conceptual shorthand rather than a literal Shannon quantity"* | reject |
| `DJMBHHZN` MOSAICO (§76a) | no — named KPIs | no | reject |
| Migliarini (§66) | no — named dimensions | no | reject |
| **`F2C2DWSI` Xu** | **yes** | **yes** — a regression variable; the DiD forces precision | **apply** |

**The discriminator, stated for reuse — the OFFERED-FOR-REUSE test:**

> **Is the measure *offered for reuse*, or *constructed to answer this paper's question*? The tell is
> whether the paper situates it in the measurement literature. Every empirical paper builds variables;
> only some argue for them.**

This is deliberately the **same shape as §57's instrumentation-vs-contribution rule** for method
facets — measurement machinery used to reach a finding is an instrument; measurement machinery argued
for on its own terms is a contribution. The two rules should be read together.

**Why the "computable" half alone is insufficient** (and why this does not reopen §80): a regression
variable is computable by construction, so computability cannot distinguish a contributed metric from
an ordinary dependent variable. **Both conditions are required, in either order** — §66 kills the
formally-dressed-but-uncomputable case (Wang), the offered-for-reuse test kills the
computed-but-incidental case (any quantitative study).

**Narrowing considered and declined.** A stricter reading was put to the arbiter — reserve `metrics`
for measures with **a name and a formula** that another paper could adopt by name, which would treat
Xu's "PR rework as proxy" as a modelling choice rather than a metric. **Declined** (*"Let's keep
metrics"*); noted here because it would also retire the Maes positive, and because it remains available
as a §41 graft if the facet proves to over-fire at closeout.

**`risk-overreliance` NOT applied** (1/3, non-modal — falls out with nothing written). Arbiter
confirmed.

## 85. Primary belongs to the MECHANISM, not the harm it targets (`QUXRX9ZL`, 2026-08-26)

Yanev et al., *The prompt–refactor–verify (PRV) cycle: a human-centered framework for AI-assisted
programming*. **Ruled Context.** Tag verification short-circuited (§42); rulings recorded below as
reasoning-of-record: primary `hitl-workflow`, theme `quality-debt`, facets `agentic`, `design-only`.

**(a) The primary question, and the rule it produced.** The arbiter's initial call was
`hitl-workflow`, then reconsidered toward `quality-debt`: *"the framework proposed as the explicit
refactor stage… is human supervised refactor and cleanup of the code. That might tilt to quality as
primary actually?"* **Held at `hitl-workflow`**, for a reason that generalises:

> **Nearly every Solution theme exists to protect quality.** `rules-based-checks`, `ai-review`, and
> `remediation-gating` all catch defects. If "the mechanism targets quality" made `quality-debt`
> primary, most of the Detect→Fix half of the taxonomy would file under a Problem heading and the
> solution themes would empty out. **`risk-quality` is the flag that records which harm is targeted;
> the primary records what kind of thing the paper is.**

Reinforced by the flag-vs-theme rule: `quality-debt` as a theme *"still requires the paper to do the
lift."* Yanev asserts the decay and cites Copilot studies for it; its own pages go to the cycle.

**Worked pair, same week, opposite rulings:**

| | Contribution | Primary |
|---|---|---|
| `F2C2DWSI` Xu (§83) | **measures** the debt | `quality-debt` |
| `QUXRX9ZL` Yanev | **proposes a workflow** to prevent it | `hitl-workflow` |

**Where the arbiter's instinct did land:** Refactor being *human-guided* is what makes this
`hitl-workflow` rather than `remediation-gating` or `steering` — the human performs the cleanup rather
than approving a machine's. That argues **for** the mechanism primary, not against it.

**(b) Mode tie-rule applied a second time, consistently.** Panel split `assistive` 2/3 / `agentic` 2/3.
Gemini's rationale is the tie-rule case verbatim — *"Prompts generate complete artifacts like
controllers that require holistic manual review."* Human-initiated, artifact-granularity → **reviewable
unit dominates → `agentic`** (cf. §81, where the same rule was restored on `T2EG4BE2`).

**(c) `design-only`, and an enforcement-gap observation.** Codex read Verify as *"a defined pre-merge
checkpoint with **blocking authority**."* **Overread.** The paper says *"confirm correctness before
merging"* and self-describes as a **"micro-methodology"** — discipline, not enforcement. This is the
third or fourth proposal in the pass that specifies human checkpoints with no machinery behind them
(cf. §61). **Watch:** if the cluster holds, "prescribed-but-unenforced human checkpoints" is a
reportable pattern about the solution literature, not just a per-paper caveat.

**(d) §53 scarcity — a worked FAILURE, run per §79 against the argument slot.** The slot is
*an unbuilt, human-centred practice discipline for vibe coding*. Corpus-wide, `hitl-workflow` plus a
proposal facet (`design-only`/`framework`/`intro-framing`) covers **32 of 128** papers. Direct
neighbours: **Elgendy** (*Responsible vibe coding*) — **already Context, same shape, same subject**;
**Mitchell** (*vibe coding needs vibe reasoning*); **Maes** (*gotchas of AI coding and vibe coding*);
**Kamalı** (*Rethinking code review in the age of AI*); **Bara** (*HAIF*). **Elgendy is the decisive
precedent — keeping Yanev at Core would contradict a ruling already made on the same profile.**
Transferable content is held elsewhere by papers with more behind them, and Yanev concedes its own
Verify stage is unreliable in the setting it targets (*"contexts lack robust test suites"*).

**(e) Preserved regardless of tier — two items.**
1. **The self-refinement contrast**, a crisp design-side statement of producer-independence reached
   without reference to §74: *"PRV's Refactor stage resembles **self-refinement**, but with a critical
   difference: **the responsibility lies with the developer, not the model.** The AI can propose
   changes, but the human…"* Feeds the independence thread's prescription leg.
2. **The commit-prefix convention** — `init-` / `refactor-` / `verify-` prefixes plus prompt logs as an
   artifact-level provenance trail. Small and unenforced, but possibly **the only artifact-level
   AI-tagging convention proposed in the corpus**. Check at closeout before discarding; if unique it is
   worth a sentence in the provenance discussion even from Context.

## 86. §52's fail-closed exclusion — second unanimous rejection, and RATE-LIMITING ≠ ROUTING (`XJAXB98T`, 2026-08-26)

Yang, He & Zhou, *Beyond banning AI: a first look at GenAI governance in open source software
communities* (arXiv 2026-03-27). **Core**, primary `org-governance` (3/3), **added to Dissertation
Primary**. Multi-stage qualitative analysis of governance materials from **67 highly visible OSS
projects**.

**(a) `oversight-scaling-inversion` REJECTED at 3/3 — the definition already covered this case.**
§52's full text carries an explicit exclusion the assistant had been quoting only in truncated form:

> *"Capacity saturation that resolves **fail-closed** — agent PRs ignored/abandoned so nothing merges —
> is **NOT** this theme: safety holds, throughput collapses, and the harm is **productivity, not
> risk**."* · *"**Synthesis test:** would the paper read naturally in a section on bad code shipping
> unreviewed? If it would jar because nothing shipped, this is the wrong home."*

Yang is the purest fail-closed case in the corpus: the entire paper documents **gates going up** —
bans, evidence requirements, disclosure mandates, queue limits. FastAPI's *"a **Denial-of-service
attack on our human effort**"* is throughput collapse, exactly the excluded harm.

**(b) The pattern this makes — a reproducible panel error, now at two instances.** `F2C2DWSI` (§83)
and `XJAXB98T` both drew **3/3** on this theme and both were rejected. **The panel reliably reads
"review burden + scaling" as the inversion and skips the fail-open requirement.** This is a §59-class
vocabulary match, and unlike most it is *predictable*: any paper whose abstract pairs rising AI volume
with maintainer strain will trip it. **Action at closeout: re-check every `oversight-scaling-inversion`
tag in the corpus against the fail-closed exclusion and the synthesis test — the theme is likely
over-applied wherever the arbiter was silent.** Note also that §83's "silence is not evidence of
fail-open" rule, while sound, was a weaker instrument than the clause already written; cite the
exclusion first.

**(c) NEW DISCRIMINATOR — rate-limiting is not routing.** `risk-routing` was proposed 1/3 on the
strength of *"independent queue limits route excess newcomer PRs away from reviewer attention."*
**Rejected.** Arbiter: ***"it would need to escalate to get risk routing."***

> **Routing directs an item to a destination chosen by its risk. Rate-limiting caps intake volume
> regardless of risk. A queue cap throttles; it does not triage.** No destination, no assessment, no
> escalation path → not `risk-routing`.

Sits alongside §82's load-reducing / coverage-ensuring split as a third distinction, and it is the
sharper one: §82 separates two *purposes* of routing; this separates routing from a mechanism that
merely *reduces* the queue without discriminating within it.

**(d) `survey-input` at its strongest instance so far.** Three governance orientations and **12
strategies in four functional groups** (entry admissibility and input qualification; responsibility and
evidence restoration; review burden and workflow protection; infrastructure and institutional
adjustment), derived from observed practice rather than proposed. This is a **ready-made instrument
skeleton** for the dissertation's org survey — the reason for the Dissertation Primary placement.

**(e) Both modes applied (`assistive` + `agentic`, 3/3 each)** — legitimate span, not indecision:
disclosure rules cover inline completion while `AGENTS.md` and autonomous-patch policies cover
artifact-granularity agents. Contrast §81/§85, where the tie-rule had to pick one because the paper
studied a single setting.

**Also applied:** `provenance-auditability` (3/3), `hitl-workflow` (3/3), `method-mining` (3/3),
`risk-quality`, `risk-ip` (3/3 each), `risk-security` (2/3), `steering` (2/3).
**Declined on arbiter ruling:** `agent-scope-drift` (1/3), `oversight-explanation` (1/3) — both
non-modal, nothing written.

## 87. DISCRIMINATING POWER as a boundary criterion — §52 stays narrow (2026-08-26)

Arising from the Yang ruling (§86a), the arbiter pressure-tested the rejection and then settled the
general question: ***"We need to be careful about being too broad, then everything qualifies."***

**The question.** The working gist of `oversight-scaling-inversion` is *"code volume overwhelms review
mechanisms."* §52 as written requires more: volume overwhelms review **and bad code ships**. The two
come apart exactly in the **fail-closed** cases — saturation answered by bans, gates, queue caps, or
expert absorption — which is where every recent dispute has landed (`NZJST99D`, `F2C2DWSI` §83,
`XJAXB98T` §86).

**Measured spread at T0 (128 Phase 5 papers):**

| | n | share |
|---|---|---|
| proposed by ≥1 model (≈ "mentions review burden") | **32** | 25% |
| panel-modal ≥2/3 — carries the tag **on arbiter silence** | **21** | 16% |
| arbiter **endorsed** | 6 | |
| arbiter **rejected** | 4 | |

**Ruling: §52 stays narrow.** Widening it to the gist would move the theme from 6 papers toward ~32.
At that point the claim *"the inversion is widespread in the literature"* would be **an artifact of the
definition rather than an observation** — the finding would be circular.

**Principle, stated for reuse across the instrument:**

> **A theme's value is its discriminating power. If a boundary is widened until the theme fires on
> everything that gestures at the topic, it stops separating papers and can no longer support a
> finding about prevalence.** When tempted to widen, ask what share of the corpus would qualify and
> whether the resulting claim would still be informative.

This generalises §55 (directness/tangency) from the *paper* side to the *tag* side: §55 asks whether
a paper is close enough to the question; this asks whether a tag still tells us anything once it
admits everything close to the topic.

**Where the excluded material goes.** Fail-closed saturation is not discarded — it is accumulating in
`Emerging_Themes.md` under two mechanisms with better resolution than a widened §52 would give:
**substitution** (`F2C2DWSI` — senior building capacity pays) and **intake restriction**
(`XJAXB98T` — communities refuse rather than triage). **Splitting beat widening.**

**CLOSEOUT ACTION, now quantified (sharpens §86b).** The arbiter has rejected **4 of the 10** cases
actually examined — a 40% error rate on a unanimous-prone theme. **15 papers currently carry the tag
on silence alone.** At the observed rate roughly six are likely misapplied. **Re-check all 15 against
the fail-closed exclusion and the synthesis test before computing `final:*`.** This is the largest
known single source of tag error in the corpus.

## 88. THE LEAKAGE TEST — §52's operative criterion, and a diagnosis of its own wording (2026-08-26)

Follows §86/§87. The arbiter narrowed `oversight-scaling-inversion` to a single sufficient condition
and named three symptoms that **do not qualify on their own**:

> ***"Burden falls on maintainers doesn't cut it. Throughput down, queue up. Maintainer who is serious
> still reviews, just takes longer. Preventing project work doesn't do it either. Has to result in
> **leakage of risky code**."***

**THE LEAKAGE TEST — the operative criterion:**

> **Risky code must escape the review that should have caught it.** Not "review is strained" — review
> **failed to hold**, and something got through as a result.

**Explicitly NOT sufficient (each of these was argued for and rejected):**

| Symptom | Why it fails | Case |
|---|---|---|
| Burden piles on maintainers | strain is not failure | `XJAXB98T` |
| Queue grows, throughput falls | *"a serious maintainer still reviews, just takes longer"* — **latency is not leakage** | `NZJST99D` |
| Real project work displaced | productivity harm, not risk harm | curl's fabricated security reports (`XJAXB98T`) |
| Experts absorb the rework | the gate held; the cost was paid elsewhere | `F2C2DWSI` (§83) |

The clearest formulation: **the gate holding slowly is not the gate failing.** Delay, cost, and
displacement are all consistent with oversight *working*.

**DIAGNOSIS — the definition is causing its own false positives.** §52's positive description reads
*"AI code is riskier yet less inspected and ships anyway — PRs auto-merged unreviewed; **review is the
bottleneck; burden piles on maintainers**."* The final clause **describes a symptom that the same
entry elsewhere rules insufficient**, and it sits in the part of the text the taggers pattern-match
against. That is very likely the mechanism behind the 25% proposal rate measured in §87 — the panel is
matching a phrase the definition itself supplies. **The assistant's "pro" case for Yang was built on
the same phrase, so this is not a model-only failure.**

**GRAFT CANDIDATE for the next versioned cut (§41 — do NOT edit `Tag_Cheatsheet.md` now):**
1. Remove *"review is the bottleneck; burden piles on maintainers"* from the positive description, or
   demote it to an explicitly-insufficient example alongside the fail-closed exclusion.
2. Lead the definition with **the leakage test** rather than with symptoms.
3. Keep the synthesis test, which already works: *would the paper read naturally in a section on bad
   code shipping unreviewed?*

**CLOSEOUT — revises the §87 estimate upward.** The 40% rejection rate was computed against the old
looser reading. Under the leakage test the bar is higher, so **more than six of the 15 silent-modal
papers are likely misapplied**. A cheap sizing is available before the re-check: tally how many of the
15 have panel rationales citing *burden/bottleneck/capacity* versus *leakage/merged-unreviewed* — the
former are near-certain rejects. **Not run (mid-pass); queued for closeout.**

## 89. STAGED FOR THE RE-RUN — `oversight-scaling-inversion` v2, built on the leakage test (2026-08-26)

**Arbiter directive:** include an inversion **v2** tag in the upcoming tagging run. Staged here; **not
grafted into `Tag_Cheatsheet.md`** (§41 — the frozen instrument does not move mid-measurement).

**Draft v2 definition — leads with the harm, not the symptom (§88):**

> **Risky AI-generated code escapes the review that should have caught it.** Requires an **escape
> event or a stated mechanism producing one**: PRs auto-merged unreviewed · merge-on-green where the
> check cannot see the defect class · review conducted without visibility into what actually changed ·
> a gate that passes what it was placed there to stop.
>
> **NOT sufficient, on their own:** maintainer burden · queue growth · falling throughput · displaced
> project work · experts absorbing the rework. ***The gate holding slowly is not the gate failing.***
>
> **Synthesis test (retained):** would the paper read naturally in a section on *bad code shipping
> unreviewed*? If it would jar because nothing shipped, this is the wrong home.

**DESIGN QUESTION — use a NEW SLUG, not a redefinition of the old one.** The namespace labels tags by
*who proposed them* (`cal:<model>:*`), **never by which instrument version produced them**. So if the
re-run emits `oversight-scaling-inversion` under the v2 definition, those proposals become
indistinguishable from the 32 v1-era proposals already in Zotero, and `final:*` would silently mix two
different constructs.

**Recommendation: a distinct slug** (working name **`oversight-leakage`**; final name the arbiter's
call). Benefits:
1. **Comparability.** v1 and v2 proposals coexist and are separately countable.
2. **It converts the §88 instrument defect into a measurement.** Re-running the *same corpus* under a
   *sharpened* definition yields a directly reportable number: **how many papers reclassify when the
   symptom language is removed.** That is a quantified demonstration that definitional wording drives
   tagger behaviour — a genuine methods-chapter result, obtainable at no extra cost because the run is
   happening anyway.
3. **No rewriting of history.** The v1 record stays intact and auditable per the additive-layers rule.

**Cost if the slug is reused instead:** the reclassification measurement is lost, and the closeout
re-check of the 15 silent-modal papers (§87/§88) becomes mandatory manual work rather than something
the re-run largely answers by itself.

**Re-run roster — this joins the existing restricted-re-run list** (`Theme_Tagging_Calibration.md`
§10.12): `agent-panel`, `cross-model`, the `evaluated-*` ladder, `scaling-dissent`,
`evaluator-reliability`, `evaluated-real-data`, **+ inversion v2**. Note this one differs in kind from
the others: they are tags the frozen instrument **never contained**, whereas this **competes with an
existing tag** — which is precisely why it needs its own slug.

**Open for the arbiter:** (a) final slug name; (b) whether v2 **supersedes** v1 at closeout (v1 tags
retired, `final:*` computed from v2 only) or whether both are reported with the delta as a finding.
Recommend the latter — the delta is more informative than either count alone.

## 90. STEERING-ONLY as a demote ground; and a search-strategy terminology hazard (`9R6TGN82`, 2026-08-26)

Yao et al., *Training language models to generate quality code with program analysis feedback* (REAL).
**Ruled Context.** Tag verification short-circuited (§42); panel proposals recorded as
reasoning-of-record: `rules-based-checks` primary 3/3, `steering` 3/3, `built-system` 3/3,
`metrics` 3/3, `risk-security` 3/3, `risk-quality` 3/3.

**(a) The ground: steering-only.** Arbiter: *"focus is on model training."* Opus put it most precisely
— *"taint/static analysis + unit tests, **but as RL reward not oversight**"* and *"steering-only."*
REAL's static analysis is a **reward function**, never a gate on an artifact; nothing it produces ever
reaches a human. The steering exclusion directs us to *"tag only the paper's inspection/comprehension/
gating contribution"* — and there is none.

> **Rule: `steering` as the *whole* contribution is a Context signal.** A paper that improves the
> generator, with no inspection or gating surface, is upstream of this review's question however good
> the engineering.

**(b) The contrast that makes it non-obvious — Spiess.** Spiess was **kept Core** on what looks like
the same ground (arbiter's own summary: *"tuning quality of generated code"*). The distinction is what
each paper *yields*: Spiess produced an **oversight finding** — that a model's own score cannot be
trusted as a quality signal — which fills a leg of the independence thread. Yao produces a **better
generator**. Under §79, Yao's argument slot is already occupied and it adds no leg.

> **Discriminator: does the paper yield a finding about oversight, or an improvement to generation?**
> Both may involve tuning; only the first belongs at Core.

**(c) TERMINOLOGY HAZARD — "scalable supervision" is a false friend.** REAL claims to be
*"prompt-agnostic and reference-free, enabling **scalable supervision** without manual intervention."*
That is the **ML-alignment** sense: reward signals at *training* time that do not require human labels.
It is **not** this review's sense: human review of AI-generated code at deployment volume. **Same
phrase, different problem, different field.**

**Consequence for the methods chapter:** any keyword search on *"scalable oversight"* / *"scalable
supervision"* will surface RLAIF and alignment work that is out of scope, and this is a plausible
source of false positives in the original screening. Recorded in
`Selection_Criteria_By_Phase.md`; the search-strategy section should state the distinction explicitly
rather than leave a reader to assume the terms were used in our sense.

## 91. `oversight-explanation` rescued at 1/3 — the explanation of a check is a separate object (`PPMTM4DG`, 2026-08-26)

Yu et al., *Fight fire with fire* (**IEEE TSE**, Dec 2024). **Core + Dissertation Primary.** Primary
`ai-review` (3/3). Applied: `oversight-explanation` (codex **1/3**, arbiter-rescued), `assistive`,
`agentic`, `method-experiment`, `risk-security` (3/3 each), `risk-quality` (2/3).

**The rescue and why it is not redundant with `ai-review`.** The paper reports two *distinct*
measurements:
1. **verdict accuracy** — the model misses **67%** of its own incorrect generations and **59%** of its
   own failed repairs → `ai-review` (reliability limits of AI judging AI);
2. **explanation accuracy** — **75%** of the explanations in its self-generated test reports are
   **inaccurate** for incorrect code and failed repairs → `oversight-explanation`.

> **Rule: the explanation of a check is a separate object from the check.** A reviewer reading the
> report to decide whether to trust the verdict is consuming the *explanation*, and it can fail
> independently of the verdict. Papers that measure explanation quality earn
> `oversight-explanation` even when the explanation is machine-produced and the verdict is the
> headline result.

This is the sharper form of the §67-adjacent worry: a check that is wrong is bad; a check that is
wrong **and explains itself persuasively** defeats the human whose job is to catch it.

**Mode: both applied (`assistive` + `agentic`, 3/3 each), and opus cited the tie-rule explicitly** —
completion tasks are snippet-granularity while generation and repair return complete artifacts
reviewed as wholes. Genuine span, consistent with §86e.

**Not applied, left to the arbiter and unaddressed:** `evaluator-reliability` (post-freeze — no model
could propose it; Yu is arguably its purest instance, measuring **one evaluator against ground truth**
rather than model-against-model) and `ai-code-insecurity` (1/3, CodeQL-confirmed vulnerabilities in
27% of completed code). **Both remain open; neither written.** `counterpoint` 1/3, non-modal,
deprecated — nothing written.

**Synthesis-structure note recorded separately** in `Emerging_Themes.md`: the chain *"self-check fails
→ therefore diverse checkers"* is **the review's own synthesis**, since Yu proposes no fix and
Mahmud/Zhu do not cite Yu. Includes the lower-bound caveat (same-session self-check is the most
degenerate configuration) and a closeout action to verify whether the corpus lacks a head-to-head
A-checks-versus-B-checks study.

**Count check run this session:** `cross-model` = 3 papers (Mahmud, Swidey, Zhu), `agent-panel` = 5
(+ Tisi, Wang). **Both are floors, not totals** — the tags are post-freeze, so only arbiter-noticed
instances exist and no systematic sweep has run. Do not report these counts before the restricted
re-run (§10.12).

## 92. "BACKWARDS" — the oversight surface faces the wrong way (`KF5MGIBI`, 2026-08-26)

Yu, Rong, Shen et al., *Fine-Tuning LLMs to Improve Accuracy and Comprehensibility of Automated Code
Review* (Carllm, **ACM TOSEM**, Dec 2024). **Ruled Context.** §42 short-circuit; panel recorded as
reasoning-of-record: `oversight-explanation` primary 2/3, `ai-review` 3/3, `built-system` 3/3,
`general-code` 3/3, `risk-quality` 3/3.

**This overrides a unanimous non-flag — 0 of 3 models proposed demote**, and the paper is strong on
its own terms: TOSEM, a working fine-tuned system, and **RQ2 is a *manual* comprehensibility
evaluation**, not automated proxy metrics. Recorded explicitly because overriding 0/3 deserves the
same visibility as overriding 3/3.

**The ground — direction, not depth.** The arbiter's first framing was *"getting into nuts and bolts
of models, not oversight"*, then sharpened to ***"Backwards."*** That is the operative reason:

> **Our question: humans overseeing AI-generated code.**
> **Carllm: AI overseeing human-written code**, with the human supervising the AI *reviewer*.

The paper states it — *"reviewed diffs are general repository code, not specifically AI-generated"* —
and `general-code` at 3/3 is precisely the flag for it. The comprehensibility insight transfers, but
transferability alone is not the test (§53); the slot is crowded — **18 of 128** papers carry
`oversight-explanation` plus a human-subjects method facet, most already Context.

**FOLLOW-UP REGISTERED — size the "backwards" cluster before the Accept pass.** `general-code` covers
**20 of 128 (16%)**, currently **5 Core · 5 Context · 10 unread**, and the unread ones are
overwhelmingly AI-code-review tools (Bugdar, BitsAI-CR, Rasheed, Dutta, Nimraka, Sun, Jin, SGCR).
**The 5/5 split is not arbitrary — an implicit rule is already operating, and it should be made
explicit before 10 more arrive:**

> **A `general-code` paper earns Core when it yields a transferable *oversight finding*; Context when
> it is a *review tool*.** Core members fit: Mahmud (cross-model routing), Sistla (external formal
> verification), Mitropoulos (LLM reviewers are attackable), Kamalı (vision for AI-era review),
> Abreu (LLMs in release). Context members are tools that review code better. Same shape as §90(b)
> — **finding versus improvement**.

Pre-committing this rule should cut per-paper churn in the Accept band, where most of the remaining
cluster sits.

**Methodological note.** This cluster is the mirror image of the §90(c) terminology hazard: there,
*"scalable supervision"* pulled in alignment work; here, *"AI + code review"* pulls in tooling for
**traditional** review. Both are search-strategy false-positive sources and both deserve a sentence in
the methods chapter rather than silent exclusion.

**PRESERVED — the comprehensibility rubric.** The paper operationalizes what makes an automated check
**reviewable by a human**:

> *"good comprehensibility requires each ACR to (a) accurately **detect and localize** the issue,
> (b) provide [**cause/explanation**], (c) [**repair suggestion**]"*

Pairs directly with `PPMTM4DG` (§91), where **75%** of AI self-generated explanations were inaccurate:
**one paper defines what a good explanation must contain, the other measures how often AI explanations
fail to.** Carry into the oversight-explanation discussion from Context; check at closeout whether
anything else operationalizes it as cleanly.

**DISSERTATION — flagged, not actioned.** Arbiter: *"Might be supporting for dissertation."* Recorded
as a **candidate** for the Supporting bucket on the strength of the comprehensibility rubric, to be
settled with the bucketing schema (see the open design note in `Emerging_Themes.md`) rather than now.
**No collection membership written.**

## 93. Pure measurement is Context — a pre-committed rule for the `ai-code-insecurity` cluster (`4PSM6ZCD`, 2026-08-26)

Zhao et al., *Is vibe coding safe? Benchmarking vulnerability of agent-generated code in real-world
tasks* (SUSVIBES). **Ruled Context**, agreeing with the panel's `demote:context` at 2/3.
`ai-code-insecurity` primary 3/3. §42 short-circuit.

**Ground.** Arbiter: *"focuses on a measurement of AI generated code quality for security… I was
optimistic they might cover agent panel or cross model, but they really didn't."* The paper measures
**what agents produce**; it contributes nothing about **how anyone checks it**.

**Scarcity — the slot is about to be crowded.** `ai-code-insecurity` covers **13 of 128**, but only 3
are adjudicated (**2 Core · 1 Context**) and **10 are unread**, nearly all the same shape and mostly in
the **Accept band**: Fu, Ji, Dora, Ghammam, Bilal Naqvi, Chang, Liu, Irfan Samsyudin, Waseem.

**PRE-COMMITTED RULE — decide the cluster once, not ten times** (same device as §92's `general-code`
rule):

> **An `ai-code-insecurity` paper earns Core when it says something about *oversight* — human
> behaviour, a detection approach, or a gate that fails. It is Context when it is *pure measurement of
> model output insecurity*.**

Consistent with what is already ruled: **Perry** Core (users with AI write less secure code — a human
finding), **Hjazeen** Core (a unified security testing approach — a detection contribution),
**Marri** Context, **Zhao** Context. This is the same finding-versus-improvement shape as §90(b) and
§92, now applied to the Problem side of the taxonomy rather than the Solution side.

**PRESERVED — two items that outlive the demote.**

1. **The tests-pass / security-fails gap, quantified on agentic real-world tasks.** 200 tasks derived
   from genuine vulnerability-fix commits; SWE-Agent with Claude 4 Sonnet reaches **61% functionally
   correct but only 10.5% secure** — roughly **83% of the code that passes its own tests is
   vulnerable**, across **77 CWEs**. This is not merely "AI code is insecure"; it is **the mechanism by
   which insecure code clears a real pipeline**: CI gates run tests, tests pass, and the defect class
   is invisible to the check being run. **Directly relevant to inversion v2 (§89) as a leakage
   pathway** — a gate that passes what it was placed there to stop. Check at closeout whether any Core
   paper states this gap more cleanly; if not, cite Zhao for it from Context.
2. **A failed mitigation on the steering side.** *"preliminary security strategies, such as augmenting
   the feature request with vulnerability hints, **cannot mitigate** these security issues."*
   Generation-side fixes do not close the gap — an argument **for** inspection, reached negatively.
   Pairs with §90: `steering` improves the generator; it does not substitute for a check.

**Note on `problem-statement-anchor`.** Codex proposed it 1/3 on the 80%+ figure. **Not written** —
§42 short-circuits — but flagged: if the anchor slot is still open at closeout, the 61%/10.5% pair is a
stronger candidate than most, and tier does not formally bar it (contrast §82g, where Watson's figure
was refused for being **secondhand**, not for being Context).

## 94. §51 does NOT fire on a deployable checker used for benchmarking (`96XE669R`, 2026-08-26)

Zhong et al., *Vibe checker: aligning code evaluation with human preference* (VeriCode / Vibe Checker).
**Ruled Context**, agreeing with the panel's `demote:context` at 2/3. `rules-based-checks` primary 2/3.
§42 short-circuit; closes the earlier partial (`evaluated-synthetic` already written).

**Ground.** Arbiter: *"focus on measuring single turn vs. multi turn success across different models."*
The paper's own aim is model development — *"to benchmark and develop models against a more
human-aligned notion of code quality beyond functionality."* Per §90(b), a measurement of generation,
not a finding about oversight.

**§51 NEAR-MISS — recorded so it is not mis-cited later.** The assistant expected §51's
reference-oracle exclusion to fire, as it did on `PR4GS7SP` (Cotroneo/ACCA). **It does not.**
VeriCode's 30 verifiers are linters, AST checks and regex tests for properties like type hints and
docstrings; they answer §51's operational question — *could this run on an artifact whose correct
answer is unknown?* — **yes**.

> **Distinction to keep: a checker can be genuinely deployable and still sit in a paper whose
> contribution is benchmarking.** §51 disqualifies checkers that *cannot work without a known-correct
> reference*; it says nothing about checkers that merely *happen to be used* for evaluation. **This
> demote rests on contribution, not on the checker being an oracle.**

**PRESERVED — two items.**

**1. Third instance of "the check that runs doesn't measure what matters."** *"current code evaluation
remains anchored to **pass@k** and captures only functional correctness, overlooking the non-functional
instructions that users routinely apply."*

| Paper | Check actually run | What it misses |
|---|---|---|
| `4PSM6ZCD` Zhao (§93) | tests / CI | security — 61% correct, 10.5% secure |
| **`96XE669R` Zhong** | pass@k | non-functional instruction compliance |
| `PPMTM4DG` Yu (§91) | AI self-verification | 67% of its own errors |

Three independent papers, three different checks, one failure shape. **Cluster candidate: the gate in
place is blind to the defect class that matters.** This is the general form of the leakage pathway
inversion v2 (§89) is built to catch — worth a synthesis paragraph, and worth checking at closeout for
a fourth instance.

**2. The refinement loop trades correctness for style — a mechanism, not just a benchmark result.**
*"single-turn generation better preserves functionality but follows fewer instructions, whereas
**multi-turn editing achieves higher IF at the cost** [of functionality]."*

The **iterative refinement loop — the core vibe-coding gesture — improves what the human can observe
(readability, structure, "feels right") while degrading what they cannot (correctness).** In a
low-inspection or `no-inspection` setting (§81a) that is a concrete mechanism for producing code that
*reads* well and *works* worse, and it compounds automation bias: the loop optimises the exact signal
the human is using to decide whether to trust it. **Carry into the automation-bias / no-inspection
discussion; strong candidate for a survey question about whether teams re-run functional tests after
iterative refinement.**

## 95. §30 considered and NOT exercised — Context with the mechanism preserved (`E689ZAXC`, 2026-08-26)

Zhou & Zhao, *Review makes workers less likely to revise AI output*. **Ruled Context**, agreeing with
a **unanimous 3/3 panel demote**. `general-ai` 3/3 (social media posts, not code); primaries split
`automation-bias` 2/3 / `oversight-theater` 1/3. §42 short-circuit.

**Disambiguation note.** The arbiter first referred to *"Zhou and Zhou"*, then *"Zhou and Zhao"* — the
Light Read queue contains **three** distinct Zhou first-author papers, so the assistant asked rather
than inferring. Resolution: **`E689ZAXC` is a single paper authored by Pete Zhou *and* Yujie Zhao.**
Recorded because the near-miss is instructive — a surname-plus-surname reference can denote one
co-authored paper or two papers, and the earlier `WH2PIBNQ` revert came from exactly this class of
misattribution. **Rule reaffirmed: never infer which paper a ruling attaches to when more than one
candidate matches the surname; ask.**

**§30 exercised? No.** The assistant flagged this as structurally identical to `9MV2IVNU` (Eze, §53) —
`general-ai`, panel-flagged demote, transferable content — where the sole-exemplar exception *was*
taken. The transferable content here is strong: seven experiments, **N = 2,895**, finding that
**expecting review makes workers less likely to revise AI output**, because modification means owning
the errors. That inverts the premise underneath most of the corpus's HITL proposals.

**Arbiter ruled demote regardless.** Recorded as a **worked instance of §30 being considered and
declined** — the exception is *"look at keeping," not "keep"* (§53), and looking at it is what
happened. The mechanism is preserved as framing in `Emerging_Themes.md` rather than promoted, so the
finding stays citable without inflating Core.

**Open, if it recurs:** a code-domain replication would change the calculus, since the objection is
domain rather than mechanism. Flagged there as a revisit condition.

**Housekeeping — SSRN typing artifact.** This item is typed `journalArticle` with no
`publicationTitle`, the known SSRN import artifact (`source:ssrn`). It is one of the ~11 Light Read
items still affected; not corrected here, and still queued for the closeout record-status sweep.
`itemType` remains unreliable for PRISMA stream counts.

## 96. `oversight-explanation` + `steering` legitimately co-occur; and where `evaluated-synthetic` came from (`XRTVITVP`, 2026-08-26)

Zhou et al., *Steering LLMs via scalable interactive oversight*. **Kept Core over a unanimous 3/3
panel demote flag.** Primary `oversight-explanation`; `hitl-workflow`, `steering`, `non-developer`,
`framework`, `built-system`, `agentic`, `evaluated-synthetic`, `method-experiment`. Rejected
`oversight-scaling-inversion` (2/3). Added to **Dissertation Supporting**.

**(a) The assistant argued the wrong way first — record of the correction.** The initial position was
that `oversight-explanation` cannot apply because the human never sees generated code (the evaluation
pivot is a **PRD**, not an artifact), making this steering-only and therefore Context under §90(a).
**The precedent refutes it:** `ZH6QIU8A` (Kasibatla, *Decision-Oriented Programming with Aporia*) is
already Core with **`oversight-explanation` as primary and `steering` as a human-written facet**, on an
essentially identical mechanism — an agent proactively eliciting structured decisions from the human.

> **Rule: `oversight-explanation` and `steering` are not mutually exclusive.** A design that gives the
> human a *structured decision surface* earns `oversight-explanation` even when the surface sits
> **before** generation and no artifact is ever displayed. §90(a)'s steering-only Context signal
> applies to papers that improve the **generator with no human control surface at all** (Yao/REAL), not
> to papers that relocate human control upstream.

**(b) `oversight-scaling-inversion` REJECTED at 2/3 — §88 leakage test.** The paper formalises a
**capability** gap (*"non-experts cannot validate autonomous software outputs"*), but nothing escapes a
review that should have caught it. No leakage, no inversion. Third consecutive rejection of this theme
on the same test (Xu §83, Yang §86, here) — see the §87 closeout action.

**(c) §34 fork respected — two genuine measurement events.** `evaluated-synthetic` and
`method-experiment` both apply because the paper runs **two separate evaluations**: a simulated-user
study (Table 1, module-level PRD scores) and **§4.4 "Real-user Study on Alignment Effectiveness — We
hired a non-expert to engage in our interaction system."** Not the `8MXATG38` failure pattern; two
events, two classifications.

**(d) PROVENANCE — this is one of the papers that produced `evaluated-synthetic`.** Arbiter: *"This was
one of the papers that led to us introducing synthetic. They concocted the data from other sources."*
Recorded because `evaluated-synthetic` is one of the six **post-freeze** tags the panel could never
propose (`Theme_Tagging_Calibration.md` §11.9), and the methods chapter should be able to say **which
papers forced each addition** rather than presenting the vocabulary as arriving fully formed.

**(e) Cluster action — DECISION SURFACE.** At the arbiter's direction, the cluster members were placed
in **Dissertation Supporting**: `XRTVITVP` (Zhou), `ZH6QIU8A` (Aporia), `CI93QRUH` (HiLDE) — none had
been in Primary or Supporting, all three sat only in Dissertation *Candidates*. Mechanism staged in
`Emerging_Themes.md`, including the two design variables (**altitude**, **options with analysis**)
drawn from the arbiter's system-building experience and explicitly marked as a **reading lens, not
corpus evidence**.

**(f) Dissertation Primary declined.** The population is **non-expert entrepreneurs building without
developers**; the dissertation's survey targets organisations governing professional developers.
Supporting fits — the paper is the contrast case for what oversight becomes when nobody can read the
code.

## 97. Consistency beats scarcity when two same-shape rulings already exist (`XK3P9C96`, 2026-08-26)

Zhou et al., *When Should Users Check? Modeling Confirmation Frequency in Multi-Step Agentic AI Tasks*
(**CHI 2026**). **Ruled Context**, agreeing with a unanimous 3/3 panel demote. Added to **Dissertation
Supporting**. §42 short-circuit; panel recorded: `risk-routing` primary 3/3, `hitl-workflow` 3/3,
`general-ai` 3/3, `agentic` 3/3, `built-system` 3/3, `method-experiment` 3/3, `method-self-report` 2/3,
`non-developer` 2/3.

**The tension, recorded because it was genuine.** §53's two legs pointed opposite ways:

- **Transferability: strong.** The model is parameterised by error rate and rollback cost, both of
  which agentic coding has (rollback = redo the PR). Results are real — 48-participant within-subjects
  study, **81% preferred intermediate confirmation**, **13.54% task-time reduction**.
- **Scarcity: the specific slot looked EMPTY.** This is the only corpus paper that **computes how much
  oversight to apply**. Others ask *whether* to review or *what to show*; this asks **how often** and
  solves it as a scheduling problem. The nearest neighbour, `7ZMU5AIF` (Grunde-McLaughlin), occupies
  **trace design** — what the human sees — not timing.

**What decided it: consistency with rulings already made.** Two structurally identical papers are
already Context — `7ZMU5AIF` (general-ai, agentic oversight, **three user studies**, measured
error-finding time) and Mozannar's *Magentic-UI* (general-ai, HITL agentic, human study). Keeping this
one would contradict both without revisiting them.

> **Rule: where the §53 legs disagree, an existing ruling on the same shape outranks an empty slot.**
> A slot that looks empty is often an artefact of how narrowly it was described; a prior ruling on a
> matching paper is evidence about where the boundary actually sits. **Revisit the earlier rulings or
> follow them — do not silently split them.**

Supporting observation: the corpus's Core `general-ai` keeps (Eze §53, Zhu, Jessee, Swidey) are all
**controls or mechanisms that transfer to governance**, not HCI interaction studies. `XK3P9C96` is the
latter.

**Dissertation Supporting, though**, because the frequency question is directly survey-relevant:
*does your org confirm every step, only at the end, or something in between — and was that chosen or
defaulted?* The paper's answer — that the right frequency is **computable** from error rate and
rollback cost — reframes a question most orgs will have settled by accident.

**Two tag corrections against the arbiter's initial list:**
- **`oversight-explanation` declined** (panel 1/3). The contribution is **timing**; the clickable
  traces are incidental. **Trace design belongs to `7ZMU5AIF`**, and the intuition appears to have been
  tracking that paper's territory.
- **`evaluated-synthetic` declined — §34 fork answers it.** This is a human-subjects study
  characterising **behaviour in the world**, so the **method facets fire and the ladder does not**
  (`method-experiment` 3/3, `method-self-report` 2/3). Worth stating because the arbiter asked
  specifically whether the new tags applied: **the ladder is for tool evaluation, not for studies of
  people.**

**Preserved: the CDCR pattern** — Confirmation–Diagnosis–Correction–Redo, a descriptive model of what
the act of overseeing actually consists of. The corpus is thin on accounts of the oversight *act*
itself (as opposed to mechanisms that invoke it); pairs with the decision-surface cluster (§96e).

## 98. A closed autonomous repair loop is not a Detect→Fix oversight pipeline (`VZ27QUPQ`, 2026-08-26)

Zhuo et al., *Identifying and mitigating API misuse in large language models* (**IEEE TSE**, 2026-03).
**Ruled Context** — arbiter: *"evaluation paper, demote."* **Overrides a unanimous NON-flag: 0 of 3
models proposed demote**, and the panel made `ai-review` primary 2/3. §42 short-circuit.

**Why the panel reached for `ai-review`, and why it is wrong here.** The mitigation is **Dr.Fix —
"Detect-reason-Fix"** — which reads like the taxonomy's own **Detect → Triage → Fix** pipeline, so the
name alone invites the tag. But the loop is **closed and autonomous**: it always attempts a repair,
scored by **BLEU** against baseline prompting. No human sees anything, and there is **no refusal
state**.

> **Discriminator: does the mechanism have a state in which it declines to proceed?** §63 established
> that autonomous fixing does **not** disqualify a paper — `ZORO`'s active rules gate *and then* drive
> a fix. The difference is that **ZORO can refuse; Dr.Fix cannot.** A repairer with no gate is **code
> improvement**, not oversight. Detect-in-the-name is not Detect-in-the-taxonomy.

**The measurement half is likewise upstream.** A large-scale characterisation of API-misuse patterns
across StarCoder-7B, Qwen2.5-Coder-7B and GitHub Copilot (3,209 method-level and 3,492 parameter-level
misuses, manually annotated) is **pure measurement of model output** — the §93 rule, applied on the
quality side rather than the security side.

**FACET INCONSISTENCY FLAGGED, NOT FIXED** (§42 — Context tag depth has no Phase-6 consumer). The
item carries **`evaluated-synthetic` and `method-mining`** from the earlier partial pass, while the
panel proposed **`method-experiment` 3/3**. Two concerns:
1. **`method-mining` looks wrong.** The corpus analysed is **LLM-generated** code, not mined
   repositories, and the findings characterise **the models**. The cheatsheet's *subjects-may-be-
   systems* rule sends that to `method-experiment`; `method-mining` requires the artifact analysis to
   *be* a finding about real repos (`NZJST99D`: 33k PRs characterised).
2. **The §34 fork may still be satisfied** if the misuse study and the Dr.Fix evaluation count as two
   events — plausible, but unverified.

**Queued for the closeout facet sweep** alongside the other Context-tier tag questions; recorded here
so the inconsistency is discoverable rather than silently inherited into `final:*`.

### 98a. §51 DOES fire on `VZ27QUPQ` — and the matched pair with §94

Follow-up after the arbiter re-read the paper and asked whether anything had been missed. **Nothing
had — and the ground is firmer than first stated.**

Zhuo's misuse identification is **reference-grounded**:

> *"since **human-written code is used as ground truth**…"* · *"we treat it as an **approximate ground
> truth**"*

So §51's **reference-oracle exclusion fires**: the Detect step **cannot operate on an artifact whose
correct answer is unknown**, exactly as with `PR4GS7SP` (Cotroneo/ACCA). It is a benchmarking oracle
wrapped in a repair loop, not a deployable checker. This is a **stronger** basis for the demote than
§98's no-refusal-state argument, and it should be cited first.

**It also closes off the residual possibility the arbiter raised** — *"maybe a risk signal, but that is
it."* API-misuse density would make a plausible producer-independent routing signal, but it is **not
operationalisable from this method**: computing it requires the human-written reference that does not
exist at review time. **Not a latent contribution — a measurement that can only exist in a lab.**

**Matched pair for §51, both from this session:**

| Paper | Checker | Runs without a reference? | §51 |
|---|---|---|---|
| `96XE669R` Zhong / VeriCode (§94) | linters, AST checks, regex | **yes** | **does not fire** — demoted on contribution instead |
| `VZ27QUPQ` Zhuo / Dr.Fix (§98) | comparison to human-written ground truth | **no** | **fires** |

Useful for the write-up: the two papers look alike from the abstract — both build checking machinery
and both were demoted — but the *reasons differ*, and conflating them would make §51 look like a
general anti-benchmark rule rather than the specific deployability test it is.

## 99. Three post-freeze tags land at once; and §83's `intro-framing` rule refined (`TA6GIUK2`, 2026-08-26)

Zietsman, *The specification as quality gate: three hypotheses on AI-assisted code review*.
**Core + Dissertation Supporting.** Primary `ai-review`; `rules-based-checks`, `evaluator-reliability`;
`agentic`, `risk-quality`, `method-experiment`, `intro-framing`, `cross-model`, `agent-panel`.
Rejected `oversight-scaling-inversion` (2/3). **Final paper of the Light Read pass.**

**(a) Three post-freeze tags apply to one paper** — the largest single-paper cluster of them so far, and
a good illustration of why the restricted re-run (§89, §10.12) is needed: **the panel could not have
proposed any of them.**
- **`cross-model`** — Experiment 3 is *"a cross-family panel of four models from three families"*, run
  against a same-family baseline. Fourth corpus instance (Mahmud, Swidey, Zhu, this).
- **`agent-panel`** — four models reviewing the same artifacts.
- **`evaluator-reliability`** — **its strongest instance to date.** The arbiter scoped this tag as
  *"this LLM compared to that LLM"*; Zietsman compares **evaluator configurations** (same-family vs
  cross-family panel) against a BDD ground truth and reports detection rates per condition. Measured,
  not asserted — better fit than Spiess or Zhu.

**(b) `evaluated-synthetic` DECLINED — §34 fork, subjects-may-be-systems.** The planted-bug corpus is
the **stimulus**, not the object of study; the subjects are **third-party models**, so the rule sends
this to `method-experiment` (3/3) and the ladder does not fire. Same reasoning as `XK3P9C96` (§97).
**Worth stating as a pattern: a contrived corpus does not by itself trigger the ladder — ask what the
findings characterise.**

**(c) §83 REFINED — the `intro-framing` test.** §83 stated the facet *"never applies to a study that
produces primary evidence."* **Too strong.** Xu's DiD evidence *was* the contribution; here the
**argument** is the contribution and the experiments illustrate it — the author's own framing is
*"directional evidence, not a controlled demonstration."*

> **Refined test: is the evidence the contribution, or does it illustrate one?** `intro-framing`
> applies to the latter even when experiments are present. Presence of evidence is not the
> discriminator; **evidentiary weight-bearing** is.

**(d) `oversight-scaling-inversion` REJECTED at 2/3 — §88 leakage test, fourth consecutive.** The
failure demonstrated is a **correlated blind spot** (AI review misses domain-opaque bugs), not a
capacity failure. No volume mechanism is involved. Cf. Xu (§83), Yang (§86), Zhou (§96b).

**(e) `counterpoint` 3/3 → NOT `scaling-dissent`.** The paper argues *this particular delegation fails
without an external reference* — thesis-**supporting**. Fifth measured polarity instance; deferred to
the closeout deprecation sweep.

**(f) Substantive contribution recorded in `Emerging_Themes.md`:** the independence thread's gradient
conflated **decorrelation** and **reference** into one axis. Zietsman separates them — *"model diversity
does not supply ground truth"* — which means a four-vendor panel with no specification produces
**agreement**, not **correctness**. This corrects our own framing and links the specification cluster
(Töpfer, `XRTVITVP`) to the panel cluster (Mahmud, Swidey, Zhu) as complementary rather than competing.

## 100. LIGHT READ BAND CLOSED — completeness audit and outstanding sweeps (2026-08-26)

**78 of 78 papers carry `s5:read`. Core 35 · Context 43. Every Core paper has a human primary theme.**
No partials remain. T1 snapshot written to
`slr-phase4/data/tags-v213/tag_layer_stats_T1-lightread_2026-08-26.json`.

**Reliability figures held steady across the pass** — worth reporting, because stability is itself
evidence the arbiter did not drift:

| | T0 (57 papers) | T1 (65 papers) |
|---|---|---|
| human origination | 8.0% | **7.7%** |
| override rate on panel-modal proposals | 8.3% | **8.8%** |

*(n counts papers carrying an arbiter layer; the 13 Context papers ruled under §42's short-circuit have
no `cal:human` tags by design.)*

### Outstanding sweeps, now sized

**1. Deprecated `counterpoint` — 8 papers still modal and unrejected** (5 Core, 3 Context): Eze 3/3,
Zietsman 3/3, Choudhuri 3/3, Tilbury 3/3, Zhou 3/3, Wang 2/3, Xu 2/3, Zhu 2/3. Under §45/§46 each
survives into `final:*` on silence. **Handle as one bulk act** (§56 deprecation), not per paper.

**2. `oversight-scaling-inversion` silent-modal — only 2 remain in this band**, both Context
(Choudhuri 3/3, Kudriavtseva 2/3). **This materially revises §87's estimate.** That figure of 15 was
corpus-wide across all 128 Phase 5 papers; the Light Read pass has since resolved nearly all of its
share through explicit adjudication — including **four consecutive rejections** on the §88 leakage test
(Xu §83, Yang §86, Zhou §96b, Zietsman §99d). **The remaining burden sits in the Accept and Full Read
bands**, which is where the closeout re-check should concentrate.

**3. SSRN `itemType` artifact — 9 Light Read items** typed `journalArticle` with no
`publicationTitle`: `WBS9U5N7` Alami, `NGIH5T4C` Batte, `9MV2IVNU` Eze, `34ELRWJH` Goodhue,
`LGZXFLSJ` Hein, `JVWUYDME` Jessee, `27YULT5I` Sharma, `5RLPIA3K` Swidey, `E689ZAXC` Zhou. Queued for
the record-status sweep; **`itemType` remains unreliable for PRISMA stream counts**.

**4. Facet inconsistency on `VZ27QUPQ`** (§98) — `method-mining` looks wrong on LLM-generated code;
flagged, not fixed, per §42.

### Pre-committed rules now in force for the Accept band
Recorded together because the Accept pass will hit all three repeatedly:
- **§92** — a `general-code` paper is Core when it yields a transferable oversight **finding**, Context
  when it is a review **tool**. ~10 unread instances waiting.
- **§93** — an `ai-code-insecurity` paper is Core when it says something about oversight, Context when
  it is **pure measurement of model output insecurity**. ~10 unread instances waiting.
- **§88 leakage test** — `oversight-scaling-inversion` requires risky code to **escape** a review that
  should have caught it; burden, queue growth, displaced work and absorbed rework do not qualify.

## 101. Closeout decisions — deprecation handled at computation; SSRN sweep deferred and scoped (2026-08-26)

Three arbiter rulings following the §100 audit.

**(a) `counterpoint` — NO bulk reject sweep. Exclude deprecated tags at the `final:*` computation
step instead.** Arbiter: *"OK to leave counterpoints on, we will likely not use them but let's not lose
the information."*

**Clarification recorded because it affected the choice:** rejecting would **not** have lost
information — the layers are additive and `cal:<model>:*` is never edited (§10.7), so a
`cal:human:reject:*` only changes what `final:*` computes. Both options preserve the record. The
computation-step exclusion is nonetheless better: **one rule instead of eight writes**, the model layer
untouched, and the §56 deprecation stays a single auditable act rather than being scattered across
papers.

> **Rule for closeout: `final:* = panel modal ∪ human endorsements − human rejections − deprecated
> vocabulary.`** The fourth term is new; `counterpoint` is its first member. Any future deprecation
> joins it without needing a per-paper sweep.

**(b) CANDIDATE FINDING — the field asserts the inversion far more often than it demonstrates it.**
Arbiter, on the v2 tag: *"Means that our tighter definition focusing on studies of actual leaks is not
common."* That is a **reportable observation about the literature's evidentiary standards**, not merely
a tagging outcome:

| | count |
|---|---|
| papers with `oversight-scaling-inversion` proposed by ≥1 model | **32 of 128** |
| panel-modal (≥2/3) | 21 |
| arbiter-endorsed under the **loose** reading | 6 |
| expected under the **§88 leakage test** | fewer — the v2 re-run will fix the number |

Four consecutive rejections on the leakage test (Xu §83, Yang §86, Zhou §96b, Zietsman §99d) all turned
on the same thing: the paper described **burden** and asserted the consequence. **The v2 re-run (§89)
therefore measures something worth reporting — the gap between how often the inversion is claimed and
how often an escape is actually documented.** Keeping v1 and v2 on distinct slugs is what makes that
gap computable; a redefinition in place would have erased it.

**(c) SSRN record sweep — DEFERRED to after the Accept band, as one run.** Scoped: **12 mistyped items
across Phase 5** (9 Light Read, 2 Accept, 1 Full Read; 2 further SSRN items are correctly typed, so the
artifact is not universal).

**Two distinct jobs, only one needing a lookup:**
1. **Type correction — deterministic, no API.** `source:ssrn` + `journalArticle` + empty
   `publicationTitle` ⇒ `preprint` with `repository: SSRN`. Scriptable.
2. **Published-version check — the substantive half.** Has the working paper since appeared in a
   journal? **OpenAlex first** (skill installed), **Semantic Scholar as fallback**; both link
   preprint↔published versions by DOI and title. **Not Google Scholar territory**, though a residue of
   perhaps 2–4 poorly-indexed SSRN working papers may need manual checking.

**Risk to carry:** if a published version is materially revised, an adjudication made on the preprint is
stale. The **Zhu precedent** (`BLR3XE3I`→`DN9R4PDQ`, converted in place, full texts diffed to confirm no
quoted passage moved) is the template. Tractable for 12 papers at closeout.

## 102. DISCLOSURE — `Tag_Cheatsheet.md` was edited three times during the pass; why the measurements still stand (2026-08-26)

Surfaced during the pre-merge review of PR #13. §10.3 describes the instrument as *"v2.13 … expressed
as `Tag_Cheatsheet.md` plus a fixed prompt prefix"*, and §41 requires gauge constancy — so an edit to
that file during an active measurement pass needs disclosing rather than leaving in the diff.

**What changed** (all in commit `b424416`, early in the branch):
1. `scaling-dissent` — four guards added (§56, §58), with the two rejected candidates as worked cases.
2. `framework` — the §49b **conformance-requirement ≠ architecture** clause.
3. `method-*` — §57's **instrumentation ≠ contribution**, plus the one-event-one-classification
   corollary and the `8MXATG38` worked failure.

**Why the measurements remain comparable:**

- **The taggers never saw any of it.** `Tag_Prompt.md` is **unchanged on this branch** (verified by
  diff against `origin/main`). Every changelog entry making these refinements recorded *"Not propagated
  to `Tag_Prompt.md` (§41)"*, and that held. **The panel ran on a genuinely frozen instrument for all
  9 runs of all 128 papers.**
- **No vocabulary was added or removed**, and **no tag's extension changed.** All three edits are
  clarifications of existing definitions, each attached to a worked case that was already decided.
- **They are arbiter-side reference material**, not measurement apparatus.

**The residual effect, stated honestly.** The *arbiter* read a slowly-sharpening reference sheet across
the pass, so rulings late in the pass had more written guidance than early ones. That is a real if small
asymmetry and cannot be undone retrospectively.

**Weak evidence against drift:** the arbiter-layer rates were stable end-to-end — origination
**8.0% → 7.7%**, override **8.3% → 8.8%** between T0 (57 papers) and T1 (65 papers, §100). If the
sharpening reference sheet were materially changing arbiter behaviour, the override rate would be
expected to move; it did not. **Not proof — the metric is coarse and the sharpening was small — but it
is the check available, and it points the right way.**

**Rule going forward:** clarifications belong in this changelog, and **`Tag_Cheatsheet.md` should not be
touched again before the versioned cut** (§41). If a clarification is urgent enough to write down mid-
pass, it is urgent enough to write *here* instead. Re-check the diff of both instrument files at every
PR from now on.

## 103. AMENDS §102 — the prompt is the instrument; frozen capture created (2026-08-26)

§102 disclosed three mid-pass edits to `Tag_Cheatsheet.md` and reasoned that the measurements still
stood. **The reasoning was right; the file model behind it was wrong, and the correction makes the
position stronger, not weaker.**

**What was actually the case.** `Tag_Prompt.md` is not a "prompt prefix" wrapped around the cheatsheet —
**it is a self-contained frozen copy** of the cheatsheet vocabulary plus the task block and JSON output
contract. Verified by vocabulary diff: **the prompt enumerates 37 slugs, the cheatsheet 38, and the
difference is exactly `scaling-dissent`** — added to the cheatsheet at §56 and, exactly as every
changelog entry claimed, never propagated.

So the two files have distinct roles, and only one of them was ever the gauge:

| File | Role |
|---|---|
| **`Tag_Prompt_v2.13.md`** *(new)* | **Instrument of record** — verbatim capture of what the taggers ran on. Frozen; never edit. |
| `Tag_Prompt.md` | Operative prompt; substantively identical to the capture. |
| `Tag_Cheatsheet.md` | **Living arbiter reference — not the instrument.** Now headed as such. |

**Consequences:**
1. **§102's conclusion is upgraded from "the edits didn't reach the panel" to "the edits *could not
   have* reached the panel."** The panel read a physically separate file that was never touched. The
   residual concern §102 raised — that the *arbiter* read a sharpening reference across the pass —
   still stands and is still the honest caveat.
2. **§10.3 of `Theme_Tagging_Calibration.md` was wrong and is corrected.** It described the instrument
   as *"`Tag_Cheatsheet.md` plus a fixed prompt prefix"*, which inverts the relationship. **The
   write-up must cite `Tag_Prompt_v2.13.md`**, not the cheatsheet.
3. **The proposed `Tag_Cheatsheet_v2.13-FROZEN.md` was dropped as redundant** — the prompt capture
   already contains the frozen vocabulary, and a third file with the same content would be one more
   thing to keep in sync.

**Convention adopted (arbiter):** *"We will be updating prompts in future, so let's have a capture of
what was used separate from the git log."* **Every prompt change gets its own
`Tag_Prompt_v<version>.md` capture.** `Tag_Prompt_v0.md` already preserved the pre-calibration
original; `Tag_Prompt_v2.13.md` now preserves the version behind all 9×128 panel runs. The gauge's
history is therefore legible from the repository tree, without archaeology through commit history —
which matters because the methods chapter needs to state *which* instrument produced *which* numbers,
and the T0/T1/T2 snapshots (§89, §100) are only interpretable against a named instrument version.

**Standing check added:** diff **both** instrument files against `origin/main` at every PR, and treat
any movement in `Tag_Prompt.md` as a versioned cut requiring a new capture and a changelog entry.

## 104. Oversight machinery used as EVALUATION APPARATUS is an instrument, not a contribution (`VG8PSMM7`, 2026-08-27)

**First paper of the Accept band.** Adnyana & Schwung, *Benchmarking and validation of prompting
techniques for AI-assisted industrial PLC programming* (*Machine Learning with Applications*, 2026).
**Ruled Context** despite **no demote flag from any of the three models**. §42 short-circuit.

**The tension the arbiter named.** *"The primary focus of the paper is to evaluate LLMs' ability to
generate code for their particular scenario. However, they used some of the techniques that might be
applicable to scaling human oversight in the setup of their pipeline — e.g. using LLMs to review the
code. So while the focus of the paper would yield a demote, the methods of the paper are aligned."*

**PRE-COMMITTED RULE** — same device as §92/§93, because this shape recurs:

> **Oversight machinery used as *evaluation apparatus* is an instrument, not a contribution.** A paper
> earns Core for it only when the machinery is **argued for** — proposed, justified, or evaluated as
> such — never when it is merely **used** to measure something else.

This generalises §57's instrumentation-≠-contribution rule from the method facets to the **tier
decision**, and it is the same shape as §84's offered-for-reuse test for `metrics`. **Three rules, one
principle: what a paper *uses* is not what a paper *contributes*.** Consistent with §94 (Zhong — a
deployable checker inside a benchmarking paper) and distinct from §98a (Zhuo — where §51 fired because
the checker was reference-grounded and could not have been deployed at all).

**Expected recurrence in this band:** Bhatnagar, Ghammam, Salem, Şeker look like the same shape.
Sollenberger, Raghavendra and Karakaya sit on the **other** side of the line, where the checker *is* the
argument — those are Core-eligible on the same rule.

### 104a. What the rule discards, and the mitigation

**The tier decision throws away real evidence**, and the arbiter identified why it matters:
*"'what that loses' sounds a lot like risk routing."*

> **Core/Context is itself a routing decision, and Context is our un-routed remainder.** Downstream,
> demoted papers get read as "nothing here" — precisely the failure staged as a tripwire from `ZBF86IJM`
> (§79): **the absence of a routing signal is interpreted as a clean bill of health.** The review's own
> method exhibits the failure mode the review documents.

**Mitigation adopted — the validation-apparatus harvest.** A paper's methods section is evidence about
**what its authors considered adequate validation of AI-generated code**. Nobody required Adnyana's team
to reject BLEU as sufficient, add a semantic LLM check, and still gate safety-critical output behind a
human expert — that layering is a **revealed belief about where machine checking runs out**. It is
evidence about norms, harvestable regardless of tier.

**Established:**
- Zotero collection **`Dissertation Lit Review / 04 - Validation Apparatus`** (`XPPEXKBN`) — additive,
  orthogonal to SLR tier.
- **`Methodology/Validation_Apparatus_Harvest.md`** — running record: layers, automated components,
  AI-as-checker (and whether cross-vendor), human position, escalation trigger, stated rationale, domain.
- **Scope: the Phase-5 128 first.** Hard constraint — full texts exist only for those. Measure the
  yield, then decide on expansion; if expanding, use **targeted retrieval**, not an abstract scan, since
  abstracts rarely describe validation apparatus.
- Accumulates during the Accept pass, with a back-fill over the Light Read band at closeout.

**`VG8PSMM7` is entry one:** BLEU → LLM-in-the-Loop (four dimensions) → HITL expert review, with
generation and syntax-checking split across **different vendors** (DeepSeek/Gemini generate;
ChatGPT-4o/Copilot check). The human sits **terminal and scoped to safety-critical** — not asked to
check everything, only what the domain marks as dangerous.

## 105. A filter that SELECTS among candidates is part of the generator (`FZK2QB5A`, 2026-08-27)

Alshahwan, Harman et al. (Meta), *Assured offline LLM-based software engineering* (InteNSE '24
keynote). **Ruled Context** despite **no demote flag from any model** and `remediation-gating` primary
3/3. §42 short-circuit. Added to `04 - Validation Apparatus`.

**§104 does NOT carry this one — recorded because the rule is one paper old.** Under §104 the filters
here *are* argued for, not apparatus, so §104 points **Core**. The demote rests on two other grounds.

**(a) NEW DISCRIMINATOR — fitness function vs gate.** The authors characterise their own mechanism:

> *"Assured LLMSE can be thought of as a kind of **Genetic Improvement** in which LLMs are used as the
> operator for generating candidate solutions. The filters we describe in this paper can be thought of
> as **playing a similar role to fitness functions** for generate-and-test approaches to GI."*

> **A filter that *selects among generated candidates* is part of the generator. A filter that *gates a
> deliverable* is oversight.** Same machinery, different position in the pipeline. Generate-many-and-keep-
> the-survivors is **search**; refuse-this-artifact is **oversight**.

This explains `steering` at 3/3 — the panel registered the generator-side placement without being able
to name it. Distinct from §98's test (*does the mechanism have a refusal state?*): Alshahwan's filters
**do** refuse — *"either the candidate code passes through the filter or it is discarded"* — but they
refuse **candidates inside a search loop**, not deliverables at a gate. **Both tests are needed; a
mechanism can pass §98 and still fail this one.**

**(b) §53 second leg fails decisively — the family is better served elsewhere.** Arbiter: *"what it
discusses is kinda standard practice now. Do we have papers that more firmly establish the goal
oriented practice?"* Corpus check on `remediation-gating`:

| Tier | Paper | Evidence |
|---|---|---|
| Core | Ma — *ZORO: active rules for reliable vibe coding* | built-system · evaluated-synthetic · **method-field-study** |
| Core | Töpfer — *feedback-based automated verification* | built-system · evaluated-synthetic |
| unread | Shinde — *STELP* | built-system |
| unread | Vargas — *SLEAN* | built-system |
| **this** | **Alshahwan** | **design-only — nothing built, nothing run** |

**Alshahwan is the only member of its own family with no implementation and no evaluation.** ZORO —
the paper that produced §63's discriminator — even has a field study.

**(c) The one thesis-relevant sentence is undeveloped.** *"The human plays the role only of final code
reviewer, as they would do with code generated by other human engineers"* appears **once, in the
abstract**, and nowhere in the remaining 5,700 words. **Framing, not argument** — it cannot be cited as
a position on where oversight sits. The Meta stakeholder interviews are likewise background for one
design choice (local optimisation), not evidence production — **no `method-self-report`**.

### 105a. §77 RESOLVED — Mitchell stays Core

Mitchell (`6ZW9QNQH`) was flagged demote-candidate contingent on whether any paper delivered
**autoformalization plus feedback**. Töpfer delivered the feedback half with hand-authored constraints
(§77); **Alshahwan was the last candidate and does not close it.** Its twin guarantees are
*"does not regress the properties of the original code"* — **regression against existing behaviour, not
specifications automatically derived from intent.**

**The gap Mitchell names is therefore unclaimed by the corpus, and Mitchell survives as its position
statement.** Decision closed; the follow-up in `Emerging_Themes.md` is marked resolved.

## 106. An oversight claim needs a contrast that VARIES the oversight (`P837LJWE`, 2026-08-27)

Bhatnagar, *Modernization of enterprise payment infrastructure: a case study on LLM-assisted migration
of legacy distributed systems* (*Array* 30, 2026). **Ruled Context** despite **no demote flag from any
model**, `hitl-workflow` primary 3/3, and `adopted` 3/3. §42 short-circuit. Added to
`04 - Validation Apparatus`.

**Recorded at length because the assistant argued Core three times and was wrong three times.** Each
of the arbiter's corrections removed a ground, and the accumulated effect is the ruling.

**(a) THE CONFOUND — a pre-committed rule.** The headline outcome (67% production-error reduction)
compares **legacy human-authored code** against **AI-refactored code**. There is no arm without the
HITL, so the improvement cannot be attributed to the oversight — only to the modernisation. Any
competent rewrite of a 15-year-old monolith would improve error rates.

> **An oversight claim requires a contrast that VARIES the oversight.** Comparing AI-with-oversight
> against no-AI measures **the AI**, with oversight held constant. Any paper reporting *"our
> HITL-governed AI process outperformed the previous manual process"* has measured the AI.

Expect this in the industrial case studies still unread in this band.

**(b) CONFIRMING A TENET IS NOT CONTRIBUTING A FINDING.** Arbiter: *"There is no insight about
oversight, just that it was important."* And the calibration that makes it operational: *"this is
oversight in the way of a human inspecting code generated in vibe coding while in an IDE is
oversight."*

> The corpus does not need more evidence that oversight matters — that is established many times over.
> It needs evidence about **what makes oversight work**. A paper showing oversight was present and
> important supplies an **instance**, not a **finding**. **Instances belong in the harvest; findings
> belong in Core.**

**(c) The three RQs, and why none of them lands.** RQ1 measures lead time (productivity). RQ2 is the
confounded comparison in (a). RQ3 — *"What specific human-centric governance protocols, such as
'Strategic Rollbacks,' are required to ensure PCI-DSS compliance…"* — **does** engage oversight, but
the arbiter's read is decisive: *"The compliance was also very light. The central focus was not related
to compliance. It showed up as a follow-up."*

**(d) `intro-framing` DECLINED** (the arbiter's own suggestion, on the reasoning that the paper
confirms a central tenet). §99c settles it: **the test is whether the evidence is the contribution or
merely illustrates one.** Here the evidence *is* the contribution, however confounded — so this is an
empirical paper, not a framing one. **"Confirms a tenet without insight" has no tag; that is what the
harvest is for.**

**(e) LARGEST CORRELATED FACET ERROR OBSERVED — three unanimous 3/3 facets, all wrong.**

| Facet | Panel | Fails |
|---|---|---|
| `framework` | **3/3** | §49 span rule — one migration, one job. The `WUUDHL8R` negative case exactly. |
| `built-system` | **3/3** | No oversight artifact was built. The migrated application is the **object** of the work, not the mechanism. §39 sends process to the theme. |
| `regulatory-compliance` | **3/3** | §78 — PCI-DSS is a **constraint input** to the migration, not the contribution. As with Watson (§82c) and `WUUDHL8R` (§44). |

`hitl-workflow` primary 3/3 and `adopted` 3/3 both hold. **Not written** (§42), but recorded: a paper
describing an industrial deployment reliably triggers the artifact-maturity cluster whether or not an
artifact exists. **Watch for this in the remaining industrial case studies.**

**(f) `adopted` is an evidence rung, not a relevance criterion.** It is genuinely scarce — 5 of 128,
and the three previously adjudicated are all Core — but it describes **maturity**, not what a paper
tells us. A production deployment with nothing to say about oversight is still Context.

## 107. §52's FIRST CLEAN POSITIVE under the leakage test (`JQPPKSFQ`, 2026-08-27)

Branco, Canelas, Gamboa & Fonseca, *LGTM! Characteristics of Auto-Merged LLM-based Agentic PRs*
(2026). **Core.** Primary `oversight-scaling-inversion`; `agentic`, `method-mining`,
`problem-statement-anchor`.

**(a) The theme's first positive after four consecutive rejections** (Xu §83, Yang §86, Zhou §96b,
Zietsman §99d). §88's leakage test is satisfied in the abstract's opening sentence:

> *"AI tools are generating code **faster than humans can properly review it**, leading repositories to
> **skip review and auto-merge** agentic Pull Requests directly."*

Volume exceeds capacity · review is skipped · **code merges anyway**. It is also the canonical case
§52's own definition names — *"PRs auto-merged unreviewed."* **After the run of rejections this matters
for the write-up: the tag is narrow, not empty.**

**(b) `problem-statement-anchor` APPLIED (opus 1/3, rescued) — and it is the corpus's best instance.**
A **primary** mining study quantifying unreviewed auto-merge across ~33k PRs, anchoring the *overall*
two-part frame rather than a sub-argument. Contrast the two near-misses: Watson's 20–30% figure was
refused as **secondhand** on a lit-review (§82g), and Zhao's 61%/10.5% was flagged only as a fallback
candidate (§93). **This one is first-hand, corpus-scale, and directly about the inversion.**

**(c) NOT applied — `ai-review` (0/3).** Proposed by the arbiter, declined on inspection: **the paper is
about review being *absent*.** Auto-merge is the *skipping* of review, not a machine performing it.
Nothing in it has AI judging an artifact.

**(d) NOT applied — `intro-framing` (0/3).** The arbiter raised it as the way to capture "gives us
stats," then identified `problem-statement-anchor` as what he actually meant. §99c settles it: **the
test is whether the evidence *is* the contribution.** Here it is — a mining study. Same ruling as Xu
(§83); opposite to Zietsman (§99c), where the argument was the contribution.

**(e) NEW DISCRIMINATOR — the WITHIN-UNIT test for `risk-routing`.** Declined at codex 1/3. The
arbiter's formulation, sharpened across two exchanges, supersedes the assistant's first attempt
(*"describing who routes ≠ contributing a routing signal"*), which located the distinction in the wrong
place:

> **Between-unit variation is policy heterogeneity. Within-unit conditional allocation is routing.**
> *Repo A requires review, Repo B does not* → **not routing.**
> *Repo A routes to humans under conditions X and auto-merges under conditions Y* → **routing.**

Better because it catches a case the contributed-vs-observed framing missed: a paper can *contribute* a
between-unit comparison and still not be routing, while a paper *observing* within-unit conditional
allocation can be.

**Second clause, added after a worked edge case.** Applying the rule to this very paper reopened one
finding — *"maintainers auto-merge agentic PRs more often but **show caution toward PRs that delete
existing code**"* — which is within-unit conditional on its face. **Arbiter's mechanism test:** *"How is
the decision made? If there is logic setup in the CI/CD pipeline to make this call, then it might
qualify. If it is a generic statement, not so much."*

**Checked: it is statistical, not configured.** The finding rests on distribution comparisons —
*"Auto-merged PRs are significantly smaller in lines changed, files changed, additions, and
deletions"* — box plots, p-values and effect sizes. **No pipeline logic exists.** The caution is an
inferred behavioural tendency from aggregate merge outcomes.

> **Full test: within-unit conditional allocation qualifies only when it is a RULE OR SIGNAL — encoded
> in a pipeline, policy, or stated condition — never a tendency inferred from aggregate outcomes.**

**Third clause — human discretion is not a computed signal.** Arbiter: *"If a human were making a
case-by-case call, that is **human routing, not risk routing**."* This is already latent in the tag's
own text — *"Signal must be **computed** & producer-independent"* — but had never been stated for the
human case, only for the model-self-confidence case. **A maintainer deciding per-PR on judgement,
however risk-sensitive, is `hitl-workflow`, not `risk-routing`.** The theme is *"the **smarts of
surfacing** (signal + selection/tiering logic)"*; unaided human judgement supplies neither.

**Consolidated — four things that are NOT `risk-routing`:**
1. **Throttling intake** — a queue cap reduces volume without discriminating within it (§86).
2. **Between-unit policy variation** — Repo A gates, Repo B doesn't; heterogeneity, not allocation.
3. **A tendency inferred from aggregate outcomes** — a p-value on a box plot is not a rule (this §).
4. **Human case-by-case discretion** — not a computed signal; `hitl-workflow` instead.

**What remains:** a computed, producer-independent signal *plus* operationalized selection or tiering
logic. Signal without the allocation decision → `routing-signal` + `metrics`. Allocation without a
computed signal → `hitl-workflow`.

**(f) `survey-input` DECLINED by the arbiter — and a definitional risk flagged.** The stated ground was
*"There was no survey. They mined repos."* The facet, however, is **not** about the paper's method:

> *"`method-self-report` ≠ `survey-input` (method vs the finding's **utility to the org survey** — **a
> mined study can be survey-input**)."*

`method-self-report` correctly does not apply here — the arbiter's second point is right on that tag.
**But the two facets are being run together, and the risk is systematic under-application.** Corpus
state at this ruling: `survey-input` is **panel-modal on 17 papers**, arbiter-endorsed on **8**, with
**7 overlapping** — i.e. **10 modal proposals stand on silence** and could be affected by the same
reading. **CLOSEOUT ACTION: re-check `survey-input` across the corpus against the utility-to-our-survey
definition, not the did-they-survey one.** Not written here (1/3, non-modal — it falls out regardless).

## 108. Documenting an ABSENCE — when it earns the theme and when it doesn't (`5BAZZWHG`, 2026-08-27)

Catalan, Dizon, Monderin & Kuang, *"I'm not reading all of that": understanding software engineers'
level of cognitive engagement with agentic coding assistants* (arXiv 2026-03).
**Core + Dissertation Primary.** Primary `automation-bias` (3/3); `oversight-explanation` (2/3);
`agentic`, `risk-overreliance`, `method-experiment`, `method-self-report` (3/3 each).

**(a) THE ABSENCE RULE.** The arbiter took `oversight-explanation` while noting *"it is more saying
that there isn't much explanation in this case."* Two papers earlier, `ai-review` was declined on
`JQPPKSFQ` **because** that paper is about review being absent (§107c). Both rulings are right, and the
reconciliation needs stating:

> **Documenting an absence earns the theme when the paper *argues about what should be there*. It does
> not when the absence is merely the *measured outcome*.**

Catalan finds ACAs *"provide limited affordances for reflection, verification, and meaning-making"*
**and** proposes directions — cognitive-forcing mechanisms, richer interaction modalities. That
contributes to the explanation-design argument. Branco measures merge outcomes and proposes nothing
about review. **Expect this repeatedly: several papers in this band study things not happening.**

**(b) Mode: `agentic` 3/3, `assistive` 0/3 — and the §81 pattern held.** The arbiter's initial
`assistive` reasoning was *"it was modelled after vibe coding, a prompt to generate code"* — the exact
configuration §81 resolved on `T2EG4BE2`: **human-prompted but artifact-scale, so the reviewable unit
dominates.** Tool-category naming pulls the wrong way here (they are called *assistants*), but the
paper studies *"agentic AI systems that operate with **minimal human involvement**."* **Third
consistent application of the tie-rule** (§81, §85, here).

**(c) Design opportunity the paper names but does not build.** *"we identify concrete design
opportunities leveraging richer interaction modalities and **cognitive-forcing mechanisms** to sustain
engagement and promote deeper thinking."* Recorded because the arbiter independently raised the same
question (*"trigger level 1 / level 2 thinking"*) — **cognitive forcing functions are the
System 1 → System 2 interrupt.** The paper names the direction and operationalises nothing, which makes
this an identified-but-unfilled opening rather than a gap the dissertation would have to argue into
existence.

### 108c. §57 RESOLVED — a self-report instrument inside a controlled task is not a second method

The two-event question was raised, then settled by the arbiter: *"There was one [survey], but it wasn't
the core (the experiments with users coding was), just a **data collection mechanism**."*

> **A self-report instrument used to measure *within* a controlled task is the INSTRUMENT, not a second
> evidence event.** One event → one method classification (§34, §57).

**`method-experiment` kept; `method-self-report` REJECTED at 3/3** (modal, so an explicit reject was
required). Same shape as the `8MXATG38` failure the rule was written for.

**Fourth application of one principle**, now spanning the taxonomy: §57 logs-as-instrument · §84
`metrics` offered-for-reuse · §104 apparatus-is-not-contribution · **§108c self-report-as-instrument**.
*What a paper uses to measure is not what a paper contributes or how it measured.*

### 108d. `oversight-scaling-inversion` DECLINED — the mechanism is not the consequence

The arbiter proposed it, reasoning that inversion *"is a consequence of humans tuning out in later
cycles, as described in the paper"*, then agreed on inspection: *"inversion is a stretch in this case."*

**The study has no review step.** Four participants, one code-generation task each, engagement measured
by self-report; **nothing is merged, shipped or gated, so no defect can escape a review that should
have caught it.** §88 unsatisfied; §83's rule applies — *a paper that does not study inspection
coverage cannot supply affirmative evidence of fail-open, however strongly its other findings rhyme
with the mechanism.*

> **A mechanism that could produce leakage is not leakage.** If *"this could lead to leakage"* fired the
> tag it would fire on **every** automation-bias paper — Tilbury, Zhou & Zhao, Parasuraman — which is
> exactly the discriminating-power collapse §87 exists to prevent.

The causal chain is preserved as a **stated hypothesis** in `Emerging_Themes.md`, with only its first
link demonstrated.

### 108e. Evidence-grade correction, self-recorded
The assistant initially presented engagement decay as "the fifth mechanism" alongside Xu's DiD and
Branco's 33k-PR mining study. **That over-weighted an N=4 formative study with self-reported outcomes.**
The `Emerging_Themes.md` entry now carries an explicit evidence-grade caveat: **Parasuraman carries the
theoretical weight; Catalan is the domain probe.** Recorded because the error was in the direction of
enthusiasm for a striking finding, which is the direction worth guarding against.

## 109. MLR of grey media — `lit-review` applies, and its consequences cascade (`R2QMVNXI`, 2026-08-27)

Chang, Shirazi, Cao & Mobasser, *Coding with AI: from a reflection on industrial practices to future
CS and SE education* (arXiv 2025-12). **Ruled Context**, added to **Dissertation Supporting**.

**(a) It is a Multivocal Literature Review, so `lit-review` applies (rescued from opus 1/3).** The
paper follows **Garousi, Felderer & Mäntylä's grey-literature/MLR guidelines**, applying their quality
criteria — including *"Evidence: inclusion of examples, rationale, or empirical support"* — to 57
curated YouTube videos. **Grey literature is still literature under that methodology.** Arbiter's
framing was exact: *"a 'lit review' of youtube videos about vibecoding and agentic coding to see how
the videos are positioning / practicing things."*

> **Rule: a systematic synthesis of grey media is `lit-review`, not a method facet.** The unit of
> analysis is *published discourse*, and the evidence is synthesised rather than produced.

**(b) TWO AUTOMATIC CONSEQUENCES, both applied.**
1. **No method facets.** *"`lit-review` papers get none — evidence synthesized, the methods live in
   the primaries."* **`method-mining` REJECTED at 2/3** (modal, explicit reject required);
   `method-self-report` 1/3 falls out. This also answers the question the paper first raised — it is
   neither mining nor self-report, it is **synthesis**.
2. **Primary must be the biggest-tent theme.** With the inversion rejected (below), the panel's
   unanimous primary vanishes and no replacement was ruled. **Left unresolved and moot** — Context
   papers do not enter Phase 6 synthesis, so the primary has no consumer (§42).

**(c) `oversight-scaling-inversion` REJECTED at 3/3 — fifth rejection, and it fails twice over.**
*"Code review as a bottleneck"* is a named RQ2 theme, but:
- **§88:** a bottleneck is **capacity strain, not leakage**. Nothing reports review being skipped or
  defects shipping. The paper cuts the other way in two places — practitioners scope vibe coding as
  *"**not meant to ship to production**"*, and quality issues are said to *"necessitate **careful human
  review**."*
- **Biggest-tent test:** review-as-bottleneck is one theme among many spanning definitions, security,
  quality, skill erosion and education. Not the largest share.

**(d) Tier — consistent with the lit-review precedent.** `RG4A4D6K` (Watson §82), `XZEHQYNZ`
(Tuape §78) and Tereci were all reviews and all demoted. This one synthesises **what practitioners say
on YouTube** — evidence about **discourse**, not practice, a limitation the authors acknowledge.

### 109a. NAMED-USE CRITERION for Dissertation Supporting

Arbiter: *"Should we dissertation support, or is this not strong enough to be helpful?"* The
substantive findings are **duplicative** — quality and security (Zhao, Fu, Perry, Waseem), skill
erosion (Catalan, Parasuraman, Xu), review bottleneck (Yang, Branco, Xu) are all sourced better
elsewhere. **Supporting is justified by one specific use, not by general relevance:**

> **Vocabulary calibration for the survey instrument.** Survey questions must use terms as respondents
> understand them. Where a controlled study gives the corrected version, **grey media gives the
> vernacular** — and for instrument design the vernacular is what matters.

**Proposed criterion, adopted:**

> **Dissertation Supporting membership carries a NAMED USE, not general relevance.** A bucket that
> admits everything tells you nothing at selection time — the §87 discriminating-power argument applied
> to collections rather than tags. **Back-fill a one-line rationale on existing Supporting members:
> cheap now, expensive at fifty.**

A **Zotero note (`VTRCWI6K`)** records the named use and the extracted definitions on the item itself,
per the source-of-truth principle.

### 109b. Three findings from the practitioner definitions

1. **INSTRUMENT HAZARD.** Practitioners scope vibe coding as **explicitly non-production** — *"that's
   the YOLO vibe coding and **not meant to ship to production**."* A survey question about *vibe coding
   in production* therefore risks denials meaning **"we don't call that vibe coding"** rather than
   **"we don't do that."** **Ask about the practice — prompt-driven generation accepted without reading
   the code — not the label.**
2. **VOCABULARY VALIDATION for a tag we invented.** The paper's term for the vibe-coding posture is
   ***"material disengagement"*** from the code — the practitioners' own name for what we staged as
   `no-inspection` (§81a). **The concept existed in the field's vernacular before it existed in our
   vocabulary**, which is useful support when defending a staged facet the panel could never propose.
3. **The practitioner spectrum matches our mode pair.** Figure 2 presents assistive → agentic as a
   recognised spectrum, and the agentic definition places the human as **orchestrator** — consistent
   with the decision-surface cluster (§96e) and the upstream-control papers.

**Possibly unique and worth watching:** the RQ3 theme *"Code review as the new primary skill"* — not
seen stated elsewhere in the corpus.

## 110. ROLE SPECIALISATION ≠ AGENT PANEL; and validation-by-execution (`6NTZ85CW`, 2026-08-27)

David & Gervais, *Multi-agent penetration testing AI for the web* (MAPTA, arXiv 2025-08).
**Ruled Context** per **§92** — a `general-code` review **tool**, not an oversight finding. Added to
`04 - Validation Apparatus`. Arbiter: *"it is building an agentic system that does penetration testing.
So not really AI generated code."*

**Motivation is our thesis; the artifact is not.** The abstract opens on the scalability crisis —
*"the pace of development now **vastly outstrips the capacity for thorough security assessment**"* — but
MAPTA is a general web-application pen-testing system benchmarked on XBOW's 104 challenges. **AI-generated
code is the justification; general web applications are the object.** `general-code` 2/3.

**No human anywhere:** *"end-to-end, continuous penetration testing **without human**"*; *"shifting
security assessment **from human-dependent** pattern recognition to adaptive adversarial execution."*

**(a) NEW DISCRIMINATOR — role specialisation is not an agent panel.** "Multi-agent" in a title
reliably invites `agent-panel`; here it should not.

> **A panel means several agents judging the SAME artifact — redundancy for decorrelated error.
> Role specialisation is a DIVISION OF LABOUR: different agents doing different jobs in sequence.**

MAPTA's structure is a **Coordinator** (strategy, orchestration) plus **Sandbox** agents (tactical
execution in isolated containers) — a pipeline, not a jury. Contrast `DJMBHHZN` (MOSAICO, §76): solution
agents propose, **separate supervision agents evaluate the same output**, and a consensus agent
adjudicates. **That is a panel.** Test: *would removing one agent lose a job, or lose a vote?*

**(b) `oversight-scaling-inversion` REJECTED at 2/3 — sixth rejection.** The scalability crisis is
**motivation, not contribution**; the paper never studies inspection coverage. Same shape as
`WUUDHL8R`'s `regulatory-compliance` (§44), and §83's rule applies directly.

**(c) `problem-statement-anchor` DECLINED (1/3).** The *"up to 40% of AI-generated code contains
vulnerabilities"* figure is **cited from other studies**, not produced here. Same refusal as Watson's
20–30% (§82g). **Action: chase the primary — a 40% vulnerability rate in AI-generated code would be a
strong anchor if it holds up at source.**

**(d) PRESERVED — validation by execution.** *"**mandatory proof-of-concept validation for all
findings**."* Every reported vulnerability is proven by a working end-to-end exploit rather than flagged
as a suspicion.

> **Validation by execution rather than by judgement.** No human adjudicates whether a finding is real,
> because the system **demonstrates** it. This removes the false-positive triage burden that makes most
> automated security tooling expensive to operate — the cost that Yang's curl case (§86) shows consuming
> scarce security-handling time.

A **design choice, not a measured finding** — the triage saving is never quantified, which is why §92
still sends the paper to Context. But it is the cleanest instance in the corpus of a check needing **no
human adjudication because the ground truth is self-demonstrating**, and it belongs in the apparatus
harvest. **Relates inversely to §51:** that exclusion disqualifies checkers needing a *known-correct
reference*; a working exploit needs none — it is its own proof.

**Cost figures worth noting for the economics of automated checking:** total $21.38 across 104
challenges; median **$0.073** per successful attempt versus **$0.357** per failure; practical
early-stopping thresholds at ~40 tool calls or $0.30. **Machine-side resource allocation, not human
attention** — so not `risk-routing` (§107e), but relevant if the dissertation ever costs out automated
versus human checking.

## 111. A proposed instrument does not rescue a measurement paper (`PDYJGF2R`, 2026-08-27)

Dora, Lunkad, Aslam et al., *The hidden risks of LLM-generated web application code: a security-centric
evaluation of code generation capabilities in large language models* (2026). **Ruled Context** per
**§93** — pure measurement of model-output insecurity across ChatGPT, DeepSeek, Claude, Gemini and Grok.
Added to `04 - Validation Apparatus`. **No Dissertation Supporting.**

**(a) §104 and §93 interact, and §93 wins — worth recording since the two could be read as conflicting.**
The paper explicitly proposes its instrument: *"**Created a checklist** for evaluating the security of
LLM-generated Web Applications: We have created a comprehensive checklist along with risk for
systematic analysis."* So §104 does **not** demote it — the machinery is *argued for*, not merely used
(contrast Adnyana, §104).

> **But a proposed instrument does not convert a measurement paper into a contribution paper.** The
> checklist occupies one bullet; the paper is the **evaluation of five LLMs**, which is exactly what §93
> sends to Context. **Ask what the paper is FOR, not only what it contains.**

**(b) Dissertation Supporting DECLINED on the §109a named-use test.** The checklist is **technical**
(authentication, session management, input validation, HTTP security headers), not organisational.
Surveys cannot enumerate technical checks, and the survey-relevant checklists are already held by
better sources — Waseem's role-specific guideline matrix, Yang's 12 governance strategies, Watson's
transparency recommendations. **No use this serves better than what is already there**, which is the
criterion. **First application of §109a as a refusal**, and it worked as intended: the question was not
*"is this relevant?"* but *"what would it be for?"*

**(c) SECOND INSTANCE — asserting the tenet (§106b).** The abstract closes:
*"Our findings underscore that **human expertise is crucial** to ensure secure software deployment or
review of LLM-generated code."* **Asserted from an evaluation with no human in it, that measured
nothing about human review.** Twice now in eight Accept-band papers (cf. `P837LJWE`, §106b). **Watch
item:** if this recurs across the band it is a reportable observation — *the literature routinely
concludes that human oversight is essential from studies that never observed any*, which would be a
finding about the field's evidentiary habits rather than about oversight.

**Harvest value:** a checklist built **because its authors judged existing assessment inadequate for
LLM-generated code** is precisely *"what did they consider adequate validation"* — the harvest's
premise. Recorded there rather than in Supporting.

## 112. PARALLEL SPECIALISTS are not a panel either; and deferring Supporting against a known cluster (`399HN438`, 2026-08-27)

Dutta, Sharma, Rajgor et al., *Turbocharging pull request reviews: exploring generative AI for code
review* (2025). **Ruled Context** per **§92** — `general-code` 3/3, and CodeEvaluator is a review
**tool** reporting *"early results"*, not a transferable oversight finding. Added to
`04 - Validation Apparatus`. **Dissertation Supporting DEFERRED, not declined.**

**(a) §110 REFINED — the test is the QUESTION, not the topology.** CodeEvaluator is a multi-agent
framework with five agents: Code Review, Bug Report, Code Smell, Code Optimization (RL-based), and
Security Vulnerability Detection. All five run against the **same diff**, which makes it look more
panel-like than MAPTA's sequential Coordinator/Sandbox arrangement. **It is not a panel either.**

> **Agents form a panel when they answer the SAME question independently** — redundancy bought for
> decorrelated error. **They are specialists when they answer DIFFERENT questions**, however parallel
> the execution. §110's test stands and sharpens: *removing an agent loses a **job** or loses a
> **vote**?* Removing the Security agent here loses **security coverage**, not a vote.

**Two flavours of specialisation now on record**, neither a panel: **by pipeline stage** (`6NTZ85CW`
MAPTA — orchestrate, then execute) and **by defect class** (`399HN438` — five parallel hunters, one
artifact). **Neither cross-checks.** Contrast `DJMBHHZN` (MOSAICO, §76), where supervision agents
evaluate the *same* proposals and a consensus agent adjudicates.

**(b) SUPPORTING DEFERRED — applying §109a prospectively.** The plausible named use is structuring a
survey question about *what AI review tools actually check for*, and the defect-class decomposition
serves that. **But four stronger candidates for the same use remain unread in this band:** `V4IRKSFI`
(Sun, *BitsAI-CR* — automated code review **in practice**, i.e. production), `5RKMGRNA` (Nimraka),
`DJHG9BBS` (Rasheed), and `A5WDGC7J` (Jin — LLM reviewer **reliability**). Dutta is 3,231 words of
early results.

> **§109a extended: a named use is not enough if a better source for that same use is known to be
> coming.** Admitting the weakest member of a cluster first means admitting the rest for parity — the
> failure mode the criterion exists to prevent. **Defer, do not decline**; the paper is in the harvest
> regardless, so nothing is lost if the stronger candidates disappoint.

**Revisit condition:** if none of the four delivers a usable decomposition of AI-review coverage,
Dutta returns to Supporting.

**Not resolved (§42 short-circuit):** `method-self-report` 3/3 is questionable on a 3,231-word paper
reporting early results — no instrument is described. Left unadjudicated; noted in case the closeout
facet sweep reaches Context papers.

## 113. The instrument's own design rule gets empirical backing — the Confidence Trap (`UIXCRBQX`, 2026-08-27)

Ferdous, Banik, Chowdhury & Shamim, *Safer builders, risky maintainers: a comparative study of breaking
changes in human vs agentic PRs* (arXiv 2026-03). **Core + Dissertation Primary + Validation
Apparatus.** Primary `quality-debt` (3/3); `agentic`, `method-mining`, `risk-quality` (3/3);
`built-system` (2/3); **`routing-signal` rescued** (codex 1/3).

**The headline is not the valuable part.** The comparison — agents introduce **fewer** breaking changes
than humans overall (**3.45% vs 7.40%**) but **more** during maintenance (refactoring **6.72%**, chore
**9.35%**) — is a quality result. Two *oversight* findings sit underneath it, and both matter more.

**(a) THE CONFIDENCE TRAP — evidence for a rule the instrument had only asserted.** `risk-routing`'s
definition states *"Signal must be **computed & producer-independent** — **model self-confidence is
disqualified**"* as a **design judgement**, recorded before any evidence (independence thread, leg 1).
This paper tests it:

> *"99.9% of AI-generated pull requests [score] between **8 and 10**"* · breaking-change rates at
> confidence **8 / 9 / 10 = 3.94% / 3.96% / 3.16%** · *"**confidence scores do not reliably reflect
> breaking change risk**"* · *"confidence scores alone are **insufficient for prioritizing review or
> deployment**, and should be supplemented with additional verification mechanisms."*

**The signal has almost no variance — 99.9% of cases in a three-point band — so it cannot discriminate
even in principle**, independent of whether it is calibrated. That is a stronger failure than
miscalibration.

**Third measurement leg for the independence thread**, from a third method:
`VTDG995V` (Gros/Spiess — intrinsic confidence poorly calibrated, ECE 0.09–0.73) · `PPMTM4DG` (Yu —
self-verification misses 67% of own errors) · **`UIXCRBQX` (self-reported confidence does not
discriminate breaking-change risk)**. Three independent groups, three designs, one conclusion.

**Worth noting for the methods chapter:** a design decision recorded in the instrument **before** the
evidence existed has now been independently corroborated. That is the strongest form the
reflexivity argument can take — cf. §11.8, where the review's convergence with its own findings was
flagged as illustration only.

**(b) `routing-signal` RESCUED — passes all three §107e clauses.**
*"we recommend practitioners apply **enhanced, task-specific review policies**"*, grounded in the
maintenance-versus-generation rate difference.
- **Within-unit conditional** ✓ — same repo, different treatment by task type, not a policy difference
  between repos.
- **A computed signal, not a tendency** ✓ — task type is derivable from the PR, not inferred from
  aggregate merge behaviour (contrast `JQPPKSFQ`, §107e).
- **Producer-independent** ✓ — task classification does not come from the agent.

**`routing-signal`, not `risk-routing`** — they recommend policies without operationalising selection or
gating logic, which is exactly the facet's scope, and the two are mutually exclusive by definition.

**(c) `rules-based-checks` DECLINED (codex 1/3).** The AST-based breaking-change detector is their
**measurement instrument**, which §104 places on the instrument side. *Building a detector to measure
something is not contributing a detection mechanism.*

**Dissertation Primary rather than Supporting.** The arbiter's stated use — agents break less than
humans — is real but comparative. **The confidence-trap finding is the one that changes an argument:**
it is the corpus's only empirical demonstration that the signal an organisation would reach for first
is unusable.

## 114. Second clean §88 positive, and a NORM inversion distinct from the capacity one (`59KP8GTP`, 2026-08-27)

Gao, Banyongrakkul, Guan, Zahedi & Treude, *On Autopilot? An Empirical Study of Human-AI Teaming and
Review Practices in Open Source* (arXiv 2026-01). **Core + Dissertation Primary.** Primary
`oversight-scaling-inversion` (3/3); `org-governance` (3/3); `problem-statement-anchor` (3/3),
`agentic`, `method-mining` (3/3). Method verified as pure mining — the only occurrence of *"survey"* in
the paper is inside a **reference title**; no questionnaire, interviews or participants.

**(a) §88 satisfied — second clean positive after `JQPPKSFQ`.** *"approximately **80% merged without any
explicit review**."* This states review *absence* directly, where Branco's evidence was auto-merge
configuration. **The theme now has two anchors and six rejections**, which is the shape §87 predicted
for a narrow tag.

**(b) THE FINDING WORTH LEADING WITH — a norm inversion, not a capacity failure.**

> *"In contrast to human-created PRs where **non-owner developers receive the most feedback**,
> AI-co-authored PRs from non-owners receive the **least**."*

**The OSS norm — scrutinise contributions from people who do not know the codebase — reverses when AI
is involved.** Newcomers *with* AI receive less scrutiny than newcomers *without*, measured against a
human baseline **in the same dataset**. With **67.5% of AI-co-authored PRs originating from
contributors with no prior code ownership**, the population receiving least scrutiny is precisely the
one that historically received most.

**This is a distinct mechanism from the capacity inversion.** Branco's repositories skip review because
volume exceeds capacity; here reviewers are *present and responding*, but allocate attention **away**
from the higher-risk population. **Not overload — misallocation**, and it runs against an established
social norm rather than against a resource limit. Recorded in `Emerging_Themes.md`.

**(c) `problem-statement-anchor` 3/3 — and possibly the better of the two.** Both this and `JQPPKSFQ`
are first-hand and corpus-scale, but *"80% merged without any explicit review"* states the inversion
more directly than auto-merge rates. **Closeout action: choose ONE to anchor the frame** — the facet is
for *the* stat that anchors the overall problem statement, and two papers doing that job dilutes it.

**(d) The governance number answers the dissertation's question directly.** *"the majority of
repositories lack guidelines for AI-coding agent usage"* — **86.9% have none.** With Yang's 12
governance strategies (§86), this gives both the **prevalence** and the **content** of AI governance in
OSS. Basis for Dissertation Primary rather than the Supporting placement first proposed.

**(e) Declined:** `provenance-auditability` (codex 1/3 — disclosure rules leaving traces is incidental),
`steering` (1/3).

**(f) `survey-input` (3/3) HELD, not written — pending a definitional ruling.** See §107f: the facet is
*"the finding's **utility to the org survey**"*, and *"a mined study can be `survey-input`"*. The
arbiter has now twice declined it on the ground that the paper did not survey anyone — which is the
`method-self-report` test, not this one. **Corpus exposure: panel-modal on 17 papers, arbiter-endorsed
on 8, so ten modal proposals stand on silence.** A ruling here settles it corpus-wide rather than
paper by paper.

**Open housekeeping:** `JQPPKSFQ` (Branco) was never placed in a dissertation collection despite its
bimodality finding being Primary-grade. Revisit alongside the anchor decision.

## 115. §104 REFINED — an instrument becomes a contribution when the paper measures the effect of USING it (`3Z45M3V3`, 2026-08-27)

Fu, Liang, Tahir, Li, Shahin & Yu, *Security weaknesses of Copilot generated code in GitHub* (arXiv
2023). **Core + Dissertation Supporting + Validation Apparatus.** Primary `ai-code-insecurity` (3/3);
`rules-based-checks` (2/3); `assistive`, `risk-security`, `method-mining` (3/3), `method-experiment`
(2/3), `problem-statement-anchor`.

**(a) THE REFINEMENT, prompted by the arbiter:** *"also an angle on tools that could be used as a
security detector in pipeline?"* The assistant had declined `rules-based-checks` under §104 — the
static analysers looked like measurement apparatus. **That was wrong.**

> **§104 refined: an instrument becomes a contribution when the paper measures the effect of USING it,
> rather than merely using it to measure something else.**

Fu's static analysers (**CodeQL**, plus ESLint for JavaScript and Bandit for Python) are a **component
of a loop whose effect is measured**: detector → warning message → LLM repair → re-scan. The headline
number *is* that measurement. Contrast `VG8PSMM7` (Adnyana, §104), where the LITL+HITL ladder scored
**prompting techniques** — there the pipeline was apparatus for a different question.

**(b) Fourth measurement leg for the independence thread — and the only one that PRICES the external
signal.**

> *"Using the fix command can fix **19.3%** of security issues, while using the enhanced prompt raises
> [it to] **up to 55.5%**"* · *"Providing Copilot Chat with a **warning message from the static analysis
> tool** resulted in a better fix."*

**The model repairs 19.3% of its own security defects unaided, 55.5% when handed an external
producer-independent signal.** Same shape as `VTDG995V` (rescaling against external ground truth moved
ECE 0.46 → 0.04) — *the rescue comes from outside the model* — but this one quantifies **what the
outside signal buys**. The thread now runs: rule (instrument design) → prescription (Zhu, Mahmud,
Sistla) → measurement (Gros/Spiess, Yu, Ferdous, **Fu**) → observed deviation (Pimenova).

**The architecture is also the one the thread endorses:** an external deterministic detector driving
repair by a model that cannot find its own defects. **Passes §51** — static analysis needs no
known-correct reference.

**(c) FIELD measurement, not benchmark — a distinction §93 does not currently make.** 733 snippets from
**real GitHub projects**, explicitly filling the gap that prior work *"examin[ed] code produced in
controlled environments rather than open source development scenarios."* 29.5% of Python and 24.2% of
JavaScript affected; 43 CWEs; 8 in the 2023 CWE Top-25.

> **Watch item for §93:** the rule sends *pure measurement of model output insecurity* to Context, but
> was written against **benchmark** papers (Zhao, Dora). **Field measurement on real repositories is
> stronger evidence** and may warrant separate treatment. Not changed now — Fu qualifies for Core on
> (b) regardless — but flagged, since `ai-code-insecurity` has ~8 unread instances left in this band.

**(d) `problem-statement-anchor` — ONE ANCHOR PER CLAIM, not one anchor total.** This resolves the
dilution concern raised at §114c. The review's frame has two halves, so each takes its own anchor:

| Claim | Anchor candidate |
|---|---|
| **AI code is risky** | `3Z45M3V3` Fu — 29.5% / 24.2% in **real projects** |
| **Oversight fails** | `59KP8GTP` Gao (80% unreviewed) *or* `JQPPKSFQ` Branco — still to choose |

Fu also carries a **legacy bare `problem-statement-anchor` tag** from an earlier pass; now written
properly in the `cal:human` namespace.

**(e) Dissertation Supporting, named use (§109a):** the **19.3% → 55.5%** figure converts directly into
a survey question — *do you feed static-analysis output back to the assistant?* — and supplies the
reason the question matters. Not Primary: it is a mechanism finding, not a picture of practice.

**Declined:** `steering` (1/3).

## 116. `survey-input` NARROWED to papers containing a user survey; and theatre vs inversion on the same data (`SHK6KAX6`, 2026-08-27)

Ghammam & Almukhtar, *AI builds, we analyze: an empirical study of AI-generated build code quality*
(arXiv 2026-01). **Core.** Primary `quality-debt` (3/3); `ai-code-insecurity` (3/3);
**`oversight-theater` rescued** (codex 1/3); `agentic`, `risk-quality`, `risk-security`, `method-mining`
(3/3). Rejected `oversight-scaling-inversion` (2/3) and `survey-input` (2/3).

### 116a. DEFINITIONAL NARROWING — `survey-input`

> **SUPERSEDED IN PART by §121b (2026-08-28).** The narrowing below stands (an actual user-survey
> instrument must exist), but the operative test is now **what the instrument ELICITS**: stated
> preferences / adoption / priorities → `survey-input`; a construct or performance measure
> (cognitive load, engagement, comprehension, satisfaction) → `method-self-report` only.
> Neither the survey's centrality to the paper nor its usefulness to us is part of the test.

The facet has been declined three times (`JQPPKSFQ`, `59KP8GTP`, here) on the ground that the paper did
not survey anyone, which contradicts its written text: *"`method-self-report` ≠ `survey-input` (method
vs the finding's **utility to the org survey** — **a mined study can be `survey-input`**)."* The arbiter
resolved the divergence: ***"The intention for input-survey was a user survey — Likert scale, etc."***

**Checked against the corpus before adopting**, since the narrow reading risks making the facet
redundant with `method-self-report`:

| | n (of 128) |
|---|---|
| `survey-input` **and** `method-self-report` | **12** |
| `survey-input` only | **5** — Chang, Gao, Ghammam, Li, Yang |
| `method-self-report` only | 15 |

**Not redundant — and the overlap figure above OVERSTATES the qualifying set.** Corrected after the
arbiter pushed back on the framing: *"self report is NOT a survey."* The definition is
**`method-self-report` — *(humans tell you: questionnaires, interviews, focus groups, diaries)***.

> **Self-report is the genus; a survey is one species.** Interviews, focus groups and diaries are
> self-report and are **not** surveys. So `survey-input` under the narrow reading is a subset of the
> *questionnaire-using* subset of self-report papers — **smaller and more discriminating** than the
> 12-paper overlap suggests. The broad reading would fire on almost any organisational-practice paper,
> which is the §87 discriminating-power problem.

> **NARROWED (binding): `survey-input` requires the paper to have collected practitioner input directly
> — survey, Likert instrument, structured questionnaire — AND for that instrument or its findings to be
> useful to the dissertation's org survey. A mined study does NOT qualify, whatever its findings say
> about practice.**

**The five affected papers lose nothing substantive** — all carry `org-governance` or `method-mining`,
and Gao and Yang are already Dissertation Primary. **Cheatsheet text is now wrong and must be corrected
at the next versioned cut (§41 — not edited now).**

**CLOSEOUT ACTION — narrowed after the arbiter confirmed he has been applying this lens throughout:**
*"I've been reviewing the papers and enforcing that lens. I will continue to."*

**The arbiter's `cal:human:facet:survey-input` endorsements are therefore authoritative and need no
re-check.** The exposure is confined to papers where the facet is **panel-modal and the arbiter was
silent** — where the models applied the broad written reading and nothing overrode it. At the time of
this ruling: **17 panel-modal, 8 arbiter-endorsed, 7 overlapping ⇒ ~10 modal proposals standing on
silence.**

> **Closeout: for each modal-on-silence instance, confirm the paper administered a questionnaire or
> survey. Remove where it did not.** Endorsed instances stand as-is.

### 116b. THEATRE, not inversion — the ritual is present but hollow

Two findings, deliberately kept apart:
- **RQ1:** 364 maintainability and security build smells in agent-authored build code.
- **RQ3:** *"**61.4% (238/387)** of the analyzed PRs were merged by developers, and in most cases, the
  merge occurred **immediately**"*; *"Reviewers often accept the PR changes with [little to no
  modification]."*

**`oversight-theater` applies** — §69 requires a process to be hollow, and here **reviewers do accept**;
the ritual exists and carries minimal engagement. **A clean contrast with `59KP8GTP` (Gao, §114):**

| | What happens | Theme |
|---|---|---|
| **Gao** | merged **without any explicit review** — no ritual | inversion |
| **Ghammam** | **reviewers accept**, then merge immediately without modification — ritual present | **theatre** |

**`oversight-scaling-inversion` REJECTED (2/3) — seventh rejection.** The paper never links RQ1 to RQ3:
it does not show the *smelly* PRs were the merged ones. Arithmetic makes it likely, but §88 requires
the escape to be demonstrated, not inferred — the same gap that kept the tag off Chang and Catalan.
**Assistant's call, twice offered to the arbiter and passed over; reversible in one edit.**

**`automation-bias` NOT applied** (0/3, and the arbiter raised it as a possibility). §16's discriminator
requires **a capable human demonstrably failing**. Fast merges with little modification are equally
consistent with rubber-stamping *or* with the code being acceptable. **Merge speed is not evidence of a
missed catch.**

### 116c. CITATION DISCIPLINE — three papers, one dataset

`JQPPKSFQ` (Branco), `59KP8GTP` (Gao) and `SHK6KAX6` (Ghammam) all mine **AIDev**, and report different
review-absence figures on overlapping data: auto-merge rates (bimodal by repo) · **~80%** of non-owner
AI PRs merged without explicit review · **61.4%** of build-code agentic PRs merged, mostly immediately.

> **Different subsets, different definitions. Cite one number for one population.** Three papers
> agreeing loosely would read as replication when it is one dataset sliced three ways — and a committee
> that notices the shared provenance will discount all three.

## 117. Read the implications section before ruling "no oversight content" (`REZGA5WF`, 2026-08-27)

He, Miller, Agarwal, Kästner & Vasilescu, *Speed at the cost of quality: how Cursor AI increases
short-term velocity and long-term complexity in open-source projects* (2026). **Core + Dissertation
Primary.** Primary `quality-debt` (3/3); `agentic`, `method-mining`, `risk-quality` (3/3). Rejected
`oversight-scaling-inversion`.

**(a) ASSISTANT ERROR, corrected by the arbiter.** The assistant assessed this as having **no oversight
content** — on the strength of the abstract and the panel's silence (no model proposed an oversight
theme) — and proposed Context. The arbiter pushed back: *"Also points to the need for an ecosystem to
maintain quality / debt."* **Section 5.2 Practical Implications is substantive:**

> *"process adaptation that **scales quality assurance with AI-era velocity**"* · *"refactoring sprints
> **triggered by code quality metrics**"* · *"test coverage requirements that **scale with lines of code
> added**"* · *"teams should treat AI-generated code as **requiring extra scrutiny during review**."*

> **Rule: panel silence plus a quiet abstract is not evidence of absence.** Empirical papers routinely
> carry their oversight content in **implications and discussion**, which the taggers weight lightly
> and the abstract omits. **Before ruling that a paper says nothing about oversight, read the
> implications section.** Third time an Accept-band paper's value sat below the abstract (cf.
> `UIXCRBQX` §113, `3Z45M3V3` §115).

**(b) THE COMPREHENSION TAX — reviewability degrading independent of correctness, measured.**
> *"a **'comprehension tax' that persists regardless of functional correctness**… LLMs may be generating
> **structurally valid but semantically opaque** code"* — complexity **+41%**, warnings **+30%**,
> persistent. *"**Unless** future workflows allow fully automated AI development **without any human code
> reviews**, code readability will remain an important dimension."*

This is `2KPHQ5IV`'s **dimension collapse** (§80) with a causal design behind it, and it makes
readability a **precondition for oversight** rather than a style preference. Carried by `risk-quality`,
whose definition already covers *"code comprehensibility — explainability of the code."*

**(c) The temporal finding, which is what makes it Dissertation Primary.** DiD with matched controls on
six months of pre-adoption history, plus panel GMM: **3–5× velocity increase in month one, gains
dissipate after two months**, while warnings and complexity persist and *"subsequently dampen future
development velocity"* — a **self-reinforcing cycle**.

**(d) `oversight-scaling-inversion` APPLIED — reversing the assistant's rejection, and §88 gains a
second satisfaction route.** The assistant first rejected it, reading the mechanism as **debt drag**
rather than review failure. The arbiter overruled. **The reversal is right:**

> §88 was being read as requiring **observed review absence** (Branco's auto-merge, Gao's 80%
> unreviewed). But this study measures **repository state** by difference-in-differences — warnings
> **+30%** and complexity **+41%** *persist post-adoption*, which means those defects are **in merged
> code**. And the paper names the cause: *"developers heavily vibe-coding and **not rigorously
> reviewing AI-generated code**."*

> **§88 REFINED — two routes to leakage:**
> **(i) observed absence** — review demonstrably skipped (`JQPPKSFQ`, `59KP8GTP`);
> **(ii) demonstrated outcome** — defects measurably present in **merged** code, with review failure as
> the stated or evident cause. **Defects in shipped code are an escape, whether or not the gate was
> watched.**

**Consistency flag — `SHK6KAX6` (Ghammam, §116b) sits closer to the line now.** It was rejected as the
seventh because it never links its 364 build smells to its 61.4% merge rate. **The distinction that
holds:** He measures the **repository** (merged by construction), whereas Ghammam measures **PRs** and
merge rates as separate quantities. That distinction is real but fine, and **Ghammam should be
revisited at closeout** alongside the other inversion re-checks (§87). Route (ii) must not be allowed
to swallow every quality-measurement paper — **the defects must be in code that shipped, not in
candidates that were assessed** (which is what keeps `4PSM6ZCD` Zhao, a benchmark, correctly out).

**(e) Mode calibration — third instance.** `agentic` 3/3, `assistive` 0/3, against an arbiter reading of
*"assistive scenarios."* The paper argues the distinction itself: *"LLM agent assistants like Cursor,
**by contrast**, are tightly integrated into the IDE with persistent codebase awareness, **autonomously
navigating files, proposing multi-file refactorings**."*

> **Calibration, now three instances deep** (`T2EG4BE2` §81, `5BAZZWHG` §108b, here): **IDE integration
> does not make a tool assistive — the reviewable unit does.** Cursor proposes multi-file refactorings;
> that is artifact granularity.

### 117f. `oversight-explanation` DECLINED on `REZGA5WF`
Arbiter: *"explanation no."* The assistant had floated it as a cold rescue (0/3) on §108's absence
rule, since the paper documents comprehensibility degrading **and** argues for what should exist
(readability-aware fine-tuning, post-hoc simplification passes). **Declined.** The comprehension tax is
carried by `risk-quality`, whose definition already covers *"code comprehensibility — explainability of
the code"*, and the paper proposes **no explanation mechanism** — it recommends the code be *simpler*,
not that it be *explained*. **Discriminator: making an artifact easier to understand is a quality
intervention; making its behaviour legible to a reviewer is `oversight-explanation`.**

## 118. `automation-bias` gets its cleanest instance; and aggregated warning counts are not risk-flag evidence (`4T5QFWZE`, 2026-08-27)

Huang, Jaisri, Shimizu, Chen, Nakashima & Rodríguez-Pérez, *More code, less reuse: investigating code
quality and reviewer sentiment towards AI-generated pull requests* (arXiv 2026-01). **Core +
Dissertation Primary + Validation Apparatus.** Primary `quality-debt` (3/3); **`automation-bias`
rescued** (gemini 1/3); `metrics`, `agentic`, `method-mining`, `risk-quality` (3/3), `risk-overreliance`
(1/3).

**(a) `automation-bias` RESCUED — the cleanest instance in the band.** §16 requires **a capable human
demonstrably failing**, which has kept the tag off papers where fast merges were ambiguous evidence
(`SHK6KAX6` §116b). Here the failure is demonstrated on **both sides simultaneously**:

> *"LLM Agents frequently disregard code reuse opportunities, resulting in **higher levels of
> redundancy** compared to human developers. **In contrast to the quality issues**, our emotions
> analysis reveals that **reviewers tend to express more neutral or positive emotions towards
> AI-generated contributions than human ones.** This disconnect suggests that the **surface-level
> plausibility of AI code masks redundancy**, leading to the **silent accumulation of technical
> debt**."*

**MRS establishes the defect exists; sentiment analysis establishes reviewers did not register it — and
felt better about it.** Reviewers looked at objectively worse code and reacted more positively. **That
is oversight failing, measured on both the artifact and the human**, not inferred from merge latency.

**(b) `metrics` — strongest instance since `F2C2DWSI`, and a clean §84 pass.** *"we propose a new metric
called the **Max Redundancy Score (MRS)**"*, computed via Type-4 semantic-clone detection, positioned
explicitly against the status quo — *"existing metrics solely measure pass rates, failing to reflect
impacts on long-term maintainability and readability."* **Named · computable · argued for · situated in
the measurement literature.** All four of §84's conditions, unusually explicit.

**(c) `risk-security` NOT applied (0/3) — verified absent.** The only occurrence of *"security"* in the
paper is a **venue name in a reference**.

### 118a. AGGREGATED WARNING COUNTS ARE NOT RISK-FLAG EVIDENCE — `risk-security` rejected on `REZGA5WF`

Closing He's last open item, and stating a rule the mining studies will keep testing. He's
`risk-security` was **2/3 modal**, resting on the static-analysis warning increase. The variable
definition settles it:

> *"**Static Analysis Warnings**ᵢₜ : Total number of **reliability, maintainability, and security
> issues** for repository i at month t"*

**The +30% is a composite of three categories, never decomposed** — the security share is
unrecoverable. Every other security mention in the paper is a **citation to other work** as background.

> **RULE: an aggregated warning count is not substantive treatment of any of its components.** The
> risk-flag bar requires *defining a metric for the harm · contributing or evaluating a mitigation ·
> reporting an empirical result **about it** · focal analysis*. A composite that happens to include a
> harm satisfies none. This is the *"intro risk-list sentence = mention, NO tag"* rule one level up —
> **from a sentence that mentions to a number that subsumes.**

**Expect recurrence:** several papers in this band use SonarQube-style composite counts. **The risk
flags must not all fire off one undifferentiated number.**

### 118b. Second EFFECT–MECHANISM pairing in the band
`59KP8GTP` (Gao, §114) measured that AI-co-authored PRs receive **the least** reviewer feedback and
recorded **three untested hypotheses** for why — one being *"polish substitutes for provenance."*
**Huang measures that hypothesis directly** and finds it holds: surface plausibility produces **positive
reviewer affect** toward objectively worse code.

> **Gao has the effect; Huang has the cause. Neither cites the other.** Second such pairing after
> He/Gao's prescription-versus-violation (§117) — and the same argument shape the independence thread
> relies on: **independent groups, converging, neither writing to support the other.**

**Flagged, not applied:** `oversight-scaling-inversion`. Under §88's route (ii) (§117d), redundancy in
**merged** code that review failed to catch would qualify — but the paper says *"silent accumulation…
in real-world development environments"* without establishing that the studied PRs merged. **Route (ii)
should not be widened on its first outing; check RQ1's sample at closeout.**

## 119. §34 MISREAD — the ladder and method facets are not a fork; and shift-left to the model maker (`YA7XNWYE`, 2026-08-28)

Ji, Jun, Wu & Gelles, *Cybersecurity risks of AI-generated code*, **Center for Security and Emerging
Technology (CSET), Georgetown** — a policy report, 2024-11. **Core + Dissertation Primary + Validation
Apparatus.** Primary `ai-code-insecurity` (3/3); `org-governance`, `regulatory-compliance` (2/3),
**`tooling-supply-chain`** (rescued 1/3); `assistive`, `risk-security`, `method-experiment` (3/3),
**`evaluated-benchmark`**, `risk-quality`, `risk-overreliance` (2/3).

**Attribution correction:** initially described as a NIST report. It is **CSET** — a policy think tank,
not a standards body. NIST appears *within* the report as a cited framework. **The distinction matters
for how much authority the recommendations carry in the write-up.**

### 119a. ASSISTANT ERROR — §34 does not bar ladder/method co-occurrence

The assistant has cited §34 three times this session as a **fork** preventing the `evaluated-*` ladder
and `method-*` facets from co-occurring — on `72W6R4JG` (§77), `XK3P9C96` (§97) and `TA6GIUK2` (§99b).
**That is not what §34 says.** Its corollary is *"one evaluation event gets ONE **method**
classification; two **method facets** require two genuinely separate measurement events"* — a rule about
method facets **among themselves**.

**Corpus practice, in the arbiter's own prior rulings, settles it:**

| Paper | Rung | Also carries |
|---|---|---|
| Kang | `evaluated-benchmark` | `method-experiment` |
| Li, Mitropoulos | `evaluated-benchmark` | `built-system`, `method-experiment` |
| Mozannar | `evaluated-benchmark` | `built-system`, `method-experiment`, `method-self-report` |
| Ma / ZORO | `evaluated-synthetic` | three method facets |

**8 of 16 ladder-tagged papers also carry method facets.**

> **CORRECTED: what governs ladder-versus-method is the WORLD-OR-TOOL test, not a fork.** Results
> describing only the tool → ladder rung, no method facet. Results describing the world (or third-party
> systems) → method facet. **A paper doing both earns both.**

**CLOSEOUT ACTION: re-check §77, §97 and §99b.** The rulings may stand on the world-or-tool test, but
**the stated reason is wrong in the record** and is cited three times.

### 119b. `evaluated-benchmark` — measuring AGAINST an accepted benchmark, not contributing one

The arbiter corrected the assistant's reading: *"evaluated benchmark is not that they created a
benchmark, it is that they **measured themselves against a standard / well accepted benchmark**."*

**`A5WDGC7J` (Jin) is the matching precedent** — `evaluated-benchmark` with **no** `built-system` and
**no** method facet, evaluating third-party LLMs on benchmarks. Same shape as Ji.

**Applied here:** the **LLMSecEval** dataset — 67 published, CWE-mapped security prompts — held constant
across **five third-party models** (GPT-4, GPT-3.5-turbo, Code Llama 7B Instruct, WizardCoder 7B,
Mistral 7B Instruct) with **CodeQL** as the assessor. The authors are explicit that they did **not**
build a benchmark: *"our objective was not to… create a new benchmark for code security."*

> **The ladder rates EVIDENCE STRENGTH, not artifact maturity.** A contributed system is not required —
> what matters is whether the evidence rests on ad-hoc tests, constructed data, or an accepted
> benchmark.

### 119c. Mode — `assistive` only (`agentic` 0/3, declined)

The arbiter proposed both, reasoning that *"their methodology was generating code from a prompt which
can happen in both scenarios."* **Declined on scope:** the mode pair marks **which setting the paper
studies**, not which settings the technique could appear in. The report is assistive throughout —
Copilot as *"autocomplete for code"*, *"AI pair programming"*, infilling models, *"AI code assistant"* —
with **no agentic content**, unsurprising for **November 2024**.

**GAP RECORDED at the arbiter's request:** the dissertation will need to argue that **the same
underlying technology powers both assistive and agentic scenarios**. **No corpus paper currently
supports this**, and our own mode-pair rulings treat the two as distinct settings. **Find a source, or
argue it explicitly as the review's own position.** Logged in `Emerging_Themes.md`.

### 119d. The accountability argument, and SHIFT-LEFT to the model maker

> *"**Regardless of its authorship**, code should be evaluated as part of **existing secure software
> development practices**"* — and — *"the burden… **falls mainly on the users**. However, the willingness
> to proactively expend costs to check code outputs for security—**at the expense of efficiency—will not
> be constant across users**. The current state **does not align** with the White House's 2023 National
> Cybersecurity Strategy to **shift the burden of responsibility away from individuals** to
> organizations best positioned to reduce systemic risk at scale."*

**Two positions that cohere into one:** *the practices are adequate; the accountability placement is
not.* And the stated reason is this review's thesis in policy language — **oversight that depends on
individual discretion, against the individual's own efficiency incentives, does not hold uniformly.**

**Arbiter's framing, recorded because it extends our gate-placement spectrum:** *"This is **shift left** —
if the model makers do a better job, there will be less left for individuals to pick up… Same as
detecting and fixing problems earlier in SDLC."* See `Emerging_Themes.md`.

**Also worth carrying:** *"Evaluation benchmarks… **overlook security, incentivizing future
code-generation models to prioritize performance over security**"* — the measurement regime shapes what
gets built, which pairs with §66/§84 on what counts as a metric.

## 120. The reuse test lives in `framework`, not `built-system` — boundary probed, NO change (`A5WDGC7J`, 2026-08-28)

**Paper:** Jin, Wang, Guo et al., *Are LLMs reliable code reviewers? Systematic overcorrection in
requirement conformance judgement*, **Automated Software Engineering** (2026-06).
**Written:** primary `ai-review`; `rules-based-checks`, `general-code`, `built-system`,
`method-experiment`, `evaluated-benchmark` (pre-existing); **`framework` rejected** (panel 2/3).
**SLR: Core · Dissertation: Primary · 04 - Validation Apparatus.**

### 120a. What the paper is, and why an LLM-evaluation paper survives the demote rule

We have demoted a long run of "how well do LLMs do X" evaluations. This one is kept, on the same
ground as Yu (`PPMTM4DG`): **the LLM under evaluation is occupying the oversight seat.** The object of
study is the *reviewer*, not the generator, so the failure it characterises is a failure of the
review mechanism itself.

The specific finding: LLM judges given a **spec and an implementation** do not fail by rubber-stamping
— they fail by **systematic overcorrection**, rejecting conformant code and inventing faults, with
false-positive rates as high as **88.74%** (GPT-4o on MBPP). Together with two papers already in the
corpus this completes an **LLM-reviewer failure triad**:

| Paper | Failure mode |
|---|---|
| Yu (`PPMTM4DG`) | **false negatives** — a model cannot catch its own defects |
| Zietsman (`TA6GIUK2`) | **circularity** — review without an external referent |
| **Jin (`A5WDGC7J`)** | **false positives** — overcorrection *even when given* a spec |

The triad matters because it closes an escape route: the fix for Yu is "give the reviewer an
independent referent," and Jin shows that supplying one produces a *different* failure rather than
no failure. **Handing the reviewer a spec is not sufficient.**

**Arbiter's substantive contribution, recorded because the corpus lacks the distinction:** this paper
applies review **against the V-model** — checking the implementation against the *specification*
rather than scanning for bugs or poor structure. That separates two things we have been calling one:

- **conformance review** — *did it build what was asked?* Requires a referent; fails by overcorrection.
- **defect review** — *is this code bad?* Needs no referent; fails by omission.

Logged to `Emerging_Themes.md`. Most corpus oversight mechanisms are defect review; the oversight
question that actually worries practitioners is conformance.

### 120b. `framework` REJECTED — the reuse test, applied

Panel proposed `framework` 2/3. **Rejected on two independent grounds.**

**Span (§49).** The contributed mechanism is a **Fix-guided Verification Filter**, and the paper states
its trigger condition plainly: *"the filter is **applied only when the judge returns NO**."* That is a
**single post-judge stage**, not an architecture governing a flow — the `WUUDHL8R` / `BU73N7PC` negative
case (a component bolted onto a pre-existing pipeline). The paper's own phrase *"filter-embedded
framework"* is technical vocabulary, not a technical artifact.

**Reuse.** `framework` already carries the test in its slug text: ***"would someone adopt it as a
reusable pipeline design?"*** Here the answer is no, and the paper's availability statements say why:

> *"To facilitate **reproducibility**, we make the curated datasets and scripts publicly available…"*
> **Code Availability:** *"The **experimental framework** and mitigation filter implementation are available…"*

**Released ≠ released for use.** These are **reproducibility artifacts**, described by the authors as an
*experimental* framework. The filter also only runs where an executable test suite exists **plus**
GPT-4o-generated augmented tests — it is a robustness patch on the authors' own measurement, not a
component a team could drop into a review pipeline.

### 120c. `built-system` — boundary probed, definition UNCHANGED

The arbiter put a sharper test to the facet: ***"would someone use what they built in other scenarios,
or was it just applicable to testing their hypothesis?"*** — i.e. **contributed artifact vs experimental
apparatus**, the §104/§115 principle applied at facet granularity.

Probed and **deliberately not adopted.** Arbiter's ruling: *"let's not change `built-system`, keep as
is. `framework` captures the case I was thinking about."* The resulting **division of labour is now
explicit**, and this is the entry to cite when it comes up again:

| Facet | Question it answers | Kind of marker |
|---|---|---|
| `built-system` | **Did they implement and run it?** | existence / maturity |
| `framework` | **Would someone adopt it elsewhere?** | reuse / transferability |

**Why leaving `built-system` bare is right — the arbiter's statement of it, which governs:**

> *"**Built is counterpoint to design.** Design, they designed it but did not build. Built-system, they
> actually built it."*

The pair is a **binary on a single question — did it get made?** — and `design-only` is already declared
*"mutually exclusive with `built-system`/`adopted`."* The two slugs partition the space of papers that
propose a mechanism, and every such paper must land on exactly one side.

That is why a reuse test could not be loaded onto it: purpose-built apparatus **was in fact built**, so
it cannot take `design-only`, and denying it `built-system` would leave it in a gap the partition does
not admit. The ladder — *unvalidated design < expert-validated < built prototype < adopted* — grades
**how far past paper the thing got**, not how useful it would be to anyone else. Reuse is a different
question, and `framework` is where it is asked.

**Two consequences, both avoided by the no-change ruling:**

1. **Jin keeps `built-system`** (panel 3/3, correct). The filter was implemented, run, and reported
   before/after: **FPR 88.74% → 39.96%**. It exists; that is all the facet claims.
2. **Ferdous (`UIXCRBQX`) is NOT backed out.** The arbiter raised it as the likeliest casualty, and
   under the rejected test it would have been — the paper is unusually explicit that its tool is
   apparatus: *"…making these tools **unsuitable for our study**. Therefore, **we develop a tool** to
   detect potential [breaking changes]"* and *"To **validate the reliability of our tool**, we randomly
   selected 94 patches."* Built for their measurement, then calibrated as an instrument. Under the
   retained definition it is still built, and `built-system` stands.

**A superseded correction, recorded so the reasoning is not repeated.** The assistant initially argued
`built-system` from §115 — *the paper measures the effect of using the instrument*. That was the wrong
lever: §115 governs **whether apparatus rises to a contribution**, and measuring your own instrument's
effect on your own error rate is **internal validity**, not a contributed tool. `built-system` never
needed §115, because it never asked the contribution question in the first place.

**Related boundary already in the instrument:** `design-only`'s carve-out exclusion — *"metrics auditing
a measurement tool's/judge's OWN reliability = tool validation → context"* (`BAWCBT9R`). Ferdous's
94-patch validation is precisely that, which is why tool-validation evidence does not lift a paper's
disposition even where `built-system` applies.

### 120d. `rules-based-checks` — kept, with the qualification stated

Panel 3/3, retained. The arbiter's challenge — *"my read was that they tested their hypothesis against
LLMs, not that they built a system that others might use"* — is correct about the paper's centre of
gravity but does not defeat the theme: the filter is a **specified deterministic decision procedure**
(*"executes both against the benchmark test cases T and an augmented test set T̃. The final verdict is
determined by four common outcomes"*).

**Qualification worth carrying:** it is **not purely deterministic** — *"the test generation step is
standardized to GPT-4o"*, so an LLM produces the augmented tests the filter then executes. This is the
increasingly common **hybrid** shape: deterministic adjudication over LLM-generated inputs. Flagged as
a candidate refinement for the next versioned cut; **no change made now.**

### 120e. Open at closeout

- **`counterpoint` 2/3** — not carried (deprecated, §56). The `scaling-dissent` question was checked:
  Jin reports a **failure mode of a delegated reviewer**, not an argument that delegation is
  unworkable as a general matter. **Does not qualify.**
- **Queue hygiene** — Jin was added to `01 - Primary` and `04 - Validation Apparatus` but left in
  `03 - Queue`. The convention is inconsistent: **16 of 21** `01 - Primary` members have been removed
  from Queue, **5 have not**. Settle the rule and sweep the 6 at closeout.
- **Mode pair** — neither panel nor arbiter assigned `assistive`/`agentic`. Reasonably absent: the
  paper studies judges over benchmark programs, so no generation setting is under study. Noted so the
  silence is not later read as an omission.

## 121. `survey-input` REFINED to an elicitation test; and a debugging paper earns core on its explanation study (`7UB2MD8Z`, 2026-08-28)

**Paper:** Kang, An, Yoo, *Explainable automated debugging via large language model-driven scientific
debugging*, **Empirical Software Engineering** (2024-12).
**Written:** primary `oversight-explanation`; `hitl-workflow`; facets `general-code`,
`risk-overreliance`, `survey-input`, `routing-signal`, `method-self-report`, `agentic`,
`built-system`, plus pre-existing `evaluated-benchmark` and `method-experiment`.
**Declined:** `ai-review` (0/3, arbiter-proposed), `risk-routing`, `framework` (1/3),
`automation-bias` (1/3). **SLR: Core · Dissertation: Primary · 04 - Validation Apparatus.**

**No rejection tags were written.** Every panel-modal proposal (≥2/3) was endorsed; everything
declined was 1/3 or 0/3 and therefore never reaches `final:*`. Recorded because the absence of
`cal:human:reject:*` on a contested paper can otherwise read as an incomplete pass.

### 121a. Why an automated-program-repair paper is core

AutoSD prompts an LLM to form hypotheses, drives a **debugger** to test them, and emits a patch **plus
the reasoning that produced it**. On its face this is APR — a family we have demoted repeatedly. It is
kept because **the contribution is the explanation, and the explanation is evaluated on human
decisions**: a 20-participant study in which *"participants with access to explanations judged patch
correctness more accurately in five out of six real-world bugs."*

That satisfies §115 exactly — **an instrument becomes a contribution when the paper measures the
effect of using it** — and it is the corpus's strongest instance of *measuring* whether explanation
improves oversight rather than asserting it. Pairs with Zhou (`XRTVITVP`, *Steering LLMs*) and the
"when users should check" paper, supplying the outcome measurement that cluster otherwise lacks.

### 121b. §116a REFINED — `survey-input` fires on WHAT THE INSTRUMENT ELICITS

**Two wrong refinements were proposed and withdrawn before the right one.** Both are recorded because
each is a plausible reading that will recur:

1. **"The survey must be the paper's core."** Drawn from the arbiter's Catalan ruling (*"it wasn't the
   core… just a data collection mechanism"*). **Wrong** — it imports a *method* question into a
   **role** facet, and it would exclude Kang, which is a correct positive.
2. **"The survey findings must be useful to the org survey."** **Wrong for a different reason**, and
   the arbiter caught it: *"this should record the method used, not its significance, right?"* A
   utility test is **not reproducible** — another coder cannot apply it, and it drifts as our
   interests change. **The decisive evidence: the panel proposes `survey-input`** (2/3 here). Models
   have no access to our interest level, so whatever they key on must be a **visible property of the
   paper**.

**The rule that survives — an elicitation test, objective and panel-codeable:**

> **`survey-input`** = the instrument elicits **stated preferences, adoption, or priorities** — the
> kind of finding that can become an item in the org survey.
> **`method-self-report` only** = the instrument measures a **construct or performance** (cognitive
> load, engagement, comprehension, satisfaction, demographics).

Neither centrality nor significance enters. The two live rulings then reconcile **without revisiting
either**:

| Paper | What the instrument measures | Verdict |
|---|---|---|
| Catalan (`5BAZZWHG`) | a **construct** — cognitive engagement by Bloom level (*"assessing their reasoning, attention"*; *"(3) Understanding, (4) Analyzing, (5) Evaluation"*), perceived cognitive load | `method-self-report` only |
| **Kang (`7UB2MD8Z`)** | **stated preferences about tooling** — *"70% agreed [explanations were wanted]"*; *"half agreed or strongly agreed that explanations would be important **when using repair tools**"* | **`survey-input`** |

The arbiter's intuition (*"in Kang the survey results are something we are super interested in, whereas
in Catalan it is just a supporting player"*) was tracking a real difference — but the difference is not
our interest. **Kang asked people what they want; Catalan measured what they did.**

`survey-input` and `method-self-report` **co-occur** on Kang, consistent with §116a's standing note
that the two are different axes (finding-role vs evidence-production).

**Closeout consequence:** the `survey-input` re-check (≈10 silent-modal instances) now applies
*preferences vs construct*, not *is there a survey* — a faster and far more consistent call. Recorded
in `Methodology/Post_Accept_Closeout.md` §B2.

### 121c. `routing-signal` YES, `risk-routing` NO — a validated signal is not a router

AutoSD emits a `<DEBUGGING DONE>` token: *"we can **gauge how confident AutoSD is**"*, and RQ3 tests
whether it predicts correctness, motivated by *"if AutoSD can indicate when it is likely to be
correct, this [lets developers skip] **patches that AutoSD is not confident in**."*

That is a **computed, per-item, producer-independent signal** — `routing-signal` fires. But **no gate
is built on it**; they measure that the signal *predicts*, they do not route on it. This is the Branco
rule applied to a within-paper case: *"the study is not showing us how that [decision] is made."*
**§107e stands: a validated signal is a signal, not routing.** The pair on one paper is a clean
worked example of the boundary.

### 121d. `general-code` — a unanimous panel MISS worth noting

**0/3.** The object of study is **human-written buggy code** from repair benchmarks, not AI-generated
code. That is precisely what the facet exists to mark: the transfer audit trail for a kept-core paper
whose findings are about code in general. The panel proposed the mode facet (`agentic` 3/3) but missed
the scope facet entirely — consistent with §11.7's finding that panel recall is bounded, and a
reminder that the **scope** question in the seven-part checklist is the one most often skipped.

### 121e. `ai-review` declined — the AI repairs, the human reviews

Proposed by the arbiter, **0/3 from the panel**, and declined on examination. AutoSD's internal
verification is a **debugger executing hypotheses** — deterministic, not a model judging code — so the
Yu/`PPMTM4DG` self-review failure mode does not arise. The reviewing in this paper is done by
**humans reading explanations**, which is why the primary is `oversight-explanation` and the human
side is carried by `hitl-workflow`. The paper's own framing (*"full developer trust requires a manual
patch review"*) names the human as the reviewer.

## 122. §117 applied and OVERRULED by §111 — concrete routing advice in a discussion section does not rescue a measurement paper (`5NZ2EDEK`, 2026-08-28)

**Paper:** Karakaya, *Understanding the Limits of Automated Evaluation for Code Review Bots in
Practice*, arXiv (2026-04-27).
**Written:** primary `ai-review` (3/3); `general-code` (3/3); `method-mining` (2/3),
`method-experiment` (3/3), `method-self-report` (3/3); `evaluator-reliability`.
**`demote:context` · Dissertation: Supporting.**
**Declined:** `scaling-dissent`, `oversight-explanation`, `routing-signal` (1/3),
`hitl-workflow` (1/3), `cross-model`.

### 122a. What the paper is — a THREE-layer oversight stack, and two of the layers fail

The arbiter's initial read was *"a measurement of how good the feedback was from ACR by seeing what
humans did with it."* That is the paper's **setup**; its finding is that the setup does not work.

| Layer | Who checks whom | Verdict |
|---|---|---|
| 1 | ACR bot reviews the PR | not the object of study |
| 2 | **LLM-as-a-Judge / G-Eval score the bot's comments** | **0.44–0.62 agreement** with human labels |
| 3 | **developer `fixed`/`wontFix` labels = "ground truth"** | **contaminated** |

Layer 3 is the more interesting failure: *"**wontFix reflects organizational or contextual constraints
rather than purely technical non-usefulness**"* — *"local priorities, release pressure, ownership
boundaries, or timing"* — corroborated by an interview with Beko's director of software engineering.

**Carry this into the dissertation's own instrument design:** developer accept/reject signals are
**not** clean ground truth for whether AI review was useful. Any survey item asking practitioners
whether AI review comments were helpful inherits exactly this contamination. Logged in
`Emerging_Themes.md`.

### 122b. `scaling-dissent` DECLINED — the §56 polarity trap, second instance

The arbiter proposed it: *"it might be a dissent since they conclude that humans should not rely on
ACR, but just treat it as one of many potential signals."* The reading of the text is right; the
polarity is not.

The paper says **this particular delegation is not yet reliable, so do not rely on it alone.** That is
**the review's thesis**, not opposition to it. Dissent requires arguing delegation is unworkable or
impermissible **as a general matter**. This is the precise failure that killed `counterpoint` at §56 —
9/9 tagged a thesis-*supporting* paper as opposition. **First recorded human-side instance of the same
polarity error**, which is worth knowing: the trap is not model-specific, it is inherent to the
construct. Guard to keep applying: *"many things can be delegated, some can't" is the thesis
(`risk-routing`); dissent argues delegation itself is unworkable.*

### 122c. §117 APPLIED — and it changed nothing, which is the point

Per §117 (*read the implications section before ruling absence*) the arbiter's *"there isn't [anything
concrete on oversight or routing] by my read"* was checked rather than accepted. **§5.1 Implications
for Practitioners does contain concrete routing content**, none of it visible in the abstract:

> **"Use automated evaluation for triage, not decision-making.** A more conservative integration is to
> use automated scores to prioritize what to inspect (e.g., **routing low-score or disputed cases to
> manual review**), rather than to automatically accept or dismiss comments. This can **reduce
> evaluation cost while limiting the harm** from misclassifications."

Plus: scores *"require periodic sampling and human verification"*, and *"any deployment should include
**routine re-evaluation after model upgrades** or prompt/rubric changes."*

The first is this review's thesis stated as a deployment pattern — a cheap computed signal allocating
scarce human attention.

### 122d. Why it is STILL context — §111 governs

**§111: a proposed instrument does not rescue a measurement paper.** Karakaya *recommends* the triage
design in a discussion section: it never builds it, never evaluates it, and reports no data on whether
routing by score works. The arbiter's own Branco rule applies unchanged — *"the study is not showing
us how that decision is made."* `routing-signal` therefore stays off at 1/3; a recommendation is not a
validated signal.

The paper's actual contribution remains **judge-vs-human agreement measurement**, which §98 routes to
context through the `BAWCBT9R` precedent: *"metrics auditing a measurement tool's/judge's own
reliability = tool validation → context; the object is the evaluator, not AI-code risk."* Karakaya is
`BAWCBT9R` in an industrial setting.

**The rule this pair establishes:** §117 obliges the *check*, not a particular *outcome*. Reading the
implications section is mandatory before ruling absence — and it may still return "found, and it does
not change the disposition." Recording a §117 pass that **confirmed** the initial call is as useful as
recording one that overturned it (§117a), because otherwise §117 reads as a rule that always rescues.

### 122e. Dissertation Supporting — two named uses (§109a)

1. **Triage-not-decision** — a directly usable design principle for the oversight architecture, stated
   nowhere else in the corpus this plainly.
2. **Evaluator drift as a governance practice** — *"routine re-evaluation after model upgrades or
   prompt/rubric changes."* Nothing else in the corpus says the **oversight apparatus itself** needs
   periodic recalibration; pairs directly with the cross-model panel design.

### 122f. `evaluated-real-data` NOT introduced here

The paper is the natural first instance — an industrial corpus of 2,604 real PR comments rather than a
benchmark — but the slug has **zero uses** and remains staged (§41). **A slug's first instance sets its
working definition, and §42 short-circuits tag verification on demoted papers**, so a context paper is
the wrong place to establish one. Deferred to the F2 instrument cut, with this paper named as the
candidate seed.

## 123. AIDev — the source dataset demoted while its data anchors the corpus; and a 3/3 inversion primary REJECTED on §88 (`QI8246A3`, 2026-08-28)

**Paper:** Li, Zhang, Hassan et al., *The rise of AI teammates in software engineering (SE 3.0)*,
arXiv (2025-07-20). **This is AIDev** — 456,000 agentic PRs, 5 agents, 61,000 repos, 47,000 devs.
**Written:** `ai-review`, `quality-debt`, `provenance-auditability`; `agentic`, `method-mining`,
`risk-quality`, `problem-statement-anchor`. **`demote:context` · Dissertation: PRIMARY.**
**Rejected:** `oversight-scaling-inversion` (**3/3**), `survey-input` (2/3).
**No primary theme recorded — deliberately** (see §123c).

### 123a. A unanimous 3/3 primary REJECTED — the panel inferred inversion from pressure alone

All three vendors made `oversight-scaling-inversion` the **primary**. It is wrong, and the paper's own
headline finding contradicts it:

> **"Finding #2: Autonomous Coding Agents lag human in PR acceptance rates by a large margin"** —
> OpenAI Codex 64%, Devin 49%, GitHub Copilot lower.

**Agent PRs are accepted LESS often. That is gatekeeping holding, not leakage.** §87/§88's test is
*risky code escaping the review that should have caught it*, and AIDev evidences the opposite.

**What the panel actually anchored on** is the volume statistic — *"176 Agentic-PRs in 3 days vs. 176
Human-PRs over the previous 3 years"* — and inferred inversion **from pressure alone**. That is
precisely the inference the arbiter ruled out on Yang (§88): *"throughput down, queue up… Preventing
project work doesn't do it either. Has to result in leakage of risky code."*

**Significance for the reliability record:** a **3/3 correlated error on the PRIMARY slot**, on the
single tag already identified as the corpus's largest error source (closeout B1). It is further
evidence that unanimity measures instrument legibility, not truth (§11.4) — and a caution for the B1
sweep: the 15 papers carrying inversion on silence should be checked for **the same substitution of
volume pressure for demonstrated leakage**, which is likely the dominant failure mode.

### 123b. Demoted — a dataset has no mechanism to be primary about

The arbiter's read: *"leaning demote because it is about constructing a new evaluation dataset."*
Sustained, and the instrument's own **struggle signal** independently confirms it: *"can't pick a
primary / stretching a definition to fill the set = the paper likely doesn't belong at core."*

The contribution is **a dataset, descriptive findings, and nine research directions** — no mechanism,
nothing deployable. It is *not* a capability benchmark (the paper explicitly positions itself as
*"beyond synthetic benchmarks like SWE-bench"*), so the demote ground is **not operationalizable**
rather than *pure tool benchmark*.

### 123c. NO primary recorded — and why that is unambiguous

Recording a stretched primary purely to fill the slot would contradict the struggle-signal rule that
justified the demote. Leaving it empty is safe because **`demote:context` disambiguates it**: the B7
partial-detection predicate is *human tags **and** no primary **and** no demote*, so a demoted paper
without a primary reads as adjudicated, not partial. Closeout F3's surviving predicate (*primary AND
not demoted*) also resolves correctly. **This is the reference case** for demoted papers where no
theme fits.

### 123d. Dissertation PRIMARY despite the demote — the tier and the role are independent

Unusual pairing, recorded because the reasoning generalises. Three named uses (§109a):

1. **The corpus's best problem-statement anchor.** *"176 Agentic-PRs in 3 days vs. 176 Human-PRs over
   the previous 3 years"* — one developer, one figure, the whole scale shift. Nothing else quantifies
   it as cleanly, and it pairs with the finding that those PRs *"alter fewer structural aspects of
   code."*
2. **Bot-reviewer analysis the mining papers never report.** AIDev classifies reviewer identities and
   analyses *"the 10 most active bot reviewers among Agentic-PRs… in comparison to human reviewers"* —
   **agents reviewing agents, measured in the wild.** Directly relevant to the agent-panel thread and
   absent from Branco, Gao and Ghammam.
3. **The §116c citation anchor.** Branco (`JQPPKSFQ`), Gao (`59KP8GTP`) and Ghammam (`SHK6KAX6`) all
   mine AIDev and report **different review-absence figures**. Reconciling them requires the source;
   the dissertation must cite AIDev directly rather than through three secondary readings.

**The general rule:** SLR tier answers *"does this paper contribute a mechanism to the review's
argument?"* Dissertation role answers *"will I use this?"* A dataset paper can be **no** to the first
and **emphatically yes** to the second. Precedent for other substrate/infrastructure papers.

### 123e. `survey-input` REJECTED at 2/3 — the case §116a was written for

AIDev is **mined repository data**; there is no instrument at all. Under §121b's elicitation test
nothing is *elicited* — no participant states a preference. This is the Ghammam pattern (§116a) that
prompted the original narrowing, recurring on the source dataset itself. Rejected explicitly rather
than left silent, since at 2/3 it is modal and would otherwise stand into `final:*`.

## 124. Shift-Up — a 3/3 primary moved on altitude; and the `evaluated-*` ladder has a HOLE (`7SH86C2W`, 2026-08-28)

**Paper:** Lipsanen et al., *Shift-Up: a framework for software engineering guardrails in AI-native
software development — initial findings*, arXiv (2026-04-22). DSR; reinterprets BDD, C4 and ADRs as
guardrails for agent-driven development.
**Written:** primary **`hitl-workflow`**; `rules-based-checks`, `agent-scope-drift`,
`provenance-auditability`; facets `framework`, `built-system`, `agentic`, `steering`, `risk-quality`.
**Rejected:** `method-experiment` (2/3), `method-self-report` (2/3), `counterpoint` (2/3).
**SLR: Core · Dissertation: Supporting.**

### 124a. PRIMARY moved from `rules-based-checks` (3/3) to `hitl-workflow` (2/3) — altitude, not evidence

The arbiter's challenge: *"rules based seems suspicious to me."* Checked, and the mechanism **is**
genuinely there — this is not steering wearing a checking costume:

> *"each user story was decomposed into **executable acceptance tests in Robot Framework 7 format**"* ·
> prompt: *"constraint (**test id's that must pass** for issue [closure])"* ·
> *"this cycle **repeats until all constrained acceptance** [tests pass]"*

So `rules-based-checks` is correctly applied — but it is **not the primary**. The tie-breaker governs:
*primary = the theme carrying its **distinctive novelty**, not the standard scaffolding.* An acceptance-
test loop gating a build is ordinary TDD/CI, merely pointed at an agent. The distinctive claim is:

> *"**verification [is] delegated to GenAI tools, allowing human developers to focus on the higher
> layers of the V-Model.** At the top-left, [developers] engage in acceptance testing, deployment
> oversight, and operational feedback. The objective of Shift-Up is thus to **free developers**…"*

**That is what the title means — *shift-up* = move the HUMAN up the V-model**, delegating implementation
*and* verification downward. A claim about **where the human sits** is `hitl-workflow`.

**Arbiter's statement of the ruling, which is the general form:** *"The gist of the paper is about how
human and machine work; rules are part of it, not the core."*

**Third consecutive paper where the panel anchored on visible machinery over framing** (§121d scope
miss, §123a volume-over-leakage, this). The pattern for the closeout: **panels read mechanisms well
and altitude poorly** — check every 3/3 primary against the tie-breaker before `final:*`.

### 124b. `steering` + `rules-based-checks` co-hold — dual-purpose artifacts, and NOT a demote trigger

The artifacts are explicitly both: *"not as documentation, but as **machine-readable, persistent
contextual constraints**"* (fed to the agent → `steering`) **and** executed as gates
(→ `rules-based-checks`). Recorded because `steering` at 3/3 could otherwise trip the demote menu's
**steering-only** clause. It is not steering-only; there is a real verification arm.

### 124c. BOTH method facets REJECTED — §98 world-or-tool, with the authors as subjects

> *"The methodology is then compared to a purely prompt-driven approach. **The authors worked as** [the
> developers]"* · *"**The authors** … re-familiarized themselves with, analyzed, and **categorized their
> own prompts**. Subsequently, the authors **cross-validated each** [other]"*

No external subjects; nothing characterises the world. Per §98 this is `built-system` evaluation and
**earns no method facet**. Authors categorising their own prompts is artifact analysis, not
`method-self-report` (which requires humans-as-subjects telling you something).

**Consequence — the honest evidence grade.** The paper produces **no empirical evidence about the
world**: n=1, self-built case, self-assessed, explicitly *"initial findings"* and *"intentionally"*
exploratory. That is why **Dissertation Supporting, not Primary** — the ideas are citable, the findings
cannot be leaned on.

### 124d. GAP FOUND — the `evaluated-*` ladder cannot describe this evaluation

Checked against every post-freeze slug; **none apply**. `cross-model` fails though two models are used
(*"GPT-5.0-Codex agent"*; *"Claude Sonnet 4.5"*) because they do **different jobs** — task allocation,
not mutual checking (the Karakaya rule). `agent-panel`, `evaluator-reliability`, `scaling-dissent`: no.

And **no rung of the `evaluated-*` ladder fits**: not a benchmark, not synthetic, not real-world data.
The evidence is *"a **qualitative evaluation** of the approaches according to 5 different categories:
upfront investment, human control, structured constraints, development speed, and guardrails"* — the
proposers judging their own artifact on a case they built.

**`built-system` says the thing exists; nothing says the only evidence is its authors' own qualitative
judgement.** That is the weakest evidence rung there is, it is common in this literature, and a review
about **oversight evidence quality** should be able to state it. **Candidate for the F2 cut:
`evaluated-self-demo`** (or similar). Not coined here — same reasoning as §122f: a slug's first
instance sets its definition and should not be established in passing.

### 124e. Dissertation named uses (§109a)

1. **The SE-discipline-for-agentic thread.** Pairs with Ji's shift-left (§119d): ***shift-up*** raises
   the human's altitude, ***shift-left*** moves the check earlier — the same gate-placement spectrum on
   **orthogonal axes**. Logged in `Emerging_Themes.md`.
2. **The prompt taxonomy** as question-seed material for the org survey. **NOT `survey-input`** — see
   §124f.
3. **The constructive answer to Jin (§120a).** Jin shows LLM *conformance* review fails badly (FPR to
   88.74%) **even when handed a spec**. Shift-Up makes the spec **executable**, so conformance becomes
   deterministic and needs no LLM judge at all. **Jin diagnoses; Shift-Up sidesteps.** Neither cites
   the other; the pairing is ours.

### 124f. §121b, third formulation — "it will yield survey questions" is not a criterion

The arbiter, on his own stated use of the prompt taxonomy: *"**May yield questions is different than
they did a survey.** May yield questions may come from mining or other sources."*

The cleanest statement yet of why the facet cannot be utility-based: **question-seeding is
unconstrained by source** — mined studies, experiments and position papers can all yield survey items,
so the property fails to discriminate at all. The three-part rule now reads:

| | requirement |
|---|---|
| §116a | an actual **survey instrument** must exist (not mined data) |
| §121b | it must **elicit stated preferences** (not measure a construct) |
| **§124f** | **"it yields questions for our survey" is not a criterion** — that is dissertation utility, recorded in the named-use list |

## 125. §119c's GAP FILLED — the first paper covering both modes; and the human baseline is ERODING (`9H6FWJME`, 2026-08-28)

**Paper:** Liu, Yue et al., *Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated
Code in the Wild*, arXiv (2026-04-26). 302.6k verified AI-authored commits, 6,299 GitHub repos, five
assistants, static analysis run **before and after** each commit, every introduced issue tracked to
the latest revision.
**Written:** primary `quality-debt`; `ai-code-insecurity`; `method-mining`, `risk-quality`,
`risk-security`, **`agentic` + `assistive`**, `problem-statement-anchor`.
**SLR: Core · Dissertation: PRIMARY.** **Declined:** `oversight-scaling-inversion` (0/3).

### 125a. BOTH mode facets applied — and this closes the §119c gap

**§119c logged an open gap:** *"the dissertation will need to argue that **the same underlying
technology powers both assistive and agentic scenarios**. **No corpus paper currently supports this** —
find a source, or argue it explicitly as the review's own position."*

**This is the source.** The five tools are *"GitHub Copilot, Claude, Cursor, Gemini, and **Devin**"* —
spanning inline assistive completion through fully agentic delivery — and the paper treats them as
**one class**, measuring identical debt outcomes across all of them. Both facets therefore apply, which
is unusual and correct: the mode pair marks *which setting the paper studies*, and this paper studies
both, deliberately.

**Why it matters beyond the tag:** the dissertation no longer has to assert mode-convergence as its
own position. It can cite a 302.6k-commit study in which assistive and agentic tools produce the
**same failure profile** — which is the empirical basis for treating oversight requirements as
mode-independent. §119c's action item is closed.

### 125b. The human baseline is ERODING — a finding hiding inside a limitation

The arbiter's critique: *"I would have loved to see comparison stats computed for human authored PRs.
**Is AI better, worse, or the same as human** rather than is it perfect or not."* Correct — and the
paper concedes it, with a reason that is more important than the omission:

> *"…AI-authored commits against a baseline of purely human-written commits. Because developers may
> use AI without [disclosure]… a **reliable human-only baseline is difficult to construct**, and
> comparing against an unreliable baseline could [mislead]."*

**The counterfactual is disappearing.** Once AI use is ubiquitous and undisclosed, *"human-authored
code"* stops being a measurable category. Three consequences worth carrying:

1. **Comparative claims have a closing window.** Papers that already made the comparison — **Xu**
   (quality below human) and **Ferdous** (`UIXCRBQX`: agents make **fewer** breaking changes than
   humans) — become *more* valuable as the baseline erodes, not less. Their measurements may be
   unrepeatable.
2. **"Is it perfect?" is the wrong question and increasingly the only answerable one.** Absolute defect
   rates without a baseline cannot support a deployment decision: 15% of commits introducing an issue
   is alarming or reassuring depending entirely on the human rate, which is now unmeasurable.
3. **Survey exposure.** Self-reported *"did a human or AI write this"* inherits exactly the
   contamination Karakaya (§122a) found in `wontFix` labels. Logged for the survey instrument.

### 125c. Statically DETECTABLE issues that survived — an oversight failure, not a capability failure

The arbiter's observation: the issues are found by **standard static analysis**, and clean static
analysis is a common pipeline gate. The paper's own numbers make the point sharper: **484,366 distinct
issues**, and **22.7% still present at the latest revision**.

These are not subtle defects requiring judgement — **a pipeline gating on clean static analysis
catches them by construction.** So the finding reframes: the tools to catch this already existed and
**were not gating**. That is a process failure, and it is the strongest argument in the corpus that
**existing engineering discipline, applied unchanged, would absorb a large share of AI-introduced
debt** — pairing directly with Ji's shift-left (§119d) and Lipsanen's Shift-Up (§124).

> **NARROWED by §133b (2026-08-28) — do NOT read this as "static analysis would solve AI code
> quality."** It holds for **Liu's defect class** (code smells, correctness and security issues that
> standard analysers already flag). It does **not** generalise: Parris (`3SU9QZ6F`) documents a class
> that *"can **pass standard static analysis** while exhibiting pervasive fail-soft behavior,"* because
> analysers are not calibrated for **failure-untruthfulness** (swallowed exceptions, optimistic
> returns). **Liu = a PROCESS failure** — detectable, not gated. **Parris = a DETECTION failure** —
> gated, not detectable. Existing discipline absorbs the first class only; the second needs
> purpose-built, AI-specific checks.

**`oversight-scaling-inversion` still DECLINED (0/3).** §88 requires **review failure as the cause**,
and the paper never examines whether review occurred. **89.3% of the issues are code smells**, which
teams routinely tolerate by choice rather than fail to catch — tolerated ≠ leaked. Given §123a, where
the panel over-applied inversion on comparably circumstantial reasoning, the bar holds.

### 125d. `evaluated-real-data` declined here — REDUNDANT with `method-mining`

The natural first instance: real production commits, no benchmark, no synthetic construction, and —
unlike the three prior candidates (§122f Karakaya, Liu `6ZC3H7AF`, §124d Lipsanen) — a **Core +
Dissertation Primary** paper, which is the right grade to establish a slug on.

**Declined anyway, on redundancy.** `method-mining` is defined as *"artifacts measured: repos, PRs,
commits, posts, logs, telemetry"* — mining **is** real-world data by definition, so on a pure mining
study the two tags carry identical information.

**Scoping decision for the F2 cut:** define `evaluated-real-data` **against `built-system`** — *a built
artifact evaluated on real production data rather than a benchmark or synthetic corpus.* That is a
genuine unmarked rung on the evidence ladder. Written as a general "real data" marker it becomes noise
on every mining paper in the corpus.

**DEFINITION SETTLED (arbiter, same day) — the discriminator is whether an artifact is under
evaluation:**

> *"In **real-data**, a **tool is developed** and that tool is **evaluated using real data**. Tool could
> be a pipeline. In **mining**, **pre-existing data is mined for insights. No new tool is being
> evaluated**."*

**Entailment to enforce when grafting: `evaluated-real-data` ⇒ `built-system`.** If nothing was built,
the tag cannot apply — which is exactly why it does not fire here. Full statement and candidate seeds
in `Methodology/Post_Accept_Closeout.md` §F2a.

## 126. CriticGPT kept on the CONFIGURATION data, not the method; and "scalable oversight" is two different things (`NRVQT89E`, 2026-08-28)

**Paper:** McAleese et al. (OpenAI), *LLM Critics Help Catch LLM Bugs*, arXiv (2024-06-28).
**Written:** primary `ai-review`; `hitl-workflow`, `oversight-explanation`, `automation-bias`; facets
`agentic`, `built-system`, `risk-quality`, `risk-overreliance`, `problem-statement-anchor`,
`evaluator-reliability`. **SLR: Core · Dissertation: PRIMARY.**
**Declined:** `risk-routing` (1/3), **`cross-model` (withdrawn — see §126c)**.
**Unchanged:** `method-experiment` + `method-field-study`, adjudicated in §34/§35's gold set.

### 126a. The keep-ground is narrow and must travel with the citation

The arbiter's opening position was that a paper about **training or evaluating a model** is normally a
demote for this review, and the scope objection was sharp: *"Our premise for scaling is that the human
doesn't have to look at everything… This is absolutely about reinforcement training of a model. A very
different animal."*

Sustained on the scope point. The paper is kept on **one ground only**, in the arbiter's words:
*"its data of human + AI is best makes a case for the joint review."*

**Why that ground holds:** this is the **only paper in the corpus measuring all three arms head-to-head
on the same tasks** — AI alone, human alone, human+AI. Kang (`7UB2MD8Z`) has two of them (humans with
explanations judged patch correctness better than humans alone, 5 of 6 bugs); nothing else has the
**AI-alone** arm alongside both. Deciding *what AI can review on its own* requires knowing how AI-alone
performs against the alternatives, and this is the only measurement of it.

**It also extends the delegation-limits family** the arbiter identified as Yu's and Jin's keep-ground
(*"evidence of leveraging machine for scaling oversight — delegate to machine"*):

| Yu (`PPMTM4DG`) | a model cannot catch its **own** defects |
| Jin (`A5WDGC7J`) | giving it a spec yields **overcorrection** instead (FPR to 88.74%) |
| **McAleese** | full delegation raises recall but **hallucinates**; adding the human back recovers precision at similar catch rate |

**Binding condition on use.** The keep is the configuration data, **not** the RLHF method. Recorded so
the paper is never cited for throughput scaling — see §126b.

### 126b. "Scalable oversight" names two different problems — the term collision

Forced by the arbiter's devil's-advocate question: *"Wouldn't this say that scaling human oversight
isn't possible since you still need a human (in partnership with AI) to look at everything?"*

**The paper's own framing answers it, and the answer is uncomfortable:** *"The ultimate goal of
scalable oversight is to **help humans evaluate model output in order to train** [better models]."*
In an RLHF labelling regime the human **cannot** leave any sample, because their judgment *is* the
product. Their scalable oversight = **quality scaling** (a better-equipped human on everything).
This review's = **throughput scaling** (the human does not look at everything).

**Diagnostic:** does the paper measure **time or volume**, or only **accuracy**? McAleese reports
contractors taking *"fifty minutes per example"* and **never claims the critic makes them faster.**
Better-but-not-faster does not scale throughput at all.

**The genuinely throughput-relevant finding is not the headline:** critics identified *"hundreds of
errors in ChatGPT training data rated as **flawless**"* — recovering coverage that human review at
volume had **already lost**. That speaks to what humans miss when they cannot look properly, which is
the allocation problem. Full statement in `Emerging_Themes.md`.

### 126c. `cross-model` WITHDRAWN — a fine-tuned critic is not a panel

The assistant proposed `cross-model` on the reasoning that a separate specialised critic checking
another model's output is the answer to Yu's self-review failure. **Withdrawn on the arbiter's
correction:** the slug is for **debate / multi-agent / mutual checking among models**, and CriticGPT is
**one** fine-tuned model doing a checking job. One model in a checking *role* ≠ models checking *each
other*. This is the fourth consecutive paper where a plausible `cross-model` reading was declined
(Karakaya = comparison, Lipsanen = task allocation, Liu = neither, this = single specialist), which is
a strong signal the slug needs its **boundary written into the F2 definition**, not just its name.

### 126d. The IDEALISED REVIEWER — human-arm baselines are optimistic

Arbiter: *"the human in this paper is likely less distracted and will do a better job. Reality is an
ugly thing."*

The human arm is **best-case** — paid to spend fifty minutes on one example, no release pressure, no
competing work. This biases the two headline findings in **opposite** directions:

- **"AI catches more bugs than human contractors" gets STRONGER** — it beat an *idealised* reviewer.
- **"Human+AI is best" gets WEAKER** — the team benefit was measured with an attentive partner. Under
  Karakaya's *"release pressure, ownership boundaries, or timing"* (§122a) a real maintainer
  contributes less, so the team advantage over AI-alone is an **upper bound**.

**General rule recorded** (`Emerging_Themes.md`): wherever a study's human arm is *paid, unhurried and
single-tasked*, its human-alone baseline is optimistic and its human-in-the-loop benefit is a ceiling.
Catalan's engagement decay is the mechanism that erodes it in practice.

### 126e. B7 CORRECTED — a "partial" may be a deliberate narrow-axis pass

This paper was flagged as a B7 partial (human tags, no primary). That framing was **wrong for this
paper**: §34/§35 record its `method-field-study` + `method-experiment` pairing as a **deliberate
adjudication** — two separate evaluation events, one per side of the ladder/method fork — and it sits
in the retained 21-item gold set.

**So it was examined, on one axis, on purpose.** The partial signal is real (no primary, theme layer
never considered) but it does **not** imply "unexamined." Closeout B7 amended accordingly: the four
partials must each be checked for a **prior narrow-axis ruling before being re-opened**, or a
deliberate adjudication risks being overwritten.

## 127. The corpus's first BUILT-AND-EVALUATED router; and a second 3/3 inversion rejected on population mismatch (`74GE3TF7`, 2026-08-28)

**Paper:** Minh, Dao Sy Duy et al., *Early-Stage Prediction of Review Effort in AI-Generated Pull
Requests*, arXiv (2026-01-27). 33,707 agent-authored PRs (MSR 2026 Mining Challenge).
**Written:** primary `risk-routing`; `agentic`, `method-mining`, `built-system`, `routing-signal`,
`problem-statement-anchor`. **Rejected:** `oversight-scaling-inversion` (**3/3**).
**SLR: Core · Dissertation: PRIMARY.**

### 127a. `risk-routing` — the strongest instance in the corpus, and the first that is BUILT

Every prior `risk-routing` candidate this session failed on the same defect: the routing was
**recommended, not built**. Karakaya proposed triage-by-score and never implemented it (§122d); Kang
validated a confidence signal but gated nothing (§121c). **This paper builds and evaluates the gate.**

- **Signal:** 35 static, creation-time features (Intent / Context / Complexity) — available *before*
  human review begins.
- **Model:** LightGBM, **AUC 0.958** on chronological splits, against CodeBERT at **0.52**.
- **Generalisation tested:** repo-disjoint **AUC ≈ 0.83**, *"validating that [the signals are general]
  rather than repo-specific"* — it is not memorising repositories.
- **The allocation result:** *"At a **20% review budget**… captures **69% of the high-effort PRs**."*
- **Policy, with thresholds:** *"We recommend a **Gated Triage Policy**: treat agents like junior
  interns, not senior engineers. Flag complex PRs (>500 additions), fast-fail those without plans, and
  enforce strict timeouts (14 days) to prevent backlog pollution."*

All four §107e clauses pass: computed (not human discretion), per-PR (not between-unit), per-item (not
aggregate tendency), and a gate rides on it (not throttling).

**Why it matters beyond the tag — this is THROUGHPUT scaling, stated as a budget.** §126b recorded that
the corpus supplies configuration performance in quantity and allocation rules almost never. This is
the allocation paper: it takes a **fixed human review budget** as the constraint and asks what fraction
of the expensive tail it can capture. That is the review's own question, answered with a number.

### 127b. `oversight-scaling-inversion` REJECTED at 3/3 — a population mismatch, not a volume argument

Second unanimous inversion rejection in the band (cf. §123a on AIDev), and the reasoning is finer here
because a genuine §88 route (i) argument exists:

- **For:** *"28.3% of PRs merge instantly"* — merged in under a minute is **observed review absence**,
  at scale, which is exactly route (i).
- **Against, and decisive:** the instantly-merged PRs are the *"narrow-scope updates (median 68 total
  changes vs 104)"* — merged fast because **trivial**, not because maintainers are swamped. The
  overload symptom is **ghosting**, and **ghosted PRs never merge**.

**The review-absence and the overload land on different PR populations, which breaks the causal link
§88 requires.** Nothing risky escapes: the cheap work is waved through appropriately and the expensive
work stalls in the open. **Arbiter concurred:** *"I don't see oversight inversion on this one."*

**Rule this sharpens for closeout B1:** route (i) requires review absence **caused by** the overload,
on the **same** population that the overload afflicts. Observed absence plus observed overload in the
same paper is **not** sufficient if they fall on disjoint sets. Add this to the B1 sweep alongside
§123a's volume-for-leakage substitution — **two distinct failure modes now identified**, and both
produced 3/3 panel agreement.

### 127c. The arbiter's extrapolation is IN the paper — as its own limitation

The arbiter, before reading the discussion: *"Even if agents are doing the reviewing, we could end up
in the same sad state of abandoned PRs because the coder agent couldn't deal with the feedback."*

The paper found exactly this, and calls it a limitation of its own model:

> *"We manually inspected false negatives and found a pattern of '**silent abandonment**': small PRs
> that look safe (no CI touches) but **stall because the agent cannot handle subjective feedback**.
> This implies that while we can catch the 'explosive' failures, the '**silent' failures require
> behavioral monitoring**."*

**Structural gates cannot see it.** The failure is not in the artifact — the PR looks fine — it is in
the agent's *inability to iterate* under feedback. **Replacing the human reviewer with an agent
reviewer does not fix this**, because the defect is on the authoring side of the loop. Logged in
`Emerging_Themes.md` as a named limit on full delegation.

Their own proposed fixes are worth carrying: *"**semantic risk models** to catch subtle logic bugs that
structural gates miss"* and *"**cryptographic identity to enable reputation tracking**"* — a per-agent
reputation signal, which is a routing input the corpus has nowhere else.

### 127d. `evaluated-real-data` — the first genuinely qualifying seed, HELD pending the arbiter's call

Under the settled F2a definition (*a tool is developed and that tool is evaluated using real data*),
this is the first clean instance: the Circuit Breaker is a built model evaluated on 33,707 **real**
agent PRs, not a benchmark or a synthetic corpus. The entailment holds — `evaluated-real-data` ⇒
`built-system`, and `built-system` is written.

It is also the first candidate at **Core + Dissertation Primary**, i.e. the grade §122f argued a
slug's first instance should be established on. The three earlier candidates were all demoted or
Supporting and were deferred for that reason. **Not written — awaiting an explicit call on whether to
apply it here or hold the whole ladder for the F2 graft.**

## 128. `risk-bias` in vocabulary ≠ in scope; and a third 3/3 altitude/mode correction (`QTJPLBYR`, 2026-08-28)

**Paper:** Naqvi et al., *Evaluating security and inclusivity in LLM-generated code: a controlled
experiment*, SSRN preprint (2026-01-10). Three prompting rounds; artifacts scored on security and
inclusivity by **13 human experts and 5 LLMs**.
**Written:** primary `ai-code-insecurity`; `ai-review`; `steering`, `method-experiment`,
`risk-security`, `risk-bias`. **Rejected:** `agentic` (**3/3**). **`demote:context`, no dissertation
role.**

### 128a. The demote ground — not operationalizable, NOT out of taxonomy

The arbiter's read: *"not related at all to our thesis"* / *"focus on inclusivity, neurodivergence."*
Sustained, but the ground needs stating precisely, because **`risk-bias` is in our vocabulary** —
inclusivity is a risk type the instrument already tracks. The paper is not off-taxonomy.

**It is a capability evaluation that contributes no oversight mechanism** — the *not operationalizable*
branch of the demote menu. It measures whether generated code meets security and inclusivity criteria;
it proposes nothing for **overseeing** either. Also an **unreviewed SSRN preprint** (*"This preprint
research paper has not been peer reviewed"*), which is not itself a demote ground but bears on how the
one transferable finding below can be used.

**Rule worth carrying:** *a risk type being in the vocabulary does not put a paper about that risk in
scope.* The instrument's risk facets describe **what a paper treats**; the core bar asks what it
**contributes to oversight**. Keeping these separate prevents a slow drift where any paper touching a
tagged risk is presumed core.

### 128b. The one transferable finding, recorded with its weakness

The paper tests two head-to-head **human vs LLM reviewer** hypotheses — the delegation question:

- **H2a — humans outperform LLMs at spotting inclusivity issues: SUPPORTED.**
- **H2b — LLMs outperform humans at detecting security vulnerabilities: NOT supported.**

Directionally consistent with Yu (`PPMTM4DG`) and Jin (`A5WDGC7J`) on the limits of delegated review,
**but well below their evidentiary grade**, and the reason is worth recording as a pattern:

> H2a's support is that *"human evaluators were **more critical** in their assessment of inclusivity,
> as reflected by consistently **lower scores**."*

**Severity is being used as a proxy for accuracy, with no ground truth.** A harsher scorer is not
necessarily a better detector — it may simply be miscalibrated. Same structural defect the arbiter
identified on Bhatnagar (§106: a comparison that does not vary the thing being measured). **Do not
cite H2a as evidence that humans out-detect LLMs.**

### 128c. `agentic` REJECTED at 3/3 — the Waseem rule, third application

The design is *"after each round, the LLM-generated code artifact [was evaluated]"* — **iterative
prompting with a human directing each round.** That is the arbiter's Waseem ruling verbatim:
*"Focused on vibe coding, which is **steering, not agentic**."* `steering` also carried 3/3, which is
the panel proposing both halves of a distinction it did not resolve.

Rejected explicitly rather than left silent: at 3/3 it is modal and would otherwise stand into
`final:*`.

### 128d. PRIMARY moved from `ai-review` (3/3) to `ai-code-insecurity` — altitude again

The object of study is the **security and inclusivity of generated code**; the human/LLM evaluation is
the **method** by which that object is measured, not the contribution. Panel put its primary on the
visible evaluation machinery.

**Third consecutive altitude correction** (§123a volume-over-leakage, §124a mechanism-over-framing,
this one method-over-object) — and the fourth including §121d's scope miss. The closeout pattern
recorded at §124a now has four instances: **check every 3/3 primary against the tie-breaker before
`final:*`.** On the evidence so far this is the panel's single most systematic error mode, and it lands
on the **primary** slot, which carries the most downstream weight.

## 129. A shipped LLM reviewer at ~40% precision — delegation RELOCATES the bottleneck (`HJMKADKU`, 2026-08-28)

**Paper:** Naulty et al., *Bugdar: AI-augmented secure code review for GitHub pull requests* (2025-05-05).
LLM + RAG vulnerability analysis wired into GitHub PRs, 56.4s per PR.
**Written:** primary `ai-review`; `built-system`, `framework`, `general-code`, `risk-security`.
**Rejected:** `method-self-report` (2/3). **`demote:context` · Dissertation: Supporting**
(child note `CAFH5M65`).

### 129a. Demote grounds — domain, not mechanism

The arbiter's read: *"a super-duper security scanner, which using an LLM, and can be integrated into
CI/CD… demote due to narrow focus. General-code BTW."* Sustained on all three points, with the domain
narrower than the framing suggests: *"decentralized applications, smart contracts"*, languages
*"Move and Solidity"*, keywords *"Blockchain, Web3"*, ground truth drawn from *"smart contracts and
blockchain-related code."* It is a **smart-contract auditing tool**.

`general-code` is correct — Bugdar reviews **all** PRs, not AI-generated code — but note it is **not**
the demote ground on its own (the instrument: *"`general-code` alone is NOT a demote reason"*). The
demote rests on the Web3 domain plus the absence of an oversight contribution beyond the tool itself.

### 129b. The paper's own numbers contradict its scaling claim — the finding worth keeping

**Detection precision 24–58%.** Best configuration *"precision of 58%, a recall of 73%"*; typical runs
**35–43% precision**. So **most findings are false positives** — in a paper whose motivation is that
*"automated tools frequently suffer from high false-positive rates, limiting their reliability."*

**And the scaling claim is speed-only.** *"Bugdar reduces the reliance on manual reviews"* rests on
line 286 — *"evaluated based on its **efficiency** compared to human reviews"* (56.4s/PR vs hours).
**Detection accuracy is never compared against human auditors.**

**The transferable point, and why it earns Dissertation Supporting despite the demote:** at ~40%
precision the human effort **does not disappear — it relocates, from reviewing code to triaging false
alarms.** Delegated review moves the bottleneck rather than removing it. This is §126b's
quality-vs-throughput distinction with a third case: a tool can be **fast** and still fail to scale
oversight, because the reviewer's output itself needs reviewing.

**Pairs with:** Jin (`A5WDGC7J`) — LLM reviewers overcorrect, FPR to 88.74% — and Minh (`74GE3TF7`) —
the maintainer attention tax. Bugdar is the **deployed** instance of the failure Jin measures in the
lab. The corpus is short of accuracy numbers from *shipped* tools rather than research prototypes, and
this supplies one.

### 129c. `method-self-report` REJECTED at 2/3 — world-or-tool

The evaluation is **tool performance** (precision/recall on smart-contract ground truth) plus a
**speed** comparison. Developer commentary in the text is anecdotal, not a data-collection instrument.
Under §98's world-or-tool test the results describe **the tool**, so no method facet is earned.
Rejected explicitly since at 2/3 it is modal and would otherwise stand into `final:*`.

### 129d. `framework` KEPT at 2/3 — the VibeGuard precedent

A single-concern architecture (scan PRs for vulnerabilities) wired into CI/CD. §49's carve-out governs:
*"not a one-off point tool… **a focused single-concern architecture qualifies** (VibeGuard, Hedwig)."*
Contrast Jin (§120b), where `framework` failed because the artifact was **one stage inside** someone
else's pipeline rather than an integration design of its own.

## 130. §111 INVERTED — a built instrument with no effectiveness measurement does not rescue a design paper (`5RKMGRNA`, 2026-08-28)

**Paper:** Nimraka et al., *An agentic-AI solution for intelligent code review* (2025-11-19). ICR —
parallel specialist LLM agents, GNN semantic-duplication detection, graph dependency-impact analysis,
rule-based PR title validation, shipped as a GitHub App + VS Code extension.
**Written:** primary `ai-review`; `built-system`, `framework`, `general-code`, `risk-quality`,
`risk-security`. **`demote:context`, no dissertation role.**

### 130a. The demote ground — the evaluation measures the software, not the oversight

The arbiter's question was the right one: *"Is the paper adding enough unique insight to keep though?"*
The evaluation section answers it:

> **"IV. EVALUATION — A. Evaluation Criteria.** The evaluation of the ICR system focused on
> **verifying its** [functionality]… **unit and integration testing**, with **all test cases passing**."

**They established that the software runs.** No precision, no recall, no ground truth, no comparison
against human reviewers — and the paper concedes the gap: *"accuracy of the underlying AI models also
presents [a limitation]."*

**The rule, as the inverse of §111.** §111 held that *a proposed instrument does not rescue a
measurement paper*. The complement now holds: **a built instrument whose effectiveness is never
measured does not rescue a design paper.** Building it is not evidence that it works; passing your own
unit tests is evidence about your test suite.

**Grading against the neighbours** — the same claim at three evidence levels, which is why this one
falls out:

| Paper | What was measured | Tier |
|---|---|---|
| Bugdar (`HJMKADKU`) | detection precision 24–58% against ground truth | Context + Supporting (the number is citable) |
| Lipsanen (`7SH86C2W`) | comparative qualitative assessment across three approaches | Core + Supporting |
| **ICR (this)** | **unit and integration tests pass** | **Context, no dissertation role** |

This is a weaker instance of the §124d ladder gap: `built-system` records that the thing exists, and
nothing distinguishes *"evaluated against ground truth"* from *"the test suite is green."* Reinforces
the case for an `evaluated-self-demo` rung at F2 — ICR sits **below** even Lipsanen's self-assessment.

### 130b. `agent-panel` DOES NOT APPLY — division of labour, third application

> *"a **parallel multi-agent architecture** orchestrated by LangGraph… each focusing on a **distinct
> category**: an Error Detection Agent for [errors]"* — plus security and performance agents.

§110/§112a governs: **a panel is agents answering the *same* question; role specialisation is division
of labour.** The discriminator — *"loses a job or loses a vote?"* — resolves cleanly: remove the
Security Agent and you lose security **coverage**, not a **vote**. No agent checks another's work;
they partition the input space.

Third application after David (§110) and Dutta (§112a). **The pattern is now stable enough to state as
a heuristic for the F2 `agent-panel` definition:** *parallel + specialist + distinct categories ⇒
division of labour. Panels require redundancy on the same question.* "Multi-agent" in a title predicts
nothing about which one it is.

### 130c. `framework` ADDED at 1/3 — panel under-called it

A multi-stage architecture (ingest PR → parallel specialist analysis → duplication/dependency checks →
structured review), distributed as a **GitHub App and VS Code extension** for adoption. Passes §49's
span test and §120b's reuse test. The panel put 3/3 on `built-system` and only 1/3 on `framework`,
which reads as anchoring on *"they built it"* over *"what shape is it."* Contrast Jin (§120b), where
`framework` was correctly rejected: one stage inside someone else's pipeline.

### 130d. The design ideas are real but not attributable here

The arbiter flagged the notable components: *"they looked at the **dependency graph** and search for
**duplicated code with semantic similarity** checks. That came out of other papers and is likely
something that any automated pipeline needs to consider."*

Agreed on both halves — including the second. GNN semantic-duplicate detection pairs directly with
**Huang** (`4T5QFWZE`), which *measured* the reuse collapse in AI-generated code; ICR builds a detector
for the problem Huang quantified. But the ideas **originate elsewhere**, so ICR is not the citation for
them, and it supplies no evidence that they help. **No dissertation role** on the arbiter's ruling
(*"demote away"*). The pipeline-component thread is recorded in `Emerging_Themes.md` against its
sources instead.

## 131. The apparent counter-example RECONCILED — same-standards is t=0 on the decay curve (`4FGIVVTG`, 2026-08-28)

**Paper:** Omidvar-Tehrani et al., *Evaluating human-AI partnership for LLM-based code migration*,
ACM (2024). Two between-subject experiments, **N=11**, participants reviewing real QCT-generated code
diffs, plus semi-structured interviews.
**Written:** primary **`hitl-workflow`**; `oversight-explanation`, `automation-bias`,
`rules-based-checks`; facets `agentic`, `steering`, `method-experiment`, `method-self-report`,
`risk-overreliance`, `risk-security`, `risk-quality`. **Rejected:** `survey-input` (2/3).
**SLR: Core · Dissertation: PRIMARY.**

### 131a. The finding, and the half that matters more

The arbiter flagged it as contrarian: *"they found that people treat the AI like a team mate, provide
the same due diligence as they would a PR from human. This goes against some of the other data about
them getting less scrutiny."* The text supports it — and then keeps going:

> *"developers consider AI to be a **teammate and hold the code produced to the same standards** as that
> of a teammate… they expect a certain level of rigor and thought put into it. **However, they do
> understand that their teammates may require some hand holding in the beginning.** Developers are
> willing to provide this handholding to teammates, **with the unspoken expectation that these
> teammates will learn over time**."*

**The teammate frame imports an expectation of learning, and that expectation is false.** A junior
colleague absorbs correction; a model does not learn from your handholding within the engagement. So
the patience developers extend is **priced against a return that will not arrive** — a misapplied
mental model rather than an accurate one. This is why `automation-bias` sits at 3/3 alongside a
same-standards finding that would otherwise look like its opposite.

**Carry this into the survey design:** an instrument asking whether practitioners review AI output as
carefully as human output may get an honest *yes* that is nonetheless uninformative, because the
comparison class ("a teammate") carries assumptions the AI does not satisfy.

### 131b. NOT a contradiction — three papers, three points on one curve

The apparent conflict with the automation-bias cluster dissolves once the settings are lined up:

| Paper | Setting | Result |
|---|---|---|
| **Omidvar** (this) | N=11 recruited **to review diffs**; reviewing *is* the task | full scrutiny |
| **Catalan** (`5BAZZWHG`) | repeated cycles over time | **engagement decay** |
| **Ghammam** (`SHK6KAX6`) | artifacts in the wild | oversight theatre |

§126d's **idealised reviewer** applies directly: participants recruited to review are attentive *by
construction*. Omidvar plausibly measures **t=0** — scrutiny before decay — rather than refuting decay.

**This is a testable claim, not a rhetorical patch:** it predicts that initial scrutiny of AI output is
**genuine and erodes**, rather than being absent from the outset. That distinction matters for
intervention design — if scrutiny starts real, the remedy targets *sustaining* attention (rotation,
forced escalation, cadence limits); if it were never there, the remedy targets *establishing* it.
Logged in `Emerging_Themes.md`.

### 131c. PRIMARY moved from `oversight-explanation` (3/3) to `hitl-workflow` (3/3)

The paper states its own contribution as *"human's role in the human-AI partnership (**human as a
director and a reviewer**) and define a **trust framework**"* — role definition and trust calibration,
not explanation design. `oversight-explanation` is retained as a theme (comprehension of model output
is substantively treated) but is not where the effort lives.

**Fifth altitude/scope correction in the band** (§121d, §123a, §124a, §128d, this). Every one landed on
the **primary** slot; four of the five were unanimous. The closeout action stands and is now
well-evidenced: **check every 3/3 primary against the tie-breaker before `final:*`.**

### 131d. `survey-input` REJECTED at 2/3 — the instrument requirement bites

A genuine edge case, and a useful one for the B2 sweep. The interviews **do** elicit stated
preferences — what makes developers trust model output — so they **pass §121b's elicitation test**.
They fail **§116a's instrument requirement**: *"The intention for input-survey was a user survey —
Likert scale, etc."* Semi-structured interviews are self-report, not a survey.

**The two tests are conjunctive, and this is the first case that isolates them:** every prior ruling
turned on elicitation (Kang on, Catalan off) or on the absence of any instrument (Ghammam, AIDev).
Here the elicitation test passes and the tag still fails. **Both conditions must hold**, and the B2
sweep should apply them in that order — instrument first, then elicitation — because the instrument
check is cheaper and disposes of interview-only studies immediately.

## 132. Authority is A factor, not THE factor — and the PM-discipline gap recorded without a citation (`N7E3MR2V`, 2026-08-28)

**Paper:** P, Praneesh Roshan; Thavasi, M; Jaslin, C Quba, *SDLC AutoPilot AI: agentic automation of
software development life cycle*, ICOIICS 2025 (IEEE), 2025-11-19.
**Written:** primary `org-governance`; `hitl-workflow`, `rules-based-checks`,
`provenance-auditability`; facets `design-only`, `framework`, `agentic`, `steering`, `risk-quality`.
**`demote:context`, no dissertation role.**

### 132a. Demote ground — evidence-to-claim proportionality, applied uniformly

The abstract promises end-to-end SDLC orchestration *"to ensure accountability and resilience, the
system includes **governance guardrails for human approval**, observability features such as decision
logs and audit trails."* What is **specified and measured** is the estimation model (a COCOMO-style
parametric baseline plus a learned residual, evaluated control-vs-treatment on accuracy / precision /
recall / F1) and role allocation.

**The oversight half is asserted, not designed.** *"human approvals at critical points"* appears twice
with no criteria, thresholds, escalation rules, or statement of who approves what; audit trails are
named as features and never specified. **Same ground as Naulty (§129) and Nimraka (§130)** — the thing
built and measured is not the thing that would make it core — applied uniformly across all three.

Also note **"role assignment" is not agents-in-engineering-roles**: *"Role Assignment Agent: **Matches
tasks to resources**"*, forming human teams. The agents map to **PM/coordination functions**
(requirement parsing, planning, role assignment, milestone tracking). **Fourth application of §130b** —
specialists on distinct functions are **division of labour**, not `agent-panel`.

### 132b. Authorship — the boundary between a legitimate factor and a retroactive filter

The arbiter raised author level (*"authored by student. What level of student? If not doctoral, that
might be an issue"*), citing precedent that **unaffiliated researchers were demoted partly on
credibility**. Facts: two authors listed as *"Student"* with `22am155@` / `22am236@` emails — the `22`
being the 2022 admission cohort, so **final-year undergraduates** — supervised by **C Quba Jaslin,
Assistant Professor**, same institution. Minor IEEE conference.

**Citation count — first application of decided signal #1, and it immediately vindicates the
decision.** `Citegeist.citedByCount: 0`; **Google Scholar: 2** (arbiter, retrieved 2026-08-28).
Recorded on the item per the §394 convention — `GS.citedByCount: 2` / `GS.retrieved: 2026-08-28` in
`extra`, **alongside** the Citegeist fields rather than replacing them, so the discrepancy stays
inspectable. This is exactly the failure mode §394 predicted: *"any authority argument built on the
existing enrichment would silently privilege arXiv and indexed venues."* The assistant reported 0 from
Citegeist without cross-checking — the error the manual-GS rule exists to prevent.

**The assistant initially argued authorship should not be used at all**, citing
`Selection_Criteria_By_Phase.md`'s design constraints: *"Apply it uniformly, or not at all"*;
*"Do not let the signal become an inclusion criterion retroactively… Re-filtering after the fact would
be a form of **HARKing**"*; and *"11 Light Read papers have zero citations and that is **uninformative,
not damning**."*

**Arbiter's correction, which is the ruling:** ***"Credibility of authorship is a factor, not THE
factor. Keep that in mind."***

**Reconciliation — the distinction that resolves both positions.** Authority is **already adopted** as
one of the four Garousi MLR criteria (*authority / accuracy / coverage / objectivity*, §Selection
Criteria item 8), and the preprint ruling explicitly preserves it: *"It does **not** flatten authority
differences… **Judge the paper, not the venue**."* What is **not** adopted is signal **#2** — turning
authority into a **formal metric** (track record, h-index) and **filtering on it**.

| Use of authority | Status |
|---|---|
| Qualitative input to a holistic assessment, alongside other factors | **Legitimate — already in force** |
| Sole or decisive ground for a disposition | **Not adopted** |
| Retroactive re-filter of already-screened papers | **Barred (HARKing)** |

**Applied here — the arbiter's statement of the compound ground (2026-08-28):** *"the main concern is
**undergraduate status along with design-only**. It is more of a **vision piece without backing
evidence of effectiveness** by junior people."*

**Neither factor is doing the work alone, and that is the point.** The principle this yields, which
generalises:

> **`design-only` + unestablished authorship = insufficient warrant.** An unevaluated proposal is
> credited *on the author's standing to have made it* — that is what a vision piece trades on. Remove
> the standing and nothing remains to credit, because the paper offers no effectiveness evidence of
> its own. Where the same design comes from an established group (Zhu, CSIRO Data61 + UNSW), the
> authority substitutes for the missing evaluation; here it cannot.

This keeps authority as **a** factor — it never decides alone, and it does not touch papers that carry
their own evidence. **A junior-authored paper with a real evaluation is unaffected by this rule**, as
is an unevaluated proposal from an authoritative group. Only the **conjunction** disqualifies.

**Corrections withdrawn by the assistant:** citation count as a signal (the doc calls zero citations
uninformative), and the claim that authority has no legitimate role.

### 132c. Dissertation role DROPPED — the gap is stronger than the citation

The arbiter valued two design ideas: *"the authors leverage the design of human engineering processes
for agentic processes and identify agents for common roles in the SDLC… They also brought in
**estimation, work breakdown structures**, etc., bringing **project management discipline** in."*

The second is a **genuine hole in the corpus**: every oversight framework reviewed governs **code
quality**; **none governs commitment and forecast**. If agents produce work at volume, someone must
estimate, sequence and budget it — and no corpus paper addresses that.

**Recorded as a gap, not as a citation** — the §130d move. A 2-citation undergraduate paper at a minor
venue is a credibility risk as an authority for an idea it did not originate and does not validate,
and the observation stands on its own without it. Note the count is **not** the reason: per the design
constraints, low citation counts are *"uninformative, not damning"* in a corpus that is 77% 2025–26. `Emerging_Themes.md` carries the gap.

## 133. Fail-soft as a REWARD ARTIFACT; the baseline problem solved by temporal cutoff; and §125c narrowed (`3SU9QZ6F`, 2026-08-28)

**Paper:** Parris, *AIRA: AI-induced risk audit — a structured inspection framework for AI-generated
code*, arXiv (2026-04-19). Three studies: enterprise environment audit; 600-file balanced pilot;
**matched-control replication, 955 AI-attributed vs 955 human-control files**.
**Written:** primary `rules-based-checks`; `ai-review`, `quality-debt`; facets `built-system`,
`framework`, `method-mining`, `method-field-study`, `metrics`, `risk-quality`, `agentic`,
`problem-statement-anchor`. **SLR: Core · Dissertation: PRIMARY.**

### 133a. The Reward-Shaped Failure Hypothesis — a directional pathology, not random bugs

> *"AI-generated code **fails quietly**, in ways that preserve the surface appearance of function"* ·
> *"**Silent exception handling** — because a swallowed error **looks like** continued success"* ·
> *"**Optimistic return values** — because returning None or raising **feels like giving up**"* ·
> *"RLHF inherently trains models toward **fail-open** behavior."*

**The mechanism is goal-orientation, as the arbiter read it:** the model optimises for the *appearance*
of success because appearance is what the reward signal rewarded. That makes fail-soft a **structural
artifact of training**, not a random defect distribution — a claim with a testable direction, and the
paper tests it: **0.435 high-severity findings/file (AI) vs 0.242 (human) = 1.80×**, consistent across
JavaScript, Python and TypeScript, concentrated in exception handling.

**Family resemblance:** same shape as Alami (`WBS9U5N7`, specification gaming) — optimisation pressure
producing a systematic, *directional* pathology rather than noise. Both argue the failure is **caused
by how the system was trained**, which is why neither is fixable by better prompting.

**Why `rules-based-checks` is primary and not merely instrumental:** AIRA's 15 checks are
**deterministic** — the only deterministic reviewer in a corpus otherwise full of LLM judges (Jin,
McAleese, Bugdar, ICR). The paper positions it for *"governance, compliance, and safety-critical
systems where **fail-closed** behavior is required"*, so the checker is the contribution, and §115 is
satisfied by the three studies measuring what it finds.

### 133b. §125c NARROWED — two different defect classes, two different failures

Parris directly contradicts a generalisation recorded on Liu/Debt two entries earlier:

> *"a codebase can **pass standard static analysis** while exhibiting pervasive fail-soft behavior"* ·
> *"**Standard code review practices are not calibrated to detect this**."*

| | Defect class | Detectable by standard tooling? | Failure type |
|---|---|---|---|
| **Liu** (`9H6FWJME`) | code smells, correctness, security | **yes** | **process** — detectable, not gated |
| **Parris** (this) | failure-**untruthfulness** (swallowed exceptions, optimistic returns) | **no** | **detection** — gated, not detectable |

§125c amended in place. The corrected reading: *existing engineering discipline absorbs a large share
of AI-introduced debt* — **but not this class**, which needs a purpose-built check because analysers
were never calibrated for it. This is the strongest argument in the corpus for **AI-specific** review
tooling rather than reusing what already exists.

### 133c. The eroding baseline — SOLVED by temporal cutoff, at a price

§125b recorded Liu's concession that *"a reliable human-only baseline is difficult to construct"*
because AI use is undisclosed and interleaved. **Parris constructs one anyway:**

> *"Human-control files were sourced from repositories whose **most recent commit predates January**
> [the AI-tooling cutoff]."*

**The trade:** a temporal cutoff buys a genuinely AI-free control and pays in a **temporal confound** —
pre-cutoff repositories differ in language versions, tooling, practice and project maturity, so some
of the 1.80× may be era rather than authorship. Honestly made and clearly the best available answer;
**the only working response in the corpus to the eroding-counterfactual problem**, and the method to
cite when the dissertation discusses why human baselines are disappearing.

**Note the interaction with §125b's implication:** the window is closing for *interleaved* baselines,
but a temporal-cutoff baseline stays constructible indefinitely — it just drifts further from the
present each year, which converts a *feasibility* limit into a *validity* limit.

### 133d. Fourth AIDev-derived paper — §116c citation discipline

Agent-attributed files were *"sourced from the **AIDev dataset** [Li et al.]"*, joining Branco
(`JQPPKSFQ`), Gao (`59KP8GTP`) and Ghammam (`SHK6KAX6`). **Four corpus papers now derive findings from
one dataset**, whose source paper is itself Context + Dissertation Primary (§123). The dissertation
must state this dependency explicitly — four "independent" results sharing a substrate are not four
independent confirmations, and the closeout should record which findings rest on AIDev.

### 133e. The arbiter's reflexive observation — our own convention fails OPEN

Recorded because it is a real design property of this review, surfaced by the arbiter while reading a
paper about fail-open behaviour: *"We've had in HOS (and even **this session**) loads of issues with
failing open when we should fail closed."*

**The three-state human layer is a fail-open design.** A panel-modal proposal **stands on silence**
(§10.8), so a tag survives into `final:*` unless someone actively rejects it. That is precisely why
`counterpoint` persists on deprecated papers (closeout B3) and why 15 papers carry
`oversight-scaling-inversion` unexamined (B1) — **the default is "let it through."**

A **fail-closed** convention would require an explicit endorsement for any tag to survive. That is a
different, more expensive instrument, and the choice was never made deliberately — it was inherited
from the supervised-band workflow. **Added to the closeout as a decision to take before `final:*`**,
with the observation that the review is, in miniature, subject to the pathology it studies.

## 134. Soft verification is CONSUMER-DEPENDENT — the same error rate is viable for a ranker and fatal for a human (`8VBH957K`, 2026-08-28)

**Paper:** Raghavendra et al., *Agentic Rubrics as Contextual Verifiers for SWE Agents* (2026-01-07).
An expert agent explores the repository, builds a context-grounded rubric, and candidate patches are
scored against it **without test execution**. SWE-Bench Verified, parallel test-time scaling: 54.2% on
Qwen3-Coder-30B, **+3.5pp over the strongest baseline**.
**Written:** primary `ai-review`; `agentic`, `built-system`, `risk-quality`, `evaluated-benchmark`,
`evaluator-reliability`. **`demote:context` · Dissertation: Supporting** (child note `GIDV2HHG`).

### 134a. Demote — verification for the AGENT, not for a human

*"Verification is critical for improving agents: it provides the **reward signal for Reinforcement
Learning** and enables inference-time gains through **Test-Time Scaling**"* · *"sampling multiple
candidates and **selecting the best one** using a verifier."*

**There is no human in the loop.** The paper names *"human-in-the-loop rubric refinement"* as **future
work**. Same ground as Yao and Yu-tuning (model-training focus), and the exact contrast with McAleese
(`NRVQT89E`), which was kept at Core **because** it measures a human arm (§126a). The distinction is
now load-bearing across three papers and should be applied as a rule: **verification serving agent
self-improvement is not oversight; verification serving a human decision is.**

### 134b. The finding worth keeping — and it is the SAME number read two ways

The arbiter's framing: *"In HOS, we tried this and eventually gave up, opting for **deterministic
guardrails** instead."* The paper explains why, without meaning to.

**Rubrics genuinely catch what tests miss:** *"rubrics surface diagnostic concerns (e.g., unnecessary
edits or missing edge-case handling) **even when tests** [pass]"* — **Root Cause Missed 17.5%**,
**Missing Edges 15.1%**, and *"**54% of rubric failures are high-utility**."*

**Read the other way: ~46% of rubric rejections are noise.**

> **The principle: soft verification is viable as an *automated ranking signal* and not as a
> *human-facing gate*.** A best-of-K selector absorbs 46% junk and still picks better patches — that is
> where the +3.5pp comes from. **A human reviewer cannot absorb that**, because every spurious
> rejection costs attention, which is the scarce resource (Minh, §127a). *Same signal, same error
> rate, opposite viability depending on who consumes it.*

**This resolves an apparent conflict in the corpus rather than adding to it.** Papers reporting soft
verification as successful and papers reporting it as unusable are **both right**, and differ in
consumer:

| Consumer | Tolerates false positives? | Corpus evidence |
|---|---|---|
| **Automated ranker / RL reward** | **yes** — noise averages out over K samples | this paper, +3.5pp at ~46% low-utility rejections |
| **Human reviewer / gate** | **no** — each false positive spends attention | Jin (`A5WDGC7J`) 88.74% FPR · Bugdar (`HJMKADKU`) 24–58% precision |

And it explains why the **deterministic** route is the one that survives contact with a human
downstream: Parris/AIRA's 15 checks (`3SU9QZ6F`), Lipsanen's executable acceptance tests
(`7SH86C2W`), Zhong's 30 verifiers (`96XE669R`). **The arbiter's HOS trajectory — rubrics abandoned
for deterministic guardrails — is the predicted outcome of putting a human at the consuming end.**

### 134c. `rules-based-checks` DECLINED at 1/3 — the distinction is the whole point

Rubrics are **LLM-judged**, not deterministic. Tagging this `rules-based-checks` would collapse
precisely the axis §134b is about. The theme is reserved for deterministic evaluation; a checklist
scored by a model is `ai-review`, however rule-shaped the checklist looks.

### 134d. `evaluated-benchmark` and `evaluator-reliability` ADDED (both 0/3)

**`evaluated-benchmark`** — SWE-Bench Verified, administered as-is under its own protocol, which is
exactly §34's requirement (*"the real, fixed, field-recognized thing, run as-is"*), as against
author-curated material sourced from a well-known pool.

**`evaluator-reliability`** — the paper measures rubric–ground-truth agreement and audits the
**utility distribution of rubric failures**, which is the facet's subject. Panel proposed neither;
both are scope/evidence-grade facets, the class the panel most consistently misses (cf. §121d, §130c).

## 135. Superseded by its own successors; and the RELAY — a third multi-agent shape (`DJHG9BBS`, 2026-08-28)

**Paper:** Rasheed et al., *AI-powered code review with LLMs: early results*, arXiv (2024-04-29). Four
specialised review agents (Code Review, Bug Report, Code Smell, Code Optimization) with sequential
handoff and a coordination layer.
**Written:** primary `ai-review`; `built-system`, `framework`, `general-code`, `risk-quality`.
**`demote:context`, no dissertation role.**

### 135a. The evidence floor of the band — a results section with no numbers

The arbiter's question was *"Is it adding anything new?"* Section 4, **"Preliminary Result"**, answers
it. In full, its findings are:

> *"demonstrated a **strong capability**"* · *"**showed good performance**"* · *"was **effective**"* ·
> *"**generally well aligned**"* · *"**in several cases**"* · *"in several test cases"*

**No dataset size, no accuracy, no baseline, nothing counted.** Accuracy is explicitly deferred:
*"our **future** research aims to evaluate the accuracy and efficiency."* The title's *"early results"*
is honest.

**Grading against the band** — this sits below every comparable paper, which is why it falls out where
Nimraka and Naulty were already marginal:

| Paper | Evidence produced |
|---|---|
| Naulty / Bugdar (`HJMKADKU`) | precision/recall against ground truth (24–58%) |
| Lipsanen (`7SH86C2W`) | structured 3-arm qualitative comparison, 5 categories |
| Nimraka (`5RKMGRNA`) | unit and integration tests pass |
| **Rasheed (this)** | **narrative assertion; no comparison, no numbers** |

It is the clearest case yet for the **`evaluated-self-demo`** rung queued at F2 (§124d) — and arguably
sits *below* it, since there is no demonstration protocol at all, only prose.

### 135b. REDUNDANCY — every claim it makes is measured elsewhere in the corpus

The decisive ground, and stronger than weak evidence alone. Its central empirical claim:

> *"in several cases, it detected issues that **traditional static analysis tools either missed** or
> reported with very limited explanation."*

**Raghavendra (`8VBH957K`) measures exactly this** — rubrics flag what tests miss: **Root Cause Missed
17.5%**, **Missing Edges 15.1%**, 54% of failures high-utility (§134b). Rasheed *asserts*; Raghavendra
*quantifies*. Likewise the architecture: **Nimraka** builds the four-specialist design more completely,
and **Dutta** (`399HN438`) confirms specialist review agents perform well.

This is the **Hjazeen ground** (`VFNJSZD9`, kept out of the dissertation collection because *"Mitropoulos
and Parris already demonstrate the trust-boundary claim it only asserts"*), applied at the SLR tier.
**Priority is not a criterion in this review** — being first to propose something the corpus later
measures does not earn core, and a 2024-04 preprint superseded by 2025–26 work is exactly that case.

Also `general-code` 3/3: the object is **code review generally**, not AI-generated code.

### 135c. NEW — the RELAY shape, a third multi-agent topology

Fifth application of §130b (*specialists on distinct aspects = division of labour, not `agent-panel`*),
but this instance is **not parallel**:

> *"forwards its findings to **subsequent agents** for deeper analysis within the multi-agent
> workflow"* · agents operate *"after the initial review phase and **receive the preliminary
> findings**."*

**Three shapes now distinguished, and the F2 `agent-panel` definition should name all three:**

| Shape | Question | Arrangement | Failure mode |
|---|---|---|---|
| **Panel** | the **same** question | redundant, votes | correlated error survives unanimity (§11.4) |
| **Parallel division** | **distinct** questions | concurrent, independent | gaps between specialisms; no cross-check |
| **Relay** | **distinct** questions | **sequential, each consuming the prior's output** | **errors COMPOUND** |

**The relay is the one worth flagging as a design hazard.** A later agent reasons *on an earlier
agent's findings*, so an upstream false positive propagates and is elaborated rather than averaged out
— the opposite of a panel, where redundancy damps error. Given the false-positive rates the corpus
records for LLM reviewers (Jin 88.74%, Bugdar 24–58%, Raghavendra ~46% low-utility), **a relay of LLM
reviewers is the architecture most likely to amplify them, and no corpus paper measures this.** Logged
in `Emerging_Themes.md` as an open question.

## 136. Literature figures presented as findings; and a high-FWCI paper that fails the quality read (`5Q4G4CQB`, 2026-08-28)

**Paper:** Salem et al., *AI-driven continuous integration: automating code review and deployment with
LLMs*, FMEC 2025 (IEEE), 2025-05-19.
**Written:** primary `ai-review`; `assistive`, `method-self-report`, `survey-input`, `risk-quality`,
`risk-overreliance`. **Rejected:** `risk-bias` (3/3), `risk-security` (3/3), `method-field-study`
(3/3). **`demote:context`, no dissertation role.**

### 136a. The abstract attributes other people's numbers to itself

> **Abstract:** *"AI-based CI improves code quality by decreasing integration failure rates by **30%**
> and deployment time by **40%**."*
>
> **Body:** *"Data from the survey has shown that **85% of the members FEEL** that AI-assisted code
> reviews make work faster. **A figure that is consistent with the literature** and says the use of AI
> in driving CI/CD reduces general software delivery time by **40%**. For instance, the bug discovery
> rates would increase by **30%**, **an estimate that finds support in literature**…"*

**The paper's own datum is a perception** (85% *feel* it is faster). The 30%/40% are **literature
estimates cited as corroboration**, and the abstract restates them as this paper's results.

This is a step beyond the claim–evidence mismatch seen in Naulty (§129), Nimraka (§130), P (§132) and
Rasheed (§135): those **overclaimed about their own work**; this one **presents borrowed figures as
findings**. Recorded as a distinct and more serious failure mode, and one that abstract-only screening
cannot catch — a reminder of why the full-text read exists.

**Two supporting defects:** **no sample sizes anywhere** (survey recruited from *"media groups of
developers"*, no N, no response rate), and a methodology written in **future tense** — *"the study
**will apply** bias audit… Regular audits **will be conducted**"* — describing intentions rather than
what was done.

### 136b. `survey-input` KEPT (3/3) — a clean instance, both conditions met

Notable because §131d had just isolated the two conditions as conjunctive:
- **§116a instrument requirement** — a real **five-point Likert** survey exists. ✔
- **§121b elicitation test** — it elicits **stated attitudes**: *"85% feel…"*, *"60% of the respondents
  voiced their fears…"*, respondents raising false-positive concerns. ✔

The facet is about **what the instrument does**, not whether the findings are trustworthy. **The
findings here are uncitable for want of an N — but the tag is still correct.** Worth stating: tag
validity and evidence quality are independent axes, and conflating them would make the facet a
quality judgement in disguise.

### 136c. Three 3/3 facets REJECTED — the intro-list trap

`risk-bias`, `risk-security` and `method-field-study` all carried **unanimous** panel support and all
come off:

- **`risk-bias` / `risk-security`** — the instrument is explicit: *"substantive treatment only, **never
  intro-lists**."* The paper **enumerates** *"security vulnerabilities, model bias and the need for
  human supervision"* without developing either. `risk-quality` and `risk-overreliance` are kept
  because the false-positive and trust material **is** developed.
- **`method-field-study`** — the "case studies" are **selection criteria with no reported cases**
  (*"Case study criteria include companies…"*). Criteria for choosing cases are not cases.

**A four-risk-facet sweep is itself a tripwire.** When a panel assigns most of the risk axis at 3/3,
the likely cause is an enumerative paper, not a comprehensive one. Add to the closeout checks
alongside the §124a altitude sweep.

### 136d. AUTHORITY SIGNAL COUNTER-CASE — high FWCI, weak method (for E8/E9)

`Citegeist.fwci: 4.38` · `percentile: 94.6` · `isTop10Percent: true`. **This paper is well cited for
its field and year, and does not survive a careful read.**

Recorded as a concrete counter-case for the authority-signal decision (closeout **E8/E9**). It
supports the documented constraint that citation evidence is for **defending** the corpus in the
methods chapter, **not for filtering it** — and demonstrates the converse of the usual worry: the risk
is not only that good papers go uncited, but that **weak papers accumulate citations**. FWCI corrects
for field and year; it does not correct for rigour. **No citation-derived signal can substitute for
reading the paper.**

Pairs with `N7E3MR2V` (§132b), where the enrichment *under*-reported (Citegeist 0 vs GS 2). Between
them the two cases bound the problem: **the signal is noisy in both directions.**

## 137. A SCOPE demote with sound method behind it; and the corpus's only CONTROLLED speed-vs-quality tradeoff (`FWKYVQPD`, 2026-08-28)

**Paper:** Samsyudin et al., *Vibe coding and AI-led conversational programming: emerging trends in
software development* (2025-09-17). Quasi-experimental, **N=30**, **within-subjects** across three
conditions (traditional · AI-assisted/Copilot · vibe coding), ANOVA with effect sizes, plus post-task
SUS surveys and semi-structured interviews.
**Written:** primary `quality-debt`; `ai-code-insecurity`; `assistive`, `method-experiment`,
`method-self-report`, `survey-input`, `risk-quality`, `risk-security`, `intro-framing`,
`problem-statement-anchor`. **Rejected:** `agentic` (3/3). **`demote:context`.**

### 137a. Demoted on CONTRIBUTION SCOPE, not rigour — a distinction worth preserving

The last four demotes (§129 Naulty, §130 Nimraka, §132 P, §135 Rasheed, §136 Salem) were **evidence
failures** — things built or claimed without adequate measurement. **This one is different**, and the
record should not blur them: the method is sound. The failure is that the contribution is normative.

The "three-pillar framework" is three sentences:

> *"1. **Hybrid Integration** – Vibe coding should be used alongside, not in place of, traditional
> [practices]. 2. **Human Oversight** – Developers must retain responsibility for validating AI
> outputs. 3. **Context-Aware Deployment** – Adoption should be limited to non-critical
> applications."*

**"Human Oversight" here means "developers must retain responsibility."** That is the arbiter's
Bhatnagar ruling verbatim (§106): *"There is no insight about oversight, just that it was important."*
The paper concedes the status itself — *"a **preliminary** framework."* Hence `intro-framing`:
confirming a central tenet without advancing it.

**Why the distinction matters for the methods chapter:** "demoted" is doing two different jobs across
this band — *we cannot trust what it reports* versus *we trust it and it is not about our question*.
The second is a scope judgement and carries no criticism of the work.

### 137b. The finding that survives — a CONTROLLED speed-vs-quality tradeoff

Checked after the disposition was settled, and better than expected. Within-subjects, same
participants, same tasks, all three conditions:

| Measure | Vibe coding vs baseline |
|---|---|
| Development time | **27% faster** than traditional · **12% faster** than Copilot-assisted |
| Duplicated logic | **15% more** |
| Complexity | **18% higher** |
| Potential vulnerabilities (scanned) | **22% more** |

**You go faster and produce worse code, measured on the same people doing the same tasks.** That is the
review's premise stated as a controlled result, and it is the **only** controlled version in the
corpus — Xu, He, Liu (`9H6FWJME`) and Huang all reach compatible conclusions by **mining**, which
cannot rule out selection effects (who adopts AI, on what kind of work). A within-subjects design can.

**Specific corroboration:** the **15% more duplicated logic** is the experimental counterpart to
**Huang** (`4T5QFWZE`, *More code, less reuse*), which mined the same phenomenon. Two independent
method families agreeing on reuse collapse is worth more than either alone.

`problem-statement-anchor` applied on this basis — **added beyond the approved tag set**, on the
strength of numbers checked after the arbiter's authorisation, and flagged as such.

**Open: this makes a case for Dissertation Supporting** that the disposition did not anticipate. The
counter-argument is N=30 with students mixed in and a *"vibe coding simulation"* rather than
production work. Left off pending the arbiter's call.

### 137c. `agentic` REJECTED at 3/3 — Waseem rule, fourth application

The experimental condition is *"Providing task instructions in natural language to the AI system"* —
vibe coding, which the arbiter ruled is **steering, not agentic** (Waseem). `assistive` is correct for
the Copilot baseline arm. Fourth application after Waseem, Catalan and Naqvi (§128c).

**Pattern worth noting for the F2 mode-pair wording:** the panel has now put `agentic` at 3/3 on four
separate vibe-coding papers. It appears to key on *"AI writes the code"* rather than on **who
initiates and at what granularity the work is reviewable** — which is what the pair actually cuts on.
The definition should lead with the initiation/granularity test rather than mentioning it mid-entry.

## 138. FORM FACETS REQUIRE A PROPOSED MECHANISM — and a productivity case study with no control (`D87A4CAS`, 2026-08-28)

**Paper:** Şeker et al., *Enhancing software development with large language models: a case study of
kolay.ai*, **Electrica** (2026).
**Written:** primary `hitl-workflow`; `rules-based-checks`; `assistive`, `steering`, `risk-quality`,
`method-field-study`, `method-self-report`, `intro-framing`.
**Rejected:** `built-system` (2/3), `framework` (2/3), `method-mining` (3/3), `agentic` (2/3).
**`demote:context`, no dissertation role.**

### 138a. NEW RULE — the form cluster presupposes a proposed mechanism

Four modal rejections is unusual, and two of them establish a rule worth stating generally.

**`built-system` and `framework` were rejected because there is nothing for them to describe.** The
authors built **Kolay.ai — a commercial product**, not a contributed oversight artifact. The paper
proposes no mechanism; it reports on adopting existing tools.

> **Rule:** the **form/maturity cluster** (`design-only` · `framework` · `built-system` · `adopted`)
> describes **the paper's proposed contribution**. Where a paper proposes no mechanism, **none of them
> applies** — regardless of how much software exists in the story. The instrument already scopes
> `design-only` this way (*"Only for papers that **propose** something"*); this extends the same
> scoping to the rest of the cluster, which was implicit and is now explicit.

**Why the panel got it wrong, and why it will recur:** the models key on *"a system exists"* rather than
*"a mechanism is offered."* Every commercial case study will trip this. Add to the F2 wording, and to
the closeout sweep alongside the §124a altitude check.

**`method-mining` (3/3) rejected** — there is no repository, commit or artifact analysis anywhere in
the paper. A straightforward unanimous error.

**`agentic` (2/3) rejected** — fifth application of the Waseem rule; this is prompt-driven delegation,
carried by `assistive` + `steering` (both 3/3).

### 138b. Demoted — standard practice described, and figures that cannot be checked

**The HITL content is practice, not contribution:** *"**HITL review:** Regular reviews were conducted
to correct hallucinations and inconsistencies in LLM-generated outputs"* · *"HITL validations and
post-sprint evaluations"* · *"manual oversight remains essential."* Bhatnagar (§106) again — *"no
insight about oversight, just that it was important."* Hence `intro-framing`.

**One near-miss:** *"routine coding tasks were **delegated to LLMs**, while more complex tasks"* went to
humans. That is allocation by complexity — the *shape* of routing — but a **generic statement with no
criteria**, which is the arbiter's Branco rule: *"If there is logic setup… then it might qualify. If it
is a generic statement, not so much."* No `risk-routing`.

**The productivity figures are unverifiable.** *"30–40% reduction in development time"* and *"30%
reduction in coding errors"* come from a **single self-reported project with no control** — there is no
baseline project to compare against. The same figures appear in the **introduction** as a general claim
and in the **results** as this project's outcome, leaving provenance ambiguous (the §136a pattern,
though milder).

**`problem-statement-anchor` deliberately NOT applied** — the contrast with Samsyudin (§137b) is the
point: that paper earned the facet on a **within-subjects** comparison; this one reports uncontrolled
self-assessment of the authors' own project. **Same headline direction, incomparable evidentiary
weight.** Anchors must be defensible under scrutiny, since they are the numbers most likely to be
quoted.

### 138c. `method-field-study` KEPT, with the contamination noted

A real project in a real setting, so the facet applies — but it is **the authors documenting their own
project**, so the "field" is observed by interested parties, and `method-self-report` (3/3) co-applies
for that reason. Distinguish from Lipsanen (§124c), where the method facets were **rejected** because
the authors evaluated their **own proposed framework** on a case they built: there, results described
the *tool*; here they describe a *real delivery project*, which is the world — however partially.

## 139. `rules-based-checks` REQUIRES DETERMINISTIC EVALUATION — an LLM-judged rubric is `ai-review` (`GCZQTNBD`, 2026-08-28)

**Paper:** Sollenberger et al., *LLM4VV: exploring LLM-as-a-judge for validation and verification
testsuites*, SC'24 Workshops (2025-02-11). LLM-as-judge over OpenMP/OpenACC **compiler validation
testsuites**.
**Written:** primary `ai-review`; `built-system`, `framework`, `agentic`, `evaluator-reliability`.
**Rejected:** `rules-based-checks` (**3/3**). **`demote:context`, no dissertation role.**

### 139a. THE RULE (arbiter, 2026-08-28)

> ***"Rubrics that are LLM evaluated are not rules-based-checks."***

**`rules-based-checks` requires the evaluation itself to be DETERMINISTIC** — a check whose verdict is
computed, reproducible, and independent of a model's judgement. **Rule-*shaped* criteria evaluated by
a model are `ai-review`**, however explicit the criteria look. The theme names *how the verdict is
produced*, not *how the criteria are written*.

**Why the distinction is load-bearing and not pedantry.** It is the axis §134b turns on: deterministic
checks and LLM judgements have **different error profiles**, and the whole soft-vs-deterministic
finding collapses if a rubric scored by GPT-4o counts as a rule-based check. Jin **88.74% FPR**,
Bugdar **24–58% precision**, Raghavendra **~46% low-utility rejections** — versus Parris's AIRA,
Töpfer's FCL verifier, Zhong's 30 verifiers, Lipsanen's executable acceptance tests, which either fire
or do not. **Collapsing them would erase the corpus's clearest practical result.**

Consistent with §134c, where the assistant declined the tag on Raghavendra for the same reason. This
entry promotes that one-off into the rule.

### 139b. Why this paper had nothing to reconsider

The arbiter's question — *"Another LLM as judge paper. We've demoted / discarded those in the past. Is
there anything in this one that should have us reconsider it?"* — checked, and the one plausible hook
fails:

**The *"agent-based approach"* is a SINGLE LLM, not a panel:** *"An agent-based approach involves
treating **the LLM as an autonomous agent** that interacts with its environment."* The *"pipeline"* is
*"pipeline stages and **parallel processing**"* — throughput, not redundancy. **No `agent-panel`
evidence**, which was the only reason to reopen the family.

Otherwise it sits further out than its predecessors: same class as Zhao (§98), Karakaya (§122) and
Raghavendra (§134); **narrower domain** (HPC compiler testsuites, judging compiler test cases); and
**no human anywhere**, which is §134a's settled rule — *verification serving automated validation is
not oversight; verification serving a human decision is.* The negative-probing design
(*"intentionally-erroneous code"*) is a third instance of a methodology the corpus already has, better
executed, in Jin's paired datasets and McAleese's tampering task.

### 139c. Retroactive exposure — 24 papers carry human-endorsed `rules-based-checks`

The rule is new, so prior applications need checking. **24 papers** carry it in the human layer
(3 as primary: Parris `3SU9QZ6F`, Töpfer `72W6R4JG`, Xie/VibeGuard `T8E8SCCG` — all deterministic, all
safe).

**Most are clearly correct** — executable tests, static analysers, constraint verifiers, security
gates. **The re-check population is papers where the evaluator is plausibly a model**, not all 24.

**One known hybrid, already flagged:** **Jin** (`A5WDGC7J`, §120d) — the Fix-guided Verification Filter
*executes* tests deterministically, but *"the test generation step is **standardized to GPT-4o**."*
**Deterministic adjudication over LLM-generated inputs.** The rule as stated does not settle this: the
*verdict* is computed, the *criteria* are model-authored. Left as written and referred to F2, which
should decide whether hybrid pipelines take both tags, the deterministic one, or a new slug.

Added to the closeout as **B10**.

## 140. THE PANEL PAPER — `agent-panel` and `cross-model` get their reference instance, and the correlation dilemma is answered (`A6ZE2A26`, 2026-08-28)

**Paper:** Ullah et al., *Vibe coding on trial: operating characteristics of unanimous LLM juries*,
arXiv (2026-02-12). 15 open models benchmarked on 82 MySQL text-to-SQL tasks under an
execution-grounded protocol; **unanimous committees of size 1–6** built from the top 6; TPR / FPR /
Youden's J reported per size **and per composition**.
**Written:** primary `ai-review`; `risk-routing`; **`agent-panel`**, **`cross-model`**,
`routing-signal`, `evaluator-reliability`, `metrics`, `built-system`, `method-experiment`, `agentic`,
`risk-quality`. **Preserved untouched:** `evaluated-synthetic` (§34/§35 gold-set ruling).
**SLR: Core · Dissertation: PRIMARY.** Arbiter: *"Ullah is gold. Our agent panel and cross vendor
wrapped up together."*

### 140a. The reference instance both staged slugs were missing

`agent-panel` and `cross-model` have been staged since §33 and applied by hand without a defining
case. **Four consecutive papers were declined** on `cross-model` — Karakaya (comparison), Lipsanen
(task allocation), Liu (neither), McAleese (§126c, one fine-tuned critic) — and five on `agent-panel`
as division of labour (§110, §112a, §130b, §132a, §135c). **This is the positive case for both:**

- **`agent-panel`** — N judges answer **the same question** on the same artifact, aggregated by an
  explicit rule (**unanimity to accept**). Redundant, not specialised. Removing a member removes a
  **vote**, not a job.
- **`cross-model`** — committees composed of **distinct models**, and composition is a measured
  variable rather than an implementation detail.

**Write both into the F2 definitions from this paper**, not from the multi-agent code-generation
literature (MetaGPT/ChatDev/AgentCoder), which is division of labour throughout.

### 140b. The correlation dilemma — ANSWERED, and the answer is composition

§(topology entry) posed the dilemma facing conjunctive gate-sets: **independent errors compound
across vetoes; correlated errors make unanimity decorative** (§11.4's 9/9 on a wrong tag). Nothing in
the corpus measured the correlation between judges. **This paper does:**

> *"**errors across judges can be correlated**"* · *"identify **complementary versus redundant** judge
> combinations"* · *"the exact **committee composition matters significantly**"* · *"where
> **conservatism delivers diminishing returns**"*

**The resolution: the variable is composition, not count.** You do not add judges, you add judges that
**fail differently** — and the paper identifies which combinations are complementary versus redundant.
That reframes the design question from *"how many reviewers?"* to *"which reviewers fail
independently?"*, which is answerable and currently unasked in practice.

**Consequence for the arbiter's architecture** (cross-vendor panel, specialists must all be satisfied):
the cross-vendor instinct is right — Yu (`PPMTM4DG`) establishes a model cannot check itself — but
**vendor diversity is a proxy for error diversity, not a guarantee of it.** §11.4 is the standing
counter-example: three vendors, three runs each, **9/9 wrong together**, because they shared a
misreading of the *instrument*. **Decorrelating the model does not decorrelate the prompt.** Ullah's
contribution is that complementarity is **measurable**, so it can be selected for rather than assumed.

### 140c. `risk-routing` ENDORSED at 1/3 — TPR *is* the human-review-avoided measure

The paper's own framing is this review's problem statement almost verbatim:

> *"What is missing is **a reliable way to tell which model written queries are safe to accept without
> sending everything to a human**."*

And the metrics are defined in exactly those terms: *"**TPR** captures utility: the ability to accept
correct SQL (**avoiding unnecessary human review**). **FPR** captures risk: the tendency to accept
incorrect SQL."*

All four §107e clauses pass — computed, per-item, within-unit, not human discretion — and a real gate
rides on it. **Second built-and-evaluated router in the corpus after Minh (`74GE3TF7`, §127a)**, and
the first where the router *is* a panel. Together they are the corpus's only quantified
**throughput-scaling** evidence (§126b).

**Direction of failure is the arbiter's, not BitsAI-CR's:** unanimity **to accept** means the default
is **reject** — *"safety first deployments where **false accepts are more costly than false
rejects**."* Fail-closed toward the codebase, which is the HOS orientation (§133e). The cost lands as
false rejects rising with committee size, which the paper measures as diminishing returns rather than
assuming away.

### 140d. The limitation that must travel with the numbers

**Domain: MySQL text-to-SQL**, where correctness is **decidable by execution** against ten
independently seeded databases. That is precisely what makes clean TPR/FPR measurement possible — and
precisely what is **absent** in general code review, where there is no oracle (Karakaya §122a: even
the human labels are contaminated).

**The method transfers; the numbers do not.** Cite Ullah for the *operating-characteristic framing*,
the *composition-over-count finding*, and the *committee-size curve* — not for specific TPR/FPR values
as expected performance in an unoracled setting.

### 140e. B7 partial closed — prior ruling preserved

Third of the four §126e partials to be resolved. Its single existing tag,
`cal:human:facet:evaluated-synthetic`, is an adjudicated §34/§35 gold-set ruling (author-constructed
82-task corpus) and was **left untouched**; the theme layer and primary were added around it. The
§126e procedure worked as intended: check for a prior narrow-axis ruling before re-opening.
Remaining partials: `MFSZPSPU` Shi · `I6FZ5GD2` Wang (Junpeng).
