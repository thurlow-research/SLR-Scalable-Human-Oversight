#!/usr/bin/env python3
"""Stage 4 Pass-2 helper: assign each core record to candidate emergent themes
via keyword/risk triggers, and report per-theme paper counts + exemplars.

The theme->trigger map is a *proposal* derived bottom-up from the observed tag
frequencies; it is here to produce defensible counts and exemplar lists for the
draft codebook, not to lock the scheme. Human review adjudicates the final map.
"""
import json
import glob
from collections import defaultdict

recs = [json.load(open(f)) for f in glob.glob(
    "/Users/scott/Code/SLR/slr-tools/stage4/work/stage4/perdoc/*.json")]


def tags(r, *fields):
    out = set()
    for f in fields:
        for x in r.get(f, []) or []:
            out.add(str(x).strip().lower())
    return out


# theme_id -> (label, trigger substrings matched against mechanism_keywords+
#              solution_mechanisms  OR  risk_types, depending on axis)
SOLUTION = {
    "S1": ("Human oversight roles & escalation",
           ["hitl", "human-in-the-loop", "human-in-command", "on-the-loop",
            "escalation", "human-review", "human-oversight", "human-in-command",
            "hild", "human-decision"]),
    "S2": ("Risk-based routing, triage & attention calibration",
           ["risk-routing", "risk-scoring", "risk-based", "triage", "routing",
            "calibration", "trust-calibration", "prioritization", "snr",
            "risk-assessment", "severity"]),
    "S3": ("Guardrails & policy-as-code enforcement gates",
           ["guardrail", "policy-as-code", "policy", "quality-gate",
            "security-gate", "defense-in-depth", "gate", "enforcement",
            "governance", "constitutional", "compliance-check", "runtime-enforcement"]),
    "S4": ("Automated verification: LLM-as-judge, ensembles & adversarial review",
           ["llm-as-judge", "ensemble", "adversarial-verification", "adversarial",
            "decorrelation", "jury", "committee", "voting", "n-version",
            "cross-model", "self-consistency", "verifier"]),
    "S5": ("Static analysis, testing & security scanning",
           ["static-analysis", "security-scanning", "sast", "dast", "linting",
            "test-generation", "testing", "fuzzing", "scanning", "code-review"]),
    "S6": ("Spec-driven & constrained generation",
           ["spec-driven", "specification", "prompt-engineering", "chain-of-thought",
            "rag", "constrained-decoding", "context-engineering", "grounding",
            "requirements", "design-by-contract"]),
    "S7": ("Provenance, traceability, audit trail & accountability",
           ["provenance", "audit-trail", "audit", "traceability", "accountability",
            "attestation", "sbom", "watermark", "lineage", "logging"]),
    "S8": ("Observability, explainability & transparency",
           ["observability", "explainability", "xai", "transparency", "monitoring",
            "dashboard", "interpretability", "visibility"]),
    "S9": ("Multi-agent orchestration of oversight",
           ["multi-agent", "orchestration", "agentic-review", "agent-workflow"]),
    "S10": ("Model-side interventions (training / fine-tuning / alignment)",
            ["training", "fine-tuning", "rlhf", "alignment", "reward-model",
             "preference-tuning"]),
}
PROBLEM = {
    "P2": ("Security & supply-chain vulnerability",
           ["security", "supply-chain", "prompt-injection", "vulnerability",
            "vulnerabilities", "sql-injection", "backdoor", "data-leakage",
            "malware", "cwe", "exploit", "insecure"]),
    "P3": ("Functional quality, correctness & reliability",
           ["quality", "correctness", "code-quality", "bugs", "reliability",
            "defects", "functional", "code-smells", "errors"]),
    "P4": ("Maintainability & technical debt",
           ["maintainability", "technical-debt", "complexity", "readability",
            "refactoring", "code-churn"]),
    "P5": ("Hallucination, specification-gaming & reward-hacking",
           ["hallucination", "specification-gaming", "reward-hacking",
            "overconfidence", "confabulation", "spec-gaming", "gaming"]),
    "P6": ("Human-factor risks: over-reliance, automation bias, deskilling",
           ["over-reliance", "automation-bias", "skill-erosion", "deskilling",
            "alert-fatigue", "complacency", "overtrust", "cognitive"]),
    "P7": ("Legal, IP, privacy & regulatory-compliance risk",
           ["legal", "licensing", "intellectual-property", "privacy",
            "regulatory-compliance", "compliance", "data-privacy", "gdpr",
            "liability", "copyright"]),
    "P8": ("Bias, fairness & ethics",
           ["bias", "fairness", "ethical", "discrimination", "inclusivity"]),
    "P9": ("Accountability & auditability gaps",
           ["accountability", "auditability", "traceability", "responsibility"]),
}


def count(themes, *fields):
    hits = defaultdict(list)
    for r in recs:
        tg = tags(r, *fields)
        for tid, (label, trigs) in themes.items():
            if any(any(t in x or x in t for x in tg) for t in trigs):
                hits[tid].append(r["citation"])
    return hits


sol = count(SOLUTION, "mechanism_keywords", "solution_mechanisms")
prob = count(PROBLEM, "risk_types")

print("### SOLUTION THEMES (by mechanism_keywords + solution_mechanisms)")
for tid, (label, _) in SOLUTION.items():
    cs = sol.get(tid, [])
    ex = ", ".join(cs[:6])
    print(f"  {tid} {len(cs):3d}  {label}\n        e.g. {ex}")
print("\n### PROBLEM THEMES (by risk_types)")
for tid, (label, _) in PROBLEM.items():
    cs = prob.get(tid, [])
    ex = ", ".join(cs[:6])
    print(f"  {tid} {len(cs):3d}  {label}\n        e.g. {ex}")

# magnitude / insufficiency universality
mg = sum(1 for r in recs if r.get("magnitude_evidence"))
print(f"\nP1 Scale/penetration (magnitude_evidence present): {mg}/114")
print(f"Insufficiency layer (present on all): "
      f"{sum(1 for r in recs if r.get('insufficiency_evidence'))}/114")
gov = sum(1 for r in recs if r.get("governance_refs"))
print(f"Governance-anchored (>=1 regulatory ref): {gov}/114")
