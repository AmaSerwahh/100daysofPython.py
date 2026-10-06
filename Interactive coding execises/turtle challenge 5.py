import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed("fastest")

turtle.colormode(255)
def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(36):
    tim.color(colors())
    tim.circle(100)
    tim.seth(tim.heading() + 10)


screen = Screen()
screen.exitonclick()

