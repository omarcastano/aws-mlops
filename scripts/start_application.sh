#!/bin/bash
curl -sSL https://install.python-poetry.org | python
export PATH=$HOME/.local/bin:$PATH
poetry shell
cd cd /home/user/ml-app
poetry install
python /home/user/ml-app/src/app/app.py