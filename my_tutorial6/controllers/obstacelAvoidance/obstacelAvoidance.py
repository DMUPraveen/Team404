from controller import Robot
from controller import DistanceSensor
from time import sleep
robot = Robot()
wheel = []
wheel_Names = ["wheel1","wheel2","wheel3","wheel4"]
TIME_STEP = 64

sensor1 = DistanceSensor("sensor1")
sensor2 = DistanceSensor("sensor2")
speed = 10
rotspeed = 5
limit = 1000

for i in range(0,4):
    wheel.append(robot.getMotor(wheel_Names[i]))
    wheel[i].setPosition(float('inf'))
    wheel[i].setVelocity(0.0)
    
def rotate():

    wheel[0].setVelocity(-rotspeed)
    wheel[1].setVelocity(rotspeed)
    wheel[2].setVelocity(-rotspeed)
    wheel[3].setVelocity(rotspeed)
    
def goforward():
    for i in range(4):
        wheel[i].setVelocity(speed)
    
goforward()

   
while robot.step(TIME_STEP) != -1:
    sensor1.enable(TIME_STEP)
    sensor2.enable(TIME_STEP)
    value1 = sensor1.getValue()
    value2 = sensor2.getValue()
    
    if(value1 < limit or value2 < limit):
        rotate()
    else:
        goforward()