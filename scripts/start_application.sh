#!/bin/bash
cd /home/user/ml-app
ls
pwd
curl -sSL https://install.python-poetry.org | python
export PATH=$HOME/.local/bin:$PATH
poetry shell
poetry install
ls
pwd
ls src/app
cd src/app
poetry run uvicorn app:app --host 0.0.0.0 --port 8000