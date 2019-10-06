from controller import Robot, Motor,PositionSensor
from math import pi, radians,atan,cos,sin,acos,asin

robot = Robot()
ServoNames = ["servo1","servo2","servo3","servo4"]
HOME = [0,-45,45,90]
POSITION1 = [90,45,0,0]
POSITION2 = [90,30,30,0]
HorizontalAngle = 0
cordinate = [0,0]
Arm1_length =0.14
Arm2_length = 0.18
sensor = PositionSensor("sensor")


def convertToRadians(position):
    radianposition = [0]*4
    for i in range(0,4):
        radianposition[i] = radians(position[i])
    return radianposition
    
def prepareServos():
    Servos = []
    for name in ServoNames:
        Servos.append(Motor(name))
    return Servos
        

def movePosition(position):
    for i in range(0,4):
        Servos[i].setPosition(position[i])

    print(sensor.getPosition())

    
def setPlateAngle(position,theta):
    position[3] = theta - (position[1]+position[2])
    return position



def forwardKinematic(position):
    a1 = Arm1_length
    a2 = Arm2_length
    cordinate = [0,0]
    theta1 = position[1]
    theta2 = position[2]
    x = a1*sin(theta1)+a2*cos(theta1+theta2)
    y = a1*cos(theta1)-a2*sin(theta1+theta2)
    cordinate = [x,y]
    

    return cordinate
    




def reverseKinematic(baseangle,cordinate,plateangle):
    position = [0]*4
    x = cordinate[0]
    y = cordinate[1]
    r = (x*x+y*y)**0.5
    if(x==0):
        alpha = pi/2
    else:
        alpha = atan(y/x)
    #alpha = atan(y/x)
    a1 = Arm1_length
    a2 = Arm2_length
    D = (a1*a1+a2*a2-r*r)/(2*a1*a2) #D = cos(theta2)
    theta2 = pi/2-acos(D)
    beta = asin((cos(theta2)*a2)/r)
                   #E = sin(theta2)
    
    theta1 = pi/2-beta-alpha
    position[0] = baseangle
    position[1] = theta1
    position[2] = theta2
    position[3] = plateangle
    return position
    
    

    



    


HOME = convertToRadians(HOME)
POSITION1 = convertToRadians(POSITION1)
POSITION2 = convertToRadians(POSITION2)
cordinate = forwardKinematic(POSITION2)
POSITION3 = setPlateAngle(reverseKinematic(pi/2,cordinate,0),HorizontalAngle)
print(POSITION3)
#print(cordinate)
POSITION1 = setPlateAngle(POSITION1,HorizontalAngle)
POSITION2 = setPlateAngle(POSITION2,HorizontalAngle)

Servos = prepareServos()
status = True
tick = 0
Tick = 0
while (robot.step(32)) != -1:
    
    if tick == 0:
        movePosition(HOME)
    if tick == 100:
        movePosition(POSITION1)
    if tick == 200:
        movePosition(POSITION2)
    if tick == 300:
        movePosition(POSITION3)
    if tick >=400 and status:
        distance = 0.001
        cordinate[1] = cordinate[1]+distance
        print(cordinate)
        print(distance)
        movePosition(setPlateAngle(reverseKinematic(pi/2,cordinate,0),HorizontalAngle))
        #print(steps)
        if(cordinate[1] > 0.23):
            status = False
            print(tick)

    if tick > 764:
        movePosition(HOME)
        
    tick = tick+1