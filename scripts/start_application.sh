#!/bin/bash
ls
source /root/.bashrc
cd /home/user/ml-app
poetry shell
poetry install
pwd
ls
poetry run python /src/app/app.py