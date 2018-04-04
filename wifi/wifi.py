import subprocess
import os
import re
from time import sleep
from shutil import copyfile

def copyicon(index):
	copyfile('/home/pi/mike/wifi/wifi_'+index+'.png', '/mnt/ramdisk/wifi.png')

while (1):
	
	try:
		wifidetails = subprocess.check_output(['iwconfig', 'wlan0'])
		signal = re.split('Link Quality=',wifidetails)[-1]
		x = int(signal[:2])
		sig = str(x)
		if 0 <= x <= 23:
			#print sig+ ' low signal...'
			copyicon('1')
		elif 23 <= x <= 46:
			#print sig+ ' medium signal...'
			copyicon('2')
		elif 46 <= x:
			#print sig+ ' strong signal ...'
			copyicon('3')
		wifiok = True
		sleep(60)
		
	except ValueError:
		#print 'no wifi signal...'
		copyicon('0')
		sleep(5)	
		