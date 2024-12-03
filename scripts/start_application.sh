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
sudo systemctl enable python-app
sudo systemctl start python-app
