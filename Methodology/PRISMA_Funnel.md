# PRISMA Funnel — Final Screening Statistics

**Vibe Coding Governance SLR · Zotero group 6505702**
**Computed 2026-09-30** from a read-only snapshot of the live library (**library version 169153**)
by `slr-tools/prisma_funnel.py`; raw output in `PRISMA_Funnel_v169153.json`.

**This document is the source of record for PRISMA counts.** It supersedes the hand-carried
snapshot figures in earlier docs (9,518 / 983 / 970 / 149 / 148 / 147-with-76-demoted) — see §6
for how each reconciles. To refresh: `python3 slr-tools/prisma_funnel.py --dump lib.json` (RO key)
then `--snapshot lib.json`; Phase-6 must still equal the computed predicate (§4) or something moved.

> **Recomputed 2026-11-03 against snapshot v170005** (`PRISMA_Funnel_v170005.json`), after the
> 2026-11-02 re-examination (§5.3b). **v170005 is now the snapshot of record.** The tables below still
> show v169153. Every figure that changed, and why, is in `Appendix_A_Text_v170005.md` §1. Headline at
> v170005: 11,198 identified (import folders) · 1,697 duplicates removed · 9,501 unique · 199 not screened · 9,299 screened → 1,212 advanced · 1,219 triaged →
> 148 Core (+1 via re-examination) · 889 Context · 182 Discard · 149 full text → 76 demoted ·
> **73 included** (Dai kept, theme tagging deferred; Grewal demoted). Figure A1 is drawn from the JSON by `slr-tools/prisma_diagram.py`
> (`Methodology/figures/`).

PRISMA mapping follows the alignment note in `SLR_Paper_Outline_v0_2026-08.md` §3.1: internal
Phases 1–2 = **Screening**; Phase 3 (abstract-level triage + human ≥55 review) **and** Phases 4–5
(full-text read) together = one multi-pass **Eligibility** determination; Phase 6 = **Included**.

---

## 1. Headline funnel

| PRISMA stage | Query stream (databases + other methods) | Snowball stream | **Total** |
|---|---:|---:|---:|
| **Identification** — unique records | 6,807 (6,557 database + 250 other methods) | 2,695 | **9,502** |
| Not screened (see §5.1) | 78 | 121 held (no abstract) | 199 |
| **Screening** — title/abstract (Phases 1–2) | 6,726 screened → **964 eligible** | 2,574 screened → **244 advanced** | 9,300 → 1,208 |
| **Eligibility (a)** — abstract triage + human ≥55 review (Phase 3) | 969 | 244 | **1,213** → **147 Core** · 886 Context · 180 Discard |
| **Eligibility (b)** — full-text read (Phases 4–5) | 114 Core read → 59 demoted | 33 Core read → 16 demoted | **147 read → 75 demoted to Context** |
| **Included** — Phase 6 Kept Core (`R9ZHDXMN`) | 55 | 17 | **72** |

Screened (9,300) + not screened (199) = 9,499. The other 3 are query records that progressed
through later stages without a Phase-1 bucket (§5.1).

**Retained Context tier** (in-scope, abstract-level, synthesis draws on it): 886 + 75 demoted = **961**.

**Full-text reversal rate: 75 / 147 = 51.0%** (query 51.8%, snowball 48.5%). Every reversal ran
one way — Core → Context; no full read promoted a paper out of the Context tier into Phase 6. This is the
reportable measure of abstract-only screening reliability called for in
`Selection_Criteria_By_Phase.md` ("Screening decisions are a LAYERED HISTORY"): the screening-stage
count (147, `s3:human:*` layer) and the final count (72, after `demote:*`) are both reported, and
the gap between them is a result.

---

## 2. Identification

### 2.1 By source

Records per source import, live and de-duplicated. **Columns overlap** — a merged record carries
every source it was found in — so rows do not sum to the stream totals.

| Source | Records | Phase-1 pass (keep ∪ maybe) | Phase-2 eligible | Final Core | Included |
|---|---:|---:|---:|---:|---:|
| ACM DL | 350 | 90 | 42 | 6 | 3 |
| IEEE Xplore | 939 | 248 | 204 | 20 | 7 |
| Scopus | 1,082 | 357 | 154 | 28 | 11 |
| SSRN | 3,782 | 2,923 | 379 | 15 | 5 |
| Web of Science | 331 | 142 | 59 | 11 | 4 |
| arXiv | 468 | 254 | 192 | 56 | 36 |
| *Other methods:* Coursework | 98 | 42 | 26 | 5 | 3 |
| *Other methods:* Practitioner Network | 7 | 2 | 2 | 1 | 1 |
| *Other methods:* Committee Recommendations | 152 | 72 | 7 | 1 | 0 |
| Backward citation snowball | 2,747 | 388 | 4 | 35 | 19 |

The snowball row's "Phase-2 eligible" and "Final Core" counts include records also found by a
query (the query record is master; §2.2). Of the 72 included: **51** carry a database source, **4**
come only from other methods, **17** only from the snowball, and **2** were found by both a query
and the snowball.

SSRN's 77% Phase-1 pass rate against 10% Phase-2 eligibility is the recall-first design working
as intended (Phase 1 deliberately loose; Phase 2 is the operationalizability screen).

### 2.2 Stream assignment and deduplication

- **Stream rule.** A record in any query or other-methods import belongs to the **query stream**;
  the snowball stream is snowball-only records. **52** snowball hits were already in the query
  stream and are counted there, not twice.
- **Duplicates.** Deduplication ran at several points (DOI/title dedupe at import; 7 published↔preprint
  pairs at Stage 3; 47 cross-type groups and 14 cross-stream overlaps in the snowball; later
  preprint→journal merges, e.g. `UDVHQ5HR`→`A5WDGC7J`). Most were resolved by client-side Zotero
  merges, which delete the losing record but keep the union of the copies' collections, so a merged
  record still sits in every import batch that brought it in. **The import folders are the source of
  truth for records identified (arbiter, 2026-11-03):** identified before dedup = memberships summed
  over the import-batch collections; duplicates removed = that − unique records. At v170005:
  **11,198 identified** (databases 8,189: ACM 365, IEEE 1,305, Scopus 1,125, SSRN 4,559, WoS 337,
  arXiv 498; other methods 263: committee 157, coursework 99, practitioner network 7; snowball
  2,746) → **1,697 duplicates removed** → **9,501 unique**. The 6 superseded records still present as
  separate items are part of the 1,697. (Zotero's `dc:replaces` merge relation is *not* usable for
  this: it also records copies merged in from non-SLR collections, and overcounts to 1,924.) This
  replaces the earlier note that a pre-dedupe total could not be recovered.
- **Not records:** 9 items in the SLR tree are not search records (software entries for HOS and
  Claude Code, an OpenAthens stub, 6 webpage stubs). They are excluded from all counts.

---

## 3. Screening (title/abstract — Phases 1–2)

### 3.1 Query stream

**Phase 1 — recall screen** (Pass 1; Claude + ChatGPT + Gemini ensemble with human override;
decision of record = `02-Screening` bucket):

| Keep | Maybe | Discard | Screened |
|---:|---:|---:|---:|
| 1,945 | 2,031 | 2,750 | **6,726** |

**Phase 2 — operationalizability screen** (Pass 2; Sonnet + Opus arbiter, human review of 39
escalations; Trust Check κ = 0.79), on the 3,976 Phase-1 passes:

| Phase 1 → Phase 2 | Keep | Maybe | Discard |
|---|---:|---:|---:|
| Keep | **905** | 11 | 1,022 |
| Maybe | **59** | 73 | 1,896 |

**Eligible pool = 905 + 59 = 964.** Phase-2 *maybes* (84) were not advanced. 11 Phase-1 passes
have no Phase-2 bucket, and 1 Phase-1 discard sits in a Phase-2 bucket (§5.2).

### 3.2 Snowball stream

2,695 snowball-only records. **121 held** (`hold:no-abstract`), none of which advanced (§5.1).
Of the 2,574 with abstracts: the first-pass screen plus the post-enrichment Sonnet re-screen
(Phase 1: `s1:sonnet` keep 232 / maybe 199 / discard 2,143) and the Opus Phase-2 arbiter
(`s2:opus`) advanced **244** to triage — every one carrying `s2:opus:keep`. **2,330 screened out.**

---

## 4. Eligibility and inclusion

### 4.1 Phase 3 — abstract-level relevance triage + human ≥55 review

Opus assigns core/context/discard + centrality; **the human reviews every item ≥ 55** (exact
parity across streams), and every Core is human-confirmed.

| | Core | Context | Discard | Total |
|---|---:|---:|---:|---:|
| Query stream | 114 | 715 | 140 | 969 |
| Snowball stream | 33 | 171 | 40 | 244 |
| **`03 - Final` (merged)** | **147** | **886** | **180** | **1,213** |

- **Human-reviewed:** 301 query-stream records carry `s3:human:*`; snowball 57 tagged plus 16 Cores
  confirmed by drag-and-drop (blank = confirm, `Stage4_Snowball…` §9) with no tag written. **All
  147 Cores are human-confirmed.**
- **Opus vs human on Core:** Opus called 191 of the final query records Core; the human-confirmed
  Core count is 114 (60% of that). Snowball: 58 Opus Cores → 33 (57%). This matches the documented
  Opus over-call (~64% Core precision); it is a ratio of counts, not a matched precision figure.
- **2 records are filed in both Final/Core and Final/Context** (`U3IQJ4VK`, `DN9R4PDQ` — merged
  query+snowball records with conflicting stream calls). Counted as **Core**: both entered
  full-text reading, which is where their tier was finally decided (`U3IQJ4VK` included;
  `DN9R4PDQ` demoted).

### 4.2 Phases 4–5 — full-text read (finalizes eligibility)

147 Cores read in full and tagged (v2.13 instrument, 3-vendor × k=3 panel, human arbiter).

| | Read | Demoted to Context | Kept |
|---|---:|---:|---:|
| Query | 114 | 59 | 55 |
| Snowball | 33 | 16 | 17 |
| **Total** | **147** | **75** | **72** |

### 4.3 Phase 6 — Included

**72 studies** (`Phase 6 - Kept Core`, `R9ZHDXMN`). The collection matches the predicate
*Final Core ∧ human primary theme present ∧ no `demote:context`* **exactly** — 0 in the
collection outside the predicate, 0 in the predicate missing from it. Every Final Core has
been adjudicated: none lack a human primary (43 demoted papers also carry one).

---

## 5. Open items and residue (do not hide in the write-up)

### 5.0 Snowball records excluded on title alone — **823** (disclosed 2026-11-03)

823 snowball records with no abstract were Pass-1 discards by Sonnet on the title alone. Enrichment
(OpenAlex backfill) and the abstract gate (`hold:no-abstract`) ran only on the 495 records the first
snowball screen kept or marked maybe, so these never reached either. Arbiter: given the volume of material and limited human review capacity,
incomplete records were not pursued; disclosed, not re-screened. They are among the
8,087 excluded. (Snowball: 944 of 2,694 records lack an abstract = 823 discards + 121 held;
query stream: 135 of 6,807.)

### 5.1 Records identified but never screened — **78 query + 121 snowball**

- **67 from `Q-arXiv-07`** (imported 2026-05-23): no `source:` tag, no `s1:` tag, no screening bucket,
  absent from every Pass-1 decision file (`nonssrn-decisions-2026-05-25.csv`, `non-ssrn.3/`). The 13
  other Q-arXiv-07 records *were* screened. This **contradicts** the 2026-07-01 status note that
  the AI-House queries were fully screened. Most titles are visibly off-topic (clinical, legal,
  education, climate), but a few are not (e.g. `UWKJZNVT` *Agentic Agile-V: From Vibe Coding to
  Verified Engineering*, `D6ZMBAAC` *Code Broker*, `KKU8IHDT` *LLM Contribution Summarization*).
  **Needs an arbiter decision:** screen them now (Phase 1 → 2 → 3, same instrument), or report
  them as identified-not-screened with the reason.
- **11 other query stragglers** never bucketed: 9 Scopus (`LTRTQZ8S`, `BM9W2DBZ`, `56I8TNPD`,
  `LJZGJR7Z`, `Y8H35PWH`, `GPZPFW86`, `GQY4VJ5C`, `E29JDGC5`, `VJZP8UZJ`), 1 Committee
  Recommendations (`E7INBNBJ`, a CSIS events page), and 1 late Coursework add (`9SFJQ2XG`,
  `Q-CW-2026-08-15`, filed to Dissertation Lit Review). 3 further query records lack a Phase-1
  bucket but progressed through later stages, so they are not counted as unscreened.
- **121 snowball `hold:no-abstract`** records: held for human exception review by design
  (`Stage4_Snowball…` §3), and none has been advanced. **Decided (arbiter, 2026-10-04): report as "not
  screened — no abstract after enrichment"**; may be revisited later. If revisited, add the result as
  a separately counted pass, not by revising these figures.
- **None of the 78 unscreened query records reached any later stage.** 0 are in Phase 3 triage,
  0 in `03 - Final` and 0 in Phase 6, so the included set is unaffected. One (`CTEMUBEX`, combustion
  science) is a title duplicate of a screened record (`4WJNSATQ`). Q-arXiv-07's decision is still open.

### 5.2 Stage-to-stage leaks (±1–3 records; itemized in the JSON)

- 11 query Phase-1 passes have no Phase-2 bucket; 1 Phase-1 discard sits in a Phase-2 bucket.
- 2 eligible records were never triaged; 3 triaged records are not in the eligible buckets
  (merge survivors whose bucket membership came from the other copy).
- 2 records are double-filed Core+Context in `03 - Final` (§4.1).

### 5.3 Supersession tags are unreliable after client merges

Of 56 `superseded-by:` tags, **24 point at the record itself and 20 at keys the merge deleted**;
only 12 name a live, different record. A Zotero merge unions tags, so the survivor inherits its
loser's `superseded-by:`. Treating the bare tag as "removed duplicate" would wrongly drop 3
Phase-6 papers (`5VTAJISY`, `6ZW9QNQH`, `95CPB7CF`). **Rule:** a record is superseded only if
`superseded-by:<key>` names a *different, existing* key. The tag tidy-up belongs to Stage 6 cleanup.

> **Recomputed 2026-10-04 against snapshot v169436 (changelog §177a): all counts above unchanged.** Context including
> the §5.3a pass: abstract-level 886 + 6 = **892**; retained Context tier 961 + 6 = **967** *(corrected §181: an earlier
> "888 + 6 = 894" double-counted the two Core+Context records)*.

### 5.3a Process-integrity re-adjudication (2026-10-04, changelog §175) — a separately counted pass

Eight records the **arbiter kept at Pass 1** were later discarded **by machine** without human review (Pass 2, or Opus
triage below the review floor). They were re-adjudicated as a **new layer** (`s4:human:*`; collection `Reconsider`), not
by revising these funnel figures: **6 reinstated, all to Context** (Pappu's triage call returned Context, §175b), **2 discards
confirmed**. Phase 6 is unchanged at 72. Report this pass separately in PRISMA; the counts above stay as recorded.

### 5.3b Re-examination pass (2026-11-02) — a second separately counted pass

Twelve records were re-adjudicated in the `s4:human:*` layer (tag `reexam:2026-11-02`; collection
`Reconsider (re-examination, 2026-11-02)` `QUA8EW43`, with 01-Core / 02-Context / 03-Discard). Change
log, plan and applier: `~/Code/Thurlow-Research/reexam_2026-11-02/` (outside the repo).

| Group | Records | Call |
|---|---|---|
| Blinded human-50 cores scored below the 55 floor | `VFZXPDJX` Dai · `4VXJUF5I` · `TLJPGLK9` · `QYT8RRWL` | core · context · discard · discard |
| Blinded human-50 Contexts that Opus discarded | `HCQSZWZR` · `PMSYQJQQ` · `6UQMFSB8` | context ×3 |
| Phase-2 eligible, never triaged | `2HTDGAT4` · `GFJN2SVU` | discard ×2 |
| Snowball Opus cores ≥ 55, triaged but never filed or reviewed | `ZSTZT2KN` Grewal · `7EK8G7I4` · `7UZ5FCF4` | core · context · context |

**Filing rule used.** Records the pipeline never filed (`2HTDGAT4`, `GFJN2SVU`, `7EK8G7I4`, `7UZ5FCF4`,
`ZSTZT2KN`, plus `IM6DJDEE`, which carried its July `s3:human:context` but was never filed) were added
(add-only) to the Phase-3 and 03-Final collections the pipeline's own rules select. This completes a
missed step and revises nothing, and it is why triage moved 1,213 → 1,219. Records that already had a
filed decision were placed only in the re-examination collection; their Phase-3 placement is unchanged,
as in §5.3a. Dai enters full text through `01-Core` of that collection; Grewal through Final/01-Core.

**Full text (2026-11-03):** Dai kept as core and added to Phase 6 (theme tagging deferred,
`followup:tagging`; the funnel's Phase 6 check accepts that tag); Grewal demoted to Context.

**Not yet decided:** 77 more records with the F6 signature (human
Pass-1 keep → machine Pass-2 discard, no human Pass-2 decision); the 45–54 triage band (308 records);
18 dissertation-cited records that left the review at a model-only step (`followup:full-eval`).

### 5.4 Outside the funnel (post-closure supplementary material)

`Sept 2026 Papers` (13 items, `s3:sonnet:*` only) and `Forward Snowball - to screen` (4,
`source:forward-snowball`) were not run through this instrument and contribute **0** to the 73.
If the F5 gap-driven search adds studies, report it as a separate "other methods" stream with its
own counts, not by revising these.

---

## 6. Reconciliation with earlier reported figures

| Earlier figure | Where | What it actually was | Now |
|---|---|---|---|
| 9,518 "unique records" | SLR_CONTEXT, handoffs | every item filed under the SLR tree — includes 9 non-records and 7 unmerged superseded duplicates | **9,502** |
| 4,061 Phase-1 Keep+Maybe | status 07-01 | pre-merge snapshot | **3,976** (query stream) |
| 973 Keep / 73 Maybe / 2,908 Discard | status 07-01, GRAD 503 | **machine** Pass-2 proposals (`s2:machine:*`) before human escalation review, *not* the final pool | 964 / 84 / 2,918 |
| 983 eligible | status 07-01 | 924 + 59 at 07-01, before later merges | **964** (905 + 59) |
| 970 eligible | SLR_CONTEXT 08-18 | 911 + 59, intermediate | **964** |
| 149 Core / 891 Context | Selection_Criteria, Stage4_Snowball §9 (07-13) | before preprint→journal merges | **147 / 886** |
| 148 Core / ~890 Context | GRAD 503, SLR_CONTEXT | one study with two records (`UDVHQ5HR`/`A5WDGC7J`) | **147** |
| 147 read, 71 surviving / 76 demoted | Post_Accept_Closeout B6 (08-28) | before the 4 partially-tagged Accept papers were resolved (B7) | **72 / 75** |
| 72 Phase 6 | handoffs 08-29, 09-04 | correct | **72** ✓ |
