import pygame
import subprocess
import os
from gpiozero import Button
from signal import pause
from time import sleep

def left_click():
	pygame.mixer.init()

	subprocess.call('/home/pi/mike/spriteview -b 0 -l 10001 -n -c 10 -r 1 -i 40 -t 360 -x -10 -y 0 /home/pi/mike/click/click_L.png &', shell=True)
	
	click = pygame.mixer.Sound('/home/pi/mike/click/click.wav')
	click.play()

	sleep(0.6)
	pygame.mixer.quit()
	
def left_remove():
	pygame.mixer.init()

	subprocess.call('/home/pi/mike/spriteview -b 0 -l 10001 -n -c 10 -r 1 -i 30 -t 270 -x -10 -y 0 /home/pi/mike/click/remove_L.png &', shell=True)
	
	click = pygame.mixer.Sound('/home/pi/mike/click/remove.wav')
	click.play()

	sleep(0.6)
	pygame.mixer.quit()
	
def right_click():
	pygame.mixer.init()

	subprocess.call('/home/pi/mike/spriteview -b 0 -l 10001 -n -c 10 -r 1 -i 40 -t 360 -x 770 -y 0 /home/pi/mike/click/click_R.png &', shell=True)
	
	click = pygame.mixer.Sound('/home/pi/mike/click/click.wav')
	click.play()

	sleep(0.6)
	pygame.mixer.quit()
	
def right_remove():
	pygame.mixer.init()

	subprocess.call('/home/pi/mike/spriteview -b 0 -l 10001 -n -c 10 -r 1 -i 30 -t 270 -x 770 -y 0 /home/pi/mike/click/remove_R.png &', shell=True)
	
	click = pygame.mixer.Sound('/home/pi/mike/click/remove.wav')
	click.play()

	sleep(0.6)
	pygame.mixer.quit()
	
leftJoy = Button(25)
leftJoy.when_pressed = left_click
leftJoy.when_released = left_remove

rightJoy = Button(8)
rightJoy.when_pressed = right_click
rightJoy.when_released = right_remove

pause()
