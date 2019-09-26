from controller import Robot , DistanceSensor,Camera 
robot=Robot() 
sensor1=DistanceSensor("sensor1")
sensor2=DistanceSensor("sensor2")
sensor3 =DistanceSensor("sensor3")
camera = Camera("camera")
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
    camera.enable(TIME_STEP)
    image = camera.getImageArray()
    average = 0
    check = 0
    X = camera.getWidth()
    Y = camera.getHeight()
    for x in range(0,X):
        for y in range(0,Y):
            r  = image[x][y][0]
            g  = image[x][y][1]
            b  = image[x][y][2]
            gray = (r+g+b)/3
            if(gray >50):
                gray = 1
            else:
                gray = 0
            average = average + gray*(x-X/2)
            #check = check+gray*(y-Y/2)
    average = average/(X*Y)
    if(average >0.5):
        rotateR()
        #print("R")
    if(average<-0.5):
        rotateL()
        #print("L")
    if(average >-0.5 and average <0.5):
        forward()
            #print("f")
    print(average)
  
 
    