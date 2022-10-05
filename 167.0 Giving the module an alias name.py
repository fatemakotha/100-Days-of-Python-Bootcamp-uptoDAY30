# Giving the module an alias name
import turtle as t # imports the Turtle as t, shortening the name*** 

#Create a new Turtle OBJECT named cutu_the_turtle
cutu = t.Turtle() #***



# print(cutu_the_turtle) #window opens but dissapears
cutu.shape("turtle") #makes the arrow change into a turtle
cutu.color("dark cyan")

#How to make the object do certain things/FUNCTIONS
for _ in range(4):
    cutu.forward(100) #moves forward by a 100 paces
    cutu.left(90.0) #turns right by 90 degress











screen  = Screen()
screen.exitonclick() #makes the window stay longer #THIS NEEDS TO BE AT THE END OF THE CODE *