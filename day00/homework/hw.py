from turtle import *


#we want to paint a house

#step 1: draw a square 
speed(30)
width(5)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)

forward(70)      #height of the door
right(90)

forward(60)
right(90)

forward(70)
end_fill()
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(145)

forward(170)
left(108)
forward(175)
end_fill()


#draw a window
color("black")
penup()
goto(190,160)
pendown()

right(55)
forward(50)
right(-90)
forward(50)
left(90)
forward(50)
right(-90)
forward(50)

#draw 2 nd window

penup()
goto(15,160)
pendown()

right(90)
forward(50)

right(90)
forward(45)

right(90)
forward(50)

right(90)
forward(45)


exitonclick()