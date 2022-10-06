import random
import turtle
from turtle import Turtle,Screen

kotha = Turtle()
kotha.pencolor("blue")
kotha.speed("fastest")
kotha.circle(80) #creates a circle with radius 80
turtle.colormode(255)


def random_color(): #returns a random color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color




for _ in range(1, 80):
    kotha.color(random_color()) #picks a random color
    kotha.left(5) #shift direction to the left by 5 degrees
    kotha.circle(80) #draws a circle with radius 80



screen = Screen()
screen.exitonclick()