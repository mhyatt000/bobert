import os
import time

import serial


def toserial():
    """writes the result of func to serial port"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(serial.Serial("/dev/ttyUSB0", 115200), "w") as file:
                file.write(str(result.encode()))

            return result

        return wrapper

    return decorator


@toserial()
def servo(unit, cmd, value, sleep=True):
    """select a servo command"""

    cmds = {
        # set to relative angle
        "relative": f"#{unit}MD{value}\r",
        # set to absolute angle
        "absolute": f"#{unit}D{value}\r",
        # set to wheel mode where it rotates in that direction (nonstop)
        "wheel": f"#{unit}WD{value}\r",
        # stop immediately and hold that angular position
        "halt": f"#{unit}H\r",
        # reset individual servos
        "reset": f"#{unit}RESET\r",
        # make servo limp
        "limp": f"#{unit}L\r",
        # the angular acceleration speed of each servo
        # accepts values between 1 and 100, increments of 10 degrees per sec squared
        "accelerate": f"#{unit}AA{value}\r",
        # determines the servo's ability to hold a desired position under load
        # values between -10 and 10
        "stiff": f"#{unit}AH{value}\r",
        # used to have the servo move to a specific angle upon power up
        "start": f"#{unit}CFD\r",
    }

    out = cmds[cmd]
    assert not "None" in out, "cant have None cmd"
    if sleep:
        time.sleep(0.25)
    return out


def allservo(cmd, value):
    for i in range(6):
        servo(i, cmd, value, sleep=False)


# MOVEMENTS, all movements end in the default position
def pickUp():
    """only picks up"""

    servo(2, "absolute", 310)
    servo(3, "absolute", 300)
    servo(5, "absolute", -600)
    servo(3, "absolute", 900)
    servo(4, "absolute", 650)
    servo(5, "absolute", 1)
    servo(3, "absolute", 300)


def put_down(loc="center"):
    """puts down turning robot servo 1 to 200 degrees"""

    loc = 200 if loc == "right" else 1500 if loc == "left" else 800

    servo(1, "absolute", loc)
    servo(3, "absolute", 900)
    servo(5, "absolute", -600)
    servo(3, "absolute", 300)
    servo(1, "absolute", 800)


def main():
    """pick up and put down first "right" and then "left"""

    allservo("start")
    allservo("accelerate", 10)

    # sets the holding stiffness for servo 5 to -9
    servo(5, "stiff", -9)

    pick_up()
    put_down()


if __name__ == "__main__":
    main()
