#!/usr/bin/env python3
"""Rebuild the instrument-critique panel input (slr-phase4/data/critique/critique_input.md).

The artifact itself is gitignored (it embeds copyrighted full texts from slr-phase4/txt/);
this generator + the repo state reproduce it exactly. Run from the SLR repo root.
Requires: ZOTERO_API_KEY_RO (or ZOTERO_API_KEY) for the four title+abstract papers.

Panel design: Methodology/Theme_Tagging_Calibration.md §5 step 1b.
Human tag sets below are the final adjudicated Set A answers (2026-07-18, §7 log).
"""
import json, os, urllib.request

FULL = ["VG6CIDQW", "Z8TPRNEU", "UB2EVUFU", "22JBEZNK", "T8E8SCCG", "F9JM9CI6"]
LIGHT = ["UDVHQ5HR", "M74M3RFJ", "2CKL96B8", "T72TU8B5"]
HUMAN = {
    "UB2EVUFU": {"primary": "ai-review", "themes": ["ai-review", "hitl-workflow", "provenance-auditability", "remediation-gating"], "facets": ["agentic", "built-system", "framework", "steering"], "flags": []},
    "UDVHQ5HR": {"primary": "ai-review", "themes": ["ai-review"], "facets": [], "flags": ["demote:context"]},
    "Z8TPRNEU": {"primary": "hitl-workflow", "themes": ["ai-review", "hitl-workflow"], "facets": ["agentic", "steering", "survey-input"], "flags": []},
    "T8E8SCCG": {"primary": "rules-based-checks", "themes": ["rules-based-checks", "ai-code-insecurity"], "facets": ["built-system", "framework"], "flags": []},
    "M74M3RFJ": {"primary": "regulatory-compliance", "themes": ["regulatory-compliance"], "facets": ["framework", "general-ai", "intro-framing"], "flags": ["already demoted core->context 2026-07-15"]},
    "2CKL96B8": {"primary": "ai-review", "themes": ["ai-review", "ai-code-insecurity", "quality-debt"], "facets": ["assistive", "intro-framing", "lit-review"], "flags": ["demote:context"]},
    "T72TU8B5": {"primary": "risk-routing", "themes": ["risk-routing", "hitl-workflow", "oversight-explanation"], "facets": ["agentic", "built-system", "framework", "survey-input"], "flags": []},
    "VG6CIDQW": {"primary": "oversight-explanation", "themes": ["oversight-explanation"], "facets": ["assistive", "built-system", "steering"], "flags": []},
    "22JBEZNK": {"primary": "oversight-explanation", "themes": ["oversight-explanation"], "facets": ["agentic", "non-developer", "survey-input"], "flags": []},
    "F9JM9CI6": {"primary": "ai-review", "themes": ["ai-review", "oversight-explanation", "risk-routing"], "facets": ["counterpoint", "general-code", "intro-framing"], "flags": []},
}

BRIEF = """# INSTRUMENT-CRITIQUE TASK (read fully before starting)

You are one of three independent frontier-model critics reviewing a *tagging instrument* for a
systematic literature review on scalable human oversight of AI-generated code ("vibe coding
governance"). Model and human taggers apply this instrument to full paper texts.

**Critique the INSTRUMENT, not the taxonomy.** All boundary decisions (the steering exclusion, the
drift object-of-mechanism rule, what counts as remediation-gating, etc.) were adjudicated by the
human arbiter after calibration and are NOT up for re-vote. The *wording* that encodes them is fully
in scope: your job is to determine whether a competent tagger can execute these instructions
consistently, and to propose improvements. Adoption of any proposal is the arbiter's decision.

**PART 1** below is the compressed operative instrument (cheat-sheet + task block) — what taggers
actually receive. **PART 2** is the full Tag reference it was compressed from (includes the decision
log). **PART 3** is the development set: 10 calibration papers with the human arbiter's final
adjudicated tags — 6 with full text, 4 with title+abstract only.

Report every finding in exactly one of five bins:
- "ambiguity" — two competent taggers could read a rule differently. Give BOTH readings.
- "inconsistency" — two parts of the instrument conflict. Quote both.
- "omission" — a common paper type or recurring decision has no rule. Describe the case.
- "compression-gap" — a rule present in PART 2 but missing or materially weakened in PART 1.
  (These are classified as bugs: a boundary only protects taggers if it is in the copy they use.)
- "boundary-disagreement" — you believe an adjudicated rule is substantively wrong. Recorded for
  the arbiter, never auto-actioned. Use sparingly.

For every ambiguity / inconsistency / omission you MUST include a **test_case**: a 2-4 sentence
hypothetical paper description on which the instrument yields two defensible answers (or none).

**Section 2 — known-answer analysis.** For each of the 10 papers in PART 3, judge whether the
instrument text FORCES the human's adjudicated tag set (primary, themes, facets, flags) for a
tagger who has never seen these answers. Where the text merely *permits* the human answer among
others, identify the too-weak wording and propose a strengthening. Do NOT argue the human tags are
wrong (that belongs in boundary-disagreement).

**Output**: ONE JSON object only, no prose around it, no markdown fences:
{"critic":"<your model name>",
 "findings":[{"id":1,"type":"ambiguity|inconsistency|omission|compression-gap|boundary-disagreement",
   "location":"<short quote of the instrument text at issue>","issue":"<the problem>",
   "test_case":"<hypothetical paper>","proposed_fix":"<concrete wording>","severity":"high|medium|low"}],
 "known_answer_analysis":[{"key":"<KEY>","forced":true,"weak_rules":"<text permitting divergence, or empty>","suggestion":"<strengthening, or empty>"}],
 "overall":"<=100 words: is this instrument ready for a 148-paper sweep?"}
"""


def fetch_abstracts(keys):
    key = os.environ.get("ZOTERO_API_KEY_RO") or os.environ["ZOTERO_API_KEY"]
    req = urllib.request.Request(
        "https://api.zotero.org/groups/6505702/items?itemKey=%s&include=data&limit=25" % ",".join(keys))
    req.add_header("Zotero-API-Key", key)
    out = {}
    for it in json.load(urllib.request.urlopen(req)):
        d = it["data"]
        out[d["key"]] = (d.get("title", ""), d.get("abstractNote", "") or "(no abstract)")
    return out


def main():
    instrument = open("slr-phase4/Tag_Prompt.md").read().split("=== PAPER FULL TEXT ===")[0]
    ref = open("Methodology/Emerging_Themes.md").read()
    ref = ref[ref.index("## Tag reference"):ref.index("## Theme 1 —")]
    abstracts = fetch_abstracts(LIGHT)

    out = [BRIEF, "\n\n===== PART 1 — THE OPERATIVE INSTRUMENT =====\n", instrument,
           "\n===== PART 2 — FULL TAG REFERENCE (source of the compression) =====\n", ref,
           "\n===== PART 3 — DEVELOPMENT SET (10 papers, human-adjudicated tags) =====\n"]
    for k in FULL:
        txt = open("slr-phase4/txt/%s.txt" % k).read()
        out.append("\n--- PAPER %s (FULL TEXT) ---\nHUMAN TAGS: %s\n\n%s\n" % (k, json.dumps(HUMAN[k]), txt))
    for k in LIGHT:
        t, a = abstracts[k]
        out.append("\n--- PAPER %s (TITLE+ABSTRACT ONLY) ---\nHUMAN TAGS: %s\nTITLE: %s\nABSTRACT: %s\n"
                   % (k, json.dumps(HUMAN[k]), t, a))

    doc = "".join(out)
    os.makedirs("slr-phase4/data/critique", exist_ok=True)
    open("slr-phase4/data/critique/critique_input.md", "w").write(doc)
    print("critique_input.md written:", len(doc.split()), "words")


if __name__ == "__main__":
    main()
