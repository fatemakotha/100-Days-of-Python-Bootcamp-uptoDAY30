#Modifying GLOBAL scope

players = "Aliens"

def increase_players():
  players = "Locals" #we are NOT changing the 1st variable named players. We are MAKING A NEW VARIABLE named players with a LOCAL SCOPE***
  print(f"players inside function: {players}") #prints: Locals

increase_players()
print(f"players outside function: {players}") #prints: Aliens

#IT IS A BAD IDEA TO NAME THE LOCAL AND GLOBAL VARIABLES USING THE EXACT SAME NAME
    