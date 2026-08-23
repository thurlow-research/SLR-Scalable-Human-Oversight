# SLR Paper — Detailed Outline v0 (beginning sections, through current state)

**Drafted 2026-08-16.** Covers Introduction → Background → Method, i.e., everything executed to
date (through sweep machine-phases complete; human review open). Results/Findings sections are
stubbed only. Numbers marked **[verify]** must be re-derived from the library (Total-Results)
before submission — do not trust prose memory for PRISMA counts.

---

## 1. Introduction

### 1.1 The oversight scaling inversion (motivating problem)
- AI coding assistants and agents raise code *production* rates faster than human review
  capacity grows; simultaneously, evidence indicates AI-generated code is riskier per unit
  (security weaknesses, quality debt) yet *less* inspected in practice.
- Anchor statistic (candidate `problem-statement-anchor`): ~80% of AI-co-authored PRs merged
  with no explicit review (`59KP8GTP`). Secondary anchors: Copilot snippet vulnerability rates
  (`3Z45M3V3`: 29.5% Python / 24.2% JS **[verify]**); issue persistence / review burden
  (`9H6FWJME`, `F2C2DWSI`, `REZGA5WF`).
- Name the inversion: risk per artifact up, scrutiny per artifact down — the review's central
  phenomenon and the dissertation's opening argument.

### 1.2 "Vibe coding" and the governance gap
- Define vibe coding (natural-language-driven, AI-generated code accepted at increasing
  granularity: suggestion → artifact → autonomous change); position on the assistive↔agentic
  spectrum (this becomes a formal facet pair in the instrument, §3.8).
- Organizations lack established governance for this production mode: policy, review
  obligations, audit trails, regulatory hooks (EU AI Act Art. 14, NIST AI RMF, ISO 42001) are
  nascent or transplanted from general-AI governance.

### 1.3 Review question and two-part frame
- RQ: *How do organizations practice and scale human oversight of AI-generated code so
  oversight keeps pace with code volume without sacrificing quality — including the
  governance/policy landscape and the strengths/limitations of current oversight practices?*
- Two-part analytical frame (the organizing spine of the whole review):
  1. **Quantify the problem** — including the *insufficiency layer*: evidence that current
     oversight practice does not close the gap (unreviewed merges, automation bias, oversight
     theater).
  2. **Characterize the solution** — oversight mechanisms, frameworks, and measurements, organized
     on a Detect → Triage → Fix → Escalate pipeline (derived bottom-up from the corpus, §3.8).
- Effectiveness clause: oversight must be *effective as well as scalable* ("without sacrificing
  quality") — links to the dissertation's survey constructs (`dissertation-input` thread).

### 1.4 Relationship to the dissertation
- The SLR builds the knowledge base for an **organizational survey** (the dissertation
  contribution). HOS (Human Oversight System, Thurlow 2026, Zenodo DOI 10.5281/zenodo.21347272)
  is a learning vehicle that seeded instrument intuitions (e.g., computed-signal-not-self-report),
  not a contribution under evaluation.

### 1.5 Contributions of this review
1. A PRISMA-informed corpus of primary evidence on oversight of AI-generated code (**[verify]**
   final counts: ~148-core / ~890-context two-tier corpus).
2. A validated, versioned **thematic instrument** (v2.13: 17 themes + 27 facets) with a public
   audit trail of every definitional ruling (Taxonomy_Changelog §1–§32).
3. A reproducible **multi-model tagging methodology** with human adjudication — cross-vendor
   panel, disagreement-triggered replication, computed quality tripwires — itself an exercise
   in scalable human oversight of AI work (reflexivity thread, §3.11).
4. Synthesis products: theme map, risk×mitigation matrix (gap cells = identified-but-unmitigated
   risks), problem-statement evidence base.

### 1.6 Paper roadmap

## 2. Background and Related Work

### 2.1 Conceptual foundations: oversight vs. steering vs. guidance
- The three-way discriminator (decisive throughout screening and tagging):
  **oversight** = inspection-and-gating of a produced artifact on quality/risk grounds with
  authority to reject/escalate; **steering** = directing generation (prompting, specs,
  fine-tuning, input/context control); **guidance** = the agent asking the human to unblock it.
  Only oversight is in scope as a solution class.
- Corollary: generation-improvement solutions are steering, not oversight — excluded from core
  Part-2 regardless of merit.
- Gate on computed, producer-independent signals, never model self-report (self-confidence is
  saturated and uninformative — HOS finding; also grounds the `routing-signal`/`risk-routing`
  boundary).

### 2.2 Adjacent literatures (and how this review differs)
- General scalable-oversight / alignment literature (e.g., `7BMFG5IK`-class): transfers as
  theory; not code-in-an-org — kept at context tier.
- Human factors of automation: automation bias, complacency, trust calibration
  (Buçinca et al. cognitive forcing functions, `UTTJ5N93` — the effectiveness dimension);
  distinguish *capable-human-failing* (bias) from *competence gap* (`22JBEZNK` ruling).
- Code review research (general-code): transfers via the `general-code` scope flag; mechanisms
  developed for human-written code that could gate AI code.
- AI-code quality/security measurement: capability benchmarks vs. governance-relevant
  measurement (bare leaderboards excluded).
- Regulatory landscape: EU AI Act Art. 14 human oversight, NIST AI RMF, ISO/IEC 42001;
  liability and audit-evidence threads.
- Prior secondary literature on AI code generation (`lit-review`-tagged): none found covering
  the *oversight-scaling* question specifically **[verify at write-up]** — the gap this review
  fills.

### 2.3 Terminology and definitions table
- Vibe coding; oversight scaling inversion; assistive vs agentic generation (initiator +
  reviewable unit, not tool location); core/context tiers; theme/facet/flag layers.

## 3. Method

> Framing note for the whole section: the review's method deliberately instantiates its own
> subject — AI does volume work, humans hold judgment gates, and every AI output passes through
> designed, computed (never self-reported) quality controls. Written up in §3.11.

### 3.1 Review design overview
- PRISMA-informed multi-stage funnel; two source streams (database queries; citation
  snowballing) run through an identical instrument and merged only at the final triage.
- Figure: pipeline diagram (Phases 1–5) with counts at every edge (**[verify]** all counts
  against Total-Results at write-up).
- Two-tier corpus design: **Core** (direct + operationalizable on scalable oversight of
  AI-generated code in org/SE-pipeline context) vs **Context** (in-scope background: behavioral,
  adoption, transferable-theory, secondary lit) — tier ≠ importance; synthesis draws on both.
- Tooling: Zotero group library (6505702) as system of record; lineage encoded as namespaced
  tags (`source:` / `s1:` / `s2:` / `s3:` / `centrality:` / `cocite:`); every stage scripted,
  resumable, and auditable (public repo, gitignored copyrighted texts).

**PRISMA alignment note (2026-08-22).** This project's internal "Phase 1–6" pipeline-tracking
scheme is custom (Zotero/workflow convention), not PRISMA vocabulary itself — the standard PRISMA
2020 flow diagram has four stages (Identification → Screening → Eligibility → Included) and
normally stops at Included. Internal Phases 1–3 map cleanly onto Identification/Screening/
Eligibility; **Phases 4–6 are not extra, post-inclusion activity — they ARE the eligibility
determination, executed as a multi-pass process rather than a single pass, because corpus volume
makes a single abstract-level pass too coarse to trust as final.** Phase 3's centrality-banded
triage is a *provisional* eligibility call from abstracts only; the Phase 5 full-text read is what
*finalizes* it — confirming or overturning the provisional tier (Core/Context/exclude) once a human
has actually read the whole paper (worked examples: VCI88UZD, Y4TIF9KW demoted Core→Context on
full read, 2026-08-22). **Phase 6 is simply the settled output of that whole determination** — the
"Included" corpus, reported once all of it (not just the cheap first pass) is done. This should be
written up as *one* PRISMA Eligibility→Included stage with a multi-pass method, not narrated as
if Phase 3 were the real inclusion decision and Phase 5/6 something that happened after.

**Distinct from the above — a volume-driven design choice worth naming explicitly:** the same
Phase 5 full-text reading pass that finalizes eligibility *also* performs data extraction/coding
(theme/facet tagging, §3.7–§3.10) in the same read, rather than as a separate pass. **With this
corpus's volume, reading each paper once and doing both jobs was the only way to get through it —
not an accidental conflation of two things PRISMA's checklist treats as separate items** (data
extraction/data items are checklist items distinct from the eligibility determination). Worth
stating plainly in the methods write-up so a PRISMA-literate reviewer sees it as a deliberate
efficiency choice, not a blurring of two things that should have stayed separate.

### 3.2 Search strategy (Phase 1)
- Nine sources: ACM DL, IEEE Xplore, Scopus, SSRN, Web of Science, arXiv, plus Coursework,
  Practitioner Network, and Committee Recommendations channels **[verify query strings and
  per-source batch counts from Phase 1 collections]**.
- Query design rationale; grey literature policy: generally excluded, rare
  extreme-relevance exceptions flagged by hand.
- Import bookkeeping: per-source `01-Import(s)/Q-<SRC>-NN` batches preserved as audit material.

### 3.3 Screening (Phases 1–2)
- **S1**: Sonnet keep/maybe/discard on title+abstract (prompt versioned in repo). **S2**: Opus
  binary keep/discard arbiter over non-discards. Tags `s1:*`/`s2:*` preserved on items.
- Abstract gate: items without abstracts after fetch effort → `hold:no-abstract` collection,
  never auto-screened (title-only screening unreliable).
- Verified pool after Phase 2: **983** (2026-07-01) **[verify]**.
- Distribution sanity-checks as standing rule (an all-one-bucket result is a bug, not a finding).

### 3.4 Citation snowballing (Stage 4 enrichment)
- Backward co-citation snowball from the triaged set: **2,787** references imported
  **[verify]**, banded by co-citation count (`cocite:`), deduplicated against the query stream
  (one-record-per-study rule; preprint→journal keeper = journal; `superseded-by:` lineage).
- Identical screening instrument applied to the snowball stream (parity by design); merged into
  Phase 3 / 03-Final only after both streams triaged.
- Validation vignette (§7 of sweep record): an arbiter hand-spotted reference (Buçinca 2021)
  was already in-corpus with correct disposition — snowball recall working as intended.

### 3.5 Relevance triage (Phase 3) and cross-model QA
- Opus triage to core/context/discard + centrality 0–100; bands: core 70–100, context 30–69,
  discard 0–29. **Human review floor ≥55** (Confirm 75–100 / Review 70–74 / Recall 55–69),
  exact parity across streams; below 55 auto-dispositioned.
- Cross-model QA findings that shaped the design (Stage 3 QA, 2026-07-06):
  - Opus over-calls core (precision ~30% on core confirms **[verify — reconcile with the ~64%
    figure recorded for the full ≥70 review]**); errors are two-sided.
  - Codex/Gemini over-keep AND their dissent from Opus does not predict human judgment
    (chance-level κ; "Trust Check" κ≈0.30) → **no model shortcut around human review**; every
    core is human-confirmed.
- Refined §3 core bar (2026-07-08 status update): both prongs required (direct scope AND
  operationalizable mechanism/measurement/framework/empirical finding); boundary rules
  (effectiveness-of-oversight = candidate core; tool benchmark = context; self-conformance out;
  what+how carve-out with tool-validation exclusion, changelog §23/§27).
- Final core corpus: 149 → **148** after one calibration-era demotion (M74M3RFJ) **[verify]**;
  context ~890 **[verify]**.

### 3.6 Full-text acquisition
- PDF→TXT conversion for all cores (pdftotext; TXT as child attachment alongside PDF);
  extraction QA (0 failures on the initial 114 **[verify]**; all 148 cores have TXT as of
  2026-08-15). Copyright handling: full texts live only in Zotero + local caches, never in the
  public repo.

### 3.7 Thematic instrument: derivation
- Bottom-up open coding of all cores (4 parallel coders + HOS experiential cross-check) →
  controlled vocabulary on a **Detect → Triage → Fix → Escalate** solution spine + problem,
  limits, governance, and supply-chain families.
- Three orthogonal layers: `theme:` (membership-not-mention), facets (role / form-maturity /
  scope / mode / contribution / risk-type / method — the seven-question checklist), flags
  (demote / insufficient-input). One PRIMARY per paper (novelty tie-breaker; altitude rule).
- Instrument text = `Tag_Cheatsheet.md` / `Tag_Prompt.md`; every definitional change logged in
  `Taxonomy_Changelog.md` (§1–§32) with the triggering paper — the changelog *is* the
  content-validity audit trail.

### 3.8 Instrument calibration (Sets A / B / C)
- 20-paper calibration (seed 714): Set A (model-informed vetting), Set B (10 papers,
  human-tagged **blind** under the co-tagging protocol; AI = post-blind QA only; blind
  snapshots preserved as Zotero versions), Set C (AI-first pilot, ZUM76CCG).
- Iteration record: v1 → v2.13 with re-tests after every change (facet Jaccard doubled
  .34–.42 → .61–.70 after the v2 freeze rulings **[verify]**; the risk-routing/hitl-workflow
  refinement converted a persistent 2/3 split into 5/5 unanimity).
- Panel accuracy vs human gold at v2.13 (n=20): opus 17/20 primaries, gemini 14/20, codex 13/20;
  Fable on the contested six only (4/6). Cross-model tagging behavior is a model disposition,
  not a vendor trait; **model consensus does not substitute for human judgment**.
- Negative results (documented by design): persona framing rejected (interest-salience drift);
  theme/facet prompt split declined; no length effect at panel tier (r≈0.0, n=20).
- Leakage disclosure: calibration papers named in the instrument score inflated when
  self-referential; sweep papers unnamed → unaffected.
- Set C pilot (production-workflow rehearsal): full protocol on ZUM76CCG including the
  replication stage's first live catch — a single-run consensus built on one unstable opus draw
  was REVERSED by modal replication; arbiter adjudication closed all five questions and set the
  §32 altitude precedent.

### 3.9 Multi-model panel and the triage ladder (production QA design)
- Panel: opus (claude-opus-4-8) + codex (gpt-5.6-sol high) + gemini (3.1-pro-high), all pinned,
  per-run provenance sidecars; premium tiers (Fable) only by per-run human authorization.
- The Jidoka ladder: **L0** schema validation → **L1** 3/3 consensus → ACCEPT + 10% seeded audit
  (seed 714); any disagreement → **replication stage** (k=3 per model on contested only; modal
  votes; noise-resolved vs persistent) → **L2** computed tripwires: sprawl (>6 themes), demote
  flags, **within-model instability** (the operationalized low-confidence signal — computed,
  never self-reported) → per-facet voting (3/3 accept · 2/3 noted · 1/3 drop-logged).
- Design rationale: run-to-run variability is real and decision-changing; CLIs expose no
  temperature/seed control — so *characterize* noise via replication instead of pretending to
  eliminate it. Dissent triggers replication; **stability carries the information** (dissent
  alone doesn't predict the human — Stage 3 QA).
- Retrospective validation on the calibration 20: ACCEPT band 7 with 1 documented legitimate
  divergence; LIGHT-REVIEW proposals 10/10 correct; HUMAN = exactly the 3 hardest papers.

### 3.10 Production sweep execution (2026-08-15/16) and human-review protocol
- 128 non-calibration cores; execution record in `Theme_Tagging_Sweep_2026-08.md`: round 1
  (384 runs, 100% valid), replication (282 runs on 47 contested), quality events all caught at
  L0/ops level (quota exhaustion, schema violations, transients — none reached the data).
- Final machine dispositions: **ACCEPT 44 · LIGHT-REVIEW 78 (18 unanimous-demote) · HUMAN 6**;
  contested rate 37% (< 43% projection); replication resolved 41/47 without human load.
- Realized human protocol (open): 6 deep reads + 78 confirmations + 4-paper seeded audit,
  organized in Zotero Phase 5 - Reading (Accept / Light Read / Full Read); nothing written to
  the library until the arbiter approves the write plan.
- Observation for the write-up: instability at sweep scale is panel-uniform (17–18 tripwires
  per model) — noise is a property of the task, not a defect of one vendor.

### 3.11 Methodological reflexivity: oversight of AI, by design
- The pipeline is an instance of the review's own thesis: AI produces volume (screening,
  tagging); humans hold judgment gates (every core human-confirmed; blind-first co-tagging;
  arbiter rulings binding); quality signals are computed, never self-reported (instability
  tripwires vs. saturated model confidence); escalation is risk-tiered (ACCEPT → audit sample;
  LIGHT → confirm; HUMAN → deep read) — a working Detect→Triage→Escalate loop.
- Even repository governance mirrors the thesis: assistant-authored changes land only via
  pull-request review by the human (adopted 2026-07-23).
- Frame honestly as *methodological alignment*, not proof of the thesis.

### 3.12 Threats to validity
- **Construct**: instrument drift during Set B (v2.2→v2.10 confound, disclosed); calibration
  leakage (named papers; sweep unaffected); single-arbiter adjudication (mitigated by binding
  written rulings + public changelog).
- **Internal**: LLM run-to-run noise (mitigated by replication + modal votes); model
  self-report distrust (designed out); screening model biases (two-sided Opus errors; human
  floor ≥55).
- **External**: corpus recency (field moves fast; search window **[verify dates]**); grey
  literature largely excluded; English-only **[verify]**.
- **Reproducibility**: pinned model tiers + provenance sidecars; seeds fixed (714); public
  repo with scripts, prompts, changelog, and per-run outputs (texts excluded for copyright).

## 4. Results (STUB — pending human review completion)
- 4.1 PRISMA flow + final corpus counts. 4.2 Theme landscape (primary distribution; Detect-heavy
  mass: `ai-review` 31 of 122 machine proposals **[provisional]**). 4.3 Problem quantification
  synthesis. 4.4 Solution characterization on the pipeline spine. 4.5 Risk×mitigation matrix
  (gap cells). 4.6 Governance/regulatory landscape. 4.7 Methodological findings from the
  multi-model process (panel accuracy, replication yield, human-load economics).

## 5. Discussion (STUB)
- Insufficiency layer → survey constructs; effectiveness-vs-scalability tension
  (`dissertation-input` thread); counterpoints; implications for org practice.

---
*Maintenance note: this outline is a working document; renumber against the target venue's
template at draft time. All **[verify]** markers must clear before any count appears in prose.*
