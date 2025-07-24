import serial
import time

serialData = ""

SerialPort = serial.Serial('/dev/ttyS10')

while 1:
    serialData = SerialPort.readline()
    print(serialData)
    


    