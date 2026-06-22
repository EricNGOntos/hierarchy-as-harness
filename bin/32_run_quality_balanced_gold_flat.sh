#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

cd "$(dirname "$0")/.."

BUDGETS="${BUDGETS:-500}"
NAV_RUN_TAG="${NAV_RUN_TAG:-fair_clean_unified_v1}"
EMBEDDING_MODEL="${EMBEDDING_MODEL:-BAAI/bge-m3}"
# Unified nav fix: hybrid discovery D* before/during nav; post-nav soft_safety removed.
export NAV_DISCOVERY_SOFT_SIGNAL="${NAV_DISCOVERY_SOFT_SIGNAL:-1}"
export NAV_DISCOVERY_RECALL_K="${NAV_DISCOVERY_RECALL_K:-10}"
export NAV_DISCOVERY_PICK_K="${NAV_DISCOVERY_PICK_K:-3}"
export NAV_PATH_ANCHOR_TASK_TYPES="${NAV_PATH_ANCHOR_TASK_TYPES:-scope_collection,regulatory_coverage,multi_hop}"

TASKS="${TASKS:-data/tasks/tasks_realdata_bodyrich_fair_clean.jsonl}"
INSPECT_TASKS="${INSPECT_TASKS:-data/tasks/tasks_realdata_bodyrich_fair_clean.inspect.jsonl}"

if [[ ! -f "${TASKS}" || ! -f "${INSPECT_TASKS}" ]]; then
  echo "missing fair-clean tasks: ${TASKS}" >&2
  exit 1
fi

ARGS=(
  --test_jsonl data/corpus/test_data_full_realdata_clean_latest.jsonl
  --tasks "${TASKS}"
  --retrieval dense
  --embedding-model "${EMBEDDING_MODEL}"
  --budget-chars-list "${BUDGETS}"
  --out-template "results/fair_clean_gold_flat_${NAV_RUN_TAG}_b{budget}.json"
  --hier-policy "${HIER_POLICY:-nav}"
  --nav-config "${NAV_CONFIG:-config/nav_default.json}"
  --nav-policy "${NAV_POLICY:-llm}"
  --inspect-tasks "${INSPECT_TASKS}"
  --inspect-judge
  --checkpoint-dir "cache/fair_clean_gold_flat_${NAV_RUN_TAG}"
)

if [[ -n "${MAX_TASKS:-}" ]]; then
  ARGS+=(--max-tasks "${MAX_TASKS}")
fi

PYTHONPATH=src/realdata:src/nav \
python3 -m agent_delivery.agent.runner_bodyrich "${ARGS[@]}"
