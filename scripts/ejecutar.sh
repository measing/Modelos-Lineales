#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
modo="${1:-todo}"
case "$modo" in
  todo|python|r|pdf) ;;
  *) echo "Uso: bash scripts/ejecutar.sh [todo|python|r|pdf]" >&2; exit 2 ;;
esac
mkdir -p resultados
if [[ "$modo" == "todo" || "$modo" == "python" ]]; then
  .venv/bin/python scripts/ejecutar_python.py
fi
if [[ "$modo" == "todo" || "$modo" == "r" ]]; then
  Rscript scripts/ejecutar_r.R html
fi
if [[ "$modo" == "pdf" ]]; then
  Rscript scripts/ejecutar_r.R pdf
fi
