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

### `6NTZ85CW` — David & Gervais (2025), *Multi-agent penetration testing AI for the web* (MAPTA) · **SLR: Context**
- **Layers:** LLM orchestration → tool-grounded execution (nmap, ffuf, etc.) → **mandatory
  proof-of-concept validation** of every finding.
- **The distinctive move — validation by execution.** Findings are not flagged; they are **proven** by a
  working end-to-end exploit. **Ground truth is self-demonstrating**, so no human adjudicates whether a
  finding is real. Removes the false-positive triage burden entirely.
- **AI-as-checker:** yes, and fully autonomous — *"penetration testing **without human**."*
- **Human position:** **none.** Explicitly framed as a shift *"from human-dependent pattern recognition
  to adaptive adversarial execution."*
- **Agent structure:** **role specialisation, not a panel** (§110a) — Coordinator orchestrates, Sandbox
  agents execute. Nothing votes.
- **Escalation trigger:** none for humans. Machine-side early-stopping at ~40 tool calls or $0.30.
- **Economics:** $21.38 total across 104 challenges; median $0.073 per success vs $0.357 per failure.
  **The only apparatus entry with a cost model.**
- **Domain:** general web applications (XBOW benchmark), not AI-generated code.
- **Why it matters:** the strongest counter-example in the harvest to human-in-the-loop framing — a
  check that is *more* trustworthy for having no human in it, because it proves rather than judges.
  **Bounded by defect class:** works where a defect is demonstrable by execution (SSRF, injection,
  misconfiguration at 83–100%), fails where it is not (blind SQLi **0%**, XSS 57%). **That boundary is
  the finding worth carrying — validation-by-execution does not generalise to defects you cannot
  exploit on demand.**

### `PDYJGF2R` — Dora, Lunkad, Aslam et al. (2026), *The hidden risks of LLM-generated web application code* · **SLR: Context**
- **Layers:** a single layer — a **purpose-built security checklist** applied by the authors to code
  generated by five LLMs (ChatGPT, DeepSeek, Claude, Gemini, Grok).
- **The apparatus IS the checklist**, and it is a stated contribution: *"We have created a comprehensive
  checklist along with risk for systematic analysis of web applications generated by LLMs."* Built
  because the authors judged existing assessment inadequate for LLM-generated code.
- **Coverage:** authentication mechanisms, session management, input validation, HTTP security headers.
  Referenced against NIST cybersecurity guidelines.
- **AI-as-checker:** no. Human-applied checklist against generated artifacts.
- **Human position:** the human **is** the check — there is no automated layer at all.
- **Escalation trigger:** none; it is an assessment instrument, not a pipeline.
- **Finding:** *"none fully align with industry best practices"* across all five models.
- **Why it matters:** the harvest's **least automated** entry, and a useful pole. Where MAPTA
  (`6NTZ85CW`) removes the human entirely via validation-by-execution, this removes the machine
  entirely and puts a human with a checklist against the artifact. **Two papers, same year, opposite
  answers to who does the checking — and neither justifies its choice against the alternative.**

### `399HN438` — Dutta, Sharma, Rajgor et al. (2025), *Turbocharging pull request reviews* (CodeEvaluator) · **SLR: Context**
- **Structure — the harvest's first PARTITIONED apparatus.** Where other entries *layer* checks in
  sequence, this one *divides* them by defect class: five agents run against the same diff —
  **Code Review** (issues in the diff), **Bug Report**, **Code Smell**, **Code Optimization**
  (reinforcement-learning based), **Security Vulnerability Detection**.
- **AI-as-checker:** yes, throughout. No deterministic layer described.
- **Human position:** terminal and unspecified. The paper notes *"the necessity for human oversight"*
  and *"the extent of human oversight required"* as open challenges rather than describing where the
  human sits. **The apparatus is fully specified; the human's role is not.**
- **Escalation trigger:** none described.
- **Coverage rationale:** the decomposition is itself the claim about adequacy — five defect classes
  are treated as spanning what review must catch. **Nobody argues for the five, or for why five.**
- **Domain:** general pull requests (`general-code`), not AI-generated code.
- **Why it matters:** the clearest statement in the harvest of *coverage-by-partition* — an implicit
  theory that adequate review means checking a defined set of defect classes. Contrast Adnyana's
  ladder (`VG8PSMM7`, escalating rigour) and MAPTA's proof (`6NTZ85CW`, execution as ground truth).
  **Three different implicit answers to "what makes a check adequate": more rungs, more classes, or
  proof.**

### `UIXCRBQX` — Ferdous, Banik, Chowdhury & Shamim (2026), *Safer builders, risky maintainers* · **SLR: Core**
- **Apparatus:** a purpose-built **AST-based breaking-change detector**, run over 8,593 PRs and 60,324
  patches (7,191 agentic vs 1,402 human) from the AIDev dataset, Python repositories.
- **What makes it distinctive:** the check is **structural and deterministic** — abstract syntax tree
  comparison for backward-compatibility violations. No model judges anything. Contrast the LLM-judge
  apparatus elsewhere in this harvest.
- **AI-as-checker:** no. The AI is the *subject*, not the checker.
- **Human position:** none in the apparatus; humans appear only in the **recommendation** —
  *"enhanced, task-specific review policies."*
- **Escalation trigger — the contribution:** **task type**. Maintenance work (refactoring 6.72%, chore
  9.35%) carries roughly double the breaking-change risk of generation (3.45%). A computed,
  producer-independent signal for where review effort should go.
- **The negative result is the more useful one.** Agent **self-reported confidence** fails as a
  triage signal: 99.9% of PRs self-score 8–10, and breaking-change rates across that band are flat
  (3.94% / 3.96% / 3.16%). **A signal with no variance cannot triage anything.**
- **Why it matters to the harvest:** the first entry whose contribution is a **signal for allocating
  review** rather than a mechanism for performing it — and the only one that tests a *candidate* signal
  and reports it failing. **Apparatus design usually reports what worked; this reports what does not,
  which is rarer and more actionable.**

### `3Z45M3V3` — Fu, Liang, Tahir et al. (2023), *Security weaknesses of Copilot generated code in GitHub* · **SLR: Core**
- **Apparatus:** off-the-shelf static analysers over AI-generated code found in real repositories —
  **CodeQL** (general purpose), **ESLint** (JavaScript), **Bandit** (Python). Nothing purpose-built.
- **The loop, and the reason this entry matters:** detector → **warning message as prompt** → LLM
  repair → re-scan to verify. **An external deterministic detector driving repair by the model that
  produced the defect.**
- **AI-as-checker:** no — the AI is the *fixer*, the static analyser is the *checker*. That separation
  is the point.
- **Human position:** none in the loop. The human chooses the tooling and reads the outcome.
- **Escalation trigger:** none; every detected weakness is sent for repair.
- **Measured effect — the only priced intervention in the harvest.** Unaided self-repair fixes
  **19.3%** of security issues; supplying the static-analysis warning raises it to **55.5%**. Success
  *"varies between CWEs."*
- **Domain:** real GitHub projects, Python and JavaScript; 733 snippets, 43 CWEs, 8 in the CWE Top-25.
- **Why it matters:** the harvest's clearest demonstration that **an external signal is worth more than
  a better prompt**. Every other entry asserts that layering helps; this one measures the gap between
  self-check and externally-informed check, with commodity tooling any team already has. **Nearly
  triples the fix rate — and still leaves 44.5% unfixed**, which is the part to quote when someone
  proposes static analysis as sufficient.

### `4T5QFWZE` — Huang, Jaisri, Shimizu et al. (2026), *More code, less reuse* · **SLR: Core**
- **Apparatus — two instruments, deliberately paired.** (1) **Internal quality:** LOC, Cyclomatic
  Complexity, and a purpose-built **Max Redundancy Score (MRS)** using Type-4 semantic-clone detection.
  (2) **External perception:** **sentiment analysis of reviewer comments** on the same PRs.
- **Why the pairing is the contribution:** the apparatus measures the artifact **and** the humans
  looking at it, on the same objects. Every other harvest entry measures only the artifact.
- **AI-as-checker:** no. Deterministic clone detection plus NLP sentiment over human comments.
- **Human position:** the humans are the **measurand**, not the mechanism — the only entry where
  reviewers are what gets assessed.
- **The finding the pairing enables:** objective quality **down**, reviewer sentiment **up**. Neither
  instrument alone could show it; the gap between them *is* the result.
- **Why it matters to the harvest:** the strongest argument yet for **instrumenting the reviewer, not
  only the artifact**. An apparatus that only measures code quality would have reported redundancy and
  missed that nobody noticed — which is the part that matters for oversight.

### `A5WDGC7J` — Jin, Wang, Guo et al. (2026), *Are LLMs reliable code reviewers?* · **SLR: Core**
- **Apparatus — the only entry where the validator is the thing being validated.** Every other entry
  here builds an apparatus to judge *code*. This one builds an apparatus to judge **judges**: paired
  datasets (a conformant program and a seeded-buggy variant of the same requirement), five LLM
  reviewers (three closed, two open), verdicts forced into structured JSON (**verdict + rationale +
  fix**), scored against ground-truth `bug_type` labels.
- **What it treats as adequate validation of a reviewer:** not agreement rate — **two-sided error**.
  FPR and FNR reported separately, because the two failures have opposite operational costs and an
  aggregate accuracy figure hides which one you are buying.
- **AI-as-checker:** yes, and that is the object of study rather than the method.
- **Human position:** absent by design — no human arm. The paper measures what the machine reviewer
  does **unsupervised**, which is what makes it usable as evidence about the unsupervised case.
- **Escalation trigger:** the **Fix-guided Verification Filter** — when the judge returns NO *and*
  proposes a fix, execute both the original and the fixed program against the benchmark tests **plus**
  a GPT-4o-generated augmented set, and decide on four outcomes. **FPR 88.74% → 39.96%** (GPT-4o/MBPP).
- **The transferable design lesson:** a rejecting reviewer can be **cheaply second-guessed by
  execution**, because a NO verdict comes with a testable claim attached — the proposed fix. This is
  differential evidence, not a second opinion, and it needs no additional model to adjudicate.
- **The caution that comes with it (§120b):** the filter only runs where an executable test suite
  already exists, and it leans on an LLM to generate the augmented tests. Released as a
  **reproducibility artifact**, not as a deployable component — do not read it as a shipped tool.
- **Why it matters to the harvest:** it supplies the failure mode the other entries assume away.
  Apparatus built on AI-as-checker generally worries about **missed defects**; Jin shows the dominant
  error can be the opposite — **rejecting correct work** — which no amount of adding reviewers fixes,
  and which burns exactly the human attention that oversight is trying to conserve.

## Back-fill candidates from the Light Read band (at closeout)
`72W6R4JG` Töpfer (FCL constraint verifier + bounded repair loop) · `TA6GIUK2` Zietsman (BDD vs AI
review head-to-head) · `96XE669R` Zhong (VeriCode's 30 deterministic verifiers) · `VZ27QUPQ` Zhuo
(Dr.Fix detect-reason-fix; **reference-grounded — note the §51 disqualifier**) · `T2EG4BE2` Waseem
(three-layer testing discipline + CI gates).
