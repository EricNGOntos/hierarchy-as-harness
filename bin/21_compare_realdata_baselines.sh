#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

cd "$(dirname "$0")/.."

python3 bin/21_compare_realdata_baselines.py \
  --budgets "${BUDGETS:-500}" \
  --gpf-template "results/fair_clean_gold_flat_fair_clean_unified_v1_b{budget}.json" \
  --treerag-template "results/fair_clean_treerag_fair_clean_unified_v2_b{budget}.json" \
  --treerag-wrapper-template "results/fair_clean_treerag_fair_clean_unified_v2_b{budget}.json" \
  --out-md "cache/compare_fair_clean_final.md"
