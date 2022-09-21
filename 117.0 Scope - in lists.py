#EX - 1
game_level = 3
enemies = ["skeletons", "zombies", "alien"]

if game_level < 5:
    new_enemy = enemies[0]
    
print(new_enemy) #prints: skeletons



#EX - 2
game_level = 3
def game():
    enemies = ["skeletons", "zombies", "alien"]
    if game_level < 5:
        new_enemy = enemies[0]
        
print(new_enemy) #NameError: name 'new_enemy' is not defined
#This is because WITHIN the function, there is LOCAL scope