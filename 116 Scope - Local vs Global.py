#Scope.....................1
players = 1

def increase_players():
  players = 2
  print(f"players inside function: {players}")

increase_players()
print(f"players outside function: {players}")


#Local Scope...............2
def drink_potion():
    potion_strength = 2 #has GLocal Scope as it is defined inside a function
    print(potion_strength)
drink_potion() #prints: 2
# print(potion_strength)
#gives error: NameError: name 'potion_strength' is not defined

#Global Scope..............3
player_health = 10 #has Global Scope as it is defined at the top of the file outside any function
def have_potion():
    potion_agility =  2 #has GLocal Scope as it is defined inside a function
    print(player_health)
have_potion() #prints: 10