# Ledshim-boot
This repo contains a simple script that uses a [Pimoroni Ledshim](https://shop.pimoroni.com/products/led-shim) to indicate network connectivity! It is useful for when you are waiting for your Pi to turn on and are waiting so you can SSH in without having to keep trying over and over again. 

## Install
1. Slip the Ledshim on your Pi. 
2. Clone this repo to the Pi and rename it to `ledshim-boot`. It's easiest if you clone it into your home directory of the `Pi` cause the paths in the scripts and service are hardcoded like so. 
3. Copy the [`ledshim-boot.service`](https://github.com/UnsignedArduino/Ledshim-Boot/blob/main/ledshim-boot.service) file to `/etc/systemd/system`. 
4. Reload `systemctl` with `sudo systemctl daemon-reload`
5. Enable the new service with `sudo systemctl enable ledshim-boot.service`
6. Test it out by running `sudo systemctl start ledshim-boot.service`
7. You can check the status of the service to make sure it works by running `systemctl status ledshim-boot.service`. 
