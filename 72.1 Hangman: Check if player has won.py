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
end_of_game = False
while not end_of_game : #which means while end_of_game is False, which mean while not at end
    guess = input("Guess a letter: ").lower()
    
    #Check guessed letter
    for position in range(word_length): ##if chosen word is camel, range is 0-4
        letter = chosen_word[position] # #i.e. letter is the chosen word' 0th index
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess: #if letter is equal to guess, i.e. c=c, then:
            display[position] = letter ##replace the display's position 0 with the letter c
    
    print(display)
        #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display: #when there is no _ in display we set the game to end:
        end_of_game = True #game has ended
        print("You have won")