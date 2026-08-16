# GRAD 503 Summary — Applying Quality-Engineering Methods to a Systematic Literature Review

**Purpose of this file.** This is a source document, written for another AI session to read and
summarize/reflect on for a Purdue GRAD 503 course assignment. The course used this SLR project
as a real-world case. It compresses ~4 months (2026-04 through 2026-08-16) of a dissertation-track
systematic literature review (SLR) into the learnings and statistics most relevant to a course
audience, without assuming prior context. Source documents live in `Methodology/` and
`Knowledge Xfer/SLR_CONTEXT.md` in this repo if deeper verification is needed.

---

## 1. The project in one paragraph

Scott Thurlow, an Engineering Management PhD candidate at Purdue (practitioner at Microsoft), is
running a systematic literature review on how organizations practice **human oversight of
AI-generated code** ("vibe coding") — the core tension being that AI raises code *production*
volume faster than human review *capacity* can grow, while evidence suggests AI-generated code is
riskier per unit yet less inspected in practice. The SLR is a standalone deliverable (targeting
venues like ICSE SEIP/EASE/HICSS) that also seeds the dissertation's literature review. What makes
it relevant to a course on quality/process methods: the review's *own execution pipeline* — search,
screening, triage, thematic tagging — was deliberately engineered as an application of classical
quality-control theory to an AI-assisted research workflow, and that engineering choice became a
teachable case in itself.

---

## 2. Key learnings

### 2.1 Two industrial quality-control theories, ported to literature review
The pipeline design explicitly borrows two frameworks rather than inventing an ad hoc process:
- **Cleanroom statistical quality control** (Cobb & Mills, 1990) — statistical sampling over
  exhaustive inspection. Applied as: validate AI screening/tagging decisions via *stratified
  samples* (Trust Checks, blinded Cohen's κ runs) rather than a human re-checking every item.
- **Lean manufacturing's *jidoka*** (Ohno) — automated detection that stops the line and escalates
  to a human only when a defect is detected, rather than a human inspecting every unit.
  Operationalized as a **triage ladder**: machine consensus → auto-accept (with a small audit
  sample) → disagreement → automated replication → still-unresolved → human escalation.

The synthesis — "AI-triggered human oversight" — routes scarce human attention by *risk*, not by
volume. This is the same construct the dissertation studies in industry, applied reflexively to
the research process that studies it (see §2.5).

### 2.2 Multi-model panels need calibration, not just aggregation
A three-vendor LLM panel (Claude Opus, GPT-5.6/Codex, Gemini 3.1 Pro) was used for screening and
thematic tagging, but **model consensus alone was empirically shown not to substitute for human
judgment**:
- Cross-model *dissent* did not predict human disagreement — inter-model Cohen's κ against human
  ground truth landed at **chance level (κ≈0.30, "Trust Check")** in one QA round.
- One model (Opus) was calibrated close to human judgment on strict "keep" decisions; the other
  two systematically over-kept, and their disagreement pattern was uninformative about which
  papers actually needed human eyes.
- **Design consequence:** every "core" corpus item is human-confirmed regardless of model
  agreement. Multi-model panels were used to *cut where humans look*, never to *replace* the
  human decision.

### 2.3 Instability is a property of the task, not of one vendor
A run-to-run replication study (same paper, same model, re-run k=3) found LLM output instability
at roughly **uniform rates across all three models (~17–18 "tripwires" per model out of 128
papers)** — contradicting an earlier assumption from calibration-scale testing that one specific
model ("Opus") was uniquely flicker-prone. The lesson generalized: at production scale, replication
— not model choice — is what "carries the signal" about which decisions are unstable and need a
human look. This is a direct empirical instance of a broader quality-engineering principle:
*characterize variation rather than assume it away*, especially when the tool being measured (an
LLM CLI) exposes no temperature/seed control to eliminate it directly.

### 2.4 Computed signals over self-report
A recurring design rule across the whole project: **never gate decisions on a model's stated
confidence** (self-report is "saturated and uninformative" — an LLM will claim high confidence
even when wrong). Instead, gate on *computed, producer-independent* signals — e.g., whether three
independent model runs actually agree, whether a tag set exceeds a sprawl threshold, whether a
replicated run flips its answer. This mirrors a classical quality-control distrust of
self-certification in favor of externally measured conformance, and became a named design
principle reused across both the SLR tagging pipeline and a separate AI-code-review pipeline
(HOS) built as a parallel learning vehicle for the same dissertation.

### 2.5 The process is reflexive — a live example, not a metaphor
The review's method chapter explicitly frames the *pipeline itself* as an instance of its own
research question: AI does volume work (screening thousands of abstracts, tagging hundreds of
papers); humans hold every judgment gate (blind-first co-tagging, binding arbiter rulings on
ambiguous cases, a public change log of every definitional decision); quality signals are computed
rather than self-reported; escalation is risk-tiered. Even the software-engineering side of the
project adopted the same principle: AI-authored code changes to the project repository are
required to land via pull request with human review before merge — never pushed directly. The
project treats this as *methodological alignment*, explicitly not as proof of the underlying
oversight thesis (correct academic caution: the pipeline working well doesn't validate the
dissertation's claims about industry, it just demonstrates the mechanism is viable).

### 2.6 Negative results were tracked deliberately, not discarded
The calibration process documented what *didn't* help, as a matter of research hygiene:
persona-based prompting for the tagging model was tried and **rejected** (it caused interest bias
drift); splitting the "theme" and "facet" tagging prompts into two calls was tried and
**declined**; document length was tested as a possible confound on tagging accuracy and found to
have **no effect** (r≈0.0 at the calibration sample size). Recording negative results prevented
re-litigating the same ideas later and is itself a small but genuine research-methods lesson: a
project log that only records what worked silently invites the same failed idea to resurface.

### 2.7 Where automation earned trust, and where it didn't
Two failure modes shaped which parts of the pipeline stayed fully automated versus human-gated:
- A **data-integrity incident**: an apply script pointed at the wrong bucket and corrupted ~38% of
  an earlier screening pass. It was fully recoverable because every decision was logged to a
  reconstructable ground-truth file — the lesson generalized into a standing rule that pipeline
  state changes must always be re-derivable from an audit trail, not just applied and trusted.
- A **coverage-decision pivot**: a calibration query against one commercial database (ABI/Inform)
  returned 3 hits versus 110 for the same query on a second database (Scopus) — a ~37× gap used as
  quantitative justification to drop a paid source rather than assume it added coverage.

---

## 3. Key statistics (verified as of 2026-08-16; see `Methodology/SLR_Paper_Outline_v0_2026-08.md` for full provenance)

**Corpus funnel (PRISMA-style):**
| Stage | Count |
|---|---|
| Phase 1 (recall-favoring title/abstract screen) | 4,061 Keep+Maybe |
| Phase 2 (tightened operationalizability screen) | 973 Keep / 73 Maybe / 2,908 Discard |
| Eligible pool after Phase 2 | 983 |
| Backward citation ("snowball") references imported | 2,787 |
| Final **Core** tier (full extraction + thematic tagging) | 148 |
| Final **Context** tier (background/transferable, lighter treatment) | ~890 |

**Screening validation:**
- Trust Check (60-item stratified, unblinded): 86.2% observed agreement, **Cohen's κ = 0.79**
  ("substantial" agreement) → screening decisions applied.
- Cross-model dissent vs. human ground truth: **κ≈0.30** (chance-level) — the finding that killed
  the idea of using model disagreement as a proxy for "needs human review."

**Thematic-tagging production sweep (2026-08-15/16), 128 non-calibration core papers, 3-model panel:**
- Round 1: 128 papers × 3 models = 384 model runs, **100% valid outputs**.
- Contested rate: **37%** (47 of 128 papers), *below* the 43% rate projected from calibration data.
- Replication stage (contested papers only): 47 papers × 3 models × 2 extra runs = 282 runs.
- **Replication resolved 41 of 47 contested papers (87%) without any human involvement.**
- Final machine disposition: **ACCEPT 44 · LIGHT-REVIEW 78 (18 unanimous auto-demotions within
  that bucket) · HUMAN 6** (i.e., only 6 of 128 papers needed a full human deep-read).
- Realized human workload: 6 deep reads + 78 light confirmations + 4 audit spot-checks — well
  under a pre-sweep estimate of 20–25 deep reads + ~45 confirmations.
- Per-model instability rate at production scale: codex 18/128, gemini 18/128, opus 17/128
  (roughly uniform across vendors).

**Instrument (tagging taxonomy) calibration, n=20 gold-labeled papers:**
- Panel primary-theme accuracy vs. human gold: Opus 17/20, Gemini 14/20, Codex 13/20.
- Facet-agreement (Jaccard similarity) roughly doubled after a taxonomy-definition freeze:
  ~0.34–0.42 → ~0.61–0.70.
- 32 versioned, binding definitional rulings recorded in a public change log over the course of
  calibration (taxonomy reached v2.13, 17 themes × 27 facets).

**Search-stage decision:** a calibration query returned 3 hits in one commercial database (ABI/Inform)
vs. 110 in another (Scopus) for the same query — a ~37× coverage gap — used to justify dropping
the thinner source rather than guessing at its value.

---

## 4. Suggested angle for a GRAD 503 reflection

If the assignment calls for connecting coursework concepts to a real project, the strongest
throughlines here are: (1) statistical sampling/inspection theory (Cleanroom SQC) applied outside
manufacturing, to a knowledge-work pipeline; (2) *jidoka*-style automated stop/escalate logic as a
general pattern for allocating scarce expert attention under increasing throughput, independent of
the AI angle; (3) the empirical demonstration that "more automated agreement" is not the same
signal as "correctness," which is a quality-engineering point as much as an AI one — an aggregate
metric (inter-rater agreement) can be exactly the wrong proxy for the outcome you actually care
about (agreement with ground truth), and a project should test that link rather than assume it.
