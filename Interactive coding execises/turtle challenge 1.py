from turtle import Turtle, Screen

tim = Turtle()

for _ in range(10):
    tim.forward(20)
    tim.penup()
    tim.forward(20)
    tim.pendown()

screen = Screen()
screen.exitonclick()