import serial
from time import sleep
from requests import post, get
from json import dumps
from random import randint


while True:
    # with serial.Serial("/dev/ttyUSB0", 115200) as ser:
        # line = ser.readline()
        # json_data = dumps(line)
        # post("127.0.0.1", json=json_data)
    
    f1 = randint(0,10)
    get("https://api.thingspeak.com/update?api_key=33MH50NFFKRC2T3Y&field1={}".format(f1))
    sleep(2)