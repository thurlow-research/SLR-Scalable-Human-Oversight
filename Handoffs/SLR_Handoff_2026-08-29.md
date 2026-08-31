# SLR handoff — 2026-08-29

Entry point for resuming work on the **Scalable Human Oversight of AI-Generated Code** systematic
literature review. Supersedes `SLR_Handoff_ThemeTagging_2026-08-22.md`.

---

## 1. What this review is

**Question.** How do organizations practice and scale human oversight of AI-generated code, and which
practices hold up under volume?

**The premise.** Code *production* scales with compute; code *inspection* is bounded by qualified
engineers and the hours they can spend reading diffs. In conventional engineering, riskier artifacts
attract more scrutiny. For AI-generated code the curves appear to cross — the artifact is measurably
riskier yet receives *less* inspection.

**Why it is a literature review and not only fieldwork.** The review establishes that the field is
**solution-heavy and evidence-thin**: mechanisms are proposed and demonstrated in research settings,
with little empirical account of how oversight is actually enacted inside firms. That absence is the
gap the dissertation's organizational study addresses.

---

## 2. Lifecycle — the funnel

| Stage | What happened | Count |
|---|---|---|
| **Sources** | 10 query families across Scopus, ACM DL, IEEE Xplore, arXiv, SSRN, + snowball | — |
| **Records** | unique records after library-wide deduplication | **9,518** |
| **Phase 1 — recall screen** | title/abstract, deliberately loose | → **4,061** keep+maybe |
| **Phase 2 — precision screen** | tighter rubric; 973 keep / 73 maybe / 2,908 discard | → **983** eligible |
| **Phase 3 — relevance triage** | abstract-level Core / Context / Discard, cross-model + human confirm | → Core band |
| **Phase 4 — full text** | PDFs fetched, text extracted, tagging instrument built | **147** unique studies |
| **Phase 5 — reading & tagging** | Light Read + Accept band + Full Read; v2.13 instrument, 3-vendor panel | 147 adjudicated |
| **Phase 6 — Kept Core** | survivors: human primary theme present AND no `demote:context` | **72** |

**Snowballing** ran alongside: 2,787 backward co-citation references imported, banded by co-citation
count, screened through the same pipeline.

**Attrition at Phase 5 is the striking number: 147 → 72.** Roughly half the full-text corpus was
demoted to Context on close reading — consistently *more* aggressively than the model panel proposed.

---

## 3. Where things are

- **Zotero** is the source of truth (group 6505702). Membership = **provenance**; phase collections
  freeze after population. Current tier lives in the `demote:context` tag, not in membership.
- **`Phase 6 - Kept Core`** = `R9ZHDXMN`, 72 items. Populated 2026-08-29. **Use this as the working
  set** — it is exactly *core ∧ ¬demote*, so downstream work no longer recomputes a predicate.
- **Methodology source of truth**: `Methodology/`. Case law: `slr-phase4/Taxonomy_Changelog.md`.
- **Conventions**: the `slr-conventions` skill.
- **Closeout tracker**: `Methodology/Post_Accept_Closeout.md`.

---

## 4. The tagging apparatus

**Three-layer namespace.** `cal:<vendor>:*` (panel proposals) → `cal:human:*` / `cal:human:reject:*`
(arbiter decisions) → `final:*` (computed).

> `final:* = panel modal ∪ endorsements − rejections − deprecated vocabulary`

**The human layer is fail-open**: a modal proposal stands unless explicitly rejected. This matters —
**every tagging error found this session ran in the same direction, false positives accumulating
because silence lets a modal through.** Whether to keep fail-open is closeout item **B9**, and it must
be decided before `final:*` is computed.

**Panel.** 3 vendors × k=3, identities *pinned* (`claude-opus-4-8`, `gpt-5.6-sol`,
`gemini-3.1-pro-high`) rather than inherited from CLI defaults — inheriting silently swaps the
calibration gauge between measurement points.

**A calibration result worth carrying into the write-up:** on the *residual* — proposals the arbiter
had not independently made — the panel ran at **50% precision (7 of 14)**. Overall precision is far
higher, but **on contested tags, three vendors agreeing unanimously is a coin flip.** The corpus's own
finding, reproduced by our instrument.

---

## 5. What happened on 2026-08-29

**Set A and Set B tag review closed** — 14 panel proposals adjudicated.

**F2 restricted re-run designed, calibrated and executed.** New vocabulary applied to all 72 survivors
without re-adjudicating settled tags: restriction is on the **output schema**, while the prompt still
describes neighbouring concepts (every new slug is defined by a boundary against an existing one).
216/216 calls valid; **262 tags written to Zotero across 55 papers, verified, 0 failures.**

**A 12-paper calibration gate** (`slr-phase4/data/f2_calibration_expected.json`) tests every slug in
both directions against arbiter-settled answers. It **caught three real defects** before the full run —
worth keeping for any future instrument.

### Taxonomy rulings (all in the changelog)

| § | Ruling |
|---|---|
| **145a** | `survey-input` — elicitation test HELD; centrality declined a second time. New bar: the elicited preference must be a **reported finding**, not **formative** material. Location test, so it is reproducible |
| **145b** | For mining/discourse studies, **risk flags track the coding scheme, not illustrative quotes**. Closes the long-open §42(e) |
| **146a** | `evaluator-reliability` consolidated to the **theme** namespace (was split 5/8) |
| **147a** | `rules-based-checks` hybrids **ruled out** — §139a's third conjunct: the verdict must be *independent of a model's judgement*, not merely reproducible |
| **147b** | **`deterministic-orchestration` coined** — code, not a model, controls which steps run and whether outcomes are honoured |
| **147c** | `scaling-dissent` **closed at zero** and dropped from the run |
| **148a** | **Dedupe moves the record but not the evidence** — Jin's corpus text was still the preprint. Generalisable; closeout owes a sweep |
| **148b** | **Curation decides, not provenance** — "concocting a dataset from established datasets is still synthetic." Written as create-vs-select so `evaluated-real-data` keeps its members |
| **148c** | `deterministic-orchestration` is **top-level only**; the adjudication split deferred to a count |
| **149a** | **`agent-panel` split; `peer-critique` coined** — see below |
| **149b** | **Catalogued ≠ implemented** — architecture facets describe what a system *is*; themes describe what a paper is *about* |

### §149a is the one that matters most

`agent-panel` was conflating two mechanisms with **opposite evidence behind them**:

> **What does the agent consume?** The primary artifact → `agent-panel` (redundancy).
> Another agent's output → `peer-critique` (mutual checking).

Redundancy is weak — 2.4pp convergence gain, correlated judge errors, our own 50%, `counterpoint` 9/9
wrong. Peer critique is strong — arbitration cut change surface 83–90%, ReviewFilter made BitsAI-CR
deployable, Jin's filter took FPR 88.74% → 39.96%.

**Consequence for the thesis:** the corpus's strongest negative result stops being an attack on
multi-agent oversight and becomes a **defence** — the failing mechanism is the one HOS does not rely on.
That claim is unavailable while the two share a tag.

**A recurring hazard, named four times in one day** (§139a, §147b, §149a, §149b): *merging constructs
that differ in their evidence because they share vocabulary.* That belongs in the methods chapter as a
finding about taxonomy construction.

---

## 6. F2 results — the census

`slr-phase4/data/f2_census.json`. Papers at ≥2/3 vendor agreement, of 72:

| Slug | ≥2/3 | Note |
|---|---|---|
| `evaluated-synthetic` | 13 | |
| `evaluated-real-data` | **10** | from **zero** known instances — the coined rung was real |
| `deterministic-orchestration` | **10** | broader than the 3–5 predicted under the top-level rule |
| `peer-critique` | 9 | **direction: 25 one-directional vs 3 mutual** |
| `rules-based-checks-v2` | 8 | v1 had **24** holders — §139a cuts hard |
| `evaluator-reliability` | 8 | |
| `agent-panel` | 5 | aggregation: vote 4 / consensus 3 / arbitration 3 |
| `cross-model` | 4 | |
| `evaluated-benchmark` | 4 | |
| `survey-input-v2` | 3 | v1 had 9 — three conjunctive conditions cut hard |
| **`oversight-scaling-inversion-v2`** | **1** | **see below** |

### The two findings to carry forward

**1. `oversight-scaling-inversion-v2` fires on exactly one paper — Gao (`59KP8GTP`), the anchor.**
Under v1 the construct was applied widely. Under the §88 leakage test — which demands *observed review
absence* or *defects in merged code with review failure as cause* — the corpus supplies volume,
pressure, queue growth and merge speed instead. **The inversion is not disproven; it is not yet
demonstrated to a strict standard anywhere in the screened literature.** That is a strong warrant for
the fieldwork and a caution for how the premise is stated.

**2. Mutual peer critique is nearly absent.** 25 one-directional versus 3 mutual. The corpus builds
dedicated critics over producers; **agents checking *each other* — the thesis mechanism, and HOS's — is
the scarce case.**

**144 flags** were raised, concentrated on the two most-narrowed slugs (`rules-based-checks-v2` 20
papers, `oversight-scaling-inversion-v2` 21). That is a real adjudication queue: the *undecidable*
flags need rulings; the *census* flags are counts and can be summarised.

---

## 7. Open work, in order

**Immediate**
1. **Adjudicate the 144 F2 flags** — undecidable ones need rulings; census ones are counts.
2. **Review F2 proposals against human tags** — the arbiter's two-sided audit: strong panel signal with
   no human tag, and weak signal with a human tag. **Plus** a full sweep of the four definition-changed
   slugs regardless of signal, since agreement under a superseded rule is not evidence.
3. **Place the 24 unplaced Phase 6 papers** — proposal in
   `Methodology/Dissertation_Classification_Proposal.md`.
4. **Finish the §149a re-read**: `5RLPIA3K` → `peer-critique`; `DJMBHHZN` → both;
   `A6ZE2A26`/`R9CDT9KB`/`CTGGMIX9`/`TA6GIUK2` stay `agent-panel`. Vargas already written.

**Closeout (`Post_Accept_Closeout.md`)**
5. **B9 — fail-open vs fail-closed.** Blocks `final:*`. Evidence now favours revisiting it.
6. **F1 — compute `final:*`.**
7. **B3** deprecated `counterpoint` sweep · **B4** §34 re-check · **B6/B8**.
8. **§148a sweep** — any consolidation where the arXiv key survived may carry the preprint text.
9. **§149b sweep** — `design-only` papers carrying architecture facets on catalogued mechanisms.
10. **Zhu `ZGST9CY6` `agentic`** — last architecture facet on that item, unruled.

**Gaps**
11. **RQ4 is thin.** Only three Phase 6 papers carry `regulatory-compliance` as primary. Make
    regulated-industry oversight an explicit target of the **F5** supplementary search.
12. **Metadata defects**: `VG6CIDQW` and `R4WJZBSF` have **no author metadata** and are in Phase 6.

---

## 8. Outreach — drafts and the playbook

`Outreach/` holds the public-facing work. **`Outreach_Playbook.md` is the durable asset** — the
measured performance of Article 01 and what was learned from drafting against it. Read it before writing
any post; the drafts are disposable, the reasoning isn't.

**Format note:** the pattern here is native LinkedIn **articles** with feed share-text, not plain
posts — which is why the analytics report "article views" separately. Body and commentary are separate
artifacts in separate files.

**Current set:**
- `LinkedIn_Article_01_Incident_Pattern.md` — **PUBLISHED**; analytics recorded on the file
- `LinkedIn_Article_02_SLR_Findings_Draft.md` — long-form, ~2,150 words, both graphics
- `LinkedIn_Article_02_ShareText_Draft.md` — feed commentary driving to it, 391 words
- `LinkedIn_Post_03_Open_Questions_Draft.md` — open questions → RQs, 428 words. **Open: should this be
  Article 03?** At 428 words it is post-length with no article behind it, against an
  articles-by-default pattern.
- `assets/` — funnel and three-mechanism graphics (PNG + editable SVG)

**The four things most worth not re-learning:**

1. **98% of Article 01's reach was out-of-network.** Assume every reader is a stranger; the first line
   carries the post. Credibility numbers go in paragraph two, not the hook.
2. **32 saves against 5 reposts.** This audience files the work rather than debating it — so concrete,
   re-readable specifics (named mechanisms, real numbers, actionable items) beat provocation. A
   recommendations list is close to the ideal shape.
3. **Naming a finding creates a gap; explaining it closes one.** That is the whole teaser/article
   distinction, and it took two overcorrections to land: ~400 words, a claim plus the evidence that
   makes it stick, then stop.
4. **The self-implicating caveat is the strongest credibility move available** — "my own three-model
   panel was right about half the time on contested calls." Costs a sentence, pre-empts the obvious
   objection, demonstrates the discipline the work argues for. Keep a version of it in every post.

**Two framing rules, both from errors caught in drafting:** the subject is oversight of AI **coding**,
not code **review** (review is one mechanism inside it); and the frame is **scaling human oversight**,
not which AI checking design wins — every finding should answer *"so what does a human still need to
look at?"*

⚠ **No recruitment until after candidacy**, and **never publish an unsettled figure** — the "1 of 72
clears the strict inversion test" number stays out until the 144 flags are adjudicated.

## 9. Standing rules

- **All assistant changes land via PR**, never direct to main. Branch `claude/<topic>` → push → PR →
  Scott merges.
- **Repo is PUBLIC.** Never commit `slr-phase4/txt/`, `Backups/`, `Downloads/`, `.envrc`, PDFs, or
  Zotero exports. Secret-scan before every commit.
- **Zotero writes need a backup first.** `ZOTERO_API_KEY_RW` to write, `_RO` to read.
- **Brainstorm and pressure-test before writing.** Wait for explicit authorization.
- **Flag model fit at session start** — judgment-heavy work (boundary adjudication, methodology text)
  warrants Opus; mechanical work does not.
- **Never duplicate a Zotero record** — add existing items to collections.
