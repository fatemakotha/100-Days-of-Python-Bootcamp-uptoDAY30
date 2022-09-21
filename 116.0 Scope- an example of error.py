player_health = 10 #has Global Scope as it is defined at the top of the file outside any function
def game(): 
    def have_potion(): #this function is now inside ANOTHER function
        potion_agility =  2 #has Local Scope as it is defined inside a function
        print(player_health)
# have_potion() #prints: NameError: name 'have_potion' is not defined

# game() #prints: NOTHING