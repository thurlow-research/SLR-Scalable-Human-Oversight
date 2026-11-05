# Handoff: Dai is now coded, so the tag counts cover all 73 studies

**For:** Claude in Word, editing Scott's dissertation draft.
**Date:** 2026-11-05. **Source of every number:** `slr-phase4/data/final_tags_2026-11-05.json` and
`slr-phase4/Taxonomy_Changelog.md` §183 in the SLR repo.

## Files

- **Document:** `~/Library/CloudStorage/OneDrive-SharedLibraries-KumaJyo/EDU - Purdue/TECH 64600 - Analysis of Research in Industry and Technology/Assignment 7 - Chapter 2/Thurlow_Chapter_1+2.docx`
- **Figure A1 does not change.** Every count in it (149 full text, 76 reclassified, 73 included) is the
  same. Don't replace the picture.

## Ground rules

1. Turn on Track Changes so Scott can accept or reject each edit.
2. **Never touch Zotero citation fields** (`ADDIN ZOTERO_ITEM` / `ADDIN ZOTERO_BIBL`). Edit only the
   surrounding text.
3. Where this file gives replacement text, use it word for word. Where it says to change a number, change
   only that number.
4. **The draft may or may not already have the 2026-11-04 edits applied.** Each step below gives both
   versions of the text. Match whichever one is there.
5. When you're done, list every edit you made and anything you couldn't find.

## What changed (context; don't paste this)

The study added by the November 2026 re-examination (Dai, Liu, & Xu, 2024) was coded on 2026-11-05.
The earlier text said its coding was deferred. That is no longer true, so:

- The coding set is now **851 tags across all 73 studies** (was 843 across 72).
- Breakdown if the draft gives one: **778 theme and facet tags + 73 primary themes** (was 771 + 72);
  **658** both proposed by a panel majority and endorsed by the human (unchanged), **120** added by the
  human alone (was 113); **0** entered without human endorsement (unchanged).
- Dai's eight tags were all assigned by the human directly, because Dai was never in the model sweep.
- Records classified as **context** in the re-examination are still uncoded. Any sentence saying *that*
  stays.

---

## A. Chapter 2, Analysis

Find one of:
> The final set comprised 843 tags across the 72 studies, all endorsed or added by the author.

> The final set comprised 843 tags across the 72 studies included before the November 2026 re-examination, all endorsed or added by the author; coding of the study added by that re-examination was deferred.

Replace with:
> The final set comprised 851 tags across the 73 studies, all endorsed or added by the author.

## B. Appendix A, Thematic coding, last paragraph

Find one of:
> The final coding set for the 72 included studies comprised 843 tags, each either endorsed or added by the human,

> The final coding set for the 72 studies included before the November 2026 re-examination comprised 843 tags, each either endorsed or added by the human,

Replace with:
> The final coding set for the 73 included studies comprised 851 tags, each either endorsed or added by the human,

Then, if this sentence follows the paragraph, **delete it**:
> Thematic coding of the study added by that re-examination was deferred.

## C. Appendix A, Re-adjudication passes

If the subsection exists, **delete** this sentence:
> Thematic coding of the retained study was deferred and does not affect its inclusion.

**Keep** this one (it is about the context records, which are still uncoded):
> Records classified as context in these passes were read and classified under the same criteria as the rest of the corpus; their thematic coding was deferred.

## D. Tag counts and percentages anywhere in the draft

The corpus denominator moved from 72 to 73, so **every** tag percentage computed over the corpus
shifts slightly, even where the count didn't change. Search Chapter 2 (findings/synthesis) and Appendix A
for any count or percentage attached to a theme or facet, e.g. "18 of 72 studies", "23.6%", "the most
frequent theme". Look the tag up in the table below and change the number(s). Rows marked ← are the
seven tags (plus one primary) whose **count** changed. Every other row changes only its percentage.

If the draft gives a count with no denominator ("31 studies were built systems"), change it only if the
row is marked ←.

**Theme and facet counts** (studies carrying the tag; a study's primary theme is also counted here):

| Tag | Was (of 72) | Now (of 73) |
|---|---|---|
| risk-quality | 47 (65.3%) | 48 (65.8%) ← |
| agentic | 46 (63.9%) | 46 (63.0%) |
| hitl-workflow | 33 (45.8%) | 33 (45.2%) |
| built-system | 31 (43.1%) | 31 (42.5%) |
| framework | 31 (43.1%) | 31 (42.5%) |
| risk-overreliance | 31 (43.1%) | 31 (42.5%) |
| ai-review | 30 (41.7%) | 30 (41.1%) |
| oversight-explanation | 27 (37.5%) | 28 (38.4%) ← |
| risk-security | 26 (36.1%) | 26 (35.6%) |
| rules-based-checks | 22 (30.6%) | 22 (30.1%) |
| metrics | 20 (27.8%) | 21 (28.8%) ← |
| org-governance | 20 (27.8%) | 20 (27.4%) |
| method-experiment | 18 (25.0%) | 19 (26.0%) ← |
| provenance-auditability | 19 (26.4%) | 19 (26.0%) |
| assistive | 18 (25.0%) | 18 (24.7%) |
| risk-routing | 17 (23.6%) | 18 (24.7%) ← |
| method-mining | 17 (23.6%) | 17 (23.3%) |
| steering | 17 (23.6%) | 17 (23.3%) |
| quality-debt | 17 (23.6%) | 17 (23.3%) |
| design-only | 15 (20.8%) | 16 (21.9%) ← |
| automation-bias | 15 (20.8%) | 15 (20.5%) |
| deterministic-orchestration-v2 | 14 (19.4%) | 14 (19.2%) |
| rules-based-checks-v3 | 13 (18.1%) | 13 (17.8%) |
| general-code | 11 (15.3%) | 12 (16.4%) ← |
| oversight-scaling-inversion | 12 (16.7%) | 12 (16.4%) |
| evaluated-real-data | 11 (15.3%) | 11 (15.1%) |
| evaluated-synthetic | 11 (15.3%) | 11 (15.1%) |
| method-field-study | 11 (15.3%) | 11 (15.1%) |
| method-self-report | 10 (13.9%) | 10 (13.7%) |
| peer-critique | 10 (13.9%) | 10 (13.7%) |
| regulatory-compliance | 10 (13.9%) | 10 (13.7%) |
| problem-statement-anchor | 9 (12.5%) | 9 (12.3%) |
| agent-scope-drift | 9 (12.5%) | 9 (12.3%) |
| ai-code-insecurity | 9 (12.5%) | 9 (12.3%) |
| evaluator-reliability | 9 (12.5%) | 9 (12.3%) |
| oversight-theater | 9 (12.5%) | 9 (12.3%) |
| general-ai | 8 (11.1%) | 8 (11.0%) |
| non-developer | 8 (11.1%) | 8 (11.0%) |
| rules-based-checks-v2 | 8 (11.1%) | 8 (11.0%) |
| deterministic-orchestration | 7 (9.7%) | 7 (9.6%) |
| routing-signal | 7 (9.7%) | 7 (9.6%) |
| adopted | 6 (8.3%) | 6 (8.2%) |
| survey-input | 6 (8.3%) | 6 (8.2%) |
| agent-panel | 5 (6.9%) | 5 (6.8%) |
| evaluated-benchmark | 5 (6.9%) | 5 (6.8%) |
| risk-ip | 5 (6.9%) | 5 (6.8%) |
| tooling-supply-chain | 5 (6.9%) | 5 (6.8%) |
| cross-model | 4 (5.6%) | 4 (5.5%) |
| intro-framing | 4 (5.6%) | 4 (5.5%) |
| risk-bias | 4 (5.6%) | 4 (5.5%) |
| remediation-gating | 4 (5.6%) | 4 (5.5%) |
| formal-methods | 3 (4.2%) | 3 (4.1%) |
| expert-validated | 2 (2.8%) | 2 (2.7%) |
| lit-review | 2 (2.8%) | 2 (2.7%) |
| survey-input-v2 | 2 (2.8%) | 2 (2.7%) |
| oversight-scaling-inversion-v2 | 1 (1.4%) | 1 (1.4%) |

The draft will usually use plain-English names ("risk-based routing", "human-in-the-loop workflow",
"AI review"), not these slugs. Match by meaning. If you can't tell which tag a sentence refers to, **don't
guess**: list it for Scott.

**Primary themes** (one per study):

| Primary theme | Was (of 72) | Now (of 73) |
|---|---|---|
| ai-review | 13 (18.1%) | 13 (17.8%) |
| hitl-workflow | 10 (13.9%) | 10 (13.7%) |
| quality-debt | 9 (12.5%) | 9 (12.3%) |
| org-governance | 8 (11.1%) | 8 (11.0%) |
| oversight-explanation | 7 (9.7%) | 7 (9.6%) |
| risk-routing | 4 (5.6%) | 5 (6.8%) ← |
| ai-code-insecurity | 4 (5.6%) | 4 (5.5%) |
| automation-bias | 3 (4.2%) | 3 (4.1%) |
| oversight-scaling-inversion | 3 (4.2%) | 3 (4.1%) |
| regulatory-compliance | 3 (4.2%) | 3 (4.1%) |
| rules-based-checks | 3 (4.2%) | 3 (4.1%) |
| formal-methods | 2 (2.8%) | 2 (2.7%) |
| oversight-theater | 1 (1.4%) | 1 (1.4%) |
| provenance-auditability | 1 (1.4%) | 1 (1.4%) |
| tooling-supply-chain | 1 (1.4%) | 1 (1.4%) |

**Rankings:** no tag changes rank except where a count tie breaks. Risk-based routing (18) now ties
assistive generation (18) and moves ahead of method-mining, steering, and quality debt (17 each).
Risk-routing as a primary theme (5) now sits alone below oversight-explanation (7), ahead of
ai-code-insecurity (4). If the draft lists themes in rank order, check those positions.

## E. Discussion text that may mention Dai

If the findings discussion lists or counts studies under risk-based routing / prioritization of human
attention, Dai, Liu, and Xu (2024) now belongs there. It proposes a computed risk score (the "Risk
Number") that selects and orders code for a programmer's inspection, plus a diagram that guides the
inspection. The mechanism was specified but not implemented as software, and was evaluated in a
12-student lab experiment, run on human-written code. **Don't add new sentences about it.** Flag to
Scott any place where it would naturally belong (for example, a list of routing studies, or a count of
"N studies proposed risk scores").

## F. Final sweep

Search the whole document for **843**, **113**, **771**, **"deferred"**, and **"72"** used as a study
or tag denominator. After A to E, none should remain in SLR text except the context-records deferral
sentence kept in C. **Don't change** 72 inside citations, page ranges, volume numbers, or Zotero field
codes. Report each remaining hit to Scott with its location.
