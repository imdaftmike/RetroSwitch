#!/usr/bin/env python

import psutil
import subprocess
import re
import os
from shutil import copyfile
from time import sleep

#############################################################################################
# Kills the task of 'procnames'
def killtasks(procnames):
    for proc in psutil.process_iter():
        if proc.name() in procnames:
            pid = str(proc.as_dict(attrs=['pid'])['pid'])
            name = proc.as_dict(attrs=['name'])['name']
            subprocess.call(["sudo", "kill", "-15", pid])

#############################################################################################

subprocess.call('touch /tmp/es-restart', shell=True)
subprocess.call('killall -2 emulationstation', shell=True)
sleep(1)
killtasks('loadmap')
copyfile('/home/pi/mike/joycons/separate.cfg', '/opt/retropie/configs/all/joystick-selection.cfg')
copyfile('/home/pi/mike/joycons/separate_retroarch.cfg', '/opt/retropie/configs/all/retroarch.cfg')

#subprocess.call('/home/pi/mike/joycons/kill_loadmap.py &', shell=True)
