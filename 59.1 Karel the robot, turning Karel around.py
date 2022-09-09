# PUT THE CODE IN THE LINK BELOW AND TRY IT OUT:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

move()
move()
turn_around()
move()
move()
turn_around()
turn_right()
#OUTCOME: moves 2 steps, turn_around(turns left and turns left again), moves 2 steps, turn_around(turns left and turns left again), turn_right(turns right 3 times)