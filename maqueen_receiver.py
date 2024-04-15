from microbit import *
import radio

# dfrobot maqueen motor control demo

i2c.init(freq=100000, sda=pin20, scl=pin19)
radio.on()
radio.config(channel=13, group=7)

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

def forward(duration=50):
    MotorControl('left', 'forward', 255)
    MotorControl('right', 'forward', 255)
    sleep(duration)

def backward(duration=50):
    MotorControl('left', 'backward', 255)
    MotorControl('right', 'backward', 255)
    sleep(duration)

def stop(duration=50):
    MotorControl('left', 'forward', 0)
    MotorControl('right', 'forward', 0)
    sleep(duration)

def left(duration=50):
    MotorControl('left', 'backward', 255)
    MotorControl('right', 'forward', 255)
    sleep(duration)

def right(duration=50):
    MotorControl('left', 'forward', 255)
    MotorControl('right', 'backward', 255)
    sleep(duration)

def test_motors():
    display.show('F')
    forward(1000)
    display.show('B')
    backward(1000)
    display.show('S')
    stop(1000)
    display.show('L')
    left(1000)
    display.show('R')
    right(1000)
    display.show('S')
    stop(1000)
    display.show(Image.YES)
    sleep(1000)

# To test the motors uncomment the line below
# test_motors()
interval = 50
display.show(Image.ASLEEP)
state = 'idle'
moveFlag = False

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        state = 'move'
    if button_b.is_pressed():
        display.show(Image.TARGET)
        sleep(1000)
        state = 'test'
    if accelerometer.current_gesture() == 'down':
        display.show(Image.ASLEEP)
        state = 'idle'

    if state == 'move':
        direction = radio.receive()
        if direction == 'F':
            display.show(Image.ARROW_N)
            forward()
        elif direction == 'B':
            display.show(Image.ARROW_S)
            backward()
        elif direction == 'L':
            display.show(Image.ARROW_E)
            left()
        elif direction == 'R':
            display.show(Image.ARROW_W)
            right()
        else:
            display.show(Image.HAPPY)
            stop()
    elif state == 'test':
        test_motors()
        state = 'idle'
    else:
        display.show(Image.ASLEEP)

