import subprocess
from shutil import copyfile
from time import sleep

def check_joycons():
	joyConL = '7C:BB:8A:93:DA:C8'
	joyConR = '7C:BB:8A:94:37:DB'
	btDevices = subprocess.check_output(['hcitool', 'con'])
	
	if joyConL in btDevices and joyConR in btDevices:
		return True
	else:
		return False
			
while True:
	if check_joycons():
		subprocess.call('sudo /home/pi/joymap/loadmap /home/pi/joymap/joycon.map &', shell=True)
		copyfile('/home/pi/mike/joycons/combine.cfg', '/opt/retropie/configs/all/joystick-selection.cfg')
		copyfile('/home/pi/mike/joycons/combine_retroarch.cfg', '/opt/retropie/configs/all/retroarch.cfg')
		subprocess.call('/home/pi/mike/joycons/spriteview -b 0 -l 50000 -x 0 -y 0 -c 1 -r 1 -i 10 -t 2000 -n /home/pi/mike/joycons/joycon_combined.png &', shell=True)
		break
	else:
		sleep(2)
