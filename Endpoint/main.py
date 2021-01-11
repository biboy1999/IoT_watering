import serial
from time import sleep
from requests import post, get
from json import dumps
from random import randint
import schedule

schedule_table = []
ser = serial.Serial("/dev/ttyACM0", 9600)
def water():
    ser.write(b"1")
    pass

if __name__ == "__main__":
    while True:
        try:
            schedule.run_pending()

            line = ser.readline().decode().strip()
            dirt_hum, air_hum, air_temp = line.split(",")
            json_data = {}
            json_data["iot_id"] = 1
            json_data["air_temp"] = air_temp
            json_data["air_hum"] = air_hum
            json_data["dirt_hum"] = dirt_hum
            post("http://140.125.207.192:8000/temp", json=json_data)
            schedule_json = get("http://140.125.207.192:8000/schedule").json()
            parsed_scahedule = schedule_json["water_schedule"].strip().split(";")
            if parsed_scahedule != schedule_table:
                schedule_table = parsed_scahedule
                schedule.clear()
                for time in schedule_table:
                    schedule.every().day.at(time).do(water)
            sleep(1)
        except Exception as ex:
            print(ex)
            pass
