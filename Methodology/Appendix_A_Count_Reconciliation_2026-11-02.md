# Appendix A Count Reconciliation (2026-11-02)

**Vibe Coding Governance SLR · read-only analysis for dissertation Appendix A (SLR summary)**

This analysis answers three questions that had to be closed before Chapter 2 was submitted:
(1) reconciling the PRISMA counts, (2) who made the title and abstract exclusions, and (3) the
triage threshold and evidence of false negatives. Every figure comes from the library, ledger files
or scripts. Nothing here comes from memory or estimation. Where the data could not answer a
question, §6 says so.

**Status: analysis only.** No library or funnel figure was changed. The open decisions in §7 are
the arbiter's to make.

## 0. How to reproduce

```
python3 slr-tools/prisma_funnel.py --dump /path/lib.json          # RO key
python3 slr-tools/prisma_funnel.py --snapshot /path/lib.json      # counts (cf. PRISMA_Funnel_v169153.json)
python3 slr-tools/appendix_a_recon.py /path/lib.json              # record-level residues used below
```

- **Source of record for counts:** snapshot **v169153** (`PRISMA_Funnel_v169153.json`, `PRISMA_Funnel.md`).
- **Snapshot used for the record-level work:** v169914 (2026-11-02). It differs from v169153 by one
  snowball Pass-1 discard: `2DEDF5PN`, moved to the trash on 2026-11-01. In the live library this gives
  9,501 identified, 2,694 in the snowball stream and 8,091 excluded. **Cite v169153 in the appendix.**
- **Stage-3 files:** `slr-tools/stage3/work/stage3_results.csv` (Opus triage, 976 primaries),
  `work/qa/qa_master_250.csv` (Opus verdicts on the QA sample), `work/qa/human_review_50.csv`
  (the human's blinded calls; `bin` = the human's bin), `work/review/*.csv` (the ≥55 review bands).

## 1. Count table

| Count reported | Breakdown | Source | Status |
|---|---|---|---|
| 9,502 identified | 6,807 query + 2,695 snowball | funnel JSON `identification.unique_records` | Confirmed (live 9,501) |
| 199 not screened | 78 query + 121 snowball | `phase1.query_unscreened` (81 − 3) + `snowball_held_no_abstract` | Confirmed |
| 121 snowball, no abstract | all `hold:no-abstract` | `phase1.snowball_held_no_abstract` | Confirmed |
| 78 query not screened | 67 Q-arXiv-07, 9 Scopus, 1 Committee, 1 Coursework | `PRISMA_Funnel.md` §5.1 | Confirmed. These 78 are unscreened because they were never bucketed, **not** because they lack an abstract |
| 9,300 screened | 6,726 + 2,574 | funnel JSON `phase1` | Confirmed |
| 3 query records "without a recorded decision" | `95CPB7CF`, `CKKGWMRH`, `WJCVBW54` | `appendix_a_recon.py` Q1a | Count confirmed; **description differs** (§2.1) |
| 8,092 excluded | 5,762 query + 2,330 snowball | 9,300 − 1,208 | Confirmed (live 8,091). Includes 84 Pass-2 maybes and 11 Pass-1 passes that never received a Pass-2 decision |
| 1,208 advanced | 964 query + 244 snowball | `phase2.query_eligible`; snowball records triaged | Confirmed. Caveat: 248 snowball records carry `s2:opus:keep`, and 4 of them were never triaged (§2.2) |
| 5 reaching triage through "other routes" | net = +7 − 2 | `appendix_a_recon.py` Q1b | **Differs**: this is a net figure, not five records |
| 1,213 at triage | 969 + 244 | `03 - Final` membership | Confirmed |
| 147 core | 114 + 33 | `fulltext.core_entering_fulltext` | Confirmed |
| 75 demoted (51.0%) | 59 + 16 | `fulltext.demoted_to_context` | Confirmed |
| 72 included | 55 + 17 | `fulltext.phase6_collection`; matches the predicate exactly | Confirmed |

## 2. Question 1: reconciling the counts

### 2.1 The three query records with no Phase-1 bucket that reached later stages

| Key | What the data shows | Furthest stage |
|---|---|---|
| `95CPB7CF` *Beyond the 'diff'* | Carries `s1:claude:keep` and `s2:machine:keep` but sits in no screening collection. Also carries `source:retrieval`, both `orig-type:` tags and a dangling `superseded-by:YDJPALG6`. **Inference:** it survived a merge, and the deleted copy held the bucket membership | Triage Core (human-confirmed) → **Phase 6, included** |
| `CKKGWMRH` *Vibe coding vs. agentic coding* | An arXiv query record that was also a snowball hit. It was screened in the snowball pipeline (`s1:sonnet:keep`, `s2:opus:keep`) and triaged there | Triage: Context (human-confirmed) |
| `WJCVBW54` *AI and agile software development* | A Q-arXiv-07 record that was also a snowball hit. It was screened in the snowball pipeline and triaged there | Triage: Context (Opus, 30–54 band, not human-reviewed) |

All three **have** screening decisions. The decisions are recorded as tags or on the snowball side,
not in the query-stream Phase-1 collections. The current figure note ("without a recorded screening
decision") is therefore inaccurate.

### 2.2 The 1,208 → 1,213 gap: +7 and −2

These are not curated, committee or post-screening additions. All of them are side effects of the
stream rule (a query record is the master) and of duplicate merges.

**Seven query-stream records in `03 - Final` that are not in the Phase-2 eligible set:**

| Route | Keys |
|---|---|
| Advanced through the **snowball** pipeline, not the query screen | `CKKGWMRH`, `WJCVBW54`, `RXNR8N95` (query Pass 2 = maybe; snowball `s2:opus:keep`), `Z76WEF74` (same) |
| **Merged record** whose triage placement came from the other copy (inferred from conflicting tags) | `95CPB7CF`; `FHUGCNKY` (has both `s2:machine:keep` and `s2:machine:discard`); `P868GNU7` (has `s2:machine:keep` and `s2:machine:maybe`) |

**Two eligible records that were never triaged** (no `s3:` tags, in no Phase-3 collection):
`2HTDGAT4` (trojan-trigger detection, SSRN) and `GFJN2SVU` (LLM frameworks for power engineering).

**Related leak:** four **snowball-only** records with `s2:opus:keep` **and `s3:opus:core`** sit in no
Phase-3 or Final collection: `7EK8G7I4`, `7UZ5FCF4`, `IM6DJDEE` (also has `s3:human:context`) and
`ZSTZT2KN`. These are Opus cores that never entered full-text review.

### 2.3 Draft Appendix A text

> Of the 9,502 unique records, 9,300 were screened at title and abstract and 199 were not screened.
> The other three were query records that were also retrieved by snowballing or were merged with a
> duplicate; their screening decisions were recorded in the snowball stream or on the merged copy
> rather than in the query-stream screening sets.ᵃ One of these three was retained in the final
> corpus. The 1,213 records at triage differ from the 1,208 that advanced by a net of five: seven
> records reached triage through the snowball stream or a merged duplicate, and two records that
> advanced were never triaged.ᵃ

ᵃ *Assumption:* the merge explanation for `95CPB7CF`, `FHUGCNKY` and `P868GNU7` is inferred from
their tags. It is not logged anywhere.

## 3. Question 2: who made the title and abstract exclusions

| Where excluded | n | Human decision present | Model only |
|---|---:|---:|---:|
| Query, Pass 1 discard | 2,750 | 1,397 (`s1:human:discard`) | 1,353 (Claude Sonnet 4.6) |
| Query, Pass 2 discard, maybe, or no Pass-2 decision | 3,012 | 30 (`s2:human:*`, escalations) | 2,982 (Sonnet → Opus arbiter) |
| Snowball, Passes 1–2 | 2,330 | 0 | 2,330 (Sonnet → Opus) |
| **Total** | **8,092** | **1,427 (17.6%)** | **6,665** |

**Agreement evidence** (`Screening_Reliability_Statistics.md` unless noted):

- **Pass 1 pilot:** the human and all three models coded the same 100 SSRN records. Claude–human κ = .273.
- **Pass 1, non-SSRN:** human overrides on 1,693 records, coded source by source, so **not a random
  sample** and skewed toward Claude discards. Claude–human κ = .371.
- **Agreement on discards, from tags** (`appendix_a_recon.py` Q2): of the 956 Claude Pass-1 discards
  the human also coded, the human agreed on 919 (96.1%) and overrode 37 (28 to keep, 9 to maybe).
  Tag-derived, so merge-unioned tags may add slight noise.
- **Pass 2 Trust Check:** 58 records, stratified and **unblinded**. κ = .792; all 20 sampled model
  discards were confirmed. It was a gate, not an IRR estimate.
- **Pass 2 blinded validation (N = 100): never coded.**
- **Snowball title and abstract screen:** no human check was found.

**Human keeps reversed by machine:** 84 query records carry `s1:human:keep`, sit in a Pass-2 discard
bucket, and have no `s2:human:` tag. Seven of them were re-adjudicated in F6 (changelog §175). The
eighth F6 record (Imai `Y9G3DA92`) was dropped at triage instead. F6 reported "8 records"; the
same signature finds **77 more that were not re-adjudicated**.

### 3.1 Draft Appendix A text

> Title and abstract exclusions were made by Claude unless the human recorded a decision, in which
> case the human decision governed. Of the 8,092 exclusions, the human decided 1,427, and the
> remaining 6,665, including all 2,330 snowball exclusions, rested on model decisions alone. Human
> Pass 1 decisions were coded source by source rather than sampled at random; among the 956 records
> Claude discarded that the human also coded, the human agreed on 919 (96.1%). At Pass 2, an
> unblinded stratified check of 58 records yielded κ = .79, and all 20 sampled model discards were
> confirmed.

## 4. Question 3: triage threshold and false negatives

### 4.1 Score and cutoff

- **Model and fields:** Claude Opus 4.8 assigned a `bin` and a `centrality` score from 0 to 100
  (`stage3_results.csv`; Zotero tag `centrality:<n>`). Rubric bands: core 70–100, context 30–69,
  discard 0–29.
- **Human-review floor: centrality ≥ 55**, the same in both streams.
- In practice every Opus core scored ≥ 63, so all of them were reviewed.

### 4.2 How 55 was chosen

- **The only written rationale** is the docstring in `slr-tools/stage3/stage3_review_buckets.py`.
  It says the blinded human-50 sample showed Opus cores held up at ≥ 75, and that the human found
  "hidden cores" at centrality **45–55**.
- **Dates:** the human sheet is dated 2026-07-06 and the review sheets 2026-07-08 (file timestamps;
  git history starts on 2026-07-15).
- **No documented reason for stopping at 55**, even though hidden cores appeared as low as 45.
- **Snowball stream** (`Stage4_Snowball_Enrichment_and_Rescreening.md` §5, 2026-07-13): 55 was
  "chosen over a looser ≥50" so the two streams would match.

### 4.3 Above and below the floor

| Stream | ≥ 55 (human-reviewed) | < 55 (auto-dispositioned) |
|---|---|---|
| Query (976 primaries) | **308**: 197 core + 111 context | **668**: 529 context + 139 discard |
| Snowball (267 triaged) | 130, reduced to **120** after cross-stream dedupe | **137**: 95 context + 42 discard (pre-dedupe) |

Below-floor records were **not excluded** as a group. Each kept Opus's bin, which was most often Context.

### 4.4 False-negative evidence

**Human-50 blinded sample:**

- The human classified 8 records as core. **4 of them scored below 55.** A fifth, `M74M3RFJ`, scored exactly 55.

  | Key | Opus | Human | Library now |
  |---|---|---|---|
  | `4VXJUF5I` | context / 52 | core | Context, no `s3:human` tag |
  | `VFZXPDJX` | context / 52 | core | Context, no `s3:human` tag |
  | `TLJPGLK9` | context / 50 | core | Context, no `s3:human` tag |
  | `QYT8RRWL` | context / 45 | core | Context, no `s3:human` tag |

- Of the 36 below-floor records in the sample, the human would have retained 26 (4 core, 22 context).
- The human classified 3 Opus discards as Context. All 3 are still Discard: `HCQSZWZR` (27),
  `PMSYQJQQ` (25) and `6UQMFSB8` (22).
- **None of these blinded human calls was applied to the library.** The 4 human cores never
  entered full-text review.

**250-record sample:** only the 50 records above were human-coded. For the other 200 the question
cannot be answered.

**After production triage:** no random sample of below-floor records was ever reviewed. The only
post-hoc check was F6, which deliberately included one below-floor record (Imai).

### 4.5 Draft Appendix A text

> At triage, Claude Opus assigned each record a centrality score from 0 to 100, and the human
> reviewed every record scoring 55 or higher (308 of 976 query records and 120 snowball records);
> records below 55 retained the model's classification, most often context, without human review.
> The floor was set in July 2026 after a blinded 50-record sample showed the model's core calls
> held at 75 and above and that the human identified core studies the model had scored between 45
> and 55.ᵃ In that sample, four of the eight records the human classified as core scored below 55.
> No sample of below-threshold records was reviewed after production triage.

ᵃ *Assumption:* the documents record no reason for setting the floor at 55 rather than lower.

## 5. Corrections to the current Appendix A text

- **Figure note ᵃ:** the three records do have screening decisions (§2.1). Reword the note.
- **Figure note ᵇ:** "five additional records reached triage through other routes" should describe
  a net of +7 − 2 (§2.2).
- **"Records scored below this threshold by Claude were excluded without individual review"** is
  inaccurate. Below-floor records were dispositioned without review. Most were retained as Context;
  only Opus discards were excluded.
- **"Records without an abstract were not screened"** sits next to "78 were query records". Readers
  may infer that the 78 also lacked abstracts. They were not screened because they were never bucketed.

## 6. Not determinable from the data

- Why `2HTDGAT4` and `GFJN2SVU` were never triaged.
- Why the four snowball Opus cores (`7EK8G7I4`, `7UZ5FCF4`, `IM6DJDEE`, `ZSTZT2KN`) are in no Phase-3 or Final collection.
- How the F6 population of eight was selected, given that the same signature finds 84.
- A written rationale or decision date for 55 over a lower floor, beyond file timestamps.
- Post-dedupe snowball above/below-floor counts against the final 244 (only 266 records carry a `centrality:` tag).
- Pre-dedupe raw hit counts (`Query_Composition_and_Log.xlsx` is not in the repo).

## 7. Open arbiter decisions

1. Apply the blinded human-50 calls for the 4 below-floor cores and 3 below-floor contexts, or
   report them as unapplied.
2. Re-adjudicate the 77 remaining human-keep → machine-discard records, or report them.
3. Disposition the 2 untriaged eligible records and the 4 orphaned snowball Opus cores.
4. If any of 1–3 is acted on, record it as a separately counted pass (the §5.3a precedent), not as
   a revision of the v169153 funnel figures.
