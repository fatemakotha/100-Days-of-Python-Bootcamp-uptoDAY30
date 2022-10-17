import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("US States Game")

image = "blank_states_img - Copy.gif"

screen.addshape(image) #adding a shape to turtle
turtle.shape(image) #using that shape

#THIS FUNCTION PRINTS COORDINATES OF THE MOUSE POINTER WHEN MAP IS CLICKED: ****
def get_mouse_click_coor(x, y): #returns x and y coordinates
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop() #keeps our screen open even though code has stopped running

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,****