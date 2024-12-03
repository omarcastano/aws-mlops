#!/bin/bash
# Install python3.10
sudo apt update && apt upgrade -y
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.10 python3.10-venv python3.10-dev
python3.10 --version