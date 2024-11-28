#!/bin/bash
pyenv install 3.10.12
pyenv global 3.10.12
pip install poetry
poetry shell
poetry install