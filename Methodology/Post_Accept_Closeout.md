# Post-Accept Closeout — the single checklist

**Trigger:** the Accept band (44 papers) closes. **22 of 44 reviewed as of 2026-08-28**; next paper
alphabetically is **Kaur**.

This is the consolidated list. Items were previously scattered across `Theme_Tagging_Calibration.md`
§10.12, `Taxonomy_Changelog.md` §120e, and the 2026-08-27/28 sessions. **Work from this file**; the
older lists are kept for their reasoning, not as separate queues.

**Ordering matters.** Section A must complete before Section B, and B before `final:*` is computed in
F. Several C items correct figures that are *currently written up as fact*, so they should not be
quoted anywhere until fixed.

---

## A. Data integrity — do these FIRST, everything downstream depends on them

### A1. Set A still holds the v1 model run in Zotero ⚠️ **highest priority**
`01-AI Calibration Run` [JFN8693L], all 10 papers. Complete 3-vendor **v2.13** data exists on disk
(`slr-phase4/data/tags-v213/{opus,codex,gemini}/`) and was never written back. The v2.13 re-run
happened *because* the instrument evolved (calibration doc §5: *"Set A re-run included because the
instrument evolved substantially"*).

- **Method (Scott's ruling, 2026-08-28):** **rename, never delete.** Prefix superseded tags with
  `v1_` (`cal:opus:theme:X` → `v1_cal:opus:theme:X`), *then* write v2.13 in the bare `cal:` form.
  The prefix falls outside the `cal:` regex the stats tooling matches, so the old run leaves the
  figures with no code change while staying queryable in Zotero.
- **Never** write the new run alongside the old un-prefixed — same prefix ⇒ silent union of two
  instruments ⇒ every band statistic corrupted.
- **Until this is done, any Zotero-derived figure for Set A is meaningless** — it measures a v1 panel
  against a v2.13-aligned human layer (computes ~54.9% origination; true value ~10.6%).
- Rule recorded in `SLR_Methodology_Bootstrap.md` §3 and the `slr-conventions` skill.
- **Set B** [IURU9UTA] was written 2026-08-28 and is correct — it has no prior run, so it needs nothing.

### A2. Build the tag-rename tool
The Zotero CLI has `tag-add` but **no rename and no remove**; A1 needs a raw version-guarded PATCH
(`If-Unmodified-Since-Version`) across ~300 tags on 10 items. Build it as a reusable script — the
same operation recurs at **every** future instrument revision, not just this one.

### A3. `04 - Calibration (Adjudicated)` [46QVUN7N] is mis-scoped
It is **not** Set A ∪ Set B: it **drops** Momcilovic (`M74M3RFJ`, Set A) and **adds** Otten
(`ZUM76CCG`, the Set C pilot). Either fix the membership or document it — but **stop using it as the
calibration band in tooling** either way (see D1). Note the phase-freeze rule: if this collection is
already "populated and frozen," the correct fix is a **new** collection, not an edit.

---

## B. Corpus-level tag corrections — all before `final:*` is computed

### B1. `oversight-scaling-inversion` re-check — **largest known single source of tag error**
15 papers carry it on arbiter silence. 4 of 10 examined cases were rejected, and the §88 leakage test
raises the bar further. Includes **Ghammam** per §117d. The v2 re-run (F2) resolves much of it
automatically **provided v2 gets its own slug**.

### B2. `survey-input` re-check (~10 silent-modal instances)
§116a narrowed it to papers containing an actual **user survey** (Likert-type instrument). Self-report
is the *genus* (questionnaires, interviews, focus groups, diaries); survey is one *species*. Scott has
been enforcing the narrow lens on everything he ruled explicitly, so exposure is only the silent
modals.

### B3. Deprecated-tag sweep — `counterpoint` (§56)
Survives into `final:*` on any paper where it was modal and never rejected, because silence lets a
modal proposal stand. **Do it as one bulk auditable act**, not per paper. Note §101a already excludes
deprecated vocabulary at the `final:*` computation step — confirm the sweep and the exclusion don't
double-count.

### B4. §34 misread — re-check §77, §97, §99b
§119a established that §34 does **not** bar ladder/method co-occurrence (the **world-or-tool test**
governs). Three earlier rulings cited the misreading and need revisiting.

### B5. Demote decisions needing a second look (4 papers)
The panel's tier judgement is weak (see C3), and these are the least-corroborated calls:

| Paper | Set | panel | human | why flagged |
|---|---|---|---|---|
| De La Cruz (`E3E5YA2E`) | B | **0/3** | demote | no panel signal at all |
| Navneet (`TF56EPIP`) | B | **0/3** | demote | no panel signal at all |
| Sudarsan (`UW2R6BBJ`) | B | **3/3** | keep | kept against unanimity (§30 exception — verify it still holds) |
| Jin (`UDVHQ5HR`) | A | **0/3** | demote | Set A parallel case |

`BAWCBT9R` (2/3, demoted) is corroborated twice over — **leave it**. `M74M3RFJ` and `2CKL96B8` have
panel agreement; `VG6CIDQW` at 1/3 is noise.

### B6. Model `demote:context` flags have no home in Zotero
5 records across `BAWCBT9R` and `UW2R6BBJ` (and any others surfaced by A1). The `cal:` namespace has
**no flag form** — Light Read encodes only `primary`/`theme`/`facet`. Either define a form
(e.g. `cal:<model>:flag:demote-context`) or record deliberately that model flags live only in the
JSON. **Decide, don't leave implicit.**

---

## C. Methodology write-ups — these correct figures currently stated as FACT

> Everything in this section is a **correction to something already written up**. Until done, the
> affected numbers should not be quoted in the dissertation, a paper, or a talk.

### C1. §11.7 — retire the 80.9% origination figure ⚠️ **it is an artifact**
`tag_layer_stats.py` reads the Zotero tag layer, but **Set B had no model tags in Zotero** until
2026-08-28. With an empty comparator every human tag counted as "originated," so Set B computed as
**100%**; blended with Set A it produced the reported **80.9%**.

**Replace with the corrected contrast.** Set A vs Set B is the **only clean anchoring comparison** —
same arbiter, same instrument, same exhaustive protocol, same era, differing *solely* in whether model
tags were visible:

| Band | protocol | originated |
|---|---|---|
| Set A — AI Calibration | model-first, exhaustive | **10.6%** |
| Set B — Human Calibration | **blind**, exhaustive | **8.4%** |
| Light Read | supervised, non-exhaustive | 7.7% |

**No anchoring effect is detectable** (blind originates *slightly less*; n=10 each, so noise).

**Retire the Light Read comparison as a control** rather than reinterpreting it — it is confounded
three ways: non-exhaustive by design, vocabulary still growing under it, and the confirmation protocol
drifted mid-band (C4). On comparable vocabulary only it reads 3.5% vs Set B's 8.4%, which *looks* like
a 2.4× anchoring effect and is not one.

### C2. §11.7 — remove the "~96% panel recall" claim
It is read off the supervised bands' origination rate. But Scott was **not** hunting exhaustively for
misses there, so a low origination rate cannot distinguish *"the panel missed nothing"* from
*"nobody went looking."*

**Recall is only estimable from the exhaustive calibration arms:** Set A 59/66 = **89.4%**, Set B
76/83 = **91.6%**. Headline **Set B (~90%, n=10)** — a blind arbiter cannot have been anchored into
agreement.

### C3. **NEW** — split tag recall from tier recall
The panel is a **decent tagger and a poor triager**, and one number has been standing for both:

| axis | recall |
|---|---|
| tags (Set B, blind, exhaustive) | **~90%** |
| **tier / demote** (all bands, n=125) | **57.4%** |

Panel gives *no signal* on **42.6%** of Scott's demotes (26 of 61). Tier precision 71.4%. Report
separately and never let the tag figure speak for the tier one.

**Sub-item — the Accept band row belongs in §11.3's frame, not §11.5's headline.** On the band the
models were most confident about: **22 reviewed, 0 model flags, 7 human demotes (32%)**. Because the
band was *constituted* by model confidence, this measures the abandoned confidence gate **on its own
exemption band**. Place it as **further detection** in §11.3's sense (*"the flaw was present at design
time; the errors were its detection, not its cause"*) — the decision was principled and predates the
measurement. It completes the tier-error picture in both directions, where §11.4 had only one side:

- **Eze (`9MV2IVNU`)** — panel 9/9 demote, arbiter kept → panel **over**-demotes *(documented)*
- **Accept band** — panel 0/22 flags, arbiter demoted 7 → panel **under**-demotes *(new)*

Recompute at band close; the 32% will move.

### C4. §10.8 / §11.5 — silence is a **weak endorsement**, not "unexamined"
Scott (2026-08-28): in Light Read, silence means *"did not need big discussion"* — tags were **lightly
scanned and inconsistencies discussed/updated**. §11.5 currently labels the 98 silent proposals
*"stands on modality,"* which reads as passing through unexamined. Reclassifying ~19% of Light Read
verdicts **improves** the panel's apparent precision:

> panel modal proposals meeting the human layer = **439 endorsed + 99 scanned-clean + 52 overturned**
> ⇒ **~91% survived human contact**, 8.8% overturned.

**Keep the two senses distinct** — this is the reconciliation with *"omission ≠ rejection"*:
- silence on a **proposal** = scanned, no objection → weak endorsement
- a tag never **originated** = not exhaustively hunted → **no signal**

**Also record the protocol drift:** Light Read *began* by explicitly confirming a subset of tags and
*moved* to confirming all of them. The band is therefore **not homogeneous** — early papers carry
silence by protocol, later ones by judgement. Relevant to the re-run (F2): a new-element proposal
landing on an early paper meets a thinner human layer, so **early papers deserve the closer look**.

### C5. §11.6b — Set B answers the open question
§11.6b (written 2026-08-28) flags as unresolved whether the blind calibration band was also
*unassisted*. **It was**: first ten co-tagged (and drove taxonomy revisions), **next ten blind**. So
there **is** an unassisted arm, **n=10** — it is the *supervised* bands that have none.

### C6. §11.9 / §41 — restricted re-run scope + a falsifiable prediction
Scope: re-run models on the **new vocabulary elements only**, not revisiting old rulings, plus quick
validation of anything that pops. That isolates the instrument as the variable.

**Record the prediction BEFORE the run so it cannot be rationalised afterwards:** 22 of Light Read's
40 originations used post-freeze slugs the panel could not propose. If the frozen instrument was the
binding constraint rather than panel recall, **those should largely collapse, taking Light Read
origination from 7.7% → ~3.5%.** If it does not collapse, the gap was the panel.

### C7. Fable — record the design history
Intended as a **tiebreaker on model disagreement**; superseded by **k=3 runs of all three vendors**.
Repeated sampling of every vendor measures intra-rater reliability, where a tiebreaker only ever cast
a deciding vote on contested items. **Principle to state generally: panel composition must be uniform
across the corpus — a vendor run on a subset cannot enter the statistics.** (Fable data exists for 5
of 10 Set B papers and was deliberately **not** written.) Fable also stays gated on explicit per-run
permission.

### C8. Full Read band is 6-for-6 demoted
Nothing survived the deepest reading protocol. Probably correct if Full Read was reserved for
borderline cases — but a band with a **100% demote rate** needs one sentence in the methods chapter,
or it reads as a protocol that could not pass anything.

### C9. Changelog §121 — the whole correction as one entry
Cover: the Set B model-tag write, the 80.9% artifact and its cause, the corrected A-vs-B contrast,
the recall split, the silence reclassification, and the Light Read protocol drift.

---

## D. Tooling

### D1. `slr-tools/tag_layer_stats.py` — three defects
1. **Wrong source for calibration.** Reads Zotero; Set B's panel output lived only in
   `slr-phase4/data/tags-v213/`. Fixed for Set B by the 2026-08-28 write, but the script should read
   the JSON for calibration bands regardless, or assert that Zotero coverage exists.
2. **Wrong membership.** Uses `46QVUN7N` (see A3). Should use **`JFN8693L` and `IURU9UTA` split**,
   never merged — they are different protocols and must never share a row.
3. **Wrong label.** Calls the whole band *"blind-first"*; only Set B is blind.

Also add: **demote-tag reading**, so tier recall (C3) is computed rather than hand-rolled.

### D2. Regenerate T0 / T1 snapshots on the fixed script
T0 is frozen at `slr-phase4/data/tags-v213/tag_layer_stats_T0_2026-08-26.json`. Both current snapshots
carry the artifactual calibration figures. **Keep the originals** (provenance) and regenerate
alongside — same principle as A1.

---

## E. Records, bibliographic, housekeeping

- **E1. SSRN item types + published-version check** — 12 items. OpenAlex → Semantic Scholar. If a
  journal version is found post-search, tag `source:retrieval` and **do not inflate the count**.
- **E2. Dissertation Queue hygiene** — `03 - Queue` [4PE2T47Q] vs `01 - Primary` [WVZFNSEC]:
  **16 of 21** Primary members were removed from Queue, **5 were not** (Jin included, added
  2026-08-28). Settle whether promotion removes from Queue and sweep the 6. *Distinct from the
  phase-collection freeze rule — the Dissertation folder is a working triage, not a phase record.*
- **E3. Back-fill named-use rationales** on Dissertation Supporting members (§109a criterion, extended
  prospectively at §112b).
- **E4. Back-fill the Validation Apparatus harvest** from the Light Read band — candidates listed at
  the foot of `Validation_Apparatus_Harvest.md`: `72W6R4JG` Töpfer · `TA6GIUK2` Zietsman ·
  `96XE669R` Zhong · `VZ27QUPQ` Zhuo (**§51 disqualifier — reference-grounded**) · `T2EG4BE2` Waseem.
- **E5. Choose the "oversight fails at scale" anchor** — Gao vs Branco — and **place Branco** in a
  dissertation collection.
- **E6. Verify the dissertation-queue records** created for Du / Huang / Islam (the agent-checks-agent
  gap, surfaced via Gemini and deliberately **not** added to the corpus).
- **E7. Confirm the untracked dir** `Scalable AI Coding Governance - 2026-08-27 - Light Reads
  Completed/` should stay untracked. **Repo is PUBLIC** — never commit paper full texts.

---

## F. Forward work — after A–E

### F1. Compute `final:*`
`final:* = panel modal ∪ human endorsements − human rejections − deprecated vocabulary` (§101a).
**Blocked on all of Section B.**

### F2. Next versioned instrument cut (§41) + restricted re-run
Graft: `scaling-dissent` · the `evaluated-*` ladder · `agent-panel` · `cross-model` ·
`evaluator-reliability` · `evaluated-real-data` · **`oversight-scaling-inversion` v2 (its own slug —
never reuse, or two constructs merge silently in `final:*`)** · corrected `survey-input` text ·
§88 leakage-first rewording. Also fold in the `rules-based-checks` hybrid question from §120d
(deterministic adjudication over **LLM-generated** inputs).

Running v1 and v2 of the inversion makes the reclassification delta a **reportable measurement** of
how far definitional wording drives tagger behaviour.

### F3. Materialise Phase 6
The surviving set. **Predicate: reviewed AND not demoted** — `cal:human:*` present **and** no
`demote:context`. *"Absent = surviving" alone is wrong* — it sweeps in unreviewed papers.

Projected as of 2026-08-28: **149 unique papers in tagging review · 127 reviewed · 64 surviving ·
63 demoted · 22 remaining.** At Accept's current 32% demote rate, Phase 6 lands near **79**.

### F4. HOS audit → survey question bank
`Methodology/Survey_Instrument_Design.md`. Mine `~/Code/Thurlow-Research/HumanOversightSystem/Human`
for questions informed by HOS **and** the SLR findings. 13 survey hooks already banked. HOS path is
recorded but **deliberately unread** so far. Survey call-for-participants stays held until **after
candidacy**.

---

## Guardrails that apply to every item here

- **Nothing is deleted.** Collections freeze after population; superseded model runs get a `v1_`
  prefix. See `SLR_Methodology_Bootstrap.md` §3.
- **Zotero writes need a library backup first**, and use `ZOTERO_API_KEY_RW`.
- **All assistant changes land via PR**; Scott reviews and merges.
- **Repo is PUBLIC** — secret-scan staged content; never commit `slr-phase4/txt/`, `Backups/`,
  `Downloads/`, `.envrc`, or PDFs.
