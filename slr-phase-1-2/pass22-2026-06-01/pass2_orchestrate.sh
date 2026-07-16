#!/usr/bin/env bash
# =============================================================================
# pass2_orchestrate.sh
# Pass 2 screening orchestration for Vibe Coding Governance SLR
#
# Workflow:
#   1. Export Phase 2 Queue items from Zotero → CSV
#   2. Randomize order (prevent topic clustering bias)
#   3. Split into 50-row Sonnet batches
#   4. Run Sonnet screening on each batch (30s rate limit)
#   5. Consolidate Sonnet results
#   6. Route: maybe + low-confidence → Opus queue; others → apply queue
#   7. Split Opus queue into 20-row batches
#   8. Run Opus review on each batch (60s rate limit)
#   9. Consolidate Opus results
#  10. Route: Opus low-confidence + conflicts → human review report
#  11. Apply all decisions to Zotero
#  12. Generate human review report
#
# Checkpoint: state saved after every batch. Re-run to resume.
# Failures: logged to failed_batches.csv for reprocessing.
#
# Usage:
#   chmod +x pass2_orchestrate.sh
#   nohup bash pass2_orchestrate.sh > pass2_nohup.log 2>&1 &
#   echo $!
#   tail -f pass2_nohup.log
#
# Resume after interruption:
#   nohup bash pass2_orchestrate.sh > pass2_nohup.log 2>&1 &
# =============================================================================

set -euo pipefail

# ============================================================
# CONFIG
# ============================================================
WORKDIR="$(pwd)"
SCRIPTS_DIR="$(pwd)"              # python scripts expected in same directory
PROMPT_SONNET="${WORKDIR}/pass2_sonnet_prompt.md"
PROMPT_OPUS="${WORKDIR}/pass2_opus_prompt.md"

SONNET_MODEL="claude-sonnet-4-6"
OPUS_MODEL="claude-opus-4-5"       # update if model string changes

SONNET_BATCH_SIZE=50
OPUS_BATCH_SIZE=20
SONNET_RATE_LIMIT=30               # seconds between Sonnet calls
OPUS_RATE_LIMIT=60                 # seconds between Opus calls

# Phase 2 Zotero collection keys
PHASE2_KEEP_QUEUE="JFHGBVLY"
PHASE2_MAYBE_QUEUE="JUDYQCPU"
PHASE2_KEEP_COLL="3D8XR6AP"
PHASE2_MAYBE_COLL="5VHKIH5W"
PHASE2_DISCARD_COLL="9A2LGHUT"
PHASE2_MAYBE_KEEP_COLL="ZB6R4G9H"
PHASE2_MAYBE_DISCARD_COLL="TA8JUISM"

CHECKPOINT="${WORKDIR}/checkpoint.json"
LOG="${WORKDIR}/pass2.log"
FAILED_CSV="${WORKDIR}/failed_batches.csv"

# ============================================================
# LOGGING
# ============================================================
log() {
    echo "[$(date -u '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "${LOG}"
}

# ============================================================
# CHECKPOINT HELPERS
# ============================================================
checkpoint_get() {
    local key="$1"
    local default="${2:-}"
    if [ -f "${CHECKPOINT}" ]; then
        python3 -c "
import json, sys
d = json.load(open('${CHECKPOINT}'))
print(d.get('${key}', '${default}'))
" 2>/dev/null || echo "${default}"
    else
        echo "${default}"
    fi
}

checkpoint_set() {
    local key="$1"
    local value="$2"
    python3 -c "
import json, os
cp = '${CHECKPOINT}'
d = json.load(open(cp)) if os.path.exists(cp) else {}
d['${key}'] = '${value}'
json.dump(d, open(cp, 'w'), indent=2)
"
}

# ============================================================
# SETUP
# ============================================================
mkdir -p "${WORKDIR}"
mkdir -p "${WORKDIR}/batches/sonnet"
mkdir -p "${WORKDIR}/batches/opus"

log "=== Pass 2 Orchestration ==="
log "Workdir: ${WORKDIR}"
log "Checkpoint: ${CHECKPOINT}"

# Init failed batches CSV if needed
if [ ! -f "${FAILED_CSV}" ]; then
    echo "batch_file,stage,error,timestamp" > "${FAILED_CSV}"
fi

# ============================================================
# STEP 1: EXPORT PHASE 2 QUEUE ITEMS FROM ZOTERO
# ============================================================
QUEUE_EXPORT="${WORKDIR}/queue_export.csv"
EXPORT_DONE=$(checkpoint_get "export_done" "false")

if [ "${EXPORT_DONE}" = "true" ]; then
    log "STEP 1: Export already done — skipping"
else
    log "STEP 1: Exporting Phase 2 Queue items from Zotero..."
    python3 "${SCRIPTS_DIR}/export_phase2_queue.py" \
        --keep-queue "${PHASE2_KEEP_QUEUE}" \
        --maybe-queue "${PHASE2_MAYBE_QUEUE}" \
        --output "${QUEUE_EXPORT}"
    EXPORT_COUNT=$(tail -n +2 "${QUEUE_EXPORT}" | wc -l | tr -d ' ')
    log "  Exported ${EXPORT_COUNT} items to ${QUEUE_EXPORT}"
    checkpoint_set "export_done" "true"
    checkpoint_set "export_count" "${EXPORT_COUNT}"
fi

# ============================================================
# STEP 2: RANDOMIZE ORDER
# ============================================================
QUEUE_RANDOM="${WORKDIR}/queue_randomized.csv"
RANDOMIZE_DONE=$(checkpoint_get "randomize_done" "false")

if [ "${RANDOMIZE_DONE}" = "true" ]; then
    log "STEP 2: Randomization already done — skipping"
else
    log "STEP 2: Randomizing item order..."
    python3 -c "
import csv, random
with open('${QUEUE_EXPORT}', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames
random.shuffle(rows)
with open('${QUEUE_RANDOM}', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
print(f'Randomized {len(rows)} items')
"
    checkpoint_set "randomize_done" "true"
fi

# ============================================================
# STEP 3: SPLIT INTO SONNET BATCHES
# ============================================================
SPLIT_DONE=$(checkpoint_get "sonnet_split_done" "false")

if [ "${SPLIT_DONE}" = "true" ]; then
    log "STEP 3: Sonnet batch split already done — skipping"
else
    log "STEP 3: Splitting into ${SONNET_BATCH_SIZE}-row Sonnet batches..."
    python3 "${SCRIPTS_DIR}/split_batches.py" \
        "${QUEUE_RANDOM}" \
        --output-dir "${WORKDIR}/batches/sonnet" \
        --batch-size "${SONNET_BATCH_SIZE}"
    SONNET_BATCH_COUNT=$(ls "${WORKDIR}/batches/sonnet"/batch_*.csv 2>/dev/null | wc -l | tr -d ' ')
    log "  Created ${SONNET_BATCH_COUNT} Sonnet batches"
    checkpoint_set "sonnet_split_done" "true"
    checkpoint_set "sonnet_batch_count" "${SONNET_BATCH_COUNT}"
fi

# ============================================================
# STEP 4: RUN SONNET SCREENING
# ============================================================
log "STEP 4: Running Sonnet screening..."
SONNET_BATCHES=$(ls "${WORKDIR}/batches/sonnet"/batch_*.csv 2>/dev/null | sort)

for batch_file in ${SONNET_BATCHES}; do
    batch_name=$(basename "${batch_file}" .csv)
    out_file="${WORKDIR}/batches/sonnet/${batch_name}_out.csv"
    ck_key="sonnet_done_${batch_name}"
    done=$(checkpoint_get "${ck_key}" "false")

    if [ "${done}" = "true" ]; then
        log "  Sonnet ${batch_name}: already done — skipping"
        continue
    fi

    log "  Sonnet ${batch_name}: screening..."

    # Build prompt with batch data appended
    PROMPT_WITH_DATA=$(mktemp)
    cat "${PROMPT_SONNET}" > "${PROMPT_WITH_DATA}"
    echo "" >> "${PROMPT_WITH_DATA}"
    cat "${batch_file}" >> "${PROMPT_WITH_DATA}"

    # Run via Claude Code CLI
    set +e
    claude -p "$(cat "${PROMPT_WITH_DATA}")" \
        --model "${SONNET_MODEL}" \
        --output-format text \
        > "${out_file}.raw" 2>&1
    EXIT_CODE=$?
    set -e

    rm -f "${PROMPT_WITH_DATA}"

    if [ ${EXIT_CODE} -ne 0 ]; then
        log "  FAILED ${batch_name}: exit code ${EXIT_CODE}"
        echo "${batch_file},sonnet,exit_code_${EXIT_CODE},$(date -u)" >> "${FAILED_CSV}"
        sleep "${SONNET_RATE_LIMIT}"
        continue
    fi

    # Extract CSV from output (strip any preamble/postamble)
    python3 -c "
import sys, re
raw = open('${out_file}.raw', encoding='utf-8').read()
# Find CSV block — look for header line
lines = raw.strip().split('\n')
csv_start = None
for i, line in enumerate(lines):
    if line.strip().startswith('item_key,'):
        csv_start = i
        break
if csv_start is None:
    print('ERROR: no CSV header found', file=sys.stderr)
    sys.exit(1)
csv_lines = lines[csv_start:]
# Stop at first blank line after data
result = []
for line in csv_lines:
    if result and not line.strip():
        break
    if line.strip():
        result.append(line)
with open('${out_file}', 'w', encoding='utf-8') as f:
    f.write('\n'.join(result) + '\n')
print(f'Extracted {len(result)-1} rows')
"
    if [ $? -ne 0 ]; then
        log "  FAILED ${batch_name}: CSV extraction failed"
        echo "${batch_file},sonnet,csv_extraction_failed,$(date -u)" >> "${FAILED_CSV}"
        sleep "${SONNET_RATE_LIMIT}"
        continue
    fi

    # Validate row count
    INPUT_ROWS=$(tail -n +2 "${batch_file}" | wc -l | tr -d ' ')
    OUTPUT_ROWS=$(tail -n +2 "${out_file}" | wc -l | tr -d ' ')
    if [ "${OUTPUT_ROWS}" -lt "${INPUT_ROWS}" ]; then
        log "  WARNING ${batch_name}: input=${INPUT_ROWS} output=${OUTPUT_ROWS} — rows missing"
        echo "${batch_file},sonnet,row_count_mismatch_${INPUT_ROWS}_vs_${OUTPUT_ROWS},$(date -u)" >> "${FAILED_CSV}"
    else
        log "  OK ${batch_name}: ${OUTPUT_ROWS} rows"
    fi

    checkpoint_set "${ck_key}" "true"
    sleep "${SONNET_RATE_LIMIT}"
done

# ============================================================
# STEP 5: CONSOLIDATE SONNET RESULTS
# ============================================================
SONNET_RESULTS="${WORKDIR}/sonnet_results.csv"
CONSOLIDATE_DONE=$(checkpoint_get "sonnet_consolidate_done" "false")

if [ "${CONSOLIDATE_DONE}" = "true" ]; then
    log "STEP 5: Sonnet consolidation already done — skipping"
else
    log "STEP 5: Consolidating Sonnet results..."
    python3 -c "
import csv, os, glob

out_files = sorted(glob.glob('${WORKDIR}/batches/sonnet/*_out.csv'))
rows = []
for f in out_files:
    try:
        with open(f, encoding='utf-8-sig') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                rows.append(row)
    except Exception as e:
        print(f'  SKIP {f}: {e}')

if not rows:
    print('ERROR: no output rows found')
    exit(1)

fieldnames = ['item_key','decision','confidence','rationale']
with open('${SONNET_RESULTS}', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(rows)
print(f'Consolidated {len(rows)} Sonnet decisions')

from collections import Counter
decisions = Counter(r.get('decision','').lower() for r in rows)
confidence = Counter(r.get('confidence','').lower() for r in rows)
print(f'Decisions: {dict(decisions)}')
print(f'Confidence: {dict(confidence)}')
"
    checkpoint_set "sonnet_consolidate_done" "true"
fi

# ============================================================
# STEP 6: ROUTE ITEMS — SONNET → OPUS OR APPLY QUEUE
# ============================================================
OPUS_INPUT="${WORKDIR}/opus_input.csv"
APPLY_FROM_SONNET="${WORKDIR}/apply_from_sonnet.csv"
ROUTE_DONE=$(checkpoint_get "sonnet_route_done" "false")

if [ "${ROUTE_DONE}" = "true" ]; then
    log "STEP 6: Sonnet routing already done — skipping"
else
    log "STEP 6: Routing Sonnet results..."
    python3 -c "
import csv

sonnet = list(csv.DictReader(open('${SONNET_RESULTS}', encoding='utf-8-sig')))

# Load original queue for title/abstract lookup
queue = {r['item_key']: r for r in
         csv.DictReader(open('${QUEUE_RANDOM}', encoding='utf-8-sig'))}

opus_rows = []
apply_rows = []

for row in sonnet:
    decision = row.get('decision','').lower().strip()
    confidence = row.get('confidence','').lower().strip()
    # Route to Opus: maybe OR low confidence
    if decision == 'maybe' or confidence == 'low':
        orig = queue.get(row['item_key'], {})
        opus_rows.append({
            'item_key':         row['item_key'],
            'title':            orig.get('title', ''),
            'abstract':         orig.get('abstract', ''),
            'prior_decision':   decision,
            'prior_confidence': confidence,
            'prior_rationale':  row.get('rationale', ''),
        })
    else:
        apply_rows.append(row)

# Write Opus input
with open('${OPUS_INPUT}', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['item_key','title','abstract',
                  'prior_decision','prior_confidence','prior_rationale']
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(opus_rows)

# Write apply-from-sonnet
with open('${APPLY_FROM_SONNET}', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['item_key','decision','confidence','rationale']
    w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    w.writeheader()
    w.writerows(apply_rows)

print(f'Routed to Opus: {len(opus_rows)}')
print(f'Direct apply:   {len(apply_rows)}')
"
    checkpoint_set "sonnet_route_done" "true"
fi

# ============================================================
# STEP 7: SPLIT OPUS BATCHES
# ============================================================
OPUS_SPLIT_DONE=$(checkpoint_get "opus_split_done" "false")

if [ "${OPUS_SPLIT_DONE}" = "true" ]; then
    log "STEP 7: Opus batch split already done — skipping"
else
    OPUS_COUNT=$(tail -n +2 "${OPUS_INPUT}" | wc -l | tr -d ' ')
    log "STEP 7: Splitting ${OPUS_COUNT} items into ${OPUS_BATCH_SIZE}-row Opus batches..."
    if [ "${OPUS_COUNT}" -gt 0 ]; then
        python3 "${SCRIPTS_DIR}/split_batches.py" \
            "${OPUS_INPUT}" \
            --output-dir "${WORKDIR}/batches/opus" \
            --batch-size "${OPUS_BATCH_SIZE}"
        OPUS_BATCH_COUNT=$(ls "${WORKDIR}/batches/opus"/batch_*.csv 2>/dev/null | wc -l | tr -d ' ')
        log "  Created ${OPUS_BATCH_COUNT} Opus batches"
    else
        log "  No items for Opus — skipping"
        OPUS_BATCH_COUNT=0
    fi
    checkpoint_set "opus_split_done" "true"
    checkpoint_set "opus_batch_count" "${OPUS_BATCH_COUNT}"
fi

# ============================================================
# STEP 8: RUN OPUS REVIEW
# ============================================================
log "STEP 8: Running Opus review..."
OPUS_BATCHES=$(ls "${WORKDIR}/batches/opus"/batch_*.csv 2>/dev/null | sort || true)

for batch_file in ${OPUS_BATCHES}; do
    batch_name=$(basename "${batch_file}" .csv)
    out_file="${WORKDIR}/batches/opus/${batch_name}_out.csv"
    ck_key="opus_done_${batch_name}"
    done=$(checkpoint_get "${ck_key}" "false")

    if [ "${done}" = "true" ]; then
        log "  Opus ${batch_name}: already done — skipping"
        continue
    fi

    log "  Opus ${batch_name}: reviewing..."

    PROMPT_WITH_DATA=$(mktemp)
    cat "${PROMPT_OPUS}" > "${PROMPT_WITH_DATA}"
    echo "" >> "${PROMPT_WITH_DATA}"
    cat "${batch_file}" >> "${PROMPT_WITH_DATA}"

    set +e
    claude -p "$(cat "${PROMPT_WITH_DATA}")" \
        --model "${OPUS_MODEL}" \
        --output-format text \
        > "${out_file}.raw" 2>&1
    EXIT_CODE=$?
    set -e

    rm -f "${PROMPT_WITH_DATA}"

    if [ ${EXIT_CODE} -ne 0 ]; then
        log "  FAILED ${batch_name}: exit code ${EXIT_CODE}"
        echo "${batch_file},opus,exit_code_${EXIT_CODE},$(date -u)" >> "${FAILED_CSV}"
        sleep "${OPUS_RATE_LIMIT}"
        continue
    fi

    # Extract CSV
    python3 -c "
import sys
raw = open('${out_file}.raw', encoding='utf-8').read()
lines = raw.strip().split('\n')
csv_start = None
for i, line in enumerate(lines):
    if line.strip().startswith('item_key,'):
        csv_start = i
        break
if csv_start is None:
    print('ERROR: no CSV header found', file=sys.stderr)
    sys.exit(1)
csv_lines = lines[csv_start:]
result = []
for line in csv_lines:
    if result and not line.strip():
        break
    if line.strip():
        result.append(line)
with open('${out_file}', 'w', encoding='utf-8') as f:
    f.write('\n'.join(result) + '\n')
print(f'Extracted {len(result)-1} rows')
"
    if [ $? -ne 0 ]; then
        log "  FAILED ${batch_name}: CSV extraction failed"
        echo "${batch_file},opus,csv_extraction_failed,$(date -u)" >> "${FAILED_CSV}"
        sleep "${OPUS_RATE_LIMIT}"
        continue
    fi

    INPUT_ROWS=$(tail -n +2 "${batch_file}" | wc -l | tr -d ' ')
    OUTPUT_ROWS=$(tail -n +2 "${out_file}" | wc -l | tr -d ' ')
    if [ "${OUTPUT_ROWS}" -lt "${INPUT_ROWS}" ]; then
        log "  WARNING ${batch_name}: input=${INPUT_ROWS} output=${OUTPUT_ROWS}"
        echo "${batch_file},opus,row_count_mismatch_${INPUT_ROWS}_vs_${OUTPUT_ROWS},$(date -u)" >> "${FAILED_CSV}"
    else
        log "  OK ${batch_name}: ${OUTPUT_ROWS} rows"
    fi

    checkpoint_set "${ck_key}" "true"
    sleep "${OPUS_RATE_LIMIT}"
done

# ============================================================
# STEP 9: CONSOLIDATE OPUS RESULTS
# ============================================================
OPUS_RESULTS="${WORKDIR}/opus_results.csv"
OPUS_CONSOLIDATE_DONE=$(checkpoint_get "opus_consolidate_done" "false")

if [ "${OPUS_CONSOLIDATE_DONE}" = "true" ]; then
    log "STEP 9: Opus consolidation already done — skipping"
else
    log "STEP 9: Consolidating Opus results..."
    python3 -c "
import csv, glob

out_files = sorted(glob.glob('${WORKDIR}/batches/opus/*_out.csv'))
rows = []
for f in out_files:
    try:
        with open(f, encoding='utf-8-sig') as fh:
            for row in csv.DictReader(fh):
                rows.append(row)
    except Exception as e:
        print(f'  SKIP {f}: {e}')

if rows:
    fieldnames = ['item_key','decision','confidence','rationale',
                  'prior_decision','prior_confidence']
    with open('${OPUS_RESULTS}', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)
    print(f'Consolidated {len(rows)} Opus decisions')
    from collections import Counter
    print(f'Decisions: {dict(Counter(r.get(\"decision\",\"\").lower() for r in rows))}')
    print(f'Confidence: {dict(Counter(r.get(\"confidence\",\"\").lower() for r in rows))}')
else:
    print('No Opus results to consolidate')
    open('${OPUS_RESULTS}', 'w').write('item_key,decision,confidence,rationale,prior_decision,prior_confidence\n')
"
    checkpoint_set "opus_consolidate_done" "true"
fi

# ============================================================
# STEP 10: ROUTE OPUS — APPLY OR HUMAN REVIEW
# ============================================================
APPLY_FROM_OPUS="${WORKDIR}/apply_from_opus.csv"
HUMAN_REVIEW="${WORKDIR}/human_review.csv"
OPUS_ROUTE_DONE=$(checkpoint_get "opus_route_done" "false")

if [ "${OPUS_ROUTE_DONE}" = "true" ]; then
    log "STEP 10: Opus routing already done — skipping"
else
    log "STEP 10: Routing Opus results..."
    python3 -c "
import csv

opus = list(csv.DictReader(open('${OPUS_RESULTS}', encoding='utf-8-sig')))
sonnet = {r['item_key']: r for r in
          csv.DictReader(open('${SONNET_RESULTS}', encoding='utf-8-sig'))}

apply_rows = []
human_rows = []

for row in opus:
    decision   = row.get('decision','').lower().strip()
    confidence = row.get('confidence','').lower().strip()
    prior_dec  = row.get('prior_decision','').lower().strip()

    # Conflict: Sonnet and Opus disagree
    conflict = (prior_dec in ('keep','discard') and
                decision != prior_dec and
                prior_dec != 'maybe')

    if confidence == 'low' or conflict:
        s = sonnet.get(row['item_key'], {})
        human_rows.append({
            'item_key':          row['item_key'],
            'sonnet_decision':   s.get('decision',''),
            'sonnet_confidence': s.get('confidence',''),
            'sonnet_rationale':  s.get('rationale',''),
            'opus_decision':     decision,
            'opus_confidence':   confidence,
            'opus_rationale':    row.get('rationale',''),
            'escalation_reason': 'opus_low_confidence' if confidence == 'low'
                                 else 'sonnet_opus_conflict',
            'reviewer_decision': '',
            'reviewer_notes':    '',
        })
    else:
        apply_rows.append({
            'item_key':   row['item_key'],
            'decision':   decision,
            'confidence': confidence,
            'rationale':  row.get('rationale',''),
        })

fieldnames = ['item_key','decision','confidence','rationale']
with open('${APPLY_FROM_OPUS}', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(apply_rows)

human_fields = ['item_key','sonnet_decision','sonnet_confidence','sonnet_rationale',
                'opus_decision','opus_confidence','opus_rationale',
                'escalation_reason','reviewer_decision','reviewer_notes']
with open('${HUMAN_REVIEW}', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=human_fields)
    w.writeheader()
    w.writerows(human_rows)

print(f'Opus apply queue: {len(apply_rows)}')
print(f'Human review:     {len(human_rows)}')
"
    checkpoint_set "opus_route_done" "true"
fi

# ============================================================
# STEP 11: APPLY DECISIONS TO ZOTERO
# ============================================================
APPLY_DONE=$(checkpoint_get "apply_done" "false")

if [ "${APPLY_DONE}" = "true" ]; then
    log "STEP 11: Zotero apply already done — skipping"
else
    log "STEP 11: Applying decisions to Zotero..."

    # Merge Sonnet + Opus apply queues
    APPLY_ALL="${WORKDIR}/apply_all.csv"
    python3 -c "
import csv

sonnet = list(csv.DictReader(open('${APPLY_FROM_SONNET}', encoding='utf-8-sig')))
opus   = list(csv.DictReader(open('${APPLY_FROM_OPUS}',   encoding='utf-8-sig')))

# Opus takes precedence over Sonnet for overlapping keys
all_rows = {r['item_key']: r for r in sonnet}
for r in opus:
    all_rows[r['item_key']] = r  # Opus overrides

rows = list(all_rows.values())
fieldnames = ['item_key','decision','confidence','rationale']
with open('${APPLY_ALL}', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    w.writeheader()
    w.writerows(rows)
print(f'Total to apply: {len(rows)}')
"

    python3 "${SCRIPTS_DIR}/apply_screening_decisions.py" \
        "${APPLY_ALL}" --apply

    checkpoint_set "apply_done" "true"
fi

# ============================================================
# STEP 12: FINAL SUMMARY
# ============================================================
log ""
log "=== PASS 2 COMPLETE ==="
log ""

python3 -c "
import csv
from collections import Counter

def count_decisions(f):
    try:
        rows = list(csv.DictReader(open(f, encoding='utf-8-sig')))
        return Counter(r.get('decision','').lower() for r in rows), len(rows)
    except:
        return Counter(), 0

s_dec, s_n = count_decisions('${SONNET_RESULTS}')
o_dec, o_n = count_decisions('${OPUS_RESULTS}')

try:
    h_n = sum(1 for _ in open('${HUMAN_REVIEW}')) - 1
except:
    h_n = 0

try:
    f_n = sum(1 for _ in open('${FAILED_CSV}')) - 1
except:
    f_n = 0

print(f'Sonnet screened:      {s_n}')
print(f'  keep:    {s_dec[\"keep\"]}')
print(f'  maybe:   {s_dec[\"maybe\"]}')
print(f'  discard: {s_dec[\"discard\"]}')
print(f'')
print(f'Opus reviewed:        {o_n}')
print(f'  keep:    {o_dec[\"keep\"]}')
print(f'  discard: {o_dec[\"discard\"]}')
print(f'')
print(f'Human review queue:   {h_n}  → {\"${HUMAN_REVIEW}\"}')
print(f'Failed batches:       {f_n}  → {\"${FAILED_CSV}\"}')
print(f'')
print(f'Log:                  ${LOG}')
print(f'Checkpoint:           ${CHECKPOINT}')
" | tee -a "${LOG}"

log ""
log "Next steps:"
log "  1. Review human_review.csv and fill in reviewer_decision column"
log "  2. Run apply_screening_decisions.py on human_review.csv --apply"
log "  3. Check failed_batches.csv for any batches needing reprocessing"
log "  4. Run phase2_queue_sanity.py to verify final state"
