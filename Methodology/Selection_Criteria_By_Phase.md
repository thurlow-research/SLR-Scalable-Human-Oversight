# Selection Criteria by Phase

**Vibe Coding Governance Systematic Literature Review · Zotero group 6505702**
**Date:** 2026-07-13 · Methods-chapter reference (consolidation, not a new decision)

Purpose: a single place that enumerates the **inclusion / exclusion criteria applied at
every phase** of screening, from search-time eligibility through the two-tier extraction
corpus. It consolidates rules that live across `SLR_Methodology_Bootstrap.md` (search +
Pass-1/2 rubrics), `Stage3_Relevance_Triage_and_CrossModel_QA.md` (triage instrument),
`SLR_Status_Update_2026-07-08.md` §3 (the refined core/context bar),
`Stage4_Snowball_Enrichment_and_Rescreening.md` (snowball parity), and the
`slr-conventions` skill. Where this doc and a source doc conflict, the source doc governs;
where the doc and the **live library** conflict, the library governs.

**Standing guardrail across all phases:** AI (Claude Sonnet/Opus) is a *consistency-check
tool, not a decision-maker*. Every automated disposition that reaches the corpus is a
routing decision subject to human confirmation; the human is the final arbiter.

---

## 0. Naming — how the phases line up

Two source streams (**database queries** and **backward citation snowball**) run the
**identical instrument** and are kept in parallel collections, then merged into
`Phase 3 / 03-Final`. Historical labels differ slightly between streams; they map as:

| This doc | Query stream label | Snowball stream label | Model | Decision space |
|---|---|---|---|---|
| **Phase A — Search / Identification** | Database Queries | Backward snowball import | — | eligible / not-eligible (search filters) |
| **Phase B — Recall screen** | Pass 1 | Phase 1 | Sonnet | keep / maybe / discard |
| **Phase C — Operationalizability screen** | Pass 2 (Sonnet + Opus arbiter) | Phase 2 (Opus arbiter) | Sonnet → Opus | keep / discard |
| **Phase D — Relevance triage** | Stage 3 | Phase 3 | Opus | core / context / discard + centrality 0–100 |
| **Phase E — Human confirmation** | Stage-3 banded review | ≥55 review | human | core / context / discard (final) |
| **Phase F — Extraction allocation** | two-tier corpus | two-tier corpus | human | full-text (core) / abstract-level (context) |

Phases B–C are **inclusion** screens (does it belong in the eligible pool?). Phase D is a
**relevance triage** — it does not re-litigate inclusion, it sorts the pool by *centrality*
to allocate extraction depth. Phase E confirms every core by hand.

---

## Phase A — Search / Identification (eligibility at search time)

**Question anchor:** *a software engineering team or engineering manager managing
AI-generated code at scale* — how human oversight of AI-generated code scales without
sacrificing quality.

**Identification tiers (PRISMA 2020, kept in separate streams):**
1. **Peer-reviewed database streams** — IEEE Xplore, ACM Digital Library, Scopus, Web of Science.
2. **Preprint stream** — arXiv (+ SSRN where the subfield has many working papers). Same
   substantive inclusion criteria as peer-reviewed, **plus** a methodological-transparency
   check at Phase B (short opinion pieces with no methods section don't pass).
3. **Curated grey-literature streams** — author-assembled prior reading ("Coursework") and a
   prospectively documented Practitioner Network / Committee Recommendations. **Tighter**
   grey-lit inclusion; capped count; enter at the deduplication stage, not the search stage.
4. **Backward citation snowball** — references co-cited by the confirmed cores (added after
   the query corpus was triaged; screened at identical parity — see the parity note below).

**Filters allowed at search time (and only these):**
- **Peer-reviewed:** yes (database streams).
- **Date range:** **2020–present** default; a secondary 2018–2019 pass for *foundational
  theory only* if needed.
- **NEVER full-text-availability** — that is a license filter, not a relevance filter.
  Retrieval failures are coded later as `not-retrievable`, never excluded at search.

**Included at identification:** any record returned by a logged query in an in-scope
database/stream within the date range. Queries are decomposed by thematic category (AI Code
Risk & Security, AI Code Quality & Debt, Human Oversight & Capacity, Org Governance & Policy,
Org Risk Recognition, Tool-Specific), OR-grouped synonym clusters AND-ed, one row per query
in `Query_Composition_and_Log.xlsx`.

**Excluded at identification:** out-of-date-range (unless foundational-theory pass);
non-scholarly grey-lit outside the curated capped streams; anything not returned by a logged
query. Saturation argued from the dedupe rate of the last database added (WoS: 116 unique /
35% yield, 65% overlap).

---

## Phase B — Recall screen (Pass 1 / snowball Phase 1) · Sonnet · keep / maybe / discard

**Intent:** high-recall title/abstract screen — **default to keep**; only discard on clear
off-scope. Errs toward inclusion so nothing on-topic is lost before the tighter screens.

**Include (keep) if the abstract hits any tier:**
- **T1 — direct hits on the core RQ:** vibe coding / AI code generation with a governance,
  risk, or oversight angle; code-review capacity / scalability / fatigue; AI code risk &
  quality; org governance of AI coding tools; developer oversight of LLM-generated code.
- **T2 — relevant supporting/contextual constructs:** human-oversight frameworks; AI
  governance with a software/DevSecOps angle; scalable oversight of high-volume AI output.
- **Auto-keep triggers (keep regardless of other content):** human oversight, AI governance,
  code/software, EU AI Act, NIST AI RMF, organizational adoption, scalable oversight.

**maybe** — reserved for a **thin abstract only** (insufficient text to decide). Not for
genuine topical ambiguity at this pass.

**Discard** — clearly off-scope on title+abstract. (Recall pass: when in doubt, keep.)

**Standard exclusion rules (carry through all phases):**
- Documents authored by the reviewer → always discard (unless explicitly overridden).
- Course-platform URLs (Brightspace/Canvas/Blackboard) → always discard (not citable).
- Items in `04-Superseded` → out of scope for analytical queries.

**Lineage tag:** `s1:sonnet:<decision>`.

---

## Phase C — Operationalizability screen (Pass 2 / snowball Phase 2) · Sonnet → Opus

**Intent:** tighten Phase B's high-recall keep set to papers that give an organization
**something to act on.** Two legs: a Sonnet re-screen of the full set, then an **Opus binary
arbiter** that commits every *maybe* / low-confidence item to keep or discard (no maybe out).

**The operationalizability test (applied first):**
> *"Does this paper give a software-engineering organization something they can act on — a
> measurement, metric, mechanism, detection signal, framework, or process?"*
> **YES →** candidate keep (apply tiers). **NO** (only establishes a problem exists) **→ discard.**

**Include (keep):**
- **Tier 1 — direct hits, if operationalizable:** vibe coding with a governance/risk/oversight
  implication beyond "AI writes code"; reviewer workload/triage/throughput **with an AI-volume
  angle**; AI code risk/quality that **quantifies** with reproducible methodology; org-level
  governance (empirical / case study / framework); developer oversight practices (review,
  override, trust calibration).
- **Tier 2 — transferable, if it generalizes to software without substantial re-derivation:**
  human-oversight frameworks whose mechanism generalizes to code review (automation bias,
  signal detection, Parasuraman levels); AI governance explicitly touching software/DevSecOps;
  EU AI Act / NIST / CISA where *software-system compliance* is discussed; legal liability that
  addresses code or generalizes to it; scalable-oversight mechanisms that transfer to code
  review. **Tiebreaker:** *"Could an SE team adopt this directly without substantial domain
  re-derivation?"* Yes → keep; substantial translation → discard.

**Exclude (discard) — the recurring Pass-2 false positives:**
1. Descriptive-only risk (AI code is risky, no measurement/detection/governance response).
2. Domain-specific governance applied *only* to non-software (clinical, financial, HR, AV).
3. Non-software HITL (physical/scientific/judicial loop with no parallel to code review).
4. General AI ethics/philosophy without an operational mechanism.
5. Creative-content copyright (text/image/music) with no code angle.
6. Agentic AI as infrastructure with no oversight/governance/control mechanism.
7. Org AI adoption — productivity/ROI only, no risk/governance/oversight angle.

**Lineage tags:** `s1:sonnet:<decision>` (Phase B carried) + `s2:opus:<decision>` (arbiter).

---

## Phase D — Relevance triage (Stage 3 / snowball Phase 3) · Opus · core / context / discard + centrality

Sorts the eligible pool by **centrality to the core RQ** to allocate extraction depth. Each
item gets one **bin** and a **0–100 centrality score** (centrality ranks; bins are score bands).
Author metadata is withheld from the model (author-blind) to avoid prestige bias.

**Core (70–100) — requires BOTH:**
1. **Directly** about scalable human oversight / governance of AI-generated code in an
   organizational or SE-pipeline context, **AND**
2. An **operationalizable mechanism, measurement, framework, or empirical finding.**

Two-part frame the core must serve one side of:
- **Quantify the problem** — including the *insufficiency layer* (evidence current/automated
  oversight doesn't close the gap).
- **Characterize the solution** — oversight mechanisms/frameworks across the design space.

**Context (30–69):** in scope, retained at abstract level — adjacent but methodologically
strong and **transferable**: the volume/risk problem; human oversight / AI governance in a
broader setting; automation-bias theory; non-code-specific regulatory frameworks — *with an
evidence base or concrete framework, not opinion*. Secondary literature defaults here
(+ `lit-review`).

**Discard (0–29):** weak **AND** off-core. Reason code (discard only), one of:
`out-of-scope | wrong-level | wrong-type | too-old | quality-threshold-not-met`.

**Operational discriminators adopted during review (the refined §3 bar — tighter than the
raw rubric):**
- Effectiveness of oversight (augment-vs-replace, signal→attention) = **candidate core**;
  tool-capability benchmark = **context**; bare leaderboard = **context/discard**.
- Human oversight (review/escalation/risk-triage) = in scope; **agent self-conformance**
  ("make the agent follow best practices") = out of core.
- Secondary lit → default **context** + `lit-review`; promote to core only for a novel central
  framework, a review of the *exact* topic, or an on-scope meta-analysis. ("Literature review"
  ≠ "code review" — code-review-practice papers are primary domain content.)
- Framing/definitional sources kept tight — **one** empirically-grounded anchor at core, the
  rest context.
- **Grey literature generally EXCLUDED** (blogs, vendor posts, benchmark landing pages, docs,
  social) — retained only as a few exceptions of *extreme* relevance, flagged by hand.

**Lineage tags:** `s3:opus:<bin>` + `centrality:<n>`.

---

## Phase E — Human confirmation (the arbiter step)

Opus **over-calls "core"** (~64% precision on the full ≥70 review; cross-model dissent does
*not* predict human judgment — κ ≈ 0.01–0.04 vs human). There is **no model shortcut**, so
**every core is human-confirmed**, with a hidden-core recall check on the adjacent context band.

**Review floor = centrality ≥ 55 (exact parity across both streams).** The human reads every
item scoring ≥ 55; items below 55 are auto-dispositioned (no human eyes). Banded worksheets:

| Band | Definition | Action |
|---|---|---|
| Confirm | core, centrality ≥ 75 | fast-confirm (top band held up in QA) |
| Review | core, centrality 70–74 | scrutinize (demote-risk cliff) |
| Recall | context, centrality 55–69 | **hidden-core hunt** (promote-risk) |
| Below-55 | context, centrality 30–54 | auto-dispositioned, not reviewed |

Per row the reviewer sets `human_bin ∈ {core, context, discard}`. **Review precedes fetching:**
PDFs are pulled only for confirmed cores. Both the model vote and the human vote are kept
(`s3:opus:<bin>` **and** `s3:human:<bin>`) — a human promotion that contradicts a model discard
preserves *both* as inter-rater reliability data, never overwrites.

---

## Phase F — Extraction allocation (two-tier corpus)

The confirmed bins set extraction depth, not membership:
- **Core → full-text fetch + full extraction** (the argument-bearing evidence; snowball cores
  need full-text fetch + TXT like the original query cores).
- **Context → retained, extracted at abstract level** (no fetch) — feeds framing and the
  planned organizational survey.
- **Discard → excluded** from the extraction corpus (with a reason code).

**Final analysis corpus (both streams merged into `Phase 3 / 03-Final`):**

| Stream | Core | Context | Discard |
|---|---|---|---|
| Query | 114 | 716 | 139 |
| Snowball | 35 | 175 | 41 |
| **Total** | **149** | **891** | — |

---

## Cross-cutting gates (apply at every phase)

**Abstract-gate (validity safeguard).** Title-only screening is unreliable — a keep/discard
made without an abstract is a decision on insufficient data. After a deliberate metadata-fetch
effort, records **still lacking an abstract** are **held**, not auto-screened and not
auto-discarded: tagged `hold:no-abstract`, filed to `Held - No Abstract (review)` for human
exception-review. (SQC: no automated decision on an insufficient measurement; Jidoka: route
the exception to the human.)

**One record per study (dedup).** Consolidate duplicates with `zotero-merge-prep` before the
native client merge (Zotero's merge keeps only the master's fields and only groups same-type
items, so preprint-vs-published never surface). The *query-stream / original* record is master;
preprint→journal keeper = the journal version; tag `superseded-by:` / `supersedes:` and preserve
`cocite:` on the survivor. Cross-check the snowball stream against the query-triaged set before
merging streams so the query record stays master.

**Snowball parity.** The snowball runs the identical B→C→D instrument on **enriched** metadata
(OpenAlex backfill + title canonicalization + cross-type consolidation), gated by the same
abstract-gate, and is reviewed at the **identical ≥55 floor** — chosen over a looser ≥50 so both
streams meet the same bar before merging.

**Sanity-check distributions.** An all-one-bucket screening result is a **bug, not a finding**
(a placeholder mismatch once defaulted all snowball Phase-2 items to discard — caught by the
implausible distribution, verified, fixed, re-run).

---

## Exclusion reason codes (Phase D discards)

Single primary reason per record — the first disqualifying factor, applied consistently:

| Code | Meaning |
|---|---|
| `out-of-scope` | doesn't address any inclusion criterion |
| `wrong-level` | technical-only, no organizational/human dimension (or vice versa) |
| `wrong-type` | opinion piece without an evidence base |
| `too-old` | pre-LLM era unless foundational theory |
| `duplicate` | content-duplicate of a record already in scope |
| `not-retrievable` | full text not obtainable after reasonable effort |
| `quality-threshold-not-met` | failed the preprint methods-transparency or grey-lit quality check |

Author-specific rules stated in the methods chapter: self-authored → discard; course-platform
URLs → discard.

---

## The decisive edge-case discriminator (oversight vs. steering vs. guidance)

A paper is **not** core merely because a human is "in the loop." Classify the human act:
- **Oversight** — *inspection-and-gating of the produced artifact on quality/risk grounds, with
  the ability to reject or escalate.* Only this earns core on the oversight axis.
- **Steering** — human *directs generation* (prompt → output → re-prompt). Before there's an
  artifact to judge. **Not** oversight.
- **Guidance** — agent asks the human how to proceed / to unblock it. Help-to-complete. **Not**
  oversight.

This cuts on the **solution** side too: a *generation-improvement* solution (better prompts,
fine-tuning against hallucination, better test generation) is **steering** — it does not earn
core Part-2. An *oversight* solution detects / gates / escalates on the produced artifact.

**Quick core vs. context (crystallized in the 2026-07-13 snowball review):**
- **Core** = *measures the AI-code problem* (CWE / defect / persistence / review-gap rates) **OR**
  *operationalizes an oversight mechanism* (gate / escalation-timing / attention-routing) with a
  model + evidence.
- **Context** = benchmarks a tool/model capability · validates *which measurement tool* is best ·
  surveys developer perception/adoption · argues a position/agenda (`intro-framing`) · proposes
  an *unevaluated* methodology/framework · general transferable theory (automation-bias, trust) ·
  or is merely **applicable/useful to** the core without operationalizing it.
- **The recurring trap:** "applicable to / could feed into" the core = **context** (it *informs*
  the solution space). Core requires the paper to *do* the measuring or the gating.
- **Gate on a computed/independent signal, never the model's self-report** — model confidence is
  saturated and flat vs. defect rate; the routing signal must be independent of the producer.

---

## Provenance — which tag each phase writes

| Phase | Tag(s) written |
|---|---|
| A — Search | `source:<db>` · `cocite:<n>` (snowball) |
| B — Recall | `s1:sonnet:<decision>` |
| C — Operationalizability | `s2:opus:<decision>` |
| D — Triage | `s3:opus:<bin>` · `centrality:<n>` |
| E — Human confirm | `s3:human:<bin>` |
| Cross-cutting | `hold:no-abstract` · `superseded-by:` / `supersedes:` · `orig-type:` / `orig-date:` |

Collection membership encodes *current disposition*; **tags encode durable lineage** so a
record's full history survives re-filing and client merges. Synthesis tags
(`problem-statement-anchor`, `theme:<name>`, `survey-input`, `intro-framing`, `lit-review`) are
**orthogonal to disposition** and applied in the separate theme-tagging pass — see
`Emerging_Themes.md`.

---

## Source documents (authoritative on their own scope)

- `SLR_Methodology_Bootstrap.md` — search construction, Pass-1/2 rubrics, exclusion codes, PRISMA streams.
- `Stage3_Relevance_Triage_and_CrossModel_QA.md` — the Phase-D instrument, cross-model QA, banded confirmation.
- `SLR_Status_Update_2026-07-08.md` §3 — the authoritative refined core/context bar.
- `Stage4_Snowball_Enrichment_and_Rescreening.md` — snowball parity, abstract-gate, enrichment, §9 review outcome.
- `SLR_Research_Questions_and_Subquestions.md` — the RQ/SQ skeleton the criteria serve.
- `slr-conventions` skill — the operative playbook (library map, tag vocabulary, discriminators).
</content>
</invoke>
