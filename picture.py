from datetime import datetime
from picamera import PiCamera
from time import sleep 
from gpiozero import MotionSensor

pir = MotionSensor(4)
camera = PiCamera()
teller = 0
toggel = True
while True:
	if pir.motion_detected:
		if toggel:
			dt_string = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
			camera.start_recording('/mnt/USBdrive/movie%s.h264' %dt_string)
			toggel = False 
			print("recording started")
	if pir.motion_detected == False:
		if toggel == False: 
			camera.stop_recording()
			teller = 0 
			toggel = True
	if toggel == False :

		sleep(1)
		teller = teller +1
		print(teller)
		if teller >= 300:
			camera.stop_recording()
			print("recording stopped")
			teller = 0
			toggel = True

