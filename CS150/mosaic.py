#Billy Boone
#CS150
#03/23
#This is a program that imports the Turtle module and creates
# 16 tiles with different colors

import turtle
import random


wn = turtle.Screen()       
bo = turtle.Turtle()
wn.bgcolor("grey")
bo.penup()
bo.goto(-100,100)
bo.pendown()
bo.pensize(5)
bo.speed("fastest")

colors = ["darkblue", "silver", "darkgreen"] #list of colors to choose from 


for i in range(16):
    color = random.choice(colors) #choose random color for block
    bo.color(color)
    bo.begin_fill()

    
    for j in range(4): #draw intitial square and fill
        bo.forward(50)
        bo.right(90)

    bo.end_fill()
    
    for j in range(4): #draw square  pattern
        bo.color("black")
        bo.forward(40)
        bo.right(90)
    
        
    if i == 3 or i == 7 or i == 11 or i == 15: #conditional for new line
        bo.penup()
        bo.backward(180)
        bo.right(90)
        bo.forward(60)
        bo.left(90)
        bo.pendown()
    else:
        bo.penup()
        bo.forward(60)
        bo.pendown()

bo.hideturtle()
        


wn.exitonclick()


