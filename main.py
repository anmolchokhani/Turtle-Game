from gc import is_tracked
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Whats you bet", prompt="Which turtle do you want to bet on? ")
print(bet)

colors= ["red", "orange", "yellow", "green", "blue"]

turtle_object=[]
t=0



for i in range(len(colors)):
    all_turtle= Turtle(shape="turtle")
    all_turtle.penup()
    all_turtle.color(colors[i])
    all_turtle.goto(x=-230 , y=-100 + t)
    t +=50
    turtle_object.append(all_turtle)


if bet:
    is_race_on=True

while is_race_on:
    for turtle in turtle_object:
        if turtle.xcor()> 230:
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print("You have won")
            else:
                is_race_on = False
                print(f"You lost, Winner is {winning_color} Turtle")
        turtle.forward(random.randint(0,10))
    





screen.exitonclick()