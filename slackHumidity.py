#!/usr/bin/python
import sys
import Adafruit_DHT
import json
import requests
import datetime

humidity, temperature = Adafruit_DHT.read_retry(11,4)

tempF = (temperature * 9/5) + 32

output='Temp: {0:0.1f} F, Humidity: {1:0.1f} %'.format(tempF, humidity)

webhook_url="<SLACK_URL>"
slack_msg= { 'text': ":sweat_drops: %s" % (output)}


requests.post(webhook_url, data=json.dumps(slack_msg))

jsonOut = { 'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'output': output }

print json.dumps(jsonOut)

