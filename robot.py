import os
import serial
import time

def setAngle(number, angle):                    #sets the servo to a RELATIVE angle
    f = serial.Serial("/dev/ttyUSB0",115200)    #opening the serial port and setting baudrate
    f.write(f"#{number}MD{angle}\r".encode())   #writing to the file
    f.close()


def posInDegrees(number, angle):                #sets the servo to an ABSOLUTE angle
    f = serial.Serial("/dev/ttyUSB0", 115200)
    f.write(f"#{number}D{angle}\r".encode())
    f.close()


def wheelModeDegrees(number, angle):            #sets servo to wheel mode where it rotates in that direction (nonstop)
    f = serial.Serial("/dev/ttyUSB0", 115200)
    f.write(f"#{number}WD{angle}\r".encode())
    f.close()

def halt(number):                               #causes servo to stop immediately and hold that angular position
    f = serial.Serial("/dev/ttyUSB0", 115200)
    f.write(f"#{number}H\r".encode())
    f.close()

def firstPos(number):                           #used to have the servo move to a specific angle upon power up
    f = serial.Serial("/dev/ttyUSB0", 115200)
    f.write(f"#{number}CFD\r".encode())
    f.close()

for x in range(6):                              #makes all servos go limp when turning on
    firstPos(x)

#Reset command
def reset(number):                              #use to reset individual servos
    f = serial.Serial("/dev/ttyUSB0", 115200)
    f.write(f"#{number}RESET\r".encode())
    f.close()

def resetAll():                                 #use to reset all servos
    time.sleep(1)
    for x in range(6):
        reset(x)


#Limp command
def limp(number):                               #make individual servos limp
    f = serial.Serial("/dev/ttyUSB0", 115200)
    f.write(f"#{number}L\r".encode())
    f.close()

def limpAll():
    for x in range(6):
        limp(x)

#ANGULAR ACCELERATION/DECELERATION
def angAccel(number,speed):                     #the angular acceleration speed of each servo
    f = serial.Serial("/dev/ttyUSB0", 115200)   #accepts values between 1 and 100, increments of 10 degrees per sec squared
    f.write(f"#{number}AA{speed}\r".encode())
    f.close()

def angDecel(number,speed):                     #the angular deceleration speed of each servo
    f = serial.Serial("/dev/ttyUSB0", 115200)   #accepts values between 1 and 100, increments of 10 degrees per sec squared
    f.write(f"#{number}AA{speed}\r".encode())
    f.close()

for x in range(6):                              #for loop used to make ang accel and decel for each servo 10 (a comfortable speed)
    angAccel(x, 10)
    angDecel(x, 10)

#ANGULAR HOLDING STIFFNESS
def holdStif(number, stiffness):                #determines the servo's ability to hold a desired position under load
    f = serial.Serial("/dev/ttyUSB0", 115200)   #values between -10 and 10
    f.write(f"#{number}AH{stiffness}\r".encode())
    f.close()

holdStif(5, -9)                                 #sets the holding stiffness for servo 5 to -9

#MOVEMENTS, all movements end in the default position
def pickUp():                                   #only picks up
    posInDegrees(2, 310)
    posInDegrees(3, 300)
    posInDegrees(5, -600)
    time.sleep(2)                               #movements temporarily sleep for alloted time (seconds)
    posInDegrees(3, 900)
    time.sleep(1)
    posInDegrees(4, 650)
    time.sleep(2)
    posInDegrees(5, 1)
    time.sleep(2)
    posInDegrees(3, 300)

def putDown():                                  #only puts down
    posInDegrees(3, 900)
    time.sleep(2)
    posInDegrees(5, -600)
    time.sleep(1)
    posInDegrees(3, 300)

def putDownRight():                             #puts down turning robot servo 1 to 200 degrees
    posInDegrees(1, 200)
    time.sleep(1)
    posInDegrees(3, 900)
    time.sleep(1)
    posInDegrees(5, -600)
    time.sleep(1)
    posInDegrees(3, 300)
    time.sleep(1)
    posInDegrees(1, 800)

def putDownLeft():                              #puts down turning robot servo 1 to 1500 degrees
    posInDegrees(1, 1500)
    time.sleep(1)
    posInDegrees(3, 900)
    time.sleep(1)
    posInDegrees(5, -600)
    time.sleep(1)
    posInDegrees(3, 300)
    time.sleep(1)
    posInDegrees(1, 800)

def mainRight():                                #pick up and put down "right" aka 200 degrees
    pickUp()
    time.sleep(1)
    putDownRight()

def mainLeft():                                 #pick up and put down "left" aka 1500 degrees
    pickUp()
    time.sleep(1)
    putDownLeft()

def main():                                     #pick up and put down first "right" and then "left"
    mainRight()
    time.sleep(1)
    mainLeft()

#os.system

if __name__ == "__main__":
    main()


