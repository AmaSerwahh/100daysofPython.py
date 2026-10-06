from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed("fast")
tim.pensize(10)

colors = ["red", "orange", "yellow", "blue", "green", "purple"]
angles = [0, 90, 180, 270]

while True:
    tim.color(random.choice(colors))
    tim.forward(50)
    tim.seth(random.choice(angles))


screen = Screen()
screen.exitonclick()
