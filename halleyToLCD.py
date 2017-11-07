import max7219.led as led
import time

device = led.sevensegment(cascaded = 1)
device.brightness(5)

while True:

	with open('my.log', 'r') as f:
		lines = f.read().splitlines()
		last_line = lines[-1]
		combinedNumbers = last_line[:2] + last_line[3:9]
		numberToDisplay = int(combinedNumbers)
	#	print last_line

		device.write_number(deviceId=0, value=numberToDisplay)

		time.sleep(0.01)
