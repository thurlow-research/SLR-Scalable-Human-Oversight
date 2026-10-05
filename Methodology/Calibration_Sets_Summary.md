# Calibration Sets — Consolidated Summary (three rounds)

**Created 2026-10-04; revised 2026-10-04** (Set C clarified by the arbiter) from a chat session
drafting Appendix A (SLR summary) of the dissertation. New document; no existing methodology document
was edited. Sources: `Theme_Tagging_Calibration.md` (§1, §5 item 7, §7 co-tagging protocol, §11.7,
closeout C5), `slr-phase4/data/calib_sets.json`, Zotero collections `JFN8693L`, `IURU9UTA`,
`U65X7JNA`, and the arbiter's account (2026-10-04).

**Purpose.** The calibration design is described across several sections of
`Theme_Tagging_Calibration.md`, with terminology that shifted over time. This document states it in one
place, in the arbiter's terms, so the dissertation and the SLR article describe it consistently.

---

## 1. The three rounds (arbiter's account, 2026-10-04)

| Round | Set (Zotero) | Arbiter's term | Protocol | Role |
|---|---|---|---|---|
| 1 | **Set A** — `01-AI Calibration Run` (`JFN8693L`), 10 studies | Co-tagged validation set | Human and Claude co-tagged; the three-vendor panel also tagged | **Validate the tagging approach.** Gaps in the vocabulary and problems with tag definitions were identified and resolved on this set. |
| 2 | **Set B** — `02-Human Calibration Run` (`IURU9UTA`), 10 studies | "Training set" | Human tagged first, blind (no model tags existed); models tagged afterward | **Human-labeled reference.** Instrument refinement continued against these labels; model output was scored against them. |
| 3 | **Set C** — `03-Set C - AI Tag, Human Validate` (`U65X7JNA`), **1 study** (Otten, `ZUM76CCG`) | Pilot test | Models tagged first under the frozen instrument; human validated/adjudicated | **Single-study pilot of the production workflow** (AI-first, human-validate). |

**After Set C.** Production tagging of the full set proceeded on the AI-first workflow **on the
standing assumption that the human would quality-check the model tags, and that QA was carried out**
(arbiter, 2026-10-04). See `Theme_Tagging_Calibration.md` §10 (procedure as practised) and the
closeout statistics in `SLR_Statistics_Reference.md` §4.2 for how the review evolved (scan-and-query
early; explicit confirm/reject later; early residue closed out explicitly; final tag set has no
modal-only silent tags).

**Terminology note for write-ups.** "Training" here means the instrument (instructions and vocabulary)
was refined against human labels. **No model was trained or fine-tuned.** In the dissertation, use
"human-labeled reference set" for Set B and say explicitly that only the instructions were refined,
so a reader does not infer fine-tuning.

## 2. Membership as recorded

From `calib_sets.json` (Sets A and B: random draw, `random.seed(714)`, from the 149-item Core set at the
time):

- **Set A (10):** UB2EVUFU · UDVHQ5HR · Z8TPRNEU · T8E8SCCG · M74M3RFJ · 2CKL96B8 · T72TU8B5 · VG6CIDQW ·
  22JBEZNK · F9JM9CI6
- **Set B (10):** B644HQFS · 6DXZGHD9 · E95T8E88 · 7V7SRG43 · UW2R6BBJ · BAWCBT9R · E3E5YA2E · 5VTAJISY ·
  TF56EPIP · R4WJZBSF
- **Set C (1):** ZUM76CCG (Otten). Designated test case, not a random draw. Confirmed by the arbiter
  (2026-10-04) as a single pilot test; no further members were intended.

## 3. Reconciled points

1. **Set C size — RESOLVED (arbiter, 2026-10-04).** One test, not ten. The record (`calib_sets.json`,
   collection `U65X7JNA`) is complete.
2. **Which set was "co-tagged."** `Theme_Tagging_Calibration.md` §7 names a co-tagging protocol
   (human tags blind, then AI quality assurance) arising **during Set B**, and says all ten Set B papers
   were ultimately co-tagged in that sense. Closeout C5 (2026-10-04) states the **first ten** calibration
   papers were co-tagged and drove the taxonomy, and **Set B was blind and unassisted** (no model tags
   seen). The arbiter's account matches C5 (Set A = co-tagged). Reconciliation: in Set B the AI audited
   the human's recorded tags against the instrument text (rule-level QA) but **proposed no tags**, so
   Set B is model-tag-free; Set A is where tags were developed jointly. Write-ups use C5's framing.
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

> Before the full set was coded, the coding approach was developed in three calibration rounds. In the
> first, 10 randomly selected core studies were tagged by the three models and by the human working
> with Claude; comparing the tags exposed gaps in the vocabulary and unclear definitions, which were
> resolved before the next round. In the second, the human tagged 10 further randomly selected studies
> first, without seeing any model output, creating a human-labeled reference set against which the
> coding instructions were refined and the models' tags were compared. The models together proposed
> 91.6% of the tags the human assigned on this set, and the human added tags at a similar rate in the
> first and second rounds, indicating no detectable anchoring on model output. In the third, a single
> study was used to pilot the production workflow, in which the models tagged first under the frozen
> instructions and the human then reviewed their tags; the full set was coded on that workflow, with
> human review of the model tags throughout. No model was fine-tuned; only the coding instructions and
> vocabulary were refined.
