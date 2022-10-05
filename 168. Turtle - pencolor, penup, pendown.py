#Turtle - pencolor, penup, pendown:

from turtle import Turtle, Screen # imports the Turtle and Screen class that's inside the turtle module

#Create a new Turtle OBJECT named cutu_the_turtle
cutu = Turtle()
# print(cutu_the_turtle) #window opens but dissapears
cutu.shape("turtle") #makes the arrow change into a turtle
cutu.color("dark cyan")

#How to make the object do certain things/FUNCTIONS
for _ in range(100):
    cutu.pencolor("black") #changes the color of the drawing pen
    cutu.forward(2) #moves forward by 2 paces
    cutu.penup() #is used to stop the drawing.
    cutu.forward(2) #moves forward by 2 paces
    cutu.pendown() #is used to continue the drawing.