# Prompt — record-status re-check sweep (paste into a new session)

**Recommended model: Sonnet.** The convention is settled and documented; this is applying it.
Not Haiku — the decisive signal is semantic title comparison, and false matches are expensive.
Escalate to Opus only for cases this prompt tells you to flag.

---

You are running the **deferred record-status re-check** over the dissertation literature-review
working set. This is a **read-only sweep that produces a report. Make no writes of any kind** — not to
Zotero, not to the methodology docs, not to the corpus. Acting on the results is a separate,
authorized batch later.

## 1. Read these first

- `Methodology/Selection_Criteria_By_Phase.md` — the section **"DEFERRED — RECORD-STATUS RE-CHECK
  across the whole surviving corpus"**. That is the authoritative specification for this task,
  including the five things to check in order of consequence and the two worked transition cases.
  **Follow it; this prompt does not replace it.**
- `Methodology/Post_Accept_Closeout.md` §B12 — the Jin preprint→journal consolidation, the worked
  example of the one-record-per-study rule.
- `Handoffs/Dissertation_LitReview_Handoff_2026-09-04.md` — corpus shape and known metadata defects.
- Load the **`slr-conventions`** skill before making any classification call.

## 2. Scope

**The 106-item lit-review working set**, and nothing else. It is the union of:

| Collection | Key |
|---|---|
| `System LIterature Review / Phase 6 - Kept Core` | `R9ZHDXMN` |
| `Dissertation Lit Review` **(parent level — 2 items sit here, do not skip it)** | `9RN9P68N` |
| `Dissertation Lit Review / 01 - Primary` | `WVZFNSEC` |
| `Dissertation Lit Review / 02 - Supporting` | `BWPP3DZA` |
| `Dissertation Lit Review / 03 - Queue` | `4PE2T47Q` |
| `Dissertation Lit Review / 04 - Validation Apparatus` | `XPPEXKBN` |

Deduplicate by item key. **`slr-tools/stage6/worklist.json` already holds exactly this set** with
resolved metadata and local TXT paths — read it rather than re-querying, then verify the count is 106.
Do **not** sweep the screened-out pool; those items are not carried into synthesis.

**Highest-yield subset:** 63 items typed `Preprint (unrefereed)` or `Working paper (SSRN/OSF)`, and
84 of 106 (79%) are dated 2025–26 — exactly the cohort likely to have moved. But per the arbiter's
2026-08-25 ruling, **check all 106**, not only the preprints.

## 3. What to check, in order of consequence

1. **Retractions, corrections, expressions of concern.** Highest consequence — a retracted paper in
   Core is a research-integrity failure. Existing coverage is unreliable: `Citegeist.isRetracted`
   appears on only 23 of 79 Light Read papers, so **absence of the flag means nothing**. Use Scite
   `editorialNotices` and Crossref `update-to` relations.
2. **Preprint → published.** Venue, DOI, publication type.
3. **Version drift on preprints that stayed preprints.** arXiv v1 → v3 can change substance.
4. **Withdrawal or removal** — especially SSRN and self-hosted items.
5. **Venue/DOI changes** — proceedings moved to journals, DOIs reassigned.

## 4. The rule that makes this affordable

**Title change is the loudest signal available before opening a file, and it is visible from metadata
alone.** Working prior, from the two verified cases:

- **Title unchanged → expect copy-editing.** Metadata update plus a targeted check of the specific
  passages the review depends on. Worked case: `ZGST9CY6` (Zhu), SSRN → *AI and Ethics* — copy-edits
  and added citations only, no tag or note needed revision.
- **Title changed → expect substantive revision. Re-extract and re-read before quoting**, and
  re-check any tag that rested on framing rather than findings. Worked case: `DN9R4PDQ` (Li), arXiv →
  CHIWORK '26, retitled twice — scale/scaling 7→13 mentions, traceability 2→5, **calibration 0→4**.
  The framing that makes the paper relevant exists *only* in the published version.

Retitling is also what defeats Zotero's duplicate detection, so the same signal flags both risks.

## 5. Tools

- **Discovery** — the **`papersflow` MCP**, not the `semantic-scholar`/`exa` skills. If it reports
  unauthenticated, run its `authenticate` tool and hand Scott the OAuth URL.
- **Metadata backfill / DOI-venue-type resolution** — the **`openalex`** skill (free, no key, high
  coverage, caches locally).
- **Editorial notices** — Scite. **Update relations** — Crossref.
- **Library mechanics** — the `zotero` skill CLI or raw `curl` with `ZOTERO_API_KEY_RO`.
- **Reading** — local first: `~/Zotero/storage/<attachmentKey>/<filename>`, TXT over PDF. Never
  refetch what the library already holds. **Check attachment labels** — one item can carry
  `★ PUBLISHED … AUTHORITATIVE` alongside `SUPERSEDED … provenance only, do not quote`.

## 6. Known traps in this specific corpus

- **Four items have free-text `date` fields** that break any positional year extraction:
  `6ZW9QNQH` (`"October 9, 2025"`), `PPMTM4DG` (`"Dec. 2024"`), `TW4I6DU6` (`"June 5, 2024"`),
  `XK3P9C96` (`"April 13, 2026"`). Their derived short cites currently read *(Octo)*, *(Dec.)*,
  *(June)*, *(Apri)*. Report these; do not fix them in this pass.
- **No item in the working set carries a DOI in `publicationTitle`-derived metadata** — 0 of 63
  preprints. Resolve DOIs externally rather than expecting them locally.
- **Three items already hold two TXT attachments** (`59KP8GTP`, `UDVHQ5HR`, `ZGST9CY6`) — version
  pairs already present locally. Confirm which is authoritative before reporting drift.
- **`UDVHQ5HR` (Jin) was consolidated in place**, not as two records: it is now `journalArticle`,
  dated 2026-06-26, carrying `orig-type:preprint`, `orig-date:2026` and `orig-title:Uncovering
  systematic failures of LLMs…`. The closeout note §B12 describes a `superseded-by:A5WDGC7J` /
  `supersedes:UDVHQ5HR` pointer pair, and `A5WDGC7J` is **not** in the working set. **Verify which
  description is current and report the discrepancy — do not reconcile it yourself.**
- **`3Z45M3V3` (Fu)** is dated 2023 (arXiv posting) though the authoritative version is TOSEM 2025 —
  an already-known instance of exactly what this sweep looks for.
- **`VG6CIDQW`, `R4WJZBSF`** have no author metadata and are in Phase 6.

## 7. Conventions that govern the later write batch — record them, don't apply them

When you find a published version, the settled convention (do **not** execute it now) is: add the
published record, dedupe to one study **keeping the published version**, inherit disposition tiers,
tag `source:retrieval` on the newly found record, add the `superseded-by:` / `supersedes:` pointer
pair and `orig-type:` / `orig-date:` lineage, and **do not inflate identification counts — it is the
same study.** Superseded versions are **kept, not deleted**, with attachments explicitly labelled and
the superseded extraction retained under a distinct filename, because the panel runs and all
`cal:human:*` tagging were performed against the superseded text and that trail must stay
reconstructible.

## 8. Engineering constraints

Follow the `slr-pipeline-patterns` conventions: batches of 10, checkpoint after each, one checkpoint
key per batch, exit codes checked before a checkpoint is written, every returned item key validated
against the 106-key input set, batch globs anchored numerically (`batch_[0-9][0-9][0-9].json`), `None`
guarded with `(x or "")`, scripts written to a permanent location in the repo rather than `/tmp`, and
the run resumable — if it dies at item 60 it restarts at 61. Throttle external APIs politely.

## 9. Deliverable

A single report, `record_status_sweep_<date>.md`, plus one JSON per item so a bad row can be re-run.
The report must contain:

1. **Action-required table**, most consequential first: item key · short cite · what changed ·
   evidence (DOI, venue, notice URL) · **title changed? yes/no** · recommended action.
2. **Retractions / corrections / expressions of concern** — called out separately at the top, even if
   the section is empty. Say explicitly that it was checked and what was checked against.
3. **Re-extraction queue** — items where the title changed, i.e. where quoting the held text is
   unsafe. This is the list that blocks synthesis writing.
4. **Metadata-only updates** — title unchanged, safe to update in place.
5. **No change** — confirmed still current, with the source that confirmed it.
6. **Could not determine** — and why. Do not guess.
7. **Flagged for Opus** — cases where "same study or follow-up?" is genuinely contested.

State counts honestly, including how many items you could not resolve. **Do not inflate the corpus
count anywhere in the report** — a preprint and its published version are one study.
