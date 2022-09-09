# PUT THE CODE IN THE LINK BELOW AND TRY IT OUT:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#EITHER:
for step in range(0,6): #the range is 0-6, and in case of normal code 0-7, as the last index of a range is not included
    jump() #carries out jump 6 times
#.....OR.....
for step in range(6):#the range is 6, and in case of normal code 7, as the last index of a range is not included
    jump() #carries out jump 6 times



#Output: kAREL passes 6 hurdles 