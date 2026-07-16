# Stage 3 — Relevance Triage (983 → Core / Context / Discard)

Reduces the 983-item eligible pool toward the two-tier extraction corpus. Abstract-only,
no PDFs. Claude/Opus is the first of three model legs (ChatGPT Pro + Gemini Advanced follow
for cross-model QA). AI is a consistency tool — final scholarly judgment stays human.

## Prereqs
- venv with deps: `/Users/scott/Code/slr-tools/venv` (already has stdlib-only build; screen needs the `claude` CLI on PATH)
- Zotero **read-only** creds in env (direnv from the project dir) or the script auto-reads the project `.envrc`
- `claude` CLI logged in (Max). Screening uses no tools, so no permission prompts.

## Run order

```
cd /Users/scott/Code/slr-tools/stage3
PY=/Users/scott/Code/slr-tools/venv/bin/python

# 1. Build inputs (read-only Zotero pull + enrich + batch split). Re-runnable.
$PY stage3_build_input.py --outdir work

# 2. SELF-TEST / CALIBRATION — run ONE batch live first (≈20 items).
#    Confirms the `claude -p` invocation works AND lets you eyeball Opus's
#    bins/rationales against the rubric before committing to all 49.
$PY stage3_screen.py --outdir work --model opus run --batch 0
#    -> inspect work/batch_000_out.csv. If the invocation or rubric needs a
#       tweak, edit call_model() / RUBRIC in stage3_screen.py and re-run.
#       (delete work/batch_000_out.csv + its checkpoint entry to redo it.)

# 3. Full run (resumable — re-run after any interruption; only pending batches execute).
$PY stage3_screen.py --outdir work --model opus run

# 4. Consolidate -> work/stage3_results.csv (verdicts + title/authors/fetch worklist),
#    propagates each primary's decision to its flagged duplicates, prints bin counts
#    and how many CORE items still need fetching.
$PY stage3_screen.py --outdir work consolidate
```

## Outputs
- `work/stage3_input.csv` — one row per item, full metadata (join key `item_key`)
- `work/batches/batch_NNN.csv` — model inputs (primaries only; dups inherit)
- `work/batch_NNN_out.csv` — per-batch verdicts
- `work/stage3_results.csv` — **the deliverable**: sorted by centrality, with
  `bin, centrality, reason_code, rationale` + `title, authors, year, source, has_pdf,
  doi, arxiv_id, retrieval_route, is_primary, dup_group`. This is your review sheet
  and your Stage-4 fetch worklist (filter `bin==core & has_pdf==no & is_primary==yes`).

## After the Opus run (cross-model QA + verification)
1. Re-use `batches/` to run the **ChatGPT Pro** and **Gemini Advanced** legs (fresh chat
   per batch, history isolation, item-key validation each batch — Gemini **Advanced only**).
2. Merge the three legs; auto-classify on agreement, route disagreements + the
   Context↔Discard border band to **human review**.
3. Verification samples (same as prior passes): stratified **Trust Check** (gate) +
   blinded **N=100 Cohen's κ**; for this ordinal pass also report inter-model rank correlation.
4. Only then apply `s3:*` tags to Zotero — after a library backup + write-key authorization.

## Notes
- `call_model()` in `stage3_screen.py` isolates the CLI call — adjust if your invocation
  differs (e.g. `--model claude-opus-4-8` if the `opus` alias doesn't resolve).
- Billing: programmatic Claude Code may draw from a separate pool at API rates — check
  `/usage` before the full 49-batch run.
- 7 items have no abstract; the rubric routes those to the human-review band.
