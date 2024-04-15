from microbit import *
import radio

accel_y = 0
accel_x = 0
# This changes the sensitivity in the x direction (left, right)
accel_x_offset = 400
# This changes the sensitivity in the y direction (forward, backward)
accel_y_offset = 400
direction = "F"

# Initialise radio
radio.on()
radio.config(channel=13, group=7)

display.show(Image.HAPPY)

while True:
    accel_x = accelerometer.get_x()
    accel_y = accelerometer.get_y()

    if accel_x > accel_x_offset:
        direction = "R"
    elif accel_x < accel_x_offset * -1:
        direction = "L"
    if accel_y > accel_y_offset:
        direction = "F"
    elif accel_y < accel_y_offset * -1:
        direction = "B"
    if accel_x < accel_x_offset and accel_x > accel_x_offset * -1 and (accel_y < accel_y_offset and accel_y > accel_y_offset * -1):
        direction = "-"

    display.show(direction)
    if direction == "-":
        direction = "S"

    radio.send(direction)
