import serial
import time
import argparse
import random

ackCode = 0
requestType = 0
moduleCode = 0
data = ""

parser = argparse.ArgumentParser(description="Chimera control command line utility")

parser.add_argument("-echo",type=str,help="Requests chimera to echo input")

args = parser.parse_args()

SerialPort = serial.Serial('/dev/ttyS10')

def sendChimeraRequest(reqType,Module,Data):
    Ack = random.randint(1,1000)
    Request = "|" + str(Ack) + "|" + str(reqType) + "|" + str(Module) + "|" + Data + "|" + "]"
    Datasz = str(len(Request.split("|")))           #Calculate data size.  split it,  to simulate what it will be on the other side
    Request = Datasz + Request                      # Append the data size to the request

    SerialPort.write(bytearray(Request,"ascii"))    # Write request to Chimera
    SerialPort.flush()

    serialData = SerialPort.read_until(b"]")        # Wait for response
    serialData = serialData.decode().split("|")
    if serialData[1] == str(Ack):
        return serialData
    else:
        print("ERROR: Ack incorrect")
        return




if args.echo:
    print(sendChimeraRequest(0,0,args.echo))