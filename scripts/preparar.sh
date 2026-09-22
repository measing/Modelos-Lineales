#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python -m venv .venv
.venv/bin/python -m pip install --disable-pip-version-check -r requirements.txt
.venv/bin/python -m ipykernel install --user --name modelos-lineales --display-name "Python (Modelos Lineales)"
bash scripts/ejecutar.sh
echo "Preparacion completada. Los informes estan en resultados/."
