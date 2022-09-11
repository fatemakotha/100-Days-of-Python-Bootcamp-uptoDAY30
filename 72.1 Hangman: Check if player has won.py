#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
    
end_of_game = False #meaning not end of game
while not end_of_game : #while not False:
    
    guess = input("Guess a letter: ").lower()
    
    for position in range(len(chosen_word)): #if chosen word is camel, range is 0-4
        letter = chosen_word[position] #i.e. letter is the chosen word's 0th index #defining letter variable
        if letter == guess: #if letter is equal to guess, i.e. c=c, then:
            display[position] = letter #replace the display's position 0 with the letter c
            print(display) #prints: ['_', '_', '_', '_', 'l']
        # print(display) if unindented prints the following:
        # ['_', '_', '_', '_', '_', '_', '_', '_']
        # ['_', '_', '_', '_', '_', '_', '_', '_']
        # ['_', '_', '_', '_', '_', '_', '_', '_']
        # ['_', '_', '_', '_', '_', '_', '_', '_']
        # ['_', '_', '_', '_', '_', '_', '_', '_']
        # ['_', '_', '_', '_', '_', '_', '_', '_']
        # ['_', '_', '_', '_', '_', '_', '_', '_']
        # ['_', '_', '_', '_', '_', '_', '_', 'k']

if "_" not in display:
    print("You have won")