# Problem-Statement Evidence — Anchor Stats & the Oversight-Scaling Inversion

**Vibe Coding Governance SLR · dissertation problem-statement source document**
**Started:** 2026-07-13 · Grows as core evidence lands during triage/extraction

Purpose: a durable home for the empirical anchors that make the case for the review's
central problem, plus the synthesis that ties them together. Feeds the dissertation
problem statement and the framing of the organizational survey. Each entry names the
Zotero item key so it is traceable back to source.

---

## 1. The through-line: the oversight-scaling *inversion*

In normal engineering, riskier artifacts draw **more** scrutiny (defense-in-depth). For
AI-generated code the curves **cross**: the code is empirically *riskier* yet *less*
inspected. **Risk ↑, inspection ↓.** That divergence is not a minor inefficiency — it *is*
the oversight-scaling crisis this review documents, and it is the empirical spine of the
"quantify the problem → insufficiency layer" core (see §3 of `SLR_Status_Update_2026-07-08.md`).

## 2. Anchor stat — `59KP8GTP` (On Autopilot? Human-AI Teaming & Review Practices in OSS)

> **~80% of AI-co-authored PRs from non-owner contributors are merged with *no explicit
> review*; AI PRs merge significantly faster with the least feedback; most repos have *no
> guidelines* for AI-coding-agent usage.**

The candidate "make a committee sit up" number. It measures oversight **by its absence** —
the gating act, missing — which is why it is core rather than an adoption study.

**Governance vacuum, not attention lapse.** The un-reviewed code comes from *non-owners*
(least project context, historically the *most*-reviewed class), merges faster, gets minimal
feedback, and lands in repos without AI-usage guidelines. This is an organizational-governance
failure — precisely the level the dissertation's organizational survey operates at.

## 3. The causal chain (the core cluster is one mechanism seen at four points)

The inspection gap in `59KP8GTP` is the **cause**; the other cores measure its downstream
consequences. They are not four separate findings.

| Item | Finding | Role in the chain |
|---|---|---|
| **`59KP8GTP`** | ~80% of AI PRs merged un-reviewed | **the gate is open** (cause) |
| **`9H6FWJME`** | 22.7% of AI-introduced issues survive to HEAD | issues **persist** because nobody gates them (consequence) |
| **`F2C2DWSI`** | core devs review 6.5% more, own productivity −19% | **who absorbs** the burden when review *does* happen |
| **`REZGA5WF`** | causal ↑ in static-analysis warnings & complexity, persistent | the **quality tax** that accumulates |

Persistence (`9H6FWJME`) is the same problem as un-review (`59KP8GTP`), seen at the other end
of the pipe: issues survive *because* the gate is open.

**Implication for HOS.** If human review has empirically collapsed at this volume, "review
more carefully" is a non-answer. That is the justification for the reviewer-agent-escalates-to-
human pattern — automated inspection that routes only the risk-bearing cases to scarce human
judgment. The insufficiency layer, made concrete: oversight isn't *imperfect*, it's being
**skipped where it's needed most**.

## 4. Scope discriminator — oversight vs. steering (definitional)

Emerged while triaging `CKKGWMRH` (kept as *context*). **Oversight = inspection-and-gating of
the produced artifact on quality/risk grounds, with the ability to reject or escalate.** It is
*not* generation-steering: the conversational co-creation loop of vibe coding
(prompt → output → re-prompt, "did you mean X or Y?") is the human as **author/director**
shaping *what gets generated*, before there is an artifact to judge. High conversational
*interaction* ≠ high *oversight*.

**Triage consequence:** a paper is not core merely because it involves "human-in-the-loop"
interaction; it must engage the **gating act** (review/escalation/risk-triage of produced code).
This is consistent with the calls on record — `59KP8GTP` core (measures the gating act, by its
absence); `CKKGWMRH` context (characterizes interaction paradigms, not gating).

---

## 5. Additional anchors & measurement-validity caveats

**Anchors (tagged `problem-statement-anchor`):**
- **`3Z45M3V3`** — 29.5 % of Python / 24.2 % of JavaScript Copilot snippets in real GitHub
  projects carry security weaknesses (43 CWE categories, 8 in the 2023 CWE Top-25). Direct
  real-repo security measurement — a security-specific companion to `59KP8GTP`.

**Measurement-validity caveats (cite carefully — a wrong number invalidates a methods section):**
- **The "AI code ~1.7× buggier" premise** traces to a *single* source (Loker/CodeRabbit 2025,
  470 PRs, AI-*co-authored* ≠ autonomous, one platform). Scope the claim precisely.
- **SonarQube ground-truth threat** (`J4RVWCM2`): SonarQube's Maintainability Rating generates
  many false positives, and studies that used it for maintainability/technical-debt ground truth
  inherit a validity threat (CodeScene/Code Health is the more accurate metric). Flag when citing
  any static-analysis-based measurement — check `9H6FWJME` and the debt/maintainability items for
  exposure before leaning on their numbers.

---

*Zotero cross-refs: `59KP8GTP` carries a child note (the anchor-stat framing) and the tag
`problem-statement-anchor`. Add future anchors here with their item key + the tag.*
