#!/usr/bin/env python3

'''This is an example program that rotates Medium Lego EV3 motor with controlled speed'''
'''                       (There is used the EV3DEV library)                          '''

from ev3dev2.display import Display
from ev3dev2.led import Leds
from ev3dev2.motor import MediumMotor, OUTPUT_A, SpeedRPM
from ev3dev2.button import Button
from time import sleep

# creating the EV3 block and Medium motor objects, plus special objects for controlling the block lights and screen
ev3 = Display()
leds = Leds()
motor = MediumMotor(OUTPUT_A)
buttons = Button()

# turning off the lights of the block
leds.all_off()

# setting the start speed of the motor in rotates per minute
MOTOR_SPEED = 50

# here is the main infinite loop:
while True:
    # rotating the motor
    motor.on(SpeedRPM(MOTOR_SPEED))

    if buttons.buttons_pressed == ["up"]:
        if MOTOR_SPEED < 100:
            # if the UP button is pressed, increasing the motor speed
            MOTOR_SPEED += 1
            leds.all_off()
        else:
            # on the speeds higher than 100 rpm (in both sides) the motor can behave strangely,
            # so instead of increasing speed turn on the red light of the block
            leds.set_color("LEFT", "RED")
            leds.set_color("RIGHT", "RED")
    
    elif buttons.buttons_pressed == ["down"]:
        if MOTOR_SPEED > -100:
            # if the DOWN button is pressed, decreasing the motor speed
            MOTOR_SPEED -= 1
            leds.all_off()
        else:
            # on the speeds higher than 100 rpm (in both sides) the motor can behave strangely,
            # so instead of decreasing speed turn on the red light of the block
            leds.set_color("LEFT", "RED")
            leds.set_color("RIGHT", "RED")
    
    # printing the current speed of the motor on the screen
    ev3.text_pixels("Motor speed is " + str(MOTOR_SPEED) + " rpm", x = 20, y = 60)
    ev3.update()
    
    # stop the program for 25 milliseconds for the stability
    sleep(0.025)