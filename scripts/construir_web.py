"""Publica exclusivamente informes verificados, código y datos del laboratorio."""
import json
from pathlib import Path
import shutil

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer, SLexer

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"
OUT.mkdir(exist_ok=True)
for name in ("reports", "downloads"):
    (OUT / name).mkdir(exist_ok=True)
for name in ("index.html", "style.css", "app.js"):
    shutil.copy2(ROOT / "web" / name, OUT / name)
(OUT / ".nojekyll").touch()

for language, source in (("python", "laboratorio_python.html"), ("r", "laboratorio_r.html")):
    report = (ROOT / "resultados" / source).read_text(encoding="utf-8")
    expected = 16 if language == "r" else 10
    count = report.count("data:image/png;base64,")
    if count < expected:
        raise ValueError(f"Faltan gráficos de {language}: {count}, se esperaban al menos {expected}")
    (OUT / "reports" / f"{language}.html").write_text(report, encoding="utf-8")

notebook = json.loads((ROOT / "resultados" / "laboratorio_python.ipynb").read_text(encoding="utf-8"))
if any(output.get("output_type") == "error" for cell in notebook["cells"] for output in cell.get("outputs", [])):
    raise ValueError("El notebook contiene errores de ejecución")
python_code = "\n\n".join("".join(cell["source"]) for cell in notebook["cells"] if cell["cell_type"] == "code")
r_lines, in_chunk = [], False
for line in (ROOT / "modelos de ventas(3).Rmd").read_text(encoding="utf-8").splitlines():
    if line.startswith("```{r"):
        in_chunk = True
    elif in_chunk and line.startswith("```"):
        in_chunk = False
        r_lines.append("")
    elif in_chunk or line.startswith("#"):
        r_lines.append(line)

formatter = HtmlFormatter(cssclass="code")
for language, code, lexer in (("python", python_code, PythonLexer()), ("r", "\n".join(r_lines), SLexer())):
    title = "Python" if language == "python" else "R"
    content = highlight(code, lexer, formatter)
    page = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Código {title}</title><style>
    body{{margin:0;padding:24px;color:#17253c;background:white;font:16px system-ui}}h1{{font-size:22px}}pre{{font:14px/1.7 ui-monospace,Consolas,monospace;white-space:pre;overflow-x:auto;padding:20px;background:#f7f9fc;border-radius:8px}}{formatter.get_style_defs('.code')}
    </style></head><body><h1>Código {title}</h1>{content}</body></html>'''
    (OUT / "reports" / f"{language}-code.html").write_text(page, encoding="utf-8")

datasets = {}
for key, title in (("ventas", "Publicidad y ventas"), ("datos", "Biomasa"), ("esperanza", "Esperanza de vida")):
    path = ROOT / f"{key}.txt"
    lines = [line.split() for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    columns, rows = lines[0], lines[1:]
    if not all(len(row) == len(columns) for row in rows):
        raise ValueError(f"Número de columnas inconsistente en {path.name}")
    datasets[key] = {"title": title, "columns": columns, "rows": rows}
    shutil.copy2(path, OUT / "downloads" / path.name)
(OUT / "data.js").write_text("window.LAB_DATA = " + json.dumps(datasets, ensure_ascii=False) + ";\n", encoding="utf-8")
for source, target in ((ROOT / "resultados/laboratorio_python.ipynb", "laboratorio_python.ipynb"), (ROOT / "modelos de ventas(3).Rmd", "laboratorio.Rmd"), (ROOT / "resultados/laboratorio_r.pdf", "laboratorio_r.pdf")):
    shutil.copy2(source, OUT / "downloads" / target)
print("Web preparada en _site/: Python, R y tres bases de datos. Gráficos verificados.")
