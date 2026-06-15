#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

cd "$(dirname "$0")/.."

python3 bin/21_compare_realdata_baselines.py \
  --budgets "${BUDGETS:-500}" \
  --gpf-template "results/latest_clean_quality_balanced60_gold_flat_quality_balanced60_costclean_v1_b{budget}.json" \
  --treerag-template "results/latest_clean_treerag_quality_balanced60_costclean_v1_b{budget}.json" \
  --out-md "cache/compare_run_summary.md"
