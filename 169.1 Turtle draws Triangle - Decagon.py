from turtle import Turtle, Screen # imports the Turtle and Screen class that's inside the turtle module

#Create a new Turtle OBJECT named cutu_the_turtle
cutu = Turtle()
# print(cutu_the_turtle) #window opens but dissapears
cutu.shape("turtle") #makes the arrow change into a turtle
cutu.color("dark cyan")

#How to make the object do certain things/FUNCTIONS ***
def draw_shape(num_sides): #takes in num_sides = no_of_sides which is 3, 4, 5 ,6 ....11
    interior_angle = 360 / num_sides
    for _ in range(num_sides):
        cutu.forward(100)
        cutu.right(interior_angle)


for no_of_sides in range(3, 11):
    draw_shape(no_of_sides) #no_of_sides: 3, 4, 5 ,6 ....11










screen  = Screen()
screen.exitonclick() #makes the window stay longer #THIS NEEDS TO BE AT THE END OF THE CODE *