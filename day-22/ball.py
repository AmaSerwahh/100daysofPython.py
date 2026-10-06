from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.shapesize(.7, .7)
        self.penup()
        self.x = 10
        self.y = 10
        self.speed_up = 0.1

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.speed_up *= 0.99

    def reset_ball(self):
        self.goto(0, 0)
        self.speed_up = 0.1
        self.bounce_x()

