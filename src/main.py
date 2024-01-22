# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Elliot Scher                                                 #
# 	Created:      1/15/2024, 9:39:10 AM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
from math import pi
from time import sleep

# Brain should be defined by default
brain=Brain()

rightMotor = Motor(Ports.PORT15, False)
leftMotor = Motor(Ports.PORT11, True)
armMotor = Motor(Ports.PORT20, False)
rangeFinder = Sonar(brain.three_wire_port.a)
bumpSensor = Bumper(brain.three_wire_port.c)
reflectance = Line(brain.three_wire_port.d)

GEAR_RATIO = 60.0/12.0

def distanceToTurns(distance):
    return distance * GEAR_RATIO / (4 * pi)

state = 0

def homingSequence():
    global state
    armMotor.spin(DirectionType.REVERSE, 5 * GEAR_RATIO, RPM)
    if bumpSensor.pressing():
        armMotor.stop(BRAKE)
        armMotor.set_position(0, TURNS)
        armMotor.spin_for(DirectionType.FORWARD, 85 * GEAR_RATIO, DEGREES, True)
        state = 1
        return

def bucketSearch():
    global state
    leftMotor.spin_for(DirectionType.FORWARD, distanceToTurns(12), TURNS, 30 * GEAR_RATIO, RPM, False)
    rightMotor.spin_for(DirectionType.FORWARD, distanceToTurns(12), TURNS, 30 * GEAR_RATIO, RPM, True)
    while True:
        if reflectance.reflectivity() < 30:
            leftMotor.spin(DirectionType.FORWARD, 30 * GEAR_RATIO, RPM)
            rightMotor.spin(DirectionType.FORWARD, 30 * GEAR_RATIO, RPM)
        else:
            break
    
    leftMotor.spin_for(DirectionType.REVERSE, distanceToTurns(12), TURNS, 30 * GEAR_RATIO, RPM, False)
    rightMotor.spin_for(DirectionType.REVERSE, distanceToTurns(12), TURNS, 30 * GEAR_RATIO, RPM, True)

    armMotor.spin_for(DirectionType.REVERSE, 20 * GEAR_RATIO, DEGREES)

    leftMotor.spin_for(DirectionType.FORWARD, distanceToTurns(12), TURNS, 30 * GEAR_RATIO, RPM, False)
    rightMotor.spin_for(DirectionType.FORWARD, distanceToTurns(12), TURNS, 30 * GEAR_RATIO, RPM, True)

    armMotor.spin_for(DirectionType.FORWARD, 25 * GEAR_RATIO, DEGREES)

    state = 2
    return

def retrieveBucket():
    global state
    leftMotor.spin_for(DirectionType.REVERSE, distanceToTurns(4), TURNS, 30 * GEAR_RATIO, RPM, False)
    rightMotor.spin_for(DirectionType.REVERSE, distanceToTurns(4), TURNS, 30 * GEAR_RATIO, RPM, True)
    while True:
        if reflectance.reflectivity() < 30:
            leftMotor.spin(DirectionType.REVERSE, 30 * GEAR_RATIO, RPM)
            rightMotor.spin(DirectionType.REVERSE, 30 * GEAR_RATIO, RPM)
        else:
            break
    leftMotor.spin_for(DirectionType.REVERSE, distanceToTurns(12), TURNS, 30 * GEAR_RATIO, RPM, False)
    rightMotor.spin_for(DirectionType.REVERSE, distanceToTurns(12), TURNS, 30 * GEAR_RATIO, RPM, True)

    state = 0

while True:
    if state == 0:
        homingSequence()

    if state == 1:
        bucketSearch()

    if state == 2:
        retrieveBucket()