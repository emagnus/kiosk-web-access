#!/bin/sh

export DISPLAY=:0

# Disable screensaver
xset s off
xset -dpms

python kiosk_web_server.py >> server.log 2>&1