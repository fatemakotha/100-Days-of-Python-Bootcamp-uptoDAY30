# PUT THE CODE IN THE LINK BELOW AND TRY IT OUT:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
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
    
    
#EITHER: While loop
#While loops are good when you don't care about a specific item, you simply want to carry out one functionality many times
while at_goal() != True: #while at goal is not equal to True, take the following steps:
    jump()
    
    
#.......OR......:

#for loops are great when you want o iterate or need to do something with each element
#for loops are great when using a range
for step in range(6): 
    jump()