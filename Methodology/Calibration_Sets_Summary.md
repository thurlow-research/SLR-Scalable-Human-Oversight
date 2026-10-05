# Calibration Sets — Consolidated Summary (three rounds)

**Created 2026-10-04** from a chat session drafting Appendix A (SLR summary) of the dissertation (Claude Desktop).
**Revised 2026-10-04** (Claude Code) to the arbiter's account of the three rounds; the record was checked against
Zotero and `calib_sets.json` (changelog §182). No existing methodology document was edited. Sources: `Theme_Tagging_Calibration.md`
(§1, §5 item 7, §7 co-tagging protocol, §11.7, closeout C5), `slr-phase4/data/calib_sets.json`, Zotero
collections `JFN8693L`, `IURU9UTA`, `U65X7JNA`, and the arbiter's account (2026-10-04).

**Purpose.** The calibration design is described across several sections of
`Theme_Tagging_Calibration.md`, with terminology that shifted over time. This document states it in one
place, in the arbiter's terms, and records the open discrepancies so the dissertation and the SLR
article describe it consistently.

---

## 1. The three rounds (arbiter's account, 2026-10-04)

| Round | Set (Zotero) | Arbiter's term | Protocol | Role |
|---|---|---|---|---|
| 1 | **Set A** — `01-AI Calibration Run` (`JFN8693L`) | **Co-tagged set: validated the tagging** | Co-tagged by the human and Claude (the model panel tagged first; the human and Claude reconciled every tag) | **Validate the tagging approach.** Gaps in the vocabulary and problems with tag definitions were identified and resolved here. Instrument gate PASS and freeze at v2.1, 2026-07-18 |
| 2 | **Set B** — `02-Human Calibration Run` (`IURU9UTA`) | **"Training set"** | Tagged by the human, blind and first (no model tags existed); Claude audited afterwards without proposing tags; models tagged after the human set was recorded | **Human-labelled reference.** The coding instructions were refined against these labels (v2.2 → v2.13), and model output was scored against them |
| 3 | **Set C** — `03-Set C - AI Tag, Human Validate` (`U65X7JNA`) | **"Validation set"** | Tagged by the AI models first under the frozen instrument; the human validated | **A single-study check of the AI-first workflow** (`ZUM76CCG`, pilot closed 2026-08-15). Broad tagging of the corpus began after it (§3, item 1) |

**Terminology note for write-ups.** "Training" here means the instrument (instructions and vocabulary)
was refined against human labels. **No model was trained or fine-tuned.** In the dissertation, use
"human-labeled reference set" or "development set" for Set B, and say explicitly that only the
instructions were refined, so a reader does not infer fine-tuning.

## 2. Membership as recorded

From `calib_sets.json` (random draw, `random.seed(714)`, from the 149-item Core set at the time):

- **Set A (10):** UB2EVUFU · UDVHQ5HR · Z8TPRNEU · T8E8SCCG · M74M3RFJ · 2CKL96B8 · T72TU8B5 · VG6CIDQW ·
  22JBEZNK · F9JM9CI6
- **Set B (10):** B644HQFS · 6DXZGHD9 · E95T8E88 · 7V7SRG43 · UW2R6BBJ · BAWCBT9R · E3E5YA2E · 5VTAJISY ·
  TF56EPIP · R4WJZBSF
- **Set C (1 as recorded):** ZUM76CCG (Otten). Defined 2026-07-20 as "designated test cases, growing as
  probes surface"; not a random draw.

## 3. Open discrepancies (resolve before final write-up)

1. **Set C size — RESOLVED 2026-10-04.** Arbiter: *"I think Set C was one to check, and then we started tagging more
   broadly."* Set C was a **single-study check** of the AI-first, human-validate workflow (Otten `ZUM76CCG`), not a set
   of ten. Its pilot closed on 2026-08-15 once that study was adjudicated (§32, altitude precedent), and broad tagging
   of the corpus began in the same AI-first mode. The sweep's override and recall figures
   (`SLR_Statistics_Reference.md` §4.2) are therefore the measured result of that workflow at scale. The record
   (`calib_sets.json`, `U65X7JNA`) is correct as it stands, and no members are added. *(An intermediate reading on the
   same day, "abbreviated", is superseded by this one.)*
2. **Which set was "co-tagged."** `Theme_Tagging_Calibration.md` §7 names a co-tagging protocol
   (human tags blind, then AI quality assurance) arising **during Set B**, and says all ten Set B papers
   were ultimately co-tagged in that sense. Closeout C5 (2026-10-04) states the **first ten** calibration
   papers were co-tagged and drove the taxonomy, and **Set B was blind and unassisted** (no model tags
   seen). The arbiter's account matches C5 (Set A = co-tagged). Reconciliation: in Set B the AI audited
   the human's recorded tags against the instrument text (rule-level QA) but **proposed no tags**, so
   Set B is model-tag-free; Set A is where tags were developed jointly. Write-ups should use C5's
   framing and note that Set B's human tags received rule-level QA without model proposals.
3. **Instrument movement during Set B.** The instrument moved v2.2 → v2.13 during Set B, so early
   Set B blind tags predate rules the models later saw (disclosed in §7). Final adjudicated Set B tags
   are consistent with the frozen v2.13.

## 4. Figures tied to these sets (from `SLR_Statistics_Reference.md` only)

- **Tag recall, blind exhaustive arm (Set B):** 76 / 83 = **91.6%** (Set A 89.4%).
- **Anchoring check:** human origination Set A (model output visible) **10.4%** vs Set B (blind)
  **7.8%** (T2/T3): no detectable anchoring. *(The session summary's 12.7% vs 9.5% is superseded by the
  reference sheet.)*
- Set B and Set A each had **3 of 10** demote flags (`Theme_Tagging_Calibration.md` §7).

## 5. Dissertation wording (Appendix A, draft 2026-10-04)

> The coding approach was developed and checked in three calibration rounds before broad tagging began. In the first,
> ten randomly selected core studies were co-tagged by the human and Claude. This round served to validate the
> tagging: the gaps in the vocabulary and the problems with tag definitions that it exposed were identified and
> resolved before the next round. In the second, the human tagged a further ten randomly selected studies first,
> without seeing any model output. This human-labelled set served as a training set: the coding instructions were
> refined against it, and the models' tags were scored against it. In the third round, a single study was used to
> check the AI-first workflow: the AI models tagged first under the frozen instructions, and the human validated their
> tags. Broad tagging of the corpus then began in that mode, with the human adjudicating the model proposals on every
> study retained for synthesis. No model was trained or fine-tuned; "training" here means only that the coding
> instructions and vocabulary were refined against human labels.

The third-round sentence reflects the resolution of discrepancy 1 (a single-study check by design).