# Restricted re-run — new vocabulary only (spec, drafted 2026-08-28)

**Status: PREP ONLY. Not authorised to run.** Four decisions below need Scott's call first.

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
| `evaluated-self-demo` | `built-system` · `design-only` |
| `scaling-dissent` | `risk-routing` — the paper's thesis vs dissent from it |
| inversion **v2** | inversion **v1** + the §88 leakage test |

Strip the contrast class and the panel over-applies — which is the error corrected **five times** in
the Accept band (§110, §112a, §130b, §132a, §135c) and **four times** on `cross-model` (§122, §124d,
§125d, §126c).

**Running the full revised instrument also fails:** it pays for 44 slugs to use 9, and it invites the
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

**Excluded:** all `demote:context` papers (§42 short-circuits tag verification at Context tier).
**Decision D3 below** asks whether that exclusion should hold.

---

## 3. Slugs in scope (9)

Five are already in hand-applied use; the panel has **never** seen any of them, all being post-freeze.

| Slug | Hand-applied so far | Reference case |
|---|---|---|
| `agent-panel` | 7 | **Ullah `A6ZE2A26`** (§140a) |
| `cross-model` | 5 | **Ullah `A6ZE2A26`** (§140a) |
| `evaluator-reliability` | 11 | Karakaya `5NZ2EDEK`, Ullah |
| `evaluated-synthetic` | 10 | §34/§35 gold set |
| `evaluated-benchmark` | 9 | §34/§35 gold set · §119b |
| `evaluated-real-data` | **0** | definition settled F2a; **no instance yet** |
| `evaluated-self-demo` | **0** | proposed §124d; **not yet coined** — see **D2** |
| `scaling-dissent` | **0** | replaces deprecated `counterpoint` (§56) |
| `oversight-scaling-inversion-v2` | **0** | own slug — must NOT reuse v1 (§10.12) |

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

### `evaluated-self-demo` — **pending D2**
**Fires when:** the **proposers** evaluate their **own artifact** on a case **they constructed**, with
no external subjects, no benchmark and no ground truth.
**Grades below `built-system`:** built-system says the thing exists; this says the only evidence is its
authors' own judgement.
**Candidates:** Lipsanen `7SH86C2W` (3-arm qualitative self-assessment) · Nimraka `5RKMGRNA` (unit
tests pass) · Rasheed `DJHG9BBS` (narrative prose, no numbers — the floor).

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

### `evaluator-reliability` · `evaluated-synthetic` · `evaluated-benchmark`
Carry the §34/§35 wording unchanged. `evaluated-benchmark` = measuring **against** a recognised
third-party benchmark **run as-is** (§119b, §34) — not contributing one, and not author-curated
material sourced from a well-known pool.

---

## 5. Output contract and guardrails

- **Schema admits the 9 slugs only.** Any other slug in output = a validation failure, not a proposal.
- **Write to `cal:<model>:*` in the normal namespace**, per-vendor, k=3 as usual.
- **Never touch `cal:human:*`.** Where a slug is already hand-applied (42 instances across 5 slugs),
  the panel proposal is **independent evidence**, not an overwrite. Agreement/disagreement with the
  arbiter on the new slugs is a **calibration signal for the new definitions** and should be reported.
- **No demote flags.** Tier is settled for this population.
- **Record as a new measurement point (T2).** `tag_layer_stats.py` must be fixed first — see closeout
  **D1** (band mis-scoping) — or T2 inherits T0/T1's defects.

---

## 6. DECISIONS NEEDED BEFORE RUNNING

**D1 — Is `evaluated-self-demo` coined?** It has no instance and was deliberately not established on a
demoted paper (§122f, §124d). Either coin it now with Lipsanen as the seed, or drop it from this run
and leave the ladder with the gap.

**D2 — Do revised EXISTING definitions get re-run?** Two changed materially this session:
- **`survey-input`** — §116a instrument requirement + §121b elicitation test + §124f (utility is not a
  criterion). Closeout **B2** currently plans a *human* re-check of ~10 silent modals.
- **`rules-based-checks`** — §139a determinism rule. Closeout **B10** plans a *human* re-check of 24
  papers.
Re-running either is **re-adjudication of an existing tag**, which Scott ruled out — but both
definitions genuinely changed. **Recommend: keep both as human re-checks (B2/B10), exclude from this
run.** Cheaper, and it preserves the no-re-adjudication rule.

**D3 — Population: kept only, or kept + Context?** Currently kept-only (68 + 4). Context papers were
excluded under §42. But several new slugs are *evidence-grade* facets whose whole purpose is grading
weak work — and the clearest `evaluated-self-demo` candidates (Nimraka, Rasheed) are **demoted**.
**Recommend: kept-only for `final:*`**, with a **separate, cheap Context pass** if the ladder rungs are
wanted for the methods chapter.

**D4 — Panel composition.** Standard 3 vendors × k=3 = 9 runs × 72 papers. Fable stays **excluded**
(§C7 — uniform composition; it was built for a tiebreaker protocol that was dropped). Confirm.
