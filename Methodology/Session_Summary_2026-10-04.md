# Session summary — 2026-10-04: F2 review, panel re-runs, and post-accept closeout

**What this session did, in one line.** It closed the SLR. Every open decision on the 72 included studies was ruled
and written. The reportable tag layer (`final:*`) was computed. The closeout tracker was worked down to one manual item
(E8). The survey question bank was started from the corpus while the rulings were fresh.

**Where the detail lives:** `slr-phase4/Taxonomy_Changelog.md` **§150–§181** (binding record, layered: never rewritten,
corrected forward) · `Methodology/Post_Accept_Closeout.md` (tracker) · `Methodology/SLR_Statistics_Reference.md` (every
quotable figure, recomputed at the end of the session).

**Roles.** The arbiter (Scott) made every ruling. The assistant (Claude Opus) prepared evidence, ran the panel and
scripts, wrote to Zotero only on authorization, and recorded all of it. All repo changes went through PRs (#23, #24
merged; #25 and #26 await the arbiter's merge).

---

## 1. Statistics documents (start of session)

- **PRISMA funnel** computed from the live library and made the source of record: 9,502 → 147 Core → **72 Included**
  (`PRISMA_Funnel.md`, PR #23).
- **Screening reliability**: keep rates and κ per stage per rater, plus a sample-set table
  (`Screening_Reliability_Statistics.md`, PR #24). It confirmed the arbiter's recollection: human ≈ 20%, Claude ≈ 30%,
  ChatGPT ≈ 56–60%, Gemini ≈ 65%.
- **Calibration figures corrected** (closeout C1–C9, §172). Two headline numbers were **retired as artifacts**:
  80.9% origination, and ~96% panel recall. They were replaced with exhaustive-arm figures: tag recall **91.6%** (blind
  Set B), tier recall **57.4%**, and **no detectable anchoring** (human origination, Set A vs Set B: 10.4% vs 7.8% at T2/T3; 12.7% vs 9.5% at T2prep-b).

## 2. F2 review — 15 general questions (§151–§165)

Rulings that change how the corpus is read:

| § | Ruling |
|---|---|
| 151, 158 | `deterministic-orchestration-v2` coined: code at the top level dispatching models for bounded tasks. **Enforcement must sit where the AI cannot route around it**: the outermost flow, or a mandatory chokepoint |
| 152–154 | Review absence counts as evidence only if observed and not shown to be selective. **No evidence means conjecture, and conjecture does not count.** Merged defects without a measured review signal do not fire. A correlational route is parked as `oversight-scaling-inversion-v3` |
| 156 | **Tests are excluded from rules-based checks.** `rules-based-checks-v3` = deterministic rule/static analysis, *"diversity of validation"*. Test authorship is parked as a future exercise, with a census collected (39 studies) |
| 157 | Architecture facets describe a paper's **own specified** architecture. A commercial product is `built-system` by definition |
| 159–162 | `survey-input-v2` kept (three conjunctive tests). Elicitation edge cases ruled. Smoke demos and fabricated outputs earn no evidence rung. *"Wants to be a benchmark ≠ is one"* |
| 163–165 | `peer-critique` is defined by topology (one agent judges another's output). **Human evaluator failure is automation bias**, not `evaluator-reliability`. Arbitration by a distinct model is a cross-model check |

**Provenance practice reaffirmed:** definitions are never edited. Each new reading gets a **new versioned tag**, all
versions coexist, and `governing_versions.json` says which one the synthesis reads.

## 3. Panel re-runs (F2b, F2c)

- **F2b** (`deterministic-orchestration-v2`) and **F2c** (`rules-based-checks-v3`) were run on all 72 by three vendors,
  each behind a **calibration gate** with blind anchors. Round 1 failed both times: a false positive (Parris) and a
  miss (Fu). The instrument wording was fixed, and round 2 passed.
- **Run-integrity incidents, disclosed:** an output directory moved mid-run (one output recovered from its raw log); one
  malformed JSON (re-run); and a greedy JSON-extraction bug that blanked one output (fixed and recovered).

## 4. Per-paper confirmations and corrections

- **144 arbiter rulings** (103 endorse, 41 reject) on 56 papers, kept in `f2_review_rulings.json` and all written to
  Zotero as `cal:human:*`.
- **Corrections recorded forward, not hidden:**
  - **§170**: a QA rejection on Ji contradicted an earlier ruling (§119b, *a rung needs no built system*). The arbiter
    reaffirmed §119b and the rejection was reversed.
  - **§173**: **the panel vote counter counted tags, not vendors.** Fifteen single-model primaries had passed as 2-of-3
    majorities. Fixed and the statistics regenerated; no ruling was invalidated.
- **B3 (`counterpoint`)**: deprecated vocabulary is excluded at the `final:*` computation step (§167). The silence audit
  found 6 silent tags on surviving papers, all `counterpoint`.

## 5. Closeout (`Post_Accept_Closeout.md`)

| Item | Outcome |
|---|---|
| **F1** | `final:*` computed and written: **843 tags on 72 studies**, all checks pass (§174) |
| **F6** | **8 human keeps reversed by machine without review**, re-adjudicated as a new `s4:human:*` layer: **6 reinstated to Context, 2 discards confirmed** (§175). Phase 6 unchanged. AgentCoder duplicate merged (§175a) |
| E1 | 4 mistyped working papers retyped to preprint; no published versions exist (§176) |
| E3 | **All 29 Dissertation Supporting members carry a named use**: 19 notes written; Vallecillos-Ruiz and Zhong added (§178) |
| E4 | Five Validation Apparatus Harvest entries back-filled from full text (§177b) |
| E5 | **Gao `59KP8GTP` is the "oversight fails at scale" anchor**; Branco is Supporting |
| E6 | Du upgraded to its ICML 2024 version; MapCoder abstract back-filled (§177c) |
| E7 | `new_pdfs/` found un-ignored and fixed, closing a route for full texts into the public repo (§177d) |
| Zhong | Upgraded to ICML 2026 (*SWE-IF*) (§179) |
| **F4** | **Survey question bank v0 written**: 55 items, 9 constructs, provenance C/H/S. The **HOS audit ran only after the corpus closed** (§180) |
| A, B, C, D, E2, E5, E9, F2, F3 | Done (see tracker) |
| **Open** | **E8** (manual Google Scholar counts, arbiter, later) · **F5** (gap assessment, unblocked by F1) · F4 continuation (wording, pilot) in its own workstream |

## 6. Statistics recomputed at session end (§177a, §181)

Every PRISMA count and every screening rate and κ **reproduced exactly** against snapshot v169436. The tag layer
statistics (T3) are unchanged from T2b, and `final:*` shows zero drift. The closeout work moved **no reported
figure**. The only addition is the separately reported F6 pass: abstract-level Context **886 + 6 = 892**, retained
Context **961 + 6 = 967**. The consolidated sheet is `SLR_Statistics_Reference.md`.

## 7. Methodological observations worth carrying into the write-up

1. **Our own pipeline is an oversight system, and it exhibited the failure modes the corpus describes.** These are
   recorded as provenance class **S** in the survey bank (design input, never findings):
   - a machine stage overturning human decisions unreviewed (F6);
   - agreement counted by tag rather than by independent source (§173);
   - silence read as confirmation (§150).

   Each was caught by a deliberate audit, not by the pipeline.
2. **Model agreement is no proxy for validity.** Models agree with each other (κ ≈ 0.5–0.6) far more than with the
   human (κ ≤ 0.30 at Stage 3). Humans confirmed every Core.
3. **Abstract-level screening over-includes by half.** 51% of abstract-level Cores were demoted at full text, all in one
   direction.
4. **The panel is a decent tagger and a poor triager**: tag recall about 90%, tier recall 57%.
5. **Attribution discipline:** the "popularity trap" belongs to Vallecillos-Ruiz et al., not Zietsman, who relays it
   (§177e).

## 8. Next

- **The arbiter:** merge PR #25, then #26. E8 when convenient.
- **F5** gap assessment (also confirms or retires the survey bank's *candidate silences*).
- **F4** continuation in its own workstream: cut 55 items to instrument length, map to hypotheses, pilot. The call for
  participants stays held until after candidacy.
- **Parked:** `oversight-scaling-inversion-v3` (correlational; Ghammam first), the test-authorship exercise (census in
  hand), and the 67 unscreened Q-arXiv-07 records.
