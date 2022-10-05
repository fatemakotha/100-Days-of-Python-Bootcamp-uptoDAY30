from turtle import Turtle, Screen # imports the Turtle and Screen class that's inside the turtle module

#Create a new Turtle OBJECT named cutu_the_turtle
cutu = Turtle()
# print(cutu_the_turtle) #window opens but dissapears
cutu.shape("turtle") #makes the arrow change into a turtle
cutu.color("dark cyan")

#How to make the object do certain things/FUNCTIONS ***

#TO DRAW AN EQUILATERAL TRIANGLE WITH SIDES 100:
for _ in range(3):
    cutu.pencolor("cyan")
    cutu.forward(100)
    cutu.right(90)
    cutu.right(30) #inside angle is 60degrees, so 90-60 = 30degrees

#TO DRAW AN SQUARE WITH SIDES 100:
for _ in range(4):
    cutu.pencolor("red")
    cutu.forward(100)
    cutu.right(90)

#TO DRAW AN PENTAGON WITH SIDES 100:
for _ in range(5):
    cutu.pencolor("green")
    cutu.forward(100)
    cutu.right(90)
    cutu.left(18) #each interior angle is 108degrees so 108-90 = 18degrees

#TO DRAW AN HEXAGON WITH SIDES 100:
for _ in range(6):
    cutu.pencolor("purple")
    cutu.forward(100)
    cutu.right(90)
    cutu.left(30) #each interior angle is 120degrees so 120-90 = 30degrees

#TO DRAW AN HEPTAGON WITH SIDES 100:
for _ in range(7):
    cutu.pencolor("pink")
    cutu.forward(100)
    cutu.right(90)
    cutu.left((900 / 7) - 90) #each interior angle is 900/7 degrees so (900/7)-90 = 38.57142857....

#TO DRAW AN OCTAGON WITH SIDES 100:
for _ in range(8):
    cutu.pencolor("yellow")
    cutu.forward(100)
    cutu.right(90)
    cutu.left(45) #each interior angle is 135degrees so 135-90 = 45degrees

#TO DRAW AN NONAGON WITH SIDES 100:
for _ in range(9):
    cutu.pencolor("black")
    cutu.forward(100)
    cutu.right(90)
    cutu.left(50) #each interior angle is 135degrees so 140-90 = 50degrees

#TO DRAW AN DECAGON WITH SIDES 100:
for _ in range(10):
    cutu.pencolor("blue")
    cutu.forward(100)
    cutu.right(90)
    cutu.left(54) #each interior angle is 144degrees so 144-90 = 54degrees










screen  = Screen()
screen.exitonclick() #makes the window stay longer #THIS NEEDS TO BE AT THE END OF THE CODE *