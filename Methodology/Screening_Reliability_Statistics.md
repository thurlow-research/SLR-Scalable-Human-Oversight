# Screening Reliability — Keep Rates and Inter-Rater Agreement by Stage

**Vibe Coding Governance SLR · methods-chapter reference**
**Computed 2026-10-03** by `slr-tools/screening_reliability.py`, read directly from the
ground-truth decision files (§6). Every rate and κ below was recomputed from raw data. The two
exceptions (Stage-3 weighted κ and Spearman ρ) are cited from `Stage3_Relevance_Triage…` §5 and
marked as such. Where an earlier summary disagrees, §5 says which figure governs and why.

Companion to `PRISMA_Funnel.md` (corpus counts) and `Selection_Criteria_By_Phase.md` (criteria).
κ = Cohen's kappa, labelled by Landis & Koch bands (<0.20 slight · 0.21–0.40 fair · 0.41–0.60
moderate · 0.61–0.80 substantial). The review adopts **κ = 0.40** as its IRR acceptability floor.

---

## 0. Evaluation sample sets at a glance

Each reliability figure in this document comes from one of these sets. **Drawn** is the size of the
sample; **coded** is how many records actually carry a usable decision from that rater.
Blinded = human coded without seeing the model's decision (n/r = not recorded).

| # | Evaluation | Stage | Drawn from (population) | Selection | Drawn | Raters → records coded | Blinded? | Purpose |
|:-:|---|---|---|---|---:|---|:-:|---|
| **A** | **Pilot A/B check** | Pass 1 | SSRN corpus (3,863 unique) | not documented (pilot workbook only) | 100 human<br>~590 per external model | Claude **3,863** · ChatGPT **586** · Gemini **584** · Human **100**<br>all four on the same items: **100** · ChatGPT ∩ Gemini: **162** | n/r | Decide whether LLMs can co-screen → **no** |
| **B** | **Non-SSRN cross-model check** | Pass 1 | non-SSRN corpus (2,952) | human: source-by-source overrides; models: 600-row batch | 600 per external model | Claude **2,952** · Human **1,693** · ChatGPT **599** · Gemini **259** of 600 (rest hallucinated keys)<br>all four: **71** · Human ∩ ChatGPT: **391** · Human ∩ Gemini: **186** | ✗ | Production consistency check |
| **C** | **Trust Check** | Pass 2 | ~3,950 Pass-2 model decisions | stratified 20 keep / 20 maybe / 20 discard | 60 | Model **60** · Human **58** | ✗ | Go/no-go gate before applying decisions |
| **D** | **Blinded methodology validation** | Pass 2 | same | simple random, seed 42 | 100 | Model **100** · Human **0** — *never coded* | ✓ | The citable Pass-2 κ — **open** |
| **E** | **Stage-3 cross-model QA** | Phase 3 | 976 primaries (eligible pool) | stratified random, proportional to Opus bin (50 core / 164 context / 36 discard); seed 20260706 | 250 | Opus **250** · GPT-5.5 **250** · Gemini **250** | — | Inter-model agreement and bin rates |
| **F** | **Stage-3 human check** | Phase 3 | subset of E | stratified random subset of E (10 / 33 / 7) | 50 | Human **50** (all three models also on these 50) | ✓ | Model-vs-human agreement |
| **G** | **Core confirmation, query stream** | Phase 3 | Opus core + context ≥55 | census of 4 centrality bands:<br>A ≥75 (69) · B 70–74 (104) · C 60–69 core (24) · D 55–69 context (111) | 308 | Human **308** reviewed (301 carry `s3:human:*` tags) | ✗ | Confirm every core; hunt hidden cores |
| **H** | **Core confirmation, snowball stream** | Phase 3 | snowball triage ≥55 | census, after cross-stream dedupe | 120 | Human **120** | ✗ | Same, at exact parity (≥55 floor) |

**Totals.** **Human codes used for reliability statistics: 1,901** (A 100 + B 1,693 + C 58 + F 50). **Human confirmation
decisions: 428** (G 308 + H 120). Sets G and H are censuses, not samples. They produce the
final dispositions, not a κ, and they are the basis of the production core-precision figure in §4.3.

---

## 1. Summary

| Stage | Rater comparison | n | κ | Reading |
|---|---|---:|---:|---|
| Pass 1 pilot | Claude vs human | 100 | **0.273** | fair, below floor |
| Pass 1 pilot | ChatGPT vs human / Gemini vs human | 100 | 0.076 / 0.052 | slight |
| Pass 2 Trust Check | Sonnet→Opus pipeline vs human | 58 | **0.792** | substantial (gating only, unblinded) |
| Stage 3 QA | Opus vs human (binary keep/discard) | 50 | **0.297** | fair, below floor |
| Stage 3 QA | GPT-5.5 / Gemini vs human (binary) | 50 | 0.041 / 0.010 | chance |

**Keep rates show a stable rater ordering across every stage:** the human is the most conservative
rater, Claude/Opus sits close to the human, and ChatGPT/GPT-5.5 and Gemini keep roughly twice as
much.

| Stage (unit) | Human | Claude / Opus | ChatGPT / GPT-5.5 | Gemini |
|---|---:|---:|---:|---:|
| Pass 1 pilot — keep (n=100, all four raters) | **32%** | 32% | 68% | 59% |
| Pass 1 pilot — keep (each rater's full SSRN set) | 32% | 33% | **60%** | **66%** |
| Pass 1 pooled, SSRN + non-SSRN — keep | **20%**ᵃ | **30%** | 56% | 65% |
| Stage 3 — core (n=50 human sample) | 16% | 20% | 38% | 30% |
| Stage 3 — retained, core + context (n=50) | 76% | 86% | 94% | 84% |

ᵃ Source-confounded; see §2.3. The ~20% / ~30% / ~60% / ~66% pattern is the one usually quoted.
It is correct, but it combines the pooled human and Claude rates with the **pilot** ChatGPT and
Gemini rates. Cite each figure with its row.

**The methodological consequence, reproduced in two independent rounds with different rubrics:**
LLM-vs-human item-level agreement is *fair at best* (Claude 0.273 at Pass 1; Opus 0.297 at Stage 3),
below the 0.40 floor. The two permissive models agree with the human only at slight-to-chance
levels. LLMs were therefore downgraded from co-screener to **consistency-check tool**, with the
human as final arbiter at every inclusion boundary.

---

## 2. Pass 1 — recall screen (keep / maybe / discard)

### 2.1 Pilot cross-model A/B check (SSRN, pre-production)

Claude, ChatGPT, Gemini, and the human screened a shared SSRN sample before production.
**n = 100 items coded by all four raters.**

**Keep / maybe / discard rates on the common 100:**

| Rater | Keep | Maybe | Discard |
|---|---:|---:|---:|
| Human | 32.0% | 28.0% | 40.0% |
| Claude | 32.0% | 40.0% | 28.0% |
| ChatGPT | 68.0% | 23.0% | 9.0% |
| Gemini | 59.0% | 41.0% | 0.0% |

Each model's rates across everything it screened (larger, overlapping SSRN sets): Claude 33.4% /
44.0% / 22.5% (n = 3,863); ChatGPT 60.4% / 30.0% / 9.6% (n = 586); Gemini 65.9% / 29.8% / 4.3%
(n = 584). **Gemini discarded none of the 100 common items.**

**Pairwise κ (3-way keep/maybe/discard), with two binary collapses:**

| Pair | n | κ (3-way) | Po | κ pass vs discard | κ keep vs not | Band (3-way) |
|---|---:|---:|---:|---:|---:|---|
| ChatGPT / Gemini | 162 | 0.344 | 67% | 0.264 | 0.380 | fair |
| Claude / ChatGPT | 586 | 0.332 | 56% | 0.408 | 0.441 | fair |
| **Claude / Human** | **100** | **0.273** | 51% | 0.386 | 0.357 | **fair** |
| Claude / Gemini | 584 | 0.154 | 45% | 0.154 | 0.197 | slight |
| Human / ChatGPT | 100 | 0.076 | 37% | 0.115 | 0.186 | slight |
| Human / Gemini | 100 | 0.052 | 34% | 0.000 | 0.192 | slight |

**Decision.** Every human/LLM pair falls below κ = 0.40. The human is retained as final arbiter;
production Pass 1 was run by Claude (Sonnet 4.6) alone, with **human decisions overriding Claude
for collection placement** (union rule). ChatGPT and Gemini were not used in production.

### 2.2 Production run — non-SSRN cross-model check

The non-SSRN corpus (2,952 items) carries Claude decisions on all items, human decisions on
1,693, ChatGPT on 599, and Gemini on 259. The Gemini count is the usable remainder of a 600-row
batch, of which ~57% of returned item keys were hallucinated (`screening_multimodel_results.md`
§5); usable batches are non-random.

| Rater | n | Keep | Maybe | Discard |
|---|---:|---:|---:|---:|
| Claude | 2,952 | 24.9% | 25.3% | 49.7% |
| Human | 1,693 | 18.9% | 1.6% | 79.5% |
| ChatGPT | 599 | 51.9% | 21.5% | 26.5% |
| Gemini | 259 | 61.8% | 21.6% | 16.6% |

| Pair | n | κ (3-way) | Po | κ pass vs discard | κ keep vs not |
|---|---:|---:|---:|---:|---:|
| ChatGPT / Gemini | 80 | 0.587 | 74% | 0.701 | 0.653 |
| Claude / ChatGPT | 599 | 0.388 | 58% | 0.487 | 0.462 |
| Claude / Human | 1,693 | 0.371 | 67% | 0.407 | 0.566 |
| Claude / Gemini | 259 | 0.240 | 47% | 0.344 | 0.319 |
| Human / ChatGPT | 391 | 0.233 | 50% | 0.200 | 0.382 |
| Human / Gemini | 186 | 0.144 | 40% | 0.115 | 0.215 |

### 2.3 Caveat on the production human rate

The 1,693 non-SSRN human decisions are **not a random sample**. They were coded source by source
(IEEE 912, Scopus 403, ACM 185, Coursework 93; arXiv and WoS were barely coded) and skew toward
items Claude discarded (55% of human-coded items vs 42% of uncoded). The human "maybe" category is
also nearly unused (1.6%) because these were override decisions, not a fresh three-way screen.
The 18.9% (non-SSRN) and 19.6% (pooled) human keep rates are therefore **descriptive of the coded
set, not population estimates**. For a clean human-vs-model keep-rate contrast, cite the pilot
(§2.1), where all four raters coded the same 100 items.

**Pooled Pass 1 (SSRN + non-SSRN), for reference:** keep rate Claude 29.8% (n = 6,815), human
19.6% (n = 1,793), ChatGPT 56.1% (n = 1,185), Gemini 64.7% (n = 843). Pooled Claude/human κ =
0.374 (3-way), 0.552 (keep vs not).

---

## 3. Pass 2 — operationalizability screen

### 3.1 Trust Check (gating sample — not the citable reliability statistic)

Stratified 20 keep / 20 maybe / 20 discard from the Pass-2 model decisions; human coded 58 of 60,
**unblinded** (AI decision visible). Purpose: a fast go/no-go before applying ~3,950 decisions.

| Metric | Value |
|---|---|
| Observed agreement (Po) | 86.2% (50 / 58) |
| **Cohen's κ** | **0.792 — substantial** |
| Discard agreement | 20 / 20 = 100% (zero false negatives) |
| Keep agreement | 17 / 20 = 85% (2 → maybe, 1 → discard) |
| Maybe agreement | 13 / 18 = 72% (3 → discard, 2 → keep) |

Decision rule: ≤5% disagreement → apply; 5–15% → apply and document; ≥15% → stop. At 13.8%
the decisions were **applied, with documentation**.

**Why 0.79 is not comparable to the Pass-1 and Stage-3 κ:** the sample is stratified (it
over-represents maybes and under-represents discards relative to the population, shifting chance
agreement), and it is unblinded (anchoring inflates agreement). It is a gate, not an IRR estimate.

### 3.2 Blinded methodology validation (N = 100) — **NOT RUN**

The designed citable statistic (random N = 100, seed 42, AI decision withheld:
`phase2/verification/validation_blind.csv` + `validation_key.csv`) **was never coded**. All 100
`human_decision` cells are empty. The key file's AI distribution is 75 discard / 21 keep / 4 maybe.
**The methods chapter cannot cite a blinded Pass-2 κ.** Either run it (≈1 h of coding) or
report Pass 2 reliability as "gating check only" with the caveats in §3.1.

---

## 4. Stage 3 — relevance triage (core / context / discard)

A 250-item QA sample was triaged by Opus, GPT-5.5 (via codex), and Gemini 3.1 Pro on the same
rubric. The human coded a **blinded** 50-item subsample (seed 20260706).

### 4.1 Bin rates

| Rater | n | Core | Context | Discard | Retained (core + context) |
|---|---:|---:|---:|---:|---:|
| Opus | 250 | 20.0% (50) | 65.6% | 14.4% | 85.6% |
| GPT-5.5 | 250 | 34.8% (87) | 58.4% | 6.8% | 93.2% |
| Gemini | 250 | 28.8% (72) | 50.4% | 20.8% | 79.2% |
| *on the human-50 subset:* | | | | | |
| Human | 50 | **16.0%** (8) | 60.0% | 24.0% | 76.0% |
| Opus | 50 | 20.0% (10) | 66.0% | 14.0% | 86.0% |
| GPT-5.5 | 50 | 38.0% (19) | 56.0% | 6.0% | 94.0% |
| Gemini | 50 | 30.0% (15) | 54.0% | 16.0% | 84.0% |

Same ordering as Pass 1: human strictest, Opus nearest, GPT-5.5 the most generous on core. Gemini
is the most willing of the models to discard but still calls 30% core. All three models rank
centrality almost identically (Spearman ρ ≈ 0.68–0.69, `Stage3_Relevance_Triage…` §5.1). They
disagree on **where the cut-off falls**, not on order.

### 4.2 Pairwise agreement

| Pair | n | κ (3-way) | Po | κ keep vs discard | Po | κ core vs not |
|---|---:|---:|---:|---:|---:|---:|
| GPT-5.5 / Gemini | 250 | 0.641 | 79% | 0.403 | 85% | 0.752 |
| Opus / GPT-5.5 | 250 | 0.509 | 74% | 0.397 | 88% | 0.599 |
| Opus / Gemini | 250 | 0.491 | 70% | 0.425 | 83% | 0.614 |
| **Opus / Human** | 50 | **0.183** | 56% | **0.297** | 78% | 0.189 |
| GPT-5.5 / Human | 50 | −0.053 | 38% | 0.041 | 74% | 0.092 |
| Gemini / Human | 50 | −0.018 | 40% | 0.010 | 68% | 0.176 |

Opus vs human, weighted (cited from `Stage3_Relevance_Triage…` §5.2, not recomputed): linear-weighted κ = 0.244, quadratic = 0.333;
98% within one bin (1 core↔discard crossover). The low unweighted κ is partly a base-rate artifact
(context ≈ 60% of items inflates chance agreement).

**Two findings that set the review's protocol:**
1. **Models agree with each other far more than with the human** (inter-model κ 0.49–0.64 vs
   model–human ≤ 0.30). Agreement among models measures shared model bias, not correctness.
2. **Cross-model dissent does not predict human judgment.** Of 8 genuine Opus over-keeps (human
   discarded), the other models caught 0. Of 5 model dissents on Opus keeps, the human kept all 5.
   So model disagreement cannot triage which items need human review. **Every core was
   human-confirmed** (≥55 centrality floor; see `PRISMA_Funnel.md` §4.1).

### 4.3 Opus core precision at production scale

Against the full human ≥55 review (not the n=50 sample), final Core is 60% of Opus's core calls
in the query stream (191 → 114) and 57% in the snowball (58 → 33) (`PRISMA_Funnel.md` §4.1). The
n=50 estimate of ~30% (3 of 10) was a small-sample low; the production figure is the one to cite.

---

## 5. Reconciliation with earlier summaries

| Earlier figure | Where | Status |
|---|---|---|
| Pilot κ table (Claude/Human 0.273, Claude/ChatGPT 0.334, Claude/Gemini 0.154, Human/ChatGPT 0.077, Human/Gemini 0.052, ChatGPT/Gemini 0.358) | `screening_multimodel_results.md` §1 | **Reproduced** to ±0.001, except ChatGPT/Gemini (0.344 recomputed on n = 162). The original overlap set is not recoverable; use 0.344. |
| Pilot keep rates ChatGPT ~60%, Gemini ~66%, Human ~32% | same | **Reproduced** (60.4%, 65.9%, 32.0%) |
| "Human ~22%, Claude ~28%" | assistant memory note | ≈ pooled Pass-1 rates (19.6%, 29.8%). Human figure is source-confounded (§2.3). |
| Trust Check κ 0.79, Po 86.2% | `SLR_CONTEXT.md`, results §4 | **Reproduced** (0.792) |
| Stage 3 Opus/human binary κ 0.297, GPT-5.5 0.041, Gemini 0.010 | `Stage3_Relevance_Triage…` §5.2–5.3 | **Reproduced** |
| Stage 3 retained rates 86% / 93% / 79% | `Stage3_Relevance_Triage…` §5.1 | **Reproduced** |
| Inter-model κ 0.51 / 0.49 / 0.64 | memory note | **Reproduced** (0.509 / 0.491 / 0.641) |

**One data correction applied:** one human cell in `ssrn-decisions.xlsx` reads `dsicard`, normalised to
`discard`. It makes the pilot n = 100, and it is what reproduces the recorded 0.273 (excluding it gives
0.280 on n = 99). The SSRN decisions sheet also has 6 duplicated item keys (3,869 rows → 3,863
unique items); rates are computed on unique items.

---

## 6. Data sources

| Stage | File | Raters |
|---|---|---|
| Pass 1 pilot (SSRN) | `slr-phase-1-2/ssrn-decisions.xlsx` (sheets `decisions`, `chatgpt`, `gemini`; the xlsx is mandatory because the CSV export drops the human column) | Claude, human, ChatGPT, Gemini |
| Pass 1 non-SSRN | `slr-phase-1-2/nonssrn-decisions-2026-05-25.csv` | Claude, human, ChatGPT, Gemini |
| Pass 2 Trust Check | `slr-phase-1-2/phase2/verification/trust_check.csv` | Sonnet→Opus, human |
| Pass 2 blinded validation | `slr-phase-1-2/phase2/verification/validation_{blind,key}.csv` | **uncoded** |
| Stage 3 QA | `slr-tools/stage3/work/qa/{qa_master_250,codex_out_250,gemini_out_250,human_review_50}.csv` | Opus, GPT-5.5, Gemini, human |

Rerun: `slr-tools/stage6/.venv/bin/python slr-tools/screening_reliability.py` (needs `openpyxl`).
