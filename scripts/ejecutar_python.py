"""Ejecuta el notebook desde cero y guarda una copia con resultados y un HTML."""
from pathlib import Path

import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "resultados"
OUTPUT.mkdir(exist_ok=True)
notebook = nbformat.read(ROOT / "laboratorio_1_Modelos_LinealesFinal.ipynb", as_version=4)
runner = ExecutePreprocessor(timeout=600, kernel_name="python3", allow_errors=False)
runner.preprocess(notebook, {"metadata": {"path": str(ROOT)}})
nbformat.write(notebook, OUTPUT / "laboratorio_python.ipynb")
html, _ = HTMLExporter().from_notebook_node(notebook)
(OUTPUT / "laboratorio_python.html").write_text(html, encoding="utf-8")
print("Python completado: resultados/laboratorio_python.html")
