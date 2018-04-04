#!/usr/bin/env python

import subprocess
import re
import os
from time import sleep
from shutil import copyfile

			
#############################################################################################
# Returns True if the 'proc_name' process name is currently running

def process_exists(proc_name):
    ps = subprocess.Popen("ps ax -o pid= -o args= ", shell=True, stdout=subprocess.PIPE)
    ps_pid = ps.pid
    output = ps.stdout.read()
    ps.stdout.close()
    ps.wait()
    for line in output.split("\n"):
        res = re.findall("(\d+) (.*)", line)
        if res:
            pid = int(res[0][0])
            if proc_name in res[0][1] and pid != os.getpid() and pid != ps_pid:
                return True
    return False
	
#############################################################################################
#

if process_exists('loadmap'):
	copyfile('/home/pi/mike/joycons/combine.cfg', '/opt/retropie/configs/all/joystick-selection.cfg')
else:
	subprocess.call('sudo /home/pi/joymap/loadmap /home/pi/joymap/joycon.map &', shell=True, stdout=open(os.devnull, 'wb'))
	copyfile('/home/pi/mike/joycons/combine.cfg', '/opt/retropie/configs/all/joystick-selection.cfg')

copyfile('/home/pi/mike/joycons/combine_retroarch.cfg', '/opt/retropie/configs/all/retroarch.cfg')
subprocess.call('/home/pi/mike/joycons/spriteview -b 0 -l 50000 -x 0 -y 0 -c 1 -r 1 -i 10 -t 2000 -n /home/pi/mike/joycons/joycon_combined.png &', shell=True)
