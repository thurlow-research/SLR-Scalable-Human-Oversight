#!/bin/bash
# v2.13 SWEEP opus leg: claude CLI pinned to claude-opus-4-8 (the calibration
# gauge — NOT the session default, which would silently swap the gauge).
# Same sharding/idempotency/sidecar pattern as run_sweep_panel.sh.
S="${PANEL_S:?set PANEL_S to the scratchpad panel dir (prompts/ inside)}"
R="$(cd "$(dirname "$0")/.." && pwd)"
WORKERS="${WORKERS:-4}"
KEYS=$(python3 -c "import json; print(' '.join(json.load(open('$R/data/tags-v213/sweep_keys.json'))))")

OPUS_MODEL="claude-opus-4-8"
CLAUDE_CLI="claude-cli $(claude --version 2>/dev/null | grep -o '[0-9.]*' | head -1)"

meta () {
  printf '{"model":"%s","effort":"%s","cli":"%s","ts":"%s"}\n' \
    "$2" "$3" "$4" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "${1%.json}.meta.json"
}

extract_json () { python3 -c "
import sys,re,json
s=sys.stdin.read()
cands=re.findall(r'\{.*\}', s, re.DOTALL)
for c in sorted(cands,key=len,reverse=True):
    try: json.loads(c); print(c); break
    except: continue
"; }

opus_one () {
  local k="$1" o="$R/data/tags-v213/opus/$k.json"
  [ -s "$o" ] && return
  timeout 900 claude -p "$(cat "$S/prompts/$k.txt")" --model "$OPUS_MODEL" < /dev/null > "$S/opus_$k.raw" 2>"$S/opus_$k.err"
  extract_json < "$S/opus_$k.raw" > "$o"
  [ -s "$o" ] && meta "$o" "$OPUS_MODEL" "default" "$CLAUDE_CLI"
  echo "opus $k -> $(wc -c < "$o" | tr -d ' ') bytes"
}

shard_loop () {
  local idx="$1" i=0
  for k in $KEYS; do
    [ $(( i % WORKERS )) -eq "$idx" ] && opus_one "$k"
    i=$(( i + 1 ))
  done
}

PIDS=""
for w in $(seq 0 $(( WORKERS - 1 ))); do
  shard_loop "$w" & PIDS="$PIDS $!"
done
wait $PIDS
echo "SWEEP_OPUS_V213_DONE"
