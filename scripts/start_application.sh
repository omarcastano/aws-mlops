#!/bin/bash
cd /home/user/ml-app
poetry shell
poetry install
python /home/user/ml-app/src/app/app.py