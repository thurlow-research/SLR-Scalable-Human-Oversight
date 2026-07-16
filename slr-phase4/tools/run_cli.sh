#!/bin/bash
S="/private/tmp/claude-501/-Users-scott-Library-CloudStorage-OneDrive-purdue-edu-Systemic-Literature-Review/5c8fcfcc-21c4-4108-a98d-205394c1967c/scratchpad"
mkdir -p "$S/tags/codex" "$S/tags/gemini"
KEYS="UB2EVUFU UDVHQ5HR Z8TPRNEU T8E8SCCG M74M3RFJ 2CKL96B8 T72TU8B5 VG6CIDQW 22JBEZNK F9JM9CI6"

extract_json () { python3 -c "
import sys,re,json
s=sys.stdin.read()
# grab the last {...} that parses
cands=re.findall(r'\{.*\}', s, re.DOTALL)
for c in sorted(cands,key=len,reverse=True):
    try: json.loads(c); print(c); break
    except: continue
"; }

for k in $KEYS; do
  sed "s/<KEY>/$k/g" "$S/model_prompt_prefix.txt" > "$S/_p_$k.txt"
  { echo "=== PAPER KEY: $k ==="; cat "$S/txt/$k.txt"; } >> "$S/_p_$k.txt"
  P="$(cat "$S/_p_$k.txt")"

  if [ ! -s "$S/tags/codex/$k.json" ]; then
    timeout 300 codex exec --skip-git-repo-check -c model_reasoning_effort="high" "$P" 2>/dev/null | extract_json > "$S/tags/codex/$k.json"
    echo "codex $k -> $(wc -c < "$S/tags/codex/$k.json") bytes"
  fi
  if [ ! -s "$S/tags/gemini/$k.json" ]; then
    timeout 300 agy -p "$P" --model "Gemini 3.1 Pro (High)" 2>/dev/null | extract_json > "$S/tags/gemini/$k.json"
    echo "gemini $k -> $(wc -c < "$S/tags/gemini/$k.json") bytes"
  fi
  rm -f "$S/_p_$k.txt"
done
echo "SETA_CLI_DONE"
