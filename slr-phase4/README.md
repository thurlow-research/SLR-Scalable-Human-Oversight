# Phase 4 — Theme Tagging (synthesis tagging of the corpus)

Home for all working materials of the theme-tagging phase: applying the synthesis
vocabulary (`theme:` / facet / scope / workflow tags) to the corpus, calibrated cross-model
+ human before the full sweep. Started 2026-07-15.

## Canonical methodology docs (live in `../Methodology/`, not here)
- **`Emerging_Themes.md`** — the **Tag reference** (operative vocabulary: themes, facets, boundaries,
  the Detect→Triage→Fix→Escalate spine, mnemonics, decision log). *Source of truth for the vocabulary.*
- **`Theme_Tagging_Calibration.md`** — calibration **design + findings** (sample, model panel, agreement
  results, the def-refinement→convergence loop).

## What's here
| File | What |
|---|---|
| `Tag_Prompt.md` | **The full model prompt** = vocab cheat-sheet + the `# YOUR TASK` block. Prepended to a paper's full text at run time. The durable instrument. |
| `Tag_Cheatsheet.md` | Vocab-only cheat-sheet (source for the human packet + the Zotero menu). `Tag_Prompt.md` = this + the task block. |
| `SETB_Human_Packet.md` | Blind human-tagging packet for Set B (10 papers + template). |
| `slr_human_tags_actions.yml` | Zotero **Actions & Tags** menu import (26 `[SLR]` toggle commands). Also kept in `~/Code/` for import. |
| `tools/run_cli.sh` | Runs `codex` + `agy`(gemini) over the sample. ⚠️ paths are scratchpad-relative — edit `S=` to re-run from here. |
| `tools/write_tags.py` | Writes source-encoded tags to Zotero (replace-mode). ⚠️ same path caveat. |
| `data/calib_sets.json` | The seeded sample: Set A (`setA`) + Set B (`setB`). |
| `data/cores.jsonl` | Title+abstract of the 149 (now 148) cores — the open-coding substrate. |
| `data/tags/<tagger>/<KEY>.json` | Per-tagger tag outputs (opus, fable, codex, gemini, gemini-fast). |
| `txt/<KEY>.txt` | Full-text extractions of the 20 calibration papers (+ TF56EPIP). |

## History / course-assignment artifacts
- `Tag_Prompt_v0.md` — the **original full prompt** (cheat-sheet + task block) fed to the first model
  run, before calibration. Pairs with `Tag_Prompt.md` (current) to show the prompt change.
- `Tag_Cheatsheet_v0.md` — vocab-only v0 (16 themes + 4 facets, original definitions).
- `Taxonomy_Changelog.md` — the **iteration log**: each disparity → diagnosis → change → measured
  outcome (incl. the confound note that *both* definitions and the prompt's task block changed).

## Tag scheme (source-encoded, calibration)
`cal:<tagger>:theme:<slug>` · `cal:<tagger>:primary:theme:<slug>` · `cal:<tagger>:facet:<slug>`
where tagger ∈ {human, opus, fable, codex, gemini, gemini-fast}. Plain workflow flags:
`demote:context`. After adjudication, agreed tags promote to plain `theme:<slug>` / facet slugs.

## Sample (seed 714, from the 149 cores)
- **Set A — "01-AI Calibration Run"** (`JFN8693L`): model panel. All 5 taggers refined + written.
- **Set B — "02-Human Calibration Run"** (`IURU9UTA`): Scott tags **blind** first, then the models.

Model panel: `opus` (Claude Opus) · `fable` (Claude Fable 5) · `codex` (gpt-5.6-sol) ·
`gemini` (Gemini 3.1 Pro High) · `gemini-fast` (Gemini 3.5 Flash High).

## Status (2026-07-15)
- Vocabulary matured through 3 vetting papers (VibeGuard `T8E8SCCG`, `M74M3RFJ`, Hedwig `T72TU8B5`) —
  drove `formal-methods`, `framework`/`built-system`/`adopted`/`general-ai` facets, `org-governance`
  rename, `theme:`/`primary:theme:` scheme, `remediation-gating` + `risk-routing`/`hitl-workflow`
  boundary sharpening, `demote:` flag.
- Set A re-tagged by all 4 models under the refined vocab; primary 8/10 unanimous; def-sharpening
  collapsed the Hedwig split to 5/5 (see calibration doc §).
- **2026-07-18 — design revised (freeze lifted):** Stage 1 = Scott human-tags the calibration papers
  as a **vocabulary-vetting pass** (changes logged in `Taxonomy_Changelog.md` — §10 `assistive`/`agentic`
  mode facets; §11 `oversight-explanation` broadened to push/pull, steering exclusion, Lumen unanimity
  overturn). Stage 2 = human-vs-model experiment on the **vetted** instrument: models re-run Sets A+B
  fresh (Set A human tags model-informed; **Set B = clean comparison** — no model runs there until
  vetting is done). v1-instrument model outputs archived in `data/tags-v1/`. Then the full 148-core
  sweep, then extend survey-input/lit-review over the 892 contexts.
- **2026-07-18 EOD — Set A human vetting pass COMPLETE.** All 10 tagged, verified, adjudicated
  (calibration doc §7 log; `Taxonomy_Changelog.md` §10–§17 = ~20 instrument products). Headlines:
  **two unanimous-model primary overturns** (Lumen §11, 22JBEZNK §16), the VibeGuard recurrence →
  compression-gap principle (§17), 2 new `demote:context` flags (3/10 demote rate — expect a demote
  tail in the sweep). Facets now 14; menu 32 actions. **Next:** instrument-critique panel (§5 step
  1b) → freeze vetted instrument → Scott tags Set B → models retag Sets A+B → comparison.
- **2026-07-19 — `design-only` form facet added mid-Set-B (v2.2, changelog §19).** Positive marker
  for "mechanism specified in buildable detail but never credibly run" (mock demos fabricating their
  own outputs ≠ built), off the R4WJZBSF probe (Set B paper 10, tagged blind; snapshot at Zotero
  v156638 predates the audit). Facets 15; menu 33 (**re-import pending**). Set B papers 1–8 remain
  untagged and model-free.
- **2026-07-20 — calibration rosters reconciled + Set C defined (calibration doc §5·7).**
  Set B = the packet's 10 exactly (`calib_sets.json` fixed); TF56EPIP restored to 02-Human (was
  mis-shelved in 01-AI Calibration Run); ZUM76CCG → new **Set C** [U65X7JNA]: AI-tags-first,
  human-validates — pilots the sweep's production workflow. M74M3RFJ reconciled same day: back in
  01-AI Calibration Run (calibration roster is frozen experiment infrastructure, orthogonal to
  disposition), +`demote:context` (predated the flag), +`design-only`, −`intro-framing`
  (contradiction rule).
- **2026-07-20 — `metrics` contribution facet (v2.3, changelog §20).** Defines-vs-uses guardrail;
  measurand-rationale rule; object via co-tagged themes (`risks` facet considered & rejected —
  mention-saturation); risk-routing boundary: signal-without-allocation ≠ routing.
  Risk-quantification family staged with sweep-cluster tripwire. Facets 16; menu 34
  (**re-import pending**).
- **2026-07-20 — `risk-ip` + `risk-bias` risk-type flags (v2.4, changelog §21).** The harms axis
  for the synthesis risk×mitigation matrix; substantive-treatment bar (never intro-lists); homeless
  types only (themed risks are their own columns); checklist now six questions. Facets 18;
  **menu 36 (re-import pending)**.
- **2026-07-20 — risk family made UNIFORM: + `risk-security`/`risk-quality`/`risk-overreliance`
  (v2.5, changelog §22).** One bar for all five flags; flag = engagement, theme = lift,
  co-occurrence expected; matrix = one query per column. Explainability three-way routing;
  measurand fixed vocabulary; define-only ≠ theme-membership in compressed copies. Facets 21;
  **menu 39 — re-import THIS version** (supersedes today's earlier counts).
- **2026-07-21 — `routing-signal` contribution flag (v2.12, changelog §29).** Positive marker for
  the signal-without-allocation boundary (two blind arbiter catches: R4WJZBSF, E95T8E88); steering
  grammar; framing test; mutually exclusive with theme:risk-routing; Triage supply-chain roster.
  Facets 27; **menu 45 — re-import required** (supersedes 44).
- **2026-07-21 — `expert-validated` PROMOTED from staging (v2.11, changelog §28).** First genuine
  contribution-validation instance (UW2R6BBJ); judges-the-contribution vs produces-the-data
  discriminator; no `method-expert-panel` (surveyed panels = `method-self-report` on the data
  axis; both can co-hold). Facets 26; **menu 44 — re-import required**.
- **2026-07-20 — co-tagging protocol named & documented (calibration doc §7).** Set B's working
  mode: human tags blind → assistant audits vs instrument + full text → arbiter rules → catches
  land in all copies same-day. Yield: v2.2→v2.10 in two days. Blind layer preserved as pre-audit
  Zotero versions (five papers); headline scoring = models vs final adjudicated sets; audit-free
  papers (E95T8E88, UW2R6BBJ, E3E5YA2E, 5VTAJISY) + Set C carry the fully-clean comparison.
- **2026-07-20 — method backfill audit → v2.9 (changelog §26).** Set A method facets backfilled
  (7/10 first-pass); whose-properties triangle + subjects-may-be-systems rules encoded;
  22JBEZNK +experiment, UB2EVUFU −experiment; `benchmark-evaluated` staged (UB2EVUFU/ProjDevBench
  = first instance). Text-only; menu stays 43.
- **2026-07-20 — data-collection method family (v2.8, changelog §25).** `method-self-report` /
  `method-mining` / `method-experiment` / `method-field-study` — own-evidence-only, multi-apply,
  lit-reviews get none; the study-designs axis for synthesis evidence-weighting + the methods
  chapter. Checklist now seven questions. Facets 25; **menu 43 — re-import required** (supersedes
  the 39-toggle import).
- **2026-07-20 — two arbiter rulings encoded (v2.6, changelog §23).** (1) **What+how carve-out:**
  names-the-elements + defines-operationalizable-metrics clears core bar (2) as measurement even
  unevaluated (amends the 2026-07-13 trap clause; encoded in slr-conventions + Status_Update §3 +
  design-only lines; R4WJZBSF kept core, no demote). (2) **F9JM9CI6 = design-only** (stated
  architectural-design contribution meets buildable detail; intro-framing off; Zotero updated;
  full 01-AI-Calibration tag audit clean). Text-only — menu stays 39.
