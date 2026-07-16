# Stage 3 — Relevance Triage, Cross-Model QA, and Core Confirmation

**Vibe Coding Governance Systematic Literature Review**
**Date:** 2026-07-06
**Scope:** Reduction of the 983-item eligible pool toward a two-tier extraction corpus. This document records the Stage-3 instrument, the AI screening run, the cross-model + human quality-assurance design and results, and the resulting human core-confirmation protocol. It is a methods-chapter source document; companion status in `screening_multimodel_results.md` and `SLR_CONTEXT.md` §13.

---

## 1. Purpose and position in the protocol

Pass 1 (recall) and Pass 2 (operationalizability) were abstract-level *inclusion* screens that produced the 983-item eligible pool (976 primaries + 7 flagged duplicates). Stage 3 is a **relevance triage**: it does not re-litigate inclusion but sorts the pool by *centrality to the core research question* to allocate downstream extraction effort under a two-tier design:

- **Core** → full-text fetch + full extraction.
- **Context** → retained, extracted at abstract level (no fetch).
- **Discard** → removed from the extraction corpus with a reason code.

Consistent with the standing methodology guardrail, **AI is a consistency-check tool, not a decision-maker**; every AI-assisted decision that reaches the corpus is subject to human confirmation.

## 2. Instrument

Each item receives one **bin** and a **0–100 centrality score** (centrality drives ranking; bins are score bands):

- **Core (70–100):** directly addresses scalable human oversight / governance of AI-generated code in an organizational or software-engineering pipeline context, *with* an operationalizable mechanism, measurement, framework, or empirical finding.
- **Context (30–69):** adjacent but methodologically strong and transferable (the volume/risk problem; human oversight / AI governance in a broader setting; automation-bias theory; non-code-specific regulatory frameworks) *with an evidence base or concrete framework* — not opinion.
- **Discard (0–29):** weak **and** off-core. Reason code (discard only), one of: `out-of-scope | wrong-level | wrong-type | too-old | quality-threshold-not-met`.

The full rubric text is version-controlled as the `RUBRIC` constant in `stage3_screen.py` and was applied verbatim to every model leg. Author metadata was withheld from all model prompts (author-blind) to avoid prestige bias.

## 3. AI screening run

- **Screener:** Claude **Opus 4.8** via the Claude Code CLI, batched (49 batches of ~20), with per-batch checkpointing, JSON-anchored extraction, and item-key hallucination validation (reject/retry if >5% invented or any missing).
- **Coverage:** 976 primaries; duplicates inherit their primary's verdict.
- **Result:** **197 core / 640 context / 139 discard** (primaries).

## 4. Cross-model QA design

Three independent screening legs on a shared sample, each applying the identical instrument:

| Leg | Model | Access | Tier rationale |
|---|---|---|---|
| Claude | Opus 4.8 | Claude Code CLI | primary screener (calibrated to human) |
| ChatGPT | GPT-5.5 @ reasoning=high | `codex exec`, ChatGPT login (no API key) | OpenAI top-reasoning tier |
| Gemini | Gemini 3.1 Pro (High) | `agy` CLI | Gemini Pro tier — **never Flash** (prior 98% key-hallucination) |

**Sample.** A **250-item stratified-random** sample of the 976 primaries (proportional to the Opus bin distribution; seed 20260706): 50 core / 164 context / 36 discard. The same 250 went to both external legs. A **50-item stratified subset** was drawn for **blinded human** review (10/33/7 by Opus bin; human never saw any model verdict). QA is on primaries only.

**Blinding.** Model input files carried no verdict and no author. The human sheet withheld model verdicts but showed authors (human adjudication is holistic). Opus verdicts were held in a separate scoring key.

**Reproducibility.** Scripts in `~/Code/SLR/slr-tools/stage3/`: `stage3_qa_sample.py` (draw), `stage3_qa_screen.py` (external legs), `stage3_qa_score.py` (agreement analysis). All seeded.

## 5. Results

### 5.1 Cross-model agreement (250)

| Pair | Cohen's κ (3-way bin) | Landis–Koch | Spearman ρ (centrality) |
|---|---|---|---|
| Opus vs GPT-5.5 | 0.509 | moderate | +0.693 |
| Opus vs Gemini 3.1 Pro | 0.491 | moderate | +0.686 |
| GPT-5.5 vs Gemini 3.1 Pro | 0.641 | substantial | +0.681 |

All three rank centrality nearly identically (ρ ≈ 0.68–0.69) but draw bin cut-points at different heights. Keep rates diverge: GPT-5.5 93%, Gemini 79%, Opus 86% (discard rates 7% / 21% / 14%).

### 5.2 Trust Check — Opus vs human (n = 50, blinded)

| Metric | Value |
|---|---|
| Exact agreement (Po) | 56% |
| Cohen's κ (unweighted, 3-way) | 0.183 (slight) |
| Linear-weighted κ | 0.244 |
| Quadratic-weighted κ | 0.333 |
| Within-one-bin agreement | 98% (1 core↔discard crossover) |
| **Binary keep/discard κ** | **0.297** (Po 78%) |

Confusion matrix (rows = Opus, cols = human):

| | core | context | discard |
|---|---|---|---|
| **core** | 3 | 6 | 1 |
| **context** | 5 | 21 | 7 |
| **discard** | 0 | 3 | 4 |

The binary keep/discard κ = 0.297 **reproduces the Pass-1 pilot's Claude/human κ = 0.273** — two independent rounds, different rubrics, the same conclusion: human↔LLM item-level agreement is "fair," below the κ = 0.4 IRR acceptability floor. This re-validates the standing decision that the LLM is a consistency-check tool and the human is the final arbiter, now confirmed for the Stage-3 instrument. The low *unweighted* κ is substantially a base-rate (kappa-paradox) artifact: context comprises ~60% of items, inflating chance agreement; 98% of items nonetheless agree within one bin.

### 5.3 Two decisive findings

**(a) Cross-model dissent does not predict human judgment.** Against the human standard, the external legs agree only at chance (binary keep/discard κ: GPT-5.5 0.041, Gemini 0.010; Opus 0.297). Of the 8 genuine Opus over-keeps (items Opus kept but the human discarded), the models caught **0**; of the 5 model-dissents on Opus-keeps, **all 5** were items the human kept. There is therefore **no model shortcut** for triaging which keeps require human review.

**(b) Opus over-calls "core."** Of 10 Opus-cores in the human sample, the human confirmed 3, demoted 6 to context, and discarded 1 — a **core precision of ~30%**. The error is overwhelmingly extraction-*depth* (core→context, still retained), not junk inclusion (only ~1 in 10 a true discard). The disagreement concentrates below centrality ~72 (items ≥75 held up; sub-75 cores demoted ~6/7). The edge is **two-sided**: the human also promoted 5 items Opus had placed in *context* (centrality 45–55) up to core — "hidden cores" — so reviewing only the core tier carries a recall risk.

## 6. Reliability sampling rationale

The 50-item human check is a **stratified Trust Check gate**, not the citable reliability statistic. Two points govern the sample size:

1. **Population size does not license a smaller reliability sample.** κ precision depends on the number of double-coded items and the number of categories, not the population size; the finite-population correction at N = 976 is negligible (~3% at n = 100). The n = 50 estimate is intentionally imprecise (unweighted κ 95% CI ≈ [−0.05, 0.42]) — adequate to reveal the direction and confusion structure for gating, inadequate to cite.
2. **The ordinal rubric argues for more items, not fewer,** for equal precision; projected κ CI half-widths are ≈ ±0.19 at n = 75, ±0.16 at n = 100, ±0.13 at n = 150.

Rather than expend high-effort coding on a large 3-way κ, the review reframes the reliability target: the *inclusion* decision that warrants an IRR statistic is **keep vs discard** (binary), for which the earlier passes and this Trust Check provide consistent "fair" estimates; **core vs context is an extraction-depth allocation**, resolved by direct human confirmation rather than a reliability coefficient. Reported statistics follow the standing rules: Po, κ (with Landis–Koch label and CI), weighted κ for the ordinal scale, per-category agreement, and the full confusion matrix.

## 7. Core-confirmation protocol (in progress)

Because Opus core precision is ~30%, no model can triage it, and core drives the expensive full-extraction tier, **every core is human-confirmed**, with a hidden-core recall check on the adjacent context band. Review is banded by centrality (the one reliable signal) and split into separate worksheets (`stage3_review_buckets.py` → `work/review/`):

| Bucket | Definition | n | Action |
|---|---|---|---|
| A | core, centrality ≥ 75 | 69 | skim / fast-confirm (top band held up in QA) |
| B | core, centrality 70–74 | 104 | scrutinize (demote-risk cliff) |
| C | core, centrality 60–69 | 24 | scrutinize (demote-risk; occasional discard) |
| D | context, centrality 55–69 | 111 | hidden-core hunt (promote-risk) |

Per row the reviewer sets `human_bin` ∈ {core, context, discard}. **Review precedes fetching:** PDFs are retrieved only for items confirmed `core`, avoiding fetches for items that demote to the abstract-level context tier. The confirm/demote/discard tallies across these buckets (n ≈ 308, unbiased by stratification) constitute the operative estimate of Opus core precision for the methods chapter.

## 8. Downstream

After confirmation: apply the human decisions over the Opus verdicts (propagating to duplicates), write the updated results and the fetch worklist (`human_bin = core & has_pdf = no`), then proceed to Stage 4 (full-text fetch + extraction of the confirmed core set; context tier extracted from abstracts). Any write of `s3:*` tags to Zotero follows the standing rule — library export backup first, write key swapped in only for the authorized write.

## 9. Artifacts

- Scripts: `stage3_build_input.py`, `stage3_screen.py`, `stage3_qa_sample.py`, `stage3_qa_screen.py`, `stage3_qa_score.py`, `stage3_core_confirm.py`, `stage3_review_buckets.py` (in `~/Code/SLR/slr-tools/stage3/`).
- Data: `work/stage3_results.csv` (triage), `work/qa/` (QA sample, three legs, human sheet, scores, `adjudicate.csv`), `work/review/` (the four confirmation buckets).
- Seeds: screening batches deterministic by input order; QA sample seed 20260706.
