'''
Program 4) Results Client
 - This program will subscribe to the topic "calculated/#"
 - The program shall print out all recieved data
'''
from mqtt_basic import MqttClient
import json
import sys
sys.path.append('..')


class ResultsClient(MqttClient):

    def __init__(self, ip, port, uid):
        super().__init__(ip, port, uid)
        self.subscribe('/calculated/#')

    def onMessage(self, client, userdata, msg):
        data: dict = json.loads(msg.payload.decode('utf-8'))
        print("First Number = ", data["num1"])
        print("Second Number = ", data["num2"])
        print("Operator = ", data["setup"])
        print("Result = ", data["result"])


if __name__ == "__main__":
    # need to change
    client = ResultsClient("127.0.0.1", 1883, '')
    client.start()
