#!/usr/bin/env pybricks-micropython

'''This is an example program that rotates Medium Lego EV3 motor with controlled speed'''
'''                      (There is used the PyBricks library)                         '''

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Button, Color
from pybricks.media.ev3dev import Font
from pybricks.tools import wait

# creating the EV3 block and Medium motor objects
ev3 = EV3Brick()
motor = Motor(Port.A)

# turning off the lights of the block and setting font parameters
ev3.light.off()
ev3.screen.set_font(Font(size = 12, bold = True))

# setting the start speed of the motor in rotates per minute
MOTOR_SPEED = 50

# here is the main infinite loop:
while True:
    # rotating the motor
    motor.run(MOTOR_SPEED * 6)
    
    if ev3.buttons.pressed() == [Button.UP]:
        if MOTOR_SPEED < 100:
            # if the UP button is pressed, increasing the motor speed
            MOTOR_SPEED += 1
            ev3.light.off()
        else:
            # on the speeds higher than 100 rpm (in both sides) the motor can behave strangely,
            # so instead of increasing speed turn on the red light of the block
            ev3.light.on(Color.RED)
    
    elif ev3.buttons.pressed() == [Button.DOWN]:
        if MOTOR_SPEED > -100:
            # if the DOWN button is pressed, decreasing the motor speed
            MOTOR_SPEED -= 1
            ev3.light.off()
        else:
            # on the speeds higher than 100 rpm (in both sides) the motor can behave strangely,
            # so instead of decreasing speed turn on the red light of the block
            ev3.light.on(Color.RED)
    
    # clearing the screen to rewrite the current speed of the motor on it
    ev3.screen.clear()
    ev3.screen.draw_text(20, 60, "Motor speed is " + str(MOTOR_SPEED) + " rpm")
    
    # stop the program for 25 milliseconds for the stability
    wait(25)