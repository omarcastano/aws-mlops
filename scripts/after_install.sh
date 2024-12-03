#!/bin/bash
set -ex
APP_USER=omar
APP_GROUP=omar
DATESTAMP="$(date +%F)"
CD_INSTALL_TARGET=/home/omar/ml-app

function systemd_unit_file_check() {
  echo "copying systemd unit file in place"
  sudo cp "${CD_INSTALL_TARGET}/configs/python-app.service" /etc/systemd/system/python-app.service
  sudo systemctl daemon-reload
}

systemd_unit_file_check