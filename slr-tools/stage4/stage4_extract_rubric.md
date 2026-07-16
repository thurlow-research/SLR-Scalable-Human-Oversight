# Stage 4 — Core Document Signal Extraction Rubric (v1)

**Vibe Coding Governance Systematic Literature Review**
**Instrument purpose:** capture structured, *descriptive* signals from the full
text of each Core document to support **bottom-up (emergent) codebook
derivation**. This step does **not** make any inclusion/exclusion or
classification decision — those come later, against the locked codebook, with a
human as the arbiter. Here the AI is a *consistency aid* that reads each document
once and records what is present; every field is subsequently human-reviewable
and traceable to the source text.

**Emergent-first stance:** do **not** force content into any pre-set theme list.
Describe mechanisms, risks, and constructs in the document's own terms. Themes
are clustered from these signals afterward, not imposed here.

---

## Task

You are given the full text of one primary research document from a systematic
literature review on **human oversight of AI-generated code** (how organizations
practice and scale oversight so it keeps pace with the volume of AI-produced code
without sacrificing quality — including the governance/policy landscape and the
strengths/limitations of current oversight practices).

Read the document and return **exactly one JSON object** with the fields below.
No prose, no markdown, no code fences — just the JSON object.

**Grounding rules**
- Every value must be supported by the document's own text. Do not infer beyond it.
- If a field does not apply, use `null` (scalars) or `[]` (lists). Never invent.
- For `magnitude_evidence` and `insufficiency_evidence`, quote the specific claim
  (a short verbatim phrase or paraphrase with the number/source), or `null`.
- Keep list items short (a few words each); they are clustering tokens.

---

## Schema

```json
{
  "item_key": "<echo the item_key given in the header>",
  "citation": "<echo the citation given in the header>",

  "evidence_type": ["<one or more of: empirical, controlled-experiment, benchmark, system-tool, conceptual-position, framework-model, case-study, secondary-review, dataset>"],

  "problem_statement": "<1-2 sentences: what oversight problem re: AI-generated code does this document address?>",
  "magnitude_evidence": "<verbatim/near-verbatim quantification of the problem's scale, prevalence, or volume (with the stat + who reported it), or null>",
  "risk_types": ["<open list of risk categories the doc names: e.g. security, quality, maintainability, legal, hallucination, specification-gaming, supply-chain, ...>"],
  "insufficiency_evidence": "<verbatim/near-verbatim evidence that current, automated, OR human oversight fails to close the gap (e.g. a tool's miss rate, a judge being fooled, review not scaling), or null>",

  "solution_mechanisms": ["<open list: each a short descriptor of an oversight mechanism/design the doc proposes, evaluates, or describes>"],
  "mechanism_keywords": ["<normalized short tags for clustering, free vocabulary: e.g. guardrail, security-gate, policy-as-code, adversarial-verification, llm-as-judge, risk-routing, escalation, hitl, observability, calibration, ensemble, decorrelation, spec-driven, provenance, ...>"],
  "oversight_locus": ["<where in the lifecycle oversight sits, open: generation-time, pre-commit, pre-publish, CI, runtime, code-review, post-deployment, ...>"],
  "human_role": "<how humans stay in the loop, open: in-the-loop | on-the-loop | in-command | escalation-target | none | unspecified>",

  "key_constructs": ["<novel named terms, frameworks, or taxonomies the doc introduces (e.g. 'cognitive camouflage', 'human-in-command', 'signal detection oversight')>"],
  "governance_refs": ["<regulatory / standards frameworks cited: e.g. EU AI Act, NIST AI RMF, ISO/IEC 42001, GDPR, ...>"],

  "scope_fit": "<one of: problem | solution | both | neither — which side of the two-part scope (quantify the problem / characterize the solution) this document primarily serves>",
  "notes": "<any caveat: garbled/truncated text, non-English, off-topic drift, or null>"
}
```

## Reminders
- Return only the JSON object.
- `both` is common and correct for papers that document an oversight failure *and*
  propose a mechanism — do not force a single side.
- A paper can have `human_role: none` (fully automated mechanism) and still be a
  core oversight-solution document; record what the text says.
