# Stage 4 QA Methodology — Statistical Quality Control & Jidoka

**Vibe Coding Governance SLR · Stage 4 (extraction / coding) quality assurance**
**Date:** 2026-07-10 · Methods-chapter input

---

## 1. Rationale — quality management for a coding process at scale

Stage-4 coding produces a large, structured dataset: 114 core documents ×
~20 paper-level fields + 0–N mechanism-instance rows, coded on the locked
codebook. Exhaustive, uniform human verification of every datum is neither
efficient nor *reliable* — sustained manual inspection degrades (inspector
fatigue; "the human brain gets numb"), so uniform re-reading spends the coder's
scarcest resource, attention, exactly where it is least effective at catching
defects. We therefore treat coding as a **production process whose output quality
is engineered and monitored**, and adopt two complementary quality-management
principles from the Toyota Production System / statistical process-control
tradition: **Statistical Quality Control (SQC)** and **Jidoka**.

**Reflexivity (worth stating explicitly).** This review studies *human oversight
of AI-generated output that scales beyond human review capacity*. Its own QA
method faces the same problem — *human oversight of AI-generated codings that
scale beyond exhaustive human review* — and resolves it with the same mechanisms
the corpus catalogs (decorrelated / ensemble verification, risk-based routing of
human attention, escalation of exceptions). The method instantiates the
phenomenon it examines; this is a deliberate, documented design choice, not a
coincidence.

The **standing guardrail is preserved throughout: AI is a consistency-check tool;
the human is the arbiter.** Both principles below are designed to *focus* human
judgment, never to replace it.

---

## 2. Statistical Quality Control (SQC)

Quality is inferred from statistically-characterized samples and monitored
process signals rather than 100% inspection.

- **Sampling-based verification.** A representative calibration sample (~20
  documents, stratified across `scope_fit`, method type, and document length) is
  fully human-verified; a blinded reliability sample supports the citable
  agreement statistic.
- **Agreement statistics as the quality metric.** Inter-model and human–model
  agreement are quantified with **weighted κ (+ CI)** on the ordinal / categorical
  codes; κ precision depends on sample size, not population (FPC negligible at
  N ≈ 114).
- **Process-control signals.** Cross-model disagreement rate functions as a
  per-item, per-field **defect indicator** that routes inspection effort. A
  document's aggregate QA-score (deterministic-rule violations + cross-model
  disagreements + audit flags) is its position relative to a control threshold.
- **Control-mechanism validation (calibration before reliance).** Before the
  automated signals are trusted at scale, they are validated on the calibration
  sample: *do the flags predict the cells the human corrected?* Only a control
  mechanism shown to capture human-identified defects is relied upon for the
  unverified remainder. This inherits the Stage-3 caution that model dissent did
  not predict human *relevance* judgments (κ ≈ 0.01–0.04); extraction is a more
  grounded task, but the assumption is tested, not presumed.

## 3. Jidoka (autonomation — "automation with a human touch")

Machines are given the ability to **detect abnormal conditions, stop, and surface
the defect to a human**, so defects do not propagate and humans supervise **by
exception** rather than by watching every unit.

- **Automated defect detection (the *andon*).** The layered agentic QA stack is
  the line's abnormality detector: it raises a flag when a coded datum is
  internally contradictory, unsupported by the text, disputed across models, or
  apparently incomplete.
- **Stop-the-line.** A flagged discrepancy is surfaced for human adjudication
  *before* the datum is accepted into the final dataset.
- **Supervision by exception.** Human attention is spent on flagged exceptions and
  a light scan of the confident remainder — the direct countermeasure to
  inspector fatigue.
- **Separation of human and machine work.** The machine *detects*; the human
  *judges*. The coder is never removed from the decision — precisely Jidoka's
  "automation with a human touch," not full automation.

---

## 4. The QA stack mapped to the principles

| Layer | Detects | Principle |
|---|---|---|
| **0 · Deterministic checks** | vocab drift; internal contradictions | Jidoka andon (mistake-proofing / *poka-yoke*) |
| **1 · Cross-model re-extraction** (Opus + codex + Gemini) | miscoding / disagreement | SQC process-control signal |
| **2 · Adversarial grounding audit** (decorrelated model) | unsupported / hallucinated codes | Jidoka stop-the-line |
| **3 · Completeness / recall audit** (decorrelated model) | *missed* codes (false negatives) | Jidoka — catches what a fatigued inspector cannot |
| **Aggregate QA-score + routing** | prioritizes human effort | SQC control threshold → supervision by exception |
| **Calibration on ~20** | validates flags predict corrections | SQC control-mechanism validation |

**Decorrelation principle:** audit layers run on models *other than* the primary
(Opus) extractor, so verification does not inherit the extractor's blind spots —
the ensemble/decorrelation logic the corpus itself documents (code S4).

---

## 5. Reporting

- **Reliability:** weighted κ (+ CI) for the human–model and cross-model agreement
  on the reliability sample; report the instrument as ordinal/categorical.
- **Control-mechanism validity:** the share of human-identified corrections that
  the automated QA-score flagged (defect-detection recall), established on the
  calibration sample and reported as the basis for exception-based review.
- **Sequence:** calibrate the full stack on the representative ~20 first (tune the
  instrument *and* validate the triage), then scale to the full 114 — a
  calibrate-before-scale discipline consistent with Stage 3.
