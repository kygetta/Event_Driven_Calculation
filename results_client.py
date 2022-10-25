import sys
sys.path.append('..')

import json
from mqtt_basic import MqttClient

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class ResultsClient(MqttClient):

	def __init__(self, ip, port, uid):
		super().__init__(ip, port, uid)
		self.subscribe('/calculated/#')

		print("First Number = ",data["num1"])
		print("Second Number = ",data["num2"])
		print("Operator = ",info["setup"])
		print("Result = ",calcinfo["result"])
				
if __name__ == "__main__":

	client = ResultsClient("127.0.0.1",1883,'')
	client.start()
	