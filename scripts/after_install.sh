#!/bin/bash
set -ex
CD_INSTALL_TARGET=/home/omar/ml-app

echo "copying systemd unit file in place"
sudo cp "${CD_INSTALL_TARGET}/configs/python-app.service" /etc/systemd/system/python-app.service
sudo systemctl daemon-reload
