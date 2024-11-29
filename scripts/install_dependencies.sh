#!/bin/bash
# List the current directory contents for debugging
echo "Current Directory:"
pwd
ls
cd aws-mlops
curl -sSL https://install.python-poetry.org | python
export PATH=$HOME/.local/bin:$PATH
poetry shell
poetry install