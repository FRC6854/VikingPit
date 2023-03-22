echo "Installing xdotool and unclutter"

sudo apt install xdotool unclutter

echo "Installing chromium-browser"
sudo apt install chromium-browser

echo "Moving service"

sudo mv /home/pi/VikingDash/vikingdash.service /lib/systemd/system/vikingdash.service

echo "Installing service"

sudo systemctl enable vikingdash.service
sudo systemctl start vikingdash.service

echo "Completed Installation..."
echo "Not working? Try rebooting your pi and checking your preferences with the software guide."