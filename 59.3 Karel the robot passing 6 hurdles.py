#GO TO THIS LINK AND PASTE CODE TO SEE HOW IT WORKS:
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def step_topass_each_hurdle():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
def no_of_steps():
    step_topass_each_hurdle()
    step_topass_each_hurdle()
    step_topass_each_hurdle()
    step_topass_each_hurdle()
    step_topass_each_hurdle()
    step_topass_each_hurdle()
no_of_steps() 
#Output: kAREL passes 6 hurdles 