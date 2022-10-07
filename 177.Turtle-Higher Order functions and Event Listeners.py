import turtle
from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)




screen.listen() #starts listening
screen.onkey(key="space", fun=move_forwards) #calls the move forward function when spacebar is hit






screen.exitonclick()