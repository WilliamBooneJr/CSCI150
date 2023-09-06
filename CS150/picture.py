#Billy Boone
#cs150
#04/01/23
#This is a program that draws pictures using functions


import turtle


wn = turtle.Screen()
wn.setup(500,500)
wn.bgcolor("light blue")

bo = turtle.Turtle()
bo.pensize(5)
bo.speed("fastest")
bo.penup()
bo.goto(-50,-50)
bo.pendown()  #setup turtle


def movebo(x, y): #function for moving mouse to click location
    bo.penup()
    bo.goto(x, y)
    bo.pendown()

def redflower():  #function for redflower
   bo.pencolor("red")
   bo.fillcolor("pink")
   bo.begin_fill()
   for i in range(12):
       bo.circle(25, 70)
       bo.left(110)
       bo.circle(25, 70)
   bo.end_fill()
def drawlavender():  #function for lavender flower
    bo.pencolor("blue")
    bo.fillcolor("lavender")
    bo.begin_fill()
    for i in range(5):
        bo.forward(50)
        bo.right(90)
    bo.end_fill()
    bo.right(90)
    bo.forward(50)
    bo.left(90)
    bo.forward(25)
    bo.circle(20)
    bo.end_fill()
def whiteflower():  #function for white flower
    bo.pencolor("white")
    bo.fillcolor("white")
    bo.begin_fill()
    for i in range(12):
        bo.forward(25)
        bo.backward(25)
        bo.right(30)
    bo.end_fill()

def sun():  #function for sun
    bo.color("orange", "yellow")
    bo.begin_fill()
    for i in range(36):
        bo.forward(150)
        bo.left(170)
    bo.end_fill()

def stem():  #function for stem(set orientation to vertical prior to forward)
    bo.color("green")
    bo.setheading(90)
    bo.forward(75)
    
    

wn.onclick(movebo) #onclick listener for move mouse function
wn.onkey(redflower, "1") #onkey listeners for flower functions
wn.onkey(drawlavender, "2")
wn.onkey(whiteflower, "3")
wn.onkey(sun, "s")
wn.onkey(stem, "t")

wn.listen()
wn.mainloop

    


    
