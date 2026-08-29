# Org survey instrument — design notes and question bank

**Status: QUEUED — do not start until the Accept band is closed.** Commissioned 2026-08-27.
This file currently holds the *specification* and the hooks banked so far; the audit itself waits.

## Commission

> *"An audit of the HOS documents, research findings, etc. and generate an MD that is a recommended
> list of questions to consider informed by HOS and our SLR work."* — and on HOS's role:
> *"HOS was a learning exercise so that we built domain knowledge to learn what questions are
> relevant. **Mine it.**"*

**Deliverable:** a question bank for the dissertation's organisational survey, each question traceable
to (a) a corpus finding, (b) an HOS operational learning, or (c) both.

## Why the timing is after the Accept band — two reasons

1. **The corpus must be closed.** Survey hooks are still accumulating paper by paper, and the
   cross-walk needs all 128 Phase-5 papers adjudicated.
2. **The HOS guardrail (the load-bearing reason).** HOS is comprehension input, never corpus evidence.
   Auditing HOS materials *while tagging is still running* risks HOS-derived framings leaking into
   Accept-band rulings. Running the audit **after all tagging closes makes contamination structurally
   impossible rather than a matter of discipline** — and *"the HOS audit was conducted after the corpus
   was closed"* is a clean answer when the committee asks how HOS influence was kept out of the coding.

## The guardrail's scope — state this in the methods chapter

**HOS informs INSTRUMENT DESIGN, not FINDINGS.** Practitioner experience shaping *which questions are
worth asking* is ordinary and defensible survey practice. What the guardrail forbids is HOS's
architecture being cited as evidence, or shaping the tagging instrument. Those are different acts and
the write-up should say so plainly rather than leave the distinction implicit.

## Survey hooks banked during the Light Read pass

Each already recorded in `Emerging_Themes.md` / `Taxonomy_Changelog.md` with its source paper.

| # | Question | Source |
|---|---|---|
| 1 | What lets a change **skip** review — and separately, what **forces** a change into review? Is it the same signal? | §86 Yang (intake restriction); §82 (two routing purposes) |
| 2 | Is there a point in your process where a human is **required to read** AI-generated code — and if not, what replaced that? | §81a zero-inspection (Waseem, Töpfer) |
| 3 | Has the share of senior engineers' time spent **reviewing vs authoring** changed since AI adoption? Do you measure senior original output separately, or only team throughput? | Xu §83 (substitution — the cost is invisible to aggregate throughput) |
| 4 | **What produces the signal** that decides review depth — the assistant itself, a different model, or a deterministic tool? Was that choice deliberate? | Independence thread §74; Yu §91 |
| 5 | Is there an **external reference** (spec, tests, formal constraints) against which AI output is checked — or only other models? | Zietsman §99f (diversity ≠ ground truth) |
| 6 | Do you govern **assistive and agentic** use under one policy, or bifurcate? | Tuape §78 (two-tiered adoption hypothesis) |
| 7 | When an agent needs a human decision, what does the human actually **see** — a diff, a summary, or a choice with alternatives and their costs? | Decision-surface cluster §96e; HOS altitude + options-with-analysis |
| 8 | Do you confirm **every step**, only at the **end**, or something in between — and was that chosen or defaulted? | Zhou `XK3P9C96` §97 |
| 9 | When AI contributions exceeded review capacity, did you **add reviewers, route by risk, or restrict what could be submitted**? | Yang §86 — 12 strategies usable as closed options |
| 10 | Does contributor **disclosure** of AI assistance exist? Is anything required *before* review begins? | Yang §86 |
| 11 | Do reviewers of AI-generated changes have enough information to determine **what was assumed** — not merely whether they have time? | Wang §80 (dimension collapse: representation vs capacity) |
| 12 | Does formal **sign-off** on AI-generated PRs change how often reviewers actually modify them? | Zhou & Zhao §95 (accountability → deference; needs code-domain testing) |
| **13** | **Is the person who reviews AI-generated output the same person who prompted it?** If so, what else in the loop is independent? | Bhatnagar §106 / independence second axis — an org can truthfully say "a human reviews everything" while having *less* separation than its pre-AI process |

## Source location — RESOLVED 2026-08-27

**HOS materials: `~/Code/Thurlow-Research/HumanOversightSystem/Human`** (arbiter). Plus the Zotero
`HOS/*` collections and `hos-area:*` tags already in the library.

**Not yet opened, deliberately.** Per the timing rule above, the HOS materials stay unread until the
Accept band closes, so nothing from them can influence Accept-band tagging.

## Method for the audit itself (proposed)

1. **Inventory HOS materials** — what was built, what was observed, what changed and why.
2. **Extract operational learnings** as candidate question seeds, each tagged with what prompted it.
3. **Cross-walk against the corpus** — for each seed, is there corpus support, corpus contradiction,
   or silence? *Silence is the interesting case: an HOS learning no paper addresses is a candidate
   contribution.*
4. **Merge with the banked hooks above**, dedupe, and group by construct.
5. **Mark provenance on every question** — corpus / HOS / both — so the instrument's design rationale
   is auditable and the guardrail is visibly respected.

## COVERAGE REQUIREMENT — ask across all DISCIPLINES, not just dev/test/UX (2026-08-28)

**Arbiter:** *"All aspects means **all disciplines**, not just dev, test, ux design."* Raised while
ruling `N7E3MR2V` (SDLC AutoPilot AI), whose lifecycle decomposition is retained as an
**instrument-design input** — a completeness prompt, not a citation (the paper is demoted, §132).

**The problem this fixes.** The corpus is **code-centric**: nearly every oversight mechanism reviewed
governs source artifacts — quality gates, scanners, review bots, conformance checks, complexity
thresholds, routing by predicted review effort. But agentic delivery produces **requirements, test
plans, architecture decisions, infrastructure-as-code, migration scripts, runbooks and
documentation**. Each has a **different reviewer, a different competence, and a different failure
mode**, and the literature says almost nothing about any of them.

**This is a place the survey can answer what the literature cannot** — where AI output is actually
landing across an organisation, and who (if anyone) checks it.

**Disciplines the instrument should cover:**
requirements / business analysis · architecture & design · **project management, estimation and
capacity planning** · development · test & QA · UX design · security · infrastructure / SRE /
platform · data & analytics · documentation and technical writing · release and change management ·
compliance and audit.

**Design implications:**
- **Ask per discipline, not once in general.** A single "do you review AI output?" collapses the
  variation that matters — the answer is plausibly *yes* for code and *no* for runbooks.
- **Ask who reviews, not just whether.** Reviewer *competence* is the live question outside
  development: a developer reviewing AI-generated IaC or a compliance mapping may not be qualified to
  catch its failures, and would not know it.
- **Expect asymmetric adoption.** Volume of AI output and depth of oversight are likely uncorrelated
  across disciplines; that asymmetry is itself a finding.
- **Cover the commitment side.** Estimation, work breakdown and capacity planning under agentic
  delivery — the gap recorded in `Emerging_Themes.md`. Every corpus mechanism gates *merges*; none
  gates *intake*.

**Guard:** discipline breadth must not dilute the instrument's focus on **scalable oversight**. The
question in each discipline is the same one — *what gets checked, by whom, and what is let through* —
not a general survey of AI adoption.

## QUESTION AREA — validating agent feedback (added 2026-08-28)

**Arbiter:** *"Will definitely want questions in survey for dissertation about **validating agent
feedback**."* Raised while ruling Sun / BitsAI-CR (`V4IRKSFI`).

**Why this area is high-value: the literature is nearly empty here.** Exactly **one** corpus paper
reports a production validation stage (BitsAI-CR's ReviewFilter, ByteDance, 12k WAU, 75% precision),
and **one** reports a lab equivalent (Jin's Fix-guided Verification Filter, FPR 88.74% → 39.96%).
Everything else measures reviewer accuracy and stops. **Practitioners will have experience the
literature does not**, which is the strongest reason to ask.

### What the corpus establishes, and therefore what to ask about

| Established | Question it generates |
|---|---|
| LLM reviewers false-positive heavily (Jin 88.74% FPR · Bugdar 24–58% precision · Raghavendra ~46% low-utility) | Do teams experience AI review as noisy? What do they do about it? |
| A validator stage measurably suppresses false positives, and is a **shared** stage (N+1, not 2N) | Is there **anything between the checker and the developer**? |
| Redundancy ≠ adjudication — intersection fails on correlated error (§11.4, 9/9 wrong) | Multiple models **agreeing**, or a second model **judging the finding**? |
| BitsAI-CR retires rules developers ignore (Outdated Rate) | Is there a **feedback loop from developer behaviour back into the checks**? |
| A second checker's real value is **missed requirements**, not missed defects | What do AI reviewers actually catch that humans miss? |

### Draft question directions (not final wording)

1. **Existence of a validation stage.** When an AI reviewer produces a finding, does anything filter,
   rank or suppress it before a human sees it? Who built it, and can they turn it off?
2. **Architecture, stated concretely rather than by label.** Avoid asking "do you use a multi-agent
   panel" — the corpus shows *"multi-agent"* predicts nothing. Ask instead: *do several checkers run
   on the same code? Must all pass? What happens when they disagree — block, iterate, or escalate?*
   That distinguishes conjunctive gate · advisory · negotiated convergence without jargon.
3. **Observed precision, and the response to it.** Roughly what fraction of AI review comments are
   acted on versus dismissed? Has anyone **turned a check off** because it was too noisy? *(Rule
   retirement is a strong, concrete signal — it happens or it doesn't.)*
4. **Measurement.** Does anyone track whether the AI reviewer is right? What metric — and critically,
   **is anything measured about what it MISSES?** BitsAI-CR measures precision and adoption and never
   surfaces suppressed findings; if practitioners are the same, that is a finding.
5. **What it catches.** Free-text or checklist: defects, style, security, **missed requirements**,
   **missed edge cases**. The corpus predicts the last two dominate; practitioners can confirm or
   refute.
6. **Escalation.** When AI review and a human disagree, who wins, and is that written down anywhere?

### Design cautions specific to this area

- **Karakaya's contamination applies directly** (§122a). Asking *"do you act on AI review comments?"*
  collects a signal shaped by *"release pressure, ownership boundaries, or timing"*, not by comment
  quality. **Prefer questions about mechanisms and observable events** (*is there a filter? has a check
  been turned off?*) over questions about attitudes or perceived usefulness.
- **Do not ask by architecture name.** Five topologies in the corpus are all described as
  *"multi-agent"* by their authors. Ask what happens on disagreement; infer the shape.
- **Suppression is invisible to practitioners too.** If nobody measures what the filter removed, they
  cannot report it — so ask whether it is measured, not what the number is.
- **Expect the honest answer to be "nothing."** Most teams likely have a raw AI reviewer wired to PRs
  with no validation stage at all. **That is the finding**, and it is the gap BitsAI-CR's production
  evidence says matters.
