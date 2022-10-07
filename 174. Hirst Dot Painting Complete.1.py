import random

import colorgram
import turtle
from turtle import Turtle, Screen
# colorgram.extract(image, number_of_colors)   #Extract colors from an image.....1

# colorgram.Color......2

# A color extracted from an image. Its properties are:
# # Color.rgb - The color represented as a namedtuple of RGB from 0 to 255, e.g. (r=255, g=151, b=210).
# # Color.hsl - The color represented as a namedtuple of HSL from 0 to 255, e.g. (h=230, s=255, l=203).
# # Color.proportion - The proportion of the image that is in the extracted color from 0 to 1, e.g. 0.34.
#
#
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.png', 30) #30 colors extracted
# print(colors)
# # prints: [<colorgram.py Color: Rgb(r=245, g=247, b=251), 81.01821862348179%>,
# # <colorgram.py Color: Rgb(r=252, g=247, b=241), 5.323886639676114%>,
# # <colorgram.py Color: Rgb(r=237, g=241, b=240), 1.7854251012145748%>, .....ETC upto 20 OBJECTS of either RGB or HSL color TUPLES ***
# print("\n")
#
#
# rgb_colors = []
# for each_color in colors: #for EXAMPLE: Color: Rgb(r=245, g=247, b=251)
#     r = each_color.rgb.r #so r = 245
#     g = each_color.rgb.g #so g = 247
#     b = each_color.rgb.b #so b = 251
#     new_color_tuple = (r, g, b) #reated a Tuple
#     rgb_colors.append(new_color_tuple)
#
# print(rgb_colors) #prints: [(47, 17, 4), (177, 15, 1), (210, 70, 14), (7, 25, 69), (241, 221, 0), (227, 145, 94), (116, 177, 203), (28, 105, 172), (236, 229, 100), (4, 55, 12), (207, 135, 12), (223, 77, 47), (32, 126, 62), (127, 31, 49), (160, 177, 165), (221, 112, 157), (16, 46, 135), (25, 188, 94), (233, 87, 92), (151, 214, 199), (243, 223, 234), (60, 79, 0), (64, 39, 68), (71, 131, 212), (203, 40, 46), (0, 159, 208), (0, 82, 106)]

color_list = [(47, 17, 4), (177, 15, 1), (210, 70, 14), (7, 25, 69), (241, 221, 0), (227, 145, 94), (116, 177, 203), (28, 105, 172), (236, 229, 100),
              (4, 55, 12), (207, 135, 12), (223, 77, 47), (32, 126, 62), (127, 31, 49), (160, 177, 165), (221, 112, 157), (16, 46, 135), (25, 188, 94),
              (233, 87, 92), (151, 214, 199), (243, 223, 234), (60, 79, 0), (64, 39, 68), (71, 131, 212), (203, 40, 46), (0, 159, 208), (0, 82, 106)]
screen = Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1) #takes turle to lower left corner of window

print(screen.window_width())
print(screen.window_height())

kotha = Turtle()
turtle.colormode(255)
kotha.speed("fastest")




kotha.penup()
kotha.forward(20)
kotha.pendown()

def row_of_circle():
    for _ in range(10):
        random_color = random.choice(color_list)
        kotha.color(random_color)
        kotha.begin_fill()
        kotha.circle(20)
        kotha.end_fill()
        kotha.penup()
        kotha.forward(70)
        kotha.pendown()

def turn_left():
    kotha.penup()
    kotha.left(90)
    kotha.forward(100)
    kotha.left(90)
    kotha.forward(70)

def turn_right():
    kotha.penup()
    kotha.right(90)
    kotha.forward(20)
    kotha.right(90)
    kotha.forward(70)


row_of_circle()
for _ in range(5):
    turn_left()
    row_of_circle()
    turn_right()
    row_of_circle()


screen.exitonclick()