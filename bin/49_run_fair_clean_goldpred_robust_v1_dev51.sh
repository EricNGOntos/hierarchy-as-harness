#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

cd "$(dirname "$0")/.."

RUN_TAG="${RUN_TAG:-fair_clean_goldpred_robust_v1b_dev51}"
RUN_ROOT="cache/${RUN_TAG}"
GOLD_ROOT="${RUN_ROOT}/gold"
PRED_ROOT="${RUN_ROOT}/pred"
LOG_ROOT="${RUN_ROOT}/logs"
mkdir -p "${GOLD_ROOT}/logs" "${PRED_ROOT}/logs" "${LOG_ROOT}"

TASKS="${TASKS:-data/tasks/tasks_realdata_bodyrich_fair_clean.jsonl}"
INSPECT_TASKS="${INSPECT_TASKS:-data/tasks/tasks_realdata_bodyrich_fair_clean.inspect.jsonl}"
CORPUS="${CORPUS:-data/corpus/test_data_full_realdata_clean_latest.jsonl}"
PRED_JSONL="${PRED_JSONL:-data/realdata_clean_m1024_best_pred_levels_prevline_fallback.jsonl}"
FLAT_SOURCE="${FLAT_SOURCE:-results/fair_clean_gold_flat_fair_clean_goldnav_e2_v1_b500.json}"
TREERAG_SOURCE="${TREERAG_SOURCE:-results/fair_clean_treerag_fair_clean_goldnav_e2_v1_b500.json}"
GOLD_OUT="results/${RUN_TAG}_gold_b500.json"
PRED_OUT="results/${RUN_TAG}_pred_b500.json"
SUMMARY_JSON="results/${RUN_TAG}_summary.json"
SUMMARY_MD="results/${RUN_TAG}_summary.md"
EMBEDDING_MODEL="${EMBEDDING_MODEL:-BAAI/bge-m3}"

for path in "${TASKS}" "${INSPECT_TASKS}" "${CORPUS}" "${PRED_JSONL}" "${FLAT_SOURCE}" "${TREERAG_SOURCE}"; do
  if [[ ! -f "${path}" ]]; then
    echo "missing required file: ${path}" >&2
    exit 1
  fi
done

python3 bin/47_prepare_pred400_cache.py \
  --run-root "${RUN_ROOT}" \
  --shared-cache cache/llm_api_cache.jsonl \
  --shared-cache cache/fair_clean_goldpred_robust_v1b_dev51/shared_llm_api_cache.jsonl \
  --shared-cache cache/latest_clean400_goldpred_robust_v1/shared_llm_api_cache.jsonl \
  > "${LOG_ROOT}/cache_prepare.log"

export BODYRICH_LLM_API_CACHE_PATH="${RUN_ROOT}/shared_llm_api_cache.jsonl"
export BODYRICH_LLM_API_CACHE=1

export NAV_DISCOVERY_SOFT_SIGNAL="${NAV_DISCOVERY_SOFT_SIGNAL:-1}"
export NAV_DISCOVERY_RECALL_K="${NAV_DISCOVERY_RECALL_K:-10}"
export NAV_DISCOVERY_PICK_K="${NAV_DISCOVERY_PICK_K:-3}"
export NAV_DISCOVERY_SCOPE_BRIDGE="${NAV_DISCOVERY_SCOPE_BRIDGE:-0}"
export MULTIHOP_COMPOSE_HOP_ALIGNMENT="${MULTIHOP_COMPOSE_HOP_ALIGNMENT:-0}"
export MULTIHOP_EVIDENCE_ALLOCATION="${MULTIHOP_EVIDENCE_ALLOCATION:-1}"
export MULTIHOP_EVIDENCE_MIN_CHARS_PER_HOP="${MULTIHOP_EVIDENCE_MIN_CHARS_PER_HOP:-180}"
export NAV_PATH_ANCHOR_TASK_TYPES="${NAV_PATH_ANCHOR_TASK_TYPES:-scope_collection,regulatory_coverage,multi_hop}"
export NAV_SCOPE_COLLECT_RELEVANCE_FIRST="${NAV_SCOPE_COLLECT_RELEVANCE_FIRST:-1}"
export NAV_SCOPE_COLLECT_STRATEGY="${NAV_SCOPE_COLLECT_STRATEGY:-multi_band}"
export NAV_SCOPE_LOCAL_BAND_MIN_POOL="${NAV_SCOPE_LOCAL_BAND_MIN_POOL:-20}"
export NAV_SCOPE_LOCAL_BAND_K="${NAV_SCOPE_LOCAL_BAND_K:-8}"
export NAV_SCOPE_LOCAL_BAND_CONTEXT_BEFORE="${NAV_SCOPE_LOCAL_BAND_CONTEXT_BEFORE:-1}"
export NAV_SCOPE_ACTION_SCORE_CAP="${NAV_SCOPE_ACTION_SCORE_CAP:-1.0}"
export NAV_SCOPE_POST_LOCK_SCORE_PENALTY="${NAV_SCOPE_POST_LOCK_SCORE_PENALTY:-2.0}"
export NAV_BLOCK_EXHAUSTED_SEARCH="${NAV_BLOCK_EXHAUSTED_SEARCH:-1}"
export NAV_FILTER_COLLECTED_SECTIONS="${NAV_FILTER_COLLECTED_SECTIONS:-1}"
export NAV_SYNTHETIC_ROOT_SECTIONS="${NAV_SYNTHETIC_ROOT_SECTIONS:-1}"
export NAV_SYNTHETIC_PREFIX_MIN_LINES="${NAV_SYNTHETIC_PREFIX_MIN_LINES:-2}"
export NAV_HYBRID_DIRECT_SEARCH="${NAV_HYBRID_DIRECT_SEARCH:-auto}"
export NAV_HYBRID_DIRECT_K="${NAV_HYBRID_DIRECT_K:-40}"
export NAV_SCOPE_DIRECT_WINDOW_BEFORE="${NAV_SCOPE_DIRECT_WINDOW_BEFORE:-1}"
export NAV_SCOPE_DIRECT_WINDOW_AFTER="${NAV_SCOPE_DIRECT_WINDOW_AFTER:-1}"

COMMON_ARGS=(
  --test-jsonl "${CORPUS}"
  --tasks "${TASKS}"
  --retrieval dense
  --embedding-model "${EMBEDDING_MODEL}"
  --budget-chars 500
  --hier-policy "${HIER_POLICY:-nav}"
  --nav-config "${NAV_CONFIG:-config/nav_default.json}"
  --nav-policy "${NAV_POLICY:-llm}"
  --inspect-judge
  --inspect-tasks "${INSPECT_TASKS}"
)

if [[ ! -f "${GOLD_OUT}" ]]; then
  export BODYRICH_LLM_API_AUDIT_RUN_ID="${RUN_TAG}_gold"
  export BODYRICH_LLM_API_AUDIT_PATH="${GOLD_ROOT}/llm_call_audit.jsonl"
  /usr/bin/time -p -o "${GOLD_ROOT}/logs/gold.time" \
    env PYTHONPATH=src/realdata:src/nav \
    python3 bin/44_run_pred_only_bodyrich.py \
      "${COMMON_ARGS[@]}" \
      --tree-source gold \
      --out "${GOLD_OUT}" \
      --task-outputs-jsonl "${GOLD_ROOT}/task_outputs_b500.jsonl" \
      --checkpoint-jsonl "${GOLD_ROOT}/gold_b500.checkpoint.jsonl" \
      2>&1 | tee "${GOLD_ROOT}/logs/gold.log"
else
  echo "reuse existing ${GOLD_OUT}"
fi

if [[ ! -f "${PRED_OUT}" ]]; then
  export BODYRICH_LLM_API_AUDIT_RUN_ID="${RUN_TAG}_pred"
  export BODYRICH_LLM_API_AUDIT_PATH="${PRED_ROOT}/llm_call_audit.jsonl"
  /usr/bin/time -p -o "${PRED_ROOT}/logs/pred.time" \
    env PYTHONPATH=src/realdata:src/nav \
    python3 bin/44_run_pred_only_bodyrich.py \
      "${COMMON_ARGS[@]}" \
      --tree-source pred \
      --pred-jsonl "${PRED_JSONL}" \
      --out "${PRED_OUT}" \
      --task-outputs-jsonl "${PRED_ROOT}/task_outputs_b500.jsonl" \
      --checkpoint-jsonl "${PRED_ROOT}/pred_b500.checkpoint.jsonl" \
      2>&1 | tee "${PRED_ROOT}/logs/pred.log"
else
  echo "reuse existing ${PRED_OUT}"
fi

python3 bin/50_summarize_goldpred_reuse.py \
  --gold "${GOLD_OUT}" \
  --pred "${PRED_OUT}" \
  --flat-source "${FLAT_SOURCE}" \
  --treerag "${TREERAG_SOURCE}" \
  --gold-run-root "${GOLD_ROOT}" \
  --pred-run-root "${PRED_ROOT}" \
  --out-json "${SUMMARY_JSON}" \
  --out-md "${SUMMARY_MD}" \
  --protocol "${RUN_TAG}" \
  --bootstrap-samples "${BOOTSTRAP_SAMPLES:-50000}"

python3 -c 'import json,sys; p=json.load(open(sys.argv[1])); q=p["quality"]["overall"]; pred=q["pred"]["score_task"]; gold=q["gold"]["score_task"]; print(f"dev51 gate: pred={pred:.4f} gold={gold:.4f}"); sys.exit(0 if pred>=0.4366 and gold>=0.4835 else 2)' "${SUMMARY_JSON}"
