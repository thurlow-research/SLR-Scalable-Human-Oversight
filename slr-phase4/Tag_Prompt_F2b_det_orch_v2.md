# Tagging instrument — F2b: `deterministic-orchestration-v2` only

**Instrument of record for the F2b run** (`Taxonomy_Changelog.md` §151). Do not use this for general
tagging — it is deliberately partial: **one facet**.

**Population:** the 72 papers in `Phase 6 - Kept Core` (`R9ZHDXMN`). All have full text.
**Panel:** 3 vendors (opus, codex, gemini), one run each — the F2 configuration.

---

## 0. WHAT THIS RUN IS, AND WHAT IT MUST NOT DO

You are applying **one new facet**, `deterministic-orchestration-v2`, to a corpus whose **existing tags
are already settled by a human arbiter**. Those tags are **not under review**. You are not being asked
whether the paper's primary theme is right, whether it should have been kept, or whether its other
facets hold.

**You may emit only `deterministic-orchestration-v2`.** Everything else is unreachable by construction.
In particular, **do not emit `deterministic-orchestration`** (the unsuffixed original): it is a frozen,
already-measured tag, and emitting it is a validation failure.

**Default to silence.** A slug you are unsure about is a slug you do not emit — flag it instead (§2).

---

## 1. INPUT

You receive the paper's **full text**. Read it before judging. This facet turns on *what advances the
state* of the contributed system — the abstract and the paper's own vocabulary ("orchestrator",
"pipeline", "agentic workflow") are systematically misleading. Read the method.

---

## 2. OUTPUT CONTRACT

Return **exactly one JSON object**, no prose around it:

```json
{
  "themes":  [],
  "facets":  ["deterministic-orchestration-v2"],
  "rationales": { "deterministic-orchestration-v2": "form (a|b|c) — which clause fired, and the evidence" },
  "flags":   [ { "slug": "deterministic-orchestration-v2", "issue": "why this is a boundary case" } ]
}
```

- `themes` is **always empty**. `facets` is `[]` or `["deterministic-orchestration-v2"]`.
- **A rationale is required if you emit**, and it **must name the form**: `form (a)`, `form (b)`,
  `form (c)`, or a combination. No rationale, or no form named = discarded.
- **Empty output is a valid and common result.** Most papers will not fire.
- **No primary, no disposition.** Never propose either.
- **`flags` has TWO uses. Both are wanted.**
  1. **Undecidable** — the definition half-fits. Flag *instead of* guessing.
  2. **Census** — the two patterns in §4 the arbiter has asked to have **counted**. Flag them **even
     when the call is clear**; certainty is not a reason to omit the flag.

---

## 3. THE FACET

### `deterministic-orchestration-v2` *(facet — §151)*

**The question this answers:** *does **code**, not a model, control the outermost flow of the
contributed system — which steps run, in what order, and what their outcomes trigger — **with at least
one step performed by a model**?*

It is the arbiter's widening of `deterministic-orchestration` (§147b). The original asks whether code
**removes** discretion an AI agent would otherwise have. This version also covers systems where code
**withholds** that discretion by design: the code holds the process and **dispatches models only for
bounded tasks** — classify this, generate that, verify this — then routes their outputs itself. No model
ever gets to decide what happens next.

Keep it separate from **checking**: whether the *verdicts* inside the flow come from a model or from
deterministic code is a **different axis** (`rules-based-checks-v2`, not in this run). This facet is
about **who controls the process**, not **who checks**.

**Fires on any of three forms. YOUR RATIONALE MUST NAME WHICH.** The arbiter counts the split.
- **(a) Sequencing** — which steps run, and in what order, is fixed in code. **The model cannot skip a
  step**, because the harness advances the state.
- **(b) Enforcement** — the consequence of a step's outcome is fixed in code. A failing check produces
  rejection, escalation, a retry, **or an overridden verdict**, **without a model choosing to honour
  it**. Fires regardless of what produced the finding — a linter or an LLM.
- **(c) Dispatch** — top-level code **calls models as bounded workers** (one task per call) and itself
  decides what is called next and what each output triggers. The models are components, not
  controllers. *This is the form the original facet excluded.*

**PRECONDITIONS, ALL REQUIRED:**
1. **The orchestrator is NOT AI.** If a model decides the sequence, nothing is deterministic.
   > ⚠ ***"Orchestrator", "manager agent" and "planner" are standard LLM-app vocabulary and usually
   > denote an LLM.*** **Read what advances the state**, not the noun. An agent that *decides what to do
   > next* is the **inverse** of this facet.
2. **At least one step is performed by a model.** A deterministic pipeline with **no model in it at
   all** — CI with linters, a static analyser, a rule engine — does **not** fire: there is nothing to
   orchestrate *around*. (This replaces the original's "discretion actually being removed".)
3. **TOP LEVEL ONLY.** The control must sit at the **outermost** level of the contributed system's
   flow. Deterministic machinery **inside** a model-controlled loop does not fire — if a model decides
   whether the deterministic part runs at all, it can route around it.

> **Judge the CONTRIBUTED SYSTEM's architecture, not the paper's centre of gravity.** A paper that is
> mostly an empirical study can still contribute a pipeline whose top-level flow is code. Equally, a
> model the authors merely *evaluate* (the subject of a study) is not a step in a contributed system.

**Positives (settled under the original, and so also positives here):**
- **Vargas `GAD5Z8PV`** — *"a static orchestration model with three fixed phases"*; *"orchestrator with
  fixed prompts, which prevents early"* termination. Form (a); the verdicts are AI.
- **Lyu `UB2EVUFU`** — *"The orchestrator is the central coordination layer… managing phase transitions.
  The orchestrator does not make software engineering decisions itself"*: a three-phase state machine in
  code, while manager agents *"dynamically hire, assign"* the team. Phase sequencing is code-determined;
  staffing is model-determined. **Fires** — the facet asks about the **control flow**, not whether any
  model has discretion anywhere.
- **Jin `UDVHQ5HR`** — form (b) alone: the filter is *"applied only when the judge returns NO"*, the
  *"final verdict is determined by four common outcomes"*, and on two cases the code *"flip[s] the
  verdict to YES"* — code overturning a model's verdict on executable evidence, bounded K=2 retry.

**Form (c), described (no worked example given — read the paper):** a fixed code pipeline whose stages
each call a model for one bounded job, with code — thresholds, routing rules, a state machine — deciding
which stage runs next and what a stage's output causes (block, escalate, retry, approve). Or a code loop
that calls a model to generate an artifact, runs it, and feeds the code's own verification result back
to the model for repair.

**Negatives:**
- An **LLM planner / manager agent** deciding what to do next (the inverse).
- An **agent that chooses** to run a linter or a test — the model decides whether the step happens.
- A **deterministic pipeline with no model in it** (precondition 2).
- A system where the models are only the **subjects being evaluated**, not steps the authors' system
  dispatches.

---

## 4. TWO CENSUS PATTERNS — FLAG, DO NOT EMIT

The arbiter has two related questions **open** (F2 review questions 6 and 8). Until they are ruled,
**do not emit** in these cases — **flag them, even when the pattern is clear**, so they can be counted:

1. **Unbuilt design.** The paper's own system is **proposed or specified but not built or run** — a
   vision paper, a reference architecture, a framework with no implementation. *Flag: "unbuilt design"
   + which form it would be.*
2. **Human-driven outer loop.** Code enforces a gate or sequence, but the **outermost** progression is
   advanced by a **human** (clicking "approve", driving phases manually) — or the agent itself invokes
   the code gate as a tool it could decline to call. *Flag: "human outer loop" or "agent-invoked gate"
   + which form the inner part is.*
