# Set B — Human Calibration Tagging Packet

**You tag these 10 first (blind).** Then I run Opus + codex + agy on the same 10 and we compare.
Read the **document contents** (each paper is in Zotero → **02-Human Calibration Run**, with PDF + TXT).

**How to record:** fill the template at the bottom (or tag in Zotero — your call). For each paper:
- **Primary** = the one home theme.
- **Themes** = all `theme:` slugs that fit (membership, not mention).
- **Facets** = any of the 4 facet tags that apply.
- (optional) a few words of *why* for the primary.

---

## Vocabulary cheat-sheet


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


---

## The 10 papers (Set B)

| # | Key | Title |
|---|---|---|
| 1 | `B644HQFS` | "An Endless Stream of AI Slop": How Developers Discuss AI-generated code |
| 2 | `6DXZGHD9` | A generative-AI cybersecurity risks mitigation model |
| 3 | `E95T8E88` | What to cut? Predicting unnecessary methods in agentic code |
| 4 | `7V7SRG43` | CodeAgent: autonomous communicative agents for code review |
| 5 | `UW2R6BBJ` | Secure AI-SDLC for critical infrastructure (NIST AI RMF) |
| 6 | `BAWCBT9R` | Bias in the loop: auditing LLM-as-a-judge for SE |
| 7 | `E3E5YA2E` | Redefining the programmer: human-AI collaboration |
| 8 | `5VTAJISY` | Human-in-the-loop software development agents (HULA) |
| 9 | `TF56EPIP` | Rethinking autonomy: preventing failures in AI-driven software |
| 10 | `R4WJZBSF` | A framework for quantifying ethical & regulatory risks |

---

## Fill-in template

```
1. B644HQFS  primary: __________   themes: __________________   facets: ________   why: ____
2. 6DXZGHD9  primary: __________   themes: __________________   facets: ________   why: ____
3. E95T8E88  primary: __________   themes: __________________   facets: ________   why: ____
4. 7V7SRG43  primary: __________   themes: __________________   facets: ________   why: ____
5. UW2R6BBJ  primary: __________   themes: __________________   facets: ________   why: ____
6. BAWCBT9R  primary: __________   themes: __________________   facets: ________   why: ____
7. E3E5YA2E  primary: __________   themes: __________________   facets: ________   why: ____
8. 5VTAJISY  primary: __________   themes: __________________   facets: ________   why: ____
9. TF56EPIP  primary: __________   themes: __________________   facets: ________   why: ____
10. R4WJZBSF primary: __________   themes: __________________   facets: ________   why: ____
```
