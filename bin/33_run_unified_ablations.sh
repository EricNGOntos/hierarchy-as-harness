#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

cd "$(dirname "$0")/.."

echo "[ablation] full unified_v3 (Phase2 nav + compose)"
NAV_RUN_TAG=fair_clean_unified_v3 bash bin/32_run_quality_balanced_gold_flat.sh

echo "[ablation] no discovery (NAV_DISCOVERY_SOFT_SIGNAL=0)"
NAV_DISCOVERY_SOFT_SIGNAL=0 NAV_RUN_TAG=fair_clean_ablation_no_discovery bash bin/32_run_quality_balanced_gold_flat.sh

echo "[ablation] no agent state (NAV_AGENT_STATE=0)"
NAV_AGENT_STATE=0 NAV_RUN_TAG=fair_clean_ablation_no_agent_state bash bin/32_run_quality_balanced_gold_flat.sh

python3 bin/21_compare_realdata_baselines.py \
  --budgets "${BUDGETS:-500}" \
  --gpf-template "results/fair_clean_gold_flat_fair_clean_unified_v3_b{budget}.json" \
  --treerag-template "results/fair_clean_treerag_fair_clean_unified_v2_b{budget}.json" \
  --treerag-wrapper-template "results/fair_clean_treerag_fair_clean_unified_v2_b{budget}.json" \
  --out-md "cache/compare_fair_clean_unified_v3.md"

echo "[ablation] wrote cache/compare_fair_clean_unified_v3.md"
