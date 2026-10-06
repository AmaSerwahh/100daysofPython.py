from turtle import Turtle
import random

COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class Car:

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        lucky_car = random.randint(1,6)
        if lucky_car == 3:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y = random.randint(-240, 240)
            new_car.goto(300, y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT




