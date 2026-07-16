# Theme-tagging cheat-sheet — v0 (ORIGINAL, pre-calibration)

> **This is the *original* taxonomy** used for the first Set A model run — *before* the calibration
> iterations. It is preserved for the course assignment to show the starting point that produced the
> cross-model disparities we then diagnosed and fixed. **Not the operative version** (see
> `Tag_Cheatsheet.md` / `Methodology/Emerging_Themes.md` for current). 16 themes + 4 facets; original
> loose definitions; no `formal-methods`, no artifact/scope facets, `governance-frameworks` not yet
> renamed, `risk-routing`/`hitl-workflow`/`remediation-gating` boundaries not yet sharpened, no primary
> tie-breaker.

Tag on the **document contents**. **Multi-tag freely** — a paper can carry several themes.
Tag on **membership** (the paper *contributes to* that theme's argument), **not mention**.
Pick **one PRIMARY theme** (the paper's home / where it'd be written up in depth).

## THEME TAGS (`theme:<slug>`)

**Problem — quantify**
- `oversight-scaling-inversion` — AI code is riskier yet *less* inspected; PRs auto-merged unreviewed; review is the bottleneck; burden piles on maintainers
- `ai-code-insecurity` — empirical **security**-vulnerability evidence in AI code (CWEs, insecure-but-confident)
- `quality-debt` — **non-security** quality decay: tech debt, complexity, smells, maintainability, breaking changes

**Limits of current oversight**
- `automation-bias` — the *human* fails: over-trust, complacency, skill erosion, misses flaws even when warned
- `oversight-theater` — review exists on paper but lacks authority/time/info to change the outcome (rubber-stamp, token HITL)

**Solution — the Detect → Triage → Fix → Escalate pipeline**
- `ai-review` — [DETECT] AI *judges* the artifact (probabilistic, can hallucinate); incl. multi-agent / cross-model review **and its reliability limits**
- `rules-based-checks` — [DETECT] deterministic **grounded** checks: tests, static analysis/lint, formal methods, symbolic exec, sandbox
- `risk-routing` — [TRIAGE] score / prioritize / route / tier: *which* items get human attention & *how much*; escalation logic
- `remediation-gating` — [FIX] oversight of autonomous **fixes** (gate / filter / escalate the fix) — not the repair technique itself
- `hitl-workflow` — [ESCALATE] the human's **control surface**: checkpoints, action guards, approval gates, bounded delegation
- `oversight-explanation` — [ESCALATE] make the handoff **comprehensible/actionable**: background + options + recommendation + risks
- `agent-scope-drift` — [cross-cutting] agents wander off-mandate / make unreviewed decisions; keeping them in scope

**Governance & policy**
- `governance-frameworks` — *internal* org governance: maturity models, policy engines, policy-as-code, responsible-adoption
- `regulatory-compliance` — *external* law/standards: EU AI Act Art.14, NIST AI RMF, ISO 42001, liability, audit evidence

**Supply chain & provenance**
- `tooling-supply-chain` — provenance/vetting of the AI **tools** (skills/MCP/agents); **+ attacks on the reviewer**
- `provenance-auditability` — traceability of AI **changes** so a human *can* review; auditable record; IP/licensing

## FACET TAGS (functional role; orthogonal — optional, apply if they fit)
- `problem-statement-anchor` — a single committee-sit-up empirical stat
- `survey-input` — adoption / preference / RAI-priority finding useful for the org survey design
- `intro-framing` — position / agenda / definitional paper that *names the gap*
- `lit-review` — secondary literature (survey / review / meta-analysis)
