# Restricted re-run — new vocabulary only (spec, drafted 2026-08-28)

**Status: PREP. All four design decisions RESOLVED 2026-08-28 (§7). Awaiting an explicit run authorisation.**

Implements closeout **F2** / §41: apply the post-freeze vocabulary to the surviving corpus **without
re-adjudicating anything already settled**.

---

## 1. Design decision — restricted OUTPUT, discriminative CONTEXT

Scott's question: *"Do we have revised instructions but ignore anything that isn't a new tag? Or
restrict instructions to the new tags only?"*

**Neither works alone.**

**Restricting the instructions to the new slugs fails**, because **every new slug is defined by a
boundary against an existing one**:

| New slug | Cannot be applied without knowing |
|---|---|
| `agent-panel` | division of labour · relay · advisory aggregation |
| `cross-model` | comparison · task allocation · a single specialist critic |
| `evaluated-real-data` | `method-mining` (and it **entails** `built-system`) |
| `scaling-dissent` | `risk-routing` — the paper's thesis vs dissent from it |
| inversion **v2** | inversion **v1** + the §88 leakage test |
| `survey-input-v2` | `method-self-report` — instrument type **and** what it elicits |
| `rules-based-checks-v2` | `ai-review` — **who produces the verdict**, code or a model |

Strip the contrast class and the panel over-applies — which is the error corrected **five times** in
the Accept band (§110, §112a, §130b, §132a, §135c) and **four times** on `cross-model` (§122, §124d,
§125d, §126c).

**Running the full revised instrument also fails:** it pays for 44 slugs to use 10, and it invites the
panel to re-read the old vocabulary under revised wording — the re-adjudication Scott ruled out.

**Adopted: a focused prompt whose OUTPUT SCHEMA admits only the new slugs**, but whose **context
includes, per slug, the neighbours it must be distinguished from, the discriminator test, and the
worked positive/negative cases from the Accept band.** Old tags are unreachable by construction, not
by instruction.

---

## 2. Population

**72 papers · TXT available for all 72.**

- **68 kept** — `cal:human:primary:theme:*` present and **no** `demote:context`
- **4 remaining** — `MFSZPSPU` Shi · `GAD5Z8PV` Vargas · `I6FZ5GD2` Wang (Junpeng) ·
  `CTGGMIX9` Wang (Kai)

**Excluded: all `demote:context` papers** — **CORE ONLY**, confirmed by the arbiter (D3). §42
short-circuits tag verification at Context tier, and `final:*` is computed from the surviving set only.
The 4 remaining are included because they are undispositioned; if any later demotes, its v2 proposals
are simply not carried into `final:*`.

---

## 3. Slugs in scope (10)

Five are already in hand-applied use; the panel has **never** seen any of them, all being post-freeze.
**`evaluated-self-demo` was DROPPED** (arbiter, 2026-08-28) — see §7 D1.

| Slug | Hand-applied so far | Reference case |
|---|---|---|
| `agent-panel` | 7 | **Ullah `A6ZE2A26`** (§140a) |
| `cross-model` | 5 | **Ullah `A6ZE2A26`** (§140a) |
| `evaluator-reliability` | 11 | Karakaya `5NZ2EDEK`, Ullah |
| `evaluated-synthetic` | 10 | §34/§35 gold set |
| `evaluated-benchmark` | 9 | §34/§35 gold set · §119b |
| `evaluated-real-data` | **0** | definition settled F2a; **no instance yet** |
| `scaling-dissent` | **0** | replaces deprecated `counterpoint` (§56) |
| `oversight-scaling-inversion-v2` | **0** | own slug — must NOT reuse v1 (§10.12) |
| **`survey-input-v2`** | **0** | revised §116a+§121b+§124f — **v2 slug, v1 untouched** |
| **`rules-based-checks-v2`** | **0** | revised §139a determinism rule — **v2 slug, v1 untouched** |

---

## 4. Per-slug prompt content

### `agent-panel`
**Fires when:** multiple agents answer **the same question** about the same artifact, and their
outputs are aggregated by an explicit rule (vote, consensus, unanimity). **Redundancy, not
specialisation.**
**Discriminator (§110):** *"loses a job or loses a vote?"* Remove one agent — if **coverage**
disappears it is division of labour; if a **vote** disappears it is a panel.
**Positive:** Ullah `A6ZE2A26` — unanimous committees of 1–6 judges on the same SQL query.
**Negatives:** Nimraka `5RKMGRNA` (parallel specialists, distinct categories) · David `6NTZ85CW` ·
Dutta `399HN438` · P `N7E3MR2V` (PM/coordination functions) · Rasheed `DJHG9BBS` (**relay** —
sequential, each consuming the prior's output).
**Warning:** *"multi-agent"* in a title or abstract **predicts nothing**. Five distinct topologies in
this corpus all use the phrase.

### `cross-model`
**Fires when:** **distinct models** check the same artifact so that their **errors can differ** —
mutual checking, not merely more than one model being present.
**Negatives:** Karakaya `5NZ2EDEK` (models **compared** as judges) · Lipsanen `7SH86C2W` (**task
allocation** — Codex implements, Claude does non-functional requirements) · McAleese `NRVQT89E`
(**one** fine-tuned critic in a checking role) · Liu `9H6FWJME` (five tools studied, none checking
another).
**Positive:** Ullah — committees composed of distinct models, **composition measured as a variable**.

### `evaluated-real-data`
**Definition (Scott, F2a):** *"a **tool is developed** and that tool is **evaluated using real data**.
Tool could be a pipeline. In mining, pre-existing data is mined for insights. **No new tool is being
evaluated**."*
**Entailment to enforce: `evaluated-real-data` ⇒ `built-system`.** If nothing was built, it cannot fire.
**Negative:** Liu `9H6FWJME` — 302.6k real commits but **pure mining**, no tool (§125d).
**Candidate positives:** Minh `74GE3TF7` · Karakaya `5NZ2EDEK` · Liu `6ZC3H7AF` · Lipsanen `7SH86C2W`.

### `scaling-dissent`
**Fires when:** the paper argues delegation of oversight is **unworkable or impermissible as a general
matter**.
**Does NOT fire when** the paper reports that *a particular* delegation is unreliable — that is **the
review's thesis**, not dissent from it.
**§56 polarity trap:** `counterpoint` was deprecated because the panel tagged a thesis-**supporting**
paper as opposition **9/9**. **First human-side instance: §122b** (Karakaya). Assume the trap is live.
**Negatives:** Karakaya `5NZ2EDEK` · Lipsanen `7SH86C2W`.

### `oversight-scaling-inversion-v2`
**Leads with the leakage test (§88).** Two satisfaction routes (§117d):
(i) **observed review absence**; (ii) **defects measurably present in MERGED code with review failure
as the cause**.
**Explicitly insufficient:** maintainer burden · queue growth · falling throughput · displaced work.
**Two failure modes found in the Accept band, both at 3/3 — screen for them:**
- **§123a — volume-for-leakage substitution.** AIDev: agent PRs *accepted less often*, yet the panel
  inferred inversion from the 3-days-vs-3-years volume figure. **Pressure is not leakage.**
- **§127b — population mismatch.** Minh: 28.3% merge instantly (absence) but those are the *trivial*
  PRs, while the overload symptom is *ghosting*, and ghosted PRs never merge. **Absence and overload
  must fall on the SAME population.**
**Run v1 and v2 as separate slugs** so the reclassification delta is a reportable measurement
(§10.12).

### `survey-input-v2`  *(v1 tags remain untouched)*
**Both conditions must hold — they are CONJUNCTIVE (§131d isolated them):**
1. **§116a instrument test** — an actual **survey instrument** exists (Likert-type / structured
   questionnaire). Semi-structured interviews alone **fail** this.
2. **§121b elicitation test** — the instrument elicits **stated preferences, adoption or priorities**.
   An instrument measuring a **construct or performance** (cognitive load, engagement, comprehension,
   satisfaction, demographics) is **`method-self-report` only**.

**Explicitly NOT criteria — both were proposed and withdrawn (§121b, §124f):**
- **Centrality** — the survey need not be the paper's main method.
- **Usefulness to us** — *"it will yield questions for our survey"* is not a criterion; question-seeding
  is unconstrained by source, so it cannot discriminate.

**Positives:** Kang `7UB2MD8Z` (*"70% agreed"* explanations were wanted — stated preference) · Salem
`5Q4G4CQB` (five-point Likert on attitudes).
**Negatives:** Catalan `5BAZZWHG` (Likert exists, but measures **cognitive engagement** — a construct) ·
Omidvar-Tehrani `4FGIVVTG` (**passes** elicitation, **fails** the instrument test — interviews) ·
mined-data papers with no instrument at all (the original §116a case).
**Note:** `survey-input-v2` and `method-self-report` **co-occur freely** — different axes.

### `rules-based-checks-v2`  *(v1 tags remain untouched)*
**Fires only when the EVALUATION is deterministic** — the verdict is **computed, reproducible, and
independent of a model's judgement**.
**Arbiter's rule (§139a):** ***"Rubrics that are LLM evaluated are not rules-based-checks."*** The theme
names **how the verdict is produced**, not how the criteria are written. **Rule-shaped criteria scored
by a model are `ai-review`**, however explicit the rubric.

**Positives:** Parris `3SU9QZ6F` (15 deterministic checks) · Töpfer `72W6R4JG` (FCL constraint
verifier) · Xie `T8E8SCCG` (VibeGuard security gate) · Zhong `96XE669R` (30 deterministic verifiers) ·
Lipsanen `7SH86C2W` (executable acceptance tests, pass/fail).
**Negatives:** Sollenberger `GCZQTNBD` (LLM judge) · Raghavendra `8VBH957K` (LLM-scored rubrics) ·
Sun `V4IRKSFI` (**both** stages are fine-tuned LLMs — *"RuleChecker"* is a **name**, not a mechanism).
**Trap:** do not tag from the component's name. Check what computes the verdict.
**Known hybrid — flag, do not force:** Jin `A5WDGC7J` — deterministic test **execution** over
**GPT-4o-generated** tests. Verdict computed, criteria model-authored. Emit the flag and let the
arbiter rule; F2 has not settled hybrids.

### `evaluator-reliability` · `evaluated-synthetic` · `evaluated-benchmark`
Carry the §34/§35 wording unchanged. `evaluated-benchmark` = measuring **against** a recognised
third-party benchmark **run as-is** (§119b, §34) — not contributing one, and not author-curated
material sourced from a well-known pool.

---

## 5. Output contract and guardrails

- **Schema admits the 10 slugs only.** Any other slug in output = a validation failure, not a proposal.
- **Write to `cal:<model>:*` in the normal namespace**, per-vendor, k=3 as usual.
- **Never touch `cal:human:*`.** Where a slug is already hand-applied (42 instances across 5 slugs),
  the panel proposal is **independent evidence**, not an overwrite. Agreement/disagreement with the
  arbiter on the new slugs is a **calibration signal for the new definitions** and should be reported.
- **No demote flags.** Tier is settled for this population.
- **Record as a new measurement point (T2).** `tag_layer_stats.py` must be fixed first — see closeout
  **D1** (band mis-scoping) — or T2 inherits T0/T1's defects.

---

## 6. Interaction with closeout B2 / B10

Running `survey-input-v2` and `rules-based-checks-v2` **changes what those items are**, and for the
better. B2 (≈10 silent-modal `survey-input`) and B10 (24 papers carrying `rules-based-checks`) were
planned as **blind human re-checks**. With v2 panel proposals in hand they become **supervised**
adjudications — the arbiter rules with a proposal in view, as everywhere else in the project, rather
than re-reading cold.

**Update B2 and B10 to depend on this run**, and note the epistemic change: they are no longer
independent of the panel.

---

## 7. DECISIONS — all resolved 2026-08-28

| | Question | Ruling |
|---|---|---|
| **D1** | Coin `evaluated-self-demo`? | **NO — dropped.** *"Delete self-demo."* The ladder gap stands unmarked; `built-system` continues to cover "it exists" with no rung below it. |
| **D2** | Re-run revised existing definitions? | **YES — but as v2 slugs.** *"Run revised but we have to have new 'v2' tags so we don't zap the previous tags."* Same principle as inversion v2: v1 stays, and the **reclassification delta becomes a reportable measurement** instead of being destroyed. |
| **D3** | Population | **CORE ONLY.** Demoted papers excluded. |
| **D4** | Panel composition | **Confirmed** — 3 vendors × k=3 = 9 runs/paper × 72 papers. **Fable excluded** (uniform composition; built for a tiebreaker protocol that was dropped). |

**Still blocking the run:** `slr-tools/tag_layer_stats.py` must be fixed first (closeout **D1 tooling**
— band mis-scoping, wrong source for calibration, mislabelled blind arm) or the **T2** measurement
point inherits the T0/T1 defects.

**Nothing runs without an explicit authorisation.**
