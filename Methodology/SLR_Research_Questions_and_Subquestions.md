# SLR Research Question & Sub-Questions (provisional skeleton)

**Vibe Coding Governance SLR** · **Date:** 2026-07-10 · Methods-chapter input
**Status:** structural decisions **locked**; substantive wording/emphasis to be
finalized at the coding→synthesis bridge on stable frequencies (see §Timing).

---

## Overarching RQ

> How do organizations **practice and scale human oversight of AI-generated code**
> so that oversight keeps pace with the *volume* of AI-produced code **without
> sacrificing quality** — including the governance/policy landscape and the
> strengths and limitations of current oversight practices?

## Sub-questions (mapped to the emergent codebook)

| SQ | Question | Codebook axes | Layer |
|---|---|---|---|
| **SQ1** | What is the **nature and magnitude** of the oversight gap AI-generated code creates? | P1 scale + risk types (P2–P8) + `magnitude_evidence` | Problem |
| **SQ2** | **How and why is current oversight insufficient** to close that gap? | insufficiency layer + `F5` insufficiency-mode | Problem |
| **SQ3** | **What** oversight mechanisms/designs exist? | S1–S8 taxonomy + `F7` architecture | Solution — *what* |
| **SQ4** | **How is oversight enacted in practice** (process, who, when, division of labor, operational form)? | `F1` locus, `F2` human-role, `oversight_actor`, `solution_maturity`, `intervention_mode` | Solution — *how* (survey-mirroring) |
| **SQ5** | **How does oversight scale with volume** without sacrificing quality? | S2 risk-routing, attention allocation | Solution — *how it scales* (RQ crux) |
| **SQ6** | **How is oversight governed, audited, and evidenced?** (accountability & compliance) | `F4` governance_refs + S7 provenance/audit/attestation + how-facets + `third-party-demonstrable` | Assurance |

## Conceptual structure

- **Problem framing** — SQ1 (magnitude) + SQ2 (insufficiency).
- **First-order oversight** — SQ3 (what) → SQ4 (how practiced) → SQ5 (how it
  scales). Mechanisms that *catch or prevent* defects.
- **Second-order oversight / assurance** — SQ6. Mechanisms that *record and
  demonstrate that oversight occurred*, enabling audit, accountability, and
  compliance. (Governance frameworks demand auditability; audit/evidence
  practices provide it — two sides of one coin.)

*What exists → how it's practiced → how it scales → how it's assured.* SQ4 is the
general anatomy of practice; SQ5 is its sharpest, most-RQ-central slice
(throughput); keeping SQ5 distinct protects the "keep pace with volume" crux.

## Design decisions locked this session (2026-07-10)

- **SQ3/SQ4/SQ5 split** — separate *what exists* (SQ3) from *how it's enacted*
  (SQ4) from *how it scales* (SQ5). SQ4 is the most direct SLR→survey bridge.
- **SQ6 broadened** — from "governance landscape" to the full accountability layer
  (govern + audit + evidence).
- **Field additions** (fold into the extraction instrument):
  - `intervention_mode` (per instance): blocking-gate · advisory · sampling/spot-check
    · continuous-monitoring · escalation-only — the operational form for SQ4.
  - `third-party-demonstrable` (per assurance instance, boolean) — verifiability
    of the evidence for SQ6.
  - **Evidence *integrity* / immutability** (blockchain, signed/append-only,
    notarization) is handled **emergently** — surfaced by S7 frequency, promoted to
    a facet only if common; otherwise a supporting-actor mention. *No pre-built field.*

## Timing & methodological guardrail

- **When to finalize:** the bottom-up RQ→SQ refinement is the **bridge step after
  the full 114 extraction + QA** (stable theme/facet frequencies tell you which SQs
  the evidence can actually support), and **before synthesis writing**. This
  skeleton is provisional and doubles now as a **field-coverage check** (every SQ
  maps to captured fields).
- **HARKing guardrail:** refine the *questions* bottom-up from corpus structure
  (descriptive/structural = legitimate); do **not** write *findings-claims* into the
  SQs before synthesis. Document the refinement transparently as an emergent step,
  consistent with the earlier two-part scope narrowing.
- **What we already see shaping emphasis:** corpus is solution-heavy (90/114 both)
  → problem SQs lighter (framing); thin effectiveness/human-subjects evidence → SQ5
  effectiveness will honestly report an *immature evidence base*, which is itself the
  finding that **justifies the organizational survey**.
