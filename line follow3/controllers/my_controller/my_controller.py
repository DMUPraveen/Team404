from controller import Robot , DistanceSensor 
robot=Robot() 
sensor1=DistanceSensor("sensor1")
sensor2=DistanceSensor("sensor2")
sensor3 =DistanceSensor("sensor3")
wheel=[] 
wheel_names=["wheel1","wheel2","wheel3","wheel4"]
TIME_STEP=64
for i in range(4):
    wheel.append(robot.getMotor(wheel_names[i]))
    wheel[i].setPosition(float('inf'))
    wheel[i].setVelocity(0.0)
    #print(wheel[i])
limit=801
def forward(speed=1):
  
    wheel[0].setVelocity(speed)
    wheel[1].setVelocity(speed)
    wheel[2].setVelocity(speed)
    wheel[3].setVelocity(speed)

def rotateL():
    wheel[0].setVelocity(-1)
    wheel[1].setVelocity(1)
    wheel[2].setVelocity(-1)
    wheel[3].setVelocity(1)
    
def rotateR():
    wheel[0].setVelocity(1)
    wheel[1].setVelocity(-1)
    wheel[2].setVelocity(1)
    wheel[3].setVelocity(-1)



def stop():
    for i in range(0,4):
        wheel[i].setVelocity(0.0)
#rotate()       
while robot.step(TIME_STEP)!= -1:
    sensor1.enable(TIME_STEP)
    sensor2.enable(TIME_STEP)
    sensor3.enable(TIME_STEP)
    x = sensor1.getValue()
    y = sensor2.getValue()
    z = sensor3.getValue()
    #print("{},{}".format(str(x),str(y)))
    '''if(z>x and z>y):
        forward()
    if(x>z and x>y):
        rotateL()
    if(y>z and y>x):
        rotateR()
    else:
        forward()'''
        
    print("{},{},{}".format(str(x),str(z),str(y)))
    
    if z >700:
        forward()
    
    elif(x>z and x>y):
        rotateR()
    elif(y>z and y>x):
        rotateL()
    else:
        rotateL()
        

    
    #print(k)

        
        

    #print(sensorL.getValue())
 
    