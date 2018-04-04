import serial
import subprocess
from time import sleep
from gpiozero import Button, LED
from shutil import copyfile
import threading


#############################################################################################
# Setup the serial port

ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=None)
ser.write("wakeup")

#############################################################################################
# Send a serial message to the Arduino periodically to wake it from sleep

def wakearduino():
	ser.write("wakeup")
	threading.Timer(90, wakearduino).start()

# start calling arduino now and every 90 sec afterwards
wakearduino()


#############################################################################################
# Safely shut-down the Raspberry Pi

def shutdown():
    print "shutdown...\n"
    subprocess.call("/home/pi/mike/pngview -l -99 -b 0 -n /home/pi/mike/switch_shutdown.png &", shell=True)
    subprocess.call("sudo shutdown -h now", shell=True)


#############################################################################################
# Set BCM 4 HIGH... the arduino reads this to determine if the Raspberry Pi is running

led = LED(4)
led.on()

# If we do a manual shutdown from within ES then our program will be stopped and the pin
# will return to a LOW state via an external pull-down, the arduino can read this and cut
# the power when appropriate.


#############################################################################################
# Main Loop
lowbatt = 0
while (1):
	try:
		line = ser.readline()
		if line != "":
			arduino = line[:-1].split(', ')		# incoming data looks like: "$$$, $$$, $$$, \n"
			message = arduino[0]  				# 'message' is a message from the arduino to do something
			voltage = arduino[1]  				# 'voltage' is the cell voltage x.xxx in Volts
			percentage = arduino[2]  			# 'percentage' is a the cell 'state-of-charge' % remaining
			
		if message != "shutdown":					# normally the message field is empty
			voltage = voltage.rstrip()				# remove unwanted characters
			percentage = str(percentage).zfill(6)	# pad the values so we have a leading zero if needed
			
			#print voltage+"V"
			#print percentage+"%"

			hunds = percentage[0]		# take the first character of 'percentage'
			tens = percentage[1]		# take the second character of 'percentage'
			units = percentage[2]		# take the third character of 'percentage'
			
			# copy the relevent .png to the theme folder in order to have them display on the 'homescreen'
			copyfile('/home/pi/mike/power/hunds/bat_'+hunds+'.png', '/mnt/ramdisk/bat_hunds.png')
			copyfile('/home/pi/mike/power/tens/bat_'+tens+'.png', '/mnt/ramdisk/bat_0.png')
			copyfile('/home/pi/mike/power/units/bat_'+units+'.png', '/mnt/ramdisk/bat_1.png')

			x = float(percentage)		# convert percentage to a float for the below comparison
			
			# copy the battery icon .pngs according to the charge state (full/medium/empty etc.)
			
			if 0 <= x <= 25:
				copyfile('/home/pi/mike/power/bat_25.png', '/mnt/ramdisk/bat.png')
			elif 25 <= x <= 50:
				copyfile('/home/pi/mike/power/bat_50.png', '/mnt/ramdisk/bat.png')
			elif 50 <= x <= 75:
				copyfile('/home/pi/mike/power/bat_75.png', '/mnt/ramdisk/bat.png')
			elif 75 <= x:
				copyfile('/home/pi/mike/power/bat_100.png', '/mnt/ramdisk/bat.png')				

	except IndexError:
		print "Serial read error...\n"		# an index error here means the serial data was corrupt

#############################################################################################
# Check serial data for a shutdown message
	if message == "shutdown":
		print "shutdown command received..."
		shutdown()

##############################################################################################
# Display Low Battery Alert when percentage goes below 15%
	if x < 15 and lowbatt == 0:
		subprocess.call("/home/pi/mike/power/spriteview -b 0 -c 2 -l 99999 -i 750 -n -r 1 -t 7500 -x 0 -y 0 /home/pi/mike/power/low_bat.png &", shell=True)
		lowbatt = 0

# having the 'lowbatt' check would make the warning only come up once, but actually it's quite
# useful for the warning to display everytime we check the battery level in case you miss it
# (maybe having a persistant on-screen low battery warning would be worth adding?)
##############################################################################################
# Shutdown the system when percentage goes below 6%
	if x < 6:
		shutdown()
		
##############################################################################################