# SLR Handoff — Theme-Tagging Phase

**Vibe Coding Governance SLR · Zotero group 6505702 · 2026-07-13**
**Next phase to run (continue in a new chat):** theme tagging (+ grafting HOS-seeded themes).
**Invoke the `slr-conventions` skill at the start of the new chat** — it holds the library map,
tag vocabulary, and triage criteria. `.envrc` supplies the Zotero/OpenAlex keys (source it, or
work from the SLR dir).

---

## 1. Where we are (status snapshot)

- **Both source streams triaged and human-reviewed.** Final analysis corpus:

  | Stream | Core | Context | Discard |
  |---|---|---|---|
  | Query | 114 | 716 | 139 |
  | Snowball | 35 | 175 | 41 |
  | **Total** | **149** | **891** | — |

  **149 cores → full-text extraction (Stage 4); 891 contexts → abstract-level.**
- Snowball human review complete + consistency-checked; every decision recorded as `s3:human:<bin>`
  beside the preserved `s3:opus:` vote. Details in `Methodology/Stage4_Snowball_Enrichment_and_Rescreening.md` §9.
- **Collections:** query cores `539H8RBQ`, contexts `85JVIR9X`; snowball cores = `UPTNJTIS`
  (root/promotions) + `RZWBRF2T` (Confirm) + `HFD75W94` (Review), contexts = `WX9WW6A7` + `ZUUGKPK2`
  (Recall) + `MBSRBERI` (Below). **PENDING:** merge both streams into `Phase 3 / 03-Final` (`C22VANXU` →
  Core `3S9B658S` / Context `QE8TWEJQ` / Discard `72SVYQMU`) — currently empty. Do this (or tag off the
  per-stream collections) as a first step.

## 2. What theme tagging is / why

**Synthesis tags** mark *why an item matters to the argument*, **orthogonal to core/context** — they
map to sections of the eventual write-up. This pass builds that map so the Discussion/Themes chapter
assembles from filters rather than re-reading. Full vocabulary + rationale in
`Methodology/Emerging_Themes.md` (tag-vocabulary table).

| Tag | Marks | Paired doc | Seeds already applied |
|---|---|---|---|
| `problem-statement-anchor` | committee-sit-up empirical stat | `Problem_Statement_Evidence.md` | `59KP8GTP`, `3Z45M3V3` |
| `theme:<name>` | cross-cutting theme membership | `Emerging_Themes.md` | `theme:tooling-supply-chain`→`6ZC3H7AF`; `theme:oversight-explanation`→`7UB2MD8Z` |
| `survey-input` | adoption/preference/RAI-priority → org survey | (survey design) | `29NBUJWT`, `K5IAE4E7`, `4J4VK52E`, `I2JHP2ZV`, `8FUS6BKG` |
| `intro-framing` | position/agenda papers for the Introduction | (Intro) | `4TUNZ7FU` |
| `lit-review` | secondary lit / snowball source | — | `CKKGWMRH`, `IM6DJDEE`, `45RNUJ97`, … |

Each tagged item also gets a **child note** (itemType:note) with the framing, for the anchor items.

## 3. Step 1 — GRAFT the HOS-seeded themes first (before the systematic pass)

Source: `Methodology/HOS_Seeded_Theme_Candidates.md` (already written; full detail there). The guardrail:
HOS is the *learning vehicle*, so its findings **seed** theme hypotheses but themes must be **grounded
in the corpus** (HOS findings that are just reading-notes on corpus papers are marked "pass-through").

**Grafting checklist:**
1. **Cross-check the pass-through corpus papers** against the library — Mitropoulos 2026 (framing
   attack), Ferdous 2026 (confidence/refactor-risk), Charoenwet/AgenticSCR 2026 (corroboration-ranking),
   Parris/AIRA 2026 (scanner-masking), Kumar/SWE-PRBench, Watanabe 2026 (agentic-PR size), Loker/CodeRabbit
   2025 (the 1.7× claim). In-corpus? If not, retrieval/snowball candidates.
2. **Ground & add T3 — "The overseer is itself an untrusted, attackable component"** to `Emerging_Themes.md`,
   anchored on those *corpus* papers (not HOS). This is the strongest new theme (the limits-of-oversight limb).
3. **Fold T0 sharpeners** into `Problem_Statement_Evidence.md` — the ⭐"enforcement not knowledge" reframe,
   "task-class not touched-content is the risk axis." (The 1.7× + SonarQube caveats are already added, §5.)
4. Core-criteria rule "**gate on a computed signal, not the model's self-report**" is **already added** to
   `slr-conventions`.
5. **Decide the backlog lenses** (E in the doc: ensemble/cross-vendor review, cost-tiered review economics,
   governance invariants, convergence architecture, interactive-vs-autonomous modes) — promote each only if
   it has corpus support, else leave as HOS-side.

## 4. Step 2 — Systematic theme-tagging pass

**Recommended approach: theme-driven sweep** (the method used for `theme:tooling-supply-chain`):
for each finalized theme, sweep the corpus (Zotero `q=` keyword search + OpenAlex if needed), read
candidates, tag members `theme:<name>`, filtering keyword false-positives (record exclusions like the
supply-chain doc does). Then a lighter pass for `survey-input` (adoption/perception studies),
`intro-framing` (position/agenda), `lit-review` (surveys/reviews), and `problem-statement-anchor` (the
few empirical committee-sit-up stats).

**Scope:** start with the **149 cores** (they carry the argument), then extend `survey-input`/`lit-review`
across the 891 contexts (contexts are where most survey-input/lit-review live). Tags are orthogonal to
disposition — a context item can be a strong `survey-input` or `theme:` member.

**Themes to tag against (after grafting):** T0 inversion (problem-statement anchors), T1 tooling-supply-chain,
T2 oversight-explanation, T3 untrusted-overseer, + any promoted backlog lenses. Expect new `theme:<name>`s
to emerge during the sweep — add them to the vocabulary table as you go.

**Good for parallelism:** a subagent per theme can sweep + return candidate item keys with a one-line
rationale; you then confirm and tag. (This is how the supply-chain + HOS syntheses were done.)

## 5. Tooling / how to tag

- **Invoke `slr-conventions`** for criteria + the tag vocabulary; `zotero` skill for library queries.
- Tagging pattern (additive, version-locked, skip-if-present) — same script shape used all session:
  `GET /items/{key}` → append `{"tag": "..."}` if absent → `PATCH` with `If-Unmodified-Since-Version`.
  For anchors, also `POST /items` a child note (itemType:note, parentItem, note=HTML).
- **`.envrc`** has `ZOTERO_API_KEY` (write), `ZOTERO_LIBRARY_ID=6505702`, `OPENALEX_API_KEY`, `OPENALEX_MAILTO`.
  Source it or run from the SLR dir (direnv).

## 6. Reference docs (all under `Methodology/`)

- `Emerging_Themes.md` — themes T1/T2 + the tag-vocabulary table (**operative reference for the pass**).
- `HOS_Seeded_Theme_Candidates.md` — the graft backlog (T3 + T0 sharpeners + backlog lenses).
- `Problem_Statement_Evidence.md` — the inversion (T0), anchors, validity caveats.
- `SLR_Status_Update_2026-07-08.md` §3 — the authoritative core/context scope bar.
- `Stage4_Snowball_Enrichment_and_Rescreening.md` — full snowball pipeline + §9 review outcome + the
  crystallized triage discriminators.
- Memory: `research-discovery-skills`, `zotero-library-structure` (synthesis-tag note), `slr-scope-refinement`.

## 7. Open decisions / pending

- **Merge streams into `Phase 3 / 03-Final`** (see §1) — or tag off per-stream collections.
- **Grafting decisions** (§3) — Scott to confirm which backlog lenses become first-class themes.
- **`J4RVWCM2` SonarQube caveat** — check `9H6FWJME` + other debt/maintainability items for
  static-analysis-tooling exposure before leaning on their numbers (noted in `Problem_Statement_Evidence.md` §5).
- Optional: stamp `s3:human:<bin>` on the *confirmed* band-sub items (not just moves) if a complete
  ≥55 review record is wanted.

## 8. Definition of done (theme-tagging phase)

Every core (and the survey/lit-review-relevant contexts) carries its synthesis tags; each `theme:<name>`
has a section in `Emerging_Themes.md` with its corpus-grounded anchor + members; the four docs
(Emerging_Themes, Problem_Statement_Evidence, HOS_Seeded, slr-conventions) are reconciled. Then →
**Stage 4 extraction** of the 149 cores (full-text fetch + TXT for the snowball cores like the original 114).
