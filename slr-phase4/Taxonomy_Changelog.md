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
