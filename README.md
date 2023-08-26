# VikingDash
A Flask and SQLite powered dashboard to help teams and passers by FRC Information  

VikingDash Dashboard, which should be run in Kiosk mode with a Raspberry Pi or simmilar
![VikingDash Panel](/images/panel.png "VikingDash Panel")
The interactive dashboard which can be controlled through a ethernet connection
![VikingDash Dashboard](/images/dashboard.png "VikingDash Dashboard")

# How to install
[You can check for a official Kiosk guide here](https://www.raspberrypi.com/tutorials/how-to-use-a-raspberry-pi-in-kiosk-mode/)
## Starting Out
Flash your pi with a hostname of `vikingdash.local`, enable ssh with a password of your choosing and a wifi network if provided.

## Updating
SSH into your pi using Ethernet or Wifi (`pi@vikingdash.local`) and use the following commands.
```sh
sudo apt update
sudo apt full-upgrade
```
Then, reboot the pi using `sudo reboot`
## Setting up display
Go into your configuration menu using `sudo raspi-config`, select `System Options (1) > Boot Auto Login (5) > Desktop Autologin (4) > Automatically login as pi user`.
## Cloning the repository
```sh
sudo apt install git
git clone https://github.com/FRC6854/VikingDash
cd VikingDash
```
## Using the software installer
This process requires internet
```sh
sudo chmod 755 install.sh
sudo ./start.sh
```
## Your all done!
Your kiosk should be online, if it does not work immediatly reset your pi.
