import sys
sys.path.append('..')

import json
from random import random
from datetime import datetime
from mqtt_basic import MqttClient
from RepeatingTimer import RepeatingTimer

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class CalculationClient(MqttClient):

	def __init__(self, ip, port, uid):
		super().__init__(ip, port, uid)
		self.pubTopic = '/calculation/setup'

	def publishCalculation(self):
		operation = input("Would you like to perform addition or subtraction? (Enter '-' or '+')")
		while True:
			info= {
			'setup' : operation
		}
		self.publish(self.pubTopic, json.dumps(info).encode('utf-8'))
		print('published random numbers')
		print(info)
		
if __name__ == "__main__":

	client = RandomNumberClient("127.0.0.1",1883,'')

	client.start()