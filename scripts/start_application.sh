#!/bin/bash
cd /home/user/ml-app
export PATH=$HOME/.local/bin:$PATH
poetry shell
poetry install
python /src/app/app.py