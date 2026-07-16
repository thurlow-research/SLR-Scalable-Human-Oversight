# SLR Handoff — Stage 4: Fetch → Theme Development → Classification

**Vibe Coding Governance Systematic Literature Review**
**Created:** 2026-07-08 · **For:** a fresh session picking up after Stage 3
**Read first:** the memory index loads automatically; also `Methodology/SLR_Status_Update_2026-07-08.md` (milestone) and `Knowledge Xfer/SLR_CONTEXT.md` (canonical bootstrap).

---

## 0. Where we are

**Stage 3 (relevance triage) is COMPLETE and committed to Zotero.** The 983-item eligible pool was AI-triaged (Opus), cross-model + human QA'd, human-confirmed at the core boundary, deduplicated, and filed into a tiered extraction corpus. **Next stage = Stage 4: fetch the core documents, develop the coding scheme (themes/tags), then classify/extract the corpus.**

## 1. The corpus (Zotero group 6505702)

Filed additively into **`Phase 3 - Relevance Triage`** (collection `X5SUGJ2L`), 969 unique primaries:

| Tier | Count | Collection key | Extraction plan |
|---|---|---|---|
| **Core** | 114 | `539H8RBQ` (01-Core) | full-text fetch + full extraction |
| **Context** | 716 | `85JVIR9X` (02-Context) | abstract-level extraction (no fetch) |
| **Discard** | 139 | `JIMGLVAL` (03-Discard) | excluded from extraction |

Provenance tags on every filed item: `s3:opus:<bin>` (model call), `s3:human:<final>` (the 301 human-reviewed), `lit-review` (secondary literature — mine for reference snowballing), `framing` (`E9RAWBDT`, the vibe-coding anchor), `theme:oversight`/`theme:governance` (pre-existing thematic tags).

## 2. Stage 4 task A — fetch the core documents

- **58 of 114 cores need a PDF** (56 already have one). Fetch worklist = core items with `has_pdf=no`.
- Fetch **from the Zotero client** (SSRN/IEEE are session/subscription-gated — script fetching mostly fails). Filter the `01-Core` collection by "no attachment," or use `work/stage3_import_plan.csv` (final=core) joined against `work/stage3_results.csv` `has_pdf` column.
- Context tier is **not** fetched — extracted from abstracts.

## 3. Stage 4 task B — theme / tag (coding-scheme) development

Develop the extraction/coding framework the documents get classified against. Anchor it to the **two-part refined scope** (see §5):
1. **Problem** themes — magnitude/volume, risk types, and the *insufficiency* of current/automated oversight.
2. **Solution** themes — oversight mechanisms/designs (risk-routing, decorrelated/ensemble reviewers, LLM-as-judge, adversarial verification, guardrails/policy, observability, escalation/HITL, calibration metrics, governance/policy).

Useful inputs already in the library: the `hos-area:*` tags (buildable-mechanism taxonomy from the HOS pass), the existing `theme:oversight`/`theme:governance` tags, and the `lit-review` set's reference lists (backward snowballing to catch gaps). Recommended: derive candidate themes bottom-up from the 114 core abstracts, reconcile with the a-priori scope structure, then lock a codebook before classifying.

## 4. Stage 4 task C — classify / code the documents

- Code core items against the codebook from full text; context items at abstract level.
- **Methodology guardrail (non-negotiable): AI is a consistency-check tool, not the decision-maker.** Every AI-assisted classification is human-verified; single-coder protocol with AI as consistency aid.
- **Reuse the proven QA pattern:** AI first pass (Opus, script-based) → human review → cross-model check on a sample (Opus + codex GPT-5.5 + `agy` Gemini 3.1 Pro) → blinded reliability sample. The screening harness in `~/Code/SLR/slr-tools/stage3/` (`stage3_screen.py`, `stage3_qa_screen.py`, `stage3_qa_score.py`) is directly adaptable — swap the rubric.

## 5. Scope & framing (drives every decision)

- **Refined two-part scope** (post-hoc narrowing, documented): quantify the problem + characterize the solution. Behavioral/effectiveness/adoption/benchmark work was routed to Context.
- **Dissertation design:** the empirical contribution is a **survey of organizations** on how they frame/solve the oversight problem. The SLR builds the knowledge base that shapes that survey. **HOS is a *learning vehicle*, not the contribution** — don't let its feature set bias corpus/theme decisions.
- RQ core: *how organizations practice and scale human oversight of AI-generated code so oversight keeps pace with volume without sacrificing quality — incl. the governance/policy landscape and strengths/limitations of current oversight practices.*

## 6. Calibration findings that should shape Stage 4

- **Opus ≈ human (strict); codex/Gemini over-keep**, and **their dissent does NOT predict human judgment** (κ ≈ 0.01–0.04 vs human). No model shortcut around human review. Use Opus as the calibrated primary.
- Human↔LLM item-level agreement is "fair" (κ ≈ 0.30) — reproduced across passes. Expect the same for classification; plan for human arbitration.
- For any reliability statistic on an ordinal/multi-class coding scheme, report **weighted κ** + CI (κ precision depends on sample size, not population; FPC negligible at N≈976). A stratified gate ≠ the citable κ.

## 7. Parallel activities (dissertation-scope, NOT SLR steps)

- **HOS-relevance pass:** lives in the HOS repo now — `~/Code/HumanOversightSystem/Improvements/hos_identify.py` (self-contained; reads the SLR corpus via `--results`, default `~/Code/SLR/slr-tools/stage3/work/stage3_results.csv`; work dir `Improvements/work/hos/`). Flags corpus articles with buildable HOS mechanisms → `hos-relevant` + `hos-area:<area>` tags + "HOS Related Articles" collection (`Y4DVYPA4`), additive, orthogonal to `s3:`. Calibrated on batch 0; **full Opus run + collection `apply` still pending** (run from that dir: `hos_identify.py run` → `consolidate` → `apply --dry-run` → `apply --apply`). **HOS is a separate future session with its own handoff** — and gets NO presence in the SLR coding scheme (themes are field/RQ-derived; flow is SLR→HOS, never HOS→themes).
- **Contrarian/disconfirming-evidence hunt:** not yet run; feeds survey-instrument design; run over ALL tiers incl. discards (to avoid baking in bias). Keep separate from SLR classification.

## 8. Zotero access & safety

- Group library **6505702**; creds via direnv (`ZOTERO_API_KEY`, `ZOTERO_LIBRARY_ID`). **The currently-loaded key is a WRITE key** — default to read-only; **swap to write only for an authorized write, and prompt for a `File → Export Library` backup first.** Do not commit keys.
- API pattern (no dedicated CLI needed): `https://api.zotero.org/groups/6505702/…` with `Zotero-API-Key` header. Writes = per-item `PATCH` with `If-Unmodified-Since-Version` (no clobber); collection/tag changes must send the full arrays and be **additive** (preserve existing memberships).
- Superseded-duplicate convention: dropped record → source stream's `04-Superceded` + `superseded-by:<keeper>` + `review:superseded-has-decision`; keeper gets `supersedes:<dropped>`; remove dropped from Phase-2 pool.

## 9. Tooling & data map

- SLR scripts: `~/Code/SLR/slr-tools/stage3/` — `stage3_screen.py`, `stage3_qa_sample.py`, `stage3_qa_screen.py`, `stage3_qa_score.py`, `stage3_review_buckets.py`, `stage3_import.py`. Venv: `~/Code/SLR/slr-tools/venv` (usable for the HOS script too). HOS script moved out to `~/Code/HumanOversightSystem/Improvements/hos_identify.py`.
- Data: `work/stage3_results.csv` (Opus triage + metadata incl. `has_pdf`, `doi`, `source`), `work/stage3_import_plan.csv` (final disposition + tags per item), `work/review/*.csv` (human bucket decisions — **CSV is authoritative; XLSX deprecated/deleted**). HOS work data: `~/Code/HumanOversightSystem/Improvements/work/hos/` (batches + `hos_candidates.csv` after the run). Seeds: QA sample `20260706`.

## 10. Cautions / open items

- Swap the Zotero key back to read-only when not writing.
- The context tier (716) is mostly machine-only (`s3:opus` without `s3:human`) — fine for abstract-level extraction, but note the provenance if any context item gets elevated.
- Discards (139) are machine-only, unreviewed — if Stage 4 wants to double-check for false-negatives, that's a discrete pass.
- HOS repo org (`thurlow-research` vs `ScottThurlow`) still unconfirmed — verify before any push.
- Methods chapter still needs: the post-hoc scope-refinement paragraph, the reflexivity note (contrarian hunt), and weighted-κ reliability reporting.
