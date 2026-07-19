# Critique-panel disposition table — 2026-07-18

Panel: fable (15 findings + full KA), codex/GPT-5 (16 findings + full KA), gemini 3.1 Pro (9
findings + KA in 3 chunks). Verdicts: gemini "nearly ready" · codex "not ready" · fable "close —
one targeted revision cycle, then sweep." Convergent prescription: **one revision cycle.**
Disposition legend: ADOPT (uncontroversial, apply) · ADAPT (apply with wording judgment) ·
**RULING** (arbiter decision required) · RECORD (boundary-disagreement / noted, no action) ·
ARTIFACT (defect of the critique packaging, not the instrument).

## A. Mechanical / schema (ADOPT)
| # | Finding | Critics |
|---|---|---|
| A1 | Task-block demote trigger list contradicts facet rules: `general-code` listed as demote trigger though it's a keep-core audit-trail flag (introduced in the F1 fix); `steering-only` missing from list | fable(high), codex(high) |
| A2 | `demote:context` criteria stated twice with different strictness ("any reason" workflow vs "ONLY if" task block) — unify | codex(high) |
| A3 | WORKFLOW's `cal:human:primary:theme:` typing instruction conflicts with task block's bare-slug JSON; mark Zotero-only; restrict `flags` to enumerated `demote:*` vocabulary | fable(low), codex(high) |
| A4 | Rationale schema: no rationale slot for primary-choice/flag justification | codex(low) |

## B. Compression-gap restorations (ADOPT — the principle is already ours)
| # | Missing from Part 1 | Critics |
|---|---|---|
| B1 | risk-routing: "computed, producer-independent signal; model self-confidence disqualified" | fable, codex (both high-value; the HOS rule!) |
| B2 | framework: point-tool exclusion + "focused single-concern qualifies" + adoption test (explains Set A's framework 1/4 split) | fable, codex, gemini |
| B3 | tooling-supply-chain: "+ poisoned/hallucinated dependencies" clause + keyword false-positive exclusions | fable, codex |
| B4 | Detect pair dual-tagging expectation on gray-zone systems ("LLM writes tests then runs them") | codex |
| B5 | formal-methods third composition: no performer → formal-methods + intro-framing | fable |
| B6 | intro-framing: "names the gap but doesn't operationalize a mechanism" qualifier | fable, codex |
| B7 | Tie-breaker: move the Hedwig worked exemplar into Part 1 | fable, gemini |

## C. Definitional sharpenings (ADAPT)
| # | Finding | Critics |
|---|---|---|
| C1 | oversight-explanation push/pull enumeration excludes *standing output explanations* (7UB2MD8Z, 22JBEZNK's actual object) — make headline govern, modes illustrative, add "system-provided explanations of AI output that support the human's verdict" | fable(high) |
| C2 | Documented-practice membership clause exists only on ai-review — generalize to all solution themes (Z8TPRNEU's hitl-workflow rests on it) | fable, codex |
| C3 | biggest-tent operationalized: "theme under which the largest share of synthesized evidence would be cited; ties → the review's own framing question" | fable, codex |
| C4 | provenance-auditability: record must be argued as serving *human* reviewability; persistence for agent coordination = plumbing | fable, codex |
| C5 | Input-floor rule: title+abstract-only → conservative tagging (no form facets / lit-review unless explicit) + insufficient-input flag instead of guessing | fable, codex |
| C6 | ai-code-insecurity evidence bar: incident analyses + original taxonomies count; secondhand rate citations alone don't | fable |
| C7 | Membership floor for vision papers: a stage mentioned in one scenario sentence = mention, not membership | codex, fable(KA) |
| C8 | survey-input inclusion threshold (one incidental stat?) | gemini, codex |
| C9 | Competence-gap keep-core note on automation-bias: paper remains core-eligible; missing theme ≠ struggle signal | fable |
| C10 | "tool benchmark" demote trigger defined: capability benchmarking with no mechanism/deployable contribution; benchmarks evaluating a contributed system ≠ demote | fable |

## D. Boundary RULINGS (arbiter only — genuinely new territory)
| # | Question | Critics |
|---|---|---|
| D1 | **Human gate over an AI-produced *plan* before execution: hitl-workflow or steering?** Fable proposes: plan = AI artifact under review → hitl-workflow; authoring/shaping prompts/specs/context yourself = steering; guidance channels consumed by the planner = steering unless the checkpoint design itself is the contribution. Live in dev set (Z8TPRNEU, UB2EVUFU) | fable(high), gemini(high) |
| D2 | **Execution-feedback loops** (test-failure output fed back to regenerate): steering, or the check side? Gemini's high-severity ambiguity | gemini(high) |
| D3 | **Remediation-gating when the human approves each fix** (human-approved auto-repair): does the human-approval loop count as the gate? | gemini(med) |
| D4 | Dependency risk **inside generated code**: tooling-supply-chain (poisoned deps clause) or ai-code-insecurity/detector themes? (T8E8SCCG precedent: human excluded t-s-c) | fable |

## E. Recorded / artifacts (no instrument action)
| # | Item | Class |
|---|---|---|
| E1 | Gemini boundary-disagreement on risk-routing/oversight-explanation vs generality | RECORD |
| E2 | 2CKL96B8 truncated abstract; "FULL TEXT" wording vs abstract-only papers; M74M3RFJ prose flag string | ARTIFACT (critique packaging) — but 2CKL96B8 should be dropped from known-answer fixtures or re-based on full text |
| E3 | Codex "namespace confusion" re general-ai placement under artifact cluster | ADAPT-lite (regroup scope flags together) |

## Known-answer synthesis (fable × codex × gemini)
Forced by current text: the big boundary calls (Lumen themes, VibeGuard exclusion+primary,
22JBEZNK not-bias + tie-rule, UB2EVUFU primary + process-gate, Z8TPRNEU ai-review, UDVHQ5HR
primary, M74M3RFJ primary+general-ai). NOT forced: facet-level and flag-level decisions almost
everywhere (framework, survey-input, demote triggers, mode on thin evidence) — divergence risk
concentrates in facets/flags, not themes. Matches the Set A observation that breadth, not
structure, is where noise lives.
