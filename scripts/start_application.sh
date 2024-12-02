#!/bin/bash
curl -sSL https://install.python-poetry.org | python
export PATH=$HOME/.local/bin:$PATH
poetry shell
poetry install /home/user/ml-app/pyproject.toml
python /home/user/ml-app/src/app/app.py