# Handoff — dissertation research-question brainstorm

**Written 2026-09-03.** Entry point for a **new session whose job is brainstorming and
pressure-testing the dissertation's research questions and the shape of the literature review.**
It is not a general SLR handoff — for pipeline state, open adjudication queues and closeout items,
read `Handoffs/SLR_Handoff_2026-08-29.md` alongside this.

**Read this first, then `Methodology/SLR_Research_Questions_and_Subquestions.md` and
`~/TECH-646/Background Brainstorming/Research_Questions_Revision_2026-08-19.md`.** Those two are the
live RQ artifacts; everything below exists to inform revising them.

---

## 0. Two things to say before starting

**Model fit.** This is judgment-heavy work — RQ wording lands in the dissertation and in the prelim,
and errors become permanent methodology entries rather than reversible file edits. **Recommend Opus.**
Say so at the top of the session, unprompted, per the project's standing rule.

**Working style.** Scott brainstorms and pressure-tests *first*; writing happens only after that,
and only on explicit authorization. Do not draft revised RQ text, edit methodology files, or write to
Zotero until asked. Park mid-discussion design questions rather than resolving them out of order.

---

## 1. Zotero access

**Library.** Group **6505702** — *Systemic Literature Review* (`ZOTERO_LIBRARY_TYPE=group`).
It is the **system of record for the entire review**: every screening decision, tier, theme tag and
adjudication lives there, not in the repo. Repo JSON/markdown is derived state.

**Credentials.** `.envrc` in the repo root (direnv, gitignored) exports `ZOTERO_LIBRARY_ID`,
`ZOTERO_LIBRARY_TYPE`, `ZOTERO_API_KEY_RO` and `ZOTERO_API_KEY_RW`. Reads use RO; writes use RW.
**Any write needs a library backup first.**

**How to reach it — three routes, and the rule that picks between them:**

- **Library mechanics** (collections, items, tags, counts, attachments) — the `zotero` skill CLI:
  `python3 ~/.claude/skills/zotero/scripts/zotero.py --help`. Subcommands worth knowing: `collections`,
  `items --collection KEY --tag TAG`, `count` (reads `Total-Results`, one request — use for every
  "how many"), `item KEY`, `tags`, `export`, `attachment KEY`. Raw `curl` against
  `https://api.zotero.org/groups/6505702/...` with the `Zotero-API-Key` header works fine too and is
  often faster for one-off tabulations.
- **Literature lookups / discovery** (finding papers not already in the library, citation chasing,
  verifying a citation) — the **`papersflow` research MCP**, *not* the zotero skill and not the
  `semantic-scholar`/`exa` skills. It carries the current keys and retrieval logic. If it reports
  unauthenticated, run its `authenticate` tool and hand Scott the OAuth URL.
- **Project rules that layer on top** — the **`slr-conventions`** skill: folder grammar, tag
  vocabulary, the Core/Context relevance bar, and the oversight-vs-steering-vs-guidance
  discriminator. Load it before making any inclusion or classification call.

**Reading documents — local first, never refetch.** Resolve an item's child attachments, take the
local path `~/Zotero/storage/<attachmentKey>/<filename>`, read from disk. Do not re-download a PDF
from a publisher, arXiv or a DOI resolver for something the library already holds. **Prefer the TXT
attachment over converting the PDF yourself** — the corpus keeps a TXT beside each PDF so full-text
reads are cheap and reproducible. If a PDF is present with no TXT, *ask* before converting (then use
`zotero-pdf-to-text` so the result attaches back to the item). If there is no local copy at all,
*ask* before fetching. Check attachment labels: one item can carry attachments at different authority
levels — Gao's item, for one, holds a SUPERSEDED preprint TXT alongside the AUTHORITATIVE published
PDF. Match the TXT to the version you mean to quote.

**Corpus full text on disk.** `slr-phase4/txt/<ITEMKEY>.txt` — 151 files, one per extracted core
paper, named by Zotero item key. **Gitignored (copyrighted); the repo is public.** This is the
cheapest way to read any core paper.

---

## 2. Where the "final" set of documents is

### The short answer

**`Phase 6 - Kept Core` — collection key `R9ZHDXMN`, 72 items.** That is the settled included
corpus. Use it as the working set. It is exactly *core ∧ ¬`demote:context`*, materialised on
2026-08-29 so downstream work no longer has to recompute the predicate.

### Why the collection tree looks confusing, and the one rule that resolves it

**Collection membership is PROVENANCE, not current state.** Phase collections freeze once populated —
an item in `Phase 3 - Final / 01-Core` is a record that Phase 3 put it there, *not* a claim that it is
still Core. **Current tier lives in the `demote:context` tag** (absent = surviving). This trips up
every count; check the tag, not the folder.

### The collections that matter

Under **`System LIterature Review`** (`AEQEL2RI`) — the pipeline, in provenance order:

- `Phase 1` (`CJQBAJ4V`) — per-source query imports and first screen. Nine sources: ACM DL, IEEE
  Xplore, Scopus, SSRN, Web of Science, arXiv, plus Coursework, Committee Recommendations,
  Practitioner Network, and Citation Snowballing.
- `Phase 2` (`2PXWECH3`) — precision screen.
- `Phase 3 - Relevance Triage` (`X5SUGJ2L`) — its `03 - Final` sub-tree is the abstract-level
  disposition: Core `3S9B658S` (147), Context `QE8TWEJQ` (890), Discard `72SVYQMU` (180).
- `Phase 4 - Tagging` (`6XXJ5297`) — calibration sets.
- `Phase 5 - Reading` (`D4JRF4GG`) — the reading bands: Accept `UIN658B7` (44), Light Read
  `WTKULZ5U` (78), Full Read `2WE2DX36` (6), Calibration `46QVUN7N` (20), Synthetic-Eval Check
  `6QT8FWFZ` (21).
- **`Phase 6 - Kept Core` (`R9ZHDXMN`) — 72. The final set.**

Under **`Dissertation Lit Review`** (`9RN9P68N`) — the *dissertation's* view, a different cut:

- `01 - Primary` — key `WVZFNSEC`, 37 items (36 of them from Phase 6)
- `02 - Supporting` — key `BWPP3DZA`, 25 items (9 from Phase 6)
- `03 - Queue` — key `4PE2T47Q`, 23 items (12 from Phase 6)
- `04 - Validation Apparatus` — key `XPPEXKBN`, 12 items (6 from Phase 6)
- `01 - Candidates` (`84B8YDJJ`) → `01 - High Confidence` `UA4U35TX` (128) and
  `02 - Medium Confidence` `ZNXKHU4K` (47) — an earlier candidate pool, superseded by Phase 6 as the
  authoritative set.

**Papers can sit in more than one bucket, and 24 of the 72 Phase-6 papers sit in none of them.** A
first-cut placement for those 24 is written up in `Methodology/Dissertation_Classification_Proposal.md`
— **proposal only, nothing written to Zotero**, and still true as of today. It is a natural early task
for the brainstorm session, because deciding *which papers are Primary for which RQ* and *what the RQs
are* are the same decision approached from two sides.

Other collections worth knowing: `HOS` (`Y4DVYPA4`, banded by relevance) holds the prototype-related
material; `AI Incidents` (`E5EZZVC3`, 11) holds incident cases used in outreach; `Methodology Support`
(`PQEDB7SV`) and `LinkedIn Posts` (`JHJN4DKW`) are self-explanatory.

### An important caveat about the tags

The tag namespace has three layers: `cal:<vendor>:*` (panel proposals) → `cal:human:*` /
`cal:human:reject:*` (Scott's arbiter decisions) → `final:*` (computed). **`final:*` has not been
computed yet** — it is blocked on closeout item B9 (whether the human layer fails open or fails
closed). So any theme/facet counts you pull today come from the `cal:human:*` layer and are
**provisional**. Report them as such. The counts in §4 below carry that caveat.

---

## 3. Where the written state lives

- `Methodology/` — source of truth for method. Key files: `SLR_Research_Questions_and_Subquestions.md`
  (the SLR's own SQ1–SQ6), `SLR_Paper_Outline_v0_2026-08.md` (Intro→Method outline, the closest thing
  to a lit-review skeleton), `Problem_Statement_Evidence.md` (the anchor statistics and their
  caveats), **`Emerging_Themes.md`** (2,752 lines — the synthesis notebook, and the single most
  valuable input to an RQ brainstorm), `Survey_Instrument_Design.md` (the question bank spec and 13
  banked survey hooks), `Post_Accept_Closeout.md` (open corrections), `GRAD_503_Summary.md` (the
  methods story told for a course audience — a good compressed narrative of what was learned).
- `slr-phase4/Taxonomy_Changelog.md` — 547 KB of binding definitional rulings, §1 through §149. This
  is the case law. Cite section numbers when a boundary question recurs.
- `~/TECH-646/Assignment 1 - Problem Statement/TECH646_Problem_Statement_Thurlow.md` — the current
  four-RQ formulation with references.
- `~/TECH-646/Background Brainstorming/` — `Research_Question_Brainstorm.md` (806 lines),
  `Research_Questions_Revision_2026-08-19.md` (the revision sent to Paul Josekutty Thomas),
  `Design_Decisions_2026-08-19.md`.
- `Outreach/Outreach_Playbook.md` — public-communication learnings; relevant only if the session
  drifts toward framing.

---

## 4. Where the RQs currently stand

**Two formulations are live and they are not identical.** Reconciling them is part of the job.

**A. The TECH-646 problem statement (four RQs).** *How is oversight enacted in practice — by whom,
at what point, with what division of labor?* · *How is scarce human review attention allocated as AI
output volume increases?* · *How is oversight evidenced, audited, and made demonstrable to a third
party?* · *How do these practices differ across large technology firms, small organizations, and
firms under regulatory obligation?* Approach: qualitative multiple-case design, practitioner
interviews plus artifact review, three strata.

**B. The 19 August revision sent to the advisor (two RQs with sub-questions).** RQ1 *How are
organizations practicing human oversight in their AI coding pipelines?* with 1a provenance
(**how do you even tell which changes contain AI output** — argued as a precondition for everything
else), 1b who/when/division of labor, 1c **which controls predate AI adoption and what changed**,
1d what record the process produces, 1e strengths/limitations. RQ2 *How do organizations connect
external AI governance frameworks to their oversight practice?* with 2a which risk framework and why,
2b what is reported externally, 2c framework-vs-practice correspondence.

**Three decisions embedded in B that should survive any rewrite:** provenance leads because every
other question presumes it; the legacy-control question (1c) is the one that separates "designed for
AI" from "predates AI and nobody revisited it"; and **practice is asked before framework vocabulary
is introduced**, because once a participant hears "NIST" the unfiltered account is gone — which is
also what makes 2c answerable.

**Three things deliberately left open in B, and they are the obvious brainstorm agenda:**
effectiveness (self-report cannot answer *actual* effectiveness — scoped to *perceived* it is
answerable); process maturity as a possible third comparison dimension alongside size and regulatory
exposure; and sub-question count (RQ1 has five; the advisor flagged over-granularity).

**C. The SLR's own sub-questions** (`SLR_Research_Questions_and_Subquestions.md`) are a separate
structure — SQ1 magnitude, SQ2 insufficiency, SQ3 what mechanisms exist, SQ4 how enacted, SQ5 how it
scales, SQ6 how governed/audited/evidenced. Structural decisions there are **locked**; wording was to
be finalized at the coding→synthesis bridge. **HARKing guardrail on record:** refine questions
bottom-up from corpus structure (legitimate, descriptive), but do **not** write findings-claims into
the questions before synthesis.

**Corpus composition, provisional (`cal:human:*` layer, 72 papers).** Primary theme: `ai-review` 13 ·
`hitl-workflow` 10 · `quality-debt` 9 · `org-governance` 8 · `oversight-explanation` 7 ·
`ai-code-insecurity` 4 · `risk-routing` 4 · `regulatory-compliance` 3 · `rules-based-checks` 3 ·
`oversight-scaling-inversion` 3 · `automation-bias` 3 · `formal-methods` 2 · three singletons.
Method facets: `built-system` 31 · `method-experiment` 18 · `method-mining` 17 · `design-only` 15 ·
`method-field-study` 11 · `method-self-report` 11 · `adopted` 6. **That distribution is itself a
finding: the corpus builds and demonstrates; it rarely deploys or measures.**

---

## 5. The learnings that should drive the RQs

These are drawn from `Emerging_Themes.md` and the Taxonomy Changelog. Each is a claim the corpus can
support and a place a research question could sit. Section markers refer to `Emerging_Themes.md`.

### 5.1 The inversion is real but conditional — and that changes the question

Branco (*LGTM!*) and Ehsani (*Where Do AI Coding Agents Fail?*) mine the **same** AIDev population and
report **opposite tails**: auto-merged agentic PRs (fail-open — review skipped, code ships) and
not-merged agentic PRs (fail-closed — PRs abandoned, throughput collapses). Branco reports acceptance
is **bimodally distributed** — repositories tend to auto-merge all or none — and that auto-merging is
*"less common in more mature, well-governed projects."*

> **The question is not *whether* the oversight inversion happens, but *in which organizations*, and
> what distinguishes them.** That is an empirical question about organizational characteristics —
> exactly what a survey can answer and a code audit cannot.

This is also the strongest available justification for the fieldwork, and it should probably be
visible in the RQ wording rather than buried in the significance section.

### 5.2 Misallocation, not overload — the norm inversion

Gao et al. (*On Autopilot?*) is the anchor. Beyond the headline (~80% of AI-co-authored PRs from
non-owners merged with no explicit review; 67.5% of AI-co-authored PRs come from contributors with no
prior code ownership; 86.9% of repositories have no AI-agent guidelines), the interesting finding is
the **reversal of an OSS norm**: for human-authored PRs non-owners receive the *most* feedback, for
AI-co-authored PRs they receive the *least*. Reviewers are present and responding — pointed the wrong
way. Candidate mechanisms, all untested: attribution laundering, diffusion of responsibility, surface
plausibility.

**A further slice, worked out on 2026-09-02 and not yet written into any methodology file** (see §8):
Gao reports aggregates, which conflate *whether anyone reviews* with *how closely they review when
they do*. Table 2 publishes both the means and the counts of PRs receiving no human feedback, so the
conditional is recoverable by division. Among merged PRs that drew **any** human engagement,
Human+AI contributions received at most ~1.6 reviews against 5.8–7.2 for human-authored ones. **The
shortfall is not only incidence but intensity** — which weakens the authors' own set-aside confound
(triviality predicts low review *incidence*, but explains less readily why engaged PRs still drew a
fifth of the customary attention).

### 5.3 Prescription versus violation

He et al. measure that AI-generated code *requires extra scrutiny* — complexity +41%, static-analysis
warnings +30%, both persistent, a *"comprehension tax regardless of functional correctness."* Gao
measures that it *receives less*. **Neither paper cites the other.** Independent prescription plus
independently observed deviation is a stronger argument shape than either finding alone, and it
converts "organizations should review AI code more carefully" from an assertion into a documented gap
between recommendation and behaviour — which is what an organizational study is positioned to explain.

He also defuses the standard counter-argument: the velocity gain is 3–5× in month one and **dissipates
after two months**, while the complexity and warning costs persist. **The gain is transient and the
cost is permanent, so the speed-for-quality trade being invoked is not the trade on offer.**

### 5.4 Only one of the two gates scales

Risk routing operates at two levels. **Gate 1 — access:** does this need human review *at all*?
Reduces the count of human touches; **this is where scaling lives.** **Gate 2 — depth:** given that it
does, how much? Reallocates a fixed workload; no scaling effect. A system with no gate 1 has a
human-attention cost that grows linearly with output no matter how good its prioritisation is.

A refinement that matters for counting: gate 1 is reached from **opposite directions** —
*load-reducing* ("what can safely skip review?", load down) and *coverage-ensuring* ("what must not
skip review?", load up, e.g. detect AI-authored code then review it harder). Only the load-reducing
kind is a scaling mechanism. **An organization adopting both is pulling in two directions**, and
whether the net effect relieves or worsens the inversion is an empirical question about the ratio.

Shared failure mode in both directions: **the absence of a routing signal gets read as a clean bill of
health.**

### 5.5 The inspection point may be absent, not merely degraded

The framing assumes oversight *degrades* under scale. A stronger possibility appears in the corpus: a
mode in which **no human inspects the artifact at any point.** Waseem's industry teams describe a
single "fix this" prompt rewriting large parts of a codebase *before architects or testers have seen
the previous version* — absence by drift. Töpfer's paper is titled *"…with no human code inspection"*
— absence by design, with a formal checker offered as the substitute.

> **An organization can arrive at zero inspection by design or by drift, and the two look identical in
> the artifact.** That distinction is precisely what an org study can detect and a code audit cannot.

Survey form: not *"how thoroughly is AI-generated code reviewed?"* but **"is there a point in your
process where a human is required to read it — and if not, what replaced that?"** The expected finding
is that some organizations cannot answer the second half.

### 5.6 The decision surface — what the human engages when they cannot read the artifact

A growing cluster (Kasibatla's Aporia, González's HiLDE, Zhou, and Virk & Liu) in which the human's
oversight object is **not an artifact but a curated decision**. Aporia names the problem: developers
*"cede decision-making authority to agents, often without realizing that important design decisions
are being made without them."*

Virk & Liu are the first to **measure** one — non-programmers assessing AI-generated code, given
delineated steps plus alternative approaches per decision. It **worked and was not enough**. Two
design variables come from Scott's HOS experience and are flagged as a *lens, not evidence*:
**altitude** (escalations pitched at code level are unreadable to anyone not already deep in the
codebase) and **options with analysis** (a decision surface without alternatives is a notification).
Options-with-analysis now has partial corpus support; **altitude remains untested by anyone** — a
genuine contribution opening.

### 5.7 "Where to look" is well covered; "does looking work" is not

Langer's signal-detection framing supplies the vocabulary the corpus lacks: **criterion** (how readily
the overseer accepts, properly set by defect base rate and cost of a miss) versus **sensitivity, d′**
(whether the overseer, once looking, actually detects). **Risk routing is criterion-setting.** The
corpus is heavily populated on criterion and thin on sensitivity — Eze operationalises it as override
rate (*"an extremely low override rate may indicate rubber-stamping"*) and little else does.

One level up, the same asymmetry: `automation-bias`, `oversight-theater` and `evaluator-reliability`
are all **determinants** of oversight effectiveness; the **outcome** — did oversight actually catch
anything — has no home in the instrument and almost none in the corpus. McKay is the only paper whose
subject is effectiveness itself, and it names the measurement gap outright.

**Direct survey convert:** *do organizations know whether their reviewers catch what gets routed to
them?* Most likely do not — which makes the gap simultaneously a literature finding and an empirical
one. **Caveat to check before reporting:** the asymmetry may be an artifact of an instrument built to
capture mechanisms rather than outcomes. Verify by counting before citing.

### 5.8 Two different things are called "scalable oversight"

**Quality scaling** = more *accurate* oversight per human-hour. **Throughput scaling** = more *code
overseen* per human-hour. **This review's premise is the second** — allocation, not augmentation.
OpenAI's usage is the first, and the papers say so plainly; their human never leaves any sample
because in an RLHF labelling regime the human's judgment *is* the product.

**The diagnostic:** does the paper measure *time or volume*, or only *accuracy*? McAleese reports
contractors taking fifty minutes per example and never claims the critic makes them faster. **Do not
cite quality-scaling results as throughput evidence.** Related: papers keep supplying *configuration*
performance (which arrangement reviews best) and almost never *allocation* rules (which items need
which arrangement) — routing evidence is what the review is actually short of.

### 5.9 The latency window

The corpus's mechanisms are not competing answers to one question; they occupy **different windows
between generation and consequence**, and the window determines which control is physically available.
Zero window (code executed on generation) → **containment only**, nobody ever reads it. Short window
(CI/CD, agentic PR) → automated gates and routing. Long window (spec, architecture) → human review,
explanation, debate. Borrowing across windows predicts the failure: a long-window mechanism applied to
a zero-window problem yields **oversight theatre**; a zero-window mechanism applied to a long-window
problem **forfeits understanding you had time to acquire**. **The dissertation sits in the middle
band, and saying so explicitly is useful scope-setting.**

### 5.10 Independence, and why it collapses under AI

Two axes, not one: independence *of the checker from the producer*, and independence *of generation
from intent*. A newcomer's AI-co-authored PR reviewed by nobody has **neither** — the weakest
configuration in the corpus, and at 67.5% the most common. The survey form is sharp:
**is the person who reviews AI-generated output the same person who prompted it?** An organization can
truthfully say "a human reviews everything" while having *less* separation than its pre-AI process.

### 5.11 The taxonomy finding, which belongs in the methods chapter

Named four separate times in one day of adjudication: **merging constructs that differ in their
evidence because they share vocabulary.** The load-bearing instance is §149a — `agent-panel` was
conflating two mechanisms with opposite evidence behind them. The discriminator is *what the agent
consumes*: the primary artifact → `agent-panel` (redundancy, weak — 2.4pp convergence gain, correlated
judge errors); another agent's output → `peer-critique` (mutual checking, strong — arbitration cut
change surface 83–90%; ReviewFilter made BitsAI-CR deployable; Jin's filter took FPR 88.74% → 39.96%).
**Consequence for the thesis: the corpus's strongest negative result stops being an attack on
multi-agent oversight and becomes a defence** — the failing mechanism is the one HOS does not rely on.
That claim was unavailable while the two shared a tag.

**And the scarcity finding underneath it:** 25 one-directional versus 3 mutual. The corpus builds
dedicated critics over producers; **agents checking *each other* is the scarce case.**

### 5.12 The methodological result about AI panels — usable as both method and finding

On the **residual** — proposals the human arbiter had not independently made — the three-vendor panel
ran at **50% precision (7 of 14)**. Overall precision is far higher, but **on contested tags, three
vendors agreeing unanimously is a coin flip.** Related: cross-model dissent did **not** predict human
disagreement (κ≈0.30, chance level), while a stratified Trust Check against human ground truth reached
κ=0.79. Run-to-run instability was roughly uniform across vendors (17–18 tripwires of 128 each) —
**replication, not model choice, carries the signal.**

This is the review's own instrument reproducing the corpus's finding, and it is the strongest
self-implicating credibility move available in any write-up or talk.

---

## 6. Gaps — where the corpus cannot answer, which is where RQs should aim

1. **RQ4 (regulated industries) is the thinnest.** Only three Phase-6 papers carry
   `regulatory-compliance` as a primary theme, and one of those is design-only with no author
   metadata. This cuts both ways: **a gap claim in the proposal's favour** (nobody has studied it) and
   **a risk for the literature review** (a chapter cannot compare strata it has no sources for). A
   targeted supplementary search is on the closeout list as item F5. **Decide in the brainstorm whether
   RQ4 survives as a research question, becomes an analysis dimension, or triggers the search first.**
2. **Effectiveness has no outcome measure** (§5.7). Nobody measures whether oversight catches
   anything.
3. **The corpus governs code quality, never commitment and forecast.** Every mechanism gates the
   *artifact*; nothing governs how much work is promised, sequenced, or estimated. **An oversight
   regime that gates merges but never gates intake will fill the queue faster than it drains it.**
   Open question worth asking: does forecast discipline even survive contact with agentic delivery,
   when an agent's cost is compute rather than person-hours and its failure mode is silent abandonment?
4. **The corpus is code-centric.** Agentic delivery produces requirements, test plans, architecture
   decisions, IaC, migration scripts, runbooks and documentation — each with a different reviewer, a
   different competence and a different failure mode. The literature says almost nothing about any of
   them. **This is a place the survey can answer what the literature cannot.**
5. **One technology, two settings.** The argument depends on assistive and agentic being one
   technology in two configurations, and **no corpus paper currently supports that claim.** Either find
   a source (a technical survey of code-assistant architectures would serve) or argue it as the
   review's own position and mark it as such.
6. **Everything is open source.** Both inversion papers, Gao, and most mining work are OSS repository
   studies. OSS maintainers can refuse work; employed reviewers often cannot. **Whether any of these
   patterns transfer to commercial settings is untested** — which is, again, the argument for the
   fieldwork.
7. **Altitude is untested** (§5.6) — a specific, small, publishable opening.
8. **Nobody has demonstrated the inversion to a strict standard.** Under the §88 leakage test (which
   demands *observed review absence* or *defects in merged code with review failure as cause*),
   `oversight-scaling-inversion` fires on exactly **one** paper of 72 — Gao. The corpus supplies volume,
   pressure, queue growth and merge speed instead. **The inversion is not disproven; it is not yet
   demonstrated to a strict standard anywhere in the screened literature.** Strong warrant for the
   fieldwork; a caution for how the premise is worded. ⚠ **This figure is unsettled** — see §7.

---

## 7. Cautions — do not repeat these numbers carelessly

- **The "1 of 72 clears the strict inversion test" figure is not final.** 144 F2 flags remain
  unadjudicated. Do not publish it, and hedge it in any RQ rationale.
- **`final:*` is not computed.** All theme/facet counts are provisional (§2).
- **The "AI code is ~1.7× buggier" premise traces to a single vendor source** (CodeRabbit, 470 PRs,
  AI-*co-authored* rather than autonomous, one platform's review taxonomy, and the vendor sells AI code
  review). Directional, not a settled effect size. Scope it precisely every time.
- **SonarQube ground-truth threat.** Studies using SonarQube's Maintainability Rating for
  technical-debt ground truth inherit a false-positive validity threat. Check exposure before leaning
  on any static-analysis-based number.
- **"New repos are less strict than older repos on AI policy" is not in Gao.** What Gao reports is
  planned versus reactive: of 19 repositories with guidance, 15 wrote it before adoption, 4 after, only
  1 updated docs, and **none revised in later patches** — governance written once and frozen.
- **PRISMA vocabulary.** The internal "Phase 1–6" scheme is a workflow convention, not PRISMA.
  Phases 4–6 are not post-inclusion activity; they *are* the eligibility determination executed as a
  multi-pass process. Write it as one PRISMA Eligibility→Included stage with a multi-pass method.
- **The HOS guardrail.** HOS informs **instrument design, not findings**. Practitioner experience
  shaping *which questions are worth asking* is ordinary survey practice; HOS architecture cited as
  evidence, or shaping the tagging instrument, is not. The HOS materials audit is deliberately
  scheduled *after* corpus close so contamination is structurally impossible rather than a matter of
  discipline — which is also the clean answer when the committee asks. Canonical citation: Thurlow
  (2026), Zenodo DOI 10.5281/zenodo.21347272.
- **Two metadata defects in Phase 6** would break a bibliography export: the Lumen paper (Goel) and
  the ethical/regulatory-risk quantification framework (Vanam) have no author metadata.

---

## 8. Not yet written down anywhere — capture this before it evaporates

A sustained analytical thread on Gao ran on 2026-09-02 and **was never written into
`Taxonomy_Changelog.md` or `Emerging_Themes.md`.** It produced material the RQ work should have:

- the three-way paradigm contrast (AI-only / Human+AI / Human-only) and what each column means;
- **the visibility fork** — reviewers *can* tell a PR is Human+AI if they look for the co-author
  trailer, but Gao never measures whether they do, so any claim that reviewers *discriminate* is an
  inference, not a finding;
- the **incidence versus intensity** decomposition and the conditional review rates (§5.2);
- **baseline contamination** — undisclosed AI-assisted PRs (autocomplete, chat-paste) sit inside the
  "Human-only" set, inflating its numbers, so the measured gap is **conservative**, i.e. the real gap
  is wider;
- **correlated cheap filters** — linters, CI style gates and a human's five-second scan are all
  surface heuristics, and AI-assisted code clears them together. Structurally the same pathology as the
  §149a correlated-judge-error result. It is not that AI code clears filters; it is that *human-curated*
  AI code does — AI supplies surface conformance, the human supplies substantive plausibility, and
  neither alone clears both classes.

**Ask Scott whether to write this up before or after the RQ session** — it is a synthesis-notebook
entry, and the incidence-versus-intensity argument in particular is close to a publishable critique.

---

## 9. Standing rules for the session

- **All assistant changes land via PR**, never direct to `main`. Branch `claude/<topic>` → push → open
  a PR describing what changed and why → Scott reviews and merges. Never merge without his explicit
  say-so.
- **The repo is PUBLIC.** Never commit `slr-phase4/txt/`, `Backups/`, `Downloads/`, `.envrc`, PDFs, or
  Zotero exports. Secret-scan staged content before every commit.
- **Never duplicate a Zotero record** — add the existing item to the new collection.
- **Never remove `v1` tags** — they are provenance.
- **Zotero writes need a library backup first**; RW key for writes, RO for reads.
- **All SLR data belongs in Zotero**, not left only in repo JSON or markdown.
- **Fable is expensive** — never run it without Scott's explicit per-run permission.
- **When naming papers**, use the author's surname where unambiguous, author plus title otherwise, and
  include the item key — but **keep item keys out of tables**, since they cannot be selected from one.
- **Preserve Scott's wording and style** in any document he authored.
