# SLR Handoff — Theme Tagging (Calibration COMPLETE → Sweep-Ready)

**Vibe Coding Governance SLR · Zotero group 6505702 · 2026-07-22 (supersedes the 2026-07-18 handoff)**
**Next thing to do: Scott rules on the ZUM76CCG pilot packet (5 questions) → Set C pilot closes →
fire the 128-core sweep (needs Scott's explicit go).**
**At the start of the new chat: invoke `slr-conventions`, read this file**, then
`slr-phase4/data/tags-v213/setC_pilot_ZUM76CCG.md` (the open review packet),
`Methodology/Theme_Tagging_Calibration.md` §5·7 + §7 (pilot protocol, co-tagging, §7 rows 11–20),
and `slr-phase4/Taxonomy_Changelog.md` §19–§30 (this session's rulings). `.envrc` supplies keys
(RO reads / RW writes). Memory notes `theme-tagging-vocabulary` + `fable-run-authorization` current.

---

## 1. Where we are

- **Instrument frozen at v2.13** — 17 themes + **27 facets**, menu **45 toggles (imported)**.
  Session products = changelog **§19–§30** (v2.1 → v2.13 in three days, every rule paper-derived).
  Staged candidates with armed tripwires: `benchmark-evaluated` (seed UB2EVUFU/ProjDevBench),
  `risk-quantification` family.
- **Set B COMPLETE** (§7 rows 11–20): all 10 human-tagged under **co-tagging** (human = ALL tagging
  judgment; AI = post-blind QA only; blind snapshots preserved for all ten as pre-audit Zotero
  versions — listed in §7). 3/10 demotes (BAWCBT9R, TF56EPIP, E3E5YA2E) = Set A's rate exactly.
  UW2R6BBJ = first zero-QA-delta human set. Corpus firsts: `adopted` (HULA), `expert-validated`
  (UW2R6BBJ), `routing-signal` (E95T8E88).
- **v2.13 blind panel run on all 20 calibration papers** (`data/tags-v213/`): **opus 17/20
  primaries (facet-J .71) · gemini 14/20 · codex 13/20**; fable ran the contested six ONLY (4/6,
  facet-J .85 on the hardest papers). **Standing panel = opus + codex + gemini. FABLE (and by
  arbiter caution any premium tier beyond the three) runs ONLY with Scott's explicit per-run
  permission** — standing directive, in memory.
- **Universal-miss papers** (all models, different wrong answers): TF56EPIP (sprawl; nobody
  demoted) and B644HQFS (all models chose oversight-scaling-inversion vs the human's documented
  quality-debt altitude ruling — a recorded legitimate divergence, not an error class).
- **Leakage caveat (standing disclosure):** calibration papers named in the instrument score
  inflated — keys/names are inert tokens to models EXCEPT when self-referential (`PAPER KEY: X`
  matches a rule naming X). Sweep papers are unnamed → unaffected. Optional systemic fix (model
  prompt uses anonymous descriptors; human copies keep keys) — **arbiter decision pending, not
  urgent**.

## 2. The production pipeline (built, validated, exercised)

`tools/triage_v213.py` — the Jidoka ladder: **L0** schema → **L1** consensus (3/3 → ACCEPT + **10%
seeded audit (seed 714)**; any disagreement → **RERUN-NEEDED**) → **replication stage** (2 extra
runs/model on contested papers only; modal votes; modal-3/3 = ACCEPT "noise-resolved"; persistent
2/1 = LIGHT-REVIEW; persistent split = HUMAN) → **L2 computed tripwires** (sprawl >6 themes, any
demote flag, **within-model instability** = the operationalized low-confidence signal — computed,
never self-reported) → per-tag facet voting (3/3 accept · 2/3 noted · 1/3 drop-logged).
- Retrospective validation (n=20): ACCEPT 7 (1 divergence = the documented B644HQFS ruling),
  LIGHT-REVIEW consensus proposals 10/10 correct, HUMAN = exactly the 3 hardest papers.
- **First live replication (ZUM76CCG) REVERSED a noise-built consensus**: codex stable
  risk-routing ×3, gemini stable org-governance ×3, opus unstable (1 rr, 2 og) → modal consensus
  org-governance 2/1 + `unstable:opus`. Replication separates noise-ambiguity (auto-resolved)
  from genuine ambiguity (reaches the human with accurate leaning).
- Runner `tools/run_setb_panel.sh` (codex arg-mode, gemini via `agy --add-dir` file-read — never
  `--dangerously-skip-permissions`; **`< /dev/null` on CLI calls** — codex hangs reading stdin in
  background contexts). Opus runs = fresh-context subagents fed the per-paper prompt file.
- Sweep workload projection: ~43% papers contested → replicates; human load ≈ 20–25 deep reads +
  ~45 light confirmations of pre-filled proposals + 10% audit of accepts (likely lower after
  noise-resolution).

## 3. OPEN QUEUE (in order)

1. **Scott rules on ZUM76CCG** (packet: `data/tags-v213/setC_pilot_ZUM76CCG.md`, incl. replication
   addendum): (a) primary — org apparatus vs use-case-level allocation; **this sets the altitude
   precedent for classification frameworks** (panel modal now leans org-governance 2/1);
   (b) intro-framing vs design-only+metrics contradiction (opposite reads of buildable detail);
   (c) demote — unanimous, §30 look-at-keeping likely doesn't trigger (classification ≠ regulatory
   dive; UW2R6BBJ holds that slot); (d) mode both — confirm; (e) risk-overreliance 2/3 keep/drop.
   Pilot protocol: Scott reviews ALL Set C papers; sampling starts only in the sweep.
2. **Close Set C pilot → fire the 128-core sweep** — needs Scott's explicit go + TXT availability
   check for the 128 (only calibration TXTs confirmed local). Write accepted tags as plain
   `theme:`/facet slugs only after Scott approves the write plan (library backup first).
3. Then: extend `survey-input`/`lit-review` over ~890 contexts; risk×mitigation matrix (recipe in
   Tag reference); batch demote review; the staged-candidate tripwires.

## 4. Session rulings (encoded — do NOT re-litigate; changelog § given)

`design-only` (§19; F9JM9CI6 = inclusive-side example, arbiter overrode assistant) · `metrics` +
measurand-vocabulary + **define-only ≠ theme membership** (§20; R4WJZBSF first catch) · risk-flag
family, **source-agnostic** (harm regardless of code source; general-code segments; general-ai
still excluded) + **lit-reviews CAN earn flags via focal synthesis** (2CKL96B8 reversal) (§21–§22,
§27) · what+how core-bar carve-out (names-elements + defines-metrics = clears bar (2) unevaluated;
**exclusion**: tool/judge self-reliability metrics = tool validation → context, BAWCBT9R) (§23,
§27) · method family + **world-or-tool test** + **subjects-may-be-systems** (§25–§26) ·
`expert-validated` promoted (judges-the-contribution vs produces-the-data; UW2R6BBJ) (§28) ·
`routing-signal` (**signal-without-allocation caught the human blind twice**; mutually exclusive
with theme:risk-routing; framing test) (§29) · general-AI **sole-exemplar exception = "look at
keeping," not "keep"** (UW2R6BBJ kept core; sunset clause if a second exemplar appears) (§30) ·
`adopted` **pilot rule** (study-site vs user) · `lit-review` **framing-section rule** (facet =
paper's role).

## 5. Model signatures (updated for the sweep)

- **opus**: best accuracy (17/20) BUT flickers on genuine boundary papers (ZUM76CCG 1-of-3 flip) —
  instability tripwire matters most for it; misses concentrate on altitude coin-flips + sprawl.
- **codex**: very stable run-to-run; signatures = drift-as-primary (component outranks
  contribution), org-governance↔regulatory-compliance conflation on compliance papers, breadth.
- **gemini**: very stable run-to-run; **Lumen regression 3rd strike** (reverted to the §11
  hitl-workflow error despite instrument text) — its primaries on multi-mechanism papers keep the
  prescribed human check; occasional spurious demote (Lumen).
- Sprawl papers (TF56EPIP-class multi-genre) defeat all models AND their demote detection — the
  sprawl tripwire (>6 themes) is the only reliable catch.

## 6. Ops cautions

Zotero Actions-menu **self-select hazard** (scroll can silently toggle the focused item; caught
twice) → post-paper server-side verification is standing protocol; client↔server **sync lag**
(re-check after Zotero sync before diagnosing); Zotero API transient 502s (retry w/ backoff);
primaries are TYPED (`cal:human:primary:theme:<slug>` — one malformed primary was schema-fixed);
prompt files live in scratchpad only (copyrighted full texts never staged); secret-scan before
every commit.

## 7. Side-project intel worth keeping (Hedwig prompt-optimization assignment)

The assignment artifacts in `Handoffs/` (context pack, three de-referenced prompt vintages,
hold-out audit) are a **side project — do not maintain**. Two findings graduated into mainline:
1. **Run-to-run variability is real and decision-changing** → became the disagreement-triggered
   replication stage (§2). CLIs offer no temperature/seed control — characterize, don't eliminate.
2. **Leakage mechanism precisely identified**: instrument keys/names are inert to models except
   when self-referential to the paper under test — grounds for the standing leakage disclosure
   and the optional descriptor-based systemic fix (§1).

## 8. Data map

`slr-phase4/data/tags-v213/{opus,codex,gemini,fable}/<KEY>.json` (+`.r2/.r3` replicates) ·
`human_gold.json` (adjudicated, authoritative) · `comparison_summary.json` ·
`setC_pilot_ZUM76CCG.md` + `setC_pilot_dispositions.json` (OPEN) · `calib_sets.json` (setA/B/C) ·
older vintages `tags/`, `tags-v1/`, `tags-v2/`, `tags-v21/` · tools: `triage_v213.py`,
`run_setb_panel.sh`, `write_tags.py` (legacy, replace-mode). Repo main @ `7cce709`+, all pushed.
