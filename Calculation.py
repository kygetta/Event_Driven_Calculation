import sys
sys.path.append('..')

import json
from random import random
from datetime import datetime
from mqtt_basic import MqttClient
from RepeatingTimer import RepeatingTimer

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class Calculate(MqttClient):

	def __init__(self, ip, port, uid):
		super().__init__(ip, port, uid)
		self.subscribe('/random_numbers')
		self.subscribe('/calculation/setup')
		if(info['setup']) = '+':
			self.pubTopic = '/calculated/add'
		elif(info['setup']) = '-':
			self.pubTopic = '/calculated/subtract'

	def PublishCalculation(self):
		if(info['setup']) = '+':
			result = (data['num1']) + (data['num2'])
		elif(info['setup']) = '-':
			result = (data['num1']) - (data['num2'])

		calcinfo= {
			'setup' : operation,
			'result': result
		}
		self.publish(self.pubTopic, json.dumps(calcinfo).encode('utf-8'))
		print(calcinfo)

if __name__ == "__main__":

	client = RandomNumberClient("127.0.0.1",1883,'')
	client.start()