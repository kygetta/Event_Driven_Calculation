'''
Program 1) Random Number Generator -> already done for you and attached.
 - publishes 2 random numbers every 1 second on the topic "/random_numbers"
 - example message -> {"type":"random_number", "num1":12.323, "num2":34.232, "timestamp":"some timestamp"}
'''
import sys
sys.path.append('..')

import json
from random import random
from datetime import datetime
from mqtt_basic import MqttClient
from RepeatingTimer import RepeatingTimer

class RandomNumberClient(MqttClient):

	def __init__(self, ip, port, uid):
		super().__init__(ip, port, uid)
		self.pubTopic = '/random_numbers'

	def publishRandomNumber(self):
		num1 = random() * 100
		num2 = random() *  100

		data = {
			'num1' : num1,
			'num2' : num2,
			'timestamp' : datetime.now().strftime("%H:%M:%S") 
		}
		self.publish(self.pubTopic, json.dumps(data).encode('utf-8'))
		print('published random numbers')
		print(data)
		
if __name__ == "__main__":

	client = RandomNumberClient("127.0.0.1",1883,'')
	
	timer = RepeatingTimer(1.0, client.publishRandomNumber)

	client.start()
	timer.start()
	