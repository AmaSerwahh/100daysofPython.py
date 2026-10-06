from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()

screen.onkey(r_pad.up, "Up")
screen.onkey(r_pad.down, "Down")

screen.onkey(l_pad.up, "w")
screen.onkey(l_pad.down, "s")

game_on = True
while game_on:
    time.sleep(ball.speed_up)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_point()

screen.exitonclick()
