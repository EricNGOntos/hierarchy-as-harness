#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

cd "$(dirname "$0")/.."

PYTHONPATH=src/realdata:src/nav \
python3 src/nav/run_latest_clean_treerag.py --check-only
