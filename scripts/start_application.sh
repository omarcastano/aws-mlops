#!/bin/bash
cd /home/omar/ml-app
sudo docker --version
sudo docker compose build
sudo docker compose up -d