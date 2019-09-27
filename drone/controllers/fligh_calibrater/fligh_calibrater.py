"""flight_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor,Accelerometer

# create the Robot instance.
robot = Robot()
motor = Motor("motor")
acc = Accelerometer("accelerometer")

# get the time step of the current world.
timestep = 64
motor.setPosition(float("inf"))
#motor.setVelocity(3.133)
velocity = 3.12
t = 0
samples = 0
f = open("calibration.txt","a")
array = []
sum = 0
# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    acc.enable(timestep)
    samples = samples +1
    
    motor.setVelocity(velocity)
    value = acc.getValues()[1]
    sum = sum + value
    t = t+1
    print(samples)
    if(t ==10):
       acceleration = sum/10 - 9.81
       
       array.append([velocity,acceleration])
       velocity = velocity + 0.001
       sum = 0
       t = 0
    if(samples > 200):
        break
       
    print(velocity)   
for data in array:
    f.write("velocity : {}, force per unit mass: {} \n".format(data[0],data[1]))  
    
f.close()
print("done calibration") 



    
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)


# Enter here exit cleanup code.
