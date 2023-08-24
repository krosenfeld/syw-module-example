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

This example shows how to incorporate a project specific python module (called `module`). The basic steps are:

1. Create a pyproject.toml or setup.py (here I use `pyproject.toml`` with a requirements.txt file)
2. Add your module with the appropriate `__init__.py ` files. 
3. Add the pip VCS install to the `environment.yml` file. E.g.:
```
git+https://github.com/krosenfeld/syw-module-example.git#egg=module
```

For a private repository follow the steps to enable the [ssh-agent action](https://github.com/webfactory/ssh-agent):

1. Generate a new SSH key with sufficient access privileges. For security reasons, don't use your personal SSH key but set up a dedicated one for use in GitHub Actions. See below for a few hints if you are unsure about this step.
2. Make sure you don't have a passphrase set on the private key.
3. Add the public SSH key to the private repository you are pulling from during the Github Action as a 'Deploy Key'.
4. Add the private SSH key to the repository triggering the Github Action: 
    * In your repository, go to the *Settings > Secrets* menu and create a new secret.  Call it `SSH_PRIVATE_KEY`. 
    * Put the contents of the *private* SSH key file into the contents field. <br>
    * This key should start with `-----BEGIN ... PRIVATE KEY-----`, consist of many lines and ends with `-----END ... PRIVATE KEY-----`. 
5. Make sure that the pip VCS install  in `environment.yml` uses `git+ssh`. E.g.:
```
git+ssh://git@github.com/krosenf/syw-module-example.git#egg=module
```

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
