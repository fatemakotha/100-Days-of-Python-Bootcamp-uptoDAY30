#Modifying GLOBAL scope

players = 1

def increase_players():
  global players #WITHOUT this line if we try to execute += there will ne error, as computer will try to find the players variable inside the function and not end up fining it as it is OUTSIDE the function
  players += 1
  print(f"players inside function: {players}") #prints: 2

increase_players()
print(f"players outside function: {players}") #prints: 2