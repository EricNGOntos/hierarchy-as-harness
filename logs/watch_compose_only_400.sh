#!/bin/bash
# Durable compose-only runner (macOS): auto-resume + loud status for agent notify.
set -u
ROOT="/Users/wuchengke/Desktop/research-code/hierarchy-as-harness_f"
cd "$ROOT"
OUT="results/latest_clean400_map_nav_waterfill_oversize_compose_only_b500.json"
CKPT="cache/compose_from_replay_latest_clean400_map_nav_waterfill_oversize_compose_only_b500/checkpoint.jsonl"
STATUS="logs/compose_only_STATUS.txt"
RUNLOG="logs/compose_only_waterfill_400_watch.log"
PATTERN="59_compose_judge_from_evidence.py"
TARGET=400

ckpt_n() {
  if [[ -f "$CKPT" ]]; then
    grep -c . "$CKPT" 2>/dev/null || echo 0
  else
    echo 0
  fi
}

is_running() {
  # Match the compose-only job specifically via out path in cmdline
  pgrep -f "59_compose_judge_from_evidence.py.*waterfill_oversize_compose_only" >/dev/null 2>&1
}

start_job() {
  nohup python bin/59_compose_judge_from_evidence.py \
    --replay-dir map_nav_trace/replay_400_waterfill_oversize_merged \
    --compose-only \
    --out "$OUT" \
    >> "$RUNLOG" 2>&1 < /dev/null &
  local pid=$!
  disown "$pid" 2>/dev/null || true
  echo "$pid"
}

echo "WATCH_START $(date '+%F %T')" | tee "$STATUS"
echo "AGENT_COMPOSE_WATCH_START {\"target\":$TARGET}"

while true; do
  n=$(ckpt_n)
  n=${n//[^0-9]/}
  n=${n:-0}
  if [[ "$n" -ge "$TARGET" ]]; then
    msg="DONE ${n}/${TARGET} at $(date '+%F %T')"
    echo "$msg" | tee "$STATUS"
    echo "AGENT_COMPOSE_DONE {\"n\":$n,\"target\":$TARGET,\"out\":\"$OUT\"}"
    exit 0
  fi
  if ! is_running; then
    msg="STOPPED ${n}/${TARGET} at $(date '+%F %T') — auto-resuming"
    echo "$msg" | tee -a "$STATUS"
    echo "AGENT_COMPOSE_STOPPED {\"n\":$n,\"target\":$TARGET,\"action\":\"resume\"}"
    pid=$(start_job)
    echo "RESUMED pid=$pid n=${n}/${TARGET} $(date '+%F %T')" | tee -a "$STATUS"
    echo "AGENT_COMPOSE_RESUMED {\"n\":$n,\"pid\":$pid}"
    sleep 5
  else
    echo "RUNNING ${n}/${TARGET} $(date '+%F %T')" > "$STATUS"
  fi
  sleep 20
done
