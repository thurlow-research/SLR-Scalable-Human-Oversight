# Synthetic-Eval Check — Reading Guide

**Who this is for:** the arbiter (Scott), reviewing `Phase 5 - Reading / 05 - Synthetic-Eval
Check` in Zotero (21 items).
**Companions:** `Methodology/HOS_Seeded_Theme_Candidates.md` (the staged facet definition +
full tripwire evidence) · `Sweep_Reading_Guide.md` (the parent protocol this borrows from) ·
`Tag_Cheatsheet.md` (the instrument).

## 1. What this collection is

A staged, not-yet-live facet candidate: **`evaluated-synthetic`** (renamed 2026-08-22 from
`synthetic-evaluated`, purely for tag-menu sort adjacency with `evaluated-benchmark` — no
definitional change) — own system evaluated against **self-constructed, non-standardized
scenarios/workloads** (constructed tasks, mock data) rather than a standardized third-party
benchmark or a real deployment. It's a `built-system` evidence-strength rung, below
`evaluated-benchmark`:

```
self-tests (untagged) < evaluated-synthetic < evaluated-benchmark < method-field-study < adopted
```

**Why it exists:** motivated by HBR7QZ2C during Full Read review — the machine panel proposed
`method-experiment` for a paper whose "evaluation" was the authors running their own system over
three self-constructed workloads, outcomes scored by human reviewers post-hoc. Wrong per the
instrument's own world-or-tool test (results describe the tool, not the world). A scan of the
full sweep confirmed this isn't a one-off: **21 of 128 sweep papers** have `built-system` +
`method-experiment` co-proposed by at least one model, vs. **zero** such co-occurrence in the 20
human-verified calibration gold papers — a real, recurring machine-only confusion that only
resolves correctly on a full-text check.

**Not yet grafted into the live `Tag_Prompt.md`/`Tag_Cheatsheet.md` v2.13 instrument** (frozen
for gauge constancy — grafting it would make future panel runs v2.14 and break comparability
with everything already scored). Available now only as a `cal:human:facet:` override you can
type by hand, or via the Actions & Tags menu **after reimporting**
`slr-phase4/slr_human_tags_actions.yml` (it now includes `[SLR] facet:evaluated-synthetic`).

## 2. The 21 candidates, pre-triaged

An automated pass (grep + full-text read, not a model panel) already sorted these into three
buckets. **Nothing here is final — every call is marked "pending confirm" and needs your read.**

### A. Tagged `cal:human:facet:evaluated-synthetic` (6) — my read says yes
Each has a child note explaining why. Confirm or override same as any Light Read: silence
(`s5:read`, no change) = agree; use the menu to remove the facet if you disagree.

- **A6ZE2A26** — Vibe coding on trial (LLM juries): 0 participant/subject signal; committee
  evaluated against a coding benchmark, no recruited humans.
- **MFSZPSPU** — human-in-the-loop patch evaluation framework: 0 participant signal despite the
  title; patch-evaluation dataset/benchmark, not a live study.
- **VZ27QUPQ** — API misuse identification/mitigation: 0 participants; "survey" hits are all
  bibliography citations, not a conducted survey.
- **WBS9U5N7** — Cognitive camouflage (specification gaming): near-zero method signal beyond
  benchmark/dataset; self-run demo.
- **A5WDGC7J** — Are LLMs reliable code reviewers?: 1 stray participant mention, "survey" hits
  all bibliography citations.
- **96XE669R** — Vibe checker (human preference alignment): 0 recruited participants; "survey"
  hits reference the external Stack Overflow developer survey as motivation, not their own study.

### B. Left untagged — genuinely mixed signal, worth your read (6)
Don't guess from the title; these had signal pointing both ways in the automated pass.

- **C88VGWMI** — Constitutional spec-driven development (case-study heavy; could be a real or
  self-constructed case study)
- **T3XTXIXW** — CoTDeceptor (adversarial case-study demo; "realistic developer workflow" is
  ambiguous — self-run or real?)
- **I6FZ5GD2** — Illuminating LLM coding agents (partnered with five real ML scientists — leans
  genuine small-n field/expert study, probably *not* synthetic)
- **X7EN6DXZ** — Contextual bias in LLM-assisted security code review ("deployed... on
  production repositories" — leans real/field, probably *not* synthetic)
- **XRTVITVP** — Steering LLMs via scalable interactive oversight (mixed signal)
- **Y4TIF9KW** — Code prism (**already in your Full Read bucket for full adjudication — don't
  let this collection preempt that; the full-read treatment supersedes this note**)

### C. Left untagged — resolved genuine on a closer read (9)
No action needed unless you disagree. Includes two that a first-pass keyword count would have
mis-flagged, corrected only by reading actual quoted context — same catch pattern as the
risk-bias/HBR7QZ2C QA earlier:

- **NRVQT89E** — LLM Critics Help Catch LLM Bugs (OpenAI CriticGPT): real contractors doing
  tampering/review tasks ("we asked contractors to introduce subtle bugs... we asked humans to
  review the completion") — genuine `method-experiment`.
- **7SH86C2W** — Shift-up framework: real stakeholder interview + build case study — genuine.
- 7UB2MD8Z, CI93QRUH, JCTP8VXP, U9VZQXGI, XK3P9C96, ZBF86IJM, ZH6QIU8A — all have heavy,
  unambiguous recruited-participant signal (30+ mentions each in most cases); real human-subject
  studies.

## 3. What to check per paper

Same world-or-tool test as the instrument itself: does the evaluation describe **the world**
(real users, real deployment, real behavior) or only **the tool** (self-run tests, constructed
scenarios, synthetic/mock workloads)? Specifically:

- Are there recruited human subjects performing assigned tasks under some condition, or is
  "evaluation" just the authors' own system run against a dataset/benchmark/synthetic workload?
- Is a "case study" a real deployment/real codebase, or a scenario the authors constructed to
  demonstrate their own system?
- Do "survey"/"interview"/"participants" hits refer to something the authors actually did, or
  are they bibliography citations / references to someone else's study (e.g., the Stack Overflow
  developer survey)?

## 4. Recording results

Same mechanics as the sweep workbook (`Sweep_Reading_Guide.md` §1): `s5:read` when done, use the
`cal:human:*` menu to override. For this collection specifically:

- **Agree with a tag** (bucket A): `s5:read`, no change.
- **Disagree with a tag** (bucket A): remove `cal:human:facet:evaluated-synthetic` via the menu,
  `s5:read`.
- **Bucket B calls**: add the facet if you agree it's synthetic; leave it off and `s5:read` if
  not. A one-line note either way helps the promotion decision below.
- **Bucket C**: no action expected; flag if you actually disagree with the "genuine" read.

## 5. Promotion decision (after your read)

If the pattern holds up — a meaningful cluster of papers where the true evaluation is
self-constructed/synthetic and the current instrument can't distinguish that from a real
`method-experiment` — the next step is deciding whether to graft `evaluated-synthetic` into a
new instrument version (v2.14) for future panel runs, vs. keeping it a human-only override tag
indefinitely. That's a separate decision from this read-through; this collection just gathers the
evidence.
