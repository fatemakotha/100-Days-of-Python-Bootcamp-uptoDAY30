#Choosing a random number between 1-100
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
#Function to check user's guess against actual answer
def check_answer(guess, answer):
    if guess > answer:
        print("Too High")
    elif guess < answer:
        print("Too low")
    else:
        print(f"YOU WIN. ANSWER IS {answer}")
        
def set_difficulty():
    level = input("Choose a difficulty easy or hard")
    if level == "easy":
        turns = EASY_LEVEL_TURNS
    else:
        turns = HARD_LEVEL_TURNS
        


print("Welcome to The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1,100)
print(answer)



#Make function to set difficulty

#Let user guess a number
guess = int(input("Make a guess"))
#Function to check user's guess against actual answer

#Track no of turns and reduce by 1 if they get it wrong

#repeating the guessing functionality if they got it wrong