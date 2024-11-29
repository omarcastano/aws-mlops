#!/bin/bash
# List the current directory contents for debugging
echo "Current Directory:"
pwd
ls
sudo mkdir -p /home/ec2-user/ml-project
cd /home/ec2-user/ml-project/
echo "Current Directory:"
pwd
ls
curl -sSL https://install.python-poetry.org | python
export PATH=$HOME/.local/bin:$PATH
poetry shell
poetry install