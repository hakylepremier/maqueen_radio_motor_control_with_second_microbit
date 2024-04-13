from microbit import *
# dfrobot maqueen motor control demo

i2c.init(freq=100000, sda=pin20, scl=pin19)

def MotorControl(motor, direction, speed):
    buf = bytearray(3)
    # control for motor ('left' for M1 (L) and 'right for M2 (R)
    if motor == 'left':
        buf[0] = 0x00
    elif motor == 'right':
        buf[0] = 0x02
    else:
        display.scroll('wrong motor name.', loop=True)
    # control for direction ('forward' for CW and 'backward' for CCW)
    if direction == 'forward':
        buf[1] = 0
    elif direction == 'backward':
        buf[1] = 1
    else:
        display.scroll('wrong direction name.', loop=True)
    # set speed
    buf[2] = speed
    i2c.write(0x10, buf)

def forward():
    MotorControl('left', 'forward', 255)
    MotorControl('right', 'forward', 255)

def backward():
    MotorControl('left', 'backward', 255)
    MotorControl('right', 'backward', 255)

def stop():
    MotorControl('left', 'forward', 0)
    MotorControl('right', 'forward', 0)

def left():
    MotorControl('left', 'backward', 255)
    MotorControl('right', 'forward', 255)

def right():
    MotorControl('left', 'forward', 255)
    MotorControl('right', 'backward', 255)

def test_motors():
    display.show('F')
    forward()
    sleep(1000)
    display.show('B')
    backward()
    sleep(1000)
    display.show('S')
    stop()
    sleep(1000)
    display.show('L')
    left()
    sleep(1000)
    display.show('R')
    right()
    sleep(1000)
    display.show('S')
    stop()
    sleep(1000)
    display.show(Image.HAPPY)

# To test the motors uncomment the line below
# test_motors()

