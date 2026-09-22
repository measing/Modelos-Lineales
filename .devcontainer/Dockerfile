FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

# Yarn no se utiliza en este laboratorio; su repositorio externo puede tener claves vencidas.
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    && apt-get update && apt-get install -y --no-install-recommends \
    r-base r-cran-psych r-cran-ggplot2 r-cran-knitr r-cran-reshape2 \
    r-cran-rmarkdown r-cran-languageserver pandoc \
    texlive-xetex texlive-fonts-recommended texlive-latex-extra \
    texlive-lang-spanish lmodern \
    && rm -rf /var/lib/apt/lists/*
