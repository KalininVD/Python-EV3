#!/usr/bin/env pybricks-micropython

'''This is a program for the remote-controlled wheeled all-terrain vehicle'''
'''                (There is used the PyBricks library)                   '''

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, InfraredSensor
from pybricks.parameters import Port, Direction, Color, Button

# creating the EV3 block object
ev3 = EV3Brick()

# creating the motors objects
turn = Motor(Port.A, Direction.CLOCKWISE, [[8, 40], [8, 40]])
front = Motor(Port.B, Direction.COUNTERCLOCKWISE, [[12, 36], [20, 28], [12, 36]])
back = Motor(Port.C, Direction.CLOCKWISE, [[12, 36], [20, 28], [12, 36]])

# creating the sensors objects
left = UltrasonicSensor(Port.S2)
right = InfraredSensor(Port.S3)
remote = InfraredSensor(Port.S4)

# setting the speed of all wheels in rotates per minute
MOTOR_SPEED = 60

# setting the limit values for the sensors of the critical turn angle of the vehicle
LEFT_CRITICAL = 35
RIGHT_CRITICAL = 15

# there are functions for the possible moves of the vehicle:

# hold() function is used to strongly stop the vehicle if the "exit" button is pressed on the remote controller
def hold():
    turn.hold()
    front.hold()
    back.hold()

# forward() function is used to move the vehicle forward without turning (changing the turn angle)
def forward():
    front.run(MOTOR_SPEED)
    back.run(MOTOR_SPEED)

# backward() function is used to move the vehicle backward without turning (changing the turn angle)
def backward():
    front.run(-MOTOR_SPEED)
    back.run(-MOTOR_SPEED)

# turn_left() function is used to change the turn angle of the vehicle so it will move left if one of "forward" buttons is pressed
def turn_left():
    if left.distance() > LEFT_CRITICAL:
        turn.run(MOTOR_SPEED)
        ev3.light.off()
    else:
        turn.hold()
        ev3.light.on(Color.RED)
        ev3.speaker.beep()

# turn_right() function is used to change the turn angle of the vehicle so it will move right if one of "forward" buttons is pressed
def turn_right():
    if right.distance() > RIGHT_CRITICAL:
        turn.run(-MOTOR_SPEED)
        ev3.light.off()
    else:
        turn.hold()
        ev3.light.on(Color.RED)
        ev3.speaker.beep()

# stop() function is used to stop all the motors to let the vehicle stop itself if no buttons are pressed on the remote controller
def stop():
    turn.stop()
    front.stop()
    back.stop()


# here is the start of the main program

# getting ready for remote control (clearing screen, turning off the block lights and playing a sound to inform the user about starting the program)
ev3.screen.clear()
ev3.light.off()
ev3.speaker.play_file("/home/robot/_Offroad Truck/ready.wav")

# setting the main flag is_remote_control_enabled to the True value to start the remote control loop
is_remote_control_enabled = True

# starting the main loop of the program
while is_remote_control_enabled:
    if remote.buttons(2) == [Button.BEACON]:
        # if the "exit" button is pressed on the remote controller on the second channel, the main flag will be set to False to stop the main loop of the program
        hold()
        ev3.speaker.play_file("/home/robot/_Offroad Truck/horn_2.wav")
        is_remote_control_enabled = False
    elif remote.buttons(1) == []:
        # if there is no buttons pressed on the remote controller, the vehicle just stops
        stop()
    elif remote.buttons(1) == [Button.LEFT_UP]:
        # pressing the left up button on the remote controller will start the left turning and moving forward
        turn_left()
        forward()
    elif remote.buttons(1) == [Button.RIGHT_UP]:
        # pressing the right up button on the remote controller will start the right turning and moving forward
        turn_right()
        forward()
    elif remote.buttons(1) == [Button.LEFT_DOWN]:
        # pressing the left down button on the remote controller will start the left turning and moving backward
        turn_left()
        backward()
    elif remote.buttons(1) == [Button.RIGHT_DOWN]:
        # pressing the right down button on the remote controller will start the right turning and moving backward
        turn_right()
        backward()
    elif remote.buttons(1) == [Button.LEFT_UP, Button.RIGHT_UP]:
        # pressing both left and right up buttons on the remote controller will move the vehicle forward without turning
        turn.hold()
        forward()
    elif remote.buttons(1) == [Button.LEFT_DOWN, Button.RIGHT_DOWN]:
        # pressing both left and right down buttons on the remote controller will move the vehicle backward without turning
        turn.hold()
        backward()
    elif remote.buttons(1) == [Button.BEACON]:
        # pressing the "exit" button on the remote controller on the first channel will hardly stop the vehicle and start the horn sound
        hold()
        ev3.speaker.play_file("/home/robot/_Offroad Truck/horn_1.wav")
    else:
        # if the buttons pressed on the remote controller can't be interpreted to some moves of the vehicle, it just stops
        stop()