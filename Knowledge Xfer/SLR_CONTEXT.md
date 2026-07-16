# SLR Bootstrap Context — Vibe Coding Governance Systematic Literature Review

> **Purpose.** Drop this file into a Claude Code session (or reference it from `CLAUDE.md`) to
> bootstrap an assistant with the full state of the SLR. It captures the research framing, the
> methodology decisions made to date, the current pipeline state, the Zotero conventions, the
> tooling, and the open work. **Err toward verifying live state at session start** (see
> §16 Startup Verification) — counts and apply-status below reflect the *last known* state and
> may have advanced.
>
> *Generated 2026-06-27. Sources: project methodology doc, advisor RQ-brainstorm transcript
> (2026-05-01), `Query_Composition_and_Log.xlsx`, and accumulated project notes.*

---

## 1. Project at a glance

- **Researcher:** Scott Thurlow — doctoral candidate, **Engineering Management, Purdue University**; practitioner at **Microsoft**.
- **Topic:** How organizations recognize and manage the risk introduced by AI-generated code / "vibe coding," where code *volume* outpaces traditional governance (esp. manual code review). Central question: how do you make **human oversight scale with volume without sacrificing quality**?
- **The SLR is a standalone deliverable** — it both (a) satisfies the program's publication requirement (target venues: **ICSE SEIP, EASE, HICSS**) and (b) seeds the dissertation's literature review. It establishes the **gap claim** that the empirical phase (survey + interviews) then addresses.
- **Self-plagiarism guard:** the dissertation methods chapter *cites* the published SLR rather than reproducing it. Check Purdue manuscript-format policy + the venue's author-rights/copyright-transfer terms before submitting.

### Committee
| Member | Affiliation | Strengths / role |
|---|---|---|
| **Paul J. Thomas** (advisor) | Purdue | IT systems, project management, cybersecurity education |
| **Linda Naimi** | Purdue | Tech law, IP, ethics, GenAI legal/ethical implications (governance angle) |
| **Hancheng Cao** | Emory (Goizueta) | Computational social science, AI in software dev teams |
| **Kyubyung Kang** | Purdue | ML & AI governance in safety-critical domains |
| **David Pistrui** | Purdue | Organizational transformation, Industry 4.0 (survey-distribution help) |

> Note: do **not** confuse committee member *Linda Naimi* with corpus author *Markus Langer*.

---

## 2. Research questions (per advisor meeting, 2026-05-01)

Thomas's key steer: **governance/policy is a separate top-level RQ, not a sub-question** — it's policy-level, distinct from organizational implementation. Keep questions **broad, non-leading**, so quantitative + qualitative answers can *emerge* from the research rather than being baked in.

- **RQ-Primary (organizational practice):** *How are organizations practicing human oversight in their AI coding pipelines?* — the "how," the intellectual heart of the dissertation.
- **RQ-Sub (candidate):** *What are the strengths and limitations of current oversight practices?* (broad enough to surface both quant and qual findings; avoids loading the question with named solutions like "adversarial agents").
- **RQ-Governance (separate top-level):** policy/regulatory landscape — what industry standards, frameworks, and government regulations (NIST AI RMF, EU AI Act, CISA) say — as distinct from what organizations *actually do*. Ideally one informs the other; how much it does in practice is itself worth inquiry (and disclosure honesty is a known risk).
- **Cross-cutting themes:** human–AI teaming (as mechanism), auditability/audit trail, tooling/platform infrastructure, regulatory/framework landscape.
- **Adjacent-domain net:** keep non-domain-specific items that speak to *scalable human oversight in other AI-application domains* (broader net on the oversight construct, not just code).

**Empirical follow-on (not part of RQs, but part of methodology):** a broad **structured survey** (target ~50–100+ responses for demographic/high-level claims) + a **small set of semi-structured interviews** (5–6 rich, hour-long conversations is enough for depth). Three target segments: **(1) big tech, (2) startups** (rich Seattle AI-startup community), **(3) regulated/safety-critical enterprises** (Boeing, MSCI, SoFi, JPMorgan — aspirational; harder for institutional approval). IRB required (human subjects); survey can collect opt-in emails for interview follow-up; mask identifying org info. Incentives TBD (swag works; Prolific is a last-resort paid-panel option with acknowledged bias).

**Program timeline (tentative):** prelim proposal (Ch. 1–3 draft) end of fall semester → prelim oral defense ~**Feb 2027** → mandatory two-semester gap → **final defense late spring 2028**. Conference submission windows (e.g., IEEE *Frontiers in Education*) tend to be early-spring abstract + paper, which lines up well.

---

## 3. Scope & key constructs

- **"Vibe coding"** — coined term (Karpathy, Feb 2025); treat as an **exact phrase** in queries. Broader concepts ("AI code generation," "LLM code generation") are **not** phrase-locked.
- **Risk *recognition* vs. *mitigation*** — the under-served gap is empirical organizational work on *recognition* (how orgs know they have a problem *before* something goes wrong), not just mitigation.
- **Oversight scaling** — the core contribution frame: scaling AI oversight is largely **porting accumulated human-review coping mechanisms** (dedup ledgers, won't-fix authority, scoped audits, reviewer briefing, standing red-team cadence) to AI reviewers; automated detection routes code to human review **only when needed** rather than requiring exhaustive inspection.
- **Prompts-as-artifact** — prompt/conversation sessions as *reviewable upstream artifacts* (versioning, provenance, audit trail). Surfaced at AI House panel 2026-05-20; independently corroborated by a senior practitioner/CTO (anonymized in Zotero). Drives queries Q-SCO-07 / Q-IEX-24 / Q-ACM-08.
- **Known false-positive classes to exclude:** blockchain; educational/classroom scenarios (teaching with AI coding); LLM capability benchmarks with no organizational-governance link.

### Theoretical framing (state in methods so the coding scheme has a home)
- **Cleanroom statistical quality control** (Cobb & Mills 1990) — statistical QC over exhaustive inspection.
- **Lean manufacturing's *jidoka*** (Ohno) — automated detection that stops the line / escalates to a human only on a detected defect.
- **AI-triggered human oversight** — the synthesis of the two: route human attention by risk.
- Human-factors + org-risk lenses to anchor coding: automation bias, signal detection theory, Parasuraman levels of automation; ISO 31000 logic, NIST AI RMF. Gap connects to Sabatier's policy-process theory (governance) and Poppendieck/lean (engineering-management).

---

## 4. SLR methodology

### 4.1 Protocol / PRISMA 2020 multi-stream identification
Document identification as **parallel streams**, each reported separately:
- **Peer-reviewed databases:** IEEE Xplore, ACM, Scopus, Web of Science.
- **Preprint stream:** arXiv (cs.SE, cs.HC primary; SSRN/OSF/TechRxiv secondary) — screened with an **extra methodological-transparency check** at Pass 1 (opinion/position pieces without a methods section don't clear the bar; structured empirical/conceptual contributions do). Tag included preprints `preprint`; update citation if later formally published.
- **Curated grey-literature "other methods":**
  - **Coursework** = "records identified through prior author engagement with the field" — **self-assembled prior reading, NOT committee-curated.**
  - **Practitioner Network** = prospective stream (declared monitored-sources list, named informants, structural queries on a cadence) so it has a defensible start date, not a back-fill. Tighter grey-lit criteria; **cap at ~20–30 sources** so it doesn't dominate. Tag distinctly (`grey-lit`).
- **Rationale for keeping practitioners:** academic publication lags practitioner knowledge 12–24+ months; a peer-review-only corpus describes the field as it was ~18 months ago. The two-track corpus enables a synthesis-chapter argument naming the gap between peer-reviewed framing and practitioner reality.

### 4.2 Search strategy
- **Recall > precision at the search stage.** Boolean clusters with wildcards + OR-grouped synonyms; precision is handled downstream in screening.
- **Filters allowed:** peer-reviewed = yes; **date range 2020–2026** (all databases). Secondary 2018–2019 pass only for foundational automation-bias/oversight theory. **Do NOT** apply full-text-availability filters at search time (that's a retrieval-convenience filter that makes the corpus a function of Purdue's licenses) — handle non-retrievable items at full-text screening with reason `not-retrievable`.
- **ABI/Inform → Scopus pivot.** ABI was rejected (results too thin); a calibration query returned **3 hits in ABI vs. 110 in Scopus (~37×)**, justifying the pivot as a coverage decision. (See `Query_Composition_and_Log.xlsx` → `Rejected_Sources` sheet.)
- **Scopus export cap:** 2,000 records per operation; document any subject-area filters applied on export.
- **Saturation evidence:** adding WoS yielded 116 unique new records (35%) with **65% overlap** against IEEE+ACM+Scopus+arXiv → multi-database strategy reached reasonable saturation. When a *synthesis* gap appears, prefer a **targeted back-fill query in an existing database** over adding a new database.
- **AI-assisted search disclosure:** Gemini used for candidate-source identification — save full prompt + response, date, visible model version; every named source is a *lead* requiring independent verification under the same inclusion criteria. Claude used for query refinement + consistency checks — **not a citeable source**; any AI-suggested citation is verified against the original.

### 4.3 Query log
- **One row per query** in `Query_Composition_and_Log.xlsx` (sheet `Query_Log`): ID, category, query string, database, field, date run, hit count, comment. Rejected databases live in `Rejected_Sources`. Tool-name lists are maintained via a named range + CONCAT formula (`Formula_Data` sheet).
- **Query ID scheme:** `Q-IEX-NN` (IEEE), `Q-ACM-NN`, `Q-SCO-NN` (Scopus), `Q-WoS-NN`, `Q-arXiv-NN`, `Q-SSRN-NN`, `Q-ABI-NN` (rejected).
- **Six thematic categories:** AI Code Risk & Security; AI Code Quality & Debt; Human Oversight & Capacity; Org Governance & Policy; Org Risk Recognition; Tool-Specific.
- **Executed to date (hit counts):**
  - IEEE `Q-IEX-01..22` (run 2026-04-09): notable — Q-IEX-03 *vibe coding*×risk = 4; Q-IEX-14 *shadow IT* = 0; Q-IEX-07 = 182; Q-IEX-17 (tool×security) = 135.
  - ACM `Q-ACM-01..06`: Q-ACM-01 = 103; Q-ACM-03 *shadow AI* = 0; Q-ACM-06 *vibe coding*×governance = 9.
  - arXiv `Q-arXiv-01..05`: Q-arXiv-01 *vibe coding* = 78; Q-arXiv-02 = 76.
  - Scopus `Q-SCO-01..05`: Q-SCO-02 = 354; Q-SCO-05 *automation bias/overtrust* = 473.
  - WoS `Q-WoS-01..03`: Q-WoS-01 *vibe coding* = 35; Q-WoS-03 = 235.
  - SSRN `Q-SSRN-01..09`: large pools — Q-SSRN-07 *EU AI Act/NIST* = 868; Q-SSRN-09 tool cross-cut = 844; Q-SSRN-03 liability/IP = 754.
- **Pending AI-House-derived queries (screening prompts UNCHANGED — vocabulary additions only):**
  - Multi-agent / adversarial oversight: **Q-IEX-23 (23 hits), Q-ACM-07 (141), Q-SCO-06 (pending), Q-arXiv-06 (pending).**
  - Prompts-as-artifact (governance framing): **Q-SCO-07 (pending).**
  - Prompts-as-artifact (technical-reproducibility framing): **Q-IEX-24 (1 hit), Q-ACM-08 (pending).**
- **Also queued:** "agentic SDLC" / "ADLC" back-fill cluster (run *after* Pass 1 restore + Pass 2 update; phrase-lock the spelled-out forms; "ADLC" alone is noisy). Deferred/contingent: Google Scholar + terminology-probe queries (Q-SSRN-10, Q-WoS-04, Q-GS-17), contingent on SSRN coverage adequacy.

### 4.4 Screening (two-phase, single-coder)
- **Single-coder protocol** with bias controls: calibration session on first 10–15 items; decision log with one-line rationales on non-obvious calls (~20–30%), especially REL-CORE vs. REL-ADJACENT borderlines. Inter-rater reliability via **advisor/committee spot-check of 10–15%** of title/abstract decisions (confirm with Thomas whether spot-check vs. full second screener is expected).
- **AI is a consistency-check tool, not a decision-maker.** The statement "abstracts were screened by a single coder using the following criteria" must remain true; inclusion/exclusion and quality-appraisal judgment stays human.
- **Two passes:**
  - **Pass 1 — recall-favoring** title/abstract screen; exclude only obvious non-matches.
  - **Pass 2 — operationalizability standard** (designed ~73% rejection of Pass-1-Keep; frame in methods as *"73% of Pass-1-Keep tightening," not "73% corpus collapse"*). Pass 2 is **weeding, not confirmation** — strip keyword-only matches.
  - **Pass 2 keep rubric:** keep if operationalizable. T1 = vibe coding; code-review scalability; AI-code risk + measurement; org governance; developer oversight; LLM-as-judge/adversarial agents as oversight trigger. T2 = human oversight; AI governance + DevSecOps; regulatory org implementation; legal liability org response; scalable oversight at any pipeline stage. Default-to-keep; *maybe* = thin abstract only.
- **Sequencing after Pass 2:** confirmed-Keep theme-balance review (surface *synthesis* gaps, not search gaps) → **data extraction** (study type, method, population, AI tool studied, RQ alignment, key finding) into a matrix → **then** thematic coding **on the extracted matrix, not the papers** (coding before reading locks a self-fulfilling mental model). Extraction-before-coding is the SLR standard.

### 4.5 Exclusion reason codes (one per record — first disqualifying factor)
`out-of-scope` · `wrong-level` (technical, no org/human dimension) · `wrong-type` (opinion, no evidence base) · `too-old` (pre-LLM unless foundational theory) · `duplicate` · `not-retrievable` · `quality-threshold-not-met`.
Apply **consistently across analogous records** (don't drop thesis-contradicting items while keeping supporting ones — consistency is what reason-coding protects).

**Two author-specific screening rules (always-on):**
1. Documents **authored by Scott himself** → **Discard** (unless explicitly instructed otherwise).
2. **Purdue Brightspace URLs** → **Discard** (course-platform pages, non-citable).

### 4.6 Classification (Pass-2) tag schema — document in an appendix
Five prefixed dimensions on Zotero tags:
- `T:` topic domain (e.g., `RISK-SEC`, `VIBE-DEFN`, `OVERSIGHT-HUMAN`)
- `S:` solution type (`SOL-TOOL`, `SOL-PROCESS`, `SOL-FRAMEWORK`, `SOL-HYBRID`)
- `M:` research method (`M-SLR`, `M-EMPIRICAL`, `M-CASE`)
- `R:` relevance to core RQ (`REL-CORE` / `REL-ADJACENT` / `REL-WEAK` / `REL-EXCLUDE`)
- `OSA:` oversight-scaling angle, multi-select (`OSA-VOLUME`, `OSA-BIAS`, `OSA-FATIGUE`, `OSA-ACCOUNTABILITY`, `OSA-SHADOW`)

> **Do not** apply the analytical `T:/S:/M:/R:/OSA:` schema until **after full-text extraction**. Abstract-level tags must be clearly provisional under the **`auto:beat:*`** namespace.
> Scopus `theme:*` Queue tags (governance/oversight/risk/orgs/tooling/empirical/vibe-coding/other) are **batching aids only** — a screening decision in any source outranks queued status.

### 4.7 Validation (two samples per pass)
- **Trust Check** — stratified 20/category, **unblinded**, gating pre-apply. Thresholds: ≤5% disagree → apply; 5–15% → apply + document; ≥15% → stop.
- **Methodology Validation** — random N=100, **blinded** (non-negotiable), Cohen's κ.
- **Cross-model validation** — use **ChatGPT + Gemini Advanced** (NOT Gemini Flash; Flash hallucinated ~98% of item keys in 7/12 batches and is unreliable here). 50 rows/batch, fresh chat per batch, history isolation, **mandatory item-key validation after each batch**. Run *after* non-SSRN screening completes.

---

## 5. Zotero structure & conventions

- **Group library ID `6505702`**, type `group`. Read-only key for browsing; **write key only when a write is explicitly authorized — ask first, then swap back immediately.** Credentials live in `~/.config/claude-zotero/.env` (keys `ZOTERO_API_KEY`, `ZOTERO_LIBRARY_ID`, `ZOTERO_LIBRARY_TYPE`). **Do not commit keys into any file.**
- **Conceptual structure** (per project description): `Database Queries` root → per-source collections → `Imports` (raw) + `Classification`/`Screening` with four buckets `00-Queue` / `01-Keep` / `02-Maybe` / `03-Discard`. **For content queries, exclude `Imports` and `Discard`.**
- **PRISMA-native naming:** rename top-level `Classification` → `Screening` (the four-bucket structure *is* screening; "classification" properly names the Pass-2 thematic activity). Keep the four buckets unchanged.
- **Provenance is permanent:** source/query collections are immutable provenance records (they replace the old `Q:` tags). Items are *added* to working collections without being *removed* from source collections — multi-collection membership is the point. **Items never move out of `01-Imports`.**
- **Dedup = always merge, never delete.** Zotero merge keeps all collection memberships + tags on the survivor. Cross-source content-duplicates that won't auto-merge go to `00-Dups`, resolved via **`04-Superseded`** (keep the most-advanced item type; venue hierarchy **journal > conference > preprint > thesis > webpage stub**; never delete the inferior copy). Screening decisions **propagate cross-source** — a decision in one source applies to the same item everywhere.
- **Counting discipline** (state which count at each PRISMA stage):
  - *papers* = unique top-level records (dedup by item key) · *items* = may include child attachments/notes · *records this query returned* = raw per-collection count (may double-count).
  - For unique counts across overlapping collections, **work with sets of item keys**, never sum per-collection counts.
  - Cross-check ≥1 stage count against the API `Total-Results` header (note: it lowercases to `total-results` in Python `urllib`); a pagination bug (fixed Apr 2026) truncated some tooling at 100 — re-verify any count hitting exactly 100.

### Key collection keys (verify before reporting)
| Collection | Key | Last-known count |
|---|---|---|
| Phase 2 Keep | `3D8XR6AP` | 923 items |
| Phase 2 Maybe→Keep | `ZB6R4G9H` | 59 items |
| LinkedIn Post 01 | `JHJN4DKW` | 5 items |
| Practitioner Network Keep | `5XM4VKNG` | — |

### Zotero API patterns
- PATCH needs the current item version + `If-Unmodified-Since-Version` header; **204 = success**.
- `parentCollection: false` (not `None`) marks a top-level collection — check `not c['data'].get('parentCollection')`.
- File attachments via API to a *group* library register metadata but don't reliably transfer bytes → **use desktop drag-and-drop** for attachments.
- Direct `urllib` calls to `https://api.zotero.org/groups/6505702/items/{key}` are more reliable than the `zotero.py raw` subcommand.
- PDF fallback: fetch `https://export.arxiv.org/pdf/{arxivID}` when S3 storage is blocked.
- **Always prompt Scott to back up Zotero (File → Export Library) before ANY major write**, even idempotent scripts.

---

## 6. Current pipeline state (last known — VERIFY)

> **Live-verified 2026-07-01** (read-only Zotero): Phase 2 apply is **complete** — `00-Queue` = 0 across all 10 sources; Phase 2 Keep `3D8XR6AP` = **924**, Maybe→Keep `ZB6R4G9H` = **59** → eligible pool **983**. The AI-House queries (Q-SCO-06/07, Q-arXiv-06/07, Q-ACM-07/08, Q-IEX-23/24) are fetched, deduped, and Pass-1 + Pass-2 screened (item traces show `s1:*` + `s2:*` tags and correct Phase 2 bucket membership). They contributed almost nothing to *Keep* under the tight Pass-2 rubric, which is why the pool held near 923.

- **Two-phase screening complete across major sources.** Phase 1 (recall) → 4,061 Keep+Maybe. Phase 2 → **973 Keep / 73 Maybe / 2,908 Discard**. Final eligible pool (live 2026-07-01): **924** items (`3D8XR6AP`) + **59** Maybe→Keep (`ZB6R4G9H`) = **983**.
- **Pass 2 validation (2026-06-03):** Trust Check 60-item stratified — Po = 86.2%, **κ = 0.79 ("substantial")**; per-category discards 100% / keeps 85% / maybes 72%; zero false-negatives in discards → **applied**. Human review of 39 escalated items (38 low-confidence + 1 model conflict) → 17 discard / 10 keep / 12 maybe → applied via union rule (`human_decisions.csv`).
- **Pass 1 restore:** a data-integrity incident (apply script pointed at Pass 1 buckets instead of Phase 2 collections) corrupted ~38% of Pass 1 items. `restore_pass1_from_csv.py` recovered it — `applied=2890`, `apply_errors=0`, `fetch_failed=79` (benign SSRN merge-orphan 404s), `skipped_superseded=30`. Ground truth: `nonssrn-decisions-2026-05-25.csv` + **`ssrn-decisions.xlsx`** (the **xlsx is mandatory** — CSV export dropped the human column).
- **Phase 2 population:** `apply_phase2.py` **confirmed complete** (live-verified 2026-07-01 — all source `00-Queue` collections drained; Phase 2 buckets populated). The mid-run state noted in prior sessions has since finished.
- **SSRN screening:** Claude Sonnet 4.6 via Claude Code CLI (Max), 30s rate limit, 3,864 items; output in `~/slr/ssrn` on Faberix. An earlier Opus partial run (~325 items) was archived for consistency.
- **Scopus state (2026-04-23):** 1,010 imports — 22 Keep / 0 Maybe / 420 Discard / 568 Queue; Queue split across 8 `theme:*` sub-collections (governance 170, oversight 161, risk 104, orgs 105, tooling 13, empirical 8, vibe-coding 1, other 6).

---

## 7. Tooling & environment

- **Brainstorming/architecture** → claude.ai chat. **File-touching / command execution** → Claude Code.
- **Machines:** **Faberix** (Ubuntu workstation) for long-running jobs — `nohup` + timestamped logs, `.pid` files, `tail -f`; **BabyBlackDragon** (Mac VM) for interactive work. *Multiply Claude's time estimates ~3× for Faberix throughput.*
- **Claude Code on Max subscription** (not API keys). Auth via **`CLAUDE_CODE_OAUTH_TOKEN`** (`claude setup-token`) in `~/.config/claude-code/env` (chmod 0600); **`ANTHROPIC_API_KEY` must be explicitly unset** so it doesn't override. *Verify billing regime for programmatic use via `/usage` — programmatic runs may draw from a separate credit pool at API rates rather than the interactive window.*
- **Git workflow:** short-lived topic branches `type/short-kebab-description`; `main` always-releasable with annotated version tags; no separate release branch. Scripts saved to **permanent locations (not `/tmp`)**. Editor preference: **vi over nano**.
- **Claude Code skills** (installed `~/.claude/skills/` on Mac + Faberix; share path `~/jukebox/scott/slr/claude-skills/`):
  - `zotero` (stdlib-only) · `zotero-slr-dedup` (stdlib-only) · `arxiv-zotero-import` (stdlib-only) · `zotero-bulk-tagging` (needs `openpyxl`) · `claude-skill-installer` (idempotent) · `slr-project-init` · `slr-pipeline-patterns`.

### Defensive pipeline patterns (codified as `slr-pipeline-patterns`)
1. None-guard: `(x or "")`, not `.get(k, "")`.
2. Anchor batch globs: `batch_[0-9][0-9][0-9].csv`, not `batch_*.csv`.
3. One checkpoint key per batch.
4. Header-anchored CSV extraction with a fence-line guard.
5. Row counts via `csv.DictReader` length, not `wc -l`.
6. Sleep between batches; check exit codes **before** setting checkpoint.
7. Item-key hallucination validation after each batch.
8. `_out` cleanup verification before re-running a phase.

---

## 8. HOS / CondoParkShare pilot

**HumanOversightSystem (HOS)** — a cross-vendor **multi-agent AI code-review pipeline** that routes human attention by risk. **CondoParkShare** is the empirical substrate: a parking reservation/booking app for condo residents.

> **Repos (verify org):** this session referenced `github.com/ScottThurlow/HumanOversightSystem` and `github.com/ScottThurlow/CondoParkShare`. Prior project notes referenced a **`thurlow-research/`** org for the same repos (+ `VibeOversightDissertation` at `~/code/VibeOversightDissertation`, CC BY-NC 4.0). Confirm which org is canonical before pushing.

- **Reviewer roles (decorrelation: a vendor never reviews its own code):** Claude = author/triage/arbiter · Codex = adversary/security · Gemini (agy) = correctness/architecture/performance · Copilot = CI baseline.
- **Access:** subscriptions (Claude Max 20×, ChatGPT Pro, Gemini Pro student), **not** API keys — panel runs locally and posts findings to PRs.
- **Architecture decisions:** worker on even minutes (`*/2`), overseer on odd (`1-59/2`), 2-min cadence. Work gate = shell only (never invokes Claude): stats files + ≤1 read-only GitHub query. Handoff = file fast-path (worker drops completed-PR list as final atomic step) with GitHub PR-queue fallback; "submitted PR = ready" valid only if `gh pr create` is the worker's single final step. Atomic claims on both layers; per-agent locks, never cross-agent. **Distinct GitHub machine accounts per agent** to separate the *actor-identity gap* from the *determination-honesty gap*. cron hardening: pin `HOME`/`PATH`, absolute `claude` path, optional nvm source, env-dump debug toggle.
- **Principles:** actor-identity gap and determination-honesty gap are *independently* necessary. Human-approval check must live **server-side**. PR is the human trigger; pre-PR prechecks stay machine-only/advisory. **Author fixes but never re-certifies** (bounded fix-and-reverify: author fixes, round cap, tier-gated escalation, fixes stay visible as commits). Prefer deterministic gates over LLM evaluators for failure detection. Structure agent PR comments as descriptive/contextual/actionable layers.
- **Notification stack:** Resend or Brevo (resident email); Twilio or Plivo (resident SMS; defer 10DLC until needed); **Pushover** (~$5 one-time) for Scott's own HOS ops alerts.
- **Change proposals:** `HOS-Evidence-Based-Change-Proposals.md` — 9 proposals (P1–P9); top severity **P9** = untrusted natural-language inputs as an adversarial trust boundary (100% attack success via iterative PR-metadata framing; adversarial bug reports triggered insecure patches in 90% of cases; cheap validated fix exists). P8 primary citation = Loker (CodeRabbit, Dec 2025, Zotero `K4CKRTEI`).

---

## 9. LinkedIn Post 01 (in progress)

Collection `JHJN4DKW`, five papers (full text attached via Zotero desktop):
- `P868GNU7` — ACM, 567 Claude Code PRs across 157 OSS projects.
- `UIXCRBQX` — agentic vs. human PRs: more bugs/security/breaking changes.
- `8CQRCPW2` — SWE-PRBench: frontier models catch 15–31% of human-flagged issues.
- `3SU9QZ6F` — AIRA: 1.80× more high-severity findings in AI vs. human code.
- `VR9AM6VV` — AgenticSCR: autonomous pre-commit secure code review.

AIRA + SWE-PRBench read in full; others at abstract level. **Post draft not yet written.**

---

## 10. AI-use disclosure & ethics (methods chapter)

- Explicit AI-use statement disclosing: (1) **Claude** = query-refinement + consistency-checking; (2) **Gemini** = candidate-source identification with a verification protocol; (3) the principle that **Claude is not citeable** for literature claims — original papers are the citable sources.
- **Verify every AI-assisted citation** (authors, years, titles, pages are common error points — leads, never confirmed records).
- **Intellectual judgment stays the coder's** — inclusion/exclusion, quality appraisal, interpretive conclusions are not delegated to AI. State this alongside the disclosure. Follow APA 7 + venue AI-use policies.

---

## 11. Key learnings & citable facts

- **CodeRabbit / Loker (Dec 2025, Zotero `K4CKRTEI`):** AI-generated code ~**1.7×** more likely to have issues than human-written, with some defect classes nearer ~3×. Citable directly to Loker as the **primary** source (do not defer to a peer-reviewed restatement).
- **Practitioner corroboration:** Aravind Bala (CTO, SeekOut) independently corroborated the prompts-as-artifact construct at the AI House panel (2026-05-20); anonymized in Zotero as "senior practitioner / CTO at a different org in HR-tech." 10+-year relationship → methodologically relevant for IRB + methods-chapter positionality; name-attribution contingent on permission.

---

## 12. Synthesis structure (informs extraction-matrix framing)

Five thematic pillars: (1) **The Vibe Coding Phenomenon** (definition/adoption); (2) **The Risk Landscape** (quality, security, accountability gap); (3) **Human Oversight & the Reviewer Capacity Problem** (the heart); (4) **Organizational Governance Responses** (tiering, IAPP, CISA, NIST, joint OT guidance); (5) **Theoretical Synthesis & Research Gaps**. Report **results by stream category** so peer-reviewed vs. practitioner framing can be compared explicitly.

---

## 13. Open work / next actions

**SLR**
- [x] **Verify Phase 2 apply completed** — DONE (live-verified 2026-07-01; queues drained, pool = 983). See §6.
- [x] **AI-House queries** Q-SCO-06/07, Q-arXiv-06/07, Q-ACM-07/08, Q-IEX-23/24 — DONE (fetched, deduped, Pass-1 + Pass-2 screened; verified via item traces 2026-07-01).
- [ ] **NEXT — Weeding the 983 → two-tier extraction corpus (strategy agreed 2026-07-01):**
  - **Stage 3 — abstract-level relevance triage (no fetch):** 3-way bin per item — **Core** (REL-CORE, directly addresses scalable human oversight of AI code → full extraction, ~100), **Context** (adjacent/context-only but methodologically strong & transferable → T2 lightweight abstract-level extraction), **Discard** (weak *and* off-core → exclude with reason code). Criterion = centrality to core RQ (distinct from Pass 2 operationalizability). Cross-model ensemble = **Claude + ChatGPT Pro + Gemini Advanced** (Advanced only — never Flash), each assigns bin + centrality score; auto-classify on 3-model agreement; **human-review two bands only:** model disagreements and the Context↔Discard borderline (where judgment lives). Tag namespace `s3:*`. Per-batch item-key validation.
  - **Stage 4 — fetch full text for Core candidates only (~100–150):** depth/quality screen (substantive oversight mechanism? rigor?) → final ~100; thin ones demote to Context or discard. Fetched PDFs feed extraction directly (no double-fetch). Context tier extracted from abstracts, so **not** fetched.
  - **QA per AI stage:** stratified Trust Check (gating: ≤5% apply / 5–15% apply+document / ≥15% stop) + blinded **N=100 Cohen's κ**; for Stage 3 (ordinal) also report inter-model rank correlation.
- [ ] Targeted spot-check of the Discard pile from Q-SCO-07 / Q-IEX-24 / Q-ACM-08 (look for prompt-versioning items dropped as wrong-level/wrong-type) — fold into Stage 3 human-review band.
- [ ] "agentic SDLC" / "ADLC" back-fill cluster — after Pass 1 restore + Pass 2 update.
- [ ] Deferred/contingent: Google Scholar + terminology-probe queries (Q-SSRN-10, Q-WoS-04, Q-GS-17), contingent on SSRN coverage.
- [ ] LinkedIn Post 01: read remaining full text, draft the post.
- [ ] Provisional `auto:beat:*` abstract-level tagging across the 983-item corpus (NOT the analytical schema).

**HOS / CondoParkShare**
- [ ] `DECISIONS.md` entry for GitHub machine-accounts implementation (write as work happens).
- [ ] Verify billing regime for programmatic Claude Code (`/usage`).
- [ ] Pipeline-observability improvements (candidate skill `slr-pipeline-observability`): None values crashing `Counter` post-write; no real-time progress summary; failures not surfaced prominently.

**Known bugs**
- [ ] `cleanup_superseded_tags.py` date-tiebreaker: year-only dates ("2026") wrongly lose to year-month ("2026-02") due to string comparison. **Fix:** pad year-only → "YYYY-01" before comparing.

---

## 14. Methodology questions to confirm with the committee

- **Thomas:** solo-coder screening vs. second-screener requirement, and whether spot-check agreement reporting suffices.
- **Thomas:** confirm "accepted for publication" definition (currently understood to permit a conference paper) before locking venue (ICSE SEIP / EASE / HICSS).
- If formalizing Practitioner Network: draft + date the one-page protocol (monitored sources, informants, structural queries, cadence, tighter grey-lit criteria) **before** collecting more items.
- Lock remaining coverage gaps before final corpus: regulatory frameworks (EU AI Act, NIST, CISA), prompt-injection + supply-chain terminology, agentic-coding vocabulary, developer overtrust/over-reliance.

---

## 15. Working style (for the assistant)

- **Short, summary-style answers**; elaborate only when asked. (This *file* is the exception — comprehensiveness was requested.)
- Always include **citations to sources**; for complex questions, give **excerpts + reasoning**.
- Scott works **stream-of-consciousness**; organize and formalize the structure implied by raw thinking.
- **Flag reusable-task opportunities** → propose a skill or embedded script, and **confirm before creating**.
- **Recommend a model switch** (Opus/Sonnet/Haiku) when it would materially change quality, or cut cost at similar quality. (Bulk screening → Sonnet has been the workhorse; heavy synthesis/architecture → Opus; trivial mechanical passes → Haiku.)
- **Throttle external APIs:** Zotero ≤10/s, others ≤1/s.

---

## 16. Startup verification checklist (run these first)

1. `Query_Composition_and_Log.xlsx` is the query source of truth — reconcile any new runs into it.
2. **Phase 2 apply status** — confirm `apply_phase2.py` finished; check `00-Queue` / `01-Keep` / `02-Maybe` / `03-Discard` counts against the last-known numbers in §6.
3. Phase 2 Keep (`3D8XR6AP`) and Maybe→Keep (`ZB6R4G9H`) counts (expect ~923 / ~59).
4. Confirm canonical repo org (`ScottThurlow/` vs `thurlow-research/`).
5. Confirm Zotero credentials load from `~/.config/claude-zotero/.env`; default to the **read-only** key; **ask before any write**, and prompt for a library backup first.
6. Confirm Claude Code auth is via `CLAUDE_CODE_OAUTH_TOKEN` and `ANTHROPIC_API_KEY` is unset.
