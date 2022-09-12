import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print("HELLO! WELCOME TO HANGMAN!")
words_list = ["camel", "rat", "dog"]
chosen_word = random.choice(words_list)
print(chosen_word)
len_of_chosen_word = len(chosen_word)
lives = 6

display = []
for number_of_gaps in chosen_word:
    display += "_"
    print(display)
    
end_of_game = False

while not end_of_game: #while not False
    guess = input("Enter a letter: ").lower()
    print(guess)
    for position in range(len_of_chosen_word):
        letter = chosen_word[position] #letter is assigned the letter from the chosen word dog[0] which is D
        if letter == guess:
            display[position] = guess
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True #end_of_game happens once when all lives are lost
            print("You Lose!")
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True #end_of_game happens AGAIN when display if full and player wins
        print("You win")
        
    print(stages[lives]) #lets say we have 3 lives, print(stage[3]), which is:
#     '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# ========='''