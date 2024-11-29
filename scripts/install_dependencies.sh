#!/bin/bash
# List the current directory contents for debugging
echo "Current Directory:"
pwd
ls
echo "Current Directory:"
ls ../
cd /home/ubuntu
curl -sSL https://install.python-poetry.org | python
export PATH=$HOME/.local/bin:$PATH
poetry shell
poetry install