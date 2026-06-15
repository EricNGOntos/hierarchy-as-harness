#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

cd "$(dirname "$0")/.."

BUDGETS="${BUDGETS:-500}"
TREERAG_MODEL="${TREERAG_MODEL:-qwen3.5-flash}"
EMBEDDING_MODEL="${EMBEDDING_MODEL:-BAAI/bge-m3}"
RUN_TAG="${RUN_TAG:-quality_balanced60_costclean_v1}"

TASKS="${TASKS:-data/tasks/tasks_realdata_bodyrich_latest_clean_quality_balanced60.jsonl}"
INSPECT_TASKS="${INSPECT_TASKS:-data/tasks/tasks_realdata_bodyrich_latest_clean_quality_balanced60.inspect.jsonl}"

ARGS=(
  --test-jsonl data/corpus/test_data_full_realdata_clean_latest.jsonl
  --tasks "${TASKS}"
  --budgets "${BUDGETS}"
  --treerag-model "${TREERAG_MODEL}"
  --embedding-model "${EMBEDDING_MODEL}"
  --out-template "results/latest_clean_treerag_${RUN_TAG}_b{budget}.json"
  --summary-md "cache/treerag_${RUN_TAG}/run_summary.md"
  --cache-dir "cache/treerag_${RUN_TAG}"
  --compose-judge
  --inspect-judge
  --inspect-tasks "${INSPECT_TASKS}"
  --skip-llm-preflight
  --skip-llm-smoke-check
)

if [[ -n "${MAX_TASKS:-}" ]]; then
  ARGS+=(--max-tasks "${MAX_TASKS}")
fi

PYTHONPATH=src/realdata:src/nav \
python3 src/nav/run_latest_clean_treerag.py "${ARGS[@]}"
