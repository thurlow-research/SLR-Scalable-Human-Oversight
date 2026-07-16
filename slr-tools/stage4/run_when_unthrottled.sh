#!/bin/bash
# Wait (gently) for OpenAlex to stop 429'ing this IP, then run the URL/title pass once.
cd ~/Code/SLR/slr-tools/stage4
export OPENALEX_MAILTO=sthurlow@purdue.edu   # this session's env snapshot lacks it
LOG=work/stage4/oa_title_url.log
URL="https://api.openalex.org/works?filter=title.search:vibe%20coding&per-page=1&mailto=sthurlow@purdue.edu"

echo "$(date '+%H:%M:%S') poller: waiting for OpenAlex 200 (probing every 90s, IPv4)..."
for n in $(seq 1 40); do            # up to ~60 min
  code=$(curl -s -4 -m 8 -o /dev/null -w '%{http_code}' "$URL")
  echo "$(date '+%H:%M:%S') probe $n -> HTTP $code"
  if [ "$code" = "200" ]; then
    echo "$(date '+%H:%M:%S') throttle cleared — launching pass"
    python3 -u oa_title_url.py
    echo "$(date '+%H:%M:%S') === PASS FINISHED ==="
    grep "DONE" "$LOG" | tail -1
    exit 0
  fi
  sleep 90
done
echo "$(date '+%H:%M:%S') gave up after ~60 min still throttled"
exit 1
