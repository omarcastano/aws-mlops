#!/bin/bash
curl -sSL https://install.python-poetry.org | sudo python
echo "export PATH=$HOME/.local/bin:$PATH" >> /root/.bashrc