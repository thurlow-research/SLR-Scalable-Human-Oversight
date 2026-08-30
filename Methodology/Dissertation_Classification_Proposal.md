# Dissertation classification — first cut on the 24 unplaced Phase 6 papers

**Drafted 2026-08-29. PROPOSAL ONLY — nothing written to Zotero.** Arbiter asked for "a cut at
classifying dissertations" plus a check on whether Phase 6 holds anything worth adding.

## Current state

Phase 6 - Kept Core holds **72** papers. Dissertation placement today:

| Collection | n |
|---|---|
| `01 - Primary` | 36 |
| `03 - Queue` | 12 |
| `02 - Supporting` | 9 |
| `04 - Validation Apparatus` | 6 |
| **in no dissertation collection** | **24** |

(Sum exceeds 72 because 15 papers sit in more than one.)

## The classification test used

Placement is proposed against the four research questions in the TECH-646 problem statement, since
that is what the collections have to serve:

- **RQ1** — how oversight is enacted: by whom, at what point, what division of labour
- **RQ2** — how scarce review attention is allocated as volume grows
- **RQ3** — how oversight is evidenced, audited, made demonstrable
- **RQ4** — how practice differs across big tech / small firms / regulated industries

**Primary** = carries an argument or supplies load-bearing evidence for an RQ.
**Supporting** = corroborates or contextualises without carrying an argument.
**Queue** = plausible but needs a closer read before placing.

## Proposed — `01 - Primary` (9)

| Key | Author | Why | RQ |
|---|---|---|---|
| `R9CDT9KB` | Mahmud | Trust-calibrated routing pipeline with real CVE/NVD evaluation — the corpus's clearest *allocation* mechanism | **RQ2** |
| `5VTAJISY` | Takerngsaksiri | **`adopted`** — HULA deployed inside Atlassian. Adoption is scarce and high-signal; this is enacted practice in a real firm | **RQ1** |
| `UW2R6BBJ` | Sudarsan | Secure AI-SDLC for **critical infrastructure**; evidence artifacts (SBOM, audit logs, threat model) + field study | **RQ3, RQ4** |
| `2KPHQ5IV` | Wang | Governance framework for scaling human-AI collaboration; provenance-auditability primary | **RQ3** |
| `SHK6KAX6` | Ghammam | The asymptote — oversight theatre observed in the wild | **RQ2** |
| `Z8TPRNEU` | Huang | *Professional Developers Don't Vibe, They Control* — field study + self-report of actual practitioner behaviour | **RQ1** |
| `B644HQFS` | Baltes | Tragedy of the commons: individual gains externalise review cost onto maintainers. States the inversion argument cleanly | **RQ2** |
| `F2C2DWSI` | Xu | *AI-Assisted Programming Decreases Productivity* — **counter-evidence**, and an honest proposal needs it | premise |
| `E95T8E88` | Watanabe | Predicting unnecessary methods in AI code; mining + metrics, inversion-adjacent | **RQ2** |

## Proposed — `02 - Supporting` (10)

`YBHHYR4P` **Perry** — foundational premise evidence (users write more insecure code with AI assistants);
controlled experiment. *Arguably Primary as a premise anchor alongside Fu — arbiter's call.*
`T2EG4BE2` **Waseem** — vibe coding in practice, technical debt, mining.
`ZUM76CCG` **Otten** — org-governance, general-AI; the §32 altitude precedent.
`6DXZGHD9` **Al-Hashimi** — the level-1 AI-oversight maturity finding is genuinely on-thesis, **but cite the
process-area scores, never the authors' conclusion** (§ note `MQRSB6GB`: three internal inconsistencies).
`F9JM9CI6` **Heander** — *Support, not automation*; design-only, oversight-explanation.
`VG6CIDQW` **Lumen** — transparent context control; built-system. ⚠ **missing author metadata.**
`X7EN6DXZ` **Mitropoulos** — contextual bias in LLM supply chain; experiment.
`T8E8SCCG` **Xie** — VibeGuard security gate; a `rules-based-checks` exemplar.
`72W6R4JG` **Töpfer** — FCL constraint verifier; the other `rules-based-checks` exemplar.
`JCTP8VXP` **Ma** — ZORO active rules; built + experiment + field study.

## Proposed — `03 - Queue` (5)

`7V7SRG43` **Tang** — CodeAgent; multi-agent, needs reading against the new `agent-panel` / `peer-critique`
split before placing.
`5DI9B43K` **Sistla** · `6ZW9QNQH` **Mitchell** — formal methods; relevant to deterministic checking but
niche relative to the RQs.
`VFNJSZD9` **Hjazeen** — unified security testing framework; design-only.
`R4WJZBSF` — regulatory/ethical quantification framework. ⚠ **missing author metadata.**

## The finding worth acting on — RQ4 is thin

**Only three Phase 6 papers carry `regulatory-compliance` as primary** (Sudarsan, Swidey, `R4WJZBSF`), and
one of those is design-only with no author metadata. RQ4 asks how practice differs in **regulated
industries** — finance, healthcare, aerospace/defence — and the corpus barely speaks to it.

That is a **gap claim in the proposal's favour** (nobody has studied it, which is why fieldwork is
needed), but it is also a **risk for the literature review**: a chapter cannot compare strata it has no
sources for. **Recommend making regulated-industry oversight an explicit target of the F5 supplementary
search**, rather than discovering the hole while drafting.

## Two metadata defects found while classifying

- `VG6CIDQW` (*Lumen*) — **no author metadata**
- `R4WJZBSF` (*A framework for quantifying ethical and regulatory…*) — **no author metadata**

Both are in Phase 6 and would break citation export. Fix before any bibliography is generated.

## What I did not do

No placements were written. Confidence is **moderate**: this cut is built on primary theme, signal
facets (`adopted`, `built-system`, `method-field-study`, `design-only`), and prior session reading —
**not** a fresh full-text read of all 24. The `03 - Queue` five are the ones I would not place without
reading.
