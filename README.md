# Kiosk web access
A small web server to remotely control Chromium via HTTP. Intended to be used in a kiosk scenario where you want the ability to change what is being shown on screen.

## Installation on a fresh RPi 3
1. Install xdotool: `sudo apt-get install xdotool`
2. Configure Chromium to start in fullscreen mode:
    1. Create a file `autstartChromium.desktop` in the directory `~/.config/autostart/`
    2. Copy the following content into the file:
    ```
    [Desktop Entry]
    Type=Application
    Exec=/usr/bin/chromium-browser --noerrdialogs --disable-session-crashed-bubble --disable-infobars --start-fullscreen http://localhost:31337/autostart
    Hidden=false
    X-GNOME-Autostart-enabled=true
    Name[en_US]=AutoChromium
    Name=AutoChromium
    Comment=Start Chromium on reboot
    ```
3. Clone this repo into some directory (let's call it KWA_HOME)
4. Edit crontab (`crontab -e`) and add autostart of the server: 
`@reboot cd KWA_HOME && ./start.sh`
5. Reboot the RPi

## Packaging this as an image

Do the steps above. Then follow [this tutorial](https://www.linuxvoice.com/build-your-own-linux-distro/)
from the step `it’s time to package it into an archive`