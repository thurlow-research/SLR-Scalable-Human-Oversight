# Pass 2 Review Prompt — Claude Opus
## Vibe Coding Governance SLR — Stage 2 Opus Review

---

## CRITICAL INSTRUCTIONS

You are performing a deep review of papers that a prior screening pass could not
confidently classify. This is a FRESH SESSION. Disregard any prior conversation
history. Apply only the criteria in this prompt.

Each paper below includes the title, abstract, and the prior screener's decision,
confidence level, and rationale. Your job is to make a **final binary decision**
(keep or discard only — no maybe). You must commit.

---

## RESEARCH CONTEXT

This SLR examines how **software engineering organizations** recognize and manage
risk from AI-generated code and "vibe coding" — specifically how human oversight
of AI-generated code can scale without sacrificing quality.

The domain anchor: **a software engineering team or engineering manager managing
AI-generated code at scale.**

---

## WHY THESE PAPERS ARE HERE

Papers reach this review for one of three reasons:
1. Prior screener returned `maybe` — genuine ambiguity, competing arguments for both keep and discard
2. Prior screener returned `keep` with `low` confidence — operationalizable but scope/transferability uncertain
3. Prior screener returned `discard` with `low` confidence — appeared off-topic but screener was uncertain

Your task is to resolve the ambiguity with deeper reasoning.

---

## THE OPERATIONALIZABILITY TEST

**"Does this paper give a software engineering organization something they can
act on — a measurement, metric, mechanism, detection signal, framework, or process?"**

- YES → candidate for Keep (apply tier criteria)
- NO → Discard

---

## TIER 1 — DIRECT HITS

| Topic | Keep if... | Discard if... |
|---|---|---|
| Vibe coding / AI code generation | Has governance, risk, or oversight implication | Purely definitional, no actionable finding |
| Code review capacity / scalability / fatigue | Addresses reviewer workload, triage, prioritization with AI volume angle | Pure process improvement without AI/oversight angle |
| AI code risk / quality | **Quantifies** with reproducible methodology | Descriptive only — no measurement method |
| Org governance of AI coding tools | Empirical, case study, or framework at org/governance level | Tool capability without org governance angle |
| Developer oversight of LLM code | Human review practices, override, trust calibration | Productivity paper without oversight angle |

---

## TIER 2 — TRANSFERABLE

**Tiebreaker: "Could a software engineering team adopt this directly without
substantial domain re-derivation?"**

For Tier 2 papers, explicitly work through:
1. What is the mechanism/framework the paper presents?
2. What would need to change to apply it to AI code review?
3. Is that translation trivial (keep) or substantial (discard)?

| Topic | Keep if... | Discard if... |
|---|---|---|
| Human oversight frameworks | Mechanism generalizes to code review | Non-transferable domain-specific loop |
| AI governance with DevSecOps angle | Explicitly addresses software/engineering orgs | No software/code connection |
| EU AI Act / NIST / CISA | Software system compliance discussed | Non-software high-risk AI systems only |
| Legal liability for AI outputs | Addresses code OR generalizes to code | Creative content only |
| Scalable oversight for high-volume AI | Scaling mechanism transfers to code review | Non-transferable domain |

---

## REASONING APPROACH

For each paper:
1. Summarize in one sentence what the paper actually does (not just what it's about)
2. State the strongest argument FOR keeping it
3. State the strongest argument AGAINST keeping it
4. State your final decision and why one argument wins

This reasoning goes in your rationale field — keep it concise but show the work.

---

## DECISION DEFINITIONS

**keep** — Paper presents an operationalizable contribution relevant to AI code
governance, oversight scaling, or risk measurement in software contexts. You are
committing — this paper goes into the synthesis corpus.

**discard** — Paper fails the operationalizability test, is descriptive-only,
or domain-specific without transferable contribution. You are committing.

No maybe. You must resolve the ambiguity.

---

## CONFIDENCE DEFINITIONS

**high** — Decision is clear after working through the reasoning.

**medium** — Decision required judgment but you are confident in the outcome.

**low** — You reached a decision but a human should verify before finalizing.
Use sparingly — if more than 20% of your decisions are low confidence, the
papers should escalate to human review rather than being resolved here.

---

## OUTPUT FORMAT

Return ONLY a CSV block with no preamble, explanation, or postamble.
Include the header row. One row per input item. Do not skip any rows.

```
item_key,decision,confidence,rationale,prior_decision,prior_confidence
ABCD1234,keep,medium,"Paper presents automation bias framework with three detection mechanisms directly applicable to code review contexts; domain is aviation but the trust calibration model transfers without re-derivation",maybe,medium
EFGH5678,discard,high,"Despite human oversight framing the loop is judicial sentencing — the feedback mechanism has no structural parallel to code review; transferability argument does not hold",maybe,medium
```

Rules:
- decision must be exactly: keep or discard (no maybe)
- confidence must be exactly: high, medium, or low
- rationale shows your reasoning — stronger argument wins — max 2 sentences
- prior_decision and prior_confidence copied exactly from input
- Return ALL input rows
- item_key copied exactly from input

---

## INPUT

The following CSV contains papers for deep review.
item_key,title,abstract,prior_decision,prior_confidence,prior_rationale
[PASTE REVIEW CSV HERE]
