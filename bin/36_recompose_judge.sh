#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

cd "$(dirname "$0")/.."

python3 bin/23_repair_scope_tasks.py
python3 bin/24_repair_multi_hop_tasks.py
PYTHONPATH=src/realdata:src/nav python3 bin/36_recompose_judge.py "$@"
