# SLR Handoff — Theme Tagging (Full-Read Cleanup + Facet Consistency Pass)

**Vibe Coding Governance SLR · Zotero group 6505702 · 2026-08-22 (supersedes the 2026-07-22 handoff)**
**Next thing to do: Scott finishes the remaining Light Read + Synthetic-Eval-Check QA confirmations
→ THEN execute the Phase 6 demotion batch (below) → THEN fire the new facet-add-on sweep.**
**At the start of the new chat: invoke `slr-conventions`, read this file**, then
`Methodology/HOS_Seeded_Theme_Candidates.md` (all staged facets, current definitions), and
`slr-phase4/Taxonomy_Changelog.md` §33 (this session's rulings). `.envrc` supplies keys
(RO reads / RW writes).

---

## 1. Where we are

Machine sweep (128 non-calibration cores) was already complete going into this session (see the
2026-08-15/16 sweep record in `Methodology/Theme_Tagging_Sweep_2026-08.md`). This session was
**arbiter full-read cleanup + instrument consistency work**, not more machine tagging:

- **Two HUMAN-bucket contested papers fully resolved** (of the original 6: 8AW26GFK, HBR7QZ2C,
  S7FPFUT8, VCI88UZD, WRXR2VTP, Y4TIF9KW):
  - **Y4TIF9KW** (Code Prism) — primary settled at `regulatory-compliance`, secondary
    `org-governance`, facets `agentic`/`built-system`/`expert-validated`/`risk-security`. Matches
    Opus's read exactly (the one panel leg stable across all 3 replicates); Codex drifted off it,
    Gemini never reached it. `theme:ai-code-insecurity` was tried and dropped — the paper audits
    for security, it doesn't evidence AI-code insecurity; `risk-security` facet alone carries that.
  - **VCI88UZD** (Human-certified module repositories) — primary `tooling-supply-chain` (a
    deliberate scope-widening call: this paper is exactly the "classic SolarWinds-class" case the
    tag's own exclusion note currently rules out — walking that back needs its own changelog entry
    if it stands past this cleanup pass). **Full-read verdict: demote to Context** — minimal AI
    involvement (one sentence: "AIs should pull from trusted repos"), no operationalized mechanism,
    states the need without specifying it. Tagged `demote:context`, **NOT yet moved** (see §3).
- **`7SH86C2W`** (Shift-Up framework) resolved off the `evaluated-synthetic` candidate list: single
  self-selected, non-repeated scenario (one snack-bar web-app build, journaled), explicitly
  self-labeled exploratory/preliminary — sits at the plain `self-tests` (untagged) rung, no new tag
  needed. Considered and **rejected** a separate `ad-hoc-evaluated` tier (bare-smoke-test vs.
  real-single-case-effort) — no corpus instance yet exists that's *weaker* than this one, and the
  split wouldn't change any synthesis claim. Full reasoning in `HOS_Seeded_Theme_Candidates.md`.
- **Facet rename (no definitional change):** `benchmark-evaluated` → `evaluated-benchmark`,
  `synthetic-evaluated` → `evaluated-synthetic` — sort adjacency only. 12 Zotero items re-tagged
  (`slr-tools/rename_eval_facets.py`), all doc references + `slr_human_tags_actions.yml` menu
  updated. `expert-validated` considered for the same treatment and **explicitly declined** — it's
  promoted/live in the frozen v2.13 instrument with real machine-panel history (9 Zotero tags + 22
  raw JSON outputs across opus/codex/gemini); renaming it would mean editing frozen instrument text
  and/or rewriting machine audit trail, which the staged-only facets never required. Left as-is.
- **Two new facets staged: `agent-panel` + `cross-model`.** Motivated by a structure/function
  conflation already sitting in `theme:ai-review`'s own text ("single-reviewer, multi-agent panels,
  and independent/cross-model review"). `theme:ai-review` **unchanged** (fires whenever AI
  judges/checks an artifact, any architecture underneath). `agent-panel` = multiple agents
  involved, any capacity (composes with generation OR review). `cross-model` = those agents are
  different vendors, not multiple instances of one (modifier on `agent-panel`, never on
  `ai-review`). Corpus check (grep for named vendors across 13 strong `ai-review` candidates, not
  yet full-text-confirmed): **10/13 genuinely cross-vendor**, 1 same-vendor (HBR7QZ2C — the
  `agent-panel`-without-`cross-model` worked example), 2 inconclusive. Preliminary read:
  cross-vendor composition looks like the *dominant* pattern in this corpus's multi-agent review
  solutions, not the exception — real dissertation-relevant signal once confirmed. Full naming
  trail (rejected: "adversarial-review", "cross-examination" — checked against the corpus, means
  something different there) in `HOS_Seeded_Theme_Candidates.md` and `Taxonomy_Changelog.md` §33.
  **HOS is explicitly not evidence for this** — the corpus check is what grounds it, per the
  standing HOS-reflexivity guardrail.

## 2. Session rulings (encoded — do NOT re-litigate; changelog §33)

Facet rename for sort adjacency (`evaluated-benchmark`/`evaluated-synthetic`), `expert-validated`
left unrenamed (frozen-instrument + machine-audit-trail reasons), 7SH86C2W resolved to untagged
`self-tests` (ad-hoc tier considered and rejected, no seed instance), `agent-panel`/`cross-model`
staged with corpus grounding. All four new/renamed facets are **staged, human-only overrides**
(`cal:human:facet:*`) — **not** grafted into the live v2.13 `Tag_Prompt.md`/`Tag_Cheatsheet.md`
instrument, to preserve gauge constancy. That graft decision is explicitly deferred, likely to
whenever the ~890-item Context tier's own gauge-qualification probe happens (§3 of the paper
outline already flags that as a separate future decision point).

## 3. OPEN QUEUE (in order — Scott's explicit sequencing)

1. **Finish the remaining Light Read confirmations + Synthetic-Eval-Check workbook** (the 21-item
   `Phase 5 - Reading / 05 - Synthetic-Eval Check` collection; several already confirmed this
   session — see `cal:human:facet:evaluated-synthetic`/`evaluated-benchmark` tags currently live).
2. **THEN execute the Phase 6 demotion batch.** Currently **tagged but not moved**:
   `demote:context` is applied to **7 items** — VCI88UZD, S7FPFUT8, UDVHQ5HR, BAWCBT9R, E3E5YA2E,
   TF56EPIP, 2CKL96B8 (full per-item collection-swap plan, verified against the M74M3RFJ
   precedent, already written out in this session's transcript — Queries-stream items swap
   `539H8RBQ`→`85JVIR9X`, Snowballing-stream S7FPFUT8 swaps `UPTNJTIS`→`WX9WW6A7`, all swap
   `3S9B658S`→`QE8TWEJQ` at the Final level). Plan also includes creating a new **top-level
   `Phase 6 - Full-Read Demotions`** collection (parallel to Phase 1–5, not a Phase-5 subfolder —
   Phase 5's own numbering is already taken through `04 - Calibration (Adjudicated)`) as an
   additive audit marker, explicitly excluding M74M3RFJ (different provenance — a `general-ai`
   scope-flag demotion from the earlier calibration pass, not this full-read pass). Verified Core
   count going in: **148** (`3S9B658S`); Context: **892** (`QE8TWEJQ`) — will land at **141**/**899**
   once executed. Scott may add more candidates during the remaining full-reads before this batch
   runs — hold everything at the tag stage until he says the full set is known.
3. **THEN run the new facet-add-on sweep** — a narrow, separate, additive machine-panel pass over
   the (post-demotion) Core roster, scoped to *only* `evaluated-benchmark`/`evaluated-synthetic`/
   `agent-panel`/`cross-model` — explicitly not re-litigating themes or other facets already
   settled by the v2.13 sweep. Open design questions for whoever builds it: (a) same pinned models
   as the original sweep (`claude-opus-4-8`/`gpt-5.6-sol` high/`gemini-3.1-pro-high`) for
   comparability; (b) `evaluated-benchmark`/`evaluated-synthetic` are genuine judgment calls and
   probably warrant the full 3-model/replication treatment the original sweep used; `agent-panel`/
   `cross-model` are closer to mechanically extractable (named-vendor detection) and may not need
   the same weight — Scott's call on uniformity vs. cost; (c) name it something like "Facet
   Add-On Sweep" / "v2.13-S1", not "v2.14" (that would imply a full-instrument version bump for
   complete re-tagging, which this isn't); (d) same output mechanism as the original sweep —
   `cal:opus:`/`cal:codex:`/`cal:gemini:facet:*` proposals → triage-ladder → human confirm →
   `cal:human:facet:*`.

## 4. Threats-to-validity note still owed

§3.12 of `Methodology/SLR_Paper_Outline_v0_2026-08.md` already discloses the Set B v2.2→v2.10
instrument-drift confound. This session's facet additions (staged post-sweep, human-only overlay,
never fed back through the frozen v2.13 panel) are the same category of event and should get
folded into that same paragraph when the outline is next touched — not yet done.

## 5. Data map / files touched this session

`Methodology/HOS_Seeded_Theme_Candidates.md` (main staging doc, rewritten section) ·
`Methodology/Emerging_Themes.md` (one reference updated) · `slr-phase4/Taxonomy_Changelog.md` §33 ·
`slr-phase4/Synthetic_Eval_Check_Guide.md`, `Sweep_Reading_Guide.md`, `README.md` (rename refs) ·
`slr-phase4/Tag_Prompt.md`/`Tag_Cheatsheet.md` (parenthetical mention only — live instrument text
otherwise untouched) · `slr-phase4/slr_human_tags_actions.yml` (menu entries renamed + 2 added) ·
`slr-tools/rename_eval_facets.py` (new, the rename script — not idempotent-safe against re-run,
check for existing new-name tags before rerunning).

Separately (not part of this handoff's thread, still uncommitted in the working tree): an
`Outreach/` LinkedIn draft (explicitly held back from any push per Scott) and
`slr-tools/add_ai_incidents.py` (AI Incident Database seeding into the `AI Incidents` Zotero
collection) — both from earlier in the same session, unrelated topic, not bundled into this PR.
