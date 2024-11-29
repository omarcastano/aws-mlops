#!/bin/bash
# List the current directory contents for debugging
cd /home/ubuntu
echo "Current Directory:"
pwd
ls
curl -sSL https://install.python-poetry.org | python
export PATH=$HOME/.local/bin:$PATH
poetry shell
poetry install