import alsaaudio
from gpiozero import Button
from signal import pause
from threading import Timer
import subprocess

usbSpeaker = alsaaudio.Mixer(control='Speaker', id=0, cardindex=1)

bg_applied = False

def bg_overlay():
	global bg_applied
	if bg_applied:
		return
	subprocess.call('killall pngview0', shell=True)
	subprocess.call('/home/pi/mike/volume/pngview0 -b 0 -l 50000 -x 0 -y 0 /home/pi/mike/volume/vol_bg.png &', shell=True)
	t = Timer(3, kill_pngview)
	t.start()
	bg_applied = True
	
def vol_up():
	vol = usbSpeaker.getvolume()
	vol = int(vol[0])
	if vol < 70:
		bg_overlay()
		subprocess.call('killall pngview', shell=True)
		newVol = vol + 10
		usbSpeaker.setvolume(newVol)
		vol = str(newVol)
		subprocess.call('/home/pi/mike/volume/pngview -b 0 -l 50001 -x 0 -y 0 /home/pi/mike/volume/vol_'+vol+'.png &', shell=True)
		
def vol_down():
	vol = usbSpeaker.getvolume()
	vol = int(vol[0])
	if vol > 0:
		bg_overlay()
		subprocess.call('killall pngview', shell=True)
		newVol = vol + -10
		usbSpeaker.setvolume(newVol)
		vol = str(newVol)
		if vol == "0":
			subprocess.call('killall pngview0', shell=True)
			subprocess.call('/home/pi/mike/volume/pngview0 -b 0 -l 50001 -x 0 -y 0 /home/pi/mike/volume/vol_0.png &', shell=True)
			global bg_applied
			bg_applied = False
		else:
			subprocess.call('/home/pi/mike/volume/pngview -b 0 -l 50001 -x 0 -y 0 /home/pi/mike/volume/vol_'+vol+'.png &', shell=True)
		
def kill_pngview():
	subprocess.call('killall pngview', shell=True)
	subprocess.call('killall pngview0', shell=True)
	global bg_applied
	bg_applied = False

	
up_button = Button(24)
down_button = Button(23)

up_button.when_pressed = vol_up
down_button.when_pressed = vol_down

pause()
