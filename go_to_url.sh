#!/bin/sh

xdotool key f11
xdotool key ctrl+l
xdotool type "$1"
xdotool key Return
xdotool key f11