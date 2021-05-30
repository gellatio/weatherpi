#!/usr/bin/python
from sense_hat import SenseHat
import time
import sys
# from ISStreamer.Streamer import Streamer

sense = SenseHat()
# logger = Streamer(bucket_name="Sense Hat Sensor Data", access_key="API KEY HERE!")
sense.clear()

try:
	while True:

		temp = sense.get_temperature()
		temp = 1.8 * round(temp, 1) + 32
		sense.show_message("Temperature: " + str(temp) + "F")
		# logger.log("Temperature F :",temp)
		
		humidity = sense.get_humidity()
		humidity= round(humidity, 1)
		sense.show_message("Humidity: " + str(humidity))
		# logger.log("Humidity :",humidity)
                
		pressure = sense.get_pressure()
                pressure = round(pressure, 1)
		sense.show_message("Pressure : " + str(pressure))
                # logger.log("Pressure :",pressure)
		
		time.sleep(1)

except KeyboardInterrupt:
	pass
	sense.clear()
