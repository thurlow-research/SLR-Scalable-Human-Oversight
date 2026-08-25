#!/usr/bin/env python3
"""One-off seeder: add AI Incident Database records into the 'AI Incidents' collection
(group 6505702, collection E5EZZVC3). Source data is hand-curated below from
incidentdatabase.ai GraphQL API pulls (2026-08-17). Not part of the SLR screening
pipeline -- no s1:/s2:/s3: lineage tags; this is a separate reference collection for
LinkedIn/dissertation/SLR-framing use.

Usage:
    python3 add_ai_incidents.py            # dry run, prints what would be created
    python3 add_ai_incidents.py --commit   # actually POSTs to Zotero
"""
from __future__ import annotations

import json
import os
import sys
import urllib.request

GROUP_ID = "6505702"
COLLECTION_KEY = "E5EZZVC3"  # "AI Incidents" top-level collection
API_BASE = f"https://api.zotero.org/groups/{GROUP_ID}"

INCIDENTS = [
    {
        "id": 1424,
        "title": "Claude Code Agent Reportedly Deleted DataTalks.Club Production Infrastructure, Database, and Snapshots via Terraform",
        "date": "2026-02-26",
        "description": "A Claude Code agent executing Terraform commands reportedly destroyed the production infrastructure behind the DataTalks.Club course platform after an outdated Terraform state file was restored and a terraform destroy command was allowed to run. The deletion reportedly removed the VPC, ECS cluster, load balancers, bastion host, RDS database, and automated snapshots, taking the platform offline and jeopardizing 2.5 years of data. AWS reportedly later restored a snapshot.",
        "deployer": "Alexey Grigorev",
        "developer": "Anthropic",
        "harmed": "DataTalks.Club; DataTalks.Club users",
        "patterns": ["destructive-production-action"],
        "reports": [
            {"title": "Claude Code deletes developers' production setup, including its database and snapshots — 2.5 years of records were nuked in an instant", "outlet": "tomshardware.com", "date": "2026-03-07", "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-code-deletes-developers-production-setup-including-its-database-and-snapshots-2-5-years-of-records-were-nuked-in-an-instant"},
            {"title": "How I Dropped Our Production Database and Now Pay 10% More for AWS", "outlet": "alexeyondata.substack.com", "date": "2026-03-06", "url": "https://alexeyondata.substack.com/p/how-i-dropped-our-production-database"},
        ],
    },
    {
        "id": 1152,
        "title": "LLM-Driven Replit Agent Reportedly Executed Unauthorized Destructive Commands During Code Freeze, Leading to Loss of Production Data",
        "date": "2025-07-18",
        "description": "An AI-powered development assistant on Replit's platform reportedly deleted a live production database during an active code freeze, despite receiving repeated instructions not to make changes. The system also reportedly produced fabricated test results and fake data, and incorrectly claimed rollback was impossible, delaying recovery. The incident reportedly resulted in significant data loss and user distrust regarding its safety and reliability.",
        "deployer": "Replit",
        "developer": "Replit",
        "harmed": "SaaStr; Jason Lemkin; end users of the SaaStr database; developers using Replit in production environments",
        "patterns": ["destructive-production-action", "accountability-diffusion"],
        "reports": [
            {"title": "Vibe coding service Replit deleted user's production database, faked data, told fibs galore", "outlet": "theregister.com", "date": "2025-07-21", "url": "https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/"},
            {"title": "AI coding platform goes rogue during code freeze and deletes entire company database — Replit CEO apologizes", "outlet": "tomshardware.com", "date": "2025-07-21", "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-coding-platform-goes-rogue-during-code-freeze-and-deletes-entire-company-database-replit-ceo-apologizes-after-ai-engine-says-it-made-a-catastrophic-error-in-judgment-and-destroyed-all-production-data"},
            {"title": "Replit AI Agent Deletes Codebase and Lies About It — CEO Issues Apology", "outlet": "thecyberexpress.com", "date": "2025-07-24", "url": "https://thecyberexpress.com/replit-ai-agent-incident/"},
        ],
    },
    {
        "id": 1469,
        "title": "PocketOS Production Database Was Reportedly Deleted by Cursor AI Agent Running Claude Opus 4.6",
        "date": "2026-04-24",
        "description": "A Cursor AI coding agent reportedly running Anthropic's Claude Opus 4.6 deleted PocketOS's production database and volume-level backups through Railway while working on a staging-environment task. Reporting said the agent used a broadly scoped API token to delete a Railway volume, disrupting PocketOS and its car-rental business customers before Railway helped recover data and patch safeguards.",
        "deployer": "PocketOS; Jer Crane",
        "developer": "Cursor; Anysphere; Anthropic",
        "harmed": "PocketOS; PocketOS customers; car rental businesses",
        "patterns": ["destructive-production-action"],
        "reports": [
            {"title": "AI Coding Agent Powered by Claude Opus 4.6 Deletes Production Database in 9 Seconds", "outlet": "cybersecuritynews.com", "date": "2026-04-28", "url": "https://cybersecuritynews.com/ai-coding-agent-deletes-data/"},
            {"title": "Here we go again: AI deletes entire company database and all backups in 9 seconds, then cheerfully admits 'I violated every principle I was given'", "outlet": "pcgamer.com", "date": "2026-04-28", "url": "https://www.pcgamer.com/software/ai/here-we-go-again-ai-deletes-entire-company-database-and-all-backups-in-9-seconds-then-cheerfully-admits-i-violated-every-principle-i-was-given/"},
        ],
    },
    {
        "id": 1210,
        "title": "Malicious Nx npm Packages Reportedly Weaponize AI Coding Agents for Data Exfiltration",
        "date": "2025-08-21",
        "description": "Malicious versions of the popular Nx monorepo tool and plugins were reportedly published to npm after attackers compromised its CI workflow. The malware's postinstall script reportedly harvested credentials and exfiltrated data, reportedly weaponizing local AI coding agents such as Claude Code, Gemini, and Amazon Q. By invoking unsafe flags, it allegedly coerced the tools into scanning developer machines for sensitive files, marking one of the first known AI-assisted supply chain attacks.",
        "deployer": "Malicious actors compromising Nx's CI/CD pipeline and publishing tainted npm packages",
        "developer": "Google; Anthropic; Amazon",
        "harmed": "Nx users and organizations installing compromised npm packages",
        "patterns": ["supply-chain"],
        "reports": [
            {"title": "Weaponizing AI Coding Agents for Malware in the Nx Malicious Package Security Incident", "outlet": "snyk.io", "date": "2025-08-27", "url": "https://snyk.io/blog/weaponizing-ai-coding-agents-for-malware-in-the-nx-malicious-package/"},
            {"title": "Artificial intelligence ushers in a golden age of hacking, experts say", "outlet": "washingtonpost.com", "date": "2025-09-20", "url": "https://www.washingtonpost.com/technology/2025/09/20/ai-hacking-cybersecurity-cyberthreats/"},
        ],
    },
    {
        "id": 731,
        "title": "Purportedly Hallucinated Software Packages with Potential Malware Reportedly Downloaded Thousands of Times by Developers",
        "date": "2023-12-01",
        "description": "Large language models have reportedly hallucinated non-existent software package names, some of which were subsequently uploaded to public repositories and incorporated into real codebases. In one case, a package named huggingface-cli, purported to have been originally suggested by an AI model, was downloaded more than 15,000 times. This dynamic enables what security researchers have termed \"slopsquatting,\" in which attackers register hallucinated package names and introduce potential malware into software supply chains.",
        "deployer": "Developers using AI-generated suggestions; Bar Lanyado",
        "developer": "OpenAI; Meta; Google; DeepSeek AI; Cohere; BigScience",
        "harmed": "Users downstream of software contaminated by hallucinated packages; software ecosystems; organizations that incorporated fake dependencies",
        "patterns": ["supply-chain"],
        "reports": [
            {"title": "AI hallucinates software packages and devs download them – even if potentially poisoned with malware", "outlet": "theregister.com", "date": "2024-03-28", "url": "https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/"},
            {"title": "AI-hallucinated code dependencies become new supply chain risk", "outlet": "bleepingcomputer.com", "date": "2025-04-12", "url": "https://www.bleepingcomputer.com/news/security/ai-hallucinated-code-dependencies-become-new-supply-chain-risk/"},
        ],
    },
    {
        "id": 1412,
        "title": "CodeWall's Autonomous Agent Reportedly Obtained Unauthorized Access to McKinsey's Lilli AI Platform Database",
        "date": "2026-02-28",
        "description": "CodeWall reported that its autonomous agent exploited vulnerabilities in McKinsey's Lilli AI platform and obtained unauthorized read and write access to production systems, allegedly exposing internal chat messages, files, user accounts, and prompts. McKinsey confirmed the vulnerability and said it fixed the issue within hours, but said it found no evidence that client data or client confidential information were accessed.",
        "deployer": "McKinsey & Company; CodeWall",
        "developer": "McKinsey & Company; CodeWall",
        "harmed": "McKinsey & Company employees; McKinsey & Company consultants; McKinsey & Company; Lilli users",
        "patterns": ["scope-drift-security"],
        "reports": [
            {"title": "How We Hacked McKinsey's AI Platform", "outlet": "codewall.ai", "date": "2026-03-09", "url": "https://codewall.ai/blog/how-we-hacked-mckinseys-ai-platform"},
        ],
    },
    {
        "id": 1442,
        "title": "Kiro AI Coding Tool Was Reportedly Implicated in 13-Hour AWS Cost Explorer Outage in Mainland China",
        "date": "2025-12-15",
        "description": "AWS Cost Explorer in one mainland China region reportedly experienced an approximately 13-hour interruption after Amazon engineers allegedly allowed Kiro, an internal AI coding tool, to make changes and it reportedly deleted and recreated part of the working environment. Amazon reportedly disputed that account, saying the interruption was an extremely limited event caused by user error and misconfigured access controls, not AI.",
        "deployer": "Amazon Web Services (AWS)",
        "developer": "Amazon Web Services (AWS)",
        "harmed": "Amazon Web Services (AWS) customers",
        "patterns": ["accountability-diffusion"],
        "reports": [
            {"title": "How an AI Bot Named Kiro Took Down AWS Cost Explorer", "outlet": "singhajit.com", "date": "2026-02-21", "url": "https://singhajit.com/aws-outage-kiro-ai-bot/"},
            {"title": "Correcting the Financial Times report about AWS, Kiro, and AI", "outlet": "aboutamazon.com", "date": "2026-02-20", "url": "https://www.aboutamazon.com/news/aws/aws-service-outage-ai-bot-kiro"},
            {"title": "Amazon blames human employees for an AI coding agent's mistake", "outlet": "theverge.com", "date": "2026-02-20", "url": "https://www.theverge.com/ai-artificial-intelligence/882005/amazon-blames-human-employees-for-an-ai-coding-agents-mistake"},
        ],
    },
    {
        "id": 1373,
        "title": "AI Coding Agent 'MJ Rathbun' Allegedly Published Personalized Accusatory Blog Post Targeting Matplotlib Maintainer After Pull Request Closure",
        "date": "2026-02-11",
        "description": "Scott Shambaugh, a matplotlib maintainer, reported that an autonomous AI coding agent using the name \"MJ Rathbun\" researched him and publicly posted a personalized critical blog post after his GitHub pull request was closed. The post accused him of bias and \"gatekeeping\" and included claims Shambaugh disputed. The agent's operator and underlying model were not identified. Shambaugh said the post risked reputational harm and could mislead readers or other agents.",
        "deployer": "Unknown deployer of MJ Rathbun; MJ Rathbun",
        "developer": "OpenClaw; Moltbook",
        "harmed": "Scott Shambaugh; open-source maintainers; matplotlib users; GitHub users",
        "patterns": ["scope-drift"],
        "reports": [
            {"title": "AI bot seemingly shames developer for rejected pull request", "outlet": "theregister.com", "date": "2026-02-12", "url": "https://www.theregister.com/2026/02/12/ai_bot_developer_rejected_pull_request/"},
            {"title": "Retraction: After a routine code rejection, an AI agent published a hit piece on someone by name", "outlet": "arstechnica.com", "date": "2026-02-13", "url": "https://arstechnica.com/ai/2026/02/after-a-routine-code-rejection-an-ai-agent-published-a-hit-piece-on-someone-by-name/"},
            {"title": "An AI Agent Published a Hit Piece on Me", "outlet": "theshamblog.com", "date": "2026-02-12", "url": "https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/"},
        ],
    },
    {
        "id": 1039,
        "title": "Anysphere AI Support Bot for Cursor Reportedly Invents Login Policy, Leading to Subscription Cancellations",
        "date": "2025-04-19",
        "description": "In April 2025, users of Cursor, an AI-powered coding assistant developed by Anysphere, reported being logged out unexpectedly. An AI-powered support bot, \"Sam,\" allegedly responded with an invented login policy to justify the behavior. The hallucinated policy was not based on any real company change. The incident reportedly led to subscription cancellations. Adjacent case: not a coding agent itself, but the support-automation layer around one, showing hallucination/accountability failures aren't confined to code generation.",
        "deployer": "Cursor; Anysphere",
        "developer": "Unknown LLM developer; Anysphere",
        "harmed": "Software developers; small businesses relying on Cursor; Cursor users",
        "patterns": ["accountability-diffusion", "adjacent-not-coding-agent"],
        "reports": [
            {"title": "A customer support AI went rogue—and it's a warning for every company considering replacing workers with automation", "outlet": "fortune.com", "date": "2025-04-19", "url": "https://fortune.com/article/customer-support-ai-cursor-went-rogue/"},
        ],
    },
    {
        "id": 1578,
        "title": "LLM-Driven Ransomware Operator Dubbed JADEPUFFER Reportedly Targeted Production Database",
        "date": "2026-07-01",
        "description": "Sysdig reported that a ransomware operator it dubbed JADEPUFFER used an LLM-driven agent to turn access through a vulnerable internet-facing Langflow deployment into a database-extortion operation. The report said the activity reached a production database server and produced concrete disruption, with the victim environment allegedly left in a damaged and unrecoverable state alongside a ransom demand. Adjacent case: an attacker-wielded agentic tool, not a legitimate dev-tool failure -- included for the 'AI agents can autonomously execute destructive actions at machine speed' pattern, not the oversight-of-legitimate-tooling pattern.",
        "deployer": "Ransomware operators; JADEPUFFER; agentic threat actors",
        "developer": "Large language model developers; AI agent system developers",
        "harmed": "Operators of Langflow deployments; database operators",
        "patterns": ["malicious-use", "adjacent-attacker-wielded"],
        "reports": [
            {"title": "JADEPUFFER: Agentic ransomware for automated database extortion", "outlet": "sysdig.com", "date": "2026-07-01", "url": "https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion"},
            {"title": "Researchers Claim First Fully Agentic Ransomware: JadePuffer", "outlet": "infosecurity-magazine.com", "date": "2026-07-06", "url": "https://www.infosecurity-magazine.com/news/researchers-first-agentic/"},
        ],
    },
]


def build_item(inc: dict) -> dict:
    reports_lines = "\n".join(
        f"- {r['title']} ({r['outlet']}, {r['date']}) {r['url']}" for r in inc["reports"]
    )
    extra = (
        f"AI Incident Database #{inc['id']}\n"
        f"Deployer: {inc['deployer']}\n"
        f"Developer: {inc['developer']}\n"
        f"Harmed/nearly-harmed: {inc['harmed']}\n\n"
        f"Primary reporting:\n{reports_lines}"
    )
    tags = [{"tag": "source:ai-incident-database"}, {"tag": "ai-incident"}]
    for p in inc["patterns"]:
        tags.append({"tag": f"pattern:{p}"})
    return {
        "itemType": "webpage",
        "title": inc["title"],
        "creators": [],
        "abstractNote": inc["description"],
        "websiteTitle": "AI Incident Database",
        "date": inc["date"],
        "url": f"https://incidentdatabase.ai/cite/{inc['id']}",
        "extra": extra,
        "tags": tags,
        "collections": [COLLECTION_KEY],
    }


def main() -> None:
    commit = "--commit" in sys.argv
    items = [build_item(inc) for inc in INCIDENTS]

    if not commit:
        print(f"DRY RUN — would create {len(items)} items in collection {COLLECTION_KEY}:")
        for it in items:
            print(f"  - [{it['date']}] {it['title']}")
        print("\nPass --commit to write.")
        return

    api_key = os.environ.get("ZOTERO_API_KEY_RW") or os.environ.get("ZOTERO_API_KEY")
    if not api_key:
        sys.exit("error: ZOTERO_API_KEY_RW (or ZOTERO_API_KEY) not set")

    body = json.dumps(items).encode("utf-8")
    req = urllib.request.Request(
        f"{API_BASE}/items",
        data=body,
        method="POST",
        headers={
            "Zotero-API-Key": api_key,
            "Zotero-API-Version": "3",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        status = resp.status
        result = json.loads(resp.read())

    print(f"HTTP {status}")
    successful = result.get("successful", {})  # index -> full item object
    failed = result.get("failed", {})
    for idx, obj in successful.items():
        inc = INCIDENTS[int(idx)]
        print(f"  created {obj['key']}  <-  incident #{inc['id']}: {inc['title'][:70]}")
    if failed:
        print("FAILURES:")
        print(json.dumps(failed, indent=2))


if __name__ == "__main__":
    main()
