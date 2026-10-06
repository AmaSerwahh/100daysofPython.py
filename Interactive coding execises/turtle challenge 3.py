from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["red", "yellow", "blue", "green", "purple"]

for side in range(3, 11):
    angle = 360 / side
    tim.color(random.choice(colors))
    for _ in range(side):
        tim.forward(100)
        tim.right(angle)


screen = Screen()
screen.exitonclick()