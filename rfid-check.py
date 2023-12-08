import time
import serial
data = serial.Serial(port='/dev/ttyUSB0',
baudrate=9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS)
print("")
try:
while True:
print("Place the card")
x = data.read(12)
print(x)
if x == "1E00CBDE718":
print("Card no –", x)

print("Welcome TYBSCIT")
print(" ")
else:
print("Wrong card....... ")
print(" ")
except KeyboardInterrupt:
data.close()
