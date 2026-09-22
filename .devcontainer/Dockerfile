FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    r-base r-cran-psych r-cran-ggplot2 r-cran-knitr r-cran-reshape2 \
    r-cran-rmarkdown r-cran-languageserver pandoc \
    texlive-xetex texlive-fonts-recommended texlive-latex-extra \
    texlive-lang-spanish lmodern \
    && rm -rf /var/lib/apt/lists/*

ENV MPLBACKEND=Agg
