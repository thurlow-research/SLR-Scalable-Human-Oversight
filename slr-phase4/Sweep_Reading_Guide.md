# Sweep Reading Guide — Phase 5 Reading Collections

**Who this is for:** the arbiter (Scott), reading in Zotero, working the 128-core sweep results.
**Companions:** `data/tags-v213/sweep_review_workbook.md` (per-paper proposals + votes) ·
`Tag_Cheatsheet.md` (the instrument) · changelog §19–§32 (binding rulings — do not re-litigate).

The collections map to effort tiers — spend attention where the machines couldn't resolve:

| Collection | n | Machine state | Your job |
|---|---|---|---|
| 01 - Accept | 44 | 3/3 consensus | Audit 4 designated papers; rest optional spot-checks |
| 02 - Light Read | 78 | 2/1 modal proposal + tripwires | Confirm or flip; ~2–5 min each |
| 03 - Full Read | 6 | replication-stable 3-way split | Full adjudication (ZUM76CCG treatment) |

---

## 1. How to record results (the mechanics)

**Default = silence-is-confirmation, with an explicit "I read it" marker.** Only deltas cost
keystrokes.

1. **Every paper you finish:** add tag **`s5:read`** (type it once; it autocompletes after the
   first use). This is the progress marker — without it we can't distinguish "reviewed, agreed"
   from "not yet reviewed."
2. **You agree with the workbook proposal** (primary + themes + 3/3 facets + flags): add
   `s5:read` and nothing else. The write pass will apply the machine proposal as-is.
3. **You disagree on anything:** use the Actions-menu toggles (the same `cal:human:*` menu from
   calibration) to record *your* ruling — your primary, your theme set, your facets. On sweep
   items, any `cal:human:*` tag is read as an **arbiter override** that beats the machine
   proposal wholesale for that layer (if you set any `cal:human:theme:*`, your theme set is THE
   theme set; same per layer for primary/facets). Partial overrides are fine (e.g., fix only the
   primary).
4. **Demote proposals** (bucket B especially): if you **confirm** the demote, toggle
   `demote:context` on the item. If you **reject** it (paper stays core), just `s5:read` with no
   demote tag — after `s5:read`, absence of the demote tag is an explicit keep-core ruling.
5. **Rationale notes** (optional but valuable on Full Reads and any override): add a child note
   starting with "**arbiter:**" — one or two sentences on which rule fired. These become the
   changelog/§7-style audit trail.
6. **New-tag instincts:** if a paper makes you want a tag that doesn't exist, do NOT improvise a
   slug — note it in a child note ("candidate: <idea>"). Staged candidates with armed tripwires
   already exist for `evaluated-benchmark` and the `risk-quantification` family.
7. **Dissertation/survey capture (any bucket):** `dissertation-input` (with its required child
   note naming the dissertation question) and `survey-input` are yours to apply on sight.

**Ops cautions (standing):** the Actions-menu self-select hazard — scrolling can silently toggle
the focused item; I run post-paper server-side verification, but glance at the tag list before
you move on. Client↔server sync lag: sync before and after a session. Nothing you tag is
written onward to plain `theme:` tags until you approve the write plan — your tags are the
ruling layer, not the final vocabulary.

---

## 2. What to look for — universal checklist (all buckets)

Read against the instrument, not your general judgment — the recurring catches:

- **Membership, not mention.** Does the paper *contribute to* each proposed theme's argument, or
  just mention it? Vision-paper floor: one scenario sentence = mention.
- **Steering exclusion.** Anything shaping *generation* (prompts, specs, fine-tuning, input
  control) is not oversight. A solution that improves the code rather than gating it earns
  `steering`, and steering-only → demote candidate.
- **Plumbing rule.** Systems papers: tag only mechanisms the paper *argues about*, not
  everything its system uses.
- **The §32 altitude precedent** (expect it constantly — 4 of the 6 Full Reads have
  org-governance in the votes): use-case/deployment-granularity classification prescribing
  oversight *regimes* = `org-governance`; `risk-routing` needs artifact-granularity selection
  driven by a computed, producer-independent signal.
- **Mention-vs-focal at paragraph length** (the ZUM76CCG lesson — this is the sweep's known
  seductive error): a dedicated *paragraph* on a risk still isn't a risk flag unless a bar
  clause fires (metric / mitigation / empirical result / focal analysis). Ask "which clause
  fired?" — if you can't name it, no flag.
- **Primary tie-breakers:** distinctive novelty over standard scaffolding; most specific theme
  that still captures the main effort; a component doesn't outrank the broader contribution.
- **Struggle signal:** if you can't pick a primary or you're stretching a definition, the paper
  probably doesn't belong at core — `demote:context` and move on. Don't force tags to justify a
  disposition.
- **Seven-question facet sweep** before leaving any paper you're overriding: role / form /
  scope / mode / contribution / risk-types / method. (Misses cluster in facets — 45 toggles
  exceed recall.)

## 3. Bucket-specific protocol and questions

### 03 - Full Read (6 papers — start here, freshest attention)
Genuine three-way splits; each model's *stable* modal read differs. For each:
- Workbook shows all three primaries. Ask: (a) which theme carries the paper's **distinctive
  novelty**? (b) is this an **altitude** disagreement (§32 territory: org apparatus vs specific
  mechanism) or a **genre** disagreement (framework vs empirical vs review)? (c) does the
  lit-review biggest-tent override apply?
- Rule the full record (primary, themes, facets, flags) via the menu + an "arbiter:" note.
  These six are precedent-setters like ZUM76CCG was — your rationale sentences matter more here
  than anywhere.
- Papers: 8AW26GFK · HBR7QZ2C · S7FPFUT8 · VCI88UZD · WRXR2VTP · Y4TIF9KW.

### 02 - Light Read (78 papers)
Machine gives a 2/1 modal proposal + tripwires telling you where to look.
- **The 18 unanimous-demote papers first** (workbook bucket B) — fastest wins. Question per
  paper: does a demote-menu reason actually hold (general-AI object · steering-only · pure tool
  benchmark · secondary lit · not operationalizable)? Remember `general-code` alone is NOT a
  demote reason, and §30's sole-exemplar exception is "look at keeping," not "keep."
- For the rest: read abstract + skim the sections the tripwires point at
  (`sprawl:codex=9` → check for theme-stuffing; `unstable:<model>` → boundary paper, check the
  dissent before confirming the majority). Confirm (silence) or override (menu).
- Codex sprawl signature: when codex is the dissent with 8–10 themes, the majority is usually
  right — but check whether one of codex's extras is a genuine miss by the other two.

### 01 - Accept (44 papers)
- **Mandatory:** the 4 audit papers — 4T5QFWZE · 5NZ2EDEK · CTGGMIX9 · D87A4CAS. Full-record
  check as if they were Light Reads. A miss here impeaches the whole ACCEPT band (then we widen
  the audit) — so be adversarial: try to *refute* the consensus, don't just nod.
- Everything else: read for content (you're reading them for the synthesis anyway); `s5:read`
  when done; override only if something jumps out. Consensus being unanimous is evidence, not
  proof — you remain the gauge.

## 4. Questions to hold across the whole read (synthesis capture)

While you're in the papers anyway, keep a running note (child notes or one master note) on:
1. **Risk×mitigation matrix cells** — which risk types does each solution paper actually
   mitigate? (Gap cells — risks identified but unmitigated — are Discussion gold.)
2. **Effectiveness evidence** (`dissertation-input` radar): anything showing oversight *quality*
   is a manipulable design variable (forcing functions, review-intensity effects), not just
   scalable/cheap.
3. **Insufficiency-layer additions**: new evidence that current practice doesn't close the gap.
4. **`problem-statement-anchor` candidates**: committee-sit-up stats anchoring the OVERALL
   inversion (never on lit-reviews).
5. **Counterpoints**: papers arguing against prevailing positions — note what they oppose.
6. **Adopted-in-production sightings** (`adopted` is scarce and high-signal — pilot rule:
   study-site ≠ adoption).

## 5. When you're done (or per sitting)

Tell me (or leave it to the standing protocol) and I will: verify your tags server-side against
the self-select hazard, diff your rulings vs the machine proposals, compute the human-delta rate
(the sweep's headline QA number), draft the write plan (backup → `apply_s4_tags.py` + plain
`theme:`/facet slugs per your rulings → verify), and queue the demote batch for the tier moves.
