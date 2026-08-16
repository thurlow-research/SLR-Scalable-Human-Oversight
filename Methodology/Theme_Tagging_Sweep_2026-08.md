# Theme-Tagging Production Sweep — Execution Record (2026-08-15/16)

**Status: machine phases COMPLETE; human review open (Phase 5 - Reading).**
Companion to `Theme_Tagging_Calibration.md` (instrument design + validation, v2.13) and
`slr-phase4/Taxonomy_Changelog.md` §19–§32 (binding rulings). This document records the
*production* run of the calibrated instrument over the non-calibration core corpus.

## 1. Gate-clearing (pre-conditions, all satisfied 2026-08-15)

1. **Set C pilot closed** — ZUM76CCG adjudicated on all five open questions (changelog §32).
   Headline precedent, binding for the sweep: *use-case/deployment-granularity classification
   frameworks prescribing oversight regimes = `org-governance`; `theme:risk-routing` requires
   artifact-granularity selection driven by a computed, producer-independent signal.* One human
   delta vs the pipeline's post-replication proposal (`theme:hitl-workflow` added) — a strong
   validation run for the triage ladder.
2. **Roster frozen** — Phase 3 / 03-Final / Core = 148 items; minus the 20 in-core calibration
   papers = **128 sweep papers** (`data/tags-v213/sweep_keys.json`). The 21st calibration key
   (M74M3RFJ) was already context. Counts verified against Total-Results.
3. **TXT availability** — all 128 have TXT attachments in Zotero (verified per-item via API);
   all cached locally from synced Zotero storage (median ~60 KB; none degenerate; zero API
   downloads needed). Prompt files (instrument + full text) built in session scratchpad only —
   copyrighted full texts are never staged to the public repo.
4. **Arbiter's explicit go** (2026-08-15), per the standing authorization protocol.

## 2. Panel configuration (gauge constancy)

| Leg | Model (pinned) | Harness |
|---|---|---|
| opus | `claude-opus-4-8` | `claude` CLI, `--model` pinned (`tools/run_sweep_opus.sh`) |
| codex | `gpt-5.6-sol`, reasoning high | codex CLI arg-mode (`tools/run_sweep_panel.sh`) |
| gemini | `gemini-3.1-pro-high` | agy file-read via `--add-dir` (`tools/run_sweep_panel.sh`) |

- **Gauge-constancy decision:** the opus leg deliberately runs through the `claude` CLI with an
  explicit model pin rather than session subagents — subagent model resolution follows the
  session default and would have silently swapped the gauge to a newer Opus mid-instrument
  (the exact hazard §31 hardening exists to prevent).
- Every run (including replicates and retries) writes a `.meta.json` provenance sidecar
  (model, effort, CLI version, UTC timestamp).
- Instrument: **v2.13, frozen** (17 themes + 27 facets); identical prompt (`Tag_Prompt.md`) +
  full text per paper. Sweep papers are unnamed in the instrument → the calibration leakage
  caveat does not apply to sweep scores.
- Within-model parallelism: 4 worker shards per model (round 1), 3 (replication).
- Fable excluded throughout, per standing per-run-permission directive.

## 3. Round 1 (128 papers × 3 models)

- Wall-clock ≈ 2.5 h. 128/128/128 valid outputs. One gemini output initially empty (transient
  CLI tool-permission denial) — recovered by idempotent rerun.
- Triage (`triage_v213.py`, seed 714, 10% audit): **ACCEPT 44 · LIGHT-REVIEW 37 ·
  RERUN-NEEDED 47** — a **37% contested rate**, under the ~43% calibration-based projection.

## 4. Replication stage (k=3 on contested only)

47 papers × 3 models × 2 extra runs = 282 runs (`tools/run_sweep_replicates.sh`, suffixes
`.r2`/`.r3`). Modal votes per model; disposition recomputed with replicates present.

**Quality events — all caught by the ladder, none reached the data:**
- **Gemini individual quota exhausted** late in r3 (28 runs failed with a quota error; resets
  ~3.5 h). Automated post-reset retry recovered all 28. *Ops note: budget gemini quota headroom
  for runs > ~250 calls.*
- 2 transient network failures (gemini) — retried clean.
- **3 L0 schema rejections** (gemini): facet slugs emitted in the `flags` array (the mirror
  image of the prompt's "never put flags in facets"). `load_one` correctly rejected the runs as
  illegal-flags; targeted reruns produced clean outputs. This is a new gemini failure signature
  worth watching in the context extension.

## 5. Final triage (all runs in)

| Disposition | n | Notes |
|---|---|---|
| **ACCEPT** | 44 | 3/3 consensus; 9 of the round-1 contested resolved to consensus as pure run-noise ("noise-resolved") |
| **LIGHT-REVIEW** | 78 | modal 2/1 proposals; **18 unanimous `demote:context`** |
| **HUMAN** | 6 | replication-stable three-way splits: 8AW26GFK, HBR7QZ2C, S7FPFUT8, VCI88UZD, WRXR2VTP, Y4TIF9KW |
| RERUN | 0 | — |

- **Replication resolved 41 of 47 contested papers without human involvement.**
- Realized human load: **6 deep reads + 78 confirmations + 4 audit checks** — substantially
  under the projected 20–25 deep reads + ~45 light confirmations.
- Instability tripwires at sweep scale: codex 18 · gemini 18 · opus 17 — roughly uniform,
  unlike calibration (where opus was the flicker-prone leg). Noise is a panel-wide property at
  n=128; the replication stage, not any one model's stability, is what carries the signal.
- Primary-theme distribution (ACCEPT+LIGHT proposals): `ai-review` 31 dominates, then
  `hitl-workflow` 12, `org-governance` 11, `oversight-explanation` 11, `quality-debt` 10,
  `automation-bias` 9 — the Detect stage holds the corpus's uncontested mass. 4 of the 6 HUMAN
  papers have `org-governance` in the vote set (the §32 altitude precedent will govern).

## 6. Human-review protocol (open)

- Review entry point: `data/tags-v213/sweep_review_workbook.md` — buckets **A** deep reads (6),
  **B** unanimous-demote confirms (18), **C** light confirms (60), **D** seeded audit of accepts
  (4: 4T5QFWZE, 5NZ2EDEK, CTGGMIX9, D87A4CAS).
- Zotero reading structure created by the arbiter: **Phase 5 - Reading** [D4JRF4GG] →
  01 - Accept [UIN658B7] (44) · 02 - Light Read [WTKULZ5U] (78) · 03 - Full Read [2WE2DX36] (6).
  Membership added additively (no existing collections touched); pre-write state snapshotted.
- `sweep_s4_tags.json` emitted; **no s4/theme tag writes to Zotero occur until the arbiter
  approves the write plan** (backup → `apply_s4_tags.py` → server-side verification).

## 7. Side additions this cycle

- **`dissertation-input` synthesis tag** (2026-08-15, human-only, never in the model
  instrument): findings the dissertation must engage with directly, beyond SLR corpus role;
  child note required. Seed: UTTJ5N93 (Buçinca et al. 2021 — the oversight-*effectiveness*
  dimension). Documented in `Emerging_Themes.md`; tier unchanged (context, `7BMFG5IK`
  precedent; tier ≠ importance).
- Snowball validation datum: UTTJ5N93, spotted independently by the arbiter while reading
  ZUM76CCG's references, was already in-corpus via co-citation snowballing (`cocite:2`) and
  correctly dispositioned at every stage.

## 8. Next steps (in order)

1. Arbiter works the workbook (A → B → C → D); rulings recorded per pilot protocol.
2. Write plan approval → library backup → `apply_s4_tags.py` for the 128 (+ accepted human
   deltas) → server-side verify.
3. Batch demote review (18 unanimous + accumulated flags).
4. Context extension (~890 items): gauge-qualification probe (k=5 consistency) required before
   any cheaper tier tags contexts; length-as-covariate re-check at n=128.
5. Risk×mitigation matrix (recipe in the Tag reference).
