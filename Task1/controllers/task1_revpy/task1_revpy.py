from controller import Robot, Motor,Display
from math import pi, radians,atan,cos,sin,acos,asin

robot = Robot()

ServoNames = ["servo1","servo2","servo3","servo4"]
HOME = [0,-45,45,90]
POSITION1 = [90,45,0,0]
POSITION2 = [-90,30,30,0]
HorizontalAngle = 0
cordinate = [0,0]
Arm1_length =0.14
Arm2_length = 0.18
cordinateoffset = 0.07
traveldistance = 0.3 - cordinateoffset
traveltime = 5
timestep = 32

def step():
    if(robot.step(timestep) == -1):
        exit(0)
        

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
        Servos[i].setVelocity(100)
        
        Servos[i].setPosition(position[i]) 
        #step()

def movePositionnohit(position):
    for i in range(0,4):
        if(i ==1):
            Servos[i].setPosition(-pi/4)
        else:
            Servos[i].setPosition(position[i])
    wait(1.5)
    Servos[1].setPosition(position[1])   
    
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
    cordinate = [position[0],x,y,position[3]]
    

    return cordinate
    




def reverseKinematic(cordinate):
    position = [0]*4
    x = cordinate[1]
    y = cordinate[2]
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
    position[0] = cordinate[0]
    position[1] = theta1
    position[2] = theta2
    position[3] = cordinate[3]
    return position
    
    

def wait(time):
    
    begin_time = robot.getTime()
    print(begin_time)
    while(robot.getTime() - begin_time < time):
        step()
            
def getMoveVerticalProgram(currentposition,distance,duration):
    duration = (duration*1000)//timestep #number of steps in the motion
    speed = distance/duration
    currentcordinate = forwardKinematic(currentposition)
    Program = []
    #displacement = 0
    cordinate = currentcordinate
    while(cordinate[2] <=distance):
        #print(cordinate)
        cordinate[2] = cordinate[2] +speed
        #displacement = displacement + speed
        position = reverseKinematic(cordinate)
        position = setPlateAngle(position,HorizontalAngle)
        Program.append(position)
    return Program
    
def runProgram(program):
    for position in program:
        movePosition(position)
        step()
def printScreen(string):
    display.setColor(0x000000)
    width = display.getWidth()
    height = display.getHeight()
    display.fillRectangle(0,0,width,height)
    display.setColor(0xFFFFFF)
    display.drawText(string,0,0)
                     

display = Display("display")


Servos = prepareServos()
HOME = convertToRadians(HOME)
POSITION1 = setPlateAngle(convertToRadians(POSITION1),HorizontalAngle)
POSITION2 = setPlateAngle(convertToRadians(POSITION2),HorizontalAngle)
program1 = getMoveVerticalProgram(POSITION2,traveldistance,traveltime)

printScreen("HOME")
movePosition(HOME)
#printScreen("WAIT 2")
wait(2)
printScreen("POSITION1")
movePositionnohit(POSITION1)
#printScreen("WAIT 2")
wait(2)
printScreen("POSITION2")
movePosition(POSITION2)
#printScreen("WAIT 1")
wait(1)
printScreen("MOVE UP")
runProgram(program1)
#printScreen("WAIT 2")
wait(2)
printScreen("HOME")
movePosition(HOME)
f = open("Program.txt","a")
for program in program1:
    f.write(str(forwardKinematic(program)) + "\n")
f.close()
 