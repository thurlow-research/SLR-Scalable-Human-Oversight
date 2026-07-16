# Multi-Model Screening Results — Summary for Claude Code

Compiled 2026-07-06 from prior Claude.ai project sessions. This is a status/handoff doc, not the methods-chapter prose (see companion .docx for that).

## 1. Pass 1 — Pilot Cross-Model A/B Check (pre-production)

Early quality check: Claude, ChatGPT, Gemini, and human decisions compared on a shared subset.

| Pair | Cohen's κ | Landis & Koch band |
|---|---|---|
| ChatGPT / Gemini | 0.358 | Fair |
| Claude / ChatGPT | 0.334 | Fair |
| Claude / Human | 0.273 | Fair |
| Claude / Gemini | 0.154 | Slight |
| Human / ChatGPT | 0.077 | Slight |
| Human / Gemini | 0.052 | Slight |

Keep rates: ChatGPT ~60%, Gemini ~66%, Claude intermediate, **Human ~32%** (most conservative rater).

**Decision:** All human/LLM pairs fell below κ=0.4 (SLR IRR acceptability floor). Human judgment retained as final arbiter; LLMs downgraded from co-screener to consistency-check tool. Production Pass 1 screening run solo by Claude.

Source file referenced in that session: `decisions.xlsx` (cols: item_key, title, decision [claude], human_decision, chatgpt_decision, gemini_decision).

## 2. Pass 1 — Production Screening Run

- Screener: **Claude Sonnet 4.6** via Claude Code CLI (Max subscription), 30s rate limit.
- SSRN corpus: 3,864 items screened. (Earlier partial Opus 4.7 run on ~325 items archived for consistency — not merged into final counts.)
- Non-SSRN corpus: ~2,952 items screened.
- Ground truth restore: `applied=2890`, `apply_errors=0`, `fetch_failed=79` (benign SSRN merge-orphan 404s), `skipped_superseded=30`.
- Union rule: **human decision overrides Claude** for collection placement.
- Ground-truth files: `nonssrn-decisions-2026-05-25.csv` (claude col 7, human col 8), `ssrn-decisions.xlsx` (decisions sheet — xlsx mandatory, csv export drops human column).

## 3. Pass 2 — Screening Result

4,061 Pass-1 Keep+Maybe items → **973 Keep, 73 Maybe, 2,908 Discard** (73% rejection rate, by design — tightened rubric).

## 4. Pass 2 — Trust Check (gating sample, stratified 20/category, unblinded)

Purpose: fast pre-apply gate, NOT the citable reliability statistic (see §6).

| Metric | Value |
|---|---|
| Items coded | 58 of 60 |
| Observed agreement (Po) | 86.2% (50/58) |
| Cohen's κ | **0.79 — substantial** |
| Discard agreement | 20/20 = 100% (zero false negatives) |
| Keep agreement | 17/20 = 85% |
| Maybe agreement | 13/18 = 72% |
| Disagreement rate | 13.8% |

Decision rule: ≤5% disagree → apply; 5–15% → apply + document; ≥15% → stop. 13.8% → **applied, with documentation.**

## 5. Pass 2 — Cross-Model Validation Attempt (non-SSRN, 600 rows, ChatGPT + Gemini)

**Gemini Flash proved unreliable as a validator:**
- 341 of 600 returned item_keys were hallucinated (~57% overall).
- Batches 1, 2, 4, 6, 7, 8, 12: ~98% hallucinated keys each (looked "clean," were actually silently fabricated).
- Batches 3, 5, 9, 10, 11 (the ones requiring re-prompting): returned valid keys.
- Only 259/600 (43%) Gemini decisions usable — and non-randomly, since usable batches are exactly the ones that needed intervention.

**Decision:** Gemini excluded from Pass 2 kappa analysis. Non-SSRN validation runs as a **two-rater design** (Claude, ChatGPT), documented with the caveat above rather than silently dropped.

## 6. Open Item — Blinded Methodology Validation (N=100)

Two-sample design (per 2026-06-03 methodology note):
1. **Trust Check** (§4 above) — stratified, unblinded, gating only.
2. **Methodology Validation** — random N=100, seed=42, no stratification, BLINDED (AI decision withheld until human re-codes), produces the citable Cohen's κ for the methods chapter.

**Status: sample #2 not confirmed complete as of this summary.** Before writing the methods-chapter reliability paragraph, confirm whether the blinded N=100 pass has been run — the Trust Check κ (0.79) is not a substitute for it by the design's own logic (Trust Check over-represents Maybe/under-represents Discard relative to the true population, biasing κ toward the wrong base rate).

## 7. Standing Rules Relevant to This Data

- Two-file blinding design (`validation_blind.csv` / `validation_key.csv`) is non-negotiable — don't collapse to one file.
- Report Po, κ (Landis & Koch label), per-category agreement, confidence-stratified agreement, and full confusion matrix whenever the blinded validation is run.
- Zero overlap confirmed between SSRN and non-SSRN corpora — combined-corpus analysis is valid to run.
