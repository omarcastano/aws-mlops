#!/bin/bash
cd /home/user3/ml-app
curl -sSL https://install.python-poetry.org | python
export PATH=$HOME/.local/bin:$PATH
poetry shell
poetry install