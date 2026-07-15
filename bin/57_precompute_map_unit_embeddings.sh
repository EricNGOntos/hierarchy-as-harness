#!/usr/bin/env bash
# Precompute map unit path/content embeddings for clean400 docs.
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONDONTWRITEBYTECODE=1

TASKS="${TASKS:-data/tasks/tasks_realdata_bodyrich_latest_clean_400.jsonl}"
CORPUS="${CORPUS:-data/corpus/test_data_full_realdata_clean_latest.jsonl}"
PRED_JSONL="${PRED_JSONL:-data/realdata_clean_m1024_best_pred_levels_prevline_fallback.jsonl}"
TREE_SOURCES="${TREE_SOURCES:-gold}"
EMBEDDING_MODEL="${EMBEDDING_MODEL:-text-embedding-v3}"
export BODYRICH_EMBEDDING_BACKEND="${BODYRICH_EMBEDDING_BACKEND:-remote}"
export BODYRICH_EMBEDDING_MODEL="${EMBEDDING_MODEL}"
export EMBEDDING_MODEL="${EMBEDDING_MODEL}"
export BODYRICH_EMBEDDING_CACHE="${BODYRICH_EMBEDDING_CACHE:-1}"
export BODYRICH_EMBEDDING_BATCH_SIZE="${BODYRICH_EMBEDDING_BATCH_SIZE:-10}"

# Load API env if present
if [[ -f src/realdata/agent_delivery/llm_api.env ]]; then
  set -a
  # shellcheck disable=SC1091
  source src/realdata/agent_delivery/llm_api.env
  set +a
fi

PYTHONPATH="src/realdata:src/nav${PYTHONPATH:+:$PYTHONPATH}" python -u bin/57_precompute_map_unit_embeddings.py \
  --tasks "${TASKS}" \
  --corpus "${CORPUS}" \
  --pred-jsonl "${PRED_JSONL}" \
  --tree-sources "${TREE_SOURCES}" \
  --embedding-model "${EMBEDDING_MODEL}"
