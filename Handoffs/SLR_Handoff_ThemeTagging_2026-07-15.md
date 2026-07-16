# SLR Handoff — Theme-Tagging Phase (Calibration → Full Sweep)

**Vibe Coding Governance SLR · Zotero group 6505702 · 2026-07-15**
**Next thing to run (continue in a new chat):** blind **Set B** human calibration → human-vs-model
comparison → finalize the instrument → **full 149-core theme-tagging sweep**.
**At the start of the new chat, invoke the `slr-conventions` skill** (library map, tag vocabulary,
triage criteria) and read `slr-phase4/README.md` + `Methodology/Theme_Tagging_Calibration.md`.
`.envrc` supplies the keys — source it or work from the SLR dir (direnv).

---

## 0. Read-first (the two source-of-truth docs)
- **`Methodology/Emerging_Themes.md`** → the **Tag reference**: the operative vocabulary — 17 themes on
  the **Detect→Triage→Fix→Escalate** spine, 8 facets, boundaries, mnemonics, decision log. *The
  vocabulary is locked; do not re-derive it.*
- **`Methodology/Theme_Tagging_Calibration.md`** → calibration **design + findings** (sample, model
  panel, agreement results, decisions, and §6 reproducibility/versioning/write-safety).

## 1. Where we are (status snapshot)

- **Corpus (unchanged):** 149 cores (114 query + 35 snowball) → full-text; 891–892 contexts →
  abstract-level. (`cores.jsonl` lists 148 after one dedupe.)
- **Vocabulary: LOCKED.** 17 themes + 8 facets, matured bottom-up from the cores + HOS experiential
  findings, then sharpened through 3 vetting papers (VibeGuard `T8E8SCCG`, `M74M3RFJ`, Hedwig
  `T72TU8B5`). Provenance preserved as **v0-vs-current** (`Tag_Prompt_v0.md`/`Tag_Cheatsheet_v0.md`
  = 16 themes + 4 facets, original defs; `Taxonomy_Changelog.md` = the iteration log).
- **Set A (AI calibration, 10 papers, `JFN8693L`): COMPLETE.** All 5 taggers (opus, fable, codex,
  gemini, gemini-fast) ran on **full text** under the refined vocab; source-encoded `cal:<model>:*`
  tags written to Zotero. Key findings:
  - **Primary theme is essentially solved** — 8/10 unanimous across 4 models; the 2 splits are
    ranking calls at known theme adjacencies. Def-sharpening collapsed the Hedwig split to 5/5.
  - **Breadth is contested and is a *disposition, not a vendor trait*** — Fable (a Claude model)
    clusters with Gemini (theme Jaccard 0.86), not with Opus. Two camps: liberal (codex 5.0 / opus
    4.7 themes/paper) vs conservative (gemini 2.7 / fable 2.6).
  - **Opus is the 3-to-1 outlier on the insufficiency layer** (automation-bias, oversight-theater,
    tooling-supply-chain, oversight-scaling-inversion) — the substantive limits-of-oversight themes.
    A model-majority vote would systematically drop exactly those. Reproduces Stage-3: **model
    consensus ≠ human; Opus ≈ human.** → Do NOT auto-assign secondary tags by model majority.
- **Instrument is FROZEN** through Set B (don't tune to model consensus — the known-wrong target).
- **Infrastructure hardened today (2026-07-15):** whole SLR now in private GitHub `thurlow-research/SLR`;
  Zotero keys rotated + split **RO/RW**; write tooling defaults to dry-run + `--commit`; skills
  re-released secret-free (v0.1.1). See calibration doc §6.

## 2. The immediate next task — Set B (human-vs-model)

**Set B — "02-Human Calibration Run"** (Zotero `IURU9UTA`), 10 papers disjoint from Set A:
`B644HQFS 6DXZGHD9 E95T8E88 7V7SRG43 UW2R6BBJ BAWCBT9R E3E5YA2E 5VTAJISY TF56EPIP R4WJZBSF`.

1. **Scott tags Set B BLIND first** — packet delivered (`slr-phase4/SETB_Human_Packet.md`; Zotero
   Actions menu `slr_human_tags_actions.yml`). Blind-first preserves an unbiased human baseline. Do
   not run the models on Set B until the human tags are in (write them as `cal:human:*`).
2. **Run the 3–5 models on Set B** (same frozen instrument, full text) → write `cal:<model>:*`.
3. **Compute human-vs-model agreement** (primary match; theme-set Jaccard; per-theme confusion).
4. **The decisive test:** does the human tag `automation-bias` / `oversight-theater` /
   `provenance-auditability` where **only Opus** did? → settles whether Opus's breadth is correct or
   over-reaching, and sets the **breadth policy** for the full sweep.
5. **Iterate the instrument ONCE**, anchored on the human tags: calibrate the breadth rule in the
   prompt; sharpen the 3 fuzzy boundaries (`oversight-explanation`, `rules-based-checks`,
   `provenance-auditability`); add/trim insufficiency-layer cues. Bump `Taxonomy_Changelog.md`.

## 3. Then — the full 149-core sweep

- Run the finalized instrument over all 149 cores. **Primary theme** is reliable enough to
  model-assign with a light human check; **secondary breadth** follows the Set-B-agreed policy, with
  the long tail human-confirmed.
- Promote agreed calibration tags from `cal:*` to plain **`theme:<slug>`** / facet slugs (the `cal:`
  prefix is the fully-reversible staging layer).
- Then **extend `survey-input` / `lit-review`** across the 891–892 contexts (that's where most live;
  tags are orthogonal to disposition).
- Handle any `demote:context` flags (a core that reads like it belongs in another disposition):
  batch-review, move, remove the flag.

## 4. Tooling / how to tag (write-safety updated)

- **Invoke `slr-conventions`** for criteria + vocabulary; the `zotero` skill for library queries.
- Tag pattern (additive, version-locked, skip-if-present): `GET /items/{key}` → append `{"tag":"…"}`
  if absent → `PATCH` with `If-Unmodified-Since-Version`. Calibration writer: `slr-phase4/tools/write_tags.py`
  (replace-mode per tagger). For anchors, also `POST /items` a child note (itemType:note, parentItem).
- **Keys are split (least-privilege):** `.envrc` has **`ZOTERO_API_KEY_RO`** (reads) and
  **`ZOTERO_API_KEY_RW`** (writes) — use RO for GETs, RW only for the PATCH; single `ZOTERO_API_KEY`
  is the fallback. `ZOTERO_LIBRARY_ID=6505702`. The custom Zotero skills now **default to dry-run**;
  pass `--commit` to actually write. **Back up the library (`File → Export Library`) before writes.**
- Lessons from Set A (carry to the full run): run **one tracked process** (don't double-background);
  normalize concurrent-writer JSON to the first valid object; re-run fills empty-output gaps (idempotent
  `[ ! -s ]` guard); Zotero PATCH returns **204 empty body** — don't `json.loads` it.

## 5. Reference docs & repos

- `Methodology/Emerging_Themes.md` — **Tag reference** (locked vocabulary). *Operative.*
- `Methodology/Theme_Tagging_Calibration.md` — design + findings + §6 reproducibility/write-safety.
- `slr-phase4/README.md` — phase home + file map; `Taxonomy_Changelog.md` — v0→current iteration log.
- `Methodology/HOS_Seeded_Theme_Candidates.md` — the HOS-seeded theme graft backlog.
- `Methodology/Problem_Statement_Evidence.md` — the inversion (T0), anchors, validity caveats.
- `Methodology/SLR_Status_Update_2026-07-08.md` §3 — authoritative core/context scope bar.
- Repos: SLR = private **`thurlow-research/SLR`** (root = OneDrive SLR dir); skills =
  **`thurlow-research/ResearchClaudeCodeSkills`** (v0.1.1, secret-free; desktop zips under `desktop/zips/`).
- Memory: `theme-tagging-vocabulary`, `slr-bootstrap-context`, `model-screening-calibration`,
  `stage3-qa-findings`, `zotero-library-structure`.

## 6. Definition of done (theme-tagging phase)

Set B adjudicated and the instrument finalized once against the human baseline; every core carries its
synthesis tags (primary + calibrated secondary breadth); `survey-input`/`lit-review` extended over the
relevant contexts; agreed tags promoted from `cal:*` to plain `theme:`/facet slugs; each `theme:<slug>`
has a corpus-grounded anchor + members in `Emerging_Themes.md`. Then → synthesis / Discussion-chapter
assembly from the tag filters.

## 7. Standing working rules (don't skip)

- **Ask before running jobs / writing** — brainstorm and confirm the plan first; authorization is
  scoped and expires when the design changes. Scott often works from an iPad and can't run scripts.
- **Every core is human-confirmed** (model dissent doesn't predict human judgment). Human is the
  arbiter on the breadth split.
- **Scan staged content for key-shaped secrets before any commit** (global rule).
