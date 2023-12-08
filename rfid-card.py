import serial
def read_rfid():
ser = serial .Serial ("/dev/ttyUSB0")
ser.baudrate = 9600
data= ser.rfid(16)
ser.close()
return data
print(“place the card”)
id= read_rfid()
print("Welcome Sanjay")
print(id)
