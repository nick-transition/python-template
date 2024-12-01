# Development Environment Setup

This guide will help you set up your development environment with Python 3.11, Poetry, Commitizen, and PoetryPlugin.

## Prerequisites

- macOS
- [Homebrew](https://brew.sh/) package manager

## Installation Steps

### 1. Install Python 3.11 with pyenv

First, install pyenv if you haven't already:

```
brew install pyenv
```

Full installation instructions can be found [here](https://github.com/pyenv/pyenv/blob/master/README.md).


### 2. Install Commitizen

Install Commitizen using Homebrew:

``` bash
brew install commitizen
```

### 3. Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

or use pipx:

```bash
pipx install poetry
```
Verify the installation:

```bash
poetry --version
```

### 4. Install Poethepoet

```bash
poetry self add poetry-plugin-poethepoet
```


