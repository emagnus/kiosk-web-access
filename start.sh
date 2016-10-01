#!/bin/sh

export DISPLAY=:0

python kiosk_web_server.py >> server.log 2>&1