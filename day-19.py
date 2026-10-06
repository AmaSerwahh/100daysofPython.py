from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput(title="Place your bet", prompt="Which color turtle will win the race?")
colours = ["red", "blue", "green", "yellow", "purple", "orange"]

all_turtles = []
game_on = True

y = -120
for _ in range(6):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(colours[_])
    turtle.goto(-230, y)
    y = turtle.ycor() + 50
    all_turtles.append(turtle)

while game_on:
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == guess:
                print(f"You win! The {winner} turtle is the winner🥳🥳")
            else:
                print(f"You lose! The {winner} turtle is the winner😔💀")
            game_on = False


screen.exitonclick()