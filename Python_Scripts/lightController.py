import sys
import serial

red = int(sys.argv[1])

ser = serial.Serial('/dev/ttyACM1',9600)

red3 = red%10
red //= 10
red2 = red%10
red //= 10
red1 = red%10
red //=10

ser.write(str(red1).encode())
ser.write(str(red2).encode())
ser.write(str(red3).encode())
ser.write('s'.encode())
