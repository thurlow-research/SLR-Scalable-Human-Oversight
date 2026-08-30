# Article 2 — citations for `Article 2.docx`

Prepared 2026-08-29. All metadata verified against the live Zotero library and, where the paper is
published, against the published version. Zotero item keys given so you can insert from the library
directly.

---

## ⚠ Read first — four issues found while mapping claims to sources

**1. The Critique row conflates two different papers into one system.** It currently reads:

> *"A ByteDance production system used this method to improve precision to 75%, reducing false
> positives from 88.7% to 40.0% by validating against executable evidence rather than another model's
> opinion."*

Those are **two unrelated systems**. The 75% precision and the ByteDance deployment are **Sun et al.
(2025)** — BitsAI-CR. The 88.7% → 40.0% false-positive reduction and the executable-evidence validation
are **Jin & Chen (2026)**, a different paper about LLM judges over-correcting. As written it attributes
Jin's result to ByteDance. Suggested split:

> *"A ByteDance production system used this approach to reach 75% precision at 12,000+ weekly active
> users (Sun et al., 2025). Separately, a verification filter that validated model verdicts against
> executable evidence — rather than a second model's opinion — cut a false-positive rate from 88.7% to
> 40.0% (Jin & Chen, 2026)."*

**2. "I started with a Multivocal Literature Review (MLR)" — this isn't accurate**, and your own
methodology says the opposite. `Selection_Criteria_By_Phase.md` records grey literature as **generally
EXCLUDED** (blogs, vendor posts, docs), and the retained corpus is 40 preprints, 20 conference papers,
10 journal articles and **2 grey items**. An MLR *deliberately searches* grey channels; you searched
five academic databases plus snowball. Also note the docx says *"Most were peer-reviewed or preprints;
some were industry reports"* — that phrasing is fine, but the MLR label above it isn't. Suggested:
*"a systematic literature review"*, with the preprint proportion stated as the notable methodological
choice.

**3. The Deterministic Orchestration row has a blank "% of Corpus" cell.** It should read **14%**.

**4. The kappa sentence mixes two measurement rounds.** *"agreed with me at κ = 0.30, with Claude
performing the best"* — the **0.30** is the aggregate blinded Trust Check (n=50, later stage), while the
per-model ranking comes from the **earlier screening pilot**, where Claude/Human was **κ = 0.273**,
ChatGPT/Human 0.077, Gemini/Human 0.052. Both are true; attributing a per-model ranking to the
aggregate figure is not. Cleanest fix is to give the per-model numbers explicitly, since they're the
more striking result anyway.

Also minor: the image placeholder says `assets/three-mechanisms.png`; the current asset with the
deterministic-orchestration band is **`assets/mechanisms.png`**.

---

## Citation placement map

| # | Where in the article | Claim | Citation | Zotero key |
|---|---|---|---|---|
| 1 | Intro, ¶2 | "automation complacency sets in" | (Parasuraman & Manzey, 2010) | `ING3D89M` |
| 2 | Finding 1 — Redundancy | "convergence among models improved acceptance by only 2.4 percentage points" | (Vargas, 2025) | `GAD5Z8PV` |
| 3 | Finding 1 — Redundancy | "unanimous committees of one to six LLM judges exhibited correlated errors" | (Ullah & Serwadda, 2026) | `A6ZE2A26` |
| 4 | Finding 1 — Critique | "ByteDance production system … precision to 75%" | (Sun et al., 2025) | `V4IRKSFI` |
| 5 | Finding 1 — Critique | "false positives from 88.7% to 40.0% … executable evidence" **[separate paper — see issue 1]** | (Jin & Chen, 2026) | `UDVHQ5HR` |
| 6 | Finding 1 — Critique | "independent audits, cross-critique, and arbitration … 83–90%" | (Vargas, 2025) | `GAD5Z8PV` |
| 7 | Finding 2, ¶1 | "cognitive engagement declined over time"; "happy path" | (Catalan et al., 2026) | `5BAZZWHG` |
| 8 | Finding 2, ¶2 | "dual-process theory: System 1 … System 2" | (Catalan et al., 2026) | `5BAZZWHG` |
| 9 | Finding 2, ¶3 | "Participants with prior experience … tended to stay in System 1" | (Catalan et al., 2026) | `5BAZZWHG` |
| 10 | Finding 2, last ¶ | "cognitive forcing designs … haven't been tested at scale" | (Catalan et al., 2026) | `5BAZZWHG` |
| 11 | Finding 3, ¶1 | "79% of merged human+AI pull requests received no external review" | (Gao et al., 2026) | `59KP8GTP` |
| 12 | Finding 3, ¶1 | "contributors without prior ownership typically receive the most feedback…" | (Gao et al., 2026) | `59KP8GTP` |
| 13 | Finding 3, ¶2 | "haven't tested whether unreviewed pull requests target easier work" | (Gao et al., 2026) | `59KP8GTP` |
| 14 | Recommendation 4 | "composition matters more than size … diminishing returns" | (Ullah & Serwadda, 2026) | `A6ZE2A26` |
| 15 | After recommendations | "The most successful deployment chose precision over recall" | (Sun et al., 2025) | `V4IRKSFI` |
| 16 | A Note of Caution | "Cohen's κ" — the statistic itself | (Cohen, 1960) | `NMUMXCJZ` |
| 17 | A Note of Caution | "below the 0.4 threshold usually considered acceptable" — the interpretive bands | (Landis & Koch, 1977) **or** (McHugh, 2012) | — / `F4BHRKPK` |

**Note on #13** — this is Gao et al.'s *own* stated limitation, so it's fair to cite them for it. Their
wording: *"Due to space constraints, we did not analyse the reasons behind it. We hypothesise that this
may stem from Human+AI PRs primarily targeting low-hanging fruit within the projects."*

---

## On citing kappa — which source, and a caveat worth knowing

Two different things need citing and they are often conflated:

**The statistic** → **Cohen (1960)**, `NMUMXCJZ`, already in the library. Cite on first use of "Cohen's κ".

**The interpretive bands** — "fair", "moderate", "substantial", and the 0.4 boundary you're leaning on
→ **Landis & Koch (1977)**. Their scale puts 0.21–0.40 at *fair* and 0.41–0.60 at *moderate*, which is
exactly where your "0.4 floor" comes from. **This paper is NOT in the library** — reference supplied
below so you can add it.

**A caveat you may want to use rather than avoid.** The library also has **McHugh (2012)**
(`F4BHRKPK`), which argues the Landis & Koch bands are **too lenient** for consequential decisions and
proposes stricter ones — under her scheme κ below about 0.60 is inadequate agreement. That makes your
result *worse*, not better, which is an honest strengthening: the models fell short of even the
permissive threshold. If you want one sentence for it:

> *Landis and Koch (1977) treat κ between 0.21 and 0.40 as "fair"; McHugh (2012) argues these bands are
> too permissive for consequential decisions. On either scale, the model–human agreement here is
> insufficient to delegate the screening decision.*

Your own methodology (`screening_multimodel_results.md`) records the 0.4 figure as the "SLR IRR
acceptability floor" with no citation attached — worth anchoring it to Landis & Koch there too, since
the same number will appear in the dissertation.

---

## References (APA 7)

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological
Measurement, 20*(1), 37–46. https://doi.org/10.1177/001316446002000104

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data.
*Biometrics, 33*(1), 159–174. https://doi.org/10.2307/2529310

McHugh, M. L. (2012). Interrater reliability: The kappa statistic. *Biochemia Medica, 22*(3), 276–282.
https://doi.org/10.11613/BM.2012.031

Catalan, C. R., Dizon, L. M., Monderin, P. N., & Kuang, E. (2026). *"I'm not reading all of that":
Understanding software engineers' level of cognitive engagement with agentic coding assistants*
[Preprint]. arXiv. https://arxiv.org/abs/2603.14225

Gao, H., Banyongrakkul, P., Guan, H., Zahedi, M., & Treude, C. (2026). On autopilot? An empirical study
of human–AI teaming and review practices in open source. In *Proceedings of the 23rd International
Conference on Mining Software Repositories* (pp. 777–781). Association for Computing Machinery.
https://doi.org/10.1145/3793302.3793573

Jin, H., & Chen, H. (2026). Are LLMs reliable code reviewers? Systematic overcorrection in requirement
conformance judgement. *Automated Software Engineering, 33*, Article 90.
https://doi.org/10.1007/s10515-026-00638-5

Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An
attentional integration. *Human Factors, 52*(3), 381–410. https://doi.org/10.1177/0018720810376055

Sun, T., Xu, J., Li, Y., Yan, Z., Zhang, G., Xie, L., Geng, L., Wang, Z., Chen, Y., Lin, Q., Duan, W.,
Sui, K., & Zhu, Y. (2025). BitsAI-CR: Automated code review via LLM in practice. In *Companion
Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering*
(FSE Companion '25). Association for Computing Machinery. https://doi.org/10.1145/3696630.3728552

Ullah, M. A., & Serwadda, A. (2026). *Vibe coding on trial: Operating characteristics of unanimous LLM
juries* [Preprint]. arXiv. https://arxiv.org/abs/2602.18492

Vargas, M. J. T. (2025). *SLEAN: Simple lightweight ensemble analysis network for multi-provider LLM
coordination: Design, implementation, and vibe coding bug investigation case study* [Preprint]. arXiv.
https://arxiv.org/abs/2510.10010

---

## Metadata verification notes

- **Gao** and **Jin** were both arXiv/SSRN preprints until recently and are now peer-reviewed; the
  Zotero records were converted in place on 2026-08-29. Cite the **published** versions above. Jin's
  volume/article number (33, Article 90) is taken from the published PDF header, as the Zotero record
  does not carry it.
- **Sun et al.** — the Zotero record has publisher "SIGSOFT FSE Companion" but no proceedings title.
  The full title above is taken from the paper's own running header: *"In 33rd ACM International
  Conference on the Foundations of Software Engineering (FSE Companion '25), June 23–28, 2025,
  Trondheim, Norway."* **Worth confirming against the ACM DL landing page** before publishing, and
  worth fixing in Zotero either way.
- **Catalan, Ullah, Vargas** remain preprints. If any has been published since, the reference needs
  updating — the "Preprint - Now Published" collection exists for exactly this.
- **Cohen (1960)** — the Zotero record lacks volume/issue/pages; the canonical values are *20*(1),
  37–46, supplied above. Worth fixing in Zotero.
- **Landis & Koch (1977)** is **not in the library**. Add it before generating the bibliography, or the
  0.4 threshold will be an uncited claim.
- **McHugh (2012)** — Zotero has the author as "McHugh, M."; the correct form is **McHugh, M. L.**
- Author counts: Sun et al. has 13 authors, so APA lists the first 19 in full — all 13 shown above,
  correctly, with no ellipsis needed.
