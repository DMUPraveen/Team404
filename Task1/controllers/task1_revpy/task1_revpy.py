from controller import Robot, Motor,PositionSensor 
from math import pi, radians,atan,cos,sin,acos,asin     #importing functions and variables required to the calculations

robot = Robot()

ServoNames = ["servo1","servo2","servo3","servo4"]      #storing names of the servos



#storing the positons given in the task in the format of [servo1 angle, servo2 angle, servo3 angle, servo4 angle]
HOME = [0,-45,45,90]
POSITION1 = [90,45,0,0]
POSITION2 = [-90,30,30,0]
#########################


#to make the code customizable we are defining the following variables. it's purpose is to store the angle which the endplate forms with the horizontal
#it is set to zero because the task specifies us to set the plate to be horizontal. (this is used in the setPlateAngle function
HorizontalAngle = 0 

#cordinate = [0,0]
#specifying arm lengths as given in the schematic of the task; for the use in inverse and forward kinematic calculations
Arm1_length =0.14
Arm2_length = 0.18
######################


cordinateoffset = 0.07                          #this variable is used to store the distance between the webots frame of reference and the frame of reference used in kinematic functions in the y direction
traveldistance = 0.3 - cordinateoffset          #changing the given height in the task from webots frame of reference to the frame of reference in the kinematic functions
traveltime = 5                                  #time taken for the arm to move 300mm height as specified in the task
timestep = 32                                   #the basic timestep of the world
sensor = PositionSensor("sensor")


#this is used to step webots stimulation and to exit the controller if webots decides to close
def step():
    if(robot.step(timestep) == -1):
        exit(0)
        
#this is used to convert the position given in the task from degrees to radians, since webots functions expect angles to be in radians
def convertToRadians(position):
    radianposition = [0]*4
    for i in range(0,4):
        radianposition[i] = radians(position[i])
    return radianposition

#this is used to create the server objects used to control the servos. it stores the objects in a list for ease of accesibility
def prepareServos():
    Servos = []
    for name in ServoNames:
        Servos.append(Motor(name))
    return Servos
        
#this function sets the servo positions to the values specified in the varible "position" that is fast in to it
#the variable is in the format [servo1angle,servo2angle,servo3angle,servo4angle] in radians
def movePosition(position):
   
    
    for i in range(0,4):
        Servos[i].setVelocity(100)
        
        Servos[i].setPosition(position[i]) 
    
#check whether the end plate has reached the desired angle (since it last to be set)   
def checkPosition(position):

    while True:
        sensor.enable(timestep)
        if(sensor.getValue() == position[3]):
            break
        step()

#does the same as the previous function but does so in a manner that avoids the end plate hiting the floor
def movePositionnohit(position):
    for i in range(0,4):
        if(i ==1):
            Servos[i].setPosition(-pi/4)
        else:
            Servos[i].setPosition(position[i])
    wait(1.5)
    Servos[1].setPosition(position[1])   

#this function calculates the angle that the end plate has to be set so that end plate makes an angle equel to the horizontal angle with the floor(by setting this ti zero we achieve the horizontal end plate)
#by providing the position to the function it returns the position after setting the end plate angle to the desired angle    
def setPlateAngle(position,theta):
    position[3] = theta - (position[1]+position[2])
    return position

#when given the position in terms of angles it returns the cartation cordinates of the end plate with origin at hing2
#the calculate cartation cordinates are returned in the format [servo1angle(base angle), x, y, servo4angle(endplate angle)]

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
    

#when this function calcuates the servo2 angle and servo3 angle for given cartation cordinates
# it takes in the position in the format [servo1angle(base angle), x, y, servo4angle(endplate angle)]  
#it returns the position in the format [servo1angle,servo2angle,servo3angle,servo4angle]

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
    
#it waits for the specified time before continuing    

def wait(time):
    
    begin_time = robot.getTime()
    while(robot.getTime() - begin_time < time):
        step()

#calculates the position the arm should be in each timestep for it to move verticaly keeping the end plate horizontal as specified in the task
#it returns this positions as a list 
#we are precalculationg this because if they are calcuated at run time it reduces the efficiency of the arm              
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

#this moves the arm to positions given in a list in each timestep 
#we are using this function to run the programme we calculated using the earlier function    
def runProgram(program):
    for position in program:
        movePosition(position)
        step()
                            

Servos = prepareServos()          #prepare servos and stores the resulting list of servo objects in the variable servos   

### converting to radians
HOME = convertToRadians(HOME)      
POSITION1 = setPlateAngle(convertToRadians(POSITION1),HorizontalAngle)
POSITION2 = setPlateAngle(convertToRadians(POSITION2),HorizontalAngle)
###############

#calculating the programme requred to move the arm to 300mm absolute hight
program1 = getMoveVerticalProgram(POSITION2,traveldistance,traveltime)


###############    THE TASK!    ###############

movePosition(HOME)
checkPosition(HOME)

wait(2)

movePositionnohit(POSITION1)
checkPosition(POSITION1)

wait(2)

movePosition(POSITION2)
checkPosition(POSITION2)

wait(1)

runProgram(program1)

wait(2)

movePosition(HOME)
################################################