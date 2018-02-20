#!/usr/bin/python
import sys
from time import sleep
import Adafruit_DHT
import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=11, cols=16, lines=2)
lcd.clear()

try:
	while True:
		humidity, temperature = Adafruit_DHT.read_retry(11,4)
		tempF = (temperature * 9/5) + 32
		output = 'Temp: {0:0.1f} F\nHumidity: {1:0.1f} %'.format(tempF, humidity)
		lcd.clear()	
		lcd.message(output)
		sleep(1)
finally:
	lcd.clear()



