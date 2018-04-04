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

sleep(1)
killtasks('loadmap')
