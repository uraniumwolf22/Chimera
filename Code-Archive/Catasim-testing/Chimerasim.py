import serial
import random
import time
import sys



SerialPort = serial.Serial('/dev/ttyS10')

serialData = ""                                                 # Serial data object is initialized
########################################################
# Variables containing mock system states stored below #
########################################################

dieselLevel = 0

waterLevel = 12

########################################################

def sendCaticoreResponse(Data,Ack):
    Request = "|" + str(Ack) + "|" + Data + "|" + "]"
    Datasz = str(len(Request.split("|")))  #Calculate data size.  split it,  to simulate what it will be on the other side
    Request = Datasz + Request          #append the data size to the request
    return bytearray(Request,"ascii")


def getSerialData():                                            # Gets serial data from port and completes data verification
    while True:
        try:
            SerialPort = serial.Serial('/dev/ttyS10')

            serialData = SerialPort.read_until(b"]")
            break
        except serial.SerialException as e:
            print("Connection error occured.  trying again")
            SerialPort.close()
            time.sleep(1)
            SerialPort.open()


    splitSerialData = serialData.decode().split('|')            # Split data on the delimiter
    calcDataSize = len(splitSerialData)                         # Calculate expected data size,  add 4 to account for delimiters and stop character
    if calcDataSize == int(splitSerialData[0]):                 # Check if data size is correct
        return splitSerialData
    else:
        print("ERROR: Serial data corrupted")
        return




def sendChimeraResponse(serialData):
    match serialData[3]:                                                # Match based on module
        case "0":
            Request = sendCaticoreResponse(serialData[4],int(serialData[1]))   # Send Caticore echo response with ack code from request
            SerialPort.write(Request)



while True:                                                             # Main code loop
    serialData = getSerialData()
    if serialData != 0:
        print("INFO: Sending response")
        sendChimeraResponse(serialData)