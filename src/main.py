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
rangeFinder = Sonar(brain.three_wire_port.a)
bumpSensor = Bumper(brain.three_wire_port.c)
lineFollower = Line(brain.three_wire_port.d)

GEAR_RATIO = 60.0/12.0

def distanceToTurns(distance):
    return distance * GEAR_RATIO / (4 * pi)

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

# testing reflectivity sensor
# while True:
#     sleep(1)
#     print(lineFollower.reflectivity())