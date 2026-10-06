from turtle import Turtle

FONT = ("Courier", 16, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_point(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

