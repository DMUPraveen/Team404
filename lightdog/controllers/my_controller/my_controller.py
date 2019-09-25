from controller import Robot , LightSensor 
robot=Robot() 
sensorR=LightSensor("sensor1")
sensorL=LightSensor("sensor2")
wheel=[] 
wheel_names=["wheel1","wheel2","wheel3","wheel4"]
TIME_STEP=64
for i in range(4):
    wheel.append(robot.getMotor(wheel_names[i]))
    wheel[i].setPosition(float('inf'))
    wheel[i].setVelocity(0.0)
    #print(wheel[i])
limit=800
def forward(speed=10):
  
    wheel[0].setVelocity(speed)
    wheel[1].setVelocity(speed)
    wheel[2].setVelocity(speed)
    wheel[3].setVelocity(speed)

def rotateL():
    wheel[0].setVelocity(-5.0)
    wheel[1].setVelocity(5.0)
    wheel[2].setVelocity(-5.0)
    wheel[3].setVelocity(5.0)
    
def rotateR():
    wheel[0].setVelocity(5.0)
    wheel[1].setVelocity(-5.0)
    wheel[2].setVelocity(5.0)
    wheel[3].setVelocity(-5.0)



def stop():
    for i in range(0,4):
        wheel[i].setVelocity(0.0)
#rotate()       
while robot.step(TIME_STEP)!= -1:
    sensorR.enable(TIME_STEP)
    sensorL.enable(TIME_STEP)
    x = sensorR.getValue()
    y = sensorL.getValue()
    #print(x)
    r = (x*x+y*y)**0.5
    if(r != 0):
        X = x/r
        Y = y/r
    else:
        X = 0
        Y = 0
    #print(str(X)+" ,"+str(Y))
    k = X-Y
    
    #print(k)
    print(x)
    if(k<0.1 and k>-0.1 and r!=0):
        forward()
        
    if(k>0.1):
        rotateL()
        
    if(k<-0.1 or r == 0):
        rotateR()
        
    if(x>2.5 or y>2.5):
        stop()
        
        

    #print(sensorL.getValue())
 
    