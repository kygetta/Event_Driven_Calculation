from RepeatingTimer import RepeatingTimer
from mqtt_basic import MqttClient
from datetime import datetime
from random import random
import json
import sys
sys.path.append('..')


class Calculate(MqttClient):

    def __init__(self, ip, port, uid):
        super().__init__(ip, port, uid)
        self.subscribe('/random_numbers')
        self.subscribe('/calculation/setup')
        self.pubTopic = ''

        def on_message(self, client, userdata, msg):
            data: dict = json.loads(msg.payload.decode('utf-8'))
            if (data['setup']) == '+':
                self.pubTopic = '/calculated/add'
            elif (data['setup']) == '-':
                self.pubTopic = '/calculated/subtract'
            else:
                print('Invalid input')#if the user enters anything other than '+' or '-'
                exit(0)#exit the program
            return data

    def PublishCalculation(self):
        if (info['setup']) == '+':
            result == (data['num1']) + (data['num2'])
        elif (info['setup']) == '-':
            result == (data['num1']) - (data['num2'])

        calcinfo = {
            'setup': operation,
            'result': result
        }
        self.publish(self.pubTopic, json.dumps(calcinfo).encode('utf-8'))
        print(calcinfo)


if __name__ == "__main__":

    client = RandomNumberClient("127.0.0.1", 1883, '')
    client.start()
