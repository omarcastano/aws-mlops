#!/bin/bash
cd /home/user/ml-app
ls
pwd
/usr/bin/python3.10 --version
curl -sSL https://install.python-poetry.org | /usr/bin/python3.10
export PATH=$HOME/.local/bin:$PATH
poetry shell
poetry install
poetry run /usr/bin/python3.10 /src/app/app.py