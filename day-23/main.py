import time
from turtle import Screen
from player import Player
from score import Score
from car import Car

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Score()
car = Car()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    for x in car.all_cars:
        if x.distance(player) < 20:
            game_on = False
            score.game_over()

    if player.ycor() >= 280:
        score.increase_point()
        player.finish()
        car.increase_speed()

screen.exitonclick()
