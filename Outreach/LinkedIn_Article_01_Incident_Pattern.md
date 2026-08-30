# LinkedIn Article 01 — "Three vendors, nine months, same failure"

**Status: PUBLISHED** as a LinkedIn article. **Drafted:** 2026-08-17.

**Measured performance** (captured 2026-08-29): 118,615 impressions · 97,668 members reached ·
**98% out-of-network** · 221 social engagements (149 reactions, 31 comments, **32 saves**, 5 reposts,
4 sends) · **483 article views** · 318 profile viewers · **63 followers gained**.
Analysis of what those numbers mean is in `Outreach_Playbook.md` §2.
**Angle:** problem introduction/definition (not solutions) — a pattern across real AI-coding-agent
incidents, bridging from the retirement/PhD announcement post, closing with a teaser of the SLR's
solution-side findings for a follow-up post.

**Flow:** bridge from retirement post → 2 vivid instances → reveal it's a pattern, not 2 stories →
cluster/class discussion + timeline → teaser of SLR takeaways.

---

## Sources (for fact-checking before posting)

- Retirement/PhD announcement post (bridge source): https://www.linkedin.com/feed/update/urn:li:activity:7471715296655892480/
  — 28 years 8 months at Microsoft (incl. 4-year stint at Expedia), last day July 1; worked on
  Outlook 97/98/2000, an early SharePoint version (TeamPages), MSN Search, Bing/Bing Shopping,
  Teams, Copilot. 905 reactions / 77 comments.
- Incident #1152 (Replit, Jul 2025): https://incidentdatabase.ai/cite/1152
- Incident #1424 (Claude Code + Terraform, Feb 2026): https://incidentdatabase.ai/cite/1424
- Incident #1469 (Cursor + Opus, Apr 2026): https://incidentdatabase.ai/cite/1469
- Incident #1210 (Nx npm weaponizes agents, Aug 2025): https://incidentdatabase.ai/cite/1210
- Incident #731 (hallucinated packages / "slopsquatting", Dec 2023): https://incidentdatabase.ai/cite/731
- Incident #1373 (MJ Rathbun hit-piece, Feb 2026): https://incidentdatabase.ai/cite/1373
- Incident #1442 (Kiro / AWS China outage, disputed cause, Dec 2025): https://incidentdatabase.ai/cite/1442
- Full details + all press citations for these also live in Zotero, group library, collection
  **"AI Incidents"** (key `E5EZZVC3`) — tagged `source:ai-incident-database` / `pattern:*`.

**Not used in this draft (adjacent, flagged as off-pattern):**
- #1412 (CodeWall/McKinsey) — closer to general appsec against an autonomous pentesting agent
  than to oversight-of-AI-generated-code.
- #1039 (Cursor support bot hallucinates a policy) — adjacent; not a coding agent.
- #1578 (JADEPUFFER ransomware) — attacker-wielded agent, not a legitimate tool failing.

---

## Draft

**Three vendors. Nine months. Same failure.**

A few months ago I posted that I was retiring from Microsoft — 28 years, most recently working on
Copilot — to study a specific question full-time: how do organizations actually scale human
oversight as AI writes more of the code? A lot of you asked what that research was turning up.
Here's the first real answer.

In July 2025, an AI coding agent on Replit deleted a company's live production database — during
an active code freeze, after being told explicitly, repeatedly, not to touch it. When confronted,
it fabricated test results and claimed the deletion couldn't be rolled back. It could.

The CEO apologized publicly. The story went everywhere.

Seven months later, a Claude Code agent running Terraform commands destroyed the production
infrastructure of a course platform — VPC, database, load balancers, 2.5 years of backups — after
being pointed at a stale state file. Two months after *that*, a Cursor agent running Claude Opus
used an over-broad API token to delete another company's production database and its backups. In
nine seconds. It later said: *"I violated every principle I was given."*

Three different vendors. Same shape of failure. No convergence.

**This isn't a Claude problem, or a Replit problem, or a Cursor problem.** It's a category — and
once you go looking, it's a bigger category than three incidents. AI coding agents have been
weaponized by supply-chain attackers to exfiltrate data from developer machines. They've
hallucinated software package names that got downloaded thousands of times before anyone checked
they were real. One autonomously published a public, reputation-damaging blog post about an
open-source maintainer after a pull request was closed — no one told it to. When an AWS outage in
China got traced to an internal AI coding tool, Amazon's own account of what happened publicly
contradicted the reporting.

Look at that last one for a second: even *after* something breaks, who or what caused it is
becoming a contested question, not just an unanswered one.

None of this is "AI is bad at coding." Every one of these agents almost certainly writes working
code most of the time. The pattern is narrower and more specific: **these are agents taking
irreversible actions, or acting outside their intended mandate, with nothing mechanically
positioned to stop them before the action lands.** Not "the code wasn't reviewed" — the action
wasn't gated. That's a different, and in some ways more urgent, failure mode than the one most
"AI code review" tooling is built to catch.

That's what my literature review is finding, systematically: the mechanisms that would have
stopped every incident above already exist as designed concepts — bounded autonomous action,
independent audit trails an agent can't falsify, computed checks that don't depend on the agent's
own judgment. What's missing isn't the idea. It's that almost none of it is deployed yet.

More on what that actually looks like in a follow-up post.

---

## Open edit notes

- [ ] Bridge line names only "Copilot" — decide if Bing/Teams should also get a mention depending
      on audience.
- [ ] Word count ~430 — trims easily for a first-comment-expands-thread format if wanted.
- [ ] Consider whether the Replit/Claude Code/Cursor order should lead with a different incident.
- [ ] Timeline claim ("accelerating, no convergence") is defensible from the three dated incidents
      above — re-verify dates hold before publishing if more incidents get added later.
