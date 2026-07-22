#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

cd "$(dirname "$0")/.."

RUN_TAG="${RUN_TAG:-latest_clean400_map_nav_v1}"
RUN_ROOT="cache/${RUN_TAG}"
GOLD_ROOT="${RUN_ROOT}/gold_map"
PRED_ROOT="${RUN_ROOT}/pred_map"
BASE_ROOT="${RUN_ROOT}/gold_baseline_same_embed"
LOG_ROOT="${RUN_ROOT}/logs"
mkdir -p "${GOLD_ROOT}/logs" "${PRED_ROOT}/logs" "${BASE_ROOT}/logs" "${LOG_ROOT}"

TASKS="${TASKS:-data/tasks/tasks_realdata_bodyrich_latest_clean_400.jsonl}"
INSPECT_TASKS="${INSPECT_TASKS:-data/tasks/tasks_realdata_bodyrich_latest_clean_400.inspect.jsonl}"
CORPUS="${CORPUS:-data/corpus/test_data_full_realdata_clean_latest.jsonl}"
PRED_JSONL="${PRED_JSONL:-data/realdata_clean_m1024_best_pred_levels_prevline_fallback.jsonl}"
FLAT_SOURCE="${FLAT_SOURCE:-results/latest_clean400_task_doc_v3_flat_b500.json}"
TREERAG_SOURCE="${TREERAG_SOURCE:-results/latest_clean400_task_doc_v3_treerag_b500.json}"

# Remote embeddings (no local GPU). text-embedding-v3 is available on the configured
# OpenAI-compatible gateway and returns 1024-d vectors. Legacy local bge-m3 caches
# are NOT reused (different embedding space).
EMBEDDING_MODEL="${EMBEDDING_MODEL:-text-embedding-v3}"
export BODYRICH_EMBEDDING_BACKEND="${BODYRICH_EMBEDDING_BACKEND:-remote}"
export BODYRICH_EMBEDDING_MODEL="${EMBEDDING_MODEL}"
export BODYRICH_EMBEDDING_CACHE="${BODYRICH_EMBEDDING_CACHE:-1}"
export BODYRICH_EMBEDDING_CACHE_DIR="${BODYRICH_EMBEDDING_CACHE_DIR:-cache/embeddings_remote}"
export BODYRICH_QUERY_EMBEDDING_CACHE="${BODYRICH_QUERY_EMBEDDING_CACHE:-1}"
export BODYRICH_EMBEDDING_BATCH_SIZE="${BODYRICH_EMBEDDING_BATCH_SIZE:-10}"

GOLD_OUT="results/${RUN_TAG}_gold_map_b500.json"
PRED_OUT="results/${RUN_TAG}_pred_map_b500.json"
BASELINE_GOLD_OUT="${BASELINE_GOLD_OUT:-results/${RUN_TAG}_gold_baseline_same_embed_b500.json}"
# Legacy bge gold is NOT the default baseline anymore (embed mismatch).
LEGACY_BGE_GOLD="${LEGACY_BGE_GOLD:-results/latest_clean400_scope_compact_cap180_v1_gold_b500.json}"
SUMMARY_JSON="results/${RUN_TAG}_summary.json"
SUMMARY_MD="results/${RUN_TAG}_summary.md"

# Rerun a non-map Gold Nav with the SAME embedding model so Map vs Gold is fair.
RERUN_SAME_EMBED_BASELINE="${RERUN_SAME_EMBED_BASELINE:-1}"

for path in "${TASKS}" "${INSPECT_TASKS}" "${CORPUS}" "${PRED_JSONL}" "${FLAT_SOURCE}" "${TREERAG_SOURCE}"; do
  if [[ ! -f "${path}" ]]; then
    echo "missing required file: ${path}" >&2
    exit 1
  fi
done

python3 bin/54_preflight_map_nav.py \
  --embedding-model "${EMBEDDING_MODEL}" \
  --embedding-backend "${BODYRICH_EMBEDDING_BACKEND}"

python3 bin/47_prepare_pred400_cache.py \
  --run-root "${RUN_ROOT}" \
  --shared-cache cache/llm_api_cache.jsonl \
  > "${LOG_ROOT}/cache_prepare.log"

export BODYRICH_LLM_API_CACHE_PATH="${RUN_ROOT}/shared_llm_api_cache.jsonl"
export BODYRICH_LLM_API_CACHE=1

# Map-first nav (core under test)
export NAV_MAP_MODE="${NAV_MAP_MODE:-1}"
export NAV_PEEK_CONTENT_ENABLED="${NAV_PEEK_CONTENT_ENABLED:-0}"
export NAV_MAP_CHILDREN_LIMIT="${NAV_MAP_CHILDREN_LIMIT:-10000}"
export NAV_AUTO_RETURN_ROOT_AFTER_COLLECT="${NAV_AUTO_RETURN_ROOT_AFTER_COLLECT:-conditional}"

# Map scoring (no Discovery soft-signal path)
export NAV_MAP_DENSE="${NAV_MAP_DENSE:-1}"
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
export NAV_FILTER_COLLECTED_SECTIONS="${NAV_FILTER_COLLECTED_SECTIONS:-1}"
export NAV_SYNTHETIC_ROOT_SECTIONS="${NAV_SYNTHETIC_ROOT_SECTIONS:-1}"
export NAV_SYNTHETIC_PREFIX_MIN_LINES="${NAV_SYNTHETIC_PREFIX_MIN_LINES:-2}"
export NAV_SCOPE_OUTLINE_MODE="${NAV_SCOPE_OUTLINE_MODE:-1}"
export BODYRICH_SCOPE_COMPACT_EVIDENCE="${BODYRICH_SCOPE_COMPACT_EVIDENCE:-1}"
export BODYRICH_SCOPE_COMPACT_CHARS_PER_CHUNK="${BODYRICH_SCOPE_COMPACT_CHARS_PER_CHUNK:-180}"

COMMON_ARGS=(
  --test-jsonl "${CORPUS}"
  --tasks "${TASKS}"
  --retrieval dense
  --embedding-model "${EMBEDDING_MODEL}"
  --budget-chars 500
  --hier-policy "${HIER_POLICY:-nav}"
  --nav-config "${NAV_CONFIG:-config/nav_default.json}"
  --nav-policy "${NAV_POLICY:-llm}"
  --search-scope "${SEARCH_SCOPE:-task_doc}"
  --inspect-judge
  --inspect-tasks "${INSPECT_TASKS}"
)

run_arm() {
  local tree_source="$1"
  local out_path="$2"
  local run_dir="$3"
  local audit_id="$4"
  local checkpoint="$5"
  local map_mode="$6"
  local pred_args=()
  if [[ "${tree_source}" == "pred" ]]; then
    pred_args=(--pred-jsonl "${PRED_JSONL}")
  fi
  if [[ -f "${out_path}" ]]; then
    echo "reuse existing ${out_path}"
    return 0
  fi
  export NAV_MAP_MODE="${map_mode}"
  export NAV_MAP_UNIT_CACHE_NS="${tree_source}"
  export BODYRICH_LLM_API_AUDIT_RUN_ID="${audit_id}"
  export BODYRICH_LLM_API_AUDIT_PATH="${run_dir}/llm_call_audit.jsonl"
  /usr/bin/time -p -o "${run_dir}/logs/wall.time" \
    env PYTHONPATH=src/realdata:src/nav \
    python3 bin/44_run_pred_only_bodyrich.py \
      "${COMMON_ARGS[@]}" \
      --tree-source "${tree_source}" \
      "${pred_args[@]}" \
      --out "${out_path}" \
      --task-outputs-jsonl "${run_dir}/task_outputs_b500.jsonl" \
      --checkpoint-jsonl "${checkpoint}" \
      2>&1 | tee "${run_dir}/logs/run.log"
}

# 1) Same-embed non-map Gold baseline (fair Map vs Gold delta)
if [[ "${RERUN_SAME_EMBED_BASELINE}" == "1" ]]; then
  run_arm gold "${BASELINE_GOLD_OUT}" "${BASE_ROOT}" "${RUN_TAG}_gold_baseline" \
    "${BASE_ROOT}/gold_baseline_b500.checkpoint.jsonl" "0"
  BASELINE_GOLD_FOR_SUMMARY="${BASELINE_GOLD_OUT}"
else
  if [[ ! -f "${LEGACY_BGE_GOLD}" ]]; then
    echo "missing legacy baseline gold and RERUN_SAME_EMBED_BASELINE=0" >&2
    exit 1
  fi
  echo "[warn] using legacy baseline gold (likely bge-m3): ${LEGACY_BGE_GOLD}" >&2
  BASELINE_GOLD_FOR_SUMMARY="${LEGACY_BGE_GOLD}"
fi

# 2) Map Gold / Pred
run_arm gold "${GOLD_OUT}" "${GOLD_ROOT}" "${RUN_TAG}_gold_map" \
  "${GOLD_ROOT}/gold_map_b500.checkpoint.jsonl" "1"
run_arm pred "${PRED_OUT}" "${PRED_ROOT}" "${RUN_TAG}_pred_map" \
  "${PRED_ROOT}/pred_map_b500.checkpoint.jsonl" "1"

python3 bin/53_summarize_map_nav.py \
  --map-gold "${GOLD_OUT}" \
  --map-pred "${PRED_OUT}" \
  --baseline-gold "${BASELINE_GOLD_FOR_SUMMARY}" \
  --flat-source "${FLAT_SOURCE}" \
  --treerag "${TREERAG_SOURCE}" \
  --gold-run-root "${GOLD_ROOT}" \
  --pred-run-root "${PRED_ROOT}" \
  --out-json "${SUMMARY_JSON}" \
  --out-md "${SUMMARY_MD}" \
  --protocol "${RUN_TAG}" \
  --bootstrap-samples "${BOOTSTRAP_SAMPLES:-100000}"

echo "embedding_model=${EMBEDDING_MODEL}"
echo "baseline_gold=${BASELINE_GOLD_FOR_SUMMARY}"
echo "summary=${SUMMARY_MD}"
