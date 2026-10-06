from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
tim.speed("fastest")
tim.hideturtle()

turtle.colormode(255)
colour_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

def draw_dots():
    for _ in range(9):
        color = random.choice(colour_list)
        tim.dot(20, color)
        tim.penup()
        tim.fd(50)
        tim.dot(20, color)

tim.penup()
tim.goto(-300, -200)

a = 10
while a > 0:
    y = tim.ycor()
    draw_dots()
    a -= 1
    tim.goto(-300, y + 50)

screen = Screen()
screen.exitonclick()


#import colorgram
#
#rgb_colors = []
#colors = colorgram.extract("image.jpg", 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    rgb = (r, g, b)
#    rgb_colors.append(rgb)

#print(rgb_colors)