<p align="center">
<a href="https://github.com/showyourwork/showyourwork">
<img width = "450" src="https://raw.githubusercontent.com/showyourwork/.github/main/images/showyourwork.png" alt="showyourwork"/>
</a>
<br>
<br>
<a href="https://github.com/krosenfeld/syw-module-example/actions/workflows/build.yml">
<img src="https://github.com/krosenfeld/syw-module-example/actions/workflows/build.yml/badge.svg?branch=main" alt="Article status"/>
</a>
<a href="https://github.com/krosenfeld/syw-module-example/raw/main-pdf/arxiv.tar.gz">
<img src="https://img.shields.io/badge/article-tarball-blue.svg?style=flat" alt="Article tarball"/>
</a>
<a href="https://github.com/krosenfeld/syw-module-example/raw/main-pdf/ms.pdf">
<img src="https://img.shields.io/badge/article-pdf-blue.svg?style=flat" alt="Read the article"/>
</a>
</p>

An open source scientific article created using the [showyourwork](https://github.com/showyourwork/showyourwork) workflow.

## Installation

Install mamba environment:
```bash
mamba env create -f environment.yml --prefix ./env
```
Update the environment:
```bash
mamba env update --prefix ./env --file environment.yml  --prune
```
## Build

```bash
showyourwork build --conda-frontend=mamba
```
