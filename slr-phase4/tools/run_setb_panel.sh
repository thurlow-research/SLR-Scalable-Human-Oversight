#!/bin/bash
# v2.13 panel run: codex + gemini over Sets A+B (20 papers). Fable EXCLUDED —
# runs only with Scott's explicit per-run permission (tie-breaks).
# Idempotent: skips non-empty outputs. codex & gemini loops run concurrently.
S="${PANEL_S:?set PANEL_S to the scratchpad panel dir}"
R="$(cd "$(dirname "$0")/.." && pwd)"
KEYS=$(python3 -c "import json; d=json.load(open('$R/data/calib_sets.json')); print(' '.join(d['setA']+d['setB']))")

# Tier-parity pins (Opus-equivalent frontier tier per vendor; never rely on CLI
# defaults — a vendor-side default change would silently swap the gauge mid-sweep):
#   anthropic: claude-opus-4-8 (subagent runs, pinned by the orchestrator)
#   openai:    gpt-5.6-sol @ high (catalog priority 1 "latest frontier"; terra/luna = lower tiers)
#   google:    gemini-3.1-pro-high (top pro tier in agy; flash line = fast tier)
CODEX_MODEL="gpt-5.6-sol"
CODEX_EFFORT="high"
GEMINI_MODEL="gemini-3.1-pro-high"

meta () {  # meta <outfile> <model> <effort> <cli-version>  — provenance sidecar per run
  printf '{"model":"%s","effort":"%s","cli":"%s","ts":"%s"}\n' \
    "$2" "$3" "$4" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "${1%.json}.meta.json"
}
CODEX_CLI="codex-cli $(codex --version 2>/dev/null | grep -o '[0-9.]*' | head -1)"
AGY_CLI="agy $(agy --version 2>/dev/null | head -1)"

extract_json () { python3 -c "
import sys,re,json
s=sys.stdin.read()
cands=re.findall(r'\{.*\}', s, re.DOTALL)
for c in sorted(cands,key=len,reverse=True):
    try: json.loads(c); print(c); break
    except: continue
"; }

codex_loop () {
  for k in $KEYS; do
    o="$R/data/tags-v213/codex/$k.json"
    [ -s "$o" ] && continue
    timeout 900 codex exec --skip-git-repo-check -c model="$CODEX_MODEL" -c model_reasoning_effort="$CODEX_EFFORT" "$(cat "$S/prompts/$k.txt")" < /dev/null > "$S/codex_$k.raw" 2>"$S/codex_$k.err"
    extract_json < "$S/codex_$k.raw" > "$o"
    [ -s "$o" ] && meta "$o" "$CODEX_MODEL" "$CODEX_EFFORT" "$CODEX_CLI"
    echo "codex $k -> $(wc -c < "$o") bytes"
  done
}
gemini_loop () {
  for k in $KEYS; do
    o="$R/data/tags-v213/gemini/$k.json"
    [ -s "$o" ] && continue
    timeout 900 agy --add-dir "$S/prompts" -p "Read the file $S/prompts/$k.txt and follow its instructions exactly. Output ONLY the single JSON object it requires — no commentary." --model "$GEMINI_MODEL" < /dev/null > "$S/gemini_$k.raw" 2>"$S/gemini_$k.err"
    extract_json < "$S/gemini_$k.raw" > "$o"
    [ -s "$o" ] && meta "$o" "$GEMINI_MODEL" "high" "$AGY_CLI"
    echo "gemini $k -> $(wc -c < "$o") bytes"
  done
}
codex_loop & CP=$!
gemini_loop & GP=$!
wait $CP $GP
echo "PANEL_V213_DONE"
