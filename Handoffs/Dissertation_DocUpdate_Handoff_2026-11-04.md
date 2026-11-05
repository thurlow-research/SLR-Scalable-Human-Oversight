# Handoff: update Chapters 1–2 and Appendix A after the November 2026 re-examination

**For:** Claude Desktop, editing Scott's dissertation draft.
**Date:** 2026-11-04. **Source of every number:** `Methodology/Appendix_A_Text_v170005.md` and
`Methodology/PRISMA_Funnel.md` in the SLR repo (snapshot v170005, plus the 2026-11-04 decisions below).

## Files

- **Document:** `~/Library/CloudStorage/OneDrive-SharedLibraries-KumaJyo/EDU - Purdue/TECH 64600 - Analysis of Research in Industry and Technology/Assignment 7 - Chapter 2/Thurlow_Chapter_1+2.docx`
  (the copy edited 2026-11-04 11:56; the one in the parent folder is an older copy, so don't edit it).
- **New Figure A1:** `~/Library/CloudStorage/OneDrive-purdue.edu/Systemic Literature Review/Methodology/figures/PRISMA_Flow_Diagram.png`
  (SVG beside it).

## Ground rules

1. Turn on Track Changes so Scott can accept or reject each edit.
2. **Never touch Zotero citation fields** (`ADDIN ZOTERO_ITEM` / `ADDIN ZOTERO_BIBL`). Edit only the
   surrounding text. Scott refreshes citations from the Zotero plugin.
3. Where this file gives replacement text, use it word for word. Where it says to change a number,
   change only that number.
4. When you're done, list anything you couldn't find.

## What changed (context; don't paste this)

- **Identification:** the box now shows records identified *before* duplicates were removed (11,198),
  1,697 duplicates removed and 9,501 unique records. The old text gave 9,502 unique records only. One
  snowball stub was merged into its duplicate, so 9,502 → 9,501 and 9,300 → 9,299.
- **Advanced 1,208 → 1,212:** four snowball records were triaged but never filed, so they had been
  missing from the count.
- **Core 147 → 148, full text 147 → 149, demoted 75 → 76, included 72 → 73:** the 2026-11-02
  re-examination added one core at triage (Grewal, later demoted) and one at re-examination (Dai,
  retained).
- **Decided 2026-11-04:** the human reviewed 77 records that were kept at screening but later excluded
  by a model (52 context, 25 discard), a random sample of 30 from the 45–54 triage band plus one more
  record from that band (28 context, 3 discard), and the 18 cited supplementary sources a model alone
  had removed (16 context, 2 discard). **None was core, so the corpus stays at 73.**
- **Thematic tags:** the 843 tags cover the 72 studies coded before the re-examination. The added
  study (Dai) is included but its coding was deferred. Inclusion is what the dissertation relies on.

---

## A. Chapter 1

**A1. Methodology preview paragraph.** Find:
> The search identified 9,502 unique records from database searches, preprint servers, and citation snowballing. Of these, 147 studies were assessed in full text, and 72 were retained in the final corpus.

Replace with:
> The search identified 11,198 records from database searches, preprint servers, and citation snowballing, or 9,501 unique records after duplicates were removed. Of these, 149 studies were assessed in full text, and 73 were retained in the final corpus.

## B. Chapter 2

**B1. Introduction.** Find "yielding a final corpus of 72 studies" and change 72 → **73**.

**B2. Screening paragraph.** Make these four replacements:
- "The search retrieved 9,502 unique records." → **"The searches identified 11,198 records; removing 1,697 duplicates left 9,501 unique records."**
- "1,208 records advanced." → **"A total of 1,212 records advanced."**
- "147 were classified as core." → **"A total of 148 were classified as core."**
- "Full-text review reclassified 75 of these as contextual, leaving 72 studies in the final corpus." →
  **"Full-text review, which also included one study classified as core in a later re-examination, reclassified 76 of 149 as contextual, leaving 73 studies in the final corpus."**

**B3. Use of AI tools (same section).** Find:
> Records below the threshold were excluded without individual review.

Replace with:
> Records below the threshold kept the model's classification without individual review.

**B4. Analysis.** Find "The final set comprised 843 tags across the 72 studies, all endorsed or added by the author." Replace with:
> The final set comprised 843 tags across the 72 studies included before the November 2026 re-examination, all endorsed or added by the author; coding of the study added by that re-examination was deferred.

## C. Appendix A

### C1. Screening process: replace the four numbered stages

Replace the text of the four numbered items (Identification … Full-text review), keeping the list
formatting and the lead-in "There were four stages in the screening:":

> 1. Identification. The searches identified 11,198 records: 8,189 from database searches (ACM Digital Library 365, IEEE Xplore 1,305, Scopus 1,125, SSRN 4,559, Web of Science 337, arXiv 498), 263 from other methods (committee recommendations 157, coursework 99, practitioner network 7), and 2,746 from backward citation snowballing. Removing 1,697 duplicates left 9,501 unique records. Of these, 199 were not screened: 121 snowball records had no accessible abstract after data enrichment, and 78 query records were never assigned a screening decision. None of these records advanced to later stages.
>
> 2. Title and abstract screening. A total of 9,299 records were screened for relevance and actionable content, retaining only those that provided practical insights or tools for organizational implementation, such as measurable indicators, operational mechanisms, detection criteria, structured frameworks, or documented processes. Claude made the screening decisions unless the human recorded a decision, in which case the human decision governed. Of the 8,087 exclusions, the human decided 1,427; the remaining exclusions, including all snowball exclusions, rested on model decisions alone. Among the 956 records Claude discarded that the human also coded, the human agreed on 919 (96.1%). Of the snowball exclusions, 823 records had no abstract and were excluded on the title alone: metadata enrichment and the abstract check were applied only to snowball records the first screen retained. Given the volume of material and limited human review capacity, incomplete records were not pursued further. After this evaluation, 1,212 records advanced.
>
> 3. Relevance triage. A total of 1,219 records were triaged by how directly they addressed oversight of AI-generated code in organizational or development-pipeline contexts. Claude Opus assigned each record a classification and a centrality score from 0 to 100, and the human reviewed every record scoring 55 or higher (308 query and 120 snowball records), confirming or changing each classification. Records scoring below 55 kept the model's classification, most often context, without human review, and could not enter full-text review. The threshold was set in July 2026 after a blinded 50-record sample showed that the model's core classifications held at scores of 75 and above, and that the human identified core studies the model had scored between 45 and 55. The threshold was not set lower because human review capacity was limited: lowering it to 45 would have added 308 records (253 query, 55 snowball) to the 428 already reviewed. In that sample, four of the eight records the human classified as core scored below 55. These records, and three records the sample had moved from discard to context, were re-examined in November 2026, together with a random sample of the records scored 45 to 54 (see Re-adjudication passes). In total, 148 studies were classified as core.
>
> 4. Full-text review. A total of 149 core studies were read in full, including one classified as core in the November 2026 re-examination. Of these, 76 (51.0%) were reclassified as context; none moved the other way. Seventy-three studies were retained in the final corpus.

### C2. Sentence after the list

Find:
> Records without an abstract were not screened.

Replace with (the old sentence contradicts step 2, which says 823 snowball records without abstracts were excluded on title):
> Records whose abstract could not be recovered were not screened, except snowball records excluded on title alone at the first screen (step 2).

Keep the following sentence ("Each publication was counted only once…") as it is.

### C3. Figure A1

Replace the picture (currently a linked `INCLUDEPICTURE` from a claude.ai URL) with the PNG listed under
Files above, **embedded, not linked**. Keep the caption "Figure A1 PRISMA 2020 flow diagram of record
identification, screening, and inclusion" and its TOC entry. The new figure shows: identified 11,198
(databases 8,189; other methods 263; snowballing 2,746); duplicates removed 1,697; unique 9,501;
not screened 199; screened 9,299; excluded 8,087; triaged 1,219; context 889; discarded 182;
full text 149; reclassified as context 76; included 73.

### C4. Figure notes: replace the whole "Note:" paragraph under the figure

> *Note.* Counts show each record's classification at the stage named. Records re-adjudicated in later passes are reported separately in the text and do not change these counts, except as noted in c.
> ᵃ Screened (9,299) plus not screened (199) equals 9,498; the remaining three query records were screened in the snowball stream or under a merged duplicate record.
> ᵇ A total of 1,212 records advanced from title and abstract screening (964 query, 248 snowball); seven additional records reached triage through the snowball stream or a merged duplicate.
> ᶜ Includes one study classified as core in the November 2026 re-examination.

(Check that the a/b/c markers on the figure match. The new PNG carries them.)

### C5. New subsection "Re-adjudication passes"

Insert after the figure notes and before "Inclusion and exclusion criteria", as a heading at the same
level as "Screening process":

> **Re-adjudication passes**
>
> Two later passes re-examined records whose handling had departed from the protocol. Their results are reported here rather than folded into the counts in Figure A1. In October 2026, a process-integrity pass reviewed eight records that the human had retained at title and abstract screening but that a model later excluded without human review; six were reinstated as context and two exclusions were confirmed. In November 2026, a re-examination reviewed 12 records: the four below-threshold records the human had classified as core in the blinded triage sample, the three model discards that sample had classified as context, two records that advanced from screening but were never triaged, and three records the model scored as core above the threshold that were never filed for human review. Two were classified as core and entered full-text review, six as context, and four as discard. Both core studies were read in full and classified under the same criteria as the rest of the corpus: one was retained and one was reclassified as context. Thematic coding of the retained study was deferred and does not affect its inclusion. The November pass also found 77 further records with the same pattern as the October pass. The human reviewed all 77: 52 were reinstated as context and 25 exclusions were confirmed, seven of them for lack of an abstract. To check the triage threshold, the human also reviewed a random sample of 30 of the 308 records scored 45 to 54, plus one record from that band the human had retained at screening; none was classified as core (28 context, three discard). Finally, the human evaluated the 18 supplementary sources cited in this dissertation that had left the review at a step decided by a model alone (three of them also appear in the groups above): 16 were classified as context and two as discard. No record in the November pass beyond the two noted above was classified as core, so the final corpus is unchanged. Records classified as context in these passes were read and classified under the same criteria as the rest of the corpus; their thematic coding was deferred. Several informed the theoretical framing, methods, and adjacent-domain evidence in this dissertation.

### C6. Supplementary sources

**Stop and check Table A1 before editing this paragraph.** The table looks mid-edit: the Research design
row says n = 11 but lists 12 sources (Li et al. 2024 and Meem & Johnson 2025 appear new), and the rows
sum to 68 while the paragraph says 67. Sorkin & Woods (1985) and de Véricourt & Gurkan (2023) are cited
in Chapter 2 and may also belong in Table A1 (Theory). **Report the actual row counts to Scott and ask
whether his Table A1 additions are final.** Don't recompute the breakdown yourself. The SLR assistant
recomputes it from Zotero once the list is final.

Until then, the paragraph text as of v170005 (67 sources) is:
> Of the 67 supplementary sources, 26 were not retrieved by the review's searches, and 41 were retrieved but not included: 15 were excluded at title and abstract screening (one of which was later reinstated as context in a re-adjudication pass), three were identified but not screened, 16 were classified as context at triage, and seven were demoted after full-text review. Eighteen of the 41 had left the review at a step decided by a model alone. The human later evaluated all 18 and classified 16 as context and two as discard (see Re-adjudication passes); none entered the systematic corpus.

Keep the existing closing sentence ("Most of the 41 reported descriptive evidence…").

### C7. Table A1 note

Find "not among the 72 studies in the systematic corpus" and change 72 → **73**. Then add right after the
note:
> Supplementary sources classified as context informed the theoretical framing, historical baseline, and adjacent evidence; only studies directly addressing human oversight of AI-generated code with an operationalizable mechanism, measurement, or finding were included in the systematic corpus.

### C8. Use of AI tools: three sentence replacements

- Find "During screening, the human examined every record above a defined relevance threshold; records scored below that threshold were excluded without human review." Replace with:
  > During triage, the human examined every record scoring at or above a relevance threshold of 55; records scored below it kept the model's classification without human review and could not advance to full-text review.
- Find "No study was included in the corpus, and no tag was assigned, based solely on model output." Replace with:
  > No study was included in the corpus, and no tag was assigned, based solely on model output. Exclusions were different: most title and abstract exclusions rested on model decisions alone.
- In the **Screening** subsection, find "Records scored below this threshold by Claude were excluded without individual review." Replace with:
  > Records scored below this threshold kept Claude's classification without individual review.

### C9. Thematic coding, last paragraph

Find "The final coding set for the 72 included studies comprised 843 tags, each either endorsed or added by the human," and replace with:
> The final coding set for the 72 studies included before the November 2026 re-examination comprised 843 tags, each either endorsed or added by the human,

Then, after the end of that sentence ("…insufficient to replace human review."), add:
> Thematic coding of the study added by that re-examination was deferred.

## D. Final sweep

Search the whole document for **9,502, 9,300, 1,208, 147, 75 (as a study count), 72 (as a study
count)** and the phrase **"excluded without"**. Any that remain in SLR text should be gone after A–C.
**Don't change** 72 or 75 inside citations, percentages (6.72%, 75.0%), volume numbers or Zotero
field codes. Report each remaining hit to Scott with its location.
