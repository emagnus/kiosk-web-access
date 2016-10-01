#!/bin/sh

xdotool key F11
sleep 0.2
xdotool key ctrl+l
xdotool type "$1"
sleep 0.2
xdotool key Return
xdotool key F11