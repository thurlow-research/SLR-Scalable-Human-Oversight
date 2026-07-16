# SLR Methodology Bootstrap

A portable reference for spinning up a new systematic literature review project using the same workflow developed for the Vibe Coding Governance SLR. Use this as the starting point for the media-metadata SLR (or any future SLR) so you don't re-derive the architecture from scratch.

---

## 1. Methodology at a glance

A multi-stream PRISMA 2020 systematic literature review run by a single coder, with AI-assisted screening as a consistency aid rather than a decision-maker. Three identification tiers:

1. **Peer-reviewed database streams** — IEEE Xplore, ACM Digital Library, Scopus, Web of Science.
2. **Preprint stream** — arXiv (and SSRN where appropriate). Same substantive inclusion criteria as peer-reviewed, plus a methodological-transparency check at Pass 1 (short opinion pieces without a methods section don't pass).
3. **Curated grey-literature streams** — author-assembled prior reading ("Coursework") and a prospectively documented Practitioner Network. Tighter grey-lit inclusion criteria; capped count.

PRISMA 2020 explicitly separates "database searching" from "other methods" and asks each "other method" to be documented separately for reproducibility — this is why grey-lit streams live in their own tiers rather than being mixed into the database identification count.

### Two-pass screening

- **Pass 1** (title/abstract): screen for obvious excludes against pre-defined criteria. Default-to-keep on the borderline. Maybe = thin abstract only.
- **Pass 2** (full-text / close-read of survivors): weed items that match by keyword but not in substance. Apply the preprint methodological-transparency check here. Resolve Maybes.
- Data extraction (matrix) → THEN topic coding on the extracted matrix. Coding before extraction locks in a mental model and becomes self-fulfilling.

### Search philosophy

- **Recall over precision at the search stage**; precision is downstream in screening.
- Coined terms get phrase treatment (`"vibe coding"`); broad concepts do not phrase-lock.
- Filters allowed at search time: peer-reviewed yes, date range. **Never** full-text-availability — that's a license filter, not a relevance filter. Retrieval failures get coded later as `not-retrievable`.
- Default date range: 2020–present, with a secondary pass at 2018–2019 for foundational theory only if needed.

### AI use and disclosure

- AI (Claude) used for query refinement, screening consistency-checks, and batch screening of large corpora. **Not** a citeable source for literature claims. Verify any citation produced with AI assistance against the original.
- Methods chapter must include an explicit AI-use statement covering: tool, version, what it was used for, what it was *not* used for (intellectual judgment), and verification protocol.
- For batch AI screening: save the prompt verbatim, record model version and date, isolate batch history (fresh chat per batch), and run cross-model validation on a sample for reproducibility.

### Single-coder protocol and bias controls

- Pre-define exclusion rules and apply mechanically.
- Calibration session on first 10–15 items; consistency review.
- Decision log with one-line rationales on non-obvious calls (~20–30% of items).
- Inter-rater reliability via advisor or committee spot-check of 10–15% of title/abstract decisions. Confirm with advisor which version (second screener vs spot-check) the program expects before starting.

---

## 2. Query construction process

This is the workflow that produced the Vibe Coding query set and is the one to reuse.

### Step 1 — Thematic categories

Decompose the research question into thematic categories before writing any queries. Each query belongs to one category. Vibe Coding example: AI Code Risk & Security, AI Code Quality & Debt, Human Oversight & Capacity, Org Governance & Policy, Org Risk Recognition, Tool-Specific. For media metadata, expect different categories — derive them from the RQ first.

### Step 2 — Boolean cluster design

For each query, build OR-grouped synonym clusters, then AND the clusters. Example pattern:
```
("vibe coding" OR "AI-assisted coding" OR "AI code generation" OR "generative AI" AND code*)
AND
("code review" OR "code quality" OR "software quality")
AND
(governance OR oversight OR review OR policy)
```

- Wildcards on stems (`code*`, `govern*`) — but check each database's wildcard syntax; they differ.
- Phrase-lock only coined terms.
- One database-specific syntax per database; keep the conceptual query in the log and translate per-database.

### Step 3 — Named-range tool list (when relevant)

For tool-specific queries (Q17–22 in the Vibe Coding set), use a single Excel named range (e.g., `Tool_Names`) and CONCAT formulas to generate the per-tool query string. Keeps the tool list maintainable in one place.

### Step 4 — Query ID scheme

Database-prefixed IDs: `Q-IEX-NN`, `Q-ACM-NN`, `Q-SCO-NN`, `Q-WoS-NN`, `Q-arXiv-NN`, `Q-SSRN-NN`. One row per query in `Query_Composition_and_Log.xlsx`:

| Column | Content |
|---|---|
| Query ID | e.g. Q-IEX-23 |
| Category | thematic category |
| Database | IEEE / ACM / Scopus / WoS / arXiv / SSRN |
| Search field | abstract / title-abstract-keyword / all-fields |
| Query string | the actual Boolean expression as run |
| Date run | YYYY-MM-DD |
| Hit count | raw |
| Notes | calibration findings, why revised, version, etc. |

### Step 5 — Calibration before commit

If a database appears not to have coverage, run a diagnostic calibration query before pivoting. Vibe Coding example: a diagnostic query returned 3 hits in ABI/Inform vs 110 in Scopus — a 37× differential that justified pivoting from ABI to Scopus and gave the methods chapter a documented basis for the choice.

### Step 6 — Coverage gap review

After the initial query set is run, deliberately list known gaps and decide whether they warrant new queries:

- Regulatory/compliance frameworks (sector-specific: GDPR, EU AI Act, CCPA, NIST etc.)
- Adversarial or attack terminology relevant to the domain
- Emerging vocabulary (e.g., "agentic," "vibe coding")
- Construct gaps (e.g., "overtrust" / "over-reliance" weren't in original queries)

Back-fill with targeted queries inside existing databases. Don't add a new database stream to fix a vocabulary gap.

### Step 7 — Saturation argument

Use the dedupe rate of the last database added as evidence of saturation. Vibe Coding: WoS added 116 unique records (35% of its yield) with 65% overlap against the existing corpus — sufficient to argue saturation in the methods chapter.

---

## 3. Zotero structure

Group library; collection-based provenance (NOT tag-based for source provenance).

```
<root>
├── Database Queries/                  ← per-source workspace
│   ├── IEEE Xplore/
│   │   ├── 00-Queue/                  ← (optional, see below)
│   │   ├── 01-Imports/                ← raw RIS imports, IMMUTABLE
│   │   │   ├── Q-IEX-01/
│   │   │   ├── Q-IEX-02/
│   │   │   └── ...
│   │   └── 02-Screening/              ← (was "Classification" — use "Screening" to match PRISMA)
│   │       ├── 00-Queue/              ← awaiting review
│   │       ├── 01-Keep/
│   │       ├── 02-Maybe/
│   │       └── 03-Discard/
│   ├── ACM Digital Library/           ← same shape
│   ├── SCOPUS/                        ← same shape; SCOPUS may also split 00-Queue into theme sub-collections
│   ├── Web of Science/
│   ├── arXiv/
│   └── SSRN/
├── Other Methods/                     ← PRISMA "other methods" streams
│   ├── Coursework/                    ← author-assembled prior reading
│   └── Practitioner Network/          ← prospectively documented grey lit
├── 00-Dups/                           ← manually curated cross-source duplicate registry
└── 04-Superseded/                     ← inferior duplicates after dedup (never delete)
```

### Hard rules

- **Items never leave `01-Imports/`**. Import membership is permanent provenance — same item can live in `Q-IEX-03` and `Q-IEX-12` and `Q-SCO-07` simultaneously; that's the audit trail.
- **Source counts are invariant** when moving items between screening buckets.
- **Always merge, never delete** for duplicates. Zotero's merge preserves all collection memberships and tags on the surviving record.
- **04-Superseded** holds the inferior duplicates after manual cross-source dedup (e.g., a preprint that was later published as a journal article — keep the journal version in the live workflow, send the preprint to Superseded).
- **Screening decisions propagate cross-source.** If the same item is in IEEE and Scopus and screened Keep in IEEE, the Scopus copy gets Keep too.
- **Tags are sorting/filtering aids only.** Source provenance lives in collections, not tags. `theme:*` and `s1:*` tags are screening aids; the screening decision in another source takes priority if there's a conflict.

### Publication venue hierarchy for dedup

When the same item exists across sources at different stages of publication:
```
journal > conference > preprint > thesis > webpage stub
```
Keep the highest in the live workflow, send the others to `04-Superseded`.

### Counting rules (read these before reporting any number)

- "How many papers" → unique top-level records, deduplicated by item key.
- "How many items" → may include child attachments and notes. Use `/items/top` to exclude those.
- "How many records this query returned" → raw per-collection count, may double-count.
- Parent collections return 0 from the API; the desktop client aggregates, the API does not. To count a subtree, enumerate leaves and union item keys.
- Per-collection sums double-count when items appear in multiple imports — work with sets of item keys.
- Cross-check first run against `Total-Results` header; a pagination bug (fixed April 2026) caused `prisma`/`review`/`dedupe` to silently truncate at 100 items.

---

## 4. Tools

### Reference manager

**Zotero (current version, 8.0.5 at last setup)** — justified by corpus scale (low thousands rather than tens of thousands), familiarity, and ability to run PRISMA workflow entirely in-tool. Rayyan is the alternative if the new project anticipates >several-thousand records after dedup; switch decision should be made up front, not mid-project.

### Zotero API access

- Group library — get the numeric group ID from the Zotero group settings page.
- Two API keys per project: read-only for ambient queries, read/write swapped in only for confirmed writes and swapped back immediately. Both kept in `~/.config/claude-zotero/.env`; the write key is excluded from any env template committed to a repo.
- Always re-fetch items immediately before `PATCH` — stale `version` causes 412 errors.
- File upload sequence: `POST` attachment metadata → `POST` to `/items/{att_key}/file` with `If-Match: {md5}` (not `If-None-Match: *`) → `POST` binary to S3 → `POST upload={uploadKey}` with `If-None-Match: *` to register (204 = success).
- API technical gotchas: `parentCollection: false` (not `None`) for top-level collections; the `Total-Results` header is lowercased in Python's `urllib`; use `format=keys` for fast set-intersection ops; the Zotero linter modifies item versions as a side effect, so post-write integrity checks (e.g., `Queue ∩ Keep == 0`) matter.

### Claude Code skills (installed at `~/.claude/skills/` on Mac and Faberix)

| Skill | Purpose | Dependencies |
|---|---|---|
| `zotero` | CLI wrapper around Zotero Web API | stdlib only |
| `zotero-slr-dedup` | Cross-source dedup with publication venue hierarchy + 04-Superseded workflow | stdlib only |
| `arxiv-zotero-import` | arXiv API search → Zotero import | stdlib only |
| `zotero-bulk-tagging` | Apply tags from collection membership; import screening CSVs; overlap reports | openpyxl |
| `claude-skill-installer` | Install skills from zips; idempotent | stdlib only |

Reinstall from share dir on Faberix:
```bash
python3 ~/.claude/skills/claude-skill-installer/scripts/install.py . --force
```

### Spreadsheet

`Query_Composition_and_Log.xlsx` — single workbook per project; one row per query; named ranges for tool lists; conditional formatting for hit counts that look anomalously small.

### Infrastructure

- macOS for primary work; VM for screening sessions.
- Faberix (Ubuntu workstation) for long-running AI batch screening jobs that need to survive a laptop closing. SSH from the macOS VM. Outputs land at `~/slr/<project>/`.
- Shared skill repo at `~/jukebox/scott/slr/claude-skills/` on Faberix.

---

## 5. AI-assisted screening workflow

This is the workflow that processed the SSRN 3,864 corpus and is the template to reuse.

### Setup

- Model: Claude Sonnet 4.6 via Claude Code CLI on a Max subscription. (Opus is overkill and was discarded for consistency partway through SSRN.)
- 30-second rate-limit-friendly pacing.
- Input CSV schema: `item_key, title, abstract`.
- Output CSV schema: `item_key, decision` (`keep` / `maybe` / `discard`, lowercase).
- 50 rows per batch. Fresh chat per batch with explicit history-isolation instruction. Row-count check before processing the next batch.

### Rubric pattern (Pass 1)

Tier the inclusion criteria so the model has clear anchors:

- **T1 (auto-keep)** — direct hits on the core RQ.
- **T2 (auto-keep)** — relevant supporting/contextual constructs.
- **Auto-keep triggers** — domain-specific terms that always warrant a keep regardless of other content (for Vibe Coding: human oversight, AI governance, code/software, EU AI Act, NIST AI RMF, organizational adoption, scalable oversight).
- **Default-to-keep**; maybe = thin abstract only.
- Output schema: `decision, confidence, rationale`; flag medium/names ambiguity.

For the media-metadata project, draft the T1/T2/auto-keep triggers up front with concrete vocabulary; this is the single biggest determinant of screening quality.

### Cross-model validation

Run a sample through GPT-4o and Gemini after non-SSRN screening completes. Same prompts as the primary run. Important gotcha: **Gemini Flash is not reliable for this workflow** — on the Vibe Coding run, 7 of 12 batches returned ~98% hallucinated `item_key` values; 341 of 600 Gemini decisions were unusable. Required mitigations:

- Item-key validation check after every batch (regex match against the input set).
- Re-prompt batches with high hallucination rates.
- Treat Gemini Flash as supplementary, not a primary validator. Prefer GPT-4o for cross-model validation.

### Standard exclusion rules (carry forward to all projects)

- Documents authored by the reviewer themselves → always Discard unless explicitly overridden.
- Course-platform URLs (Brightspace, Canvas, Blackboard pages) → always Discard. They aren't citable scholarly sources.
- Items in `04-Superseded` are not in scope for analytical queries.

---

## 6. Exclusion reason codes

Single primary reason per record — the first disqualifying factor. Apply consistently across analogous records.

| Code | Meaning |
|---|---|
| `out-of-scope` | doesn't address any of the inclusion criteria |
| `wrong-level` | technical-only, no organizational/human dimension (or vice versa, depending on RQ) |
| `wrong-type` | opinion piece without evidence base |
| `too-old` | pre-LLM era unless foundational theory (adjust for media metadata) |
| `duplicate` | content-duplicate of another record already in scope |
| `not-retrievable` | full text not obtainable after reasonable effort |
| `quality-threshold-not-met` | failed methodological-transparency check (preprints) or grey-lit quality criteria |

Author-specific exclusion rules go in the methods chapter alongside the codes:
- self-authored documents → Discard
- course-platform URLs → Discard

---

## 7. PRISMA reporting

### Identification streams (separate columns in flow diagram)

Each database its own column. "Other methods" streams (Coursework, Practitioner Network) as their own columns. Coursework enters at deduplication stage, not the search stage — these were already in hand before the formal search began.

### Per-stage counts to report

- Records identified (broken out by source)
- Records after deduplication
- Records screened at title/abstract
- Records excluded at title/abstract (counts per reason category)
- Full-text articles assessed
- Full-text excluded (specific reasons)
- Studies included in final synthesis

### Authoritative count pattern (avoid pagination bugs)

```
GET /groups/{id}/collections/{key}/items/top?limit=1
→ header: Total-Results: <N>
```

Cross-check at least one stage count against this header on first run. Any count hitting exactly 100 is suspect.

---

## 8. What to do first in a new project

A literal checklist to bootstrap the media-metadata SLR (or whatever's next):

1. **Write the research question(s) first.** Don't write queries yet. Use Thomas's framing principle: practice as primary framing, mechanism, and lever as separate questions; sub-RQs broad and not leading.
2. **Decompose RQ → thematic categories.** Six is the right ballpark.
3. **Draft inclusion/exclusion criteria** (PICO/SPIDER-style). Carry forward the two author-specific exclusion rules (self-authored, course-platform URLs).
4. **Choose databases.** Default set: IEEE, ACM, Scopus, WoS, arXiv. SSRN if the field has a lot of working papers. Add domain-specific databases if relevant (for media metadata: maybe LISA / Library & Information Science Abstracts, ACM, IEEE).
5. **Create the Zotero group and structure** exactly as in §3. Get the group ID; provision read-only and read/write API keys; populate `~/.config/claude-zotero/.env`.
6. **Create `Query_Composition_and_Log.xlsx`** with the column schema in §2 Step 4.
7. **Run a calibration query** in each database before locking the query set — one query per database with a known expected term, just to verify field syntax and confirm reasonable hit counts.
8. **Draft Pass 1 rubric** (T1 / T2 / auto-keep triggers) before any screening begins.
9. **Document the AI-use statement** in the methods skeleton up front — easier than retrofitting.
10. **Set up the Practitioner Network protocol prospectively** if grey lit will be a stream. Date the protocol. Don't backfill.

---

## 9. Open questions to confirm with the advisor for any new project

- Solo-coder vs second-screener requirement; spot-check sample size and agreement reporting.
- Publication requirement — is a conference paper acceptable for the publication-as-chapter pattern? What venues are appropriate for the new topic?
- Copyright transfer terms at the target venue and Purdue's manuscript-format dissertation policy on chapter reuse.
- IRB requirements for any empirical extension.

---

*Source documents this synthesizes: `SLR_Methodology_Suggestions_From_Chats.docx`, `Research_Question_Brainstorm.docx` (May 1 2026 meeting with Thomas), `Query_Composition_and_Log.xlsx`, project memory on the Vibe Coding Governance SLR, and the `zotero` skill SKILL.md.*
