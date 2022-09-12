#Write your code below this line 👇
import math

# number_of_cans = round((test_h * test_w) / coverage)
def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover) #to round up you need to import math and call ceil function
    print(f"You'll need {number_of_cans}")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage) #calls the paint_calc function and prints:
# Height of wall: 5
# Width of wall: 20
# You'll need 20
# > 