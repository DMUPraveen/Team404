"""robotarmcontroller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor
from time import time
# create the Robot instance.
robot = Robot()

TIME_STEP = 64

pi = 3.14159

rotstep = pi/12

motor2 = Motor("motor2")
motor1 = Motor("motor1")
while (robot.step(TIME_STEP))!=-1:
    pos = 0
    t = robot.getTime()
    
    for i in range(0,7):
        if( i+1>t and t>i):
            motor2.setPosition(-rotstep*i)
            motor1.setPosition(rotstep*i)
            pos = pi*i
        
    
    if pos > pi*5:
        break

# Enter here exit cleanup code.
