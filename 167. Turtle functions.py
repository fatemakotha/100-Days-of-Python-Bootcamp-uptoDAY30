from turtle import * #the asterisk * imports everything that's inside the turtle module

#Create a new Turtle OBJECT named cutu_the_turtle
cutu = Turtle()
# print(cutu_the_turtle) #window opens but dissapears
cutu.shape("turtle") #makes the arrow change into a turtle
cutu.color("dark cyan")

#How to make the object do certain things/FUNCTIONS
for _ in range(4):
    cutu.forward(100) #moves forward by a 100 paces
    cutu.left(90.0) #turns right by 90 degress











screen  = Screen()
screen.exitonclick() #makes the window stay longer #THIS NEEDS TO BE AT THE END OF THE CODE *