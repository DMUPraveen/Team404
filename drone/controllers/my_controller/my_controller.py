"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot ,Motor,Accelerometer,Keyboard
robot = Robot()
acc = Accelerometer("accelerometer")
motor = Motor("motor")
keyboard = Keyboard()
#acc =Accelerometer("accelerometer")
motor.setPosition(float("inf"))
velocity = 31.33
motor.setVelocity(31.33)
timestep = 64
stability = True
keyboard.enable(timestep)
while robot.step(timestep)!=-1:
    acc.enable(timestep)
    
    yg = acc.getValues()[1]
    ya = yg -9.81
    if(yg>0 and stability):
        velocity = velocity - (ya/0.06)*0.01
        #print(ya)
        motor.setVelocity(velocity)
    k = keyboard.getKey()
    #print(k)    
    if(k == ord('S')):
        motor.setVelocity(31)
        #stability = False
        print("going down")
        
    if(k == ord('W')):
        motor.setVelocity(31.5)
        print("going up")

    #print(velocity)
# create the Robot instance.
