'''
Program 3) Calculation 
 - This program will receive data on the topics "/random_numbers" and "/calculation/setup"
 - The program will use the input from "Calculation Setup" to tell it whether to perform addition("+") or subtraction("-")
 - The program will use the random number data to calculate either the addition or subtraction of "num1" and "num2"
 - Once the calcualtion is complete, the program will publish the result on topic "/calculated/add" for "+" or "/calculated/subtract" for "-"
 - example message {"type":"calculation","setup":"+","result":43.3453}
'''

from mqtt_basic import MqttClient
from random import random
import json
import sys

from random_num_client import RandomNumberClient
sys.path.append('..')


class Calculate(MqttClient):

    def __init__(self, ip, port, uid):
        super().__init__(ip, port, uid)
        self.subscribe('/random_numbers')
        self.subscribe('/calculation/setup')
        self.pubTopic = ''  # we decide what topic to publish to when we receive a message
        self.calcDict: dict[str, str] = {}

    def on_message(self, client, userdata, msg):
        data: dict = json.loads(msg.payload.decode('utf-8'))
        # if we receive message with random numbers, save them in calcDict as num1 and num2
        if (data['type'] == 'random_number'):
            self.calcDict['num1'] = data['num1']
            self.calcDict['num2'] = data['num2']
        # else if we receive message with setup, save it in calcDict as the operator
        elif (data['type'] == 'setup'):
            self.calcDict['setup'] = data['setup']

        # if we have both numbers and the operator, send the calculation to publishCalculation
        if (self.calcDict['num1'] != None and self.calcDict['num2'] != None and self.calcDict['setup'] != None):
            self.publishCalculation(self.calcDict)

    def publishCalculation(self, calcDict):
        result: int = 0
        if (calcDict['setup']) == '+':
            result = (calcDict['num1']) + (calcDict['num2'])
        elif (calcDict['setup']) == '-':
            result = (calcDict['num1']) - (calcDict['num2'])

        calcInfo = {
            'setup': calcDict['operation'],
            'result': result
        }

        self.publish(self.pubTopic, json.dumps(calcInfo).encode('utf-8'))
        # print(calcinfo) for debugging


if __name__ == "__main__":
    # need to change

    client = RandomNumberClient("127.0.0.1", 1883, '')
    client.start()
