#!/bin/bash
curl -sSL https://install.python-poetry.org | python
export PATH=$HOME/.local/bin:$PATH
poetry shell
cd /home/user/ml-app
poetry install
pwd
ls
python /home/user/ml-app/src/app/app.py