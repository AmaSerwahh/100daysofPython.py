import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):

        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-250, 260)
        y = random.randint(-250, 260)
        self.goto(x, y)
