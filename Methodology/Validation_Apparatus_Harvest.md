# Validation apparatus in the wild — harvest

**Zotero collection:** `Dissertation Lit Review / 04 - Validation Apparatus` (`XPPEXKBN`).
Membership is **additive and orthogonal to SLR tier** — a Context paper can and often will belong here.

## What this is, and why it exists

A record of **how each paper validated AI-generated code** — what layers, in what order, where the human
sits, and what triggers escalation — harvested from **methods sections**, independent of what the paper
set out to argue.

**The claim it supports.** A methods section is evidence about **what its authors considered adequate
validation**. Nobody made them layer their checks; the layering is a *revealed belief* about where
machine checking runs out and a human becomes necessary. That is evidence about **norms**, and it is
available even in papers whose findings are irrelevant to this review.

## Why it is needed — tier assignment is itself risk routing

Arbiter, 2026-08-27: *"'what that loses' sounds a lot like risk routing."* Exactly so, and the parallel
is uncomfortable enough to state plainly:

> **Core/Context is a routing decision, and Context is our un-routed remainder.** §42 short-circuits tag
> verification on a demote, and downstream those papers get read as "nothing here" — which is precisely
> the failure staged as a tripwire from `ZBF86IJM` (§79): **the absence of a routing signal is
> interpreted as a clean bill of health.**

**This harvest is the mitigation for our own un-routed remainder.** It belongs in the methods chapter
next to the reflexivity note at §11.8, as a worked case of the review applying its own findings to
itself — and, unlike the §11.8 illustration, this one changed what we do.

## Scope — the 128, then decide

**Start with the Phase-5 128.** A hard constraint decides it: **full texts exist only for those**
(`slr-phase4/txt/`). The wider Context pool was screened on titles and abstracts, so harvesting from it
means fetching hundreds of PDFs first.

**Measure the yield, then choose.** If 128 papers give a thin or repetitive picture, expansion is not
worth the retrieval cost; if a real typology of validation layering emerges, that justifies the fetch.
Calibrate-then-scale, as with every other pass here.

**If expanding later, do NOT blanket-scan abstracts** — abstracts almost never describe validation
apparatus. Expand by **targeted retrieval** on abstracts mentioning validation, review, or evaluation
pipelines, then read methods sections.

## What to record per paper

| Field | Notes |
|---|---|
| Layers, in order | e.g. lexical → semantic → human |
| Automated components | what kind of check, and whether deployable or reference-grounded (§51) |
| AI-as-checker | present? same model as generator, or different vendor? (feeds `cross-model`) |
| **Human position** | where the human sits, and **what triggers** their involvement |
| Escalation trigger | threshold, disagreement, risk class, or none |
| Stated rationale | did they *argue* for the layering, or just use it? (decides §104 tier) |
| Domain | safety-critical, general, competitive-programming, etc. |

## Entries

### `VG8PSMM7` — Adnyana & Schwung (2026), *Benchmarking and validation of prompting techniques for AI-assisted industrial PLC programming* · **SLR: Context**
- **Layers:** BLEU (lexical similarity) → **LLM-in-the-Loop (LITL)** semantic check across four
  dimensions — functional correctness, readability, safety compliance, modularity → **Human-in-the-Loop
  (HITL)** expert review for safety-critical code.
- **AI-as-checker:** yes, and **cross-vendor** — DeepSeek and Gemini 2.5 Pro generate ST/IL; syntax is
  cross-checked by ChatGPT-4o and Copilot Pro. *Whether the separation is argued for or incidental is
  unresolved — flagged for the harvest, not for tagging.*
- **Human position:** terminal, and scoped to **safety-critical** review — the human is not asked to
  check everything, only what the domain marks as dangerous.
- **Domain:** industrial automation, IEC 61131-3, Siemens TIA Portal / Beckhoff TwinCAT.
- **Why it matters:** the team judged lexical similarity insufficient, added a semantic machine check,
  and **still would not let safety-critical code through without a human**. A three-rung ladder with the
  human at the top, chosen without anyone requiring it.

### `FZK2QB5A` — Alshahwan, Harman et al. (Meta, 2024), *Assured offline LLM-based software engineering* · **SLR: Context**
- **Layers:** a **series of semantic filters** applied to LLM-generated candidates — build success, unit
  tests, linters, and any further *"syntactic or semantic filter"*. Explicitly extensible: *"The filters
  depicted in Figure 1 are merely illustrative."*
- **Filter semantics:** *"Filters tend to be boolean; either the candidate code passes through the
  filter or it is **discarded**."* Generalisable to a real-valued **fitness measure** by scoring the
  degree of failure — the authors' own framing (Genetic Improvement).
- **AI-as-checker:** no. The checks are conventional CI machinery; the LLM is the *generator* only.
- **Human position:** **outside the assurance loop entirely.** Stated goal is code improvement
  *"independently of any human"*, with the human as *"final code reviewer, as they would do with code
  generated by other human engineers."* **Asserted once, never developed.**
- **Escalation trigger:** none. Failing candidates are discarded, not escalated.
- **Twin guarantees:** (1) no regression of the original code's properties, (2) verifiable and
  measurable improvement — **both defined against existing behaviour**, not against derived intent.
- **Domain:** general software at Meta scale; offline/batch rather than IDE.
- **Why it matters — the contrast with `VG8PSMM7`:** two papers, two opposite placements of the human.
  Adnyana puts the human **terminal and scoped to safety-critical**; Alshahwan puts the human
  **outside the loop**, on the argument that assurance filters make AI code no more burdensome to
  review than human code. **Neither position is defended empirically. The choice appears to follow from
  domain risk, not from evidence** — a hypothesis the org survey can test directly.
- **Caveat for the harvest:** these filters are **fitness functions inside a search**, not gates on a
  deliverable (§105a). When comparing apparatus across papers, record *where in the pipeline* a check
  sits — the same machinery means different things at different positions.

### `P837LJWE` — Bhatnagar (2026), *Modernization of enterprise payment infrastructure* · **SLR: Context**
- **Layers:** a **five-stage constraint-based protocol** — (1) human sets non-negotiable constraints
  (PCI-DSS, sub-2s latency); (2) LLM proposes architectural patterns; (3) trade-off analysis against
  operational complexity and resilience; (4) LLM generates with security hardening (CSP, CSRF) by
  default; (5) **Strategic Governance gate** — human judgement, *"frequently resulted in 'strategic
  rollbacks' in which proposed AI optimizations were **rejected**"*.
- **Determinism controls:** frozen model version (Claude 4 Sonnet), **temperature 0**, chain-of-thought
  prompting, and **cross-verification across multiple scanning passes** to confirm the 29.4% code
  reduction was consolidation rather than lost functional coverage. *The most explicit reproducibility
  apparatus in the harvest so far.*
- **AI-as-checker:** no. The LLM analyses and generates; all checking is human.
- **Human position:** **both ends** — constraints before generation, governance gate after. But
  **the same person occupies both**, and there is no second reviewer (§106 / independence second axis).
- **Escalation trigger:** rejection criteria named — architectural complexity threatening low-risk
  operational continuity, or exceeding resource budgets.
- **Domain:** PCI-DSS-regulated payment infrastructure; 85k lines C# → 60k TypeScript; `adopted`.
- **Why it matters:** the only harvest entry so far with an **observed, exercised refusal state in
  production**, and the only one with named rejection criteria. Also the clearest case of the
  prompter-as-reviewer configuration.

## Back-fill candidates from the Light Read band (at closeout)
`72W6R4JG` Töpfer (FCL constraint verifier + bounded repair loop) · `TA6GIUK2` Zietsman (BDD vs AI
review head-to-head) · `96XE669R` Zhong (VeriCode's 30 deterministic verifiers) · `VZ27QUPQ` Zhuo
(Dr.Fix detect-reason-fix; **reference-grounded — note the §51 disqualifier**) · `T2EG4BE2` Waseem
(three-layer testing discipline + CI gates).
