# Light Read — Per-Paper Tagging Questions (78 papers)

**Purpose:** prep sheet for the "02 - Light Read" pass (`WTKULZ5U`), combining (a) the original
sweep task — confirm the panel's modal theme proposal or flip to the dissent, using the listed
tripwires — with (b) new checks for the two facet pairs staged 2026-08-22: the built-system
evidence-strength ladder (`evaluated-synthetic`/`evaluated-benchmark`/plain `self-tests`) and the
structural pair (`agent-panel`/`cross-model`). Source data: `sweep_review_workbook.md` (original
proposals/tripwires/facets) + this session's rescan of the parallel Synthetic-Eval-Check collection.

**How to read the "new facet check" line:**
- **Ladder check** — flagged when the panel proposed `built-system`. Ask: does the system self-run
  against material and get judged after the fact (→ check `evaluated-synthetic`/`evaluated-benchmark`/
  plain `self-tests`), or does a real subject perform the task live (→ `method-experiment`/
  `method-field-study` instead, **not** the ladder — see the exclusivity rule, Changelog §34)?
- **Exclusivity conflict** — flagged when the panel proposed `built-system` **and**
  `method-experiment`/`method-field-study` together on the *same* paper. This is exactly the
  pattern that produced real mistags this session (ZBF86IJM, CI93QRUH, ZH6QIU8A, JCTP8VXP) — the
  panel conflates them often; resolve by checking whether there's a real user in the loop or two
  genuinely separate evaluation events (NRVQT89E-style).
- **Agent-panel/cross-model check** — flagged when the panel's primary proposal is `theme:ai-review`.
  Ask: is more than one agent involved (`agent-panel`), and if so, are they different vendors
  (`cross-model`)? `theme:ai-review` itself needs no change either way.
- **Already resolved this session** — no action needed unless you disagree with the recorded call.

---

## Section B — Unanimous-Demote Light Confirmations (18)

All three models flagged `demote:context`. Confirm the demote, or rescue per the §30 sole-exemplar
exception.

### 5AVZQCVU — With Great Capabilities Come Great Responsibilities
- **APA:** Khoo, S., Foo, J., & Lee, R. K.-W. (2025). *With Great Capabilities Come Great Responsibilities: Introducing the Agentic Risk & Capability Framework for Governing Agentic AI Systems*. arXiv.org. https://doi.org/10.48550/arXiv.2512.22211
- Confirm: **org-governance** | tripwires: demote:context (all 3), sprawl:codex=7
- New facet check: none triggered (no built-system, no ai-review).

### 5DCQDB4C — Effective human oversight of AI-based systems
- **APA:** Langer, M., Baum, K., & Schlicker, N. (2024). Effective human oversight of AI-based systems: a signal detection perspective on the detection of inaccurate and unfair outputs. *Minds and Machines*, *35*(1), 1. https://doi.org/10.1007/s11023-024-09701-0
- Confirm: **automation-bias** | tripwires: demote:context (all 3)
- New facet check: none triggered.

### 5RLPIA3K — Adversarial verification as reference architecture for EU AI Act Art. 14
- **APA:** Eric Swidey. (2026). *Adversarial verification as reference architecture for EU AI act article 14 compliance in employment AI*. 10. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5958495
- Confirm: **regulatory-compliance** | tripwires: unstable (all 3), demote:context (all 3), sprawl:codex=7
- New facet check: **ladder** — `built-system` in facets (2/3 noted). No method-* co-proposed;
  check where it lands (likely self-test or evaluated-synthetic).

### 6TZHUCMD — Source code guardrail
- **APA:** Sharma, R., & Gupta, A. (2026). Source code guardrail: AI driven solution to distinguish critical vs. Generic code for enterprise LLM security. In Yang G., Liu S., Su C., Otsuka A., & Lian Z. (Eds.), *Lect. Notes Comput. Sci.: 16172 LNCS* (pp. 449–458). Springer Science and Business Media Deutschland GmbH. Scopus. https://doi.org/10.1007/978-981-95-2961-2_23
- Confirm: **org-governance** | tripwires: unstable:opus, demote:context (all 3)
- New facet check: **exclusivity conflict** — `built-system` (3/3) + `method-field-study` (2/3)
  co-proposed. Check for a real user in the loop before assigning either.

### 7ZMU5AIF — Overseeing Agents Without Constant Oversight
- **APA:** Grunde-McLaughlin, M., Mozannar, H., Murad, M., Chen, J., Amershi, S., & Fourney, A. (2026). *Overseeing Agents Without Constant Oversight: Challenges and Opportunities*. arXiv. https://doi.org/10.48550/arXiv.2602.16844
- Confirm: **oversight-explanation** | tripwires: demote:context (all 3)
- New facet check: none — `design-only` present, excludes the ladder by definition.

### 84D2AMVM — Realizing the promise of AI governance involving humans-in-the-loop
- **APA:** McKay, M. H. (2024). Realizing the promise of AI governance involving humans-in-the-loop. In Degen H. & Ntoa S. (Eds.), *Lect. Notes Comput. Sci.: 15382 LNCS* (pp. 107–123). Springer Science and Business Media Deutschland GmbH. Scopus. https://doi.org/10.1007/978-3-031-76827-9_7
- Confirm: **automation-bias** | tripwires: demote:context (all 3)
- New facet check: none triggered.

### 9MV2IVNU — Human-in-the-loop isn't a checkbox
- **APA:** Eze, S. (2026). *Human-in-the-loop isn’t a checkbox: designing meaningful intervention in automated AI decisions*. 24. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6552159
- Confirm: **oversight-theater** | tripwires: demote:context (all 3), sprawl:codex=7
- New facet check: none — `design-only` present.

### E689ZAXC — Review makes workers less likely to revise AI output
- **APA:** Zhou, P., & Zhao, Y. (2026). *Review makes workers less likely to revise AI output*. 15. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6325399
- Confirm: **automation-bias** | tripwires: unstable:opus, unstable:codex, demote:context (all 3)
- New facet check: none — `method-experiment` present, no `built-system` co-proposed.

### EB49Q8QM — The rationality of automation bias in security operation centers
- **APA:** Tilbury, J., & Flowerday, S. (2024). The rationality of automation bias in security operation centers. *Journal of Information Systems Security*, *20*(2), 89–109. Scopus. https://www.researchgate.net/profile/Jack-Tilbury-2/publication/387902110_The_Rationality_of_Automation_Bias_in_Security_Operation_Centers/links/67816f8c8210a977a17fb3a1/The-Rationality-of-Automation-Bias-in-Security-Operation-Centers.pdf
- Confirm: **automation-bias** | tripwires: demote:context (all 3)
- New facet check: none triggered.

### JVWUYDME — Scapegoat-as-a-service
- **APA:** Jessee, R. T. (2026). *Scapegoat-as-a-service: moving from “human-in-the-loop” to “human-in-command” in regulated systems*. 20. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6052874
- Confirm: **hitl-workflow** | tripwires: demote:context (all 3), sprawl:codex=10
- New facet check: none — `design-only` present.

### NGIH5T4C — The evolving landscape of code review
- **APA:** Batte, B. (2025). *The evolving landscape of code review: leveraging artificial intelligence for enhanced software quality and developer productivity*. 7. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5214508
- Confirm: **ai-review** | tripwires: demote:context (all 3)
- New facet check: **agent-panel/cross-model** — primary is `ai-review`; check reviewer
  architecture. No `built-system` co-proposed.

### RNDPW7VA — Measuring Progress on Scalable Oversight for Large Language Models
- **APA:** Bowman, S. R., Hyun, J., Perez, E., Chen, E., Pettit, C., Heiner, S., Lukošiūtė, K., Askell, A., Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McKinnon, C., Olah, C., Amodei, D., Amodei, D., Drain, D., Li, D., Tran-Johnson, E., … Kaplan, J. (2022). *Measuring Progress on Scalable Oversight for Large Language Models*. arXiv.org. https://doi.org/10.48550/arXiv.2211.03540
- Confirm: **oversight-explanation** | tripwires: demote:context (all 3)
- New facet check: none on this pair (primary isn't `ai-review`, no `built-system`). Side note:
  this is the paper where "cross-examine" appears in the corpus — describes a *human*
  cross-examining a single AI, not agent-vs-agent; doesn't feed `agent-panel`/`cross-model`.

### TW4I6DU6 — On the Quest for Effectiveness in Human Oversight
- **APA:** Sterz, S., Baum, K., Biewer, S., Hermanns, H., Lauber-Rönsberg, A., Meinel, P., & Langer, M. (2024, June 5). On the Quest for Effectiveness in Human Oversight: Interdisciplinary Perspectives. *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency*. https://doi.org/10.1145/3630106.3659051
- Confirm: **hitl-workflow** | tripwires: unstable:opus, unstable:codex, demote:context (all 3)
- New facet check: none triggered.

### WZCULPXN — AI tools in web application development
- **APA:** Sulova, S. (2025). Artificial intelligence tools in web application development – advantages and challenges. *2025 International Conference on Intelligent Computing and Next Generation Networks (ICNGN)*, 1–5. https://doi.org/10.1109/ICNGN67480.2025.11413758
- Confirm: **org-governance** | tripwires: demote:context (all 3)
- New facet check: none triggered.

### XK3P9C96 — When Should Users Check? (confirmation frequency)
- **APA:** Zhou, J., Roy, A., Gupta, S., Weitekamp, D., & MacLellan, C. J. (2026, April 13). When Should Users Check? Modeling Confirmation Frequency in Multi-Step Agentic AI Tasks. *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3772318.3790655
- Confirm: **risk-routing** | tripwires: demote:context (all 3)
- New facet check: **exclusivity conflict** — `built-system` + `method-experiment` both 3/3.
  Side note: an earlier corpus check this session found this paper names both Claude and GPT —
  worth a look for `agent-panel`/`cross-model` too, even though the primary proposal isn't `ai-review`.

### XRTVITVP — Steering LLMs via scalable interactive oversight
- **APA:** Zhou, E., Xi, Z., Ma, L., Zhang, Z., Dou, S., Lei, Z., Wang, G., Zheng, R., Yan, H., Gui, T., Zhang, Q., & Huang, X. (2026). *Steering LLMs via scalable interactive oversight* (2602.04210). arXiv. https://arxiv.org/abs/2602.04210
- Confirm: **hitl-workflow** | tripwires: unstable:opus, demote:context (all 3)
- New facet check: **exclusivity conflict** — `built-system` + `method-experiment` both 3/3.

### ZGST9CY6 — Designing meaningful human oversight in AI
- **APA:** Liming Zhu, Qinghua Lu, Ding Ming, Sung Une Lee, & Chen Wang. (2025). *Designing meaningful human oversight in AI*. 16. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5501939
- Confirm: **oversight-explanation** | tripwires: sprawl:opus=7, demote:context (all 3), sprawl:codex=9
- New facet check: none — `design-only` present.

### ZSB2S59N — Designing guardrails
- **APA:** Kumar, A. (2026). Designing guardrails: ensuring responsible AI behavior. *GenAI and LLMs for Beyond 5G Networks*, 107–144. Scopus. https://doi.org/10.1007/978-3-032-06418-9_5
- Confirm: **org-governance** | tripwires: demote:context (all 3), sprawl:codex=7
- New facet check: none triggered.

---

## Section C — Light Confirmations, 2/1 with tripwires (60)

Confirm the modal proposal or flip to the dissent; tripwires tell you where to look.

### 27YULT5I — AI-assisted code migration ethics in regulated financial systems
- **APA:** Sharma, R. (2026). *The ethics of AI-assisted code migration in regulated financial systems: accountability, transparency, and human oversight in LLM-driven software conversion*. 15. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6252918
- Confirm: **org-governance** | tripwires: sprawl:codex=10
- New facet check: none triggered.

### 2KPHQ5IV — Scaling human-AI coding collaboration / governable consensus layer
- **APA:** Wang, T., Hao, Z., Wu, Y., Wu, W., Lin, Q., Dong, H., Yuan, N. J., & Xiong, H. (2026). *Scaling human-AI coding collaboration requires a governable consensus layer* (2604.17883). arXiv. https://arxiv.org/abs/2604.17883
- Confirm: **provenance-auditability** | tripwires: sprawl:opus=7, sprawl:codex=10
- New facet check: none — `design-only` present.

### 34ELRWJH — The hidden legal minefield of vibe coding
- **APA:** Goodhue, J. (2025). *The hidden legal minefield: how AI-assisted “vibe coding” amplifies software development risks and how technology can provide solutions*. 10. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5403926
- Confirm: **regulatory-compliance** | tripwires: demote:context:gemini
- New facet check: none triggered.

### 3ZVMBGPB — Rethinking code review in the age of AI
- **APA:** Kamalı, H. Ö., Tuna, E., Haratian, V., & Tüzün, E. (2026). *Rethinking code review in the age of AI: a vision for agentic code review* (arXiv:2605.17548; Version v1). arXiv. https://arxiv.org/abs/2605.17548v1
- Confirm: **ai-review** | tripwires: sprawl:codex=11
- New facet check: **agent-panel/cross-model** — primary is `ai-review`. `design-only` present so
  no ladder question.

### 4AXDVW7J — Ethical prompt engineering for AI-driven SE
- **APA:** Migliarini, P., Autili, M., Inverardi, P., & Pelliccione, P. (2026). Ethical prompt engineering for AI-driven SE: evidence-informed interaction-time governance roadmap to 2030. *ACM Trans. Softw. Eng. Methodol.* https://doi.org/10.1145/3801980
- Confirm: **org-governance** | tripwires: unstable:codex, demote:context:codex, demote:context:gemini
- New facet check: none triggered.

### 4PSM6ZCD — Is vibe coding safe? (agent-generated code vulnerability benchmarking)
- **APA:** Zhao, S., Wang, D., Zhang, K., Luo, J., Li, Z., & Li, L. (2025). *Is vibe coding safe? Benchmarking vulnerability of agent-generated code in real-world tasks* (arXiv:2512.03262). arXiv. https://arxiv.org/abs/2512.03262
- Confirm: **ai-code-insecurity** | tripwires: demote:context:codex, demote:context:gemini
- New facet check: none — `method-experiment` present, no `built-system` co-proposed.

### 59ZW4R58 — The gotchas of AI coding and vibe coding
- **APA:** Maes, S. (2025). *The gotchas of AI coding and vibe coding. It’s all about support and maintenance*. OSF Preprints. https://doi.org/10.31219/osf.io/kjz9t_v1
- Confirm: **quality-debt** | tripwires: —
- New facet check: none — `design-only` present.

### 5DI9B43K — Towards verified code reasoning by LLMs
- **APA:** Sistla, M., Balakrishnan, G., Rondon, P., Cambronero, J., Tufano, M., & Chandra, S. (2025). *Towards verified code reasoning by LLMs* (arXiv:2509.26546; Version v2). arXiv. https://arxiv.org/abs/2509.26546v2
- Confirm: **formal-methods** | tripwires: —
- New facet check: **ladder** — `built-system` (3/3), no method-* co-proposed. Check ladder rung.

### 5I2W8IC6 — Mapping the trust terrain: LLMs in SE
- **APA:** Khati, D., Liu, Y., Palacio, D. N., Zhang, Y., & Poshyvanyk, D. (2025). Mapping the trust terrain: LLMs in software engineering - insights and perspectives. *ACM Trans. Softw. Eng. Methodol.* https://doi.org/10.1145/3771282
- Confirm: **automation-bias** | tripwires: demote:context:codex, demote:context:gemini
- New facet check: none triggered (method-self-report present, no built-system).

### 6F3S8IB7 — HAIF: human-AI integration framework
- **APA:** Bara, M. (2026). *HAIF: a human-AI integration framework for hybrid team operations* (2602.07641). arXiv. https://arxiv.org/abs/2602.07641
- Confirm: **risk-routing** | tripwires: unstable:opus, unstable:gemini, sprawl:codex=9
- New facet check: none — `design-only` present.

### 6ZW9QNQH — Position: vibe coding needs vibe reasoning
- **APA:** Mitchell, J., & Shaaban, Y. (2025). Position: vibe coding needs vibe reasoning: improving vibe coding with formal verification. *Proceedings of the 1st ACM SIGPLAN International Workshop on Language Models and Programming Languages, LMPL ’25*, 84–90. https://doi.org/10.1145/3759425.3763390
- Confirm: **formal-methods** | tripwires: sprawl:codex=8
- New facet check: **ladder** — `built-system` (3/3), no method-* co-proposed.

### 72W6R4JG — Vibe-coding: feedback-based automated verification
- **APA:** Töpfer, M., Plášil, F., Bureš, T., & Hnětynka, P. (2026). *Vibe-coding: feedback-based automated verification with no human code inspection, a feasibility study* (2604.14867). arXiv. https://arxiv.org/abs/2604.14867
- Confirm: **rules-based-checks** | tripwires: unstable:codex
- New facet check: **ladder** — `built-system` (3/3), no method-* co-proposed.

### 8KJEKBGT — Software vulnerability and functionality assessment using LLMs
- **APA:** Jensen, R. I. T., V. Tawosi, & S. Alamir. (2024). Software vulnerability and functionality assessment using LLMs. *2024 IEEE/ACM International Workshop on Natural Language-Based Software Engineering (NLBSE)*, 25–28. https://ieeexplore.ieee.org/document/10647161
- Confirm: **ai-review** | tripwires: demote:context:codex, demote:context:gemini
- New facet check: **agent-panel/cross-model** — primary is `ai-review`. `method-experiment`
  present, no `built-system` co-proposed (no ladder question).

### 8MXATG38 — AI-augmented SE for rapid feature delivery/ops
- **APA:** Karuppuchamy, S. (2026). AI-augmented software engineering for rapid feature delivery and operations automation. *2026 IEEE 16th Annual Computing and Communication Workshop and Conference (CCWC)*, 0607–0614. https://doi.org/10.1109/CCWC67433.2026.11393761
- Confirm: **org-governance** | tripwires: sprawl:codex=7
- New facet check: **rich ladder case** — `adopted` + `built-system` + `method-field-study` +
  `method-mining` + `method-self-report` all co-proposed (3/3 each). Worth a careful read: likely
  legitimate (real deployment = `adopted`/`method-field-study` genuinely apply together), but
  confirm there isn't also a separate self-constructed sub-evaluation that would need
  `evaluated-synthetic` instead/additionally.

### 95CPB7CF — Beyond the 'diff': agentic entropy
- **APA:** Casserini, M., Facchini, A., & Ferrario, A. (2026). *Beyond the “diff”: addressing agentic entropy in agentic software development*. https://arxiv.org/abs/2604.16323
- Confirm: **oversight-explanation** | tripwires: sprawl:codex=7
- New facet check: none — `design-only` present.

### 96XE669R — Vibe checker (human-preference code evaluation)
- **APA:** Zhong, M., Zhou, X., Chang, T.-Y., Wang, Q., Xu, N., Si, X., Garrette, D., Upadhyay, S., Liu, J., Han, J., Schillings, B., & Sun, J. (2025). *Vibe checker: aligning code evaluation with human preference* (2510.07315). arXiv. https://arxiv.org/abs/2510.07315
- Confirm: **rules-based-checks** | tripwires: unstable:gemini, demote:context:opus, demote:context:gemini
- New facet check: **already resolved this session** — `evaluated-synthetic` confirmed (new
  instrument built on established benchmarks = synthetic, not benchmark; no public release found).

### 9R6TGN82 — Training LMs with program analysis feedback
- **APA:** Yao, F., Wang, Z., Liu, L., Cui, J., Zhong, L., Fu, X., Mai, H., Krishnan, V., Gao, J., & Shang, J. (2025). *Training language models to generate quality code with program analysis feedback* (2505.22704). arXiv. https://arxiv.org/abs/2505.22704
- Confirm: **rules-based-checks** | tripwires: demote:context:opus
- New facet check: **ladder** — `built-system` (3/3), no method-* co-proposed.

### B4TVIG5Y — Maturity model for AI-assisted software development
- **APA:** Tereci, S., Gökalp, E., & Dikici, A. (2026). Toward a maturity model for AI-assisted software development: conceptual framework and research agenda. *2026 5th International Informatics and Software Engineering Conference (IISEC)*, 656–661. https://doi.org/10.1109/IISEC69317.2026.11418422
- Confirm: **org-governance** | tripwires: demote:context:gemini
- New facet check: none triggered.

### B7APR28B — Human-in-the-loop software development agents (survey)
- **APA:** Pasuksmit, J., Takerngsaksiri, W., Thongtanunam, P., Tantithamthavorn, C., Zhang, R., Wang, S., Jiang, F., Li, J., Cook, E., Chen, K., & Wu, M. (2025, April 25). *Human-In-the-loop software development agents: challenges and future directions*. https://arxiv.org/abs/2506.11009
- Confirm: **ai-review** | tripwires: demote:context:gemini
- New facet check: **agent-panel/cross-model** — primary is `ai-review`. Also **ladder** —
  `built-system` noted 2/3, worth a look.

### BLR3XE3I — Vibe coding in product teams
- **APA:** Li, J., Hou, Y., Lin, L., Zhu, R., Cao, H., & El Ali, A. (2026). Vibe coding in product teams: reconfiguring AI-assisted workflows, prototyping, and collaboration. *Proceedings of the 5th Annual Symposium on Human-Computer Interaction for Work, CHIWORK ’26*, 1–16. https://doi.org/10.1145/3808045.3808062
- Confirm: **automation-bias** | tripwires: unstable:gemini, sprawl:codex=9
- New facet check: none — `method-self-report`, no `built-system`.

### BU73N7PC — Moving Faster and Reducing Risk (LLMs in release deployment)
- **APA:** Abreu, R., Murali, V., Rigby, P. C., Maddila, C., Sun, W., Ge, J., Chinniah, K., Mockus, A., Mehta, M., & Nagappan, N. (2025, April). Moving Faster and Reducing Risk: Using LLMs in Release Deployment. *2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP)*. https://doi.org/10.1109/ICSE-SEIP66354.2025.00045
- Confirm: **risk-routing** | tripwires: unstable:codex
- New facet check: **ladder** — `adopted` + `built-system` (3/3), no method-* co-proposed. Likely
  `adopted` is correct (real deployment) — confirm it's not just `built-system`-alone being
  over-read as adopted.

### C88VGWMI — Constitutional spec-driven development
- **APA:** Marri, S. R. (2026). *Constitutional spec-driven development: enforcing security by construction in AI-assisted code generation* (2602.02584). arXiv. https://arxiv.org/abs/2602.02584
- Confirm: **ai-code-insecurity** | tripwires: unstable (all 3), demote:context:opus, demote:context:gemini
- New facet check: **exclusivity conflict** — `built-system` (3/3) + `method-experiment` (2/3
  noted). Already spot-checked this session (0 participant/contractor mentions found) — current
  `evaluated-synthetic` tag likely correct, but the panel's method-experiment tripwire is worth a
  quick confirm given the demote/instability tripwires stacked on this one too.

### CI93QRUH — HiLDE: human-in-the-loop decoding
- **APA:** E. A. González, R. Rothkopf, S. Lerner, & N. Polikarpova. (2025). HiLDE: intentional code generation via human-in-the-loop decoding. *2025 IEEE Symposium on Visual Languages and Human-Centric Computing (VL/HCC)*, 222–233. https://doi.org/10.1109/VL-HCC65237.2025.00032
- Confirm: **oversight-explanation** | tripwires: unstable:codex
- New facet check: **already resolved this session** — `method-experiment` confirmed (18 real
  participants, 4 programming tasks), `evaluated-synthetic` removed.

### DJMBHHZN — MOSAICO: AI-agent community orchestration
- **APA:** Tisi, M., Cabot, J., Di Ruscio, D., & Garcia-Dominguez, A. (2025). MOSAICO: management, orchestration and supervision of AI-agent COmmunities for reliable AI in software engineering. In Fonseca C.M. & Fumagalli M. (Eds.), *CEUR Workshop Proc.* (Vol. 4050). CEUR-WS. Scopus. https://ceur-ws.org/Vol-4050/paper07.pdf
- Confirm: **ai-review** | tripwires: demote:context:opus
- New facet check: **agent-panel/cross-model** — primary is `ai-review`, and the title itself
  suggests a multi-agent architecture. `design-only` present, no ladder question.

### E5SQKRH7 — Assessing Correctness in LLM-Based Code Generation
- **APA:** Sharma, A., & David, C. (2025). *Assessing Correctness in LLM-Based Code Generation via Uncertainty Estimation*. arXiv.org. https://doi.org/10.48550/arXiv.2502.11620
- Confirm: **formal-methods** | tripwires: unstable:codex, unstable:gemini
- New facet check: **ladder** — `built-system` (3/3), no method-* co-proposed.

### E9RAWBDT — Good vibrations? (qualitative co-creation study)
- **APA:** Pimenova, V., Fakhoury, S., Bird, C., Storey, M.-A., & Endres, M. (2025). *Good vibrations? A qualitative study of Co-creation, communication, flow, and trust in vibe coding* (2509.12491). arXiv. https://arxiv.org/abs/2509.12491
- Confirm: **automation-bias** | tripwires: unstable:opus, sprawl:codex=10
- New facet check: none — no `built-system`.

### F2C2DWSI — AI-Assisted Programming Decreases Productivity of Experienced Developers
- **APA:** Xu, F., Medappa, P. K., Tunç, M., Vroegindeweij, M., & Fransoo, J. C. (2025). *AI-Assisted Programming Decreases the Productivity of Experienced Developers by Increasing the Technical Debt and Maintenance Burden*. arXiv preprint. https://doi.org/10.2139/ssrn.5521379
- Confirm: **oversight-scaling-inversion** | tripwires: unstable:opus
- New facet check: none — no `built-system`.

### ID7IN65K — To copilot and beyond (22 AI systems developers want)
- **APA:** Choudhuri, R., Bird, C., Badea, C., & Sarma, A. (2026). *To copilot and beyond: 22 AI systems developers want built* (2604.07830). arXiv. https://arxiv.org/abs/2604.07830
- Confirm: **hitl-workflow** | tripwires: sprawl (all 3, 8-10)
- New facet check: none — no `built-system`.

### JCTP8VXP — ZORO: active rules for reliable vibe coding
- **APA:** Ma, J., Wang, S., Kung, J. H., & Chilton, L. B. (2026). *ZORO: active rules for reliable vibe coding* (2604.15625). arXiv. https://arxiv.org/abs/2604.15625
- Confirm: **hitl-workflow** | tripwires: unstable:codex, sprawl:codex=7
- New facet check: **already resolved this session** — `method-experiment` confirmed (12 real
  participants, real coding tasks), `evaluated-synthetic` removed (no separate tool-only
  evaluation found in the text).

### KF5MGIBI — Fine-Tuning LLMs for comprehensibility of review comments
- **APA:** Yu, Y., Rong, G., Shen, H., Zhang, H., Shao, D., Wang, M., Wei, Z., Xu, Y., & Wang, J. (2024). Fine-Tuning Large Language Models to Improve Accuracy and Comprehensibility of Automated Code Review. *ACM Trans. Softw. Eng. Methodol.* https://doi.org/10.1145/3695993
- Confirm: **oversight-explanation** | tripwires: unstable:gemini
- New facet check: **ladder** — `built-system` (3/3), no method-* co-proposed.

### LCPH3THV — LLM-as-a-judge for software engineering (lit review)
- **APA:** He, J., Shi, J., Zhuo, T. Y., Treude, C., Sun, J., Xing, Z., Du, X., & Lo, D. (2026). LLM-as-a-judge for software engineering: literature review, vision, and the road ahead. *ACM Transactions on Software Engineering and Methodology*. https://doi.org/10.1145/3797276
- Confirm: **ai-review** | tripwires: demote:context:codex, demote:context:gemini
- New facet check: **agent-panel/cross-model**, with a caveat — `lit-review` facet present, so
  confirm this is really *about* an ai-review architecture rather than surveying others' work
  before applying either new facet.

### LGZXFLSJ — Causal mapping of GenAI risks in software development
- **APA:** Hein, D. K., Persson, J., Jensen, V. V., Bruun, A. R., & Jaatun, M. G. (2025). *Causal mapping of the risks of using generative ai in software development*. 28. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5273073
- Confirm: **org-governance** | tripwires: demote:context:gemini
- New facet check: none — no `built-system`.

### NZJST99D — Where Do AI Coding Agents Fail? (failed agentic PRs)
- **APA:** Ehsani, R., Pathak, S., Rawal, S., Mujahid, A. A., Imran, M. M., & Chatterjee, P. (2026). *Where Do AI Coding Agents Fail? An Empirical Study of Failed Agentic Pull Requests in GitHub*. arXiv.org. https://doi.org/10.48550/arXiv.2601.15195
- Confirm: **oversight-scaling-inversion** | tripwires: unstable:gemini
- New facet check: none — no `built-system`.

### PD297DUM — My code is less secure with gen AI (developer perceptions survey)
- **APA:** Kudriavtseva, A., Hotak, N. A., & Gadyatskaya, O. (2025). My code is less secure with gen AI: surveying developers’ perceptions of the impact of code generation tools on security. *Proc ACM Symp Appl Computing*, 1637–1646. Scopus. https://doi.org/10.1145/3672608.3707778
- Confirm: **automation-bias** | tripwires: unstable:gemini
- New facet check: none — no `built-system`.

### PPMTM4DG — Fight fire with fire (trusting ChatGPT on code tasks)
- **APA:** X. Yu, L. Liu, X. Hu, J. W. Keung, J. Liu, & X. Xia. (2024). Fight fire with fire: how much can we trust ChatGPT on source code-related tasks? *IEEE Transactions on Software Engineering*, *50*(12), 3435–3453. https://doi.org/10.1109/TSE.2024.3492204
- Confirm: **ai-review** | tripwires: demote:context:gemini
- New facet check: **agent-panel/cross-model** — primary is `ai-review`. `method-experiment`
  present, no `built-system` (no ladder question).

### PR4GS7SP — Automating correctness assessment for security contexts
- **APA:** Cotroneo, D., Foggia, A., Improta, C., Liguori, P., & Natella, R. (2023). *Automating the correctness assessment of AI-generated code for security contexts*. https://doi.org/10.1016/j.jss.2024.112113
- Confirm: **rules-based-checks** | tripwires: unstable:codex
- New facet check: **ladder** — `built-system` (3/3), no method-* co-proposed.

### QUXRX9ZL — The prompt-refactor-verify (PRV) cycle
- **APA:** N. Yanev, I. Getova, E. Mihaylova, I. Kostadinova, M. Bankovska, & G. Dimitrov. (2025). The prompt–refactor–verify (PRV) cycle: a human-centered framework for AI-assisted programming. *2025 6th International Conference on Communications, Information, Electronic and Energy Systems (CIEES)*, 1–5. https://doi.org/10.1109/CIEES66347.2025.11300239
- Confirm: **hitl-workflow** | tripwires: unstable:opus
- New facet check: none — `design-only` present.

### R9CDT9KB — Trust-calibrated multi-stage LLM pipeline for vulnerability assessment
- **APA:** A. Mahmud, Y. Rawajfih, & R. Arnold. (2025). Trust-calibrated multi-stage large language model pipeline for vulnerability assessment in DevSecOps workflows. *2025 Annual Computer Security Applications Conference Workshops (ACSAC Workshops)*, 459–466. https://doi.org/10.1109/ACSACW69556.2025.00074
- Confirm: **risk-routing** | tripwires: unstable:gemini
- New facet check: **ladder** — `built-system` (3/3), no method-* co-proposed.

### RG4A4D6K — From black box to open book (transparency imperative)
- **APA:** N. Watson, & M. Van Italie. (2025). From black box to open book: an emerging transparency imperative in generative AI codebases. *2025 IEEE Conference on Artificial Intelligence (CAI)*, 1369–1374. https://doi.org/10.1109/CAI64502.2025.00266
- Confirm: **provenance-auditability** | tripwires: sprawl:codex=7, demote:context:codex, demote:context:gemini
- New facet check: none — no `built-system`.

### RPHK78A9 — Vibe coding: building production-grade software
- **APA:** Kim, G., & Yegge, S. (2025). *Vibe coding: building production-grade software with GenAI, chat, agents, and beyond* (Kindle Ed.). IT Revolution. https://openalex.org/W7114300968
- Confirm: **hitl-workflow** | tripwires: unstable:opus, unstable:gemini, sprawl (opus/codex), demote:context:gemini
- New facet check: none by strict rule (`method-field-study` noted 2/3 but no `built-system`) —
  still worth a glance given how many tripwires are stacked here.

### RX9SICP9 — IACDM: interactive adversarial convergence development methodology
- **APA:** Moreira, J. (2026). *IACDM: interactive adversarial convergence development methodology -- a structured framework for AI-assisted software development* (2604.16399). arXiv. https://arxiv.org/abs/2604.16399
- Confirm: **hitl-workflow** | tripwires: unstable:opus, sprawl:codex=9
- New facet check: **rich ladder case** — `adopted` + `built-system` (3/3) + `method-field-study`
  (2/3 noted). Same pattern as 8MXATG38 — confirm real deployment vs. self-constructed component.

### T2EG4BE2 — Vibe coding in practice: flow, technical debt, guidelines
- **APA:** Waseem, M., Ahmad, A., Kemell, K.-K., Rasku, J., Lahti, S., Mäkelä, K., & Abrahamsson, P. (2025). *Vibe coding in practice: flow, technical debt, and guidelines for sustainable use* (2512.11922). arXiv. https://arxiv.org/abs/2512.11922
- Confirm: **quality-debt** | tripwires: sprawl:opus=9, sprawl:codex=12
- New facet check: none by strict rule (`method-field-study`/`method-mining` present, no
  `built-system`).

### T3XTXIXW — CoTDeceptor (adversarial code obfuscation vs. CoT-enhanced review)
- **APA:** Li, H., Li, M., Zuo, J., Li, S., Li, X., Wu, H., Lu, Y., & He, X. (2025). *CoTDeceptor:adversarial code obfuscation against CoT-enhanced LLM code agents* (arXiv:2512.21250; Version v1). arXiv. https://arxiv.org/abs/2512.21250v1
- Confirm: **ai-review** | tripwires: unstable:gemini
- New facet check: **agent-panel/cross-model** — primary is `ai-review`. Ladder position already
  resolved this session — tagged `evaluated-benchmark`. The `method-experiment` noted (2/3) is
  likely a panel miscall (same pattern as WBS9U5N7/X7EN6DXZ below) — worth a fast confirm, not a
  full re-derivation.

### TA6GIUK2 — The specification as quality gate
- **APA:** Zietsman, C. (2026). *The specification as quality gate: three hypotheses on AI-assisted code review* (arXiv:2603.25773; Version v1). arXiv. https://arxiv.org/abs/2603.25773v1
- Confirm: **ai-review** | tripwires: —
- New facet check: **agent-panel/cross-model** — primary is `ai-review`. `method-experiment`
  present, no `built-system` (no ladder question).

### TJH7QFAX — Code for machines, not just humans (AI-friendliness/code health)
- **APA:** Borg, M., Hagatulah, N., Tornhill, A., & Söderberg, E. (2026). *Code for machines, not just humans: quantifying AI-friendliness with code health metrics* (2601.02200). arXiv. https://arxiv.org/abs/2601.02200
- Confirm: **risk-routing** | tripwires: unstable:codex
- New facet check: none — `method-experiment` present, no `built-system`.

### U9VZQXGI — Magentic-UI
- **APA:** Mozannar, H., Bansal, G., Tan, C., Fourney, A., Dibia, V., Chen, J., Gerrits, J., Payne, T., Maldaner, M. K., Grunde-McLaughlin, M., Zhu, E., Bassman, G., Alber, J., Chang, P., Loynd, R., Niedtner, F., Kamar, E., Murad, M., Hosn, R., & Amershi, S. (2025). *Magentic-UI: Towards Human-in-the-loop Agentic Systems*. arXiv.org. https://doi.org/10.48550/arXiv.2507.22358
- Confirm: **hitl-workflow** | tripwires: demote:context:codex, demote:context:gemini
- New facet check: **already resolved this session** — genuine two-event paper: `evaluated-benchmark`
  confirmed (GAIA/AssistantBench/WebVoyager, established agentic benchmarks) **and**
  `method-experiment` added (separate 12-user study). Both stand.

### VFNJSZD9 — Beyond SAST and DAST (unified security testing architecture)
- **APA:** Michel Hjazeen. (2026). *Beyond SAST and DAST: a unified security testing architecture for autonomous coding agents*. 17. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6271220
- Confirm: **ai-review** | tripwires: unstable:opus, unstable:gemini, sprawl:codex=9
- New facet check: **agent-panel/cross-model** — primary is `ai-review`. `design-only` present, no
  ladder question.

### VTDG995V — Calibration and Correctness of Language Models for Code
- **APA:** Spiess, C., Gros, D., Pai, K. S., Pradel, M., Rabin, M. R. I., Alipour, A., Jha, S., Devanbu, P., & Ahmed, T. (2025, April). Calibration and Correctness of Language Models for Code. *2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE)*. https://doi.org/10.1109/ICSE55347.2025.00040
- Confirm: **ai-review** | tripwires: unstable:opus
- New facet check: **agent-panel/cross-model** — primary is `ai-review`. `method-experiment` noted
  (2/3), no `built-system` (no ladder question).

### VZ27QUPQ — Identifying and mitigating API misuse in LLMs
- **APA:** Zhuo, T. Y., He, J., Sun, J., Xing, Z., Lo, D., Grundy, J., & Du, X. (2026). Identifying and mitigating API misuse in large language models. *IEEE Transactions on Software Engineering*, *52*(3), 855–873. https://doi.org/10.1109/TSE.2026.3651566
- Confirm: **quality-debt** | tripwires: unstable:opus
- New facet check: **already resolved this session** — `evaluated-synthetic` confirmed ("our
  benchmark" is self-labeled, not a field-recognized standard; release-upon-acceptance plan noted
  but not yet adopted by anyone).

### WBS9U5N7 — Cognitive camouflage (specification gaming evading review)
- **APA:** Alami, D. (2026). *Cognitive camouflage: specification gaming in LLM-generated code evades holistic evaluation but not adversarial execution*. 9. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6512960
- Confirm: **ai-review** | tripwires: unstable:opus
- New facet check: **agent-panel/cross-model** — primary is `ai-review`. Ladder already confirmed
  this session as `evaluated-synthetic` (0 participants found; the panel's `method-experiment`
  (3/3!) proposal here is a clean example of the exact machine-only confusion this facet pair was
  built to catch — worth knowing as a reference case, not re-deriving).

### WH2PIBNQ — Responsible vibe coding: architecture and research agenda
- **APA:** Elgendy, I. A., Dwivedi, Y. K., Al-Sharafi, M. A., Hosny, M., Helal, M. Y. I., Crick, T., Hughes, L., Alwahaishi, S., Mahmud, M., Dutot, V., & Al-Busaidi, A. S. (2026). Responsible vibe coding: architecture, opportunities, and research agenda. *Journal of Computer Information Systems*. Scopus. https://doi.org/10.1080/08874417.2026.2621186
- Confirm: **org-governance** | tripwires: sprawl:codex=10, demote:context:codex, demote:context:gemini
- New facet check: none — no `built-system`.

### WPWF7A32 — DevLicOps (licensing risk mitigation framework)
- **APA:** Sharma, P. N., Wright, L., Herfurth, A., Sokiyna, M., Sharma, P. N., Das, S., & Siponen, M. (2025). *DevLicOps: a framework for mitigating licensing risks in AI-generated code* (2508.16853). arXiv. https://arxiv.org/abs/2508.16853
- Confirm: **org-governance** | tripwires: sprawl:codex=8
- New facet check: none — no `built-system`.

### WUUDHL8R — AI-driven refactoring pipeline (data clumps)
- **APA:** Baumgartner, N., Iyenghar, P., Schoemaker, T., & Pulvermüller, E. (2024). AI-driven refactoring: a pipeline for identifying and correcting data clumps in git repositories. *Electronics (Switzerland)*, *13*(9). Scopus. https://doi.org/10.3390/electronics13091644
- Confirm: **ai-review** | tripwires: unstable:codex
- New facet check: **agent-panel/cross-model** — primary is `ai-review`. Also **ladder** —
  `built-system` (3/3), no method-* co-proposed.

### WWBUQM7V — Developers' perspective on ChatGPT-generated code trustworthiness
- **APA:** Rabani, Z. S., Khorashadizadeh, H., Abdollahzade, S., Groppe, S., & Ghofrani, J. (2023). Developers’ perspective on trustworthiness of code generated by ChatGPT: insights from interviews. In M. A. Jabbar, S. Tiwari, F. Ortiz-Rodríguez, S. Groppe, & T. Bano Rehman (Eds.), *Applied Machine Learning and Data Analytics*. https://doi.org/10.1007/978-3-031-55486-5_16
- Confirm: **quality-debt** | tripwires: demote:context:gemini
- New facet check: none — no `built-system`.

### X7EN6DXZ — Measuring and exploiting contextual bias in LLM-assisted security code review
- **APA:** Mitropoulos, D., Alexopoulos, N., Alexopoulos, G., & Spinellis, D. (2026). *Measuring and exploiting contextual bias in LLM-assisted security code review* (arXiv:2603.18740; Version v2). arXiv. https://arxiv.org/abs/2603.18740v2
- Confirm: **tooling-supply-chain** | tripwires: unstable:opus, unstable:gemini
- New facet check: **already resolved this session** — `evaluated-benchmark` confirmed (CrossVul,
  genuine standardized third-party dataset, 0 real participants found). The panel's
  `method-experiment` (3/3) proposal here is another clean example of the machine-only
  built-system/method-experiment confusion — reference case, no action needed.

### XJAXB98T — Beyond banning AI (GenAI governance in OSS communities)
- **APA:** Yang, W., He, R., & Zhou, M. (2026). *Beyond banning AI: a first look at GenAI governance in open source software communities* (2603.26487). arXiv. https://arxiv.org/abs/2603.26487
- Confirm: **org-governance** | tripwires: sprawl:codex=9
- New facet check: none — no `built-system`.

### XZEHQYNZ — Architecting trust (human oversight/accountability for AI-driven SE)
- **APA:** M. Tuape, Y. Gabrielmichael, & J. Kasurinen. (2025). Architecting trust: designing human oversight and accountability for AI-driven software engineering under the EU AI act. *2025 13th International Conference in Software Engineering Research and Innovation (CONISOFT)*, 325–331. https://doi.org/10.1109/CONISOFT66928.2025.00048
- Confirm: **regulatory-compliance** | tripwires: demote:context:opus, demote:context:codex
- New facet check: none — no `built-system`.

### YBHHYR4P — Do users write more insecure code with AI assistants?
- **APA:** Perry, N., Srivastava, M., Kumar, D., & Boneh, D. (2023). Do users write more insecure code with AI assistants? *Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security*, 2785–2799. https://doi.org/10.1145/3576915.3623157
- Confirm: **ai-code-insecurity** | tripwires: unstable:gemini
- New facet check: none — `method-experiment` present, no `built-system`.

### ZBF86IJM — Generation Probabilities Are Not Enough (uncertainty highlighting)
- **APA:** Vasconcelos, H., Bansal, G., Fourney, A., Liao, Q., Vaughan, J. W., & Vaughan, J. W. (2025). Generation Probabilities Are Not Enough: Uncertainty Highlighting in AI Code Completions. *ACM Trans. Comput.-Hum. Interact.* https://doi.org/10.1145/3702320
- Confirm: **oversight-explanation** | tripwires: unstable:codex
- New facet check: **already resolved this session** — `method-experiment` confirmed (30 real
  programmers, live use), `evaluated-synthetic` removed (the LeetCode-sourcing question that
  started this whole thread doesn't change the outcome — off the ladder either way).

### ZH6QIU8A — Decision-Oriented Programming with Aporia
- **APA:** Kasibatla, S. R., Rothkopf, R., Peleg, H., Pierce, B. C., Lerner, S., Goldstein, H., & Polikarpova, N. (2026). *Decision-Oriented Programming with Aporia*. arXiv.org. https://doi.org/10.48550/arXiv.2604.05203
- Confirm: **oversight-explanation** | tripwires: unstable:gemini
- New facet check: **already resolved this session** — `method-experiment` confirmed (14 real
  participants, 25-minute live task), `evaluated-synthetic` removed.

---

## Summary counts

- **Already resolved this session, no action needed:** CI93QRUH, JCTP8VXP, U9VZQXGI, VZ27QUPQ,
  WBS9U5N7, X7EN6DXZ, ZBF86IJM, ZH6QIU8A, 96XE669R, T3XTXIXW (10 of 78).
- **`agent-panel`/`cross-model` check flagged:** 3ZVMBGPB, 8KJEKBGT, B7APR28B, DJMBHHZN, LCPH3THV,
  NGIH5T4C, PPMTM4DG, T3XTXIXW*, TA6GIUK2, VFNJSZD9, VTDG995V, WBS9U5N7*, WUUDHL8R, X7EN6DXZ*
  (14, *already resolved on the ladder side but still worth the panel-structure check).
- **Ladder check (no conflict) flagged:** 5RLPIA3K, 5DI9B43K, 6ZW9QNQH, 72W6R4JG, 9R6TGN82,
  E5SQKRH7, KF5MGIBI, PR4GS7SP, R9CDT9KB (9).
- **Exclusivity conflict flagged (built-system + method-* co-proposed):** 6TZHUCMD, XK3P9C96,
  XRTVITVP, C88VGWMI (4, plus the 10 already-resolved ones above which were this exact pattern).
- **Rich/multi-tag ladder cases worth a careful read:** 8MXATG38, BU73N7PC, RX9SICP9 (3).
- **No new-facet question at all** (original theme-confirmation task only): the remaining ~38.
