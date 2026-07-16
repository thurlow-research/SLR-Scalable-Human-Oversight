# Codebook v0 — Vibe Coding Governance SLR (Stage 4)

**Status:** DRAFT for human review — **not locked.**
**Derivation:** emergent-first, bottom-up from structured signal extraction over
the full text of all **114 Core documents** (`core_theme_signals.csv`,
instrument = `stage4_extract_rubric.md`). Themes were clustered from the
open-vocabulary `mechanism_keywords`, `risk_types`, and `key_constructs` fields,
then reconciled against the a-priori two-part scope. **AI extraction is a
consistency aid; the human is the arbiter of this codebook.**

**How to read the counts:** counts are **non-exclusive** — a document is coded on
as many themes as it touches (median doc carries several). They indicate salience,
not partition. Exemplars are the first few matching papers, not an exhaustive list.

**Corpus shape (from `scope_fit`):** 90 documents serve *both* scope halves, 22
are solution-only, 2 problem-only. In practice the **Problem** axis is usually the
motivating setup and the **Solution** axis the contribution — so most papers code
on both. Extraction is therefore **multi-label across both axes**.

---

## Axis A — PROBLEM (quantify the problem, incl. its insufficiency)

### P1 · Scale & penetration of AI-generated code  *(94/114 carry quantified magnitude)*
The volume driver: how much code is AI-generated and how fast, establishing the
oversight-throughput gap.
- **Include:** any quantified prevalence/volume/adoption claim (e.g. "20–30% of
  enterprise code AI-generated", "95% of devs use GenAI", LOC migrated, % teams).
- **Exclude:** generic "AI is growing" with no figure → not P1 (may still motivate).
- **Exemplars:** N. Watson 2025 (20–30% enterprise code; 95% adoption), Bhatnagar
  2026 (~85k LOC migration), Choudhuri 2026 (860-dev survey), Chang 2025 (25% of
  teams 95% AI-generated).

### P2 · Security & supply-chain vulnerability  *(~79)*
Security defects introduced by AI-generated code and the software supply chain.
- **Include:** insecure-code rates, CWE/CVE classes, prompt-injection, malicious
  dependencies, backdoors, secret leakage, SBOM/supply-chain exposure.
- **Exclude:** security *mechanisms* → those are Solution (S3/S5).
- **Exemplars:** Kudriavtseva 2025 (Copilot insecure ~40%), Ji 2024, VibeGuard/Xie
  2026, Enyedi 2026 (SolarWinds/XZ supply-chain).

### P3 · Functional quality, correctness & reliability  *(~77)*
Whether AI code is correct and dependable.
- **Include:** pass/correctness rates, defect density, reliability, functional bugs.
- **Exclude:** maintainability/debt (→ P4).
- **Exemplars:** X. Yu 2024 (57% correct), Ghammam 2026, Ferdous 2026 (breaking changes).

### P4 · Maintainability & technical debt  *(~52)*
Longer-horizon code-health costs.
- **Include:** technical debt, complexity, readability, churn, reuse decay.
- **Exemplars:** Borg 2026 (code-health/AI-friendliness), Huang 2026 (more code less reuse).

### P5 · Hallucination, specification-gaming & reward-hacking  *(~54)*
The model produces plausible-but-wrong artifacts, incl. gaming its own evaluation.
- **Include:** hallucinated APIs, spec-gaming, reward-hacking, self-validating tests,
  overconfident wrong output.
- **Exemplars:** Alami 2026 (cognitive camouflage), Jin & Chen 2025 (spec-verification
  failures), Li 2025 (CoTDeceptor).

### P6 · Human-factor risks: over-reliance, automation bias, deskilling  *(~46)*
Failure modes of the *human* in the loop.
- **Include:** automation bias, over-reliance/overtrust, alert fatigue, complacency,
  skill erosion / deskilling.
- **Exemplars:** Catalan 2026 (cognitive engagement), Langer 2024 (signal-detection),
  A. Mahmud 2025 (alert fatigue / "fix later").

### P7 · Legal, IP, privacy & regulatory-compliance risk  *(~48)*
Non-technical liability surface.
- **Include:** licensing/IP, copyright, privacy/GDPR/HIPAA, regulatory non-compliance.
- **Exemplars:** Goodhue 2025 (legal minefield), L. Vanam 2025 (ethical/regulatory risk).

### P8 · Bias, fairness & ethics  *(~41)*
- **Include:** bias/discrimination in generated code or outcomes, fairness, inclusivity.
- **Exemplars:** Bilal Naqvi 2026 (security & inclusivity), Kudriavtseva 2025.

### P9 · Accountability & auditability gaps  *(~21)*
Who is answerable, and can it be reconstructed.
- **Include:** unclear responsibility, un-auditable AI actions, "scapegoat" dynamics.
- **Exemplars:** Jessee 2026 (scapegoat-as-a-service), M. Tuape 2025 (architecting trust).
- **Boundary note:** the *problem* of missing accountability (P9) vs the *mechanism*
  of provenance/audit (S7) — code the deficit as P9, the tooling as S7.

### ⟂ Insufficiency layer — *required coded dimension, present in all 114*
Every core carries evidence that current oversight (automated **or** human) fails
to close the gap. Coded as a facet with a **mode** (see F5), not as its own theme.

---

## Axis B — SOLUTION (characterize the oversight mechanisms/designs)

### S1 · Human oversight roles & escalation  *(~84)*
The human's position in the loop and when they are engaged.
- **Include:** HITL / on-the-loop / human-in-command designs, escalation paths,
  review responsibilities, when a human must (re-)enter the loop.
- **Exclude:** *routing logic* that decides escalation → S2.
- **Exemplars:** Eze 2026 (HITL isn't a checkbox), Jessee 2026 (human-in-command),
  Liming Zhu 2025 (meaningful oversight).

### S2 · Risk-based routing, triage & attention calibration  *(~54)*
Directing scarce human attention by risk/signal — the "keep pace with volume" lever.
- **Include:** risk scoring, triage/routing, severity thresholds, trust calibration,
  SNR-based prioritization of what humans review.
- **Exemplars:** A. Mahmud 2025 (trust-calibrated multi-stage pipeline), Kumar 2026,
  Parris 2026 (AIRA risk audit).

### S3 · Guardrails & policy-as-code enforcement gates  *(~79)*
Automated policy enforcement in the action/publish path.
- **Include:** guardrails, policy-as-code / OPA, quality/security gates, hard-block
  rules, runtime enforcement, constitutional constraints, defense-in-depth.
- **Exemplars:** Jackson 2025 (policy engine), VibeGuard/Xie 2026 (security gate),
  Kumar 2026 (guardrails), Lipsanen 2026 (Shift-up guardrails), Ma 2026 (ZORO active rules).

### S4 · Automated verification: LLM-as-judge, ensembles & adversarial review  *(~49)*
Machines checking machine output, esp. decorrelated/adversarial designs.
- **Include:** LLM-as-judge, juries/committees, ensemble/voting, n-version,
  adversarial/counter-test execution, decorrelated reviewers, cross-model checks.
- **Exemplars:** Ullah 2026 (unanimous LLM jury), Alami 2026 (adversarial execution),
  LLM4VV/Sollenberger 2025, He 2026 (LLM-as-judge for SE).

### S5 · Static analysis, testing & security scanning  *(~60)*
Deterministic and test-based checks (incl. AI-augmented code review).
- **Include:** SAST/DAST, linters, test generation, fuzzing, secret/dependency
  scanning, AI-augmented code-review pipelines.
- **Boundary note:** overlaps S3 (a scan wired as a blocking gate is S3+S5) and S4
  (LLM-driven review is S4+S5). Code both when both apply.
- **Exemplars:** Naulty 2025 (Bugdar), Michel Hjazeen 2026 (unified security testing),
  Dutta 2025 (GenAI code review).

### S6 · Spec-driven & constrained generation  *(~54)*
Preventing defects up front by constraining what gets generated.
- **Include:** spec-driven / constitutional development, design-by-contract,
  requirements grounding, prompt engineering, constrained decoding, RAG grounding.
- **Exemplars:** Marri 2026 (constitutional spec-driven), Zietsman 2026 (spec as
  quality gate), Enyedi 2026 (human-certified modules).

### S7 · Provenance, traceability, audit trail & accountability  *(~68)*
Recording what was AI-generated and reconstructing decisions.
- **Include:** provenance/attribution metadata, SBOM, audit trails, traceability,
  watermarking, accountability infrastructure.
- **Exemplars:** Enyedi 2026 (human-certified repos), N. Watson 2025, Bhatnagar 2026.

### S8 · Observability, explainability & transparency  *(~53)*
Making AI behavior visible/understandable to the overseer.
- **Include:** monitoring/observability, dashboards, explainability/XAI,
  transparency reporting.
- **Exemplars:** Kumar 2026, Wang 2026, Otten 2026.

> **S9 (Multi-agent orchestration) — RETIRED as a strategy, moved to architecture
> facet F7 (2026-07-10).** Multi-agent is the *substrate* a strategy runs on, not a
> strategy itself (adversarial verification can be multi-agent or single-harness;
> multi-agent can serve adversarial review or plain labor division). It is now an
> `architecture` value, so e.g. Alami 2026 = `S4` strategy + `multi-agent` architecture.

> **S9 (Model-side interventions) — RETIRED 2026-07-10.** Out of scope: it isn't
> human oversight (it's automated generator improvement), and average orgs consume
> models rather than train them — the "make the agent self-conform" angle already
> routed out of core at Stage 3 (see [[slr-scope-refinement]]).
>
> **Re-code rule:** training an *oversight* model (LLM-judge / risk-classifier /
> reviewer) → code as **S4** (verification) or **S3** (guardrail/gate), since the
> oversight is still the mechanism. Training the *generator* → **not** a solution
> code; if it is a paper's sole contribution, set a **scope-boundary flag** for
> review (possible Context demotion) rather than a separate re-examination pass.

*Solution taxonomy is now **S1–S8** — every code is something a practitioner/org
actually does, which is what the organizational survey will ask about.*

---

## Cross-cutting facets (coded on every document, alongside themes)

- **F1 · Oversight locus (lifecycle stage):** code-review (97) · generation-time (89)
  · pre-commit (58) · CI (57) · pre-publish/pre-deploy (36) · runtime (24) ·
  post-deployment (25). *The "where" axis — multi-value.*
- **F2 · Human-role gradient:** in-the-loop (54) · on-the-loop (23) · in-command (14)
  · escalation-target (7) · none/automated (14). *Directly answers the RQ's
  "how do humans stay in the loop as volume scales."*
- **F3 · Evidence type:** empirical (72) · framework-model (56) · system-tool (47) ·
  conceptual-position (44) · case-study (40) · benchmark (25) · controlled-experiment
  (21) · secondary-review (14). *Governs synthesis weighting.*
- **F4 · Governance/regulatory anchoring:** 55/114 cite ≥1 framework — EU AI Act (18),
  GDPR (13), NIST AI RMF (10), ISO/IEC 42001 (6), OWASP, CWE, SBOM. *Supports the
  "governance/policy landscape" RQ sub-question.*
- **F5 · Insufficiency mode** *(present on all 114 — pick the dominant):*
  automated-tool-miss · human-review-doesn't-scale · LLM-judge-fooled ·
  false-positive/alert-fatigue · no-oversight-applied.
- **F6 · Research method / design** — *LOCKED 2026-07-10.* Full-multi-label,
  derived full-text (not abstract), `method:` prefix (matches tag grammar).
  Plus two booleans: `empirical`, `human_subjects`. 14 tags:
  - `method:conceptual` — conceptual / position / framework (no empirical eval)
  - `method:design-science` — design-science / prototype / tool-build
  - `method:benchmark` — benchmark-evaluation
  - `method:case-study` — case study (single/multi, in situ)
  - `method:qualitative` — qualitative analysis (thematic, grounded-theory, LLM-assisted coding)
  - `method:experiment` — controlled experiment (incl. ablation)
  - `method:mining` — repository-mining/MSR + measurement study (observational archival)
  - `method:dataset` — dataset/resource contribution
  - `method:survey` — survey / questionnaire
  - `method:interview` — interviews
  - `method:user-study` — user study
  - `method:review` — secondary study (SLR / mapping / multivocal)
  - `method:formal` — formal analysis / proof
  - `method:simulation` — simulation
  *Early signal (74/114): artifact/benchmark-heavy; human-subjects thin (~19%) —
  supports the practitioner-survey gap the dissertation fills.*
- **F7 · Solution architecture** — *added 2026-07-10, absorbs former S9.* The
  computational structure a mechanism runs on (multi-label): `single-model` ·
  `multi-agent` · `staged-pipeline` · `deterministic/tooling`. Orthogonal to the
  S-strategy: e.g. adversarial verification (S4) × `multi-agent` (Alami 2026), or
  S4 × `deterministic/tooling` (a single counter-test harness). Lets co-occurrence
  recover strategy×architecture relationships without per-paper graph coding.

---

## Decisions needed before locking (v0 → v1)

1. **Theme granularity.** Keep S5 separate, or fold static-analysis/testing into S3
   (gates) + S4 (verification)? Same question for P9 (accountability) vs S7 provenance.
2. **P1 status.** Treat "scale/penetration" as a coded theme, or as the review's
   framing premise captured only via the magnitude facet?
3. **S10 relevance.** Model-side interventions are the "make the agent self-conform"
   angle the scope memo routed *out of core* — confirm S10 stays a minor/optional code
   rather than a first-class theme.
4. **Insufficiency as facet vs theme.** Proposed as facet F5 (it's universal). Confirm.
5. **Two-axis multi-label** is assumed. Confirm a doc is coded on all applicable P and
   S themes rather than assigned one primary theme.
6. **Merge/rename** any labels, and set the minimum evidence bar for coding a theme
   "present" (a passing mention vs a substantive treatment).

*Next step after your edits: lock v1, then run the Task-C classification pass
(Opus first pass → human verify → cross-model QA sample → weighted-κ), reusing
`core_theme_signals.csv` as the first-pass evidence layer.*
