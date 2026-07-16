# SLR Pipeline / Corpus — Status Update

**Vibe Coding Governance Systematic Literature Review**
**Date:** 2026-07-01
**Baseline:** `SLR_CONTEXT.md` (2026-06-28) — the canonical bootstrap; this is the thin delta on top.
**Purpose:** Bring the SLR state current ahead of switching to Claude Code.
**Corrected 2026-07-01 (Claude Code, live Zotero item traces):** two items this note carried forward from June 28 as "pending" — Phase 2 apply and the seven AI House queries — are actually **done**. See the Resolved section. The counts table was already accurate.

---

## Headline

Corpus is effectively stable since the June 28 snapshot. One item moved into Phase 2 Keep (923 → 924); nothing else changed. No new queries executed, no drafts written. The open queue from June 28 carries forward intact.

---

## Verified current state (live from Zotero, 2026-07-01)

| Collection | Key | Count | Δ since 06-28 |
|---|---|---|---|
| Phase 2 Keep | `3D8XR6AP` | 924 | **+1** |
| Phase 2 Maybe→Keep | `ZB6R4G9H` | 59 | 0 |
| **Total eligible corpus** | — | **983** | **+1** |
| LinkedIn Post 01 | `JHJN4DKW` | 5 | 0 |
| Phase 2 queue | — | 0 (complete) | 0 |

*Counts pulled from the Zotero group library (ID 6505702) via authoritative `Total-Results` headers, not page-length inference.*

---

## What changed since the last update

- **Phase 2 Keep +1 (923 → 924).** A newly published Hancheng Cao article, relevant to the review, pulled in via the **committee** source stream. Separate from `apply_phase2.py` — and that apply's end state is now confirmed complete (see Resolved).
- Everything else in the June 28 snapshot still holds as the current state.

---

## Pipeline status recap (carried forward, unchanged)

- **Pass 2 screening:** complete. 4,061 Pass-1 K+M → 973 Keep / 73 Maybe / 2,908 Discard (73% Pass-2 rejection by design).
- **Pass 2 Trust Check:** applied. 60-item stratified sample, Po = 86.2%, Cohen's κ = 0.79 ("substantial"); zero false negatives in discards.
- **Pass 1 restoration:** completed 2026-06-07 (`applied = 2890`, `apply_errors = 0`).
- **PDF coverage:** ~26% of Phase 2 Keep have attached PDFs. Root causes unchanged: SSRN (~381 items, 0%, session-gated) and IEEE Xplore (~188 items, ~7%, subscription-gated).

---

## Resolved (live-verified via Zotero item traces, 2026-07-01)

Both carried forward from June 28 as "pending"; the live library shows them **done**:

- ✅ **Phase 2 collection population — COMPLETE.** `00-Queue` = 0 across all 10 sources; Phase 2 branches populated (Phase-1-Keep 924/11/1025, Phase-1-Maybe 59/75/1900) and reconcile with the source-level in-scope total (3,994 ≈ 4,003 − superseded). The script-run *log* was never captured (hence the prior "unconfirmed"), but the end state is complete.
- ✅ **Seven AI House queries — FETCHED + SCREENED** (Q-IEX-23/24, Q-ACM-07/08, Q-SCO-06/07, Q-arXiv-06). Item traces show `s1:*` + `s2:*` tags and correct Phase 2 bucket membership; single-source items (e.g. `8GRSSX8L`, in *only* Q-ACM-08 → `s2:human:discard` + Phase 2) prove the queries ran through both passes. They contributed ≈nothing to Keep under the tight Pass-2 rubric.

## Open / pending

1. **Weed 983 → two-tier corpus (strategy agreed 2026-07-01).** Stage 3: abstract-level relevance triage — Core / Context / Discard + 0–100 centrality score — via a 3-model ensemble (**Claude/Opus + ChatGPT Pro + Gemini Advanced**; script-based, results CSV imported). Stage 4: full-text fetch of Core candidates only (~100–150) → depth/quality screen → final ~100 for full extraction; Context tier extracted at abstract level (no fetch). Cross-model + human verification samples per pass (Trust Check gate + blinded N=100 κ). See `SLR_CONTEXT.md` §13.
2. **"Agentic SDLC" / "ADLC" back-fill cluster** — phrase-lock spelled-out forms; ADLC noisy alone.
3. **Deferred / contingent:** Google Scholar + terminology probes (Q-SSRN-10, Q-WoS-04, Q-GS-17) — contingent on SSRN coverage adequacy.
4. **SLR standalone paper draft** — post-corpus; RQ restructure per Thomas (governance as a separate top-level RQ, sub-RQs broadened/less leading).
5. **LinkedIn Post 01 draft** — five papers selected and fully read; draft not yet written.

---

## Known items to fix before next run

- **`cleanup_superseded_tags.py` date tiebreaker bug** — string comparison makes year-only dates ("2026") lose to year-month ("2026-02"). Fix: pad year-only to "YYYY-01" before comparing. Fix **before** next dedup run.
- **Repo org name ambiguity** — `ScottThurlow/` vs. `thurlow-research/`. Confirm canonical org at startup.

---

## Before any write

Export the Zotero library first (desktop: File → Export Library). Prompt before every `--apply`, even on idempotent scripts. Swap in the write key only for the authorized write, then swap back to read-only.

---

## Claude Code handoff note

`SLR_CONTEXT.md` (2026-06-28, updated 2026-07-01) remains the canonical bootstrap. Load that first; this file is the delta. Startup checklist: (1) Phase 2 apply end state confirmed complete 2026-07-01 — no re-verification needed; (2) confirm canonical repo org (`ScottThurlow/` vs `thurlow-research/`).
