# Post-Accept Closeout — the single checklist

**Trigger:** the Accept band (44 papers) closes.

**Progress (2026-08-28): 24 of 44 adjudicated · 3 partial · 17 untouched.**
Next alphabetically: **Minh** (`74GE3TF7`). Partials awaiting a pass: `MFSZPSPU` Shi ·
`A6ZE2A26` Ullah · `I6FZ5GD2` Wang (Junpeng) — see B7, and check each for a prior narrow-axis
ruling before re-opening.

This is the consolidated list. Items were previously scattered across `Theme_Tagging_Calibration.md`
§10.12, `Taxonomy_Changelog.md` §120e, and the 2026-08-27/28 sessions. **Work from this file**; the
older lists are kept for their reasoning, not as separate queues.

**Ordering matters.** Section A must complete before Section B, and B before `final:*` is computed in
F. Several C items correct figures that are *currently written up as fact*, so they should not be
quoted anywhere until fixed.

---

## A. Data integrity — do these FIRST, everything downstream depends on them

### A1. Set A v1 → v2.13 supersession ✅ **DONE 2026-08-29**
**Executed** with `slr-tools/supersede_model_run.py --collection JFN8693L --prefix v1
--new-run slr-phase4/data/tags-v213 --commit` after a library backup. **10 items · 233 tags renamed to
`v1_` · 255 written.** Verified: **0 stray old-run tags** in the live namespace across all 10; the
`cal:gemini-fast:*` near-miss preserved as 8 `v1_cal:gemini-fast:` tags with no bare remnant; human
and demote layer **unchanged at 85 tags**; instrument guard **cleared** (was 0.0% match).

**Result — the anchoring contrast is now computable from Zotero**, which was the point:

| Band | Origination |
|---|---|
| Set A (model-first) | **12.7%** *(was a meaningless 54.9% — v1 panel vs v2.13 human layer)* |
| Set B (**blind**) | **9.5%** |

**The blind arm originates LESS than the model-first arm — no anchoring effect detectable.** Retires
the 80.9% artifact and supplies §11.7's replacement claim (closeout **C1**).
Snapshot: `tag_layer_stats_T2prep-b_2026-08-29.json`.

*Original item, kept for the record:*
### A1-original. Set A still holds the v1 model run in Zotero
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

**Apply the §121b ELICITATION TEST — it is much faster and more consistent than "is there a survey":**

> **`survey-input`** = the instrument elicits **stated preferences / adoption / priorities** (findings
> that could become org-survey items).
> **`method-self-report` only** = the instrument measures a **construct or performance** — cognitive
> load, engagement, comprehension, satisfaction, demographics.

**Neither the survey's centrality to the paper nor its usefulness to us is part of the test** (both
were proposed as refinements and withdrawn — see §121b). Worked pair: Catalan `5BAZZWHG` measures
cognitive engagement → **off**; Kang `7UB2MD8Z` asks what developers *want* → **on**. The two facets
**co-occur** freely; they are different axes.

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

### B7. Four Accept-band papers are PARTIALLY tagged — not adjudicated
Discovered 2026-08-28 while checking the band roster. They sit out of alphabetical order with 1–5
human tags each, **no primary theme**, and **19 of 22 modal proposals silent** — the shape of a
targeted earlier write, not an Accept-band pass:

| Paper | key | human tags | silent modals |
|---|---|---|---|
| McAleese, *LLM Critics Help Catch LLM Bugs* | `NRVQT89E` | 2 | 5 |
| Shi, *Towards a HITL framework…* | `MFSZPSPU` | 1 | 5 |
| Ullah, *Vibe coding on trial…* | `A6ZE2A26` | 1 | 5 |
| Wang (Junpeng), *Illuminating LLM coding agents* | `I6FZ5GD2` | 5 | 4 |

**They need a real pass.**

> **CORRECTED 2026-08-28 (arbiter).** An earlier version of this item claimed they *"sit outside the
> alphabetical queue."* **Wrong** — Shi (S), Ullah (U) and Wang (W) all sort **after** the current
> position and will surface normally in the alphabetical walk. **No special scheduling is needed.**
> The actual risk is narrower: when reached, they may look *"already started"* and be waved through.
> Treat each as a **full pass**, and check for a prior narrow-axis ruling first (§126e).
> The only place they stay genuinely invisible is a **query-based** sweep keyed on "no `cal:human`
> tag" — which is why **B8** exists and why the two items are separate.

> **AMENDED 2026-08-28 (§126e). A "partial" may be a DELIBERATE narrow-axis pass, not an unexamined
> paper.** McAleese was worked and closed on 2026-08-28: its two tags turned out to be an adjudicated
> §34/§35 ruling (two evaluation events, one per side of the ladder/method fork) and it sits in the
> retained 21-item gold set. It was examined — on one axis, on purpose — and simply never given a
> theme layer. **Check each remaining partial for a prior narrow-axis ruling BEFORE re-opening it**,
> or a deliberate adjudication may be silently overwritten. Remaining: `MFSZPSPU`, `A6ZE2A26`,
> `I6FZ5GD2`.

**Consequence for C4 — scope the silence reclassification.** Silence means *"lightly scanned, nothing
to discuss"* **only where a pass actually happened**. On these four, silence is genuine **absence**.
Applying the reclassification blanket would convert 19 un-examined modal proposals into weak
endorsements and inflate the panel's apparent precision. **C4 applies to Light Read (and any band
with a completed pass), not to partially-tagged papers.**

### B9. DECIDE: should the human layer fail OPEN or fail CLOSED? (before `final:*`)
Raised by the arbiter 2026-08-28 while reading Parris (`3SU9QZ6F`) on fail-soft behaviour:
*"We've had in HOS (and even **this session**) loads of issues with failing open when we should fail
closed."*

**The three-state convention is a fail-OPEN design.** A panel-modal proposal **stands on silence**
(§10.8), so a tag reaches `final:*` unless someone actively rejects it. **The default is "let it
through."** That is the direct cause of two other closeout items:
- **B3** — `counterpoint` survives on deprecated papers because nobody rejected it individually.
- **B1** — 15 papers carry `oversight-scaling-inversion` on silence, the largest known error source.

**A fail-CLOSED convention** would require an explicit endorsement for any tag to survive. More
expensive, and it would invalidate the non-exhaustive supervised passes (silence would become
rejection, which is *not* what it meant when those bands were worked — see C4).

**The choice was never made deliberately** — it was inherited from the supervised-band workflow.
Options: (a) keep fail-open and rely on the B1/B3 sweeps to clean up; (b) fail-closed for **new**
work only, leaving existing bands under the old rule with the difference documented; (c) fail-closed
for a defined **high-risk subset** (the deprecated vocabulary and the inversion tag), which is
effectively what B1 and B3 already do — in which case make that explicit and general rather than
per-tag firefighting.

**Recommendation: (c)**, then state the rule in §10.8 so the next instrument version inherits a
decision rather than an accident. **Note the reflexivity:** the review is, in miniature, subject to
the pathology it studies — worth a sentence in the methods chapter, under the §11.8 guardrail
(illustration, not evidence).

### B10. `rules-based-checks` re-check — the evaluation must be DETERMINISTIC (§139a)
**Rule (arbiter, 2026-08-28):** *"Rubrics that are LLM evaluated are not rules-based-checks."* The
theme names **how the verdict is produced**, not how the criteria are written. Rule-shaped criteria
scored by a model are `ai-review`.

**Exposure: 24 papers** carry `cal:human:*:theme:rules-based-checks`. **Do not re-open all 24** — most
are plainly deterministic (executable tests, static analysers, constraint verifiers, security gates),
including all three that carry it as **primary** (Parris `3SU9QZ6F`, Töpfer `72W6R4JG`, Xie
`T8E8SCCG`).

**Re-check only where the evaluator is plausibly a model.** Screening question per paper: *does a
model produce the verdict, or does code?* Candidates to look at first — titles suggesting
LLM-based reasoning or agentic review: `5DI9B43K` Sistla · `3ZVMBGPB` Kamalı · `6ZW9QNQH` Mitchell ·
`RX9SICP9` Moreira · `59ZW4R58` Maes · `RPHK78A9` Kim. (Demoted papers carrying it — `WBS9U5N7`,
`27YULT5I`, `N7E3MR2V`, `QWHE9EXH`, `D87A4CAS` — are lower priority under §42.)

**Known hybrid, referred to F2:** **Jin** (`A5WDGC7J`, §120d/§139c) — deterministic test execution
over **GPT-4o-generated** tests. Verdict computed, criteria model-authored. The rule does not settle
it; F2 must decide whether hybrids take both tags, the deterministic one, or a new slug.

**Why it matters:** this is the axis §134b turns on. Deterministic checks and LLM judgements have
different error profiles (Jin 88.74% FPR · Bugdar 24–58% precision · Raghavendra ~46% low-utility vs
checks that either fire or do not). Conflating them erases the corpus's clearest practical result.

### B11. Re-check the hand-applied post-freeze tags — one is a KNOWN ERROR (§142a)
Five post-freeze slugs were applied **by hand, ad hoc**, outside the panel-proposes /
human-adjudicates workflow that governs every other tag in the corpus.

**One has already been found wrong.** `agent-panel` was removed from `I6FZ5GD2` — and the arbiter's
ruling, having read the paper, is that it was an **error**, not a casualty of a changing definition
(*"Consider it a QA correction, not a change"*). There is no panel there under any reading.

**Why it happened (arbiter, 2026-08-29):** these tags were applied *while the slug was being defined*.
**§33** staged both and instructed hand-application *"ahead of a formal graft decision"*; the reference
case did not arrive until Ullah (§140a), ~100 papers later. So the set dates from the window of
**maximum definitional instability** — exactly when errors and genuine boundary cases both cluster.
Necessary at the time; the cost is that the set now needs a look.

**Exposure:** `agent-panel` **7** hand-applied · `cross-model` **5** · `evaluator-reliability` 11 ·
`evaluated-synthetic` 10 · `evaluated-benchmark` 9.

**Do NOT re-open all of them.** The F2 restricted re-run proposes these slugs independently across the
surviving corpus. **Where the panel disagrees with a hand-applied instance, re-examine the HUMAN tag.**
The normal presumption (human is the criterion) is weakened for this specific set — not because the
arbiter is less reliable, but because these tags bypassed the workflow that catches mistakes
everywhere else: no panel proposal to react to, no contrast class in view, no adjudication step.

**Priority:** the 7 `agent-panel` and 5 `cross-model` instances, checked against §140a's discriminator
(*same question + explicit aggregation rule* / *distinct models checking each other, not comparing*).

### B8. Verify every item with NO `cal:human` tag — confirm it was genuinely never examined
**Scott's rule (2026-08-28):** *"we've modified tags on every item, so if there aren't any with human
tags, they are highly unlikely to have been examined."* Every paper that received a pass got **at
least one** human tag written, so **absence of `cal:human:*` is a reliable proxy for "not looked at."**

**Still sweep them to be sure** — it is a cheap query and the whole corpus count depends on it.
As of 2026-08-28: **22 items** carry no human layer at all.

**Note the asymmetry with B7 — the two failure modes are opposite and need different checks:**

| signal | meaning | action |
|---|---|---|
| **no `cal:human` tag** | almost certainly never examined | sweep to confirm (this item) |
| **human tags but no primary** | examined? unclear — a targeted write leaves the same trace | **must re-open individually** (B7) |

A "no human tags" sweep will **not** surface the B7 papers, because they *have* tags. That is exactly
why they stayed invisible until the roster was checked by hand.

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

### D1. `slr-tools/tag_layer_stats.py` — three defects ✅ **FIXED 2026-08-29**
**Done on branch `claude/tag-layer-stats-fix`.** Band split (`JFN8693L` / `IURU9UTA`, merged
`46QVUN7N` no longer used and named as do-not-use), correct blind-arm labelling, demote/tier stats,
**primary-based completeness predicate** (partial and untouched now reported separately), and a new
**`instrument_check()` guard** that compares each band's Zotero model layer against the current
instrument JSON. On first run it **immediately flagged Set A at 0.0% match** — the v1-run trap that
produced the bogus 80.9%. Superseded `v1_cal:` tags are excluded by the anchored regex and counted.
First corrected snapshot: `tag_layer_stats_T1b_2026-08-29.json`.

**T0 and T1 snapshots are retained unchanged** (layered-history rule) but **carry the artifactual
calibration figures** — do not quote them; use T1b or later.

*Original defect list, kept for the record:*
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
- **E8. Google Scholar citation retrieval — DECIDED but not executed.**
  `Selection_Criteria_By_Phase.md` §394 signal #1: manually retrieve GS counts, with Semantic Scholar
  as the reproducible cross-check. **SCOPE (arbiter, 2026-08-28): run on the SURVIVORS only** — the
  Phase 6 set (reviewed, no `demote:context`), not the whole corpus. Demoted papers are not being
  defended in the write-up, so they do not need counts. This makes the manual effort tractable:
  ~75–80 papers rather than ~150. Not started; **first instance
  recorded 2026-08-28** on `N7E3MR2V` (Citegeist **0** vs GS **2**), which is the discrepancy the
  decision exists to catch.
  - **Storage convention:** `GS.citedByCount:` / `GS.retrieved:` in the Zotero `extra` field,
    **alongside** the `Citegeist.*` fields, never replacing them.
  - **Mandatory methods-chapter obligations** (all five, from §394): record the retrieval date with
    every count · state that GS is not API-accessible and automated retrieval is against its terms,
    hence manual · state what GS counts include (preprints, theses, non-refereed citing sources) ·
    report the S2 count alongside and **state the discrepancy rather than choosing the flattering
    number** · keep provenance inspectable.
  - **Why it matters:** existing Citegeist/OpenAlex enrichment covers only **23 of 79** Light Read
    papers and fails **systematically on SSRN** — the stream most in need of defending. Zhu
    (`ZGST9CY6`) has **15 GS citations and no Citegeist record at all**.
  - **Constraint:** this is for **defending** the corpus in the methods chapter, **not re-filtering
    it**. Counts are uninformative in a corpus that is 77% 2025–26 — *"uninformative, not damning"*.

- **E9. Decide whether authority signals #2–#8 are adopted** (`Selection_Criteria_By_Phase.md` §394).
  Only #1 is decided. Standing ruling (§132b, 2026-08-28): **credibility of authorship is A factor,
  not THE factor** — legitimate as qualitative input to a holistic assessment (it is already one of
  the four Garousi criteria), **not** as a sole ground and **never** as a retroactive re-filter
  (HARKing). If any of #2–#8 is to bear on the write-up, decide it and apply it **uniformly**.

- **E7. Confirm the untracked dir** `Scalable AI Coding Governance - 2026-08-27 - Light Reads
  Completed/` should stay untracked. **Repo is PUBLIC** — never commit paper full texts.

---

## F. Forward work — after A–E

### F1. Compute `final:*`
`final:* = panel modal ∪ human endorsements − human rejections − deprecated vocabulary` (§101a).
**Blocked on all of Section B.**

### F2-PREP. Restricted re-run spec — DRAFTED, awaiting 4 decisions
`slr-phase4/Restricted_Rerun_Spec.md` (2026-08-28). **Prep only, not authorised to run.**

**Design settled:** restricted **output**, discriminative **context** — the prompt admits only the 9
new slugs, but carries for each the neighbours it must be distinguished from, the discriminator test,
and the Accept-band worked cases. A bare new-slug list would over-apply (the error corrected 5× on
`agent-panel`, 4× on `cross-model`); the full revised instrument would invite re-adjudication of old
tags. Old tags are unreachable **by schema**, not by instruction.

**Population: 72** — 68 kept (primary present, no demote) + the 4 remaining (`MFSZPSPU`, `GAD5Z8PV`,
`I6FZ5GD2`, `CTGGMIX9`). TXT available for all 72.

**Blocked on D1 (coin `evaluated-self-demo`?) · D2 (re-run revised `survey-input`/`rules-based-checks`,
or keep as human re-checks B2/B10?) · D3 (kept-only or + Context?) · D4 (confirm 3×k=3, fable
excluded).** Also blocked on **D1 tooling** — `tag_layer_stats.py` must be fixed before T2 is
recorded, or T2 inherits the T0/T1 band defects.

### F2a. `evaluated-real-data` — definition SETTLED (2026-08-28), ready to graft

Scott's formulation, which is the definition of record:

> *"In **real-data**, a **tool is developed** and that tool is **evaluated using real data**. Tool could
> be a pipeline. In **mining**, **pre-existing data is mined for insights. No new tool is being
> evaluated**."*

**The discriminator is: is there a developed artifact under evaluation?**

| | artifact built? | evidence source | tag |
|---|---|---|---|
| `evaluated-real-data` | **yes** — tool or pipeline | real production data | the artifact was proven outside a benchmark |
| `method-mining` | **no** | pre-existing artifacts | the study characterises the world |
| `evaluated-benchmark` | (either) | a standard benchmark | measured **against** an accepted benchmark (§119b) |

**Entailment to enforce at grafting: `evaluated-real-data` ⇒ `built-system`.** If nothing was built,
the tag cannot apply. Worth a consistency check in the tooling.

**Why the scoping matters:** written as a general "real data" marker it fires on every mining paper in
the corpus and carries no information (mining **is** real data by definition — §125d). Scoped to a
built artifact it marks a genuine, currently unmarked rung: *proven on production data rather than on
a benchmark or a synthetic corpus.*

**Candidate seeds** (all deferred rather than tagged, so first use lands deliberately):
Karakaya `5NZ2EDEK` (§122f) · Liu `6ZC3H7AF` · Lipsanen `7SH86C2W` (§124d).
**Not** Liu `9H6FWJME` — pure mining, no tool (§125d).

**Related open rung — `evaluated-self-demo`** (§124d): the proposers qualitatively judging their own
artifact on a case they built. Weakest evidence there is, common in this literature, currently
unmarked; `built-system` says only that the thing exists.

### F2. Next versioned instrument cut (§41) + restricted re-run
Graft: `scaling-dissent` · the `evaluated-*` ladder · `agent-panel` · `cross-model` ·
`evaluator-reliability` · `evaluated-real-data` · **`oversight-scaling-inversion` v2 (its own slug —
never reuse, or two constructs merge silently in `final:*`)** · corrected `survey-input` text ·
§88 leakage-first rewording. Also fold in the `rules-based-checks` hybrid question from §120d
(deterministic adjudication over **LLM-generated** inputs).

Running v1 and v2 of the inversion makes the reclassification delta a **reportable measurement** of
how far definitional wording drives tagger behaviour.

### F3. Materialise Phase 6
The surviving set. **Predicate: `cal:human:primary:theme:*` present AND no `demote:context`.**

**Use the PRIMARY, not "any `cal:human` tag."** Two weaker predicates are both wrong:
- *"absent `demote:context` = surviving"* — sweeps in the 22 papers never looked at.
- *"any `cal:human` tag = reviewed"* — sweeps in **partially-tagged** papers (see B7). A targeted
  earlier write (one `evaluated-*` facet, say) leaves a human tag behind without an adjudication.

**Every properly adjudicated paper carries a primary theme**; partial writes do not. That is the only
reliable completeness signal in the data.

**Corrected projection, 2026-08-28** — supersedes an earlier 149/64/63 count that used the loose
predicate *and* pulled Otten (`ZUM76CCG`) in through the mis-scoped `46QVUN7N` (A3):

| | n |
|---|---|
| unique papers in tagging review | **148** |
| **surviving** (primary, not demoted) | **60** |
| demoted | 62 |
| **partial** (human tags, no primary) | **4** |
| untouched | 22 |

At Accept's current demote rate, Phase 6 lands near **75–80**.

### F5. GAP ASSESSMENT → targeted supplementary search (AFTER F1 + F2)
**Arbiter's sequencing (2026-08-28):** *"What we should look at is what these papers cover. First
question — **do they close gaps**? Then if so, we figure out a strategy to look for papers on those
specific gaps. Let's do that after we finish the tagging including applying the new tags. **We will
first assess whether we have a gap** after that."*

**Why this ordering matters methodologically.** The alternative — reviewing excluded papers because
they were machine-discarded, or because they surfaced in a citation while reading — makes the
selection rule *"papers I noticed."* That is the HARKing problem in §394's design constraints. A
**gap-driven** search takes its selection rule from **what the synthesis cannot answer**, which is
defensible, reportable, and reproducible.

**Sequence (do not start early):**
1. **F1** `final:*` computed · **F2** instrument cut + restricted re-run applied.
2. **Assess coverage.** Which themes/facets are thin or empty? Which questions does the corpus fail
   to answer? Only claims the synthesis actually needs count as gaps.
3. **Only if a gap exists**, define a targeted search **for that gap**, stated before looking.
4. **Search sources, in order:** (i) the **machine-only discard pool** — 2,389 `source:snowball`
   items excluded at title/abstract by machine with **no human screening tag**, filterable by
   `cocite:` (≥3 → 53 items · ≥2 → 197); (ii) fresh database queries; (iii) forward citation from
   Core papers.
5. **Record as a new layer** — a `Reconsider` collection (never edit `03-Discard`; phase-freeze) and
   a new `s4:human:*` tag rather than revising `s1:`. **Report in PRISMA**: original exclusions and
   any reinstatements, with reasons.

**Candidate gaps already accumulated during the Accept band** — the starting list for step 2, not a
commitment that any is real:

| Gap | Recorded | Status |
|---|---|---|
| **`agent-panel` reference architectures** — MetaGPT, ChatDev, AgentCoder are the canonical multi-agent SE systems and are all machine-discarded; needed to *distinguish* panel from division of labour | §130b, §135c | likely needed for the F2 definition even if not re-admitted |
| **Relay error compounding** — does error amplify across sequential agents, and at what rate? | §135c | **no corpus paper measures it** |
| **Agents as negotiators** — capacity to take critique and converge, vs as producers/reviewers | §127c | unaddressed |
| **Commitment side** — estimation, work breakdown, capacity planning under agentic delivery | §132c | unaddressed; may need out-of-corpus sources |
| **Certified-registry revocation** — what happens when a certified artifact is later found vulnerable | Liu `6ZC3H7AF` | unaddressed |
| **Allocation rules** (as against configuration performance) | §126b, §127a | thin — Minh only |
| Mode convergence (assistive ≡ agentic failure profile) | §119c | **CLOSED** by Liu `9H6FWJME` (§125a) |

### F6. Process-integrity items, independent of any gap
Small, defined populations — worth doing regardless of whether a gap is found, because they are
records where the review's own rules were not applied, not judgements about scope.

- **8 records carry a human KEEP that a machine later discarded.** The human is the criterion in this
  project; an unreviewed machine reversal of a human keep is the one combination the layered-history
  rule (§548) does not sanction. Includes **Karpathy `Z4IKFZJ4`** — *"There's a new kind of coding I
  call vibecoding"*, the **origin of the term this review is about**; **Pappu `2XV8ZVM8`** —
  *"Multi-agent teams hold experts back"*, a possible `scaling-dissent` counter-finding; plus
  `D3ZU22JC` Dong, `Y9G3DA92` Imai, `UG5D8G6U` Alenezi, `EN5DT6ZJ` J. Wang, `6NR73DTR` Li,
  `MBKP4DCY` Liang. **Review all 8**; a complete population is not cherry-picking.
- **AgentCoder is duplicated and unlinked** — `G3FF4MDW` (snowball, discarded) and `WWDHF6EU`
  (retrieval, sitting in `03 - Queue`), with **no `superseded-by:`/`supersedes:` between them** and
  contradictory dispositions. Breaks the one-record-per-study rule. Merge per the dedupe convention.

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
