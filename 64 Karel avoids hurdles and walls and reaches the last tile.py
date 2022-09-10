# PUT THE CODE IN THE LINK BELOW AND TRY IT OUT:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def jump():
    if wall_in_front():
        turn_left()
        move()
        turn_right()
    elif right_is_clear():
        move()
    else:
        turn_right()
        
while not at_goal():
    jump()