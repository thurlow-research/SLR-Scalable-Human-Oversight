#!/bin/bash
# v2.13 SWEEP panel run: codex + gemini over the 128-core sweep roster
# (data/tags-v213/sweep_keys.json). Fable EXCLUDED — per-run permission only.
# Same gauge pins + provenance sidecars as run_setb_panel.sh; adds within-model
# parallelism (WORKERS shards per model) for sweep-scale wall-clock.
# Idempotent: skips non-empty outputs — safe to rerun after interruption.
S="${PANEL_S:?set PANEL_S to the scratchpad panel dir (prompts/ inside)}"
R="$(cd "$(dirname "$0")/.." && pwd)"
WORKERS="${WORKERS:-4}"
KEYS=$(python3 -c "import json; print(' '.join(json.load(open('$R/data/tags-v213/sweep_keys.json'))))")

# Tier-parity pins (never rely on CLI defaults — a vendor-side default change
# would silently swap the gauge mid-sweep):
CODEX_MODEL="gpt-5.6-sol"
CODEX_EFFORT="high"
GEMINI_MODEL="gemini-3.1-pro-high"

meta () {  # meta <outfile> <model> <effort> <cli-version>
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

codex_one () {
  local k="$1" o="$R/data/tags-v213/codex/$k.json"
  [ -s "$o" ] && return
  timeout 900 codex exec --skip-git-repo-check -c model="$CODEX_MODEL" -c model_reasoning_effort="$CODEX_EFFORT" "$(cat "$S/prompts/$k.txt")" < /dev/null > "$S/codex_$k.raw" 2>"$S/codex_$k.err"
  extract_json < "$S/codex_$k.raw" > "$o"
  [ -s "$o" ] && meta "$o" "$CODEX_MODEL" "$CODEX_EFFORT" "$CODEX_CLI"
  echo "codex $k -> $(wc -c < "$o" | tr -d ' ') bytes"
}
gemini_one () {
  local k="$1" o="$R/data/tags-v213/gemini/$k.json"
  [ -s "$o" ] && return
  timeout 900 agy --add-dir "$S/prompts" -p "Read the file $S/prompts/$k.txt and follow its instructions exactly. Output ONLY the single JSON object it requires — no commentary." --model "$GEMINI_MODEL" < /dev/null > "$S/gemini_$k.raw" 2>"$S/gemini_$k.err"
  extract_json < "$S/gemini_$k.raw" > "$o"
  [ -s "$o" ] && meta "$o" "$GEMINI_MODEL" "high" "$AGY_CLI"
  echo "gemini $k -> $(wc -c < "$o" | tr -d ' ') bytes"
}

shard_loop () {  # shard_loop <fn> <shard-index>
  local fn="$1" idx="$2" i=0
  for k in $KEYS; do
    [ $(( i % WORKERS )) -eq "$idx" ] && "$fn" "$k"
    i=$(( i + 1 ))
  done
}

PIDS=""
for w in $(seq 0 $(( WORKERS - 1 ))); do
  shard_loop codex_one  "$w" & PIDS="$PIDS $!"
  shard_loop gemini_one "$w" & PIDS="$PIDS $!"
done
wait $PIDS
echo "SWEEP_PANEL_V213_DONE"
