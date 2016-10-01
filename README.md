# Kiosk web access
A small web server to remotely control Chromium via HTTP. Intended to be used in a kiosk scenario where you want the ability to change what is being shown on screen.

## Installation on a fresh RPi 3
1. Install xdotool: `sudo apt-get install xdotool`
2. Configure Chromium to start in fullscreen mode
3. Clone this repo into some directory (let's call it KWA_HOME)
4. Edit crontab (`crontab -e`) and add autostart of the server: 
`@reboot cd KWA_HOME && ./start.sh`
5. Reboot the RPi