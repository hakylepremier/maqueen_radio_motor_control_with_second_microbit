from microbit import *
# dfrobot maqueen motor control demo

i2c.init(freq=100000, sda=pin20, scl=pin19)

def MotorControl(motor, direction, speed):
    buf = bytearray(3)
    # control for motor (0 for M1 (L) and 1 for M2 (R)
    if motor == 'left':
        buf[0] = 0x00
    elif motor == 'right':
        buf[0] = 0x02
    else:
        display.scroll('wrong motor name.', loop=True)
    # control for direction (0 for CW and 1 for CCW)
    if direction == 'forward':
        buf[1] = 0
    elif direction == 'backward':
        buf[1] = 1
    else:
        display.scroll('wrong direction name.', loop=True)
    # set speed
    buf[2] = speed
    i2c.write(0x10, buf)
