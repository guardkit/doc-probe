#!/usr/bin/env bash
# doc-probe's one check command (.guardkit/config.yaml toolchain.test). Exit code = verdict.
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ ! -x .venv/bin/python ]]; then
  python3 -m venv .venv
fi
.venv/bin/python -m pip install -q -e ".[dev]"
exec .venv/bin/python -m pytest -q
