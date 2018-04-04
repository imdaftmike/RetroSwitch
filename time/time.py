import datetime
from shutil import copyfile
from time import sleep
from signal import pause

while (1):
	hour = datetime.datetime.now().strftime('%H')
	minute = datetime.datetime.now().strftime('%M')
		
	#hour = int(hour) + 1	# crude BST fix
	if hour == 24:			# make sure 24 displays as 00
		hour = 0
		
	hourtens = str(hour).zfill(2) [0]
	hourunits = str(hour).zfill(2) [1]
			
	mintens = str(minute)[0]
	minunits = str(minute)[1]
	
	copyfile('/home/pi/mike/time/colon.png', '/mnt/ramdisk/colon.png')

	copyfile('/home/pi/mike/time/hour/tens/'+hourtens+'.png', '/mnt/ramdisk/hour_tens.png')
	copyfile('/home/pi/mike/time/hour/units/'+hourunits+'.png', '/mnt/ramdisk/hour_units.png')

	copyfile('/home/pi/mike/time/min/tens/'+mintens+'.png', '/mnt/ramdisk/min_tens.png')
	copyfile('/home/pi/mike/time/min/units/'+minunits+'.png', '/mnt/ramdisk/min_units.png')
	
	sleep(60)
