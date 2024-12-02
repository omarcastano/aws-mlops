#!/bin/bash
export PATH=$HOME/.local/bin:$PATH
poetry shell
poetry install
python /home/user/ml-app/src/app/app.py