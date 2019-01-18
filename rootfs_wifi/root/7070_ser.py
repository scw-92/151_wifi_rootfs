import serial
import os
from time import sleep
if __name__ == '__main__':
    serial = serial.Serial('/dev/ttyUSB0', 9600,timeout = 3600)
    if serial.isOpen() :
        print("open success")
    else :
        print("open failed")
        exit()
    test_cmd = "255.255.255.0"
    while True:
        send_data = input("input a data: ")
        send_data = send_data + '\r\n'
        send_data = "AT+CGCONTRDP" + '\r\n'
        serial.write(send_data.encode())
        data=serial.read(1)
        sleep(0.1)
        data = (data + serial.read(serial.inWaiting())).decode()
        print(data)
        #if test_cmd in data :
         #   print("7020c test ok")
        #break

