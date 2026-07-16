#!/usr/bin/env python3
import os
"""
Multi-source SLR bulk-screening via Claude Code SDK (uses your Max subscription).

Screens items in the 00-Queue of all non-SSRN sources:
  ieee, scopus, acm, arxiv, wos

SCOPUS 00-Queue has theme subcollections — these are walked automatically.
Items already in 01-Keep, 02-Maybe, or 03-Discard are skipped.

Usage:
    cd ~/slr/non-ssrn
    python3 slr_llm_screen.py

    # Screen a single source only:
    python3 slr_llm_screen.py --source ieee

    # Dry-run (fetch items, print what would be screened, no Claude calls):
    python3 slr_llm_screen.py --dry-run

Output (per run, in WORKDIR):
    decisions.csv        - all decisions (keep + maybe + discard), appendable across runs
    state.json           - resume checkpoint (re-run to continue)
    progress.log         - human-readable progress log
    decisions.jsonl      - newline-delimited JSON, one record per decision

NO ZOTERO WRITES. Review decisions.csv then bulk-apply separately.
"""
import json, urllib.request, urllib.error, subprocess, sys, time, csv, os, random, argparse
from datetime import datetime, timezone

# ============================================================
# CONFIG
# ============================================================
ZOTERO_API_KEY = os.environ.get("ZOTERO_API_KEY_RO", "")  # read-only
LIB = "6505702"
BASE = f"https://api.zotero.org/groups/{LIB}"

WORKDIR = os.path.expanduser("~/slr/non-ssrn")
CSV_PATH      = f"{WORKDIR}/decisions.csv"
STATE_PATH    = f"{WORKDIR}/state.json"
LOG_PATH      = f"{WORKDIR}/progress.log"
DECISIONS_PATH = f"{WORKDIR}/decisions.jsonl"

# Rate limits
CLAUDE_RATE_LIMIT_SEC  = 30.0   # Sonnet via Max subscription — same as SSRN production run
ZOTERO_RATE_LIMIT_SEC  = 0.3

CHECKPOINT_EVERY = 1   # save state after every item (cheap at this pace)

CLAUDE_MODEL = "sonnet"  # sonnet / opus / haiku

# ============================================================
# SOURCE → 02-Screening parent collection key
# Queue items live at: <02-Screening parent> / 00-Queue[/<theme-subcol>]
# Screened items (already in 01-Keep / 02-Maybe / 03-Discard) are skipped.
# ============================================================
SOURCES = {
    "ieee":    "7XHWH8NM",
    "scopus":  "2RWBC7QH",
    "acm":     "G4IIYGV6",
    "arxiv":   "YK2CHQLN",
    "wos":     "E7AS4HD4",
}

# ============================================================
# SCREENING RUBRIC  (identical to SSRN run for consistency)
# ============================================================
RUBRIC = """You are screening academic papers for a systematic literature review (SLR) on:
"How organizations manage risk from AI-generated code and 'vibe coding', particularly the
challenge of scalable human oversight when AI dramatically increases code volume."

Your job: read the title and abstract, output ONE of three decisions:
  - "discard"     → clearly off-topic, no transferable contribution
  - "maybe"       → uncertain or peripheral, leave for human reviewer
  - "keep"        → relevant or potentially relevant

DISCARD if the paper is purely about ANY of these (and lacks any oversight/governance angle):
  - K-12 / pedagogy of AI tools (classroom use of ChatGPT, AI literacy for students, cheating detection in education)
  - Autonomous weapons systems specifically (lethal autonomous weapons, drone swarms, military AI hardware)
  - Voting / elections / political campaigns specifically
  - Narrow clinical AI applications (cancer detection, retinopathy, single-disease diagnosis) WITHOUT a governance lens
  - Pure ML/technical papers (new architectures, benchmarks, hyperparameter tuning, ablation studies) with no oversight angle
  - Algorithmic trading / high-frequency trading / quantitative finance specifically
  - Marketing/advertising/recommender system technical work without governance
  - AI as a writing aid for academic papers (LLM as co-author essays — but DETECTION-AT-SCALE methodology is KEEP)
  - Single-author vendor whitepapers without methodology

KEEP regardless of domain if the paper is about ANY of these:
  - Vibe coding / AI code generation / Copilot / LLM-based coding tools
  - Human oversight, scalable oversight, human-in-the-loop, meaningful human control
  - AI governance frameworks, AI risk management, AI auditing, accountability
  - EU AI Act, NIST AI RMF, GDPR Article 22, AI regulation/compliance
  - Organizational adoption of AI at scale (case studies, empirical studies)
  - AI alignment, AI safety, RLHF as governance mechanism
  - Code review research generally (capacity, fatigue, scalability)
  - Methodology for detecting AI output at scale (transferable to detecting AI-generated code)
  - Responsibility gap, legal liability for AI systems

MAYBE for borderline cases — when a paper is in a discard category but has SOME governance/oversight/regulatory angle that makes it potentially transferable.

DEFAULT TO MAYBE when uncertain. Only "discard" when clearly off-topic.

Output ONLY a single JSON object on one line, no other text:
{"decision":"keep|maybe|discard","category":"category-tag-or-null","rationale":"one sentence explaining why"}

The category tag should be one of: K12pedagogy, WeaponsSpecific, VotingDemocracy, ClinicalNarrow, PureML, FinanceTrading, MarketingAds, AISciWriting, VendorWhitepaper, OffTopicOther — or null for keep/maybe.
"""

# ============================================================
# ZOTERO API
# ============================================================
def zot_get(path, retries=5):
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(f"{BASE}{path}")
            req.add_header("Zotero-API-Key", ZOTERO_API_KEY)
            req.add_header("Zotero-API-Version", "3")
            with urllib.request.urlopen(req, timeout=30) as r:
                total = r.headers.get("Total-Results")
                return json.loads(r.read()), total
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                wait = 2 ** attempt + random.uniform(0, 1)
                log(f"  Zotero HTTP {e.code}, retry in {wait:.1f}s")
                time.sleep(wait)
                continue
            last_err = f"HTTP {e.code}"
        except Exception as e:
            last_err = str(e)
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
    return None, last_err

def get_child_collections(parent_key):
    """Return all direct child collections of parent_key."""
    cols, _ = zot_get(f"/collections?limit=100")
    if not cols:
        return []
    return [
        c for c in cols
        if c.get("data", {}).get("parentCollection") == parent_key
        and not c.get("data", {}).get("deleted", False)
    ]

def get_items_in_collection(col_key):
    """Fetch all top-level items in a collection, paginated."""
    items = []
    start = 0
    while True:
        data, _ = zot_get(f"/collections/{col_key}/items/top?limit=100&start={start}")
        if not data:
            break
        for it in data:
            d = it.get("data", {})
            creators = d.get("creators", [])
            authors = "; ".join(
                (c.get("lastName", "") or c.get("name", "")) for c in creators[:5]
            )
            items.append({
                "key": it["key"],
                "title": d.get("title", ""),
                "abstract": d.get("abstractNote", ""),
                "authors": authors,
                "year": (d.get("date", "") or "")[:4],
                "url": d.get("url", ""),
                "source": "",   # filled in by caller
            })
        if len(data) < 100:
            break
        start += 100
        time.sleep(ZOTERO_RATE_LIMIT_SEC)
    return items

def get_screened_keys(screening_parent_key):
    """
    Return set of item keys already in 01-Keep, 02-Maybe, or 03-Discard
    under this source's screening parent. These are skipped.
    """
    screened = set()
    children = get_child_collections(screening_parent_key)
    for c in children:
        name = c.get("data", {}).get("name", "")
        if any(name.startswith(prefix) for prefix in ("01-", "02-", "03-")):
            col_key = c["data"]["key"]
            items = get_items_in_collection(col_key)
            for it in items:
                screened.add(it["key"])
    return screened

def get_queue_collection_key(screening_parent_key):
    """Find the 00-Queue child collection under a screening parent."""
    children = get_child_collections(screening_parent_key)
    for c in children:
        if c.get("data", {}).get("name", "").startswith("00-"):
            return c["data"]["key"]
    return None

def get_queue_items_for_source(source_name, screening_parent_key):
    """
    Fetch all unscreened Queue items for a source.
    For SCOPUS: walks into theme subcollections under 00-Queue.
    Returns list of item dicts with source name filled in.
    """
    log(f"  Fetching screened keys for {source_name}...")
    screened = get_screened_keys(screening_parent_key)
    log(f"  {len(screened)} items already screened in {source_name} — will skip")

    queue_key = get_queue_collection_key(screening_parent_key)
    if not queue_key:
        log(f"  WARNING: No 00-Queue collection found under {source_name} ({screening_parent_key})")
        return []

    # Collect candidate items — from 00-Queue itself and any subcollections
    candidate_keys_seen = set()
    candidates = []

    def collect_from(col_key, depth=0):
        items = get_items_in_collection(col_key)
        for it in items:
            if it["key"] not in candidate_keys_seen:
                candidate_keys_seen.add(it["key"])
                it["source"] = source_name
                candidates.append(it)
        # Walk subcollections (SCOPUS theme subcols, or any other nesting)
        if depth < 2:
            subcols = get_child_collections(col_key)
            for sub in subcols:
                collect_from(sub["data"]["key"], depth + 1)

    collect_from(queue_key)

    # Filter out already-screened items
    unscreened = [it for it in candidates if it["key"] not in screened]
    log(f"  {source_name}: {len(candidates)} in Queue, {len(unscreened)} unscreened")
    return unscreened

# ============================================================
# CLAUDE SDK CALL  (identical logic to ssrn_llm_screen.py)
# ============================================================
def call_claude(title, abstract):
    item_text = f"TITLE: {title}\n\nABSTRACT: {abstract or '(no abstract)'}"
    prompt = f"{RUBRIC}\n\nNow screen this item:\n\n{item_text}"

    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", CLAUDE_MODEL, "--output-format", "text"],
            capture_output=True, text=True, timeout=120
        )
    except subprocess.TimeoutExpired:
        return None, "claude-timeout"
    except FileNotFoundError:
        return None, "claude-not-found"

    if result.returncode != 0:
        stderr_lower = result.stderr.lower() if result.stderr else ""
        rate_limit_signals = ["rate limit", "rate-limit", "rate_limit", "429",
                              "too many requests", "usage limit", "quota",
                              "claude usage limit", "approaching usage limit",
                              "5-hour", "5 hour"]
        if any(sig in stderr_lower for sig in rate_limit_signals):
            return None, f"RATE_LIMIT: {result.stderr[:300]}"
        return None, f"claude-rc-{result.returncode}: {result.stderr[:200]}"

    raw = result.stdout.strip()
    try:
        start = raw.find("{")
        end = raw.rfind("}")
        if start >= 0 and end > start:
            obj = json.loads(raw[start:end+1])
            return obj, None
        return None, f"no-json-found: {raw[:200]}"
    except json.JSONDecodeError as e:
        return None, f"json-error: {e} :: raw={raw[:200]}"

# ============================================================
# LOGGING & STATE
# ============================================================
def log(msg):
    line = f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG_PATH, "a") as f:
        f.write(line + "\n")

def init_csv():
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, "w", newline="") as f:
            csv.writer(f).writerow([
                "item_key", "source", "decision", "category",
                "title", "authors", "year", "url",
                "rationale", "abstract_first_500"
            ])

def append_csv(row):
    with open(CSV_PATH, "a", newline="") as f:
        csv.writer(f).writerow(row)

def append_decisions(d):
    with open(DECISIONS_PATH, "a") as f:
        f.write(json.dumps(d) + "\n")

def load_state():
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH) as f:
            return json.load(f)
    return {
        "all_keys": None,
        "items_cache": {},
        "processed": [],
        "discarded": 0, "kept": 0, "maybe": 0, "errors": 0,
        "rl_backoff_attempts": 0,
        "sources_loaded": [],
    }

def save_state(state):
    with open(STATE_PATH, "w") as f:
        json.dump(state, f)

# ============================================================
# MAIN
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="Screen non-SSRN SLR sources via Claude.")
    parser.add_argument("--source", choices=list(SOURCES.keys()),
                        help="Screen only this source (default: all)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Fetch and count items only, no Claude calls")
    args = parser.parse_args()

    os.makedirs(WORKDIR, exist_ok=True)
    init_csv()

    state = load_state()

    # Determine which sources to include this run
    sources_this_run = {args.source: SOURCES[args.source]} if args.source else SOURCES

    # Build/extend item list if not already in state
    if state["all_keys"] is None or any(s not in state["sources_loaded"] for s in sources_this_run):
        log("Building item list from Zotero...")
        new_items = {}
        for src, parent_key in sources_this_run.items():
            if src in state.get("sources_loaded", []):
                log(f"  {src}: already loaded, skipping fetch")
                continue
            log(f"\n--- {src.upper()} ---")
            items = get_queue_items_for_source(src, parent_key)
            for it in items:
                if it["key"] not in state["items_cache"]:
                    new_items[it["key"]] = it
            state["sources_loaded"] = state.get("sources_loaded", []) + [src]

        # Merge into state
        state["items_cache"].update(new_items)
        existing_keys = set(state.get("all_keys") or [])
        state["all_keys"] = list(existing_keys | set(new_items.keys()))
        save_state(state)

        total = len(state["all_keys"])
        log(f"\nTotal unscreened items across all sources: {total}")

        if args.dry_run:
            log("\n[DRY RUN] Item counts by source:")
            source_counts = {}
            for it in state["items_cache"].values():
                src = it.get("source", "unknown")
                source_counts[src] = source_counts.get(src, 0) + 1
            for src, count in sorted(source_counts.items()):
                log(f"  {src}: {count}")
            log(f"  TOTAL: {total}")
            log("\nExiting (dry run). Remove --dry-run to screen.")
            return
    else:
        already_done = len(state["processed"])
        log(f"Resuming: {len(state['all_keys'])} total items, {already_done} already processed")

    if args.dry_run:
        log("\n[DRY RUN] State already loaded. Counts by source:")
        source_counts = {}
        for it in state["items_cache"].values():
            src = it.get("source", "unknown")
            source_counts[src] = source_counts.get(src, 0) + 1
        for src, count in sorted(source_counts.items()):
            log(f"  {src}: {count}")
        log(f"  TOTAL: {len(state['all_keys'])}")
        log("\nExiting (dry run). Remove --dry-run to screen.")
        return

    processed_set = set(state["processed"])
    t_start = time.time()
    consecutive_errors = 0

    for i, k in enumerate(state["all_keys"]):
        if k in processed_set:
            continue

        item = state["items_cache"].get(k)
        if not item:
            log(f"[{i+1}] {k} missing from cache — skipping")
            state["errors"] += 1
            continue

        # Rate-limit sleep BEFORE the call
        time.sleep(CLAUDE_RATE_LIMIT_SEC)

        decision, err = call_claude(item["title"], item["abstract"])

        if decision is None:
            log(f"[{i+1}/{len(state['all_keys'])}] {k} ({item.get('source','?')}) CLAUDE ERROR: {err}")
            state["errors"] += 1
            consecutive_errors += 1

            if err and err.startswith("RATE_LIMIT"):
                consecutive_errors -= 1
                save_state(state)
                rl_attempts = state.get("rl_backoff_attempts", 0)
                wait_sec = [300, 900, 1800, 3600][min(rl_attempts, 3)]
                log(f"  RATE LIMIT. Sleeping {wait_sec//60} min before retrying...")
                time.sleep(wait_sec)
                state["rl_backoff_attempts"] = rl_attempts + 1
                continue
            else:
                state["rl_backoff_attempts"] = 0

            if consecutive_errors >= 5:
                log("  5 consecutive non-rate-limit errors — pausing 60s")
                time.sleep(60)
                consecutive_errors = 0
            continue

        consecutive_errors = 0
        state["rl_backoff_attempts"] = 0

        d_val = decision.get("decision", "").lower()
        if d_val not in ("keep", "maybe", "discard"):
            log(f"[{i+1}] {k} INVALID DECISION: {decision}")
            state["errors"] += 1
            continue

        category = decision.get("category") or ""
        rationale = decision.get("rationale", "")[:300]
        source = item.get("source", "")

        # Write to CSV (all decisions)
        append_csv([
            k, source, d_val, category,
            item["title"], item["authors"], item["year"], item["url"],
            rationale, (item["abstract"] or "")[:500]
        ])

        # Write to decisions.jsonl
        append_decisions({
            "key": k,
            "source": source,
            "decision": d_val,
            "category": category,
            "rationale": rationale,
            "title": item["title"][:120],
        })

        if d_val == "discard":
            state["discarded"] += 1
        elif d_val == "maybe":
            state["maybe"] += 1
        else:
            state["kept"] += 1

        state["processed"].append(k)
        save_state(state)

        # Progress log every 10 items
        if len(state["processed"]) % 10 == 0:
            elapsed = time.time() - t_start
            done = len(state["processed"]) - len(processed_set)
            rate = done / elapsed if elapsed > 0 else 0
            remaining = len(state["all_keys"]) - len(state["processed"])
            eta_min = (remaining / rate) / 60 if rate > 0 else 0
            log(f"  [{len(state['processed'])}/{len(state['all_keys'])}] "
                f"discard={state['discarded']} maybe={state['maybe']} keep={state['kept']} "
                f"err={state['errors']} rate={rate:.2f}/s eta={eta_min:.0f}min")

    save_state(state)
    log("\n=== DONE ===")
    log(f"Total processed : {len(state['processed'])}")
    log(f"Kept            : {state['kept']}")
    log(f"Maybe           : {state['maybe']}")
    log(f"Discarded       : {state['discarded']}")
    log(f"Errors          : {state['errors']}")
    log(f"\nCSV       : {CSV_PATH}")
    log(f"Decisions : {DECISIONS_PATH}")

if __name__ == "__main__":
    main()
