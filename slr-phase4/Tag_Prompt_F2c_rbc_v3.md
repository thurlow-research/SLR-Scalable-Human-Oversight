# Tagging instrument — F2c: `rules-based-checks-v3` only

**Instrument of record for the F2c run** (`Taxonomy_Changelog.md` §156). Do not use this for general
tagging — it is deliberately partial: **one theme**.

**Population:** the 72 papers in `Phase 6 - Kept Core` (`R9ZHDXMN`). All have full text.
**Panel:** 3 vendors (opus, codex, gemini), one run each — the F2 configuration.

---

## 0. WHAT THIS RUN IS, AND WHAT IT MUST NOT DO

You are applying **one new theme**, `rules-based-checks-v3`, to a corpus whose **existing tags are
already settled by a human arbiter**. Those tags are **not under review**.

**You may emit only `rules-based-checks-v3`.** Emitting `rules-based-checks` or `rules-based-checks-v2`
(the frozen earlier versions) is a validation failure.

**Default to silence.** A slug you are unsure about is a slug you do not emit — flag it instead (§2).

---

## 1. INPUT

You receive the paper's **full text**. Read the method, not the abstract. Component **names** are
systematically misleading here ("RuleChecker", "Verifier", "Guard" are often LLMs) — ask what actually
**computes the verdict**.

---

## 2. OUTPUT CONTRACT

Return **exactly one JSON object**, no prose around it:

```json
{
  "themes":  ["rules-based-checks-v3"],
  "facets":  [],
  "rationales": { "rules-based-checks-v3": "which rule-checking tool, what rules, and what it validates" },
  "flags":   [ { "slug": "rules-based-checks-v3", "issue": "..." } ]
}
```

- `facets` is **always empty**. `themes` is `[]` or `["rules-based-checks-v3"]`.
- **A rationale is required if you emit**: name the tool or mechanism, the kind of rules, and what it
  validates. No rationale = discarded.
- **Empty output is a valid and common result.**
- **No primary, no disposition.**
- **`flags` has TWO uses. Both are wanted.**
  1. **Undecidable** — the definition half-fits. Flag *instead of* guessing.
  2. **Census** — the test-authorship pattern in §4. Flag it **whenever you meet it, even when the
     call is clear and even when you also emit the theme.** Certainty is not a reason to omit the flag.

---

## 3. THE THEME

### `rules-based-checks-v3` *(theme — §156)*

**The question this answers:** *is code validated against **rules** by a **deterministic, non-AI
evaluator**?*

The arbiter's intent is **diversity of validation**: knowing which systems check code with
deterministic rule-based analysis **alongside** (or instead of) AI evaluation. It is **orthogonal** to
AI checking — a system that also uses an LLM reviewer still fires if rule-based analysis is part of its
validation.

**Fires on:** static analysers · linters · security scanners (SAST, dependency/SCA, secret, licence
scanners) · type checkers · formal verifiers and model checkers · policy or constraint **rule engines**
— including runtime monitors that check execution against **general rules or properties**.

**THE BOUNDARY — RULES vs EXAMPLES. TESTS ARE EXCLUDED.**
- A **rules-based check** tests code against **general properties or policies** that hold across all
  inputs or all code: *"no empty exception handlers"*, *"no hard-coded secrets"*, *"dependency has no
  known CVE"*, *"this temporal property eventually holds on every run"*. Checking a **runtime trace**
  against a general temporal or constraint rule is a rules-based check, even though it is dynamic.
- A **test** checks behaviour on **specific examples**: unit tests, acceptance tests, BDD scenarios,
  integration tests, property-based tests' individual cases, benchmark test suites. **Tests do NOT
  fire this theme — whoever wrote them, human or model, and however deterministic their pass/fail.**
  (This is a deliberate exclusion, not an oversight; test-based validation is being counted separately
  — see §4.)

**THREE MORE CONDITIONS, ALL REQUIRED:**
1. **The verdict is computed by code, not judged by a model.** ***"Rubrics that are LLM evaluated are
   not rules-based-checks"*** (§139a). Rule-*shaped* criteria scored by a model are AI review, however
   explicit or numbered the rules.
2. **Do not tag from a component's name.** Ask what computes the verdict.
3. **Use, not mere measurement (§104/§115).** The rule-based tool must validate code **within the
   paper's system or process**, or the paper must **measure the effect of using it**. A static
   analyser used only as the study's **measuring instrument** — to count defects in a mined corpus, or
   as the oracle that scores third-party models — does **not** fire.

**Also not this theme:** *deterministic orchestration* — fixed control flow sequencing the steps — is
not deterministic *checking*. Rigid control flow with an LLM judge at the end does not fire.

**Positives:** Parris `3SU9QZ6F` (AIRA — 15 parser-backed deterministic checks) · Xie `T8E8SCCG`
(VibeGuard — scanner findings turned into pass/fail by coded thresholds and hard-block rules) · Zhong
`96XE669R` (30 deterministic verifiers).

**Negatives:** Sollenberger `GCZQTNBD` (LLM judge) · Raghavendra `8VBH957K` (LLM-scored rubrics) ·
Sun `V4IRKSFI` — **both** stages are fine-tuned LLMs; *"RuleChecker"* is a **name**, not a mechanism.

---

## 4. CENSUS — TEST-BASED VALIDATION AND WHO WROTE THE TESTS

Whenever the paper's system or process validates code with **tests** (any kind — §3's exclusion), add
a `flags` entry, **whether or not you also emit the theme**:

```json
{ "slug": "rules-based-checks-v3",
  "issue": "TESTS: <kind of tests>; AUTHOR: <same-as-code | different-model | human | mixed | unclear> — <one-line evidence>" }
```

- **same-as-code** — the producer of the code (a model, or a human) also wrote the tests for it.
- **different-model** — a different model wrote the tests than wrote the code.
- **human** — humans wrote the tests; the code is model-generated.
- **mixed** — e.g. human reference tests plus model-generated augmented tests.
- **unclear** — the paper does not say.

This is data for a separate, future exercise. It does **not** affect whether the theme fires.
