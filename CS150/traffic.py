#Billy Boone
#CS150
#This program simulates a traffic light and is activated with the space key

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgrey")
bo = turtle.Turtle()
bo.speed(0)
bo.penup()
bo.goto(0,200)



def draw_light():
    bo.fillcolor("darkblue")   # Create traffic light
    bo.begin_fill()
    for i in range(2):
        bo.forward(100)
        bo.right(90)
        bo.forward(360)
        bo.right(90)
        bo.forward(100)
    bo.end_fill()
    
    bo.fillcolor("green")
    bo.shape("circle")   # Create the turtle as a light bulb
    bo.shapesize(5)
    bo.goto(0,125)
    


# This variable holds the current state of the machine (0, 1, 2)
lightState = 0

def light_green():
    global lightState  # Globalize lightState variable for entire program
    bo.goto(0,125) #start location for green light
    if lightState == 0:      # Set turtle at green
       bo.fillcolor("green")
       lightState += 1  #increment lightState
    wn.ontimer(light_yellow, 5000) #after 5 seconds run light_yellow

def light_yellow():
    global lightState
    bo.goto(0,25) #move to location for yellow light to appear
    if lightState == 1:
        bo.fillcolor("yellow")
        lightState += 1
    wn.ontimer(light_red, 2000) #after 2 seconds run light_red

def light_red():
    global lightState
    bo.goto(0,-75)
    if lightState == 2:
        bo.fillcolor("red")
        lightState = 0
    
    wn.ontimer(light_green, 5000) #after 5 seconds restart to light_green

def start_timer():
    wn.ontimer(light_green, 500) #offset lightgreen from draw_light to maintain correct location


    

wn.onkey(draw_light, "space") #when space call draw_light
wn.onkeypress(start_timer, "space") #when space pressed simultaneously call start_timer

wn.listen()  # Listen for events
wn.mainloop()

