# Appendix A and Figure A1 text, recomputed at snapshot v170005 (2026-11-03)

Ready-to-paste dissertation text for Chapters 1–2 and Appendix A after the 2026-11-02 re-examination.
Every number comes from `PRISMA_Funnel_v170005.json` (`slr-tools/prisma_funnel.py`) or the record lists
in `PRISMA_Funnel.md` §5.3b. Figure: `Methodology/figures/PRISMA_Flow_Diagram.{png,svg}`
(`slr-tools/prisma_diagram.py`).

**Full-text decisions made 2026-11-03:** Dai (`VFZXPDJX`) kept as core and added to Phase 6, with theme
tagging deferred (`followup:tagging`); Grewal (`ZSTZT2KN`) demoted to Context. **Still open, and marked
[PENDING] below:** the arbiter's decisions on review sheet 4a (77 records) and sheet 4b (308 records); the
full evaluation of the 18 `followup:full-eval` records. Each one can change the counts here. Re-run the
two scripts once they land.

---

## 1. What changed since v169153, and why

| Figure | Was | Now | Why |
|---|---:|---:|---|
| Unique records | 9,502 | 9,501 | Snowball stub `2DEDF5PN` merged into Johnson et al. (2013) `F4ZS7B6Z` on 2026-10-28 (same study) |
| Snowball stream | 2,695 | 2,694 | same merge |
| Screened | 9,300 | 9,299 | same merge (the stub was a Pass-1 discard) |
| Duplicate records removed (box) | 7 | 6 | One leftover superseded arXiv duplicate was merged in the client. The script counts only superseded records still present, so the box understates removals. See §2 note |
| Advanced from screening | 1,208 | 1,212 | 248 snowball records carry `s2:opus:keep`, not 244. Four were triaged by Opus but never filed, so they were missing from the old count (`7EK8G7I4`, `7UZ5FCF4`, `IM6DJDEE`, `ZSTZT2KN`) |
| Excluded at screening | 8,092 | 8,087 | −1 merge, −4 now counted as advanced |
| Triaged | 1,213 | 1,219 | +4 snowball records filed; +2 eligible query records now triaged (`2HTDGAT4`, `GFJN2SVU`) |
| Core at triage | 147 | 148 | `ZSTZT2KN` (Grewal) |
| Context at triage | 886 | 889 | `7EK8G7I4`, `7UZ5FCF4`, `IM6DJDEE` |
| Discard at triage | 180 | 182 | `2HTDGAT4`, `GFJN2SVU` |
| Full text | 147 | 149 | + Grewal (triage) + Dai (re-examination) |
| Demoted after full text | 75 | 76 | Grewal |
| Included | 72 | **73** | Dai (kept core; theme tagging deferred) |
| Figure note ᵇ "two advancing records were not triaged" | 2 | 0 | both now triaged |
| Table A1: advanced but not triaged / context at triage | 1 / 15 | 0 / 16 | Jiang `7UZ5FCF4` now triaged (Context) |

## 2. Figure A1

Box counts (top to bottom): identified 9,501 (databases 6,557; other methods 250; citation
snowballing 2,694); duplicates removed 6; not screened 199 (no abstract after enrichment 121; query
records 78); screened 9,299; excluded 8,087; assessed in relevance triage 1,219; classified at abstract
level as context 889 and discarded 182; core studies assessed in full text 149; reclassified as context
after full-text review 76; included 73.

> **Decision for the arbiter: duplicates box.** The 9,501 count is post-dedupe, and most duplicates were
> removed by client merges that delete the losing record. The pre-dedupe total cannot be recovered
> from the library (`PRISMA_Funnel.md` §2.2). "n = 6" counts only the superseded duplicates still
> present, so it understates the duplicates actually removed. Options: (a) take raw hit counts from
> `Query_Composition_and_Log.xlsx` and report raw − 9,501; (b) keep the box and add
> "duplicates removed before import are not shown" to the note.

**Notes (paste under the figure):**

> *Note.* Counts show each record's classification at the stage named. Twenty records re-adjudicated in
> two later passes are reported separately in the text and do not change these counts, except as noted in c.
> ᵃ Screened (9,299) plus not screened (199) equals 9,498; the remaining three query records were
> screened in the snowball stream or under a merged duplicate record.
> ᵇ A total of 1,212 records advanced from title and abstract screening (964 query, 248 snowball);
> seven additional records reached triage through the snowball stream or a merged duplicate.
> ᶜ Includes one study classified as core in the November 2026 re-examination.

## 3. Appendix A, Screening process (replaces the four numbered stages)

> 1. Identification. The literature search yielded 9,501 unique records after de-duplication. Of
>    these, 199 were not screened: 121 snowball records had no accessible abstract after data
>    enrichment, and 78 query records were never assigned a screening decision. None of these
>    records advanced to later stages.
>
> 2. Title and abstract screening. A total of 9,299 records were screened for relevance and actionable
>    content, retaining only those that provided practical insights or tools for organizational
>    implementation, such as measurable indicators, operational mechanisms, detection criteria,
>    structured frameworks, or documented processes. Claude made the screening decisions unless the
>    human recorded a decision, in which case the human decision governed. Of the 8,087 exclusions,
>    the human decided 1,427; the remaining exclusions, including all snowball exclusions, rested on
>    model decisions alone. Among the 956 records Claude discarded that the human also coded, the
>    human agreed on 919 (96.1%). After this evaluation, 1,212 records advanced.
>
> 3. Relevance triage. A total of 1,219 records were triaged by how directly they addressed oversight
>    of AI-generated code in organizational or development-pipeline contexts. Claude Opus assigned
>    each record a classification and a centrality score from 0 to 100, and the human reviewed every
>    record scoring 55 or higher (308 query and 120 snowball records), confirming or changing each
>    classification. Records scoring below 55 kept the model's classification, most often context,
>    without human review, and could not enter full-text review. The threshold was set in July 2026
>    after a blinded 50-record sample showed that the model's core classifications held at scores of
>    75 and above, and that the human identified core studies the model had scored between 45 and 55.ᵃ
>    In that sample, four of the eight records the human classified as core scored below 55. These
>    records, and three records the sample had moved from discard to context, were re-examined in
>    November 2026 (see Re-adjudication passes). No other sample of below-threshold records was
>    reviewed. In total, 148 studies were classified as core.
>
> 4. Full-text review. A total of 149 core studies were read in full, including one classified as
>    core in the November 2026 re-examination. Of these, 76 (51.0%) were reclassified as context; none
>    moved the other way. Seventy-three studies were retained in the final corpus.

ᵃ *Disclosure to keep or drop:* the project documents record no reason for setting the floor at 55
rather than lower; for the snowball stream, 55 was chosen over 50 so that the two streams would match.
If kept, add: "The documents do not record why the threshold was not set lower."

## 4. Appendix A, new subsection: Re-adjudication passes (after Screening process)

> Two later passes re-examined records whose handling had departed from the protocol. Their results
> are reported here rather than folded into the counts in Figure A1. In October 2026, a
> process-integrity pass reviewed eight records that the human had retained at title and abstract
> screening but that a model later excluded without human review; six were reinstated as context and
> two exclusions were confirmed. In November 2026, a re-examination reviewed 12 records: the four
> below-threshold records the human had classified as core in the blinded triage sample, the three
> model discards that sample had classified as context, two records that advanced from screening but
> were never triaged, and three records the model scored as core above the threshold that were never
> filed for human review. Two were classified as core and entered full-text review, six as context,
> and four as discard. The November pass also found 77 further records with the same pattern as the
> October pass. [PENDING: "These were reviewed by the human; n were reinstated …" once sheet 4a is decided.]

## 5. Appendix A, Use of AI tools (sentence replacements)

- Replace *"During screening, the human examined every record above a defined relevance threshold;
  records scored below that threshold were excluded without human review."* with:
  > During triage, the human examined every record scoring at or above a relevance threshold of 55;
  > records scored below it kept the model's classification without human review and could not
  > advance to full-text review.
- Replace *"No study was included in the corpus, and no tag was assigned, based solely on model
  output."* with:
  > No study was included in the corpus, and no tag was assigned, based solely on model output.
  > Exclusions were different: most title and abstract exclusions rested on model decisions alone.
- In the Screening subsection, replace the last sentence (*"Records scored below this threshold by
  Claude were excluded without individual review."*) with:
  > Records scored below this threshold kept Claude's classification without individual review.

## 6. Chapter 2, Use of AI tools (one sentence)

Replace *"Records below the threshold were excluded without individual review."* with:
> Records below the threshold kept the model's classification without individual review.

Also in Ch. 2 Screening, replace "1,208 records advanced" with **"A total of 1,212 records advanced"**,
"147 were classified as core" with **"148 were classified as core"**, and "Full-text review reclassified
75 of these as contextual, leaving 72 studies in the final corpus" with **"Full-text review, which also
included one study classified as core in a later re-examination, reclassified 76 of 149 as contextual,
leaving 73 studies in the final corpus."** Change "9,502" to 9,501 in the same paragraph.

## 7. Supplementary sources (Table A1 note and breakdown paragraph)

Category counts are unchanged: theory 8, research design 10, historical baseline 11, policy context 5,
adjacent empirical evidence 32, author's prior work 1 (67).

> Of the 67 supplementary sources, 26 were not retrieved by the review's searches, and 41 were
> retrieved but not included: 15 were excluded at title and abstract screening (one of which was
> later reinstated as context in a re-adjudication pass), three were identified but not screened, 16
> were classified as context at triage, and seven were demoted after full-text review.

[PENDING: 18 of the 41 left the review at a step decided by a model alone or never decided (tag
`followup:full-eval`). Once they are evaluated, recompute this paragraph. Any that reach the final
corpus leave Table A1.]

Table A1 note: change the corpus count to 73, *"…not among the 73 studies in the systematic
corpus."* Table A1 itself is unchanged: neither Dai nor Grewal is in `10 - Used`.

## 8. Every place the final corpus count "72" appears (`Thurlow_Chapter_1+2.docx`, 2026-11-02 22:40)

| # | Location | Text |
|---|---|---|
| 1 | Ch. 1, methodology preview paragraph | "Of these, 147 studies were assessed in full text, and 72 were retained in the final corpus." → "149 … and 73 were retained" |
| 2 | Ch. 2, introduction | "…yielding a final corpus of 72 studies." |
| 3 | Ch. 2, Screening | "…leaving 72 studies in the final corpus." (also 147, 75) |
| 4 | Ch. 2, Analysis | "843 tags across the 72 studies" → see the tags note below |
| 5 | App. A, Screening process step 4 | "72 studies were retained in the final corpus." |
| 6 | App. A, Table A1 note | "…not among the 72 studies in the systematic corpus." |
| 7 | App. A, Thematic coding, last paragraph | "The final coding set for the 72 included studies comprised 843 tags…" |

Linked figures to update in the same edit: 9,502 → 9,501 (Ch. 1, Ch. 2 Screening, App. A step 1);
9,300 → 9,299; 1,208 → 1,212; "147 were classified as core" → 148; 147 / 75 / 51.0% in full-text
sentences → 149 / 76 / 51.0%; every "72" → 73.

**Tags note (rows 4 and 7).** Dai has no theme tags yet, so "843 tags across the 73 studies" would be
false. Either drop the tag count, or write *"…843 tags across 72 of the 73 included studies; one study
added in the November 2026 re-examination was not coded."*
