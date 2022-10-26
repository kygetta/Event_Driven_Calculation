'''
Program 2) Calculation Setup
 - This program will ask for user input as to whether they want to the system to perform addition or subtraction
 - Ask the user to input either a "+" for addition or a "-" for subtraction
 - Once the user input is received, the program will publish the selection over the topic "/calculation/setup"
 - This format can be in any format you wish to use
 - The program should continue asking the user for input as it should be able to change at any point in time
 - example message -> {"type":"setup", "setup":"+"} or {"type":"setup", "setup":"-"} 
'''
from random_num_client import RandomNumberClient
from mqtt_basic import MqttClient
from random import random
import json
import sys
sys.path.append('..')


class CalculationSetupClient(MqttClient):

    def __init__(self, ip, port, uid):
        super().__init__(ip, port, uid)
        self.pubTopic = '/calculation/setup'

    def publishCalculation(self, operation):
        
        info = {
            'type': 'setup',
            'setup': operation

        }

        self.publish(self.pubTopic, json.dumps(info).encode('utf-8'))
        print('published random numbers')
        print(info)
        
        


if __name__ == "__main__":
    # need to change
    client = CalculationSetupClient("127.0.0.1", 1883, '')

    client.start()
    
    while True:
      operation = input(
            "Would you like to perform addition or subtraction? (Enter '-' or '+' or 'exit' to exit)")
      if(operation == '+' || operation == '-'):
        client.publishCalculation(operation)
      elif(operation == 'exit'):
        break
      else: 
        print("Invalid inuput")

