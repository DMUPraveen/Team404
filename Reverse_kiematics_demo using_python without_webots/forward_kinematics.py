from math import pi, atan, acos, asin, sin, fabs, degrees


import turtle
t = turtle.Turtle()
arm = turtle.Turtle()
t.speed(0)

def DrawAxis():
    t.forward(500)
    t.backward(1000)
    t.forward(500)
    t.left(90)
    t.forward(500)
    t.backward(1000)
    t.forward(500)
    t.right(90)

def verticalGridline(num):
    for line in range(num):
        t.forward(25)
        t.left(90)
        t.forward(500)
        t.backward(1000)
        t.forward(500)
        t.right(90)
    t.backward(num*25)
    for line in range(num):
        t.backward(25)
        t.left(90)
        t.forward(500)
        t.backward(1000)
        t.forward(500)
        t.right(90)
    t.forward(num*25)

def HorizontalGridline(num):
    for line in range(num):
        t.left(90)
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.backward(1000)
        t.forward(500)
    t.right(90)
    t.forward(num*25)
    t.left(90)
    for line in range(num):
        t.right(90)
        t.forward(25)
        t.left(90)
        t.forward(500)
        t.backward(1000)
        t.forward(500)
    t.left(90)
    t.forward(num*25)
    t.right(90)


    

t.color('black')
verticalGridline(20)
HorizontalGridline(20)
t.color('blue')
DrawAxis()

print("specify arm length")
print(" ")
a1= 100
a2 = 100
wrong = True
while wrong:
    try:
        a1 = float(input("give the arm1 length"))
        a2 = float(input("give the arm2 length"))
        print(" ")
        print("-"*10)
        wrong = False
    except:
        print("you must give a number")
        print(" ")
        wrong = True
    if a1 ==0 or a2 == 0:
        print("the lengths must be non zero")
        wrong = True


def draw_arm(x,y):
    r = (x**2+y**2)**0.5
    print(r)
    theta1 = 0
    theta2 = 0

    if(r<=(a1+a2) and r>=fabs(a1-a2) and not (x == 0 and y==0)):
        if(x !=0):
            alpha = atan(y/x)
        else:
            if(y >= 0):
                alpha = pi/2
            else:
                alpha = -pi/2

        if(x >0):
            alpha = alpha

        if(x < 0):
            alpha = pi +alpha
            
        theta2 = acos((r*r-a1*a1-a2*a2)/(2*a1*a2))
        beta = asin((a2*sin(theta2))/r)
        theta1 = pi/2-alpha -beta
        #print("done")

        theta1 = degrees(theta1)
        theta2 = degrees(theta2)
        print(theta1)
        print(theta2)
        arm.color("red")
        arm.left(90)
        arm.right(theta1)
        arm.forward(a1)
        arm.right(theta2)
        arm.forward(a2)
    elif(r<=(a1+a2) and r>=fabs(a1-a2) and (x == 0 and y==0)):
        arm.color('red')
        arm.forward(a1)
        arm.backward(a2)
        #print("0,0 ")
    else:
        print("I cant reach that point")
        print(" ")

    

def main():
    while True:
        arm.reset()
        wrong = True
        x = 0
        y = 0
        while wrong:
            try:
                x = float(input("give the x cordinate"))
                y = float(input("give the y cordinate"))
                wrong = False
            except:
                print("you must give me a number")
                print("")
                wrong = True

        draw_arm(x,y)

        status = input("would you like to continue(q to quit and any key to continue)")
        print("")
        if status == "q":
            break
            
    quit()  
            
        
    
        

if __name__ == "__main__":
    main()

    

    


