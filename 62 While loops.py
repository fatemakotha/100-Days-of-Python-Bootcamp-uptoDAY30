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

number_of_hurdles = 6 #as there are 6 hurdles
while number_of_hurdles > 0: #when number_of_hurdles > 0, carry out the two lines below:
    jump()
    number_of_hurdles -= 1# every time it jumps, number_of_hurdles decreases by 1
    print(number_of_hurdles) #prints: 5, then 4, then 3, then 2, then 1, then 0