#!/bin/bash
cd /home/omar/ml-app
ls
pwd
curl -sSL https://install.python-poetry.org | python
export PATH=$HOME/.local/bin:$PATH
poetry shell
poetry install
ls
pwd
cd
pwd
ls
sudo systemctl enable python-app
sudo systemctl start python-app