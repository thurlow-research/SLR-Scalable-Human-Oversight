# Pass 2 Screening Prompt — Claude Sonnet 4.6
## Vibe Coding Governance SLR — Stage 2 Title/Abstract Screen

---

## CRITICAL INSTRUCTIONS

You are screening academic papers for a systematic literature review. This is a
FRESH SESSION. Disregard any prior conversation history entirely. Apply only the
criteria in this prompt. Do not let earlier batches influence this batch.

---

## RESEARCH CONTEXT

This SLR examines how **software engineering organizations** recognize and manage
risk from AI-generated code and "vibe coding" — specifically how human oversight
of AI-generated code can scale without sacrificing quality.

The domain anchor for every decision: **a software engineering team or engineering
manager managing AI-generated code at scale.**

---

## YOUR TASK

Screen each paper using the operationalizability test and criteria below.
For each paper output: item_key, decision, confidence, rationale.

---

## THE OPERATIONALIZABILITY TEST (apply first)

Before classifying, ask: **"Does this paper give a software engineering organization
something they can act on — a measurement, metric, mechanism, detection signal,
framework, or process?"**

- YES → candidate for Keep (apply tier criteria below)
- NO (paper only establishes that a problem exists) → Discard

---

## TIER 1 — DIRECT HITS (Keep if operationalizable)

| Topic | Keep if... | Discard if... |
|---|---|---|
| Vibe coding / AI code generation | Has governance, risk, or oversight implication beyond "AI writes code" | Purely definitional with no actionable finding |
| Code review capacity / scalability / fatigue | Addresses reviewer workload, triage, prioritization, or throughput — especially with AI volume | Pure process improvement without AI volume or oversight angle |
| AI code risk / quality | **Quantifies** defect rates, vulnerability classes, or quality metrics with reproducible methodology | Descriptive only — "AI code has more bugs" without measurement method |
| Org governance of AI coding tools | Empirical, case study, or framework at the organizational/governance level | Tool capability paper without org governance angle |
| Developer oversight of LLM-generated code | Human review practices, override mechanisms, trust calibration for AI code | Developer productivity paper without oversight angle |

---

## TIER 2 — TRANSFERABLE (Keep if framework generalizes to software context)

Tiebreaker: **"Could a software engineering team adopt this directly without
substantial domain re-derivation?"** If yes → Keep. If requires significant
translation → Discard.

| Topic | Keep if... | Discard if... |
|---|---|---|
| Human oversight frameworks | Mechanism generalizes to code review (automation bias, signal detection, Parasuraman levels, etc.) | Domain-specific HITL (lab automation, robotics, judicial) — non-transferable loop |
| AI governance with software/DevSecOps angle | Explicitly addresses software development, DevSecOps pipelines, or engineering orgs | General AI governance with no software/code connection |
| EU AI Act / NIST AI RMF / CISA | Article 14 / software system compliance discussed | Non-software high-risk AI systems only (medical devices, credit scoring, HR) |
| Legal liability for AI outputs | Addresses code specifically OR framework generalizes to code | Creative content copyright only (text, images, music) — no code angle |
| Scalable oversight for high-volume AI output | Scaling mechanism transfers to code review context | Domain-specific volume/oversight with no structural parallel to code review |

---

## COMMON DISCARD PATTERNS — PASS 2

These were the primary false positives from Pass 1. Be alert:

1. **Descriptive-only risk** — establishes AI code is risky/vulnerable but presents no measurement method, detection signal, or governance response
2. **Domain-specific governance** — EU AI Act, NIST, or AI governance applied exclusively to non-software domains (clinical AI, financial AI, HR AI, autonomous vehicles)
3. **Non-software HITL** — human-in-the-loop papers where the loop is physical, scientific, or judicial (materials science, lab automation, judicial decision-making)
4. **General AI ethics/philosophy** — fairness, accountability, transparency without an operational mechanism
5. **Creative content copyright** — AI-generated text, images, music — no code angle
6. **Agentic AI as infrastructure** — multi-agent systems or autonomous agents without oversight, governance, or control mechanism
7. **Organizational AI adoption — productivity only** — ROI, efficiency, change management without risk, governance, or oversight angle

---

## DECISION DEFINITIONS

**keep** — Paper presents an operationalizable contribution directly relevant to
AI code governance, oversight scaling, or risk measurement in software contexts.

**maybe** — Genuine ambiguity that cannot be resolved from the abstract alone:
transferability is plausible but requires argument; abstract is substantive but
domain applicability is unclear. NOT for thin abstracts — use keep/discard with
low confidence for those. Reserve maybe for papers where you can articulate
competing reasons for both keep and discard.

**discard** — Paper fails the operationalizability test, is descriptive-only,
or is domain-specific without transferable contribution.

---

## CONFIDENCE DEFINITIONS

**high** — Rubric applies clearly and unambiguously. You would reach the same
decision on re-read.

**medium** — Rubric applies but requires judgment on one dimension (e.g.
transferability is plausible but not certain; abstract mentions measurement
but scope is unclear).

**low** — Genuinely uncertain. Thin abstract, ambiguous domain, or competing
rubric criteria pulling in different directions. Flag for deeper review.

Target distribution: aim for ~20-30% medium or low confidence across the batch.
If >85% are high confidence, you are likely over-confident — recalibrate.

---

## OUTPUT FORMAT

Return ONLY a CSV block with no preamble, explanation, or postamble.
Include the header row. One row per input item. Do not skip any rows.
Do not add markdown formatting or code fences.

```
item_key,decision,confidence,rationale
ABCD1234,keep,high,"Empirical study measuring AI code defect rates by vulnerability class with reproducible methodology — directly operationalizable for org risk scoring"
EFGH5678,discard,high,"EU AI Act analysis focused exclusively on medical device classification — no software or code angle"
IJKL9012,maybe,medium,"Human oversight framework from autonomous vehicle domain — transferability to code review is plausible but requires domain argument not resolvable from abstract"
MNOP3456,keep,low,"Abstract mentions AI code governance framework but scope and methodology unclear — thin abstract prevents confident classification"
```

Rules:
- rationale is ONE sentence maximum
- rationale explains WHY, not what the paper is about
- decision must be exactly: keep, maybe, or discard
- confidence must be exactly: high, medium, or low
- Return ALL input rows — never filter or skip rows
- item_key must be copied exactly from input — do not modify or generate new keys

---

## INPUT

The following CSV contains the papers to screen.
item_key,title,abstract
[PASTE BATCH CSV HERE]
