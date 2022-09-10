# PUT THE CODE IN THE LINK BELOW AND TRY IT OUT:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    #move() # our jump functions moves forwar fist befoe jumping, so in this case we need to remove that one steo
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal(): 
    if wall_in_front():
        jump()
    else:
        move()