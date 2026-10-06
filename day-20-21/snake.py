import turtle
from turtle import Turtle
class Snake:

    def __init__(self):
        self.segments = []
        self.x = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(3):
            self.add_segment()

    def add_segment(self):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(self.x, 0)
        self.x -= 20
        self.segments.append(turtle)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(self.segments[-1].position())
        self.segments.append(turtle)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)
