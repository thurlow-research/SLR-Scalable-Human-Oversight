#!/bin/bash
# v2.13 SWEEP replication stage: k=3 on contested papers only (the
# disagreement-triggered rule). Runs suffix $RUN (r2|r3) for all three legs —
# codex + gemini CLIs and the opus claude-CLI leg pinned to the calibration
# gauge. Keys come from $KEYS_FILE (JSON list = the RERUN-NEEDED worklist).
# Idempotent per (model, key, suffix).
S="${PANEL_S:?set PANEL_S to the scratchpad panel dir (prompts/ inside)}"
RUN="${RUN:?set RUN to r2 or r3}"
KEYS_FILE="${KEYS_FILE:?set KEYS_FILE to the contested-keys JSON list}"
R="$(cd "$(dirname "$0")/.." && pwd)"
WORKERS="${WORKERS:-4}"
KEYS=$(python3 -c "import json; print(' '.join(json.load(open('$KEYS_FILE'))))")

CODEX_MODEL="gpt-5.6-sol"
CODEX_EFFORT="high"
GEMINI_MODEL="gemini-3.1-pro-high"
OPUS_MODEL="claude-opus-4-8"

meta () {
  printf '{"model":"%s","effort":"%s","cli":"%s","ts":"%s"}\n' \
    "$2" "$3" "$4" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "${1%.json}.meta.json"
}
CODEX_CLI="codex-cli $(codex --version 2>/dev/null | grep -o '[0-9.]*' | head -1)"
AGY_CLI="agy $(agy --version 2>/dev/null | head -1)"
CLAUDE_CLI="claude-cli $(claude --version 2>/dev/null | grep -o '[0-9.]*' | head -1)"

extract_json () { python3 -c "
import sys,re,json
s=sys.stdin.read()
cands=re.findall(r'\{.*\}', s, re.DOTALL)
for c in sorted(cands,key=len,reverse=True):
    try: json.loads(c); print(c); break
    except: continue
"; }

codex_one () {
  local k="$1" o="$R/data/tags-v213/codex/$k.$RUN.json"
  [ -s "$o" ] && return
  timeout 900 codex exec --skip-git-repo-check -c model="$CODEX_MODEL" -c model_reasoning_effort="$CODEX_EFFORT" "$(cat "$S/prompts/$k.txt")" < /dev/null > "$S/codex_${k}_$RUN.raw" 2>"$S/codex_${k}_$RUN.err"
  extract_json < "$S/codex_${k}_$RUN.raw" > "$o"
  [ -s "$o" ] && meta "$o" "$CODEX_MODEL" "$CODEX_EFFORT" "$CODEX_CLI"
  echo "codex $k.$RUN -> $(wc -c < "$o" | tr -d ' ') bytes"
}
gemini_one () {
  local k="$1" o="$R/data/tags-v213/gemini/$k.$RUN.json"
  [ -s "$o" ] && return
  timeout 900 agy --add-dir "$S/prompts" -p "Read the file $S/prompts/$k.txt and follow its instructions exactly. Output ONLY the single JSON object it requires — no commentary." --model "$GEMINI_MODEL" < /dev/null > "$S/gemini_${k}_$RUN.raw" 2>"$S/gemini_${k}_$RUN.err"
  extract_json < "$S/gemini_${k}_$RUN.raw" > "$o"
  [ -s "$o" ] && meta "$o" "$GEMINI_MODEL" "high" "$AGY_CLI"
  echo "gemini $k.$RUN -> $(wc -c < "$o" | tr -d ' ') bytes"
}
opus_one () {
  local k="$1" o="$R/data/tags-v213/opus/$k.$RUN.json"
  [ -s "$o" ] && return
  timeout 900 claude -p "$(cat "$S/prompts/$k.txt")" --model "$OPUS_MODEL" < /dev/null > "$S/opus_${k}_$RUN.raw" 2>"$S/opus_${k}_$RUN.err"
  extract_json < "$S/opus_${k}_$RUN.raw" > "$o"
  [ -s "$o" ] && meta "$o" "$OPUS_MODEL" "default" "$CLAUDE_CLI"
  echo "opus $k.$RUN -> $(wc -c < "$o" | tr -d ' ') bytes"
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
  shard_loop opus_one   "$w" & PIDS="$PIDS $!"
done
wait $PIDS
echo "SWEEP_REPLICATES_${RUN}_DONE"
