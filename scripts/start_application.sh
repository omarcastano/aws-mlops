#!/bin/bash
cd /home/user/ml-app
curl -sSL https://install.python-poetry.org | sudo python
echo "export PATH=$HOME/.local/bin:$PATH" >> /root/.bashrc
poetry shell
poetry install
poetry run python /src/app/app.py