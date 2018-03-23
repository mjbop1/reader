#!/bin/sh
# reader.sh
# navigate to home directory, then to this directory, then execute python script, then back home
sleep 10
cd /
cd home/pi/reader
sudo python3 reader.py
cd /home/pi
