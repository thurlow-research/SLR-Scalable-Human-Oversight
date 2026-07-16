# Verification Sampling — What to Look For

Two complementary samples, two different purposes, two different review modes. Do not conflate them.

---

## Sample 1: Trust Check (`trust_check.csv`)

**Purpose.** Pre-flight quality check before applying 3,952 decisions to Zotero. Answers "can I trust this enough to import?"

**Design.** Stratified by decision (20 keep / 20 discard / 20 maybe). Stratified so low-population categories (maybes) get equal attention to high-population ones (discards). NOT population-representative.

**Reading mode.** See everything together — AI decision, confidence, rationale, title, abstract. The point is to check whether the rationale matches what the abstract actually says.

**Time budget.** 20–30 minutes. ~30 seconds per item.

### What to look for, by category

**For each KEEP:**
- Does the rationale point to a concrete operationalizable contribution (measurement, mechanism, framework, detection signal, process)?
- Does the abstract actually contain what the rationale claims it contains?
- If the rationale invokes Tier 2 transferability ("framework generalizes to code review") — is the generalization claim plausible from the abstract?
- **Red flag:** rationale describes the paper accurately but the contribution is descriptive-only without an operationalizable angle. That's a Pass 2 rubric violation.

**For each DISCARD:**
- Is the discard reason consistent with one of the documented discard patterns (out-of-scope, wrong-level, wrong-type, descriptive-only, non-software domain, productivity-only)?
- Does the abstract actually fit the stated reason?
- Could a reasonable reader argue the paper IS in scope? If yes, that's a borderline call that should have been a Maybe.
- **Red flag (highest stakes):** abstract clearly discusses software/code/oversight AND has a methodology/measurement angle, but rationale dismisses on a thin pretext. False negatives in SLR are unrecoverable — these items disappear from your corpus.

**For each MAYBE:**
- Did the LLM articulate competing arguments for both keep and discard, or did it punt on a thin abstract?
- A legitimate Maybe has *two* opposing reasonable interpretations. A "I'm not sure" Maybe is rubric-violation — those should be keep-with-low-confidence or discard-with-low-confidence, not Maybe.
- **Red flag:** Maybe rationale is "abstract is too short to tell" — that's not a Maybe, that's a low-confidence call.

### Decision rule for whether to apply

Count items where you actively disagree with the AI's call (not just quibbles, real disagreements that would have flipped your decision).

| Disagreement count out of 60 | Action |
|---|---|
| 0–3 (≤5%) | Apply. The screening is trustworthy. |
| 4–9 (5–15%) | Apply, but **document the disagreement pattern** in your methods chapter and flag those item types for closer review at extraction. |
| 10–18 (15–30%) | Stop. Investigate disagreement patterns. Is one category (e.g., maybes) systematically miscategorized? Adjust rubric and re-screen the affected category. |
| 19+ (≥30%) | Do not apply. The screening is unreliable. Revisit Pass 2 design before re-running. |

**Document whatever you find for the methodology chapter.** Even a clean trust check (1 disagreement out of 60) becomes a defensible methods statement: "A stratified verification sample of 60 items (20 per decision category) was reviewed before applying decisions; agreement was N/60 (P%)."

---

## Sample 2: Methodology Validation (`validation_blind.csv` + `validation_key.csv`)

**Purpose.** Inter-rater reliability artifact for the methods chapter. Answers "what is the accuracy of this screening method?" defensibly enough to publish.

**Design.** Pure random N=100, no stratification. Population-representative — your sample will be ~25 keeps / 2 maybes / 73 discards, reflecting the corpus.

**Reading mode.** **BLINDED.** You see ONLY item_key, title, abstract, and three empty columns: `human_decision`, `human_confidence`, `human_rationale`. The AI's decision is in `validation_key.csv` which you do not open until your coding is complete.

This blinding is the entire methodological point. If you see "AI says discard" before reading the abstract, you anchor on that and your "verification" becomes rubber-stamping. Inter-rater reliability calculated against an unblinded reviewer is not inter-rater reliability — it is a confirmation bias measurement.

**Time budget.** ~2 hours total, ideally over multiple sittings to limit fatigue. ~70 seconds per item.

**Reading protocol (follow exactly):**

1. Close `validation_key.csv`. Do not open it. Move it to a separate folder if tempted.
2. For each row in `validation_blind.csv`:
   - Read the title and abstract.
   - Apply the same Pass 2 rubric the AI applied (operationalizability test, then Tier 1 / Tier 2 criteria).
   - Fill in `human_decision` (keep / maybe / discard).
   - Fill in `human_confidence` (high / medium / low).
   - Fill in `human_rationale` (one sentence, same format the AI uses).
3. Do **not** consult the AI decision until every row is coded. If you peek, the entire validation is compromised and you start over with a new random sample.
4. After coding all 100, merge with the key file (see the script's docstring for the one-liner) and calculate κ.

### What to look for during blind coding

You are not looking for AI errors. You are independently producing screening decisions from scratch, as if no AI had ever touched these items. The comparison happens later, separately.

That said, two things to note in your `human_rationale`:

- **When the abstract genuinely doesn't support a confident decision** — say so explicitly ("thin abstract, no methodology described"). This will matter when analyzing disagreements: if both you and the AI flagged low-confidence on the same items, that's strong evidence the items themselves are ambiguous rather than the screening being wrong.
- **When a decision pivots on a specific rubric tier** — name it. ("Discard: descriptive-only, no measurement method." "Keep: T1 direct hit on AI code risk quantification.") This makes post-hoc disagreement analysis tractable.

### Calculating agreement after merge

Once merged, you'll have a CSV with both `ai_decision` and `human_decision` columns. Compute:

- **Overall agreement rate** — simple percentage match
- **Cohen's κ** — agreement corrected for chance. >0.61 is "substantial," >0.81 is "almost perfect" (Landis & Koch 1977 thresholds, conventionally cited)
- **Per-category agreement** — confusion matrix of the 3×3 decisions
- **Confidence-stratified agreement** — does agreement increase with the AI's stated confidence? If yes, the confidence signal is calibrated. If no, the AI is overconfident.

A useful Python snippet for the methods chapter:

```python
import csv
from collections import Counter

rows = list(csv.DictReader(open('validation_merged.csv')))
ai_dec    = [r['ai_decision'].lower()    for r in rows]
human_dec = [r['human_decision'].lower() for r in rows]

# Agreement
n = len(rows)
agree = sum(1 for a, h in zip(ai_dec, human_dec) if a == h)
po = agree / n
print(f"Observed agreement (Po): {po:.3f} ({agree}/{n})")

# Expected agreement (by chance)
ai_counts    = Counter(ai_dec)
human_counts = Counter(human_dec)
pe = sum((ai_counts[c]/n) * (human_counts[c]/n) for c in set(ai_dec) | set(human_dec))
kappa = (po - pe) / (1 - pe) if pe < 1 else 0
print(f"Cohen's kappa: {kappa:.3f}")

# Confusion matrix
print("\nConfusion matrix (rows = human, cols = AI):")
cats = ['keep', 'maybe', 'discard']
print(f"{'':<10}" + "".join(f"{c:<10}" for c in cats))
for h in cats:
    row = [f"{h:<10}"] + [
        str(sum(1 for hd, ad in zip(human_dec, ai_dec) if hd == h and ad == a))
        for a in cats
    ]
    print("".join(f"{x:<10}" for x in row))
```

### Methods chapter language (drop-in template)

> Pass 2 screening decisions were validated via an independent blinded sample of 100 items drawn at random (seed=42, no stratification) from the 3,954-item Pass 2 corpus. The sample preserved the population distribution of decisions (~N% keep / N% maybe / N% discard). The author independently re-coded each item using only its title and abstract, with the AI's decision withheld until coding was complete. Agreement against the AI's decisions was Po=0.NNN, Cohen's κ=0.NN (NN% CI: [a, b]), constituting [substantial / almost perfect] agreement by Landis & Koch (1977) thresholds. Per-category agreement was N% for keep, N% for maybe, N% for discard. The full confusion matrix and disagreement analysis are reported in Appendix X.

Replace the N's with your actual numbers after the analysis.

---

## Why two samples

Trying to do both with one sample compromises both:

- The stratified trust-check design over-represents Maybes and under-represents Discards relative to the population, so κ from it would be biased toward the wrong distribution.
- The blinded validation design hides the AI's reasoning, which is exactly the thing the trust check needs to see.
- The trust check's goal is fast debugging; the validation's goal is defensible measurement. Different speeds, different tolerances for error.

The two samples are also independent — `seed` is used differently for each, so there will be minimal overlap by design. If a few items end up in both, that's fine; the validation's blinding still holds because you code it before consulting any AI decisions.

---

## Order of operations

1. **Today (before apply):** Run trust check. If it passes, apply decisions to Zotero. If it fails, stop and investigate.
2. **Within the next week (after apply, for methodology):** Run validation. Code blind. Merge. Calculate κ. Write it up.

Doing validation before apply is fine but pointless — the methodology artifact is about the screening decisions, not about the Zotero state. The screening decisions in `apply_all.csv` are stable once produced.
