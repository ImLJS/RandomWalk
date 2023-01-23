import turtle
from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup


tim = Turtle()
tim.width(5)
turtle.colormode(255)

angles = [0, 90, 180, 270]

for _ in range(50):
    tim.setheading(random.choice(angles))
    tim.color(random_color())
    tim.forward(20)

screen = Screen()
screen.exitonclick()
