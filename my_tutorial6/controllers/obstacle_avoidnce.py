from controller import Robot
from controller import DistanceSensor
from time import sleep
robot = Robot()
wheel = []
wheel_Names = ["wheel1","wheel2","wheel3","wheel4"]
TIME_STEP = 64

sensor = DistanceSensor("distance sensor")
speed = 10
rotspeed = 5
limit = 800

for i in range(4):
    wheel.append(robot.getMotor(wheel_Names[i]))
    wheel[i].setPosition(float('inf'))
    wheel[i].setVelocity(0.0)
    
def rotate()

    wheel[0].setVelocity(-rotspeed)
    wheel[1].setVelocity(rotspeed)
    wheel[2].setVelocity(-rotspeed)
    wheel[4].setVelocity(rotspeed)
    
def goforward():
    for i in range(4):
        wheel[i].setVelocity(speed)
    
    
while robot.step(TIME_STEP) != -1:
    sensor.enable(TIME_STEP)
    value = sensor.getValue()
    
    if(value < limit):
        rotate()
        while True:
            if value > limit:
                goforward()
                break
    