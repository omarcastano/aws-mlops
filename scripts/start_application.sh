#!/bin/bash
cd /home/user/ml-app
ls
pwd
python3.10 --version
curl -sSL https://install.python-poetry.org | python3.10
export PATH=$HOME/.local/bin:$PATH
poetry shell
poetry install
poetry run python3.10 /src/app/app.py