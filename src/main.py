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
lineFollower = Line(brain.three_wire_port.d)

class State:
    def __init__(self) -> None:
        self.STATE = 0

    def setState(self, state):
        self.STATE = state
    
    def getState(self):
        return self.STATE

# def distanceToTurns(distance):
#     return distance * GEAR_RATIO / (4 * pi)

# motor testing
# leftMotor.spin_for(DirectionType.FORWARD, distanceToTurns(24), TURNS, 30 * GEAR_RATIO, RPM, False)
# rightMotor.spin_for(DirectionType.FORWARD, distanceToTurns(24), TURNS, 30 * GEAR_RATIO, RPM, False)

# range finder testing
# while True:
#     sleep(1)
#     print(rangeFinder.distance(INCHES))

# bump sensor testing
# while (not bumpSensor.pressing()):
#     rightMotor.spin(DirectionType.FORWARD, 30 * GEAR_RATIO, RPM)
#     leftMotor.spin(DirectionType.FORWARD, 30 * GEAR_RATIO, RPM)
#     print(leftMotor.torque())
#     if (bumpSensor.pressing() == 1):
#         break
#         exit

# # testing reflectivity sensor
# while True:
#     sleep(1)
#     print(lineFollower.reflectivity())

GEAR_RATIO = 60.0/12.0
TIMES_SEEN = 0
state = 0

def homingSequence():
    global state
    armMotor.spin(DirectionType.REVERSE, 5 * GEAR_RATIO, RPM)
    if bumpSensor.pressing():
        armMotor.stop(BRAKE)
        armMotor.set_position(0, TURNS)
        armMotor.spin_for(DirectionType.FORWARD, 75 * GEAR_RATIO, DEGREES, True)
        state = 1


while True:
    if state == 0:
        homingSequence()

    if state == 1:
        leftMotor.spin(DirectionType.FORWARD, 5 * GEAR_RATIO, RPM)
        rightMotor.spin(DirectionType.FORWARD, 5 * GEAR_RATIO, RPM)

