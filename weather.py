#!/usr/bin/python
from sense_hat import SenseHat
import time
import sys
from datetime import datetime
# from ISStreamer.Streamer import Streamer

sense = SenseHat()
# logger = Streamer(bucket_name="Sense Hat Sensor Data", access_key="API KEY HERE!")
sense.clear()

try:
	while True:
		now = datetime.now()
		dt = now.strftime("%d/%m/%Y %H:%M:%S")
		temp = sense.get_temperature()
		humidity = sense.get_humidity()
		pressure = sense.get_pressure()
		
		temp = 1.8 * round(temp, 1) + 32
		humidity= round(humidity, 1)
		pressure = round(pressure, 1)
		
		
		print("*** " + dt + " ***")
		print("Temperature: " + str(temp) + "F")
		print("Humidity: " + str(humidity))
		print("Pressure : " + str(pressure))
		
		sense.show_message("Temperature: " + str(temp) + "F")
		# logger.log("Temperature F :",temp)
		sense.show_message("Humidity: " + str(humidity))
		# logger.log("Humidity :",humidity)
		sense.show_message("Pressure : " + str(pressure))
                # logger.log("Pressure :",pressure)
		
		time.sleep(1)

except KeyboardInterrupt:
	pass
	sense.clear()
