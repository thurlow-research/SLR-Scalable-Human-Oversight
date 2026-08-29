#!/bin/bash
# F2 restricted re-run — all three legs (codex + gemini CLIs, opus via claude CLI).
#
# Same sharding / idempotency / sidecar pattern as run_sweep_panel.sh, with the
# panel identities PINNED rather than inherited from CLI defaults — inheriting
# would silently swap the calibration gauge between measurement points.
#
# Writes JSON to slr-phase4/data/tags-f2/<vendor>/<key>[.<RUN>].json.
# NOTHING is written to Zotero here; the write-back is a separate authorised step.
#
# Idempotent per (vendor, key, run): an existing non-empty output is never redone,
# so an interrupted run resumes by re-invoking the same command.
#
# Usage:
#   PANEL_S=<scratchpad> slr-phase4/tools/run_f2_panel.sh          # replicate r1
#   PANEL_S=<scratchpad> RUN=r2 slr-phase4/tools/run_f2_panel.sh   # replicate r2
#   PANEL_S=<scratchpad> LEGS="opus" slr-phase4/tools/run_f2_panel.sh
set -u

S="${PANEL_S:?set PANEL_S to the scratchpad panel dir (prompts/ inside)}"
R="$(cd "$(dirname "$0")/.." && pwd)"
WORKERS="${WORKERS:-4}"
RUN="${RUN:-r1}"
LEGS="${LEGS:-codex gemini opus}"
KEYS_FILE="${KEYS_FILE:-$S/f2_keys.json}"
KEYS=$(python3 -c "import json;print(' '.join(json.load(open('$KEYS_FILE'))))")

# Pinned panel identities — must match the v2.13 sweep so T2 stays comparable.
CODEX_MODEL="gpt-5.6-sol"
CODEX_EFFORT="high"
GEMINI_MODEL="gemini-3.1-pro-high"
OPUS_MODEL="claude-opus-4-8"

CODEX_CLI="codex $(codex --version 2>/dev/null | grep -o '[0-9.]*' | head -1)"
AGY_CLI="agy $(agy --version 2>/dev/null | grep -o '[0-9.]*' | head -1)"
CLAUDE_CLI="claude-cli $(claude --version 2>/dev/null | grep -o '[0-9.]*' | head -1)"

sfx () { [ "$RUN" = "r1" ] && echo "" || echo ".$RUN"; }
SFX="$(sfx)"

for v in codex gemini opus; do mkdir -p "$R/data/tags-f2/$v"; done

meta () {
  printf '{"model":"%s","effort":"%s","cli":"%s","run":"%s","instrument":"Tag_Prompt_F2_restricted.md","ts":"%s"}\n' \
    "$2" "$3" "$4" "$RUN" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "${1%.json}.meta.json"
}

extract_json () { python3 -c "
import sys,re,json
s=sys.stdin.read()
cands=re.findall(r'\{.*\}', s, re.DOTALL)
for c in sorted(cands,key=len,reverse=True):
    try: json.loads(c); print(c); break
    except: continue
"; }

codex_one () {
  local k="$1" o="$R/data/tags-f2/codex/$k$SFX.json"
  [ -s "$o" ] && return
  timeout 900 codex exec --skip-git-repo-check -c model="$CODEX_MODEL" \
    -c model_reasoning_effort="$CODEX_EFFORT" "$(cat "$S/prompts/$k.txt")" \
    < /dev/null > "$S/codex_$k$SFX.raw" 2>"$S/codex_$k$SFX.err"
  extract_json < "$S/codex_$k$SFX.raw" > "$o"
  [ -s "$o" ] && meta "$o" "$CODEX_MODEL" "$CODEX_EFFORT" "$CODEX_CLI"
  echo "codex  $k$SFX -> $(wc -c < "$o" | tr -d ' ') bytes"
}

gemini_one () {
  local k="$1" o="$R/data/tags-f2/gemini/$k$SFX.json"
  [ -s "$o" ] && return
  timeout 900 agy --add-dir "$S/prompts" \
    -p "Read the file $S/prompts/$k.txt and follow its instructions exactly. Output ONLY the single JSON object it requires — no commentary." \
    --model "$GEMINI_MODEL" < /dev/null > "$S/gemini_$k$SFX.raw" 2>"$S/gemini_$k$SFX.err"
  extract_json < "$S/gemini_$k$SFX.raw" > "$o"
  [ -s "$o" ] && meta "$o" "$GEMINI_MODEL" "high" "$AGY_CLI"
  echo "gemini $k$SFX -> $(wc -c < "$o" | tr -d ' ') bytes"
}

opus_one () {
  local k="$1" o="$R/data/tags-f2/opus/$k$SFX.json"
  [ -s "$o" ] && return
  timeout 900 claude -p "$(cat "$S/prompts/$k.txt")" --model "$OPUS_MODEL" \
    < /dev/null > "$S/opus_$k$SFX.raw" 2>"$S/opus_$k$SFX.err"
  extract_json < "$S/opus_$k$SFX.raw" > "$o"
  [ -s "$o" ] && meta "$o" "$OPUS_MODEL" "default" "$CLAUDE_CLI"
  echo "opus   $k$SFX -> $(wc -c < "$o" | tr -d ' ') bytes"
}

shard_loop () {  # shard_loop <fn> <shard-index>
  local fn="$1" idx="$2" i=0
  for k in $KEYS; do
    [ $(( i % WORKERS )) -eq "$idx" ] && "$fn" "$k"
    i=$(( i + 1 ))
  done
}

echo "F2 run=$RUN legs='$LEGS' keys=$(echo "$KEYS" | wc -w | tr -d ' ') workers=$WORKERS"
echo "out: $R/data/tags-f2/<vendor>/  (nothing written to Zotero)"

PIDS=""
for w in $(seq 0 $(( WORKERS - 1 ))); do
  for leg in $LEGS; do
    shard_loop "${leg}_one" "$w" & PIDS="$PIDS $!"
  done
done
wait $PIDS
echo "F2_PANEL_${RUN}_DONE"
