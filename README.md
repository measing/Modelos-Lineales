# Laboratorio 1: Modelos Lineales

Analisis en R y Python de publicidad y ventas, biomasa y esperanza de vida.
Los tres archivos de datos estan incluidos en este repositorio.

Trabajo de laboratorio 1 de la asignatura de Modelos Lineales.

## Ver el trabajo en la web

**[Abrir la página del laboratorio](https://measing.github.io/Modelos-Lineales/)**

No requiere cuenta ni instalaciones. Incluye pestañas de **Python**, **R** y **Datos**:
códigos, resultados, gráficos, las tres bases completas y descargas del notebook,
documento R Markdown e informe PDF. Los resultados ya están calculados.

Para modificar o ejecutar los análisis, usa Codespaces:

[![Abrir en GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/measing/Modelos-Lineales)

## Abrir y ejecutar en GitHub Codespaces

1. Inicia sesion en GitHub y abre este repositorio.
2. Selecciona **Code → Codespaces → Create codespace on main** (o la rama disponible).
3. Espera a que termine la preparacion inicial. Se instalan los paquetes y se ejecutan ambos analisis automaticamente. La primera apertura puede tardar varios minutos.
4. En la carpeta **resultados/** encontraras:
   - `laboratorio_python.ipynb`: notebook ejecutado, con tablas y graficos.
   - `laboratorio_python.html`: informe de Python.
   - `laboratorio_r.html`: informe de R.

Abre el notebook ejecutado directamente en el editor. Para ver un HTML en tu navegador,
haz clic derecho sobre el archivo, selecciona **Download** y abre la copia descargada.
Los resultados generados se guardan en tu Codespace; no se suben automaticamente a GitHub.
Tambien se ejecutan los analisis en **Actions → Verificar R y Python** con cada cambio.
Cuando una ejecucion termine correctamente, puedes descargar sus informes desde
el artefacto **informes-laboratorio** (incluye el PDF de R).

## Volver a ejecutar

Pulsa **Ctrl+Shift+B** para ejecutar R y Python de nuevo. Tambien puedes usar
**Terminal → Run Task** y elegir solo Python, R o el PDF de R.

Para trabajar celda por celda, abre `laboratorio_1_Modelos_LinealesFinal.ipynb`,
selecciona el kernel **Python (Modelos Lineales)** y pulsa **Run All**.
Para R, abre `modelos de ventas(3).Rmd`. El entorno usa VS Code en el navegador.

Comandos equivalentes, desde la raiz del repositorio:

```bash
bash scripts/ejecutar.sh           # R (HTML) y Python
bash scripts/ejecutar.sh python    # Solo Python
bash scripts/ejecutar.sh r         # Solo R (HTML)
bash scripts/ejecutar.sh pdf       # R (PDF con XeLaTeX)
```

Si la instalacion inicial se interrumpe, consulta el error en el registro de creacion
y vuelve a ejecutar `bash scripts/preparar.sh` en la terminal.

## Archivos de datos

| Archivo | Analisis |
| --- | --- |
| `ventas.txt` | Publicidad y ventas |
| `datos.txt` | Biomasa, pH y potasio |
| `esperanza.txt` | Esperanza de vida |

No es necesario subir datos manualmente. Conserva estos archivos junto al notebook
y al documento R Markdown.

## Entorno

La web se actualiza desde GitHub Actions después de ejecutar correctamente R y Python.
Su código está en `web/`; `scripts/construir_web.py` reúne los informes y los datos
en `_site/` y verifica que estén incluidos los gráficos antes de publicar.

La configuracion de `.devcontainer/` instala Python 3.11, R, Pandoc y XeLaTeX.
Las versiones de las dependencias directas de Python estan en `requirements.txt`;
los paquetes de R proceden de los repositorios de Debian Bookworm.
La imagen base y los paquetes de sistema pueden recibir actualizaciones.

Codespaces requiere una cuenta de GitHub y consume su cuota de computo y almacenamiento.
Deten el Codespace cuando termines. Consulta las condiciones en la
[documentacion de GitHub](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces).
