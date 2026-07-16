# Stage 3 Cross-Model + Human QA — Protocol

Verifies the Opus Stage-3 triage (200 core / 643 context / 140 discard) against two
independent model legs and a blinded human check, then computes agreement before any
`s3:*` tag is written to Zotero.

**Sample (seed 20260706, stratified random over 976 primaries):**

| Sample | n | core | context | discard | Given to |
|---|---|---|---|---|---|
| Model set | 250 | 50 | 164 | 36 | Gemini **Advanced** + ChatGPT Pro (same 250) |
| Human set | 50 | 10 | 33 | 7 | You (blinded) — a subset of the 250 |

All input files are **blinded**: no Opus verdict; authors withheld from the model files
(the rubric is deliberately author-blind). Opus verdicts live only in `qa_master_250.csv`
(the scoring key — never paste it into a chat).

Files:
- `gemini_chunks/chunk_00..09.csv`, `chatgpt_chunks/chunk_00..09.csv` — 10 chunks of 25.
- `gemini_input_250.csv` / `chatgpt_input_250.csv` — the full 250 (record copy).
- `human_review_50.csv` — fill `bin` / `centrality` / `reason_code` / `rationale` yourself.

---

## Model legs — fresh chat PER chunk

Run **Gemini Advanced** and **ChatGPT Pro** separately. **Never use Gemini Flash**
(it hallucinated ~98% of item keys in the prior pass). One fresh chat per chunk keeps
histories isolated and holds key-hallucination down. Paste the block below, then paste
the chunk's CSV rows underneath it.

> **PROMPT (paste, then paste the chunk CSV rows after "ITEMS TO SCREEN:")**
>
> [paste the full contents of `_rubric.txt` here]
>
> The rows below are CSV with header `seq,item_key,title,year,item_type,abstract`
> (plus empty verdict columns — ignore those). Screen every row. Echo `item_key`
> EXACTLY. Return ONLY the JSON array specified above — no prose, no code fences.
>
> ITEMS TO SCREEN:
> [paste chunk_NN.csv rows]

After each chunk: save the JSON to `gemini_out/chunk_NN.json` (resp. `chatgpt_out/`).
Spot-check that every `item_key` returned matches one you sent — if any key is invented
or missing, re-run that chunk in a new chat (the scorer flags this automatically too).

## Human leg — 50 items, blinded

Open `human_review_50.csv`, apply the same rubric from your own judgment (authors are
shown here; the AI legs did not see them), and fill in `bin` + `centrality` +
`reason_code` (discard only) + a one-line `rationale`. Don't consult the Opus call while
judging — the point is an independent reference.

---

## Scoring (after all three legs return)

`python stage3_qa_score.py --outdir work` will:
1. Validate item keys per leg (drop/flag hallucinated or missing keys).
2. **Trust Check (gate):** Opus vs human on the 50 — Cohen's κ on the 3-way bin +
   confusion matrix; any human↔Opus core/discard *crossovers* (a real FN/FP) block
   auto-apply and go to manual adjudication.
3. **Cross-model:** pairwise κ (Opus/Gemini/ChatGPT) on the shared 250 (3-way bin),
   plus Spearman rank correlation on centrality (this is an ordinal pass).
4. Emit `qa/adjudicate.csv` = every item where the three model legs disagree on bin,
   plus the Context↔Discard border band — the only items needing a human decision.

Auto-classify where the legs agree; human-review only the disagreements + border band.
Only after the gate passes: back up the Zotero library (File → Export Library), swap in
the write key, apply `s3:*` tags, swap back to read-only.
