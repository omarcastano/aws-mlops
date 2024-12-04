#!/bin/bash
# cd /home/omar/ml-app
# curl -sSL https://install.python-poetry.org | python
# export PATH=$HOME/.local/bin:$PATH
# poetry shell
# poetry install
# sudo systemctl enable python-app
# sudo systemctl start python-app
cd /home/omar/ml-app
sudo docker compose build
sudo docker compose up -d