#!/bin/bash
# run_ssrn_screen.sh
# Archives previous run artifacts and starts a fresh SSRN screening run.
# Usage: cd ~/slr/ssrn && bash run_ssrn_screen.sh

set -e
WORKDIR="$(pwd)"
SCRIPT="ssrn_llm_screen.py"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "=== SSRN Screening Run ==="
echo "Working directory: $WORKDIR"
echo "Timestamp: $TIMESTAMP"
echo ""

# Verify the script exists
if [ ! -f "$SCRIPT" ]; then
    echo "ERROR: $SCRIPT not found in $WORKDIR"
    exit 1
fi

# Archive previous run artifacts if they exist
for f in state.json discards.csv decisions.csv decisions.jsonl progress.log; do
    if [ -f "$f" ]; then
        mv "$f" "${f}.archived-${TIMESTAMP}"
        echo "Archived: $f -> ${f}.archived-${TIMESTAMP}"
    fi
done
echo ""

# Start the run detached
echo "Starting screening run..."
nohup python3 "$SCRIPT" > "run_${TIMESTAMP}.log" 2>&1 &
PID=$!
echo "PID: $PID"
echo ""

# Brief pause then show early output
sleep 3
echo "=== Early log output (Ctrl+C to stop tailing, script keeps running) ==="
tail -f "run_${TIMESTAMP}.log"
