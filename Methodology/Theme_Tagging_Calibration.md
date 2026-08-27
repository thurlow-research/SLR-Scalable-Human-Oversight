# Theme-Tagging Calibration — Design & Findings

**Vibe Coding Governance SLR · methodology + results record**
**Started:** 2026-07-14 · Status (2026-07-18 EOD): **validation cycle complete; GATE = PASS
(Scott, 2026-07-18); instrument frozen v2.1+altitude; Set A human tags fully reconciled in Zotero;
next = Scott tags Set B blind (Set B remains model-free until then)**

Purpose: before applying the 16-theme controlled vocabulary (see `Emerging_Themes.md` → *Tag
reference*) to all 149 cores, establish **tagging reliability** on a small calibrated sample —
cross-model agreement first, then human-vs-model. This mirrors the Stage-3 cross-model QA approach
(κ, human-confirm) but for a *different task*: multi-label theme assignment rather than keep/discard
screening, so calibration is re-established from scratch.

---

## 1. Design

**Sample.** 20 cores drawn at random (Python `random.seed(714)`, reproducible) from the 149-item
Core set, split into two disjoint sets of 10:
- **Set A — "01-AI Calibration Run"** (Zotero collection `JFN8693L`): tagged by 3 models →
  cross-*model* agreement + worked examples.
- **Set B — "02-Human Calibration Run"** (Zotero collection `IURU9UTA`): **Scott tags first, blind**,
  then the 3 models → human-vs-model agreement. (Blind-first preserves an unbiased human baseline.)

| Set A (`JFN8693L`) | Set B (`IURU9UTA`) |
|---|---|
| UB2EVUFU UDVHQ5HR Z8TPRNEU T8E8SCCG M74M3RFJ | B644HQFS 6DXZGHD9 E95T8E88 7V7SRG43 UW2R6BBJ |
| 2CKL96B8 T72TU8B5 VG6CIDQW 22JBEZNK F9JM9CI6 | BAWCBT9R E3E5YA2E 5VTAJISY TF56EPIP R4WJZBSF |

**Taggers (three distinct frontier families, top reasoning tier).**
| Label | Model | How run |
|---|---|---|
| `opus` | Claude Opus (this assistant) | 5 subagents, 2 papers each, full-text read |
| `fable` | Claude Fable 5 | 5 subagents (`model:fable`), 2 papers each, full-text read (added 2026-07-14) |
| `codex` | `gpt-5.6-sol` (OpenAI) | `codex exec --skip-git-repo-check -c model_reasoning_effort=high` |
| `gemini` | Gemini 3.1 Pro (High), via `agy` | `agy -p … --model "Gemini 3.1 Pro (High)"` |

Deliberately three *different* vendors (not `agy`'s Claude option, which would duplicate Opus; not
Gemini Flash, which is not Opus-equivalent).

**Input.** **Full document text** (child TXT attachments, 2k–32k words each) — per Scott, tagging is
on document contents, not title/abstract. All 20 items had both PDF + TXT.

**Instrument.** Identical vocabulary cheat-sheet + prompt for every tagger (`TAG_CHEATSHEET.md`,
`model_prompt_prefix.txt`). Each tagger returns, per paper: one **primary** theme, all **theme**
memberships (multi-label, on *membership not mention*), any **facet** tags, and a ≤12-word rationale
per tag. Output = strict JSON.

**Tag scheme in Zotero (source-encoded so all taggers coexist on one item, fully reversible via the
`cal:` prefix):**
- `cal:<model>:theme:<slug>` — each theme membership (explicit `theme:` marker added 2026-07-15, so it
  strip-maps to the final `theme:<slug>` convention)
- `cal:<model>:primary:theme:<slug>` — the single primary theme (same `theme:<slug>` tail as the
  membership tag, with `primary:` prepended — consistent schema)
- `cal:<model>:facet:<slug>` — each facet
- `demote:<state>` (plain, not source-encoded) — transient re-scope flag, e.g. `demote:context`: this
  core looks like it belongs in another disposition; batch-reviewed then moved + flag removed.
- `cal:human:theme:<slug>` / `cal:human:primary:theme:<slug>` / `cal:human:facet:<slug>` — the
  arbiter's working judgment; can be revised mid-review.
- `cal:human:reject:theme:<slug>` / `cal:human:reject:facet:<slug>` — **RATIFIED 2026-08-23
  (changelog §46).** An explicit arbiter rejection of a panel proposal: *"I considered this and it
  does not apply."* Needed because arbiter tagging is **non-exhaustive** — an omission means "didn't
  jump out," not "rejected," so the two must be distinguishable. Semantics of the human layer are
  therefore: **endorsement (`cal:human:theme|facet:*`, additive) · rejection
  (`cal:human:reject:*`) · silence (not considered — panel proposal stands)**. The final write pass
  computes **panel modal ∪ endorsements − rejections**. Primary is exempt (single-valued —
  `cal:human:primary:theme:*` simply replaces the machine's). Rejections are part of the permanent
  audit trail and, like the rest of `cal:human:*`, are never stripped; they do not themselves become
  `final:*` tags — they *subtract* from what does. First instances: `WUUDHL8R`
  (`reject:theme:regulatory-compliance`, `reject:theme:hitl-workflow`).

**Final-tag convention — RATIFIED 2026-08-21 (supersedes the "plain `theme:<slug>`" plan above,
which was never executed).** Two things forced a decision: (1) Scott's standing principle that
**Zotero is the sole source of truth — all data lives in Zotero**, including the per-model
proposals (not just the human-adjudicated set), so the panel's individual votes get written to
Zotero for every sweep paper, not left only in `sweep_triage_final.json`/the workbook; (2) a bare
`theme:<slug>` namespace turned out to already be live — 3 legacy tags (`theme:tooling`,
`theme:oversight`, `theme:vibe-coding`) from an unrelated Phase-1 topic-bucket system predate the
v2.13 instrument, so "final = plain, unprefixed" would collide. Decision:
- `cal:<model>:*` (opus/codex/gemini/+fable tie-breaks) — per-model proposals, as above, extended
  to all 128 sweep papers (data already exists: `slr-phase4/data/tags-v213/{opus,codex,gemini}/`).
- `cal:human:*` — the arbiter's working pass, as above. **Kept permanently, not stripped** —
  Scott's call: the SLR needs a full audit trail/provenance, not just a locked final value.
- **`final:theme:<slug>` / `final:primary:theme:<slug>` / `final:facet:<slug>`** (new, prefixed
  — not bare) — the locked, reportable copy. Written once, at paper closeout (same moment as
  `s5:read`), by copying whatever `cal:human:*` holds at that instant. **Stats/reporting queries
  run against `final:*` only** — an in-progress `cal:human:*` edit never contaminates a report
  mid-review. All three layers coexist permanently: `cal:<model>:*` = what the panel proposed,
  `cal:human:*` = the arbiter's working record, `final:*` = the locked value used for reporting.

**Tooling** (now under `slr-phase4/tools/`; scripts are resumable/idempotent): `run_cli.sh`
(codex+gemini loop with per-call `timeout 300` + JSON salvage), Opus subagents, `write_tags.py`
(additive/replace-mode PATCH with `If-Unmodified-Since-Version`; reads `ZOTERO_API_KEY_RW` for writes,
falls back to `ZOTERO_API_KEY`). Model outputs kept as per-tagger JSON files (`data/tags/<model>/<key>.json`)
→ comparison; no plain `theme:` writes during calibration.

**Process notes / lessons (for the full run):** (1) don't double-background (`nohup … &` inside a
background call spawned racing runners); run one tracked process. (2) Concurrent writers can
concatenate two JSON objects into one file — normalize each file to its first valid object
(`json.JSONDecoder().raw_decode`) before parsing. (3) `agy`/`codex` occasionally emit empty output on
a long paper; the idempotent `[ ! -s ]` guard + re-run fills gaps. (4) Zotero PATCH returns 204 with
an empty body — don't `json.loads` it.

---

## 2. What we did

- Drew the sample, populated the two Zotero collections (additive collection membership).
- Downloaded the 20 TXT full-texts.
- Tagged **Set A** with all three models on full text; wrote 30 source-encoded tag sets to the
  `01-AI Calibration Run` items in Zotero.
- Computed cross-model agreement (below).
- Delivered Scott a self-contained **Set B human-tagging packet** (`SETB_PACKET_FULL.md`).
- **Froze the instrument** pending Set B (see §4 decision).

---

## 3. What we observed — Set A cross-model agreement (n=10)

### 3.1 Primary "home" theme — highly reliable
Unanimous **9/10**. Pairwise primary match: **codex–gemini 10/10, opus–codex 9/10, opus–gemini 9/10.**

| key | opus | codex | gemini |
|---|---|---|---|
| UB2EVUFU | **hitl-workflow** | ai-review | ai-review |
| UDVHQ5HR | ai-review | ai-review | ai-review |
| Z8TPRNEU | hitl-workflow | hitl-workflow | hitl-workflow |
| T8E8SCCG | rules-based-checks | rules-based-checks | rules-based-checks |
| M74M3RFJ | regulatory-compliance | regulatory-compliance | regulatory-compliance |
| 2CKL96B8 | ai-code-insecurity | ai-code-insecurity | ai-code-insecurity |
| T72TU8B5 | risk-routing | risk-routing | risk-routing |
| VG6CIDQW | hitl-workflow | hitl-workflow | hitl-workflow |
| 22JBEZNK | automation-bias | automation-bias | automation-bias |
| F9JM9CI6 | hitl-workflow | hitl-workflow | hitl-workflow |

The lone disagreement (`UB2EVUFU`) is a **ranking** call, not a miss: each model's chosen primary is
*present in the other two's membership sets* (ai-review ↔ hitl-workflow, a multi-agent framework with
async human oversight).

### 3.2 Secondary (multi-label) breadth — where all the noise is
- **Themes per paper:** opus **4.7**, codex **5.0**, gemini **2.7**.
- **Pairwise theme-set Jaccard:** opus–codex 0.53, opus–gemini 0.48, **codex–gemini 0.62**.
- **Consensus core vs long tail:** across the 10 papers, **23** tags all-three agree on vs **27**
  asserted by a *single* model. ~Half the secondary tags are one model's opinion.

### 3.3 Model signatures (directional bias) — assignment counts / 10 papers
| theme | opus | codex | gemini | read |
|---|---|---|---|---|
| hitl-workflow | 5 | 5 | 5 | unambiguous |
| regulatory-compliance | 1 | 1 | 1 | unambiguous |
| provenance-auditability | 4 | 4 | **0** | gemini blind to it |
| risk-routing | 4 | 5 | **1** | gemini under |
| agent-scope-drift | 3 | 4 | **1** | gemini under |
| governance-frameworks | 2 | 4 | 1 | codex over |
| oversight-explanation | 5 | **7** | 4 | codex over |
| rules-based-checks | 4 | **7** | 4 | codex over |
| automation-bias | **4** | 1 | 1 | opus only |
| oversight-theater | **2** | 0 | 0 | **opus only** |
| tooling-supply-chain | **1** | 0 | 0 | **opus only** |

- **gemini = conservative floor** — anchors on the primary; skips relational themes
  (provenance-auditability 0, risk-routing/agent-scope-drift 1).
- **codex = liberal ceiling** — over-extends process themes (rules-based-checks, oversight-explanation 7).
- **opus = middle, but the *only* model reaching the insufficiency layer** (oversight-theater,
  tooling-supply-chain, automation-bias).
- **Facets** follow the same shape: gemini under-tags (survey-input 2 vs 4/4; problem-statement-anchor
  3 vs 5/5).

### 3.5 Fable 5 added as a 4th tagger (2026-07-14) — the decisive comparison
Ran Claude **Fable 5** on Set A (same instrument, full text). It produced the run's most telling result.

- **Fable clusters with Gemini, not with Opus** — despite both being Claude. Pairwise theme Jaccard:
  **fable–gemini 0.86** (tightest pair in the whole matrix), fable–codex 0.62, codex–gemini 0.62,
  opus–codex 0.53, **fable–opus 0.49**, opus–gemini 0.48. → Tagging breadth is **not a vendor/family
  effect**; it's a verbosity disposition. Vendor doesn't predict behavior.
- **Two breadth camps:** liberal = codex 5.0 / opus 4.7 themes/paper; conservative = gemini 2.7 /
  **fable 2.6** (the most conservative tagger).
- **Opus is the outlier among *all four*, 3-to-1, on the insufficiency layer.** Fable (a Claude model)
  skips these just like Gemini/codex: automation-bias (opus 4 · fable 1 · codex 1 · gemini 1),
  oversight-theater (2 · 0 · 0 · 0), tooling-supply-chain (1 · 0 · 0 · 0), oversight-scaling-inversion
  (2 · 0 · 1 · 1). Only Opus reaches them.
- **Primary theme across 4 models: 8/10 unanimous.** Two splits, both *ranking calls at known theme
  adjacencies*: `UB2EVUFU` (Opus hitl-workflow vs three ai-review) and `T72TU8B5`/Hedwig (Fable
  hitl-workflow vs three risk-routing — the routing↔control-surface boundary).
- `provenance-auditability`/`risk-routing` split on the *liberal/conservative* axis (opus+codex reach
  them; fable+gemini don't), distinct from the insufficiency-layer axis.

### 3.4 Insights
1. **Structure agreed, breadth contested.** Primary theme is essentially solved; disagreement lives
   entirely in secondary membership.
2. **Opus is the outlier among all four models (3-to-1), and its outlier tags are the substantive
   ones.** With Fable added, three independent models (fable, codex, gemini) converge on a narrower
   reading and *only Opus* reaches the limits-of-oversight themes (automation-bias, oversight-theater,
   tooling-supply-chain). A naive **model-majority vote would systematically drop exactly those
   themes.** Crucially, Fable is a *Claude* model yet sides with the narrow camp (fable–gemini J=0.86),
   so this is **not vendor-driven** — it's a breadth disposition, and Opus's is the distinctive one.
   Reproduces the Stage-3 finding (**model consensus ≠ human; Opus ≈ human**). Do **not** auto-assign
   secondary tags by model majority; the human (Set B) is the arbiter on the now-3:1 split.
3. **Breadth is the tunable knob:** gemini too thin for complete rosters; codex slightly over; the
   right target is unknown until the human sets it.
4. **Well-defined vs fuzzy themes:** hitl-workflow / regulatory-compliance are crisp; the over/under-
   applied `oversight-explanation`, `rules-based-checks`, `provenance-auditability` are the boundaries
   to sharpen in `Emerging_Themes.md`.

---

## 4. Decisions

- **Freeze the instrument through Set B.** Do not iterate the prompt or tag definitions on Set A
  model results — that would tune the instrument toward *model consensus*, the known-wrong target
  (§3.4 #2), and break A/B comparability. Iterate **once, after Set B, anchored on the human tags.**
- Source-encode all calibration tags (`cal:<model>:…`); keep disposition-independent; reversible.
- Primary theme is reliable enough to model-assign with a light human check; secondary breadth is the
  open policy question Set B resolves.
- **2026-07-18 — `assistive`/`agentic` generation-mode facet pair added mid-Set-B** (additive, per the
  `formal-methods` precedent: no theme redefined, no Set A re-run needed). Human Set B tagging from this
  date can apply it; **TF56EPIP was human-tagged before the pair existed → backfill**; all 20
  calibration papers get it backfilled in the post-Set-B iteration. In the same pass the Set B human
  packet's embedded cheat-sheet was found stale (v0-vintage) and refreshed to the current instrument
  (the Zotero Actions menu was already current; TF56EPIP's tags used current slugs, so nothing recorded
  was affected). See `Taxonomy_Changelog.md` §10.

---

## 5. Open / next steps — REVISED 2026-07-18 (freeze lifted; two-stage sequence)

**Design change (2026-07-18):** the freeze-then-iterate-once plan is replaced by a two-stage
sequence. **Stage 1 — human vocabulary-vetting pass:** Scott human-tags the calibration papers;
gaps and *unanticipated uses* drive definition changes as they surface, each logged in
`Taxonomy_Changelog.md` (first product: §11 — `oversight-explanation` broadened to push/pull
"helping the human understand what the AI is doing"; steering exclusion extended to input-side
context control; "context transparency" relocated out of `hitl-workflow`; record-vs-live-view test
on `provenance-auditability`; the Lumen unanimity overturn that motivated all of it). **Stage 2 —
the summative human-vs-model experiment on the vetted instrument.** Rationale: tuning toward the
*human* was always the plan; doing it before the comparison means the experiment tests the final
instrument, so disagreement is attributable to the models, not to known-fuzzy definitions.

1. Scott completes the vetting pass over the 20 calibration papers (+ types the
   `cal:human:primary:theme:<slug>` tag per paper — the menu can't). **Comparability note (corrected
   2026-07-18, post-pass):** Set A model tags were *present in Zotero* during the pass, but **Scott
   reports he never viewed them during his initial reads** — so initial-read human tags were
   *effectively blind (self-report)*; model outputs entered only through the post-tagging audit
   dialogue, which drove the documented corrections and the two re-adjudications. Accurate
   description: **Set A = blind first read + model-aware adjudication.** Notably, the two
   unanimity overturns (Lumen §11, 22JBEZNK §16) occurred at *blind* first read — the human
   independently diverged without knowing four models were unanimous against him, and full text
   vindicated him both times, materially strengthening the "model consensus ≠ correctness" finding.
   **Set B remains the fully clean comparison** (no model tags will exist there at all — do not run
   models on Set B until the human tags are in).
1b. **Instrument-critique panel (added 2026-07-18; design detailed 2026-07-18 EOD):** after the Set A
   vetting pass, validate the instrument itself before spending the retag. Sequence: (i) Fable
   **known-answer dry-run** — fresh-context taggers apply the current instrument to the 10 Set A
   papers; diff vs human tags; fix residuals (finds where the text doesn't *force* the adjudicated
   answer); (ii) **critique panel** — Fable 5 + Gemini top tier + Codex top tier, fresh contexts,
   given the instrument + Tag reference + curated Set A (full text for the 5 adjudication-rich
   papers, title/abstract for the rest) **with human tags only** (injected into the prompt — no
   tool access needed; the prompt is archived as the frozen critique input); critique + propose
   improvements; adversarial test cases required per finding; (iii) Scott dispositions findings
   (suggestions are proposals, adoption is the arbiter's); (iv) freeze instrument v2; (v) **retag
   Set A** under v2 and evaluate improvement (human-vs-model agreement + the §10–§17 regression
   checks) — **gate: only after v2 is judged improved does Scott tag Set B**, under the frozen
   instrument, then models tag Set B for the clean comparison. **GATE CALLED: PASS (Scott,
   2026-07-18)** — fable 10/10 / codex 9/10 / gemini 9/10 primaries, facet agreement doubled,
   altitude regression 8/9. Set A backfills executed same day (counterpoint → Z8TPRNEU+VG6CIDQW,
   agentic → T8E8SCCG, general-code → UDVHQ5HR); all 10 Set A items verified consistent with every
   adjudication and ruling. Actions menu (32 toggles) re-imported by Scott. **Critique taxonomy — only the first category is directly actionable:** (a) *ambiguity /
   inconsistency / omission* in the written instrument → fix; (b) *disagreement with an adjudicated
   boundary decision* (e.g., the drift object-of-mechanism rule, the steering exclusion) → recorded
   but the human arbiter's call stands — otherwise the critique loop re-tunes the instrument toward
   model consensus, the known-wrong target. Critique agents run in fresh contexts, separate from the
   tagger runs.
2. Freeze the *vetted* instrument; **archive check:** v1-instrument model outputs preserved in
   `slr-phase4/data/tags-v1/` (done 2026-07-18) before any re-run overwrites `data/tags/`.
3. Re-run all 5 models on Sets A+B in fresh contexts under the vetted instrument; write `cal:<model>:*`.
   **AMENDED 2026-07-21 (panel economics):** the v2.13 comparison panel = **codex + gemini over
   both sets (20 papers)** — Set A re-run included because the instrument evolved substantially
   (v2 → v2.13) since its last model pass. **Fable is $$$$-tier and runs ONLY with Scott's explicit
   per-run permission**, deployed *targeted* (tie-breaks: contested primaries, schema violations) —
   the assistant proposes tie-break targets and waits for authorization. **AMENDED same day
   (Scott): OPUS is a standing panel member** — the run set going forward is
   **opus + codex + gemini** over all papers; **Fable is reserved for tie-breaks/input beyond
   those three** (per-run permission unchanged). Opus ran all 20 blind on 2026-07-21; Fable ran
   the trimmed contested six. Outputs:
   `data/tags-v213/<tagger>/<KEY>.json`; runner `tools/run_setb_panel.sh` (gemini via file-read
   mode — `agy --add-dir`, no permission-skipping flags; prompt files scratchpad-only so full
   texts can't be staged).
4. Compute human-vs-model agreement (primary match; theme-set Jaccard; per-theme confusion) —
   **headline on Set B**; Set A reported as model-informed.
5. Decisive tests: (a) the insufficiency-layer breadth question (§3.4 — does the human tag
   `automation-bias`/`oversight-theater` where only Opus did?); (b) does the broadened
   `oversight-explanation` + steering cue fix the Lumen class of error?
6. Set the breadth policy; run the **full 148** under the final instrument; human-confirm the long tail.
7. **Set C (defined 2026-07-20) — AI-first validation set.** The inverse protocol of Set B and a
   pilot of the production sweep workflow: **models tag first** under the frozen instrument, the
   human **validates/adjudicates** rather than tags blind — measuring validation burden, catch
   rate, and error profile at review time (the mode the 148-sweep actually runs in; Sets A/B can't
   measure this). Membership = designated test cases, growing as probes surface. First member:
   `ZUM76CCG` (surfaced by the 2026-07-20 Set B roster reconciliation — it sat in the 02-Human
   collection and `calib_sets.json` but never in the human packet; Scott ruled it a Set C test case
   rather than an 11th Set B paper). Same reconciliation restored `TF56EPIP` to the 02-Human
   collection (it had been mis-shelved in 01-AI Calibration Run — all docs and its human-only tags
   confirm it is Set B). Zotero: `03-Set C - AI Tag, Human Validate` [U65X7JNA]; Set B = the
   packet's 10, matching `calib_sets.json`. **Pilot protocol (Scott, 2026-07-21):** Set C runs the
   full production ladder (`tools/triage_v213.py`: L0 schema → L1 consensus [3/3 ACCEPT + **10%
   seeded random audit**, 2/1 LIGHT-REVIEW, split HUMAN] → L2 computed tripwires [sprawl >6
   themes, any demote flag] → per-tag facet voting), but **Scott reviews ALL Set C papers**
   regardless of disposition — the pilot scores the ladder itself; sampling begins only in the
   sweep. **Replication stage (Scott, 2026-07-22 — disagreement-triggered, not universal):**
   observing run-to-run variability during the assignment work, the design adds targeted
   replication: any primary disagreement triggers **2 extra runs per model (k=3)**; each model's
   vote becomes its **modal** primary (tags = asserted in ≥2/3 runs); re-triage on modals —
   modal 3/3 = ACCEPT annotated *noise-resolved*, persistent 2/1 = LIGHT-REVIEW, persistent split
   = HUMAN. **Within-model instability** (a model disagreeing with itself across runs) is a new
   computed tripwire biasing one rung toward review — the operationalized "low-confidence" signal
   (computed, never self-reported, per doctrine). Unanimous first-pass papers are never
   replicated; the 10% audit covers residual false unanimity. The contested-subset replicates
   double as the gauge-R&R (repeatability) study for the methods chapter. Note: CLI taggers offer
   no temperature/seed control — nondeterminism is a property of the gauge, characterized rather
   than eliminated. Retrospective validation on the calibration 20: 7 ACCEPT (6 correct; the 1 divergence =
   the documented B644HQFS altitude ruling), 10 LIGHT-REVIEW (consensus proposal matched gold in
   all 10), 3 HUMAN (exactly the three hardest papers: 2CKL96B8, E95T8E88, TF56EPIP).

---

## 6. Reproducibility, versioning & write-safety (2026-07-15)

Infrastructure hardening done this date so the phase is reproducible and the instrument's evolution
is auditable (relevant for the course assignment and the dissertation methods chapter):

- **The whole SLR is now version-controlled.** Private GitHub repo **`thurlow-research/SLR`** (repo
  root = the OneDrive `Systemic Literature Review` dir; branch `main`). Phase-4 working materials live
  under `slr-phase4/` (prompt, cheat-sheet, calibration sets, per-tagger tag JSON, tools). Copyrighted
  full-texts (`slr-phase4/txt/`) and secrets are gitignored; `.gitignore` also excludes editor
  swap/backup files (`*.swp`, `.envrc.*`) so no credential-bearing temp file can be staged.
- **Instrument provenance captured as v0-vs-current.** `Tag_Prompt_v0.md` / `Tag_Cheatsheet_v0.md`
  (16 themes + 4 facets, original defs) preserved alongside the current `Tag_Prompt.md` /
  `Tag_Cheatsheet.md`; `Taxonomy_Changelog.md` logs each disparity → diagnosis → change → measured
  outcome, and flags the confound that *both* the definitions and the prompt's task block changed
  between versions (so the v0→current delta is not attributable to definitions alone).
- **Zotero Actions-menu self-select hazard (2026-07-20):** with the menu at 40+ toggles, scrolling
  can silently fire a toggle on the focused item — caught twice (a facet swap on 6DXZGHD9; a
  `risk-security` drop on 7V7SRG43). Standing mitigation: **post-paper server-side verification**
  (sync, then API-echo the tag set) after every tagging session; keyboard shortcuts on
  high-frequency toggles are the ergonomic fix if it recurs.
- **Zotero write-safety tightened after a key leak.** The single Zotero API key was found hard-coded in
  older scripts/skills; **all keys were revoked and rotated**, then **split least-privilege**:
  `ZOTERO_API_KEY_RO` (reads) / `ZOTERO_API_KEY_RW` (writes), with fallback to a single
  `ZOTERO_API_KEY`. Calibration/tagging tooling reads RO for GETs and RW only for the tag PATCH.
  The custom Zotero skills now **default to dry-run** and require an explicit `--commit` to write, and
  were re-released secret-free (`ResearchClaudeCodeSkills` v0.1.1). A standing global rule now scans
  staged content for key-shaped literals before any commit.

---

## 7. Human vetting pass — method & running log (Stage 1, 2026-07-17 → )

**What this is.** Before the summative human-vs-model experiment, Scott human-tags the 20
calibration papers as a **vocabulary-vetting pass**. The unit of work is not the tag set but the
*probe*: each paper tests whether the vocabulary can express what the paper actually is. This
reframes the human's first read from "baseline data collection" (the original blind design) to
**instrument validation** — the strongest use of the arbiter's limited attention, since Stage 2 then
measures the models against a vetted instrument and disagreement becomes attributable to the models.

**Method (per paper).**
1. Read full text; tag in Zotero via the Actions menu (`cal:human:theme:*` / `cal:human:facet:*`);
   **type** the `cal:human:primary:theme:<slug>` tag (the menu cannot toggle primaries).
2. Where the vocabulary resists, classify the failure before resolving it:
   - **Uncaptured concept** → candidate new tag; stage in `HOS_Seeded_Theme_Candidates.md` unless
     clearly needed now (bar: the concept recurs and no existing tag's *reasonable broadening* holds it).
   - **Unanticipated use of an existing tag** → the definition MUST be updated to sanction the use.
     "No new tag needed" does not mean "no instrument change": models tag from the written text, so
     an unwritten broadening would be scored as model error when it is doc lag.
   - **Boundary collision** → sharpen *both* themes' Boundary lines with the discriminating test.
3. Land every change immediately in the Tag reference + `Taxonomy_Changelog.md` (no batching), so
   the instrument converges monotonically and the models eventually see the settled text.
4. Model tags are *visible* on Set A during this pass (they already ran) — used **diagnostically**
   (does the human's difficulty reproduce a model split?). Set B carries no model tags; it stays
   clean for Stage 2.

**Decisions / learnings so far (through the first papers of the current 10):**
- **The Lumen unanimity overturn (§5, changelog §11).** 4-model unanimous primaries can encode a
  shared *category error*, not just ranking noise — unanimity is not a proxy for correctness even on
  the "solved" primary task. Boundary rules that exist only in the triage discriminator (steering
  exclusion) must be restated in the tagging instrument or models won't apply them.
- **The unanticipated-use principle** (method step 2b) — the pass's first-order product is
  definition text, not tags.
- **Facets carry explanatory load.** `assistive` (added a day earlier) *explained* the Lumen
  difficulty: in assistive mode there is no handoff for the old `oversight-explanation` to bite on.
  Mode facets validated on day one.
- **Word-collision discipline.** "Transparency" joins "framework" as a word that must route by
  object, never be tagged as such — now a preamble rule.
- **Lens-vs-lever** emerged as a cross-theme discriminator: information themes
  (`oversight-explanation`, `provenance-auditability`) vs action themes (`hitl-workflow`,
  `risk-routing`), with persistence (record vs live view) separating the two information themes.
- **Instrument-copy drift is real.** The Set B packet's embedded cheat-sheet was silently v0-vintage
  while the Zotero menu was current — caught 2026-07-18. All copies (cheat-sheet, prompt, packet)
  must be updated in the same commit as the Tag reference.
- **Tooling gap:** the Actions menu cannot set primaries → primaries are typed; early-tagged papers
  need backfill when the vocabulary moves under them (TF56EPIP: mode facet + primary pending).
- **Coder fatigue is a reliability factor of the human instrument** (UB2EVUFU, self-diagnosed
  "dinner fatigue"): the first-pass tag set had several oversights (facets missed, one theme
  mis-filed), all caught on a second look. With 29 tags/paper, recall-based tagging degrades when
  tired. Mitigations now in the instrument/process: the **five-question facet checklist** (mechanical
  coverage, not recall) and a **second-look verification** of each paper's tags before moving on —
  worth reporting in the methods chapter as an honest human-reliability observation alongside the
  model biases.
- **Self-correction is evidence the boundaries work:** the human's own `risk-routing` retraction on
  UB2EVUFU (error-condition handback ≠ triage decision) shows the sharpened definitions catch the
  arbiter too — the instrument is doing work independent of who holds it.
- **A boundary only protects taggers if it's in the copy they tag from** (VibeGuard recurrence, §17):
  the same human repeated the same documented error on the same paper because the exclusion lived in
  the reference doc but not the compressed cheat-sheet. Compression gaps are instrument bugs.
- **The struggle signal is a disposition tripwire:** difficulty picking a primary, or stretching a
  definition to fill a tag set, reliably indicated the paper didn't belong at core (2CKL96B8,
  UDVHQ5HR — both demote-flagged; 3 demotes / 10 calibration papers → expect a demote tail in the
  full sweep; the tagging pass doubles as a scope audit).
- **Model salience bias:** models anchor primaries and `problem-statement-anchor` on a paper's most
  vivid/quantified section rather than its overall shape or the facet's bar — a distinct failure mode
  from plumbing over-tagging and boundary pattern-matching.
- **Unanimity overturned twice:** Lumen (§11) and 22JBEZNK (§16) — in both, 4-model unanimous
  primaries encoded a shared category error the human caught. Model consensus ≠ correctness holds
  even at n-of-4 unanimity; the human vetting pass is what caught it.

**Running log** *(update at the end of the current 10)*:

| # | Paper | Set | Human outcome | Instrument action |
|---|---|---|---|---|
| 1 | `TF56EPIP` | B | 6 themes incl. `automation-bias`, `provenance-auditability`; no primary/facets yet | pre-dates mode pair → backfill primary + mode facet |
| 2 | `VG6CIDQW` (Lumen) | A | **COMPLETE & verified 2026-07-18:** primary `oversight-explanation` + `assistive` + `built-system` + `steering`; overturned 4-model unanimous `hitl-workflow` | changelog §11: `oversight-explanation` broadened (push/pull); steering exclusion → input side (confirmed, §12); `hitl-workflow` levers-only; `provenance-auditability` record test; transparency routing rule |
| 3 | `Z8TPRNEU` | A | **COMPLETE & verified 2026-07-18:** primary `hitl-workflow` (= 4/4 models) + `ai-review` (sides with codex alone) + `agentic`/`steering`/`survey-input`; rejected 3-model `agent-scope-drift` | changelog §13: object-of-mechanism rule; drift Captures tightened + Z8TPRNEU → counter-example; `steering` amended to cover documented practice; `ai-review` slug-connotation noted (watch in re-run) |
| 4 | `UB2EVUFU` | A | **COMPLETE & verified 2026-07-18** (after self-corrected second pass — "dinner fatigue"): primary `ai-review` (resolves v1 split: 3 models + human vs Opus) + `hitl-workflow`/`provenance-auditability`/`remediation-gating`; facets `agentic`/`built-system`/`framework`/`steering`; rejected `rules-based-checks` (plumbing — confirmed by full-text scan) and self-retracted `risk-routing` | changelog §14: error-condition-handback boundary on `risk-routing`; `remediation-gating` process gates; plumbing ≠ membership rule; five-question facet checklist |
| 5 | `T72TU8B5` (Hedwig) | A | **COMPLETE & verified 2026-07-18:** primary `risk-routing` — **human confirms the 5/5 post-fix model unanimity** (the tie-breaker sharpening's flagship result now human-validated); themes exact-match opus/fable v1 (`risk-routing`+`hitl-workflow`+`oversight-explanation`); facets `agentic`/`built-system`/`framework`/`survey-input` (resolves the framework 1/4 split against gemini); rejected codex's 4 plumbing extras + drift (object-of-mechanism applied consistently) | **none — first no-change probe**; instrument held on its previously hardest case |
| 6 | `F9JM9CI6` | A | **COMPLETE; primary RE-ADJUDICATED 2026-07-18 late** → `oversight-explanation` (altitude refinement: the vision's energy lives in explanation design; models unanimous there in v2) — was `ai-review` + `oversight-explanation`/`risk-routing`; facets `intro-framing`/`counterpoint`/`general-code`; **no mode facet** (AI on review side only — human reversed twice before the clarifier settled it) | changelog §15: `counterpoint` role facet (stance polarity, direction-agnostic); `general-code` scope flag (object-of-oversight); mode-pair clarifier ("uses agents" ≠ agentic); narrowness ruled extent-not-tagged |
| 7 | `22JBEZNK` | A | **COMPLETE & verified 2026-07-18:** primary `oversight-explanation` + `agentic`/`non-developer`/`survey-input`; **overturned 4-model unanimous `automation-bias`** (paper controls for + rejects overconfidence — capability gap, not bias); self-corrected `risk-routing` off | changelog §16: capability discriminator on `automation-bias` (22JBEZNK → counter-example); competence-gap candidate upgraded to arbiter-validated; mode tie-rule (reviewable unit dominates) |
| 8 | `T8E8SCCG` (VibeGuard) | A | **COMPLETE & verified:** primary `rules-based-checks` (= 4/4 models) + `ai-code-insecurity` + `framework`/`built-system`; `remediation-gating` re-applied then removed — **the documented §4 error recurred** | changelog §17: root cause = exclusion absent from the compressed cheat-sheet (the day-1 compression gap); exclusion now in all copies; "every human-catching boundary goes in the compressed instrument" |
| 9 | `2CKL96B8` | A | **COMPLETE & verified; primary RE-ADJUDICATED 2026-07-18 late** → `ai-code-insecurity` (human conceded to the operationalized biggest-tent after all 3 v2 models converged there; original `ai-review` was "scope-expanding its definition") + `ai-review`/`quality-debt` themes + `lit-review`/`intro-framing`/`assistive`; `demote:context` stands | changelog §17: lit-review structure-not-required clarifier; biggest-tent primary convention; struggle-signal workflow cue |
| 10 | `UDVHQ5HR` | A | **COMPLETE & verified:** `demote:context` flagged (LLM-judge capability benchmark, `VP7TS6CX` precedent); `ai-review` primary + sole theme (= all 4 models after removing stretched `quality-debt`/`intro-framing`) | changelog §17: demote-signature validation; anchor bar set (overall problem statement only; never on lit-review) |
| — | `M74M3RFJ` | A | verified (pre-pass tags stand): primary `regulatory-compliance` + `general-ai`/`framework`/`intro-framing`; demoted core→context 2026-07-15 | none — the `general-ai` tripwire case, already §6. **2026-07-20 reconciliation:** restored to the 01-AI Calibration collection (roster = frozen infrastructure); +`demote:context` (predated the flag); +`design-only` (2nd confirmed — GSN exemplars, engine = future work); −`intro-framing` (contradiction rule) |
| 11 | `R4WJZBSF` | B | **COMPLETE 2026-07-20** (blind snapshot v156638; blind read + model-aware adjudication): blind primary `risk-routing` → final **`regulatory-compliance`** + `hitl-workflow`; facets `metrics`/`framework`/`design-only`/`risk-ip`/`risk-bias`/`risk-quality`/`risk-overreliance`; no mode facet; **core, no demote** (what+how carve-out). Blind primary = the signal-without-allocation stretch — the boundary's first catch. Two define-only theme over-tags (`automation-bias`, `quality-debt` + `oversight-explanation`) caught in audit and removed | changelog §19 (`design-only`), §20 (`metrics` + routing boundary), §21–§22 (risk-flag family), §23 (what+how carve-out — this paper's ruling) — the most instrument-productive paper of the calibration |
| 12 | `6DXZGHD9` | B | **COMPLETE 2026-07-20** (blind snapshot v156680; final v156686): blind primary `ai-code-insecurity` (sole theme) → final **`org-governance`** + `ai-code-insecurity` secondary; facets `built-system`/`metrics`/`risk-security`/`risk-quality`/`risk-overreliance`/`survey-input`; `framework` OFF (pipeline test); no mode facet. **Four arbiter reads to converge** (detection → governance assessment) — logged as diagnostic: if models scatter here, human difficulty predicted it. Template-family caution (ANN-ISM) in child record | changelog §24: risk-quality consistency catch (PA-2 = PA-5 clause); metrics measurand settled by output-is-the-score test; Set B consultation Q&A on this paper produced the lit-review framing rule + input-side expert-panel ruling |
| — | *Set B process note (superseded same day — see the co-tagging protocol below)* | B | Original note: papers 1, 3–8 fully clean. By EOD 2026-07-20 the audit loop had extended to papers 1 (B644HQFS), 4 (7V7SRG43), and 6 (BAWCBT9R); only **3, 5, 7, 8 (E95T8E88, UW2R6BBJ, E3E5YA2E, 5VTAJISY)** remain audit-free (+ TF56EPIP backfill pending). No Set B paper has model tags | — |
| 13 | `B644HQFS` | B | **COMPLETE 2026-07-20** (blind v156722 → final v156726): primary `quality-debt` — **arbiter altitude ruling** (coded volume over the commons-framing wrapper; a documented human data point for the models' identical choice) + `oversight-scaling-inversion`/`automation-bias`/`org-governance`/`hitl-workflow` (documented-practice: the slop-mitigations); `risk-quality` parity catch; −`tooling-supply-chain` (no AI-tooling object; **knowledge-ecosystem pollution noted as a homeless observation** — watch in sweep) | mining-study archetype for the risk flags via coded categories |
| 14 | `BAWCBT9R` | B | **COMPLETE 2026-07-20** (blind v156730): primary `ai-review` + `demote:context` (judge-audit = validates-which-tool); `metrics` (measurand: judge bias-sensitivity/consistency); `method-experiment` (subjects-may-be-systems); QA removed `agentic` (mode-clarifier verbatim case) + `risk-quality` (wrong object — the evaluator, not the code) | changelog §27: the carve-out tool-validation **exclusion** encodes this paper's demote |
| 15 | `7V7SRG43` (CodeAgent) | B | **COMPLETE 2026-07-20** (blind v156742 → final v156790): primary `ai-review` + `agent-scope-drift` (**the §13 worked-pair, missed blind — QA catch**); +`general-code`; −`method-experiment` (whose-properties, 2nd occurrence); `risk-security`+`risk-quality` kept per the **source-agnostic ruling** (§27) — `risk-security` was then dropped by the **menu self-select hazard** and restored | §27 source-agnostic rule born here; menu hazard discovered here |
| 16 | `E95T8E88` (What to Cut) | B | **COMPLETE 2026-07-21** (blind v156811 → final v156819): blind primary `risk-routing` → **`oversight-scaling-inversion`** — the **second blind catch** of the signal-without-allocation boundary; +`routing-signal` (the facet's seed); malformed typed primary schema-fixed | changelog §29: `routing-signal` facet born here |
| 17 | `5VTAJISY` (HULA) | B | **COMPLETE 2026-07-21** (blind v156761 → final v156815): primary `hitl-workflow` ✓ blind (plan-gate home case); **first `adopted` of the calibration** (Atlassian JIRA internal deployment — the facet's scarcity bar held until a real one); method swap −`experiment` (own-system offline eval — whose-properties, 3rd occurrence) +`field-study`; −`metrics` (apparatus), −`ai-review` (the human reviews in HULA); `steering` ✓ (hybrid steer-and-check documented) | none — nine facet axes exercised cleanly |
| 18 | `UW2R6BBJ` (Secure AI-SDLC) | B | **COMPLETE 2026-07-21** (blind = final v156802 — **zero QA tag deltas, first human-solo-perfect set**): primary `regulatory-compliance` + `provenance-auditability`/`tooling-supply-chain`; `expert-validated` (the **promotion instance**, §V.E structured 12-expert post-implementation validation; Phase-1 consultation separately input-side); `general-ai` kept as audit trail — **core via the sole-exemplar exception** (§30, arbiter-weighed) | changelog §28 (promotion) + §30 (kept-core exception) born here |
| 19 | `E3E5YA2E` | B | **COMPLETE 2026-07-21** (blind v156770 → final v156826): primary moved `hitl-workflow` → **`automation-bias`** (named in its own abstract + skill erosion); +`survey-input` (perception-study archetype) + `demote:context` (§3 perception class); −`theme:ai-code-insecurity` (perception ≠ empirical — B644HQFS consistency; `risk-security` flag stays), −`method-field-study` (interviews only), −`org-governance` (implications ≠ lift) | none |
| 20 | `TF56EPIP` (backfill) | B | **COMPLETE 2026-07-21** (v156789): retagged under the mature instrument — 3 themes (from the pre-mode-pair 6), both mode facets, `lit-review` + `metrics` + `steering` + risk flags; `demote:context` (agreed: model-evaluation focus per UDVHQ5HR/VP7TS6CX precedent; **background wealth preserved via context tier, child note, and reference snowballing**); primary `ai-review` confirmed as biggest tent under the binding lit-review rule | none |

**Co-tagging protocol (named 2026-07-20; role division clarified same day; documented for the
methods chapter).** During Set B the working mode evolved from "human tags blind, alone" into
**co-tagging — precisely: human-tags + AI-QA**. The role asymmetry is the design: **the human
performs ALL tagging judgment; the AI never proposes tags before the human's blind set is
recorded** — it performs quality assurance after. The loop: (1) the human tags each paper blind
(no model tags exist; the assistant has not read the paper); (2) on request, the assistant
*audits* the recorded tag set against the instrument text and the full text — consistency checks,
rule-pointers, textual evidence — and answers definition questions at rule level; (3) the arbiter
rules on every delta (the assistant's audit findings are proposals; adoption is the arbiter's, per
the §5·1b critique-taxonomy rule); (4) every boundary that catches or nearly catches the human
lands in the compressed instrument the same day (compression-gap principle). Where the assistant
wrote tags via API, it executed the arbiter's already-made rulings mechanically (e.g., the
M74M3RFJ reconciliation, the agreed method-facet corrections) — execution, not judgment. **Yield:** instrument v2.2 → v2.10
in two days (changelog §19–§27: design-only, metrics, the five-flag risk family, the method
family, the what+how carve-out, ~a dozen boundary rules), a per-paper catch record (define-only
over-tags, word-trap saves, the §13 worked-pair miss on 7V7SRG43), and near-model-error
prediction (the human's difficulty spots flag where models are expected to scatter).
**Comparability accounting (state precisely in writeups; AMENDED 2026-07-21 at Set B close):**
ALL TEN Set B papers were ultimately co-tagged (the arbiter chose QA for the final four as well) —
every Set B human set is **"blind first read + AI-audited adjudication, model-tag-free."** The
**human-solo layer is preserved for all ten** as pre-audit Zotero versions: R4WJZBSF v156638 ·
6DXZGHD9 v156680 · B644HQFS v156722 · BAWCBT9R v156730 · 7V7SRG43 v156742 · 5VTAJISY v156761 ·
E3E5YA2E v156770 · TF56EPIP v156784 · E95T8E88 v156811 · UW2R6BBJ v156802 (blind = final there —
zero QA deltas). Scoring plan: **headline = models vs the final adjudicated sets** (the
co-tagging gold standard); secondary = models vs the blind snapshots (human-solo performance).
**Disclosed confound:** the instrument moved during the pass (v2.2→v2.13), so blind tags for
early papers predate rules the models will see (the §9 confound's smaller sibling); the final
adjudicated sets are consistent with the closing instrument. The **fully-clean comparison role
rests on Set C** (AI-first protocol, untouched). Set B tally: 3 `demote:context` flags in 10
(BAWCBT9R, TF56EPIP, E3E5YA2E) — matching Set A's 3/10 demote rate exactly.

---

## 8. Prompt-design validation experiments (2026-07-22/23) — persona rejected; no length effect at panel tier

Two candidate prompt refinements, surfaced by course work (GRAD 50300 prompt-optimization
assignment) and by observed behavior of a cheaper model tier, were evaluated against the
calibration corpus before the sweep. Both were **rejected for the production instrument** — the
value of the exercise is that the rejections are now empirical, not argued. v2.13 is unchanged.

### 8.1 Persona framing — evaluated and rejected

**Motivation.** Persona definition is a standard prompt-refinement technique; a Gemini-Flash-tier
probe on Hedwig (assignment side) suggested a persona block stabilized the
`hitl-workflow`↔`risk-routing` primary flip. Question: does a persona help the production panel?

**Design.** One-variable variant: a 13-line "WHO YOU ARE" block (doctoral researcher, the review's
framing, explicit research-interest list, instrument-discipline stance) prepended to the
hedwig-free assignment vintage of the instrument; otherwise byte-identical. Run:
gemini-3.1-pro-high (the panel seat), single pass over all 20 calibration papers, scored against
`human_gold.json` beside the v2.13 gemini baseline. Artifacts:
`slr-phase4/data/experiments/persona-20260722/` (instrument, per-paper outputs, scorer,
scored.json).

**Results.** Primaries 13/20 vs baseline 14/20; theme-Jaccard .64 vs .61; facet-Jaccard .68 vs
.67; demote-flag accuracy 15/20 vs 14/20. Four primaries changed: one gain (F9JM9CI6 →
`oversight-explanation`, matching gold), two losses (UB2EVUFU → `remediation-gating`; UW2R6BBJ →
`org-governance`), one wrong→differently-wrong (TF56EPIP). No change on any
`hitl-workflow`/`risk-routing` paper — Hedwig stayed `risk-routing` in both arms, notably on a
**hedwig-free** instrument (the baseline had the §9-class self-reference advantage), so
de-referencing cost nothing at panel tier; the Flash flip is a tier fragility.

**Findings.** (a) **Interest-salience drift is real:** both losses moved *toward* content named in
the persona's research-interest list (`remediation-gating` appears verbatim; the
"governance/regulatory landscape" phrase blurs the org/regulatory boundary) — the predicted
failure mode of persona-with-interests, now observed. Gemini is the panel's most run-stable seat,
so these are likely prompt effects, not sampling noise. (b) **Disclosed confound:** the variant
bundles the persona with the assignment vintage's de-referenced worked examples; the course
vintage's tie-breaker example ends in `remediation-gating`, exactly where UB2EVUFU flipped —
example-anchoring is the rival explanation for that regression. A persona-free control arm on the
same vintage would separate them if it ever matters.

**Decision.** v2.13 stays persona-free for the sweep. The methods chapter cites this as a
*defended* design choice: tagging behavior is driven entirely by the versioned instrument text;
role-play framing added no accuracy and its one systematic effect was pulling assignments toward
the persona's declared interests — consistent with the corpus's own findings that non-semantic
framing cues manipulate LLM judgment (`BAWCBT9R`, `X7EN6DXZ`).

### 8.2 Prompt splitting (themes vs facets) — assessed and declined; the length question tested instead

**Motivation.** Flash-tier runs showed variance increasing with prompt size (a candidate
lost-in-the-middle effect), prompting the question of whether splitting the instrument into
separate theme and facet prompts would improve consistency.

**Assessment (not run).** Splitting was declined for the production pipeline on structural
grounds: the v2.13 rule mass *couples* the axes (define-without-allocation → `metrics` not
`theme:risk-routing`; `routing-signal` mutually exclusive with the theme; contradiction rules
feeding demote logic), so a split either breaks cross-references or duplicates them into both
prompts, while doubling per-paper cost and adding a cross-call consistency failure mode the
ladder cannot currently detect.

**The testable premise was tested on existing data.** If prompt size drove panel-tier trouble,
paper length should predict disagreement. Across the calibration 20 (TXT 17KB–210KB): Pearson r
between TXT size and distinct-primaries **+0.01**, theme-set dispersion **+0.09**, gold-primary
hits **+0.03** — no length effect. The hard papers are short and boundary-hard (2CKL96B8 17KB,
E95T8E88 27KB); three of the four longest are unanimous and correct. **At panel tier, difficulty
is conceptual, not contextual**; the Flash size-sensitivity is a property of that tier.

**Lessons carried forward (staged, not sweep-blocking):** (1) paper length becomes a monitored
covariate in the sweep — re-run the correlation at n=128 where the instability tripwire supplies
a per-paper variance signal; (2) a "sandwich recap" (schema + checklist + top boundary rules
repeated after the paper text) is staged as a v2.14 robustness candidate, to be tested
Flash-side first under the same graduation bar as the persona; (3) **gauge qualification for
tier substitution** — before any cheaper model tags the ~890-context extension, it must pass a
consistency probe (k≈5 on a small set, modal-agreement threshold), because the Flash observations
demonstrate that tier swaps change the gauge's variance properties, not just its accuracy.

### 8.3 Gauge constancy (same dates, recorded here for the methods chapter)

Panel model identities are now **pinned** in the runner rather than inherited from CLI defaults
(codex `-c model="gpt-5.6-sol"`, effort high; gemini `--model gemini-3.1-pro-high`; opus = Claude
Opus 4.8 via the orchestrator), after a session-log audit verified all v2.13 calibration runs had
in fact used these tiers. Every run now emits a `<KEY>.meta.json` provenance sidecar (model,
effort, CLI version, timestamp), repo-side only. Caveat for the writeup: "high" effort is a fixed
operating point per vendor, not a cross-vendor equivalence claim — comparability rests on the
calibration results themselves.


## 9. External precedent for the multi-model panel design (ID7IN65K, found 2026-08-23)

Until now the panel design was justified internally — decorrelation reasoning plus our own
calibration results. `ID7IN65K` (Choudhuri, Bird, Badea & Sarma, *To Copilot and Beyond: 22 AI
Systems Developers Want Built*, Oregon State + Microsoft Research, arXiv 2604.07830) supplies an
**independent published instance of substantially the same design**, applied to qualitative coding
of survey data. Worth citing in the methodology chapter: it moves "we invented a defensible
procedure" to "we applied a procedure others independently arrived at."

**Their pipeline (their §3.2), against ours:**

| Their stage | Ours |
|---|---|
| S1 Independent theme discovery — three models, separately | Independent per-model tagging runs |
| S2 Codebook reconciliation | Instrument consolidation across calibration rounds |
| S3 **Author review and codebook approval** — humans lock the codebook before coding | v2.13 human-locked instrument, frozen before the sweep |
| S4 Systematic coding — all three models code every response, **rationale before code** | All three models tag every paper; rationale required in the JSON schema |
| S5 IRR — **Krippendorff's α** + **pairwise Cohen's κ**, then consensus | Cross-model agreement + κ; consensus/tripwire triage ladder |

**Convergent points worth naming explicitly** — these are the design choices that were arguable in
isolation and are corroborated here: (a) humans approve the codebook *before* machine coding, not
after; (b) models are required to produce a rationale *before* assigning a code; (c) inter-rater
statistics are computed **between models**, treating each as a rater; (d) disagreement routes to a
consensus step rather than a majority vote alone.

**Where we go further:** k=3 replication per model (they run each model once), so we can separate
*inter*-model disagreement from *intra*-model instability — the `unstable:<model>` tripwire has no
counterpart in their design. Also our arbiter rules on every item's tier, where their humans
approve the codebook but do not re-code.

**Reflexive caution (important, and the paper illustrates it).** Their multi-model machinery is
their **method**, not their subject — and our own panel proposed `ai-review` 3/3 on this paper,
almost certainly by reading the methods section as content. That is the apparatus-vs-object failure
(Taxonomy_Changelog §47), and it is the same trap our corpus tagging must avoid when a paper's
research design resembles the phenomenon under study. Cite this paper for its method; do not tag it
for it. Disposition: Context, `survey-input`, `02 - Supporting`.

## 9b. Second external precedent — divergence detection as a *designed* oversight mechanism (ZGST9CY6, found 2026-08-24)

§9 established that others independently arrived at our panel **procedure**. Zhu, Lu, Ding, Lee &
Wang (2025), *Designing Meaningful Human Oversight in AI* (CSIRO Data61 / UNSW, `ZGST9CY6`) supplies
a different and stronger kind of support: it names the same construct as a **prescribed design
mechanism** for oversight in general, not as one team's study method.

Their mechanism catalogue (their Table 4) lists:

> **Divergence detection and independent checker** — *"Comparison against a second AI/system,
> heuristic, or ruleset with alerting"* — agency dimension *source of action* — solve–verify
> contribution: *"Flags cases that need verification when solvers disagree, **avoids blind
> trust**."*

It recurs in all four of their end-to-end patterns, including *"Stand up a lightweight rules checker
to power divergence alerts"* (Pattern 1) and *"an **independent summariser** or rule-based sampler to
**challenge the main synthesis**"* (Pattern 3).

**Why this is worth citing in the methodology chapter, alongside §9.** §9 is a precedent of
*practice* — another team happened to do this. This is a precedent of *prescription* — an
AI-assurance group states that independent cross-checking is a mechanism oversight designs **should**
include, and gives the reason (disagreement is the signal that a case needs human verification;
blind trust is the failure it prevents). Cited together, the pair moves the panel design from "we
invented a defensible procedure" (§9: "others did it too") to "we applied a mechanism the oversight
literature independently prescribes."

**Two further alignments worth naming:**

- **Zhu's Pattern 3 is a literature-synthesis pipeline** — corpus register with frozen
  inclusion criteria, dedup rules, per-claim provenance anchors, sentinel-item coverage probes,
  minority-view mining, risk-weighted spot checks, abstain on low evidence density. That is a close
  structural match to this SLR's own Stage 3–5 design, arrived at independently. Their "Known Uses"
  for the pattern are Consensus, Elicit, and Scite.
- **Their Pattern 2 prescribes reviewer calibration on a golden set with inter-rater agreement
  tracking** — the same instrument as our calibration rounds and κ reporting.

**Guardrail — do NOT let this become circular.** Zhu is a *corpus paper* under review by the very
panel whose design it is being cited to support. Two consequences: (a) its own tagging must be
argued from its content, never from its usefulness to our method (it was: `org-governance` primary,
nine themes, all textually grounded); and (b) when cited in the methodology chapter it must be
presented as **independent published prescription encountered during screening**, with the
screening-discovery noted — not as a source consulted while designing the panel, which it was not.
The panel design predates this paper's discovery; the changelog and this file carry that timeline.

**Corpus-tagging consequence.** `ZGST9CY6` carries the staged `cal:human:facet:agent-panel` +
`cal:human:facet:cross-model` by arbiter ruling (2026-08-24). Note the evidence is *"a second
AI/system"* / *"independent model"* — **functional independence, not named vendor diversity**. If
the staged facets are formally grafted, the `cross-model` definition ("different underlying
vendors/models") needs a decision on whether prescriptive "independent model" language qualifies, or
whether the facet requires an actually-composed multi-vendor panel. This is the first item where the
distinction bites; the sweep will produce more.

## 10. THE PROCEDURE AS PRACTISED — consolidated statement (2026-08-26)

Sections 1–9 record how this method was *developed*, chronologically and with the dead ends left in.
This section states what the method **is**, so the write-up does not have to reconstruct it from the
history. Where something is still open it says so.

### 10.1 What it is, in one sentence
**Independent multi-rater coding of full texts by three decorrelated LLM taggers with intra-rater
replication, followed by human arbitration** — the human being the instrument of record, the models
being an instrument for surfacing the contested surface.

### 10.2 Corpus and bands
128 Core papers, in three bands by expected effort, **all of which receive a human tier call**:
**6 Full Read** · **78 Light Read** (the per-paper checklist pass) · **44 Accept**. Band determines
*depth of tag verification*, never *whether a human ruled* (§42). An earlier design gated review on
**panel agreement** instead; that band was removed — see **§11** for why and for the measured
override rate that settled it.

### 10.3 Instrument
A single frozen vocabulary — **v2.13**, 17 themes + 27 facets = **44 tags** — identical for every
tagger. **Frozen deliberately for gauge constancy**: the instrument must not move while measurements
are being taken with it, so refinements accumulate in `Taxonomy_Changelog.md` and are grafted only at
a versioned cut (§41).

**Which file is the instrument** (corrected 2026-08-26; an earlier draft of this section had these the
wrong way round — see changelog §103):

| File | Role |
|---|---|
| **`slr-phase4/Tag_Prompt_v2.13.md`** | **The instrument of record.** The exact prompt the taggers ran on — vocabulary **plus** task block and JSON output contract — captured verbatim as a standing artifact. Frozen; never edited. Cite **this** in the write-up. |
| `slr-phase4/Tag_Prompt.md` | The operative prompt; currently identical in substance to the v2.13 capture. |
| `slr-phase4/Tag_Cheatsheet.md` | **The living arbiter reference — NOT the instrument.** It has continued to evolve since the freeze and is clearly headed as such. |

The separation is what made gauge constancy hold in practice rather than only in principle: the
cheatsheet accrued `scaling-dissent` (§56), the §49b `framework` clause and the §57 method rules
**during** the pass, and none of it reached the taggers, because the prompt is a physically separate
frozen file. Verified by vocabulary diff — the prompt carries 37 enumerated slugs to the cheatsheet's
38, the difference being exactly `scaling-dissent`.

Versioned prompt captures are the convention (`Tag_Prompt_v0.md` preserves the pre-calibration
original). **Every future prompt change gets its own capture**, so the gauge's history never depends on
reading `git log`.

### 10.4 Input
**Full document text**, not title/abstract — child TXT attachments, roughly 2k–32k words. Tagging is
on what the paper *does*, which cannot be read off an abstract.

### 10.5 Taggers and replication
Three **different vendors**, top reasoning tier — Claude Opus, OpenAI `gpt-5.6-sol` via `codex`,
Gemini 3.1 Pro. Vendor diversity is deliberate **decorrelation**: same-vendor raters share failure
modes, and correlated error is invisible to agreement statistics.
Each model runs the same paper **k=3** times, giving **9 runs per paper**. The replication measures
**intra-model instability** separately from **inter-model disagreement** — a distinction single-run
designs cannot make, and the basis of the `unstable:<model>` tripwire.

### 10.6 Output contract
Per paper, per run: one **primary** theme, all **theme** memberships (multi-label, membership not
mention), any **facets**, and a **≤12-word rationale per tag**, as strict JSON. **Rationale is
required before the code is accepted** — the same constraint Choudhuri et al. impose (§9), and it is
what makes a wrong tag diagnosable rather than merely wrong.

### 10.7 The three-layer namespace
| Layer | Written by | Meaning |
|---|---|---|
| `cal:<model>:*` | the taggers | proposals; never edited |
| `cal:human:*` and `cal:human:reject:*` | the arbiter | endorsement and rejection |
| `final:*` | computed at closeout | the reportable set |

**Final = panel modal ∪ human endorsements − human rejections.** Layers are additive and never
overwritten, so the current state is always recomputable from the record and the record is never
recoverable from the state (cf. the same principle for screening tiers in
`Selection_Criteria_By_Phase.md`).

### 10.8 The three-state human layer (§45/§46)
The arbiter's pass is **deliberately non-exhaustive**, so silence had to be given a defined meaning:
- **endorsement** — `cal:human:theme|facet:*`, additive
- **rejection** — `cal:human:reject:*`, subtractive; needed wherever a panel proposal is **modal**, or
  the deprecated/incorrect tag survives into `final:*`
- **silence** — not considered; the panel proposal stands or falls on its own modality

**Silence is not disagreement.** This is why the assistant prompts the arbiter per paper with the
specific contested tags rather than presenting a full list.

### 10.9 Arbitration
Every Light Read paper gets a human read and an **independent human tier call**; panel unanimity does
not skip the review. A **demote ruling short-circuits downstream tag verification** — Context papers
do not enter Phase 6 synthesis, so their tag depth has no consumer (§42). Effort is proportional to
what the tags are used for — to **downstream consequence**, never to panel agreement (§11.8).

The panel's role here is **recall**: it holds the whole vocabulary against every paper so the arbiter
does not have to. Its proposals are **suggestions, never facts** — measured at T0, **8.3% of
panel-modal proposals were overturned** by the arbiter (§11.5).

### 10.10 What the design deliberately does NOT do
- **No feedback between raters, and no revision rounds.** Taggers never see one another's output. The
  panel is not run to reach consensus; **disagreement is the measurement**, and averaging it away
  would destroy the signal the panel exists to produce.
- **No model adjudicates another model.** Only the human resolves conflict.
- **No instrument changes mid-measurement** (§10.3).
- **No tier decided by the panel.** Models propose tags; tier is always human.

### 10.11 Reliability reporting
Cross-model agreement and κ are computed **between models, treating each as a rater**; the human is
kept as an independent baseline via the blind-first Set B design (§1). Known measured facts to carry
into the write-up: primary-theme assignment is reliable, secondary multi-label breadth is where the
noise concentrates (§3.1–3.2), and model signatures show directional bias (§3.3).

### 10.12 Still open at time of writing
- `final:*` has not been computed; it is a closeout step.
- Whether to re-run the panel on the revised instrument after the Light Read pass closes is
  **undecided** (§41).
- A restricted re-run is queued for tags the frozen instrument never contained — `agent-panel`,
  `cross-model`, the `evaluated-*` ladder, `scaling-dissent`, `evaluator-reliability`,
  `evaluated-real-data`.
- **Plus `oversight-scaling-inversion` v2** (changelog §89), which differs in kind from the rest: the
  others are tags the instrument never had, whereas v2 **competes with an existing tag**. Its
  definition leads with the **leakage test** — *risky code escapes the review that should have caught
  it* — and names maintainer burden, queue growth, falling throughput and displaced work as
  insufficient (§88). **Needs its own slug**, because the namespace records *who* proposed a tag but
  never *which instrument version* produced it; reusing the slug would silently merge two constructs
  in `final:*`. Running both makes the reclassification delta a **reportable measurement** of how far
  definitional wording drives tagger behaviour.
- **Re-check the 15 papers carrying `oversight-scaling-inversion` on arbiter silence** before
  computing `final:*` (§87/§88). 4 of the 10 examined cases were rejected, and the leakage test raises
  the bar further, so this is the **largest known single source of tag error in the corpus**. The v2
  re-run answers much of it automatically if the slug is kept distinct.
- **A closeout sweep is owed for deprecated tags that are still panel-modal.** `counterpoint` (§56)
  survives into `final:*` on any paper where it was modal and never rejected, since silence lets a
  modal proposal stand. Handle as one bulk act rather than per paper, so the deprecation is a single
  auditable event.
- **T1 and T2 measurement points are outstanding** (§11.9). Regenerate with
  `slr-tools/tag_layer_stats.py`; T0 is frozen at `slr-phase4/data/tags-v213/tag_layer_stats_T0_2026-08-26.json`.
- **Human override rate is the headline reliability figure** and is computed by that script —
  8.3% at T0, to be recomputed on the closed corpus.

---

## 11. HOW THE PROCEDURE EVOLVED — and why the confidence gate was abandoned (2026-08-26)

§10 states the method as it now stands. This section records **how it got there**, because the
single largest change — from confidence-gated sampling to full human supervision — was forced by
measurement rather than chosen up front, and a methods chapter that presents the end state as if it
were the design would be misrepresenting it.

### 11.1 Provenance of the instrument — co-authored, not machine-generated
The controlled vocabulary was **not** produced by the models that later applied it. Its chain:

1. **Emergent** — derived bottom-up from the extracted core full texts (`Emerging_Themes.md` →
   *Tag reference*), not imposed a priori from the literature.
2. **Co-authored** — machine-drafted, human-revised, iteratively. Neither party authored it alone.
3. **Human-locked before any coding** — v2.13 approved by the arbiter *before* the panel ran.
4. **Calibrated** — Sets A/B/C sharpened boundaries and produced the discriminators.
5. **Frozen** for the measurement pass (§41).
6. **Gaps found in use** — accumulated in `Taxonomy_Changelog.md`, grafted only at a versioned cut.

Steps 1–3 map stage-for-stage onto Choudhuri et al.'s S1→S2→S3 (§9): independent machine theme
discovery, codebook reconciliation, then **author review and approval before coding**. The
provenance therefore matches a published precedent rather than requiring a defense from first
principles. Step 6 is the stage their pipeline does not have, because they coded once.

**Why this matters beyond bookkeeping:** a machine-authored, machine-applied vocabulary would be the
panel grading its own homework at the instrument level. Co-authorship, human lock, and human-driven
revision each break that.

### 11.2 The design as originally specified — a confidence-gated triage ladder
The 2026-07-21/22 design (§5) routed papers by **panel agreement**:

| Consensus | Disposition |
|---|---|
| 3/3 | **ACCEPT** — auto-accepted, covered only by a 10% seeded random audit |
| 2/1 | LIGHT-REVIEW |
| split | HUMAN |

Replication was **disagreement-triggered**, not universal: *"unanimous first-pass papers are never
replicated."* Sampling was to begin at the sweep. Under that design most of the corpus would have
received no human read.

### 11.3 Why it was wrong in principle — the ACCEPT band violated producer-independence
Panel agreement is **the producer's own signal**. Gating review on it lets the thing being checked
decide whether it needs checking — precisely the failure the corpus documents when practitioners
delegate review to the generator (§71), and precisely what `risk-routing`'s producer-independence
clause forbids (§74).

This reframes the change as a **principled correction rather than a reaction**: the flaw was present
at design time, and the errors below were its *detection*, not its cause.

### 11.4 Why it was wrong in practice — measured unanimous error
| Instance | Panel | Arbiter |
|---|---|---|
| `WUUDHL8R` — `regulatory-compliance` (§44) | **9/9** | rejected: the Act is motivation, not contribution |
| `WUUDHL8R` — `hitl-workflow` (§46) | 8/9 | rejected |
| `PR4GS7SP` — `rules-based-checks`+`formal-methods` (§51) | **9/9** | rejected: benchmarking oracle, not a deployable check |
| Maes — `counterpoint` (§64) | 8/9 | **polarity inverted** — a thesis-*supporting* paper read as opposition |
| `9MV2IVNU` (Eze) — `demote:context` (§53) | **9/9** | **overruled; kept Core** — the tier half of the same finding |

**Vendor decorrelation reduces correlated error but does not eliminate shared misreadings of the
instrument, and those are invisible to agreement statistics.** Unanimity measures how legible the
cheatsheet is, not whether the tag is true.

### 11.5 The measured override rate — the figure that settles it
Over the 57 Light Read papers adjudicated at T0, across **515 panel-modal proposals** (≥2 of 3
models):

| | n | % |
|---|---|---|
| human endorsed | 374 | 72.6% |
| **human rejected** | **43** | **8.3%** |
| human silent (stands on modality) | 98 | 19.0% |

Plus **29 non-modal (1/3) proposals rescued** by human endorsement — found by the panel, and
discarded by any consensus rule.

**Roughly one modal proposal in twelve is wrong.** A 3/3 auto-accept band would have shipped those
into the reported statistics. This single figure carries the argument better than the anecdotes in
§11.4, and it is recomputed at every measurement point (§11.9).

### 11.6 What the panel is actually for — recall and coding consistency
The correction is **not** that the panel is untrustworthy. It is that panel output has a different
epistemic status: **proposals, not facts.** The division of labour follows cognitive strength:

- **Panel → recall.** Holds the entire vocabulary against every paper, every time. Human working
  memory cannot do that reliably across 44 tags and 128 papers; that is the failure the panel fixes.
- **Human → precision.** Validates each proposal against the text.

Supervision is therefore **validate-not-reproduce**, which is the same efficiency the oversight
literature runs on — and §52's inversion is what happens when validating stops being cheaper than
producing. This procedure sits on the working side of that line.

**Consequence for the statistics:** the panel measures **reliability** (inter-rater agreement across
vendors; intra-rater repeatability via k=3). The human is the **criterion**, so agreement with the
human is **validity**. Reliability is *necessary but not sufficient* for validity — three raters can
be perfectly consistent and consistently wrong, which is exactly `WUUDHL8R` at 9/9. High κ therefore
never licenses skipping the criterion.

### 11.7 The anchoring limitation — real, measured, and narrower than expected
Supervision creates an obvious risk: validation is **anchored by what gets proposed**. A tag no
model offers is one the arbiter is less likely to add — automation bias in our own instrument.

At T0 the effect is measurable, and the design happens to contain its own control. The blind-first
calibration band (§1) had the same arbiter tag the same instrument **without seeing proposals**:

| Band | human tags | originated by the human |
|---|---|---|
| Light Read (supervised) | 438 | **8.0%** |
| Calibration (blind-first) | 157 | **80.9%** |

But **17 of the 35 Light Read originations are post-freeze tags the panel could not propose** —
`evaluated-synthetic`, `agent-panel`, `cross-model`, `evaluated-benchmark`, `evaluator-reliability`.
Excluding what was unreachable, human origination against the vocabulary the panel *could* see is
**~4%**.

**So the limitation lands somewhere more useful than "the arbiter gets anchored": panel recall on
its own vocabulary is ~96%, and the real bound is that a frozen instrument caps what can be proposed
at all.** The mitigation is instrument revision (§41 graft + restricted re-run), not more human
vigilance.

Three caveats belong in the write-up rather than in a reviewer's question:
- **"Originated" means absent from every model's *modal* set.** Only modal tags reach Zotero, so a
  1-of-3-run proposal counts as originated; 8.0% is an **upper bound**.
- **80.9% vs 8.0% is directional, not an effect size.** The blind-first pass was an *exhaustive*
  coding; the supervised pass is deliberately non-exhaustive (§10.8, silence = not considered). The
  share attributable to anchoring versus to intended design is not separable from these data.
- **Because the vocabulary was co-authored with the arbiter**, recall is measured against a *shared*
  instrument, not independent ground truth. Standard for codebook studies; still ours to say.

### 11.8 What survives from the ladder, and the two axes
The triage ladder was not deleted — it was **demoted from gate to sort order**. Tripwires (sprawl,
`unstable:<model>`, demote flags, split primaries) still **rank attention and mark contested
surface**; they no longer **grant exemptions**.

Two axes, deliberately independent:

| Axis | Scaled by | Rule |
|---|---|---|
| **Whether** a human rules | nothing | 100% — every paper, tags and tier |
| **How deep** verification goes | **downstream use** | Core → full scrutiny; Context → §42 short-circuit |

Depth is never scaled by panel agreement. Because coverage is total, **there is no sampling-error
argument for the methods chapter to make**, and the 10% seeded audit is moot.

This is itself risk-routed oversight: earlier weeding was low-consequence and was delegated to
models with sampling-based oversight; final tagging produces the reported statistics and is
therefore fully supervised. The routing signal is **downstream consequence**, not confidence.

> **Reflexivity guardrail.** That convergence is a **worked illustration, not evidence.** It is n=1
> self-observation and does not enter the findings — the same rule that keeps HOS's architecture out
> of the instrument. It earns a paragraph in the methods chapter answering *"why review everything,
> isn't that expensive?"* and nothing more.

### 11.9 Instrument drift, and the measurement points
The instrument grew in use. At T0:

| | count |
|---|---|
| **v2.13 frozen** — what the panel ran on | **44** (17 themes + 27 facets) |
| **Cheatsheet today** | **45** (17 + 28) — `scaling-dissent` added (§56); `counterpoint` retained as a deprecated tombstone |
| **Live in Zotero, Phase 5** | **50** (18 themes + 32 facets) |

Two different comparisons, both worth stating because they answer different questions:

- **Beyond the *frozen instrument* (44) — 6 tags**, i.e. what the panel could not propose:
  `evaluator-reliability`, `agent-panel`, `cross-model`, `evaluated-synthetic`,
  `evaluated-benchmark`, `scaling-dissent`. This is the set the restricted re-run targets.
- **Beyond the *current cheatsheet* (45) — 5 tags**: the same list minus `scaling-dissent`, which was
  grafted at the §56 cut. This is the set still awaiting a graft.

All are human-originated. `evaluated-real-data` is staged with no uses yet.

**Every one of the 45 cheatsheet tags has fired at least once** — no dead vocabulary, which is a
small instrument-validity result worth reporting.

**An instrument revised during use would normally invalidate the measurement.** It does not here
because revisions are **deferred to a versioned cut**: `Taxonomy_Changelog.md` is a **queue, not a
patch stream** — 75 sections of accumulated refinements, none applied mid-sweep (§41). Gauge
constancy is what lets the pass survive the discovery of its own gaps.

Figures are regenerated by `slr-tools/tag_layer_stats.py` at three points:

| Point | State | Question it answers |
|---|---|---|
| **T0** | now, frozen instrument | baseline — `tag_layer_stats_T0_2026-08-26.json` |
| **T1** | Light Read + Accept closed, still frozen | do the T0 rates hold over the full corpus? |
| **T2** | after the restricted re-run on the revised instrument | was the gap the *instrument* or the *panel*? |

**T1→T2 is the informative comparison.** If origination on the post-freeze slugs collapses toward
zero, the gap was the instrument. If the panel still misses them with the definitions in hand, that
is a panel capability limit and a reportable finding.

> **Caveat that must be stated first.** The revised definitions were written **from** the arbiter's
> rulings (§56, §65, and others). T2 therefore does **not** independently rediscover those tags — it
> tests whether the definition is **transmissible**. Worth measuring; not a blind validation.

### 11.10 Earlier changes, with what prompted each
| Change | Prompted by |
|---|---|
| Fable 5 added as a fourth tagger (2026-07-14), later dropped | cost per marginal disagreement not justified once the decisive comparison ran (§3.5) |
| k=3 replication: disagreement-triggered → universal | run-to-run variability observed during assignment; needed to separate intra-model instability from inter-model disagreement (§5) |
| Persona framing evaluated and **rejected** | no measurable effect at panel tier (§8.1) |
| Prompt splitting assessed and **declined** | no length effect at panel tier; three of the four longest papers were unanimous and correct (§8.2) |
| Instrument **frozen**; refinements queued to the changelog | gauge constancy — the instrument must not move while measurements are taken with it (§8.3, §41) |
| `cal:human:reject:*` created mid-pass | endorsement-only could not remove a *modal* wrong proposal from `final:*` (§45/§46) |
| `primary-proposed:` staged-tag convention | let a candidate tag accumulate instances without moving the frozen instrument |
| §42 clarified: demote short-circuits tag verification, but every band still gets a human tier call | separating *coverage* from *depth* once the ACCEPT band was removed |
