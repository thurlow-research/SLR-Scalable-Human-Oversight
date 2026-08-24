# Light Read — Per-Paper Tagging Checklist (78 papers)

Prep sheet for the "02 - Light Read" pass (`WTKULZ5U`). Papers are listed alphabetically by first
author, one entry per paper — work top to bottom. Each entry is headed by its APA reference-list
citation (Zotero key given for lookup). The bullets under each entry are the specific tags to
verify on that item — confirm the panel's call or flip to the dissent. Where a call turns on
something non-obvious, a short *Question* line follows the bullet.

Source data: `sweep_review_workbook.md` (panel proposals/tripwires) + the 2026-08-22
Synthetic-Eval-Check rescan for the two newer facet pairs:
- **Evidence-strength ladder** (`evaluated-synthetic` / `evaluated-benchmark` / plain
  `self-tests`) — only applies when the system self-runs against material and gets judged after
  the fact. If a real subject performs the task live instead, it's `method-experiment` /
  `method-field-study`, **not** the ladder (Changelog §34).
- **Structural facets** (`agent-panel` / `cross-model`) — split off `theme:ai-review`'s own
  conflated language: is more than one agent involved (`agent-panel`), and if so, different
  vendors (`cross-model`)? `theme:ai-review` itself is unaffected either way.
- **Demote to Context** — flagged when one or more models proposed `demote:context`. Confirm the
  demote, or rescue per the §30 sole-exemplar exception.

---

### Abreu, R., Murali, V., Rigby, P. C., Maddila, C., Sun, W., Ge, J., Chinniah, K., Mockus, A., Mehta, M., & Nagappan, N. (2025, April). Moving Faster and Reducing Risk: Using LLMs in Release Deployment. *2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP)*. https://doi.org/10.1109/ICSE-SEIP66354.2025.00045 (`BU73N7PC`)
- **Primary theme — `risk-routing`:** confirm or flip to the dissent (unstable: codex disagrees).
- **Evidence-strength ladder — multi-tag case:** `adopted` + `built-system` both 3/3, no method-* co-proposed.
  - *Question:* likely `adopted` is correct (real deployment) — confirm it isn't just `built-system` alone being over-read as adopted.

### Alami, D. (2026). *Cognitive camouflage: specification gaming in LLM-generated code evades holistic evaluation but not adversarial execution*. 9. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6512960 (`WBS9U5N7`)
- **Primary theme — `ai-review`:** confirm or flip to the dissent (unstable: opus disagrees).
- **Structural facet** (`agent-panel` / `cross-model`): primary is `ai-review` — check the reviewer architecture.
- **RESOLVED 2026-08-23 — two-event paper, both sides stand.** `evaluated-synthetic` (ZTARE's own performance) **and** `method-experiment` (controlled comparison of Claude / GPT-4o / Gemini, findings characterizing those third-party models — the "subjects may be systems" clause, UDVHQ5HR precedent). Also endorsed: `theme:ai-review` (membership, **not** primary), `theme:rules-based-checks`, `facet:built-system`. Rejected: `facet:agentic` (apparatus, not the studied generation — §47). Primary left empty; slot held by `primary-proposed:theme:evaluator-reliability`. Demoted to Context.
  - *Correction:* an earlier draft of this sheet called the panel's `method-experiment` proposal a machine-only confusion exemplar. That was wrong — see changelog §48.

### Bara, M. (2026). *HAIF: a human-AI integration framework for hybrid team operations* (2602.07641). arXiv. https://arxiv.org/abs/2602.07641 (`6F3S8IB7`)
- **Primary theme — `risk-routing`:** confirm or flip to the dissent (unstable: opus and gemini disagree; sprawl: codex proposed 9 themes).
- No ladder facet applies — `design-only` is already present.

### Batte, B. (2025). *The evolving landscape of code review: leveraging artificial intelligence for enhanced software quality and developer productivity*. 7. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5214508 (`NGIH5T4C`)
- **Primary theme — `ai-review`:** confirm or flip to the dissent.
- **Demote to Context:** confirm (flagged by all 3 models).
- **Structural facet** (`agent-panel` / `cross-model`): primary is `ai-review` — check the reviewer architecture. No `built-system` co-proposed, so no ladder question.

### Baumgartner, N., Iyenghar, P., Schoemaker, T., & Pulvermüller, E. (2024). AI-driven refactoring: a pipeline for identifying and correcting data clumps in git repositories. *Electronics (Switzerland)*, *13*(9). Scopus. https://doi.org/10.3390/electronics13091644 (`WUUDHL8R`)
- **Primary theme — `ai-review`:** confirm or flip to the dissent (unstable: codex disagrees).
- **Structural facet** (`agent-panel` / `cross-model`): primary is `ai-review` — check the reviewer architecture.
- **Evidence-strength ladder:** `built-system` (3/3), no method-* co-proposed — check which rung.

### Borg, M., Hagatulah, N., Tornhill, A., & Söderberg, E. (2026). *Code for machines, not just humans: quantifying AI-friendliness with code health metrics* (2601.02200). arXiv. https://arxiv.org/abs/2601.02200 (`TJH7QFAX`)
- **Primary theme — `risk-routing`:** confirm or flip to the dissent (unstable: codex disagrees).
- No ladder facet applies — `method-experiment` is present, no `built-system`.

### Bowman, S. R., Hyun, J., Perez, E., Chen, E., Pettit, C., Heiner, S., Lukošiūtė, K., Askell, A., Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McKinnon, C., Olah, C., Amodei, D., Amodei, D., Drain, D., Li, D., Tran-Johnson, E., … Kaplan, J. (2022). *Measuring Progress on Scalable Oversight for Large Language Models*. arXiv.org. https://doi.org/10.48550/arXiv.2211.03540 (`RNDPW7VA`)
- **Primary theme — `oversight-explanation`:** confirm or flip to the dissent.
- **Demote to Context:** confirm (flagged by all 3 models).
- No ladder/structural facet applies (primary isn't `ai-review`, no `built-system`).
  - *Question:* this is the paper where "cross-examine" shows up in the corpus, but it describes a *human* cross-examining a single AI, not agent-vs-agent — it doesn't feed `agent-panel`/`cross-model`. Just flagging so you don't second-guess it.

### Casserini, M., Facchini, A., & Ferrario, A. (2026). *Beyond the "diff": addressing agentic entropy in agentic software development*. https://arxiv.org/abs/2604.16323 (`95CPB7CF`)
- **Primary theme — `oversight-explanation`:** confirm or flip to the dissent (sprawl: codex proposed 7 themes).
- No ladder facet applies — `design-only` is already present.

### Choudhuri, R., Bird, C., Badea, C., & Sarma, A. (2026). *To copilot and beyond: 22 AI systems developers want built* (2604.07830). arXiv. https://arxiv.org/abs/2604.07830 (`ID7IN65K`)
- **Primary theme — `hitl-workflow`:** confirm or flip to the dissent (sprawl: all 3 models proposed 8–10 themes — check for over-tagging).
- No ladder facet applies — no `built-system` co-proposed.

### Cotroneo, D., Foggia, A., Improta, C., Liguori, P., & Natella, R. (2023). *Automating the correctness assessment of AI-generated code for security contexts*. https://doi.org/10.1016/j.jss.2024.112113 (`PR4GS7SP`)
- **Primary theme — `rules-based-checks`:** confirm or flip to the dissent (unstable: codex disagrees).
- **Evidence-strength ladder:** `built-system` (3/3), no method-* co-proposed — check which rung.

### Ehsani, R., Pathak, S., Rawal, S., Mujahid, A. A., Imran, M. M., & Chatterjee, P. (2026). *Where Do AI Coding Agents Fail? An Empirical Study of Failed Agentic Pull Requests in GitHub*. arXiv.org. https://doi.org/10.48550/arXiv.2601.15195 (`NZJST99D`)
- **Primary theme — `oversight-scaling-inversion`:** confirm or flip to the dissent (unstable: gemini disagrees).
- No ladder facet applies — no `built-system` co-proposed.

### Elgendy, I. A., Dwivedi, Y. K., Al-Sharafi, M. A., Hosny, M., Helal, M. Y. I., Crick, T., Hughes, L., Alwahaishi, S., Mahmud, M., Dutot, V., & Al-Busaidi, A. S. (2026). Responsible vibe coding: architecture, opportunities, and research agenda. *Journal of Computer Information Systems*. Scopus. https://doi.org/10.1080/08874417.2026.2621186 (`WH2PIBNQ`)
- **Primary theme — `org-governance`:** confirm or flip to the dissent (sprawl: codex proposed 10 themes).
- **Demote to Context:** codex and gemini flagged this (opus did not) — check the split.
- No ladder facet applies — no `built-system` co-proposed.

### Eze, S. (2026). *Human-in-the-loop isn't a checkbox: designing meaningful intervention in automated AI decisions*. 24. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6552159 (`9MV2IVNU`)
- **Primary theme — `oversight-theater`:** confirm or flip to the dissent (sprawl: codex proposed 7 themes).
- **Demote to Context:** confirm (flagged by all 3 models).
- No ladder facet applies — `design-only` is already present.

### Goodhue, J. (2025). *The hidden legal minefield: how AI-assisted "vibe coding" amplifies software development risks and how technology can provide solutions*. 10. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5403926 (`34ELRWJH`)
- **Primary theme — `regulatory-compliance`:** confirm or flip to the dissent.
- **Demote to Context:** only gemini flagged this (opus/codex did not) — check whether gemini's dissent is right.

### E. A. González, R. Rothkopf, S. Lerner, & N. Polikarpova. (2025). HiLDE: intentional code generation via human-in-the-loop decoding. *2025 IEEE Symposium on Visual Languages and Human-Centric Computing (VL/HCC)*, 222–233. https://doi.org/10.1109/VL-HCC65237.2025.00032 (`CI93QRUH`)
- **Primary theme — `oversight-explanation`:** confirm or flip to the dissent (unstable: codex disagrees).
- **Evidence-strength ladder — already resolved:** `method-experiment` confirmed this session (18 real participants, 4 programming tasks), `evaluated-synthetic` removed. No action needed unless you disagree.

### Grunde-McLaughlin, M., Mozannar, H., Murad, M., Chen, J., Amershi, S., & Fourney, A. (2026). *Overseeing Agents Without Constant Oversight: Challenges and Opportunities*. arXiv. https://doi.org/10.48550/arXiv.2602.16844 (`7ZMU5AIF`)
- **Primary theme — `oversight-explanation`:** confirm or flip to the dissent.
- **Demote to Context:** confirm (flagged by all 3 models).
- No ladder/structural facet applies — `design-only` is already present, which excludes the ladder by definition.

### He, J., Shi, J., Zhuo, T. Y., Treude, C., Sun, J., Xing, Z., Du, X., & Lo, D. (2026). LLM-as-a-judge for software engineering: literature review, vision, and the road ahead. *ACM Transactions on Software Engineering and Methodology*. https://doi.org/10.1145/3797276 (`LCPH3THV`)
- **Primary theme — `ai-review`:** confirm or flip to the dissent.
- **Demote to Context:** codex and gemini flagged this (opus did not) — check the split.
- **Structural facet** (`agent-panel` / `cross-model`): primary is `ai-review`, but `lit-review` is also present.
  - *Question:* is this really *about* an ai-review architecture, or is it surveying other people's architectures? Confirm before applying either new facet.

### Hein, D. K., Persson, J., Jensen, V. V., Bruun, A. R., & Jaatun, M. G. (2025). *Causal mapping of the risks of using generative ai in software development*. 28. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5273073 (`LGZXFLSJ`)
- **Primary theme — `org-governance`:** confirm or flip to the dissent.
- **Demote to Context:** only gemini flagged this — check whether gemini's dissent is right.
- No ladder facet applies — no `built-system` co-proposed.

### Michel Hjazeen. (2026). *Beyond SAST and DAST: a unified security testing architecture for autonomous coding agents*. 17. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6271220 (`VFNJSZD9`)
- **Primary theme — `ai-review`:** confirm or flip to the dissent (unstable: opus and gemini disagree; sprawl: codex proposed 9 themes).
- **Structural facet** (`agent-panel` / `cross-model`): primary is `ai-review` — check the reviewer architecture. `design-only` is present, so no ladder question.

### Jensen, R. I. T., V. Tawosi, & S. Alamir. (2024). Software vulnerability and functionality assessment using LLMs. *2024 IEEE/ACM International Workshop on Natural Language-Based Software Engineering (NLBSE)*, 25–28. https://ieeexplore.ieee.org/document/10647161 (`8KJEKBGT`)
- **Primary theme — `ai-review`:** confirm or flip to the dissent.
- **Demote to Context:** codex and gemini flagged this (opus did not) — check the split.
- **Structural facet** (`agent-panel` / `cross-model`): primary is `ai-review` — check the reviewer architecture. `method-experiment` is present, no `built-system` (no ladder question).

### Jessee, R. T. (2026). *Scapegoat-as-a-service: moving from "human-in-the-loop" to "human-in-command" in regulated systems*. 20. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6052874 (`JVWUYDME`)
- **Primary theme — `hitl-workflow`:** confirm or flip to the dissent (sprawl: codex proposed 10 themes — check for over-tagging).
- **Demote to Context:** confirm (flagged by all 3 models).
- No ladder facet applies — `design-only` is already present.

### Kamalı, H. Ö., Tuna, E., Haratian, V., & Tüzün, E. (2026). *Rethinking code review in the age of AI: a vision for agentic code review* (arXiv:2605.17548; Version v1). arXiv. https://arxiv.org/abs/2605.17548v1 (`3ZVMBGPB`)
- **Primary theme — `ai-review`:** confirm or flip to the dissent (sprawl: codex proposed 11 themes — check for over-tagging).
- **Structural facet** (`agent-panel` / `cross-model`): primary is `ai-review` — check the reviewer architecture. `design-only` is present, so no ladder question.

### Karuppuchamy, S. (2026). AI-augmented software engineering for rapid feature delivery and operations automation. *2026 IEEE 16th Annual Computing and Communication Workshop and Conference (CCWC)*, 0607–0614. https://doi.org/10.1109/CCWC67433.2026.11393761 (`8MXATG38`)
- **Primary theme — `org-governance`:** confirm or flip to the dissent (sprawl: codex proposed 7 themes).
- **Evidence-strength ladder — multi-tag case:** `adopted` + `built-system` + `method-field-study` + `method-mining` + `method-self-report` all co-proposed 3/3.
  - *Question:* worth a careful read — likely legitimate (real deployment means `adopted`/`method-field-study` genuinely apply together), but confirm there isn't also a separate self-constructed sub-evaluation that would need `evaluated-synthetic` in addition.

### Kasibatla, S. R., Rothkopf, R., Peleg, H., Pierce, B. C., Lerner, S., Goldstein, H., & Polikarpova, N. (2026). *Decision-Oriented Programming with Aporia*. arXiv.org. https://doi.org/10.48550/arXiv.2604.05203 (`ZH6QIU8A`)
- **Primary theme — `oversight-explanation`:** confirm or flip to the dissent (unstable: gemini disagrees).
- **Evidence-strength ladder — already resolved:** `method-experiment` confirmed this session (14 real participants, 25-minute live task), `evaluated-synthetic` removed. No action needed unless you disagree.

### Khati, D., Liu, Y., Palacio, D. N., Zhang, Y., & Poshyvanyk, D. (2025). Mapping the trust terrain: LLMs in software engineering - insights and perspectives. *ACM Trans. Softw. Eng. Methodol.* https://doi.org/10.1145/3771282 (`5I2W8IC6`)
- **Primary theme — `automation-bias`:** confirm or flip to the dissent.
- **Demote to Context:** codex and gemini flagged this (opus did not) — check the split.
- No ladder facet applies — `method-self-report` is present, no `built-system`.

### Khoo, S., Foo, J., & Lee, R. K.-W. (2025). *With Great Capabilities Come Great Responsibilities: Introducing the Agentic Risk & Capability Framework for Governing Agentic AI Systems*. arXiv.org. https://doi.org/10.48550/arXiv.2512.22211 (`5AVZQCVU`)
- **Primary theme — `org-governance`:** confirm or flip to the dissent (sprawl: codex proposed 7 themes — check for over-tagging).
- **Demote to Context:** confirm (flagged by all 3 models).

### Kim, G., & Yegge, S. (2025). *Vibe coding: building production-grade software with GenAI, chat, agents, and beyond* (Kindle Ed.). IT Revolution. https://openalex.org/W7114300968 (`RPHK78A9`)
- **Primary theme — `hitl-workflow`:** confirm or flip to the dissent (unstable: opus and gemini disagree; sprawl: opus/codex both flagged).
- **Demote to Context:** only gemini flagged this — check whether gemini's dissent is right.
- No ladder facet applies by strict rule (`method-field-study` noted 2/3 but no `built-system`).
  - *Question:* still worth a glance given how many tripwires are stacked on this one.

### Kudriavtseva, A., Hotak, N. A., & Gadyatskaya, O. (2025). My code is less secure with gen AI: surveying developers' perceptions of the impact of code generation tools on security. *Proc ACM Symp Appl Computing*, 1637–1646. Scopus. https://doi.org/10.1145/3672608.3707778 (`PD297DUM`)
- **Primary theme — `automation-bias`:** confirm or flip to the dissent (unstable: gemini disagrees).
- No ladder facet applies — no `built-system` co-proposed.

### Kumar, A. (2026). Designing guardrails: ensuring responsible AI behavior. *GenAI and LLMs for Beyond 5G Networks*, 107–144. Scopus. https://doi.org/10.1007/978-3-032-06418-9_5 (`ZSB2S59N`)
- **Primary theme — `org-governance`:** confirm or flip to the dissent (sprawl: codex proposed 7 themes).
- **Demote to Context:** confirm (flagged by all 3 models).

### Langer, M., Baum, K., & Schlicker, N. (2024). Effective human oversight of AI-based systems: a signal detection perspective on the detection of inaccurate and unfair outputs. *Minds and Machines*, *35*(1), 1. https://doi.org/10.1007/s11023-024-09701-0 (`5DCQDB4C`)
- **Primary theme — `automation-bias`:** confirm or flip to the dissent.
- **Demote to Context:** confirm (flagged by all 3 models).

### Li, H., Li, M., Zuo, J., Li, S., Li, X., Wu, H., Lu, Y., & He, X. (2025). *CoTDeceptor: adversarial code obfuscation against CoT-enhanced LLM code agents* (arXiv:2512.21250; Version v1). arXiv. https://arxiv.org/abs/2512.21250v1 (`T3XTXIXW`)
- **Primary theme — `ai-review`:** confirm or flip to the dissent (unstable: gemini disagrees).
- **Structural facet** (`agent-panel` / `cross-model`): primary is `ai-review` — check the reviewer architecture.
- **Evidence-strength ladder — already resolved:** tagged `evaluated-benchmark` this session.
  - *Question:* the `method-experiment` noted (2/3) is likely a panel miscall (same pattern as WBS9U5N7/X7EN6DXZ) — worth a fast confirm, not a full re-derivation.

### Li, J., Hou, Y., Lin, L., Zhu, R., Cao, H., & El Ali, A. (2026). Vibe coding in product teams: reconfiguring AI-assisted workflows, prototyping, and collaboration. *Proceedings of the 5th Annual Symposium on Human-Computer Interaction for Work, CHIWORK '26*, 1–16. https://doi.org/10.1145/3808045.3808062 (`BLR3XE3I`)
- **Primary theme — `automation-bias`:** confirm or flip to the dissent (unstable: gemini disagrees; sprawl: codex proposed 9 themes).
- No ladder facet applies — `method-self-report` is present, no `built-system`.

### Ma, J., Wang, S., Kung, J. H., & Chilton, L. B. (2026). *ZORO: active rules for reliable vibe coding* (2604.15625). arXiv. https://arxiv.org/abs/2604.15625 (`JCTP8VXP`)
- **Primary theme — `hitl-workflow`:** confirm or flip to the dissent (unstable: codex disagrees; sprawl: codex proposed 7 themes).
- **Evidence-strength ladder — already resolved:** `method-experiment` confirmed this session (12 real participants, real coding tasks), `evaluated-synthetic` removed (no separate tool-only evaluation found in the text). No action needed unless you disagree.

### Maes, S. (2025). *The gotchas of AI coding and vibe coding. It's all about support and maintenance*. OSF Preprints. https://doi.org/10.31219/osf.io/kjz9t_v1 (`59ZW4R58`)
- **Primary theme — `quality-debt`:** confirm or flip to the dissent (no tripwires — clean modal call).
- No ladder facet applies — `design-only` is already present.

### A. Mahmud, Y. Rawajfih, & R. Arnold. (2025). Trust-calibrated multi-stage large language model pipeline for vulnerability assessment in DevSecOps workflows. *2025 Annual Computer Security Applications Conference Workshops (ACSAC Workshops)*, 459–466. https://doi.org/10.1109/ACSACW69556.2025.00074 (`R9CDT9KB`)
- **Primary theme — `risk-routing`:** confirm or flip to the dissent (unstable: gemini disagrees).
- **Evidence-strength ladder:** `built-system` (3/3), no method-* co-proposed — check which rung.

### Marri, S. R. (2026). *Constitutional spec-driven development: enforcing security by construction in AI-assisted code generation* (2602.02584). arXiv. https://arxiv.org/abs/2602.02584 (`C88VGWMI`)
- **Primary theme — `ai-code-insecurity`:** confirm or flip to the dissent (unstable: all 3 models disagree — check closely).
- **Demote to Context:** opus and gemini flagged this (codex did not) — check the split.
- **Evidence-strength ladder vs. method-\* — exclusivity conflict:** `built-system` (3/3) + `method-experiment` (2/3 noted).
  - *Question:* already spot-checked this session (0 participant/contractor mentions found) — the current `evaluated-synthetic` tag is likely correct, but with demote + instability tripwires stacked here too, worth a quick re-confirm rather than trusting the earlier pass blind.

### McKay, M. H. (2024). Realizing the promise of AI governance involving humans-in-the-loop. In Degen H. & Ntoa S. (Eds.), *Lect. Notes Comput. Sci.: 15382 LNCS* (pp. 107–123). Springer Science and Business Media Deutschland GmbH. Scopus. https://doi.org/10.1007/978-3-031-76827-9_7 (`84D2AMVM`)
- **Primary theme — `automation-bias`:** confirm or flip to the dissent.
- **Demote to Context:** confirm (flagged by all 3 models).

### Migliarini, P., Autili, M., Inverardi, P., & Pelliccione, P. (2026). Ethical prompt engineering for AI-driven SE: evidence-informed interaction-time governance roadmap to 2030. *ACM Trans. Softw. Eng. Methodol.* https://doi.org/10.1145/3801980 (`4AXDVW7J`)
- **Primary theme — `org-governance`:** confirm or flip to the dissent (unstable: codex disagrees).
- **Demote to Context:** codex and gemini flagged this (opus did not) — check the split.

### Mitchell, J., & Shaaban, Y. (2025). Position: vibe coding needs vibe reasoning: improving vibe coding with formal verification. *Proceedings of the 1st ACM SIGPLAN International Workshop on Language Models and Programming Languages, LMPL '25*, 84–90. https://doi.org/10.1145/3759425.3763390 (`6ZW9QNQH`)
- **Primary theme — `formal-methods`:** confirm or flip to the dissent (sprawl: codex proposed 8 themes).
- **Evidence-strength ladder:** `built-system` (3/3), no method-* co-proposed — check which rung.

### Mitropoulos, D., Alexopoulos, N., Alexopoulos, G., & Spinellis, D. (2026). *Measuring and exploiting contextual bias in LLM-assisted security code review* (arXiv:2603.18740; Version v2). arXiv. https://arxiv.org/abs/2603.18740v2 (`X7EN6DXZ`)
- **Primary theme — `tooling-supply-chain`:** confirm or flip to the dissent (unstable: opus and gemini disagree).
- **Evidence-strength ladder — already resolved:** `evaluated-benchmark` confirmed this session (CrossVul, genuine standardized third-party dataset, 0 real participants found).
  - *Question:* the panel's `method-experiment` proposal here (3/3) is another clean example of the machine-only built-system/method-experiment confusion — reference case, no action needed.

### Moreira, J. (2026). *IACDM: interactive adversarial convergence development methodology -- a structured framework for AI-assisted software development* (2604.16399). arXiv. https://arxiv.org/abs/2604.16399 (`RX9SICP9`)
- **Primary theme — `hitl-workflow`:** confirm or flip to the dissent (unstable: opus disagrees; sprawl: codex proposed 9 themes).
- **Evidence-strength ladder — multi-tag case:** `adopted` + `built-system` (3/3) + `method-field-study` (2/3 noted) — same pattern as Karuppuchamy (8MXATG38).
  - *Question:* confirm real deployment vs. a self-constructed component before assigning `adopted`.

### Mozannar, H., Bansal, G., Tan, C., Fourney, A., Dibia, V., Chen, J., Gerrits, J., Payne, T., Maldaner, M. K., Grunde-McLaughlin, M., Zhu, E., Bassman, G., Alber, J., Chang, P., Loynd, R., Niedtner, F., Kamar, E., Murad, M., Hosn, R., & Amershi, S. (2025). *Magentic-UI: Towards Human-in-the-loop Agentic Systems*. arXiv.org. https://doi.org/10.48550/arXiv.2507.22358 (`U9VZQXGI`)
- **Primary theme — `hitl-workflow`:** confirm or flip to the dissent.
- **Demote to Context:** codex and gemini flagged this (opus did not) — check the split.
- **Evidence-strength ladder — already resolved, both stand:** genuine two-event paper — `evaluated-benchmark` confirmed (GAIA/AssistantBench/WebVoyager, established agentic benchmarks) **and** `method-experiment` added (separate 12-user study). No action needed unless you disagree.

### Pasuksmit, J., Takerngsaksiri, W., Thongtanunam, P., Tantithamthavorn, C., Zhang, R., Wang, S., Jiang, F., Li, J., Cook, E., Chen, K., & Wu, M. (2025, April 25). *Human-In-the-loop software development agents: challenges and future directions*. https://arxiv.org/abs/2506.11009 (`B7APR28B`)
- **Primary theme — `ai-review`:** confirm or flip to the dissent.
- **Demote to Context:** only gemini flagged this — check whether gemini's dissent is right.
- **Structural facet** (`agent-panel` / `cross-model`): primary is `ai-review` — check the reviewer architecture.
- **Evidence-strength ladder:** `built-system` noted (2/3) — worth a look.

### Perry, N., Srivastava, M., Kumar, D., & Boneh, D. (2023). Do users write more insecure code with AI assistants? *Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security*, 2785–2799. https://doi.org/10.1145/3576915.3623157 (`YBHHYR4P`)
- **Primary theme — `ai-code-insecurity`:** confirm or flip to the dissent (unstable: gemini disagrees).
- No ladder facet applies — `method-experiment` is present, no `built-system`.

### Pimenova, V., Fakhoury, S., Bird, C., Storey, M.-A., & Endres, M. (2025). *Good vibrations? A qualitative study of Co-creation, communication, flow, and trust in vibe coding* (2509.12491). arXiv. https://arxiv.org/abs/2509.12491 (`E9RAWBDT`)
- **Primary theme — `automation-bias`:** confirm or flip to the dissent (unstable: opus disagrees; sprawl: codex proposed 10 themes).
- No ladder facet applies — no `built-system` co-proposed.

### Rabani, Z. S., Khorashadizadeh, H., Abdollahzade, S., Groppe, S., & Ghofrani, J. (2023). Developers' perspective on trustworthiness of code generated by ChatGPT: insights from interviews. In M. A. Jabbar, S. Tiwari, F. Ortiz-Rodríguez, S. Groppe, & T. Bano Rehman (Eds.), *Applied Machine Learning and Data Analytics*. https://doi.org/10.1007/978-3-031-55486-5_16 (`WWBUQM7V`)
- **Primary theme — `quality-debt`:** confirm or flip to the dissent.
- **Demote to Context:** only gemini flagged this — check whether gemini's dissent is right.
- No ladder facet applies — no `built-system` co-proposed.

### Sharma, A., & David, C. (2025). *Assessing Correctness in LLM-Based Code Generation via Uncertainty Estimation*. arXiv.org. https://doi.org/10.48550/arXiv.2502.11620 (`E5SQKRH7`)
- **Primary theme — `formal-methods`:** confirm or flip to the dissent (unstable: codex and gemini disagree).
- **Evidence-strength ladder:** `built-system` (3/3), no method-* co-proposed — check which rung.

### Sharma, P. N., Wright, L., Herfurth, A., Sokiyna, M., Sharma, P. N., Das, S., & Siponen, M. (2025). *DevLicOps: a framework for mitigating licensing risks in AI-generated code* (2508.16853). arXiv. https://arxiv.org/abs/2508.16853 (`WPWF7A32`)
- **Primary theme — `org-governance`:** confirm or flip to the dissent (sprawl: codex proposed 8 themes).
- No ladder facet applies — no `built-system` co-proposed.

### Sharma, R. (2026). *The ethics of AI-assisted code migration in regulated financial systems: accountability, transparency, and human oversight in LLM-driven software conversion*. 15. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6252918 (`27YULT5I`)
- **Primary theme — `org-governance`:** confirm or flip to the dissent (sprawl: codex proposed 10 themes — check for over-tagging).

### Sharma, R., & Gupta, A. (2026). Source code guardrail: AI driven solution to distinguish critical vs. Generic code for enterprise LLM security. In Yang G., Liu S., Su C., Otsuka A., & Lian Z. (Eds.), *Lect. Notes Comput. Sci.: 16172 LNCS* (pp. 449–458). Springer Science and Business Media Deutschland GmbH. Scopus. https://doi.org/10.1007/978-981-95-2961-2_23 (`6TZHUCMD`)
- **Primary theme — `org-governance`:** confirm or flip to the dissent (unstable: opus disagrees).
- **Demote to Context:** confirm (flagged by all 3 models).
- **Evidence-strength ladder vs. method-\* — exclusivity conflict:** `built-system` (3/3) and `method-field-study` (2/3) both proposed.
  - *Question:* is there a real user in the loop, or is this a self-run evaluation? Pick one, not both.

### Sistla, M., Balakrishnan, G., Rondon, P., Cambronero, J., Tufano, M., & Chandra, S. (2025). *Towards verified code reasoning by LLMs* (arXiv:2509.26546; Version v2). arXiv. https://arxiv.org/abs/2509.26546v2 (`5DI9B43K`)
- **Primary theme — `formal-methods`:** confirm or flip to the dissent (no tripwires — clean modal call).
- **Evidence-strength ladder:** `built-system` (3/3), no method-* co-proposed — check which rung (`self-tests` / `evaluated-synthetic` / `evaluated-benchmark`).

### Spiess, C., Gros, D., Pai, K. S., Pradel, M., Rabin, M. R. I., Alipour, A., Jha, S., Devanbu, P., & Ahmed, T. (2025, April). Calibration and Correctness of Language Models for Code. *2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE)*. https://doi.org/10.1109/ICSE55347.2025.00040 (`VTDG995V`)
- **Primary theme — `ai-review`:** confirm or flip to the dissent (unstable: opus disagrees).
- **Structural facet** (`agent-panel` / `cross-model`): primary is `ai-review` — check the reviewer architecture. `method-experiment` noted (2/3), no `built-system` (no ladder question).

### Sterz, S., Baum, K., Biewer, S., Hermanns, H., Lauber-Rönsberg, A., Meinel, P., & Langer, M. (2024, June 5). On the Quest for Effectiveness in Human Oversight: Interdisciplinary Perspectives. *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency*. https://doi.org/10.1145/3630106.3659051 (`TW4I6DU6`)
- **Primary theme — `hitl-workflow`:** confirm or flip to the dissent (unstable: opus and codex disagree — check closely).
- **Demote to Context:** confirm (flagged by all 3 models).

### Sulova, S. (2025). Artificial intelligence tools in web application development – advantages and challenges. *2025 International Conference on Intelligent Computing and Next Generation Networks (ICNGN)*, 1–5. https://doi.org/10.1109/ICNGN67480.2025.11413758 (`WZCULPXN`)
- **Primary theme — `org-governance`:** confirm or flip to the dissent.
- **Demote to Context:** confirm (flagged by all 3 models).

### Eric Swidey. (2026). *Adversarial verification as reference architecture for EU AI act article 14 compliance in employment AI*. 10. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5958495 (`5RLPIA3K`)
- **Primary theme — `regulatory-compliance`:** confirm or flip to the dissent (unstable: all 3 models disagree — check closely; sprawl: codex proposed 7 themes).
- **Demote to Context:** confirm (flagged by all 3 models).
- **Evidence-strength ladder:** `built-system` noted (2/3) with no method-* co-proposed — check where it lands (likely `self-tests` or `evaluated-synthetic`).

### Tereci, S., Gökalp, E., & Dikici, A. (2026). Toward a maturity model for AI-assisted software development: conceptual framework and research agenda. *2026 5th International Informatics and Software Engineering Conference (IISEC)*, 656–661. https://doi.org/10.1109/IISEC69317.2026.11418422 (`B4TVIG5Y`)
- **Primary theme — `org-governance`:** confirm or flip to the dissent.
- **Demote to Context:** only gemini flagged this — check whether gemini's dissent is right.

### Tilbury, J., & Flowerday, S. (2024). The rationality of automation bias in security operation centers. *Journal of Information Systems Security*, *20*(2), 89–109. Scopus. https://www.researchgate.net/profile/Jack-Tilbury-2/publication/387902110_The_Rationality_of_Automation_Bias_in_Security_Operation_Centers/links/67816f8c8210a977a17fb3a1/The-Rationality-of-Automation-Bias-in-Security-Operation-Centers.pdf (`EB49Q8QM`)
- **Primary theme — `automation-bias`:** confirm or flip to the dissent.
- **Demote to Context:** confirm (flagged by all 3 models).

### Tisi, M., Cabot, J., Di Ruscio, D., & Garcia-Dominguez, A. (2025). MOSAICO: management, orchestration and supervision of AI-agent COmmunities for reliable AI in software engineering. In Fonseca C.M. & Fumagalli M. (Eds.), *CEUR Workshop Proc.* (Vol. 4050). CEUR-WS. Scopus. https://ceur-ws.org/Vol-4050/paper07.pdf (`DJMBHHZN`)
- **Primary theme — `ai-review`:** confirm or flip to the dissent.
- **Demote to Context:** only opus flagged this — check whether opus's dissent is right.
- **Structural facet** (`agent-panel` / `cross-model`): primary is `ai-review`, and the title itself suggests a multi-agent architecture. `design-only` is present, so no ladder question.

### Töpfer, M., Plášil, F., Bureš, T., & Hnětynka, P. (2026). *Vibe-coding: feedback-based automated verification with no human code inspection, a feasibility study* (2604.14867). arXiv. https://arxiv.org/abs/2604.14867 (`72W6R4JG`)
- **Primary theme — `rules-based-checks`:** confirm or flip to the dissent (unstable: codex disagrees).
- **Evidence-strength ladder:** `built-system` (3/3), no method-* co-proposed — check which rung.

### M. Tuape, Y. Gabrielmichael, & J. Kasurinen. (2025). Architecting trust: designing human oversight and accountability for AI-driven software engineering under the EU AI act. *2025 13th International Conference in Software Engineering Research and Innovation (CONISOFT)*, 325–331. https://doi.org/10.1109/CONISOFT66928.2025.00048 (`XZEHQYNZ`)
- **Primary theme — `regulatory-compliance`:** confirm or flip to the dissent.
- **Demote to Context:** opus and codex flagged this (gemini did not) — check the split.
- No ladder facet applies — no `built-system` co-proposed.

### Vasconcelos, H., Bansal, G., Fourney, A., Liao, Q., Vaughan, J. W., & Vaughan, J. W. (2025). Generation Probabilities Are Not Enough: Uncertainty Highlighting in AI Code Completions. *ACM Trans. Comput.-Hum. Interact.* https://doi.org/10.1145/3702320 (`ZBF86IJM`)
- **Primary theme — `oversight-explanation`:** confirm or flip to the dissent (unstable: codex disagrees).
- **Evidence-strength ladder — already resolved:** `method-experiment` confirmed this session (30 real programmers, live use), `evaluated-synthetic` removed.
  - *Question:* the LeetCode-sourcing question that originally started this whole thread doesn't change the outcome — it's off the ladder either way.

### Wang, T., Hao, Z., Wu, Y., Wu, W., Lin, Q., Dong, H., Yuan, N. J., & Xiong, H. (2026). *Scaling human-AI coding collaboration requires a governable consensus layer* (2604.17883). arXiv. https://arxiv.org/abs/2604.17883 (`2KPHQ5IV`)
- **Primary theme — `provenance-auditability`:** confirm or flip to the dissent (sprawl: opus proposed 7 themes, codex proposed 10).
- No ladder facet applies — `design-only` is already present.

### Waseem, M., Ahmad, A., Kemell, K.-K., Rasku, J., Lahti, S., Mäkelä, K., & Abrahamsson, P. (2025). *Vibe coding in practice: flow, technical debt, and guidelines for sustainable use* (2512.11922). arXiv. https://arxiv.org/abs/2512.11922 (`T2EG4BE2`)
- **Primary theme — `quality-debt`:** confirm or flip to the dissent (sprawl: opus proposed 9 themes, codex proposed 12 — check for over-tagging).
- No ladder facet applies by strict rule (`method-field-study`/`method-mining` present, no `built-system`).

### N. Watson, & M. Van Italie. (2025). From black box to open book: an emerging transparency imperative in generative AI codebases. *2025 IEEE Conference on Artificial Intelligence (CAI)*, 1369–1374. https://doi.org/10.1109/CAI64502.2025.00266 (`RG4A4D6K`)
- **Primary theme — `provenance-auditability`:** confirm or flip to the dissent (sprawl: codex proposed 7 themes).
- **Demote to Context:** codex and gemini flagged this (opus did not) — check the split.
- No ladder facet applies — no `built-system` co-proposed.

### Xu, F., Medappa, P. K., Tunç, M., Vroegindeweij, M., & Fransoo, J. C. (2025). *AI-Assisted Programming Decreases the Productivity of Experienced Developers by Increasing the Technical Debt and Maintenance Burden*. arXiv preprint. https://doi.org/10.2139/ssrn.5521379 (`F2C2DWSI`)
- **Primary theme — `oversight-scaling-inversion`:** confirm or flip to the dissent (unstable: opus disagrees).
- No ladder facet applies — no `built-system` co-proposed.

### N. Yanev, I. Getova, E. Mihaylova, I. Kostadinova, M. Bankovska, & G. Dimitrov. (2025). The prompt–refactor–verify (PRV) cycle: a human-centered framework for AI-assisted programming. *2025 6th International Conference on Communications, Information, Electronic and Energy Systems (CIEES)*, 1–5. https://doi.org/10.1109/CIEES66347.2025.11300239 (`QUXRX9ZL`)
- **Primary theme — `hitl-workflow`:** confirm or flip to the dissent (unstable: opus disagrees).
- No ladder facet applies — `design-only` is already present.

### Yang, W., He, R., & Zhou, M. (2026). *Beyond banning AI: a first look at GenAI governance in open source software communities* (2603.26487). arXiv. https://arxiv.org/abs/2603.26487 (`XJAXB98T`)
- **Primary theme — `org-governance`:** confirm or flip to the dissent (sprawl: codex proposed 9 themes).
- No ladder facet applies — no `built-system` co-proposed.

### Yao, F., Wang, Z., Liu, L., Cui, J., Zhong, L., Fu, X., Mai, H., Krishnan, V., Gao, J., & Shang, J. (2025). *Training language models to generate quality code with program analysis feedback* (2505.22704). arXiv. https://arxiv.org/abs/2505.22704 (`9R6TGN82`)
- **Primary theme — `rules-based-checks`:** confirm or flip to the dissent.
- **Demote to Context:** only opus flagged this — check whether opus's dissent is right.
- **Evidence-strength ladder:** `built-system` (3/3), no method-* co-proposed — check which rung.

### X. Yu, L. Liu, X. Hu, J. W. Keung, J. Liu, & X. Xia. (2024). Fight fire with fire: how much can we trust ChatGPT on source code-related tasks? *IEEE Transactions on Software Engineering*, *50*(12), 3435–3453. https://doi.org/10.1109/TSE.2024.3492204 (`PPMTM4DG`)
- **Primary theme — `ai-review`:** confirm or flip to the dissent.
- **Demote to Context:** only gemini flagged this — check whether gemini's dissent is right.
- **Structural facet** (`agent-panel` / `cross-model`): primary is `ai-review` — check the reviewer architecture. `method-experiment` is present, no `built-system` (no ladder question).

### Yu, Y., Rong, G., Shen, H., Zhang, H., Shao, D., Wang, M., Wei, Z., Xu, Y., & Wang, J. (2024). Fine-Tuning Large Language Models to Improve Accuracy and Comprehensibility of Automated Code Review. *ACM Trans. Softw. Eng. Methodol.* https://doi.org/10.1145/3695993 (`KF5MGIBI`)
- **Primary theme — `oversight-explanation`:** confirm or flip to the dissent (unstable: gemini disagrees).
- **Evidence-strength ladder:** `built-system` (3/3), no method-* co-proposed — check which rung.

### Zhao, S., Wang, D., Zhang, K., Luo, J., Li, Z., & Li, L. (2025). *Is vibe coding safe? Benchmarking vulnerability of agent-generated code in real-world tasks* (arXiv:2512.03262). arXiv. https://arxiv.org/abs/2512.03262 (`4PSM6ZCD`)
- **Primary theme — `ai-code-insecurity`:** confirm or flip to the dissent.
- **Demote to Context:** codex and gemini flagged this (opus did not) — check the split.
- No ladder facet applies — `method-experiment` is present, no `built-system` co-proposed.

### Zhong, M., Zhou, X., Chang, T.-Y., Wang, Q., Xu, N., Si, X., Garrette, D., Upadhyay, S., Liu, J., Han, J., Schillings, B., & Sun, J. (2025). *Vibe checker: aligning code evaluation with human preference* (2510.07315). arXiv. https://arxiv.org/abs/2510.07315 (`96XE669R`)
- **Primary theme — `rules-based-checks`:** confirm or flip to the dissent (unstable: gemini disagrees).
- **Demote to Context:** opus and gemini flagged this (codex did not) — check the split.
- **Evidence-strength ladder — already resolved:** `evaluated-synthetic` confirmed this session (new instrument built on established benchmarks = synthetic, not benchmark; no public release found). No action needed unless you disagree.

### Zhou, E., Xi, Z., Ma, L., Zhang, Z., Dou, S., Lei, Z., Wang, G., Zheng, R., Yan, H., Gui, T., Zhang, Q., & Huang, X. (2026). *Steering LLMs via scalable interactive oversight* (2602.04210). arXiv. https://arxiv.org/abs/2602.04210 (`XRTVITVP`)
- **Primary theme — `hitl-workflow`:** confirm or flip to the dissent (unstable: opus disagrees).
- **Demote to Context:** confirm (flagged by all 3 models).
- **Evidence-strength ladder vs. method-\* — exclusivity conflict:** `built-system` and `method-experiment` both proposed 3/3.

### Zhou, J., Roy, A., Gupta, S., Weitekamp, D., & MacLellan, C. J. (2026, April 13). When Should Users Check? Modeling Confirmation Frequency in Multi-Step Agentic AI Tasks. *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3772318.3790655 (`XK3P9C96`)
- **Primary theme — `risk-routing`:** confirm or flip to the dissent.
- **Demote to Context:** confirm (flagged by all 3 models).
- **Evidence-strength ladder vs. method-\* — exclusivity conflict:** `built-system` and `method-experiment` both proposed 3/3.
  - *Question:* the paper names both Claude and GPT — worth checking `agent-panel`/`cross-model` too, even though the primary proposal isn't `ai-review`.

### Zhou, P., & Zhao, Y. (2026). *Review makes workers less likely to revise AI output*. 15. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6325399 (`E689ZAXC`)
- **Primary theme — `automation-bias`:** confirm or flip to the dissent (unstable: opus and codex disagree — check closely).
- **Demote to Context:** confirm (flagged by all 3 models).
- No ladder facet applies — `method-experiment` is present, no `built-system` co-proposed.

### Liming Zhu, Qinghua Lu, Ding Ming, Sung Une Lee, & Chen Wang. (2025). *Designing meaningful human oversight in AI*. 16. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5501939 (`ZGST9CY6`)
- **Primary theme — `oversight-explanation`:** confirm or flip to the dissent (sprawl: opus proposed 7 themes, codex proposed 9 — check for over-tagging).
- **Demote to Context:** confirm (flagged by all 3 models).
- No ladder facet applies — `design-only` is already present.

### Zhuo, T. Y., He, J., Sun, J., Xing, Z., Lo, D., Grundy, J., & Du, X. (2026). Identifying and mitigating API misuse in large language models. *IEEE Transactions on Software Engineering*, *52*(3), 855–873. https://doi.org/10.1109/TSE.2026.3651566 (`VZ27QUPQ`)
- **Primary theme — `quality-debt`:** confirm or flip to the dissent (unstable: opus disagrees).
- **Evidence-strength ladder — already resolved:** `evaluated-synthetic` confirmed this session ("our benchmark" is self-labeled, not a field-recognized standard; release-upon-acceptance plan noted but not yet adopted by anyone). No action needed unless you disagree.

### Zietsman, C. (2026). *The specification as quality gate: three hypotheses on AI-assisted code review* (arXiv:2603.25773; Version v1). arXiv. https://arxiv.org/abs/2603.25773v1 (`TA6GIUK2`)
- **Primary theme — `ai-review`:** confirm or flip to the dissent (no tripwires — clean modal call).
- **Structural facet** (`agent-panel` / `cross-model`): primary is `ai-review` — check the reviewer architecture. `method-experiment` is present, no `built-system` (no ladder question).
