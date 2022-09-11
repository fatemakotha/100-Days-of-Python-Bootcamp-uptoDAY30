#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list) #lets say it picks camel

#Testing code
print(f'Pssst, the solution is {chosen_word}.') #prints: camel

display = [] #set display variable to an empty list
for _ in range(len(chosen_word)): #we aren't doing anything with the _ thus it needs no name #range is 0-4 as length of camel is 5
    display += "-" #display keeps adding blanks as many letters are there in the chosen word
print(display)
    
guess = input("Guess a letter: ").lower() #lets say L, then L is converted to l



for position in range(len(chosen_word)): #range 0-4
#when postion is 0, then its going to go to the next line and put 0 there as the position
    letter = chosen_word[position] # letter = camel[0] whic is letter = c #letter = chosen word at the current position: camel[0], camel[1], camel[2], camel[3], camel[4], 
    if letter == guess: #a = a  #camel[0] = c, camel[1], camel[2], camel[3], camel[4],
        display[position] = letter #display[0] = a 
        #letter is c, and that is at display position 0, thus display is now ['c', '-', '-', '-', '-']
        
        
print(display)