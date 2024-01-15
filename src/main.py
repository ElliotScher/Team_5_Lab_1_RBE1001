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

# Brain should be defined by default
brain=Brain()

rightMotor = Motor(Ports.PORT15, False)
leftMotor = Motor(Ports.PORT11, True)

GEAR_RATIO = 60.0/12.0

leftMotor.spin_for(DirectionType.FORWARD, 1 * GEAR_RATIO, TURNS, 5 * GEAR_RATIO, RPM, True)

rightMotor.spin_for(DirectionType.FORWARD, 1 * GEAR_RATIO, TURNS, 5 * GEAR_RATIO, RPM, True)

leftMotor.spin_for(DirectionType.FORWARD, 1 * GEAR_RATIO, TURNS, 5 * GEAR_RATIO, RPM, False)
rightMotor.spin_for(DirectionType.FORWARD, 1 * GEAR_RATIO, TURNS, 5 * GEAR_RATIO, RPM, False)