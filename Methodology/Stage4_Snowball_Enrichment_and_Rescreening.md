# Citation-Snowball Corpus — Data-Quality Enrichment & Three-Phase Re-Screening

**Vibe Coding Governance SLR · backward-snowball source stream**
**Date:** 2026-07-12 · Methods-chapter input

---

## 1. Rationale — screen on *good measurements*, and mirror the main corpus

The backward-snowball stream (references co-cited by the 114 Stage-3 cores) entered
the library as a large, **metadata-thin** pool: many records arrived title-only or
with OCR-mangled titles, missing abstracts, DOIs, and author lists, and with the
same work often present under several item types (preprint vs. published
journal/conference version). Two consequences follow, and this document records how
each was handled:

1. **Screening reliability depends on input quality.** An earlier calibration
   established that title-only screening is unreliable — a keep/discard decision made
   without an abstract is a decision made on insufficient data. Before re-screening,
   we therefore invested in a **data-quality enrichment pass** (§2) so that the
   automated screen operates on the best available measurement of each record.

2. **The snowball must meet the same bar as the database-query corpus.** The 983-item
   query corpus was screened Phase 1 → Phase 2 → Phase 3 and reviewed to a fixed
   relevance floor. To keep the two streams poolable, the snowball is pushed through
   an **identical three-phase instrument** (§4) and reviewed at the **identical bar**
   (§5). Collection structure mirrors the query stream (`01-Queries` / `02-Snowballing`
   under both Phase 2 and Phase 3, feeding a merged `03-Final`).

**Standing guardrail (unchanged):** the AI models are *consistency-check tools*; the
human is the arbiter. Every automated disposition is a routing decision, not a final
one — human review is focused (§5), never eliminated.

---

## 2. Data-quality enrichment (pre-screening)

Applied to the snowball keep/maybe set and the singleton review collections, in order:

- **Metadata backfill (OpenAlex).** For thin records, fill real URL, DOI, abstract,
  author list, venue, and date from OpenAlex, matched by title (exact) with a
  same-title similarity guard (SequenceMatcher ≥ 0.5) to reject wrong-paper hits.
  Key-less title search proved too strict for OCR-garbled titles and a broadened
  fuzzy search produced a **false positive** (matched *SecRepoBench* → a different
  *RealSec-bench* at 0.83 similarity); we reverted it and set the correct arXiv URL
  from the record's own identifier. *Lesson recorded in method: loosening the
  match threshold trades a few recoveries for silent metadata corruption, which is
  unacceptable in a review — strict exact matching is retained.*

- **Title canonicalization.** 34 OCR-corrupted titles of *real papers* were
  reconstructed by hand (broken intra-word spacing — "Git Hub Copilot", "LL Ms";
  run-together words — "Writesthe Docsin"; garbled OCR — "auto mating code revie wac
  ti viti es" → "Automating code review activities"). Extraction fragments (mis-
  imported section headings, sentences, table captions) and grey-lit stubs were
  **left untouched** — they are not reconstructable titles. Canonicalizing the real
  titles then unlocked OpenAlex matches that had been failing, recovering an
  additional 19 URLs plus DOIs/abstracts/authors once the titles were legible.

- **Cross-type de-duplication (pre-merge consolidation).** Zotero's native *Merge
  Items* keeps only the master record's fields and only groups items of the **same**
  item type — so a preprint and its published version never surface as duplicates.
  Before merging, duplicate groups were consolidated so each carried identical
  unioned metadata and a single normalized type (with `orig-type:` / `orig-date:`
  lineage tags), making the client merge lossless. **47 groups** were consolidated
  across the review collections plus a dedicated cross-type `Dedup` set; every group
  was confirmed same-work by shared DOI/arXiv id (false-positive-proof) or ≥0.99
  title+author confidence.

- **Grey-literature exclusion.** Grey literature (vendor/industry blogs, benchmark
  landing pages, documentation, social posts) is **generally excluded** from this
  stream, retained only as a few exceptions of extreme relevance flagged by hand.
  No web-search (Exa) URL-recovery pass was run, since grey-lit items are out of
  scope by policy.

---

## 3. Abstract-gating — a validity safeguard (SQC + Jidoka)

After the targeted enrichment effort, records were partitioned by a single quality
gate: **does the record carry an abstract?**

- **Abstract-bearing records (369)** proceed to the automated three-phase screen.
- **No-abstract records (126)** are **held**, not auto-screened and **not
  auto-discarded**: tagged `hold:no-abstract` and filed into a
  `Held - No Abstract (review)` collection for human exception-review.

Rationale. The items still lacking an abstract *after* a deliberate fetch effort are,
by construction, the de-facto deprioritized ones — grey-lit/documentation (e.g. ISO/IEC
42001, GitHub Copilot docs), foundational out-of-scope papers ("Language models are
few-shot learners"), and a residue of recent preprints not yet indexed. Auto-screening
them on title alone would reintroduce exactly the unreliable title-only decision the
enrichment pass exists to prevent. A handful are genuinely in-scope preprints, so blind
discard is also wrong. **Holding for human review** is the SQC-correct move (no
automated decision on an insufficient measurement) and the Jidoka-correct move
(route the exception to the human rather than let the line produce a defect).

---

## 4. Three-phase automated screen (mirrors the main corpus)

Run on the 369 abstract-bearing records, re-screened on the **enriched** metadata:

| Phase | Model | Rubric | Decision space | Lineage tag |
|---|---|---|---|---|
| **1** | Sonnet | `pass2_sonnet_prompt.md` | keep / maybe / discard | `s1:sonnet:<decision>` |
| **2** | Opus | `pass2_opus_prompt.md` | re-screen Phase-1 *maybes* → keep / discard | `s2:opus:<decision>` |
| **3** | Opus | Stage-3 relevance rubric | core / context / discard + **centrality 0–100** | `s3:opus:<bin>` (+ centrality) |

Final Phase-1/2 disposition = Phase-1 decision, except a Phase-1 *maybe* is resolved by
its Phase-2 decision. Phase-1 results **update** the existing
`Citation Snowballing/02-Screening` Keep/Maybe/Discard buckets in place; Phase-2 and
Phase-3 results are filed into the mirrored `Phase 2 / 02-Snowballing` and
`Phase 3 / 02-Snowballing` collections. The screen is batched (20/call), tolerantly
parsed, and resumable.

Why re-run all three (rather than reuse the first snowball screen): the first pass
screened the *pre-enrichment* data (title-only, mangled titles, missing abstracts). The
enrichment materially improved the measurement for a large fraction of records, so the
decisions are re-derived on the improved input to raise confidence and correct
title-only errors.

---

## 5. Human review — exact parity with the query corpus

Phase-3 assigns a 0–100 centrality score. The human reviews **every item scoring ≥ 55**;
items below 55 are auto-dispositioned. This floor is **exact parity** with the query
corpus, whose Stage-3 human review bottomed at the 55–69 context-recall band (cores
confirmed ≥ 70). Choosing 55 — rather than a looser 50 — ensures both streams are
dispositioned on the identical bar before they merge into `Phase 3 / 03-Final`.

Reviewed cores/contexts (both streams) become the extraction corpus for Stage 4;
snowball cores, like the original 114, require full-text fetch prior to coding.

---

## 6. Provenance & lineage (durable ground truth in tags)

Collection membership encodes *current disposition*; **tags encode durable lineage** so
every record's full history survives re-filing and client merges:

- `source:snowball`, `cocite:<n>` — origin and co-citation frequency
- `s1:sonnet:<d>`, `s2:opus:<d>`, `s3:opus:<bin>` (+ centrality) — each screening decision
- `hold:no-abstract` — held from automated screening for human review
- `orig-type:<kebab>`, `orig-date:<date>` — pre-merge type/lineage for consolidated dups

Inter-rater signal is preserved rather than overwritten: a human promotion that
contradicts a model discard keeps *both* votes as reliability data.

---

## 7. Reflexivity

This review studies human oversight of AI output that scales beyond human review
capacity; its own screening method faces the same problem and resolves it with the same
mechanisms the corpus catalogs — risk-based routing of human attention (the ≥55 floor),
exception escalation (abstract-gating hold; low-confidence keeps routed to a second
model), and decorrelated verification (Sonnet then Opus). Automated screening compresses
the pool; it never closes a case the human would want to see. The method instantiates
the phenomenon it examines — a deliberate, documented design choice.

---

## 8. Outcome (final distributions)

Input: 495 snowball keep/maybe records → **126 held** (`hold:no-abstract`) · **369**
abstract-bearing auto-screened.

- **Phase 1 (Sonnet, 369):** 250 keep · 27 maybe · 92 discard
- **Phase 2 (Opus, 277 non-discards):** **267 keep** · 10 discard
  (247/250 P1-keeps confirmed; 18/27 maybes rescued; 3 keeps + 9 maybes dropped)
- **Phase 3 (Opus relevance triage, 267):** 73 core · 152 context · 42 discard

Filed into `Phase 3 / 02-Snowballing` band sub-collections (score on each item as a
`centrality:<n>` tag):

| Sub-collection | n | In human review? |
|---|---|---|
| Core / 01-Confirm (75–100) | 20 | ✅ |
| Core / 02-Review (70–74) | 53 | ✅ |
| Context / 01-Recall (55–69) | 57 | ✅ |
| Context / 02-Below-55 (30–54) | 95 | — (below floor) |
| 03-Discard | 42 | — |

**Cross-stream de-duplication (post-triage).** Because dedup + metadata enrichment since
import made more matches detectable by DOI/arXiv, the live snowball set was re-checked
against the original triaged query corpus (Phase 3 / 01-Queries). **14 overlaps** found and
removed from the snowball collections so the query record stays master: **9 same-key**
(one record double-filed; 7 already query cores, 2 context) + **5 true cross-stream dups**
(different key, matched by DOI/arXiv/title — all map to query *context* masters; tagged
`superseded-by:<master>` with co-citation copied to the master). Detection guarded against a
bare-number false-match bug (arXiv ids matched only with context), which had inflated the
count from 14 to 40. Net: review set **130 → 120**; `Core/Confirm` 20 → 14 (the removed
"cores" were originals resurfacing via co-citation, not new finds).

**Human review set = 120** (all bins with centrality ≥ 55, after cross-stream dedup),
reviewed by drag/drop in the Zotero client. Reviewed cores/contexts merge with the query
stream in `Phase 3 / 03-Final` and feed Stage-4 extraction.

*Process note: a placeholder-mismatch bug initially caused Phase 2 to return 100 %
"discard" (all defaulted, `MISSING-from-model`). It was caught by a sanity check on the
distribution — an implausible result was verified rather than trusted — fixed, smoke-tested,
and re-run. This is the SQC discipline in §1 applied to the tooling itself.*

## 9. Human review outcome (≥55 confirmation, 2026-07-13)

Scott reviewed the 120-item ≥55 set (drag/drop in the client), applying the tighter §3 bar and the
oversight-vs-steering-vs-guidance discriminator.

- **Snowball final: 35 core · 175 context · 41 discard.** Opus over-called core (73 → 35) —
  consistent with the ~64 % Opus core-precision on the query stream; demoted items were
  overwhelmingly benchmark/eval/perception/theory (extraction-*depth* correction, not junk).
- **Filing convention:** band sub-collections (`Confirm`/`Review`/`Recall`/`Below`) = Opus-centrality
  bins; **Core-root** = human promotions (context→core); **Context-root** = human core→context
  overrides. Opus-context items mistakenly promoted then reverted go back to their *score band*, not
  root. Every reviewed decision is recorded as an `s3:human:<bin>` tag beside the preserved
  `s3:opus:` vote (inter-rater data).
- **Consistency QA:** an automated cross-check (collection placement vs `s3:opus` bin vs `s3:human`
  tag) caught 1 double-file and an automation-bias over-promotion cluster; all resolved.

**Final analysis corpus (both streams → `Phase 3 / 03-Final`):**

| Stream | Core | Context | Discard |
|---|---|---|---|
| Query | 114 | 716 | 139 |
| Snowball | 35 | 175 | 41 |
| **Total** | **149** | **891** | — |

**149 cores → full-text extraction (Stage 4)**; contexts → abstract-level. Snowball cores need
full-text fetch + TXT like the original 114.

### Triage discriminators that crystallized (for the methods chapter / codebook)
- **Core** = *measures the AI-code problem* (direct measurement — CWE/defect/persistence/review-gap
  rates) OR *operationalizes an oversight mechanism* (gate / escalation-timing / attention-routing)
  with a model + evidence.
- **Context** = benchmarks a tool/model capability · validates *which measurement tool* is best ·
  surveys developer perception/adoption · argues a position/agenda · proposes an *unevaluated*
  methodology/framework · general transferable theory (automation-bias, trust) · or is merely
  *applicable/useful to* the core problem without operationalizing it.
- **The recurring trap:** "applicable to / could feed into" the core = **context** (it *informs* the
  solution space); core requires the paper to *do* the measuring or the gating. And a *solution* only
  counts for core if it's an *oversight* solution (gate the produced artifact), not a *generation*
  solution (better prompts/training/tests = steering).
