# Ejecutar desde cualquier directorio: las rutas se resuelven desde este script.
script_arg <- grep("^--file=", commandArgs(), value = TRUE)
script_path <- normalizePath(sub("^--file=", "", script_arg[[1]]))
root <- dirname(dirname(script_path))
setwd(root)
args <- commandArgs(trailingOnly = TRUE)
formato <- if (length(args)) args[[1]] else "html"
if (!formato %in% c("html", "pdf")) stop("Formato valido: html o pdf")
dir.create("resultados", showWarnings = FALSE)
salida <- if (formato == "pdf") {
  rmarkdown::pdf_document(latex_engine = "xelatex", toc = TRUE, toc_depth = 2)
} else {
  rmarkdown::html_document(toc = TRUE, toc_depth = 2, self_contained = TRUE)
}
rmarkdown::render(
  "modelos de ventas(3).Rmd",
  output_format = salida,
  output_file = paste0("laboratorio_r.", formato),
  output_dir = file.path(root, "resultados"),
  knit_root_dir = root,
  envir = new.env(parent = globalenv()),
  encoding = "UTF-8"
)
message("R completado: resultados/laboratorio_r.", formato)
