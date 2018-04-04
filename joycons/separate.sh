#!/bin/bash

sudo pkill loadmap
cp /home/pi/mike/joycons/separate.cfg /opt/retropie/configs/all/joystick-selection.cfg
cp /home/pi/mike/joycons/separate_retroarch.cfg /opt/retropie/configs/all/retroarch.cfg
