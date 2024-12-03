#!/bin/bash
cd /home/user/ml-app
ls
pwd
python --version
curl -sSL https://install.python-poetry.org | python
export PATH=$HOME/.local/bin:$PATH
poetry shell
poetry install
poetry run python /src/app/app.py