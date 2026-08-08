#!/usr/bin/env bash
# Clean400 Flat + TreeRAG under task_corpus (42-doc) search space with text-embedding-v3.
#
# Stages (run separately or all):
#   STAGE=embed    warm Flat flat_chunks + TreeRAG doc indices (tree+embeddings)
#   STAGE=flat     Flat-ReAct retrieval + compose + inspect judge (400 tasks)
#   STAGE=treerag  TreeRAG retrieval + compose + inspect judge (400 tasks)
#   STAGE=all      embed -> flat -> treerag
#
# Examples:
#   STAGE=embed   bash bin/62_run_task_corpus_flat_treerag.sh
#   STAGE=flat    bash bin/62_run_task_corpus_flat_treerag.sh
#   STAGE=treerag bash bin/62_run_task_corpus_flat_treerag.sh
#
# Does NOT reuse legacy bge-m3 baselines; outputs are under a new RUN_TAG.
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1
cd "$(dirname "$0")/.."

STAGE="${STAGE:-all}"
SEARCH_SCOPE="task_corpus"
RUN_TAG="${RUN_TAG:-latest_clean400_${SEARCH_SCOPE}_v3}"
RUN_ROOT="cache/${RUN_TAG}"
LOG_ROOT="${RUN_ROOT}/logs"
FLAT_ROOT="${RUN_ROOT}/flat"
TREERAG_ROOT="${RUN_ROOT}/treerag"
mkdir -p "${LOG_ROOT}" "${FLAT_ROOT}/logs" "${TREERAG_ROOT}/logs"

TASKS="${TASKS:-data/tasks/tasks_realdata_bodyrich_latest_clean_400.jsonl}"
INSPECT_TASKS="${INSPECT_TASKS:-data/tasks/tasks_realdata_bodyrich_latest_clean_400.inspect.jsonl}"
CORPUS="${CORPUS:-data/corpus/test_data_full_realdata_clean_latest.jsonl}"

EMBEDDING_MODEL="${EMBEDDING_MODEL:-text-embedding-v3}"
export BODYRICH_EMBEDDING_BACKEND="${BODYRICH_EMBEDDING_BACKEND:-remote}"
export BODYRICH_EMBEDDING_MODEL="${EMBEDDING_MODEL}"
export EMBEDDING_MODEL="${EMBEDDING_MODEL}"
export BODYRICH_EMBEDDING_CACHE="${BODYRICH_EMBEDDING_CACHE:-1}"
export BODYRICH_EMBEDDING_CACHE_DIR="${BODYRICH_EMBEDDING_CACHE_DIR:-cache/embeddings_remote}"
export BODYRICH_QUERY_EMBEDDING_CACHE="${BODYRICH_QUERY_EMBEDDING_CACHE:-1}"
export BODYRICH_EMBEDDING_BATCH_SIZE="${BODYRICH_EMBEDDING_BATCH_SIZE:-10}"

FLAT_OUT="${FLAT_OUT:-results/${RUN_TAG}_flat_b500.json}"
# NOTE: do not put `{budget}` inside `${var:-...}` — bash treats the first `}` as
# closing the parameter expansion and mangles the template into `{budget.json}`.
if [[ -z "${TREERAG_OUT_TEMPLATE:-}" ]]; then
  TREERAG_OUT_TEMPLATE="results/${RUN_TAG}_treerag_b{budget}.json"
fi
TREERAG_SUMMARY_MD="${TREERAG_SUMMARY_MD:-${TREERAG_ROOT}/run_summary.md}"
TREERAG_CACHE_DIR="${TREERAG_CACHE_DIR:-${TREERAG_ROOT}}"
BUDGET_CHARS="${BUDGET_CHARS:-500}"
MAX_TASKS="${MAX_TASKS:-0}"

if [[ -f src/realdata/agent_delivery/llm_api.env ]]; then
  set -a
  # shellcheck disable=SC1091
  source src/realdata/agent_delivery/llm_api.env
  set +a
fi

# Prefer llm_api.env embedding if present; keep CLI override via EMBEDDING_MODEL.
export BODYRICH_EMBEDDING_MODEL="${BODYRICH_EMBEDDING_MODEL:-$EMBEDDING_MODEL}"
export EMBEDDING_MODEL="${BODYRICH_EMBEDDING_MODEL}"

for path in "${TASKS}" "${INSPECT_TASKS}" "${CORPUS}"; do
  if [[ ! -f "${path}" ]]; then
    echo "missing required file: ${path}" >&2
    exit 1
  fi
done

export BODYRICH_LLM_API_CACHE="${BODYRICH_LLM_API_CACHE:-1}"
export BODYRICH_LLM_API_CACHE_PATH="${BODYRICH_LLM_API_CACHE_PATH:-${RUN_ROOT}/shared_llm_api_cache.jsonl}"

echo "=== Flat/TreeRAG search_scope=${SEARCH_SCOPE} ==="
echo "STAGE=${STAGE}"
echo "RUN_TAG=${RUN_TAG}"
echo "embedding_model=${EMBEDDING_MODEL}"
echo "embedding_backend=${BODYRICH_EMBEDDING_BACKEND}"
echo "embedding_cache_dir=${BODYRICH_EMBEDDING_CACHE_DIR}"
echo "search_scope=${SEARCH_SCOPE}"
echo "tasks=${TASKS}"
echo "max_tasks=${MAX_TASKS}"
echo "treerag_cache_dir=${TREERAG_CACHE_DIR}"

run_embed() {
  echo "[embed] Flat flat_chunks warm-up…"
  /usr/bin/time -p -o "${LOG_ROOT}/embed_flat.time" \
    env PYTHONPATH="src/realdata${PYTHONPATH:+:$PYTHONPATH}" \
    python3 -u bin/62_precompute_task_corpus_flat_embeddings.py \
      --tasks "${TASKS}" \
      --corpus "${CORPUS}" \
      --embedding-model "${EMBEDDING_MODEL}" \
      2>&1 | tee "${LOG_ROOT}/embed_flat.log"

  echo "[embed] TreeRAG doc indices (tree-chunk + embeddings)…"
  local treerag_args=(
    --test-jsonl "${CORPUS}"
    --tasks "${TASKS}"
    --budgets "${BUDGET_CHARS}"
    --out-template "${TREERAG_OUT_TEMPLATE}"
    --summary-md "${TREERAG_SUMMARY_MD}"
    --cache-dir "${TREERAG_CACHE_DIR}"
    --embedding-model "${EMBEDDING_MODEL}"
    --search-scope "${SEARCH_SCOPE}"
    --index-only
  )
  if [[ "${MAX_TASKS}" != "0" ]]; then
    treerag_args+=(--max-tasks "${MAX_TASKS}")
  fi
  /usr/bin/time -p -o "${LOG_ROOT}/embed_treerag.time" \
    env PYTHONPATH="src/realdata:src/nav${PYTHONPATH:+:$PYTHONPATH}" \
    python3 -u src/nav/run_latest_clean_treerag.py \
      "${treerag_args[@]}" \
      2>&1 | tee "${LOG_ROOT}/embed_treerag.log"
}

run_flat() {
  echo "[flat] Flat-ReAct task_corpus eval…"
  export BODYRICH_LLM_API_AUDIT_RUN_ID="${RUN_TAG}_flat"
  export BODYRICH_LLM_API_AUDIT_PATH="${FLAT_ROOT}/llm_call_audit.jsonl"
  local flat_args=(
    --test_jsonl "${CORPUS}"
    --tasks "${TASKS}"
    --out "${FLAT_OUT}"
    --retrieval dense
    --embedding-model "${EMBEDDING_MODEL}"
    --budget-chars "${BUDGET_CHARS}"
    --search-scope "${SEARCH_SCOPE}"
    --arms flat
    --inspect-judge
    --inspect-tasks "${INSPECT_TASKS}"
    --task-outputs-jsonl "${FLAT_ROOT}/task_outputs_b${BUDGET_CHARS}.jsonl"
    --checkpoint-dir "${FLAT_ROOT}/checkpoints"
  )
  if [[ "${MAX_TASKS}" != "0" ]]; then
    flat_args+=(--max-tasks "${MAX_TASKS}")
  fi
  /usr/bin/time -p -o "${FLAT_ROOT}/logs/flat.time" \
    env PYTHONPATH="src/realdata:src/nav${PYTHONPATH:+:$PYTHONPATH}" \
    python3 -u -m agent_delivery.agent.runner_bodyrich \
      "${flat_args[@]}" \
      2>&1 | tee "${FLAT_ROOT}/logs/flat.log"
  echo "[flat] saved ${FLAT_OUT}"
}

run_treerag() {
  echo "[treerag] TreeRAG task_corpus eval…"
  export BODYRICH_LLM_API_AUDIT_RUN_ID="${RUN_TAG}_treerag"
  export BODYRICH_LLM_API_AUDIT_PATH="${TREERAG_ROOT}/llm_call_audit.jsonl"
  local treerag_args=(
    --test-jsonl "${CORPUS}"
    --tasks "${TASKS}"
    --budgets "${BUDGET_CHARS}"
    --out-template "${TREERAG_OUT_TEMPLATE}"
    --summary-md "${TREERAG_SUMMARY_MD}"
    --cache-dir "${TREERAG_CACHE_DIR}"
    --embedding-model "${EMBEDDING_MODEL}"
    --search-scope "${SEARCH_SCOPE}"
    --compose-judge
    --inspect-judge
    --inspect-tasks "${INSPECT_TASKS}"
  )
  if [[ "${MAX_TASKS}" != "0" ]]; then
    treerag_args+=(--max-tasks "${MAX_TASKS}")
  fi
  /usr/bin/time -p -o "${TREERAG_ROOT}/logs/treerag.time" \
    env PYTHONPATH="src/realdata:src/nav${PYTHONPATH:+:$PYTHONPATH}" \
    python3 -u src/nav/run_latest_clean_treerag.py \
      "${treerag_args[@]}" \
      2>&1 | tee "${TREERAG_ROOT}/logs/treerag.log"
  echo "[treerag] saved template ${TREERAG_OUT_TEMPLATE}"
}

case "${STAGE}" in
  embed)
    run_embed
    ;;
  flat)
    run_flat
    ;;
  treerag)
    run_treerag
    ;;
  all)
    run_embed
    run_flat
    run_treerag
    ;;
  *)
    echo "unsupported STAGE=${STAGE}; expected embed|flat|treerag|all" >&2
    exit 1
    ;;
esac

echo "=== done STAGE=${STAGE} RUN_TAG=${RUN_TAG} ==="
