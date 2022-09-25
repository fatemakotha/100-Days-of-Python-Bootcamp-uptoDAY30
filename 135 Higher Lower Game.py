import random
from art import logo, vs
print(logo)
from replit import clear

# print(vs)
from game_data import data
# # print(data)
# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },

#Format the data:
def format_data(account): #re-use it to format for account a and b
    """Taked the account data and returns printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"


#check if user is correct:
def check_answer(guess, a_followers, b_followers):
    """Take the user's guess and the follower counts of a and b and return if user is correct"""
    if a_followers > b_followers:
        return guess == "a" #if gues === a then it will return True but                             if gues != a it will return False
    else:
        return guess == "b" #if gues === b then it will return True but                             if gues != b it will return False
        




account_b = random.choice(data)#picks one entry from the data list

score = 0
game_should_continue = True
#While loop to repeat game:
while game_should_continue:
    # Generate a random account from the game data:
    account_a = random.choice(data) #picks one entry from the data list
    if account_a == account_b: #incase both the picked entry is same 
        account_b = random.choice(data)
    
    print(f"Compare A: {format_data(account_a)}") #format_data returns "name", "description" and "country" for account_a
    print(vs)
    print(f"Against B: {format_data(account_b)}") #format_data returns "name", "description" and "country" for account_b
    
    # #Format the account data into printable format
    # account_name = account_a["name"]
    # account_descr = account_a["description"]
    # account_country = account_a["country"]
    # print(f"{account_name}, a {account_description} from {account_country}")
    
    #Ask the user for a guess:
    guess = input("Who has more folllowers? Type 'A' or 'B': ").lower()
    
    #Check if user is correct:
    ##Get follower count of each account 
    a_follower_count = account_a["follower_count"] #pulls the value of "follower_count" from account_a 
    b_follower_count = account_b["follower_count"] #pulls the value of "follower_count" from account_b
    is_correct = check_answer(guess, a_follower_count, a_follower_count) #Returns True or False
    
    
    #Give user some feedback on guesses:
    if is_correct:
        score += 1
        #clear screen in between rounds:
        clear()
        print(logo)
        print(f"You're right, you're score is {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Your final score is {score}")