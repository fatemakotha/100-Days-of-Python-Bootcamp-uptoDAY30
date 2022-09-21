#Modifying GLOBAL scope

players = 1

def increase_players():
# global players     Intead of tapping into global variables to modify them. do this using the return statement:
  print(f"players inside function: {players}") #prints: 1   
  return players + 1 #returns 1+1 which is 2
  

players = increase_players() #you get hold of the output of increase_players() and save it to the GLOBAL variable "players". The result of 2 is now assigned to the variable "players"
print(f"players outside function: {players}") #prints: 2