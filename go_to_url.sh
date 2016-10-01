#!/bin/sh

xdotool key F11
sleep 1
xdotool key ctrl+l
xdotool type "$1"
xdotool key Return
sleep 1
xdotool key F11