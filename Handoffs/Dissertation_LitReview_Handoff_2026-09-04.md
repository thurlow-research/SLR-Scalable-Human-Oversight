# Handoff — dissertation literature review

**Written 2026-09-04.** Entry point for a **session whose job is writing and structuring the
dissertation's literature review** from the SLR corpus.

It is not a pipeline handoff. For screening state, adjudication queues and closeout items read
`Handoffs/SLR_Handoff_2026-08-29.md`; for RQ wording read
`Handoffs/Dissertation_RQ_Brainstorm_Handoff_2026-09-03.md`. This document assumes those exist and
covers what is specific to *writing the review*: what the corpus can support, which numbers survive
scrutiny, and where the argument is currently thin.

---

## 0. Two things to say before starting

**Model fit.** Judgment-heavy. Prose written here lands in the dissertation, and a mis-stated figure
becomes a permanent citation error rather than a reversible file edit. **Recommend Opus**, unprompted,
per the standing rule. Mechanical work — assembling bibliographies, reformatting tables, batch Zotero
reads — is fine on Sonnet.

**Working style.** Scott brainstorms and pressure-tests *first*. Do not draft chapter prose, edit
methodology files, or write to Zotero until explicitly authorized. Park mid-discussion design questions
rather than resolving them out of order.

---

## 1. Access, in one paragraph

Zotero group **6505702** is the system of record — every screening decision, tier, theme tag and
adjudication lives there, not in the repo. Credentials in `.envrc` (direnv, gitignored):
`ZOTERO_API_KEY_RO` for reads, `_RW` for writes, and **any write needs a library backup first**. Use the
`zotero` skill CLI or raw `curl` for mechanics, the **`papersflow` MCP** for discovery of things not
already in the library, and load **`slr-conventions`** before any inclusion or classification call.
**Read documents from disk** — `~/Zotero/storage/<attachmentKey>/<filename>`, TXT in preference to PDF,
never refetch what the library already holds.

---

## 2. The corpus, and which set to use

The funnel: 9,518 deduplicated records → 4,061 after a deliberately loose recall screen → 983 eligible
after a precision screen → 147 unique studies at full text → **72 in `Phase 6 - Kept Core`**
(`R9ZHDXMN`). Attrition at Phase 5 is the number worth remembering: **147 → 72**, roughly half the
full-text corpus demoted to Context on close reading, consistently more aggressively than the model
panel proposed.

**The lit-review working set is larger than Phase 6.** It is the union of Phase 6 with the four
`Dissertation Lit Review` sub-collections *and the parent collection itself*:

| Collection | Key | Items |
|---|---|---|
| `System LIterature Review / Phase 6 - Kept Core` | `R9ZHDXMN` | 72 |
| `Dissertation Lit Review` **(parent level)** | `9RN9P68N` | 2 |
| `Dissertation Lit Review / 01 - Primary` | `WVZFNSEC` | 37 |
| `Dissertation Lit Review / 02 - Supporting` | `BWPP3DZA` | 25 |
| `Dissertation Lit Review / 03 - Queue` | `4PE2T47Q` | 23 |
| `Dissertation Lit Review / 04 - Validation Apparatus` | `XPPEXKBN` | 12 |

**= 106 unique items after dedupe by item key.**

⚠️ **The parent collection is easy to miss.** Two items sit *directly* in `Dissertation Lit Review`
rather than in 01–04, and a query that walks only the four numbered children silently drops them. That
happened on 2026-09-04 and cost the corpus **Vaccaro et al. (2024)** — see §4, it is one of the most
consequential papers in the set. The sibling `01 - Candidates` (`84B8YDJJ`) is empty. There is **no
collection named "Stage 6"**; `slr-tools/stage6/` is pipeline-stage numbering, not a Zotero folder.

---

## 3. The thesis, compressed

**Overarching RQ.** How do organizations practice and scale human oversight of AI-generated code so
that oversight keeps pace with the *volume* of AI-produced code without sacrificing quality — including
the governance landscape and the strengths and limits of current practice?

**The core claim (the oversight-scaling inversion).** In conventional engineering, riskier artifacts
draw more scrutiny. For AI-generated code the curves appear to cross: the code is measurably riskier
*and* receives less inspection. Risk ↑, inspection ↓.

**Why "review more carefully" is a non-answer.** Parasuraman & Manzey establish that automation
complacency emerges precisely under the conditions AI-generated code creates — a usually-correct
automated process plus competing task demands — in both expert and novice operators, and is not
correctable by training or practice. Oversight has to be redesigned into the process, not intensified.

**Six sub-questions** (locked structurally 2026-07-10, wording still open):
SQ1 magnitude of the gap · SQ2 why current oversight is insufficient · SQ3 what mechanisms exist ·
SQ4 how oversight is enacted in practice · SQ5 **how it scales** (the crux) · SQ6 how it is governed,
audited and evidenced. Shape: *what exists → how it's practiced → how it scales → how it's assured.*

### Two findings from F2 that constrain how the thesis may be stated

**1. The inversion is not yet demonstrated to a strict standard.** Under the §88 leakage test —
which demands *observed review absence*, or defects in merged code with review failure as the cause —
`oversight-scaling-inversion-v2` fires on **exactly one paper in 72**: Gao (`59KP8GTP`). The corpus
supplies volume, pressure, queue growth and merge speed instead. **Not disproven; not demonstrated.**
That is simultaneously the strongest warrant for the fieldwork and a hard caution on how the premise is
worded. Do not write the inversion as established literature.

**2. Mutual peer critique is nearly absent.** 25 one-directional versus 3 mutual. The corpus builds
dedicated critics over producers; **agents checking each other — the thesis mechanism, and HOS's — is
the scarce case.** This is a genuine gap claim and it is defensible.

---

## 4. The evidentiary spine — key documents by the job they do

Cite these with the qualifications in §5. Zotero keys are the stable handle.

**The anchor.** `59KP8GTP` **Gao et al. (2026)**, *On Autopilot?*, MSR '26. The single paper that
meets the strict inversion test. AI-co-authored PRs from non-owners merge with no human review at a
higher rate than any other cohort, and the scrutiny gradient *inverts* relative to human PRs.

**The scaling boundary — and a negative result.** `2K5GNIJU` **Vaccaro, Almaatouq & Malone (2024)**,
*When combinations of humans and AI are useful*, Nature Human Behaviour. Preregistered meta-analysis,
106 experiments, 370 effect sizes. Human–AI combinations performed **significantly worse than the
better of human or AI alone** (Hedges' g = −0.23, CI −0.39 to −0.07) — no synergy — while beating the
*human alone* (g = +0.64). The decisive moderator is the thesis in miniature: when the human is better
alone, combining helps (g = 0.46); **when the AI is better alone, combining hurts (g = −0.54).** This
is the most rigorous single piece of evidence in the corpus and it is the one that most constrains
optimistic framings.

**The other boundary — who can oversee.** `22JBEZNK` **Virk & Liu (2025)**, VL/HCC. Skeptical,
incentivised, explicitly primed non-programmers still failed to detect safety-critical flaws. Rules out
"widen the reviewer pool" as an escape from the scaling argument — *but* participants never saw code,
only natural-language explanations, so it does not test code review. State that qualification.

**Downstream consequence.** `9H6FWJME` **Liu et al. (2026)**, *Debt Behind the AI Boom*. 302.6k
AI-authored commits, 6,299 repos; 22.7% of AI-introduced issues survive to HEAD.

**Insufficiency of automated substitutes.** `5NZ2EDEK` **Karakaya et al. (2026)**, EASE '26. LLM
judges cannot reliably evaluate AI review-bot output against industrial developer labels — and the
authors' own preferred metric says the alignment is nil. The strongest available evidence that you
cannot automate your way out of the evaluation problem.

**Practice at scale.** `5VTAJISY` **Takerngsaksiri et al. (2025)**, ICSE-SEIP. HULA deployed in
Atlassian JIRA. The most detailed real deployment funnel in the corpus, and it contains an
approval-versus-judgment gap that is directly on-theme (§5).

**Theory.** `ING3D89M` **Parasuraman & Manzey (2010)** — complacency and automation bias as
attention-driven, training-resistant phenomena. `5DCQDB4C` **Langer et al. (2024)**, Minds
and Machines — Signal Detection Theory applied to oversight, separating *sensitivity* from *response
bias*. Langer is Context-tier (general-AI, not code) but supplies the measurement vocabulary.

**Governance.** `84D2AMVM` **McKay (2024)**, HCII — synthesises decision-making research into
HITL-effectiveness risk factors (complacency, persuasion, workload, conformity, unequal error
treatment, org policies that deter challenge). All evidence is transferred from non-AI settings; it is
a framework for what to ask, not measured AI-oversight risk.

**Explanation as the last mile.** `7UB2MD8Z` **Kang et al. (2024)**, EMSE. Explanations improved
reviewers' patch-correctness judgment — with two regressions, one via uncritical acceptance of the
tool's reasoning (§6).

**Security framing.** `3Z45M3V3` **Fu et al.**, TOSEM 2025 — the Zotero record carries the **2023
preprint date**, so `Short cite` renders *Fu et al. (2023)* while the problem statement cites 2025. Fix
the record or the citation, but be consistent. `6ZC3H7AF` **Liu et al. (2026)**,
*Agent Skills in the Wild* — the anchor for the AI-tooling supply chain as an under-governed oversight
surface.

**Do not cite as evidence.** `5RLPIA3K` **Swidey (2026)** is a **vendor white paper with a declared
patent interest** — sole author is Founder & CEO of the company selling the architecture, two USPTO
filings on the title page, and **no evaluation of any kind**. Cite the mechanisms as an industry
proposal; never the claims.

---

## 5. What the full-text pass changed — citation cautions

A full-text extraction pass over the corpus (39 of 106 items complete as of 2026-09-04) has produced
**146 recorded discrepancies, 70 of them high-severity**. Full detail in
`slr-tools/stage6/discrepancies.md`, one JSON per item in `slr-tools/stage6/extraction/`. **Read that
file before writing any sentence containing a number.** The recurring patterns:

**Figures in the problem statement that need correcting.**

- **Gao.** The problem-statement anchor and the `dissertation-input` note both say "~80% of
  AI-co-authored PRs from non-owners merge with zero review." **Table 2 gives 11,817/13,618 = 86.8%.**
  The 79.0% in the body is *all* Human+AI merged PRs, not non-owners. The current anchor **understates
  the finding by about 7 points.**
- **Gao's 67.5%** has a stated human baseline of **61.0%** in the RQ1 summary — a 6.5-point gap, far
  less striking cited alone. And the same 67.5% is described as a share of *PRs* in the abstract and a
  share of *users* in the body; Table 2 settles it as PRs.
- **Gao's 86.9% no-guidelines** figure has a denominator of **145 sampled repositories**, not the 2,253
  in the dataset.
- **Fu et al.** The 29.5%/24.2% per-language figures are accurate, but the **overall rate is 27.3%**
  (200/733), not the "around 30%" the paper's own introduction rounds to. The same introduction says
  both "43 different CWEs" and "the 38 CWEs identified" one line apart.

**Headline numbers whose baseline changes the reading.**

- **Fu's 55.5% Copilot-Chat fix rate** is the best of three conditions and requires feeding the tool a
  static-analysis warning. Out of the box it is **19.3%.**
- **HULA's 82% plan approval** sits against **41%** of the same practitioners agreeing the plans were
  accurate — a 40-point gap between clicking approve and judging correct. End-to-end, **56 of 663
  issues reached a merged PR (8.4%)**; the three quoted rates each use a different shrinking
  denominator. Directly on-theme for oversight-theater.
- **HULA's planner recall falls 86% → 30%** moving from SWE-bench to real Atlassian issues. The
  abstract does not mention it. It is the best benchmark-to-practice collapse evidence in the corpus.
- **Karakaya's "moderate alignment"** (agreement 0.44–0.62) is contradicted by the paper's own MCC:
  **−0.002, −0.059, +0.011** — chance level, negative for two of three models — reported *because* the
  data are imbalanced. Cite the MCC.
- **Liu's 22.7% survival** has **no human baseline**; the authors say so explicitly and explain why
  they judged one infeasible. And **89.3% of the 484k issues are code smells**, not correctness or
  security.
- **8MXATG38's 20× deployment frequency** is attributed in the body to "service-level autonomy *and*
  AI integration" — an organisational change the abstract omits entirely.

**Second-hand figures that will be misattributed if you are not careful.** The "**~40% of
AI-generated code contains vulnerabilities**" claim (Pearce et al.) circulates through at least four
corpus papers as citation, never as measurement. Likewise "55% faster task completion," "up to 50%
faster merges," and "25–35% acceptance rates." **Retrieve the primary source before citing any of
them.**

**One unresolved cross-source conflict.** `6ZW9QNQH` cites "318 benchmark programs, strongest model
generates secure *and* correct code at **28%**." The TECH646 problem statement cites Zhao et al. at
"200 feature-request tasks, 61% correct, 10.5% secure." **These are different benchmarks with
different denominators and different joint criteria.** Do not combine or interchange them; establish
which is which before either appears in the chapter.

**Quality signals worth knowing about.** `6DXZGHD9` (Scientific Reports, 2026) contains **unfilled
template placeholders** where its expert-panel reliability statistics should be — "Kendall's W (0.\_\_)",
"Fleiss' κ = 0.\_\_", CVR "from \_\_ to \_\_" — while concluding the input was "reliable and valid."
`399HN438` reports accuracy figures for an agent that does not appear in its own architecture, with no
evaluation protocol described anywhere.

---

## 6. Cross-corpus tensions to adjudicate before writing

These are real disagreements between corpus papers. They need rulings, not smoothing.

**Does explanation help oversight?** `7UB2MD8Z` (AutoSD) found explanations significantly improved
reviewers' patch-correctness judgment (Mann–Whitney p < 0.05) — but across the full 12 problems the
tally was 7 improved, **2 worsened**, and in one case participants "accepted the reasoning of AutoSD
without significant scrutiny." Against that, `2K5GNIJU` (370 effect sizes) found **neither explanations
nor confidence levels significantly affected human–AI performance.** Not necessarily contradictory —
different tasks, different outcome measures — but **the oversight-explanation theme cannot be built on
an assumption that explanation reliably helps.**

**Is the automated reviewer a substitute or a router?** `5NZ2EDEK` says LLM evaluation of review
output is chance-level against developer labels. `72W6R4JG` says a *deterministic* verifier with
diagnostic feedback works well — but its constraints are hand-authored by a domain expert, so oversight
effort moved upstream rather than disappearing, and the paper is one toy domain with n=10 per arm.

---

## 7. What the evidence base can and cannot support

Composition of the 106-item set, from the adjudicated tags:

- **Venue.** 56 preprints (unrefereed) · 30 peer-reviewed conference · 11 journal · 7 working paper ·
  1 book · 1 vendor report. **The corpus is preprint-heavy and the methods chapter must say so.**
- **Contribution.** 54 empirical · 17 design-only framework · 3 literature review (74/106 tagged).
- **Evaluation basis.** Of the 40 items where it is derivable: **17 report no evaluation at all**
  (stated as future work) · 7 deployed in production · 7 benchmark · 5 synthetic · 3 expert-validated ·
  **1 real-world data.** This is the single most important structural fact about the corpus: **the
  literature proposes mechanisms far more often than it evaluates them**, and almost never against real
  data. SQ5's effectiveness answer will honestly report an immature evidence base — which is itself a
  finding.
- **Primary theme.** ai-review 19 · hitl-workflow 12 · oversight-explanation 10 · org-governance 10 ·
  quality-debt 9 · risk-routing 7.

**Known thin spots.** RQ4/SQ6 is thin — only three Phase 6 papers carry `regulatory-compliance` as
primary; regulated-industry oversight is an explicit target of the F5 supplementary search. `2K5GNIJU`
carries **no theme tags at all** and needs adjudication.

**Metadata defects that will surface in citations.** Fix in Zotero before generating any bibliography:

- **Four items hold free-text `date` fields** rather than ISO dates, so any `date[:4]` year
  extraction returns a word fragment. Derived short cites currently read *Mitchell & Shaaban
  **(Octo)***, *Yu et al. **(Dec.)***, *Sterz et al. **(June)*** and *Zhou et al. **(Apri)***:
  `6ZW9QNQH` `"October 9, 2025"` · `PPMTM4DG` `"Dec. 2024"` · `TW4I6DU6` `"June 5, 2024"` ·
  `XK3P9C96` `"April 13, 2026"`. Data defects, not a script bug — they will recur anywhere the year
  is parsed positionally, and they also break any year-based cohort filter.
- **`3Z45M3V3`** — dated 2023 (original arXiv posting) though the authoritative version is TOSEM 2025.
- **`VG6CIDQW`** and **`R4WJZBSF`** — no author metadata at all, and both are in Phase 6.
- **No item in the working set carries a DOI** in its derivable metadata — 0 of the 63 preprints and
  working papers. DOIs must be resolved externally.

---

## 8. The extraction pass — state and how to resume

`slr-tools/stage6/` holds a resumable full-text extraction harness. **39 of 106 items complete**,
3 batches checkpointed.

| File | What it is |
|---|---|
| `build_worklist.py` | Fetches the 6 collections, dedupes, resolves TXT paths, applies the derivations **imported from `prepopulate_extraction.py`**. Outputs `worklist.json`. |
| `read_paper.py` | Condenses a TXT for reading — strips references, keeps front matter, every numeric passage, and the tail (limitations live there). ~49% reduction. |
| `batch_ctl.py` | Batches of 10; validates every emitted key against the input set before writing a checkpoint. |
| `save.py` | Writes one extraction record with schema + key validation. |
| `write_workbook.py` | Fills `Extraction_FullText.xlsx` from row 5. |
| `verify_coverage.py` | Resolves each Coverage formula against written cells (no spreadsheet engine here). |
| `write_reports.py` | Regenerates `discrepancies.md` and `run_report.md` from the JSONs. |

**To resume:** `./.venv/bin/python batch_ctl.py status`, then work the next batch. The extraction JSONs
are keyed by item key, so they survive re-batching. Everything regenerates from them.

**Two design notes.** The template's example rows 3–4 are **skipped, not deleted** — every Coverage
formula already points at `5:204`, so no formula edits were needed. And the quality-appraisal fields
(*Limitations I assess*, *Confidence*, *Disconfirming?*) plus *RQ alignment* and *Intended use* are
**left blank by design** — the methods chapter's AI-use disclosure states that inclusion, exclusion and
quality appraisal are not delegated to AI.

**Known gap to decide.** `Contribution type` prepopulates on 74/106 and `Evaluation basis` on only
40/106, because those derivations key off `cal:human` facets many items lack. Values were left blank
rather than invented, each flagged as a `prepopulated_field_empty` discrepancy carrying the value that
*would* have been assigned. Applying the panel fallback to facets as well as themes is a one-line
change and a re-run — **Scott's call.**

---

## 9. Standing rules that apply here

- **Zotero is the source of truth.** Findings, decisions and adjudications live there; repo
  JSON/markdown is derived state. Never leave a decision only in a repo file.
- **Membership = provenance, never current state.** Phase collections freeze after population; tier
  lives in the `demote:context` tag.
- **All assistant-authored changes land via PR**, branch `claude/<topic>`, never direct to main.
- **The repo is public.** Never commit paper full texts (`slr-phase4/txt/`), `Backups/`, `.envrc`, or
  PDFs.
- **HARKing guardrail.** Refine the *questions* bottom-up from corpus structure; do **not** write
  findings-claims into the SQs before synthesis.
- **Verify before citing.** The `discrepancies.md` pass exists because the abstract and the body
  disagreed in **14 of the first 39 papers read**. Assume the next one does too.
