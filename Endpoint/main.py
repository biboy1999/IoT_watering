import serial
from time import sleep
from requests import post, get
from json import dumps
from random import randint

with serial.Serial("/dev/ttyUSB0", 115200) as ser:
    while True:
        line = ser.readline()
        dirt_hum, air_hum, air_temp = line.split(",")
        json_data = {}
        json_data["iot_id"] = 1
        post("140.125.207.192:8000", json=json_data)
        sleep(2)
