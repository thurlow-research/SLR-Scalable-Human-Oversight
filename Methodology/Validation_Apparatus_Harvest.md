# Validation apparatus in the wild — harvest

**Zotero collection:** `Dissertation Lit Review / 04 - Validation Apparatus` (`XPPEXKBN`).
Membership is **additive and orthogonal to SLR tier** — a Context paper can and often will belong here.

## What this is, and why it exists

A record of **how each paper validated AI-generated code** — what layers, in what order, where the human
sits, and what triggers escalation — harvested from **methods sections**, independent of what the paper
set out to argue.

**The claim it supports.** A methods section is evidence about **what its authors considered adequate
validation**. Nobody made them layer their checks; the layering is a *revealed belief* about where
machine checking runs out and a human becomes necessary. That is evidence about **norms**, and it is
available even in papers whose findings are irrelevant to this review.

## Why it is needed — tier assignment is itself risk routing

Arbiter, 2026-08-27: *"'what that loses' sounds a lot like risk routing."* Exactly so, and the parallel
is uncomfortable enough to state plainly:

> **Core/Context is a routing decision, and Context is our un-routed remainder.** §42 short-circuits tag
> verification on a demote, and downstream those papers get read as "nothing here" — which is precisely
> the failure staged as a tripwire from `ZBF86IJM` (§79): **the absence of a routing signal is
> interpreted as a clean bill of health.**

**This harvest is the mitigation for our own un-routed remainder.** It belongs in the methods chapter
next to the reflexivity note at §11.8, as a worked case of the review applying its own findings to
itself — and, unlike the §11.8 illustration, this one changed what we do.

## Scope — the 128, then decide

**Start with the Phase-5 128.** A hard constraint decides it: **full texts exist only for those**
(`slr-phase4/txt/`). The wider Context pool was screened on titles and abstracts, so harvesting from it
means fetching hundreds of PDFs first.

**Measure the yield, then choose.** If 128 papers give a thin or repetitive picture, expansion is not
worth the retrieval cost; if a real typology of validation layering emerges, that justifies the fetch.
Calibrate-then-scale, as with every other pass here.

**If expanding later, do NOT blanket-scan abstracts** — abstracts almost never describe validation
apparatus. Expand by **targeted retrieval** on abstracts mentioning validation, review, or evaluation
pipelines, then read methods sections.

## What to record per paper

| Field | Notes |
|---|---|
| Layers, in order | e.g. lexical → semantic → human |
| Automated components | what kind of check, and whether deployable or reference-grounded (§51) |
| AI-as-checker | present? same model as generator, or different vendor? (feeds `cross-model`) |
| **Human position** | where the human sits, and **what triggers** their involvement |
| Escalation trigger | threshold, disagreement, risk class, or none |
| Stated rationale | did they *argue* for the layering, or just use it? (decides §104 tier) |
| Domain | safety-critical, general, competitive-programming, etc. |

## Entries

### `VG8PSMM7` — Adnyana & Schwung (2026), *Benchmarking and validation of prompting techniques for AI-assisted industrial PLC programming* · **SLR: Context**
- **Layers:** BLEU (lexical similarity) → **LLM-in-the-Loop (LITL)** semantic check across four
  dimensions — functional correctness, readability, safety compliance, modularity → **Human-in-the-Loop
  (HITL)** expert review for safety-critical code.
- **AI-as-checker:** yes, and **cross-vendor** — DeepSeek and Gemini 2.5 Pro generate ST/IL; syntax is
  cross-checked by ChatGPT-4o and Copilot Pro. *Whether the separation is argued for or incidental is
  unresolved — flagged for the harvest, not for tagging.*
- **Human position:** terminal, and scoped to **safety-critical** review — the human is not asked to
  check everything, only what the domain marks as dangerous.
- **Domain:** industrial automation, IEC 61131-3, Siemens TIA Portal / Beckhoff TwinCAT.
- **Why it matters:** the team judged lexical similarity insufficient, added a semantic machine check,
  and **still would not let safety-critical code through without a human**. A three-rung ladder with the
  human at the top, chosen without anyone requiring it.

## Back-fill candidates from the Light Read band (at closeout)
`72W6R4JG` Töpfer (FCL constraint verifier + bounded repair loop) · `TA6GIUK2` Zietsman (BDD vs AI
review head-to-head) · `96XE669R` Zhong (VeriCode's 30 deterministic verifiers) · `VZ27QUPQ` Zhuo
(Dr.Fix detect-reason-fix; **reference-grounded — note the §51 disqualifier**) · `T2EG4BE2` Waseem
(three-layer testing discipline + CI gates).
