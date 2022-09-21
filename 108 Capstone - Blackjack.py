import random #imports the random function
#PART 1
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """Pick a random card from the deck"""
    card = random.choice(cards)
    return card

#PART 2
user_cards = []
computer_cards = []
for _ in range(0,2): #for two indexes: 0th and 1st
    user_cards.append(deal_card()) #add one card to user cards
    computer_cards.append(deal_card()) #add one card to computer cards
print(f" User cards: {user_cards} and Computer cards: {computer_cards}")
# prints: User cards: [11, 10] and Computer cards: [4, 10]   

# PART 3
def calculate_score(user_cards, computer_cards):
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    # PART 4
    is_game_over = False
    print(f"USER SCORE: {user_score} and COMPUTER SCORE: {computer_score}")
    #prints: USER SCORE: 22 and COMPUTER SCORE: 16
    def repeat():
        while not is_game_over: 
            if 11 in user_cards and 10 in user_cards and len(user_cards) == 2:
                is_game_over = True
                return 0
            if 11 in computer_cards and 10 in computer_cards and computer_cards == 2:
                return 0
            if 11 in user_cards and user_score > 21:
                user_cards.remove(11)
                user_cards.append(1)
                is_game_over = True
            if 11 in computer_cards and computer_score > 21:
                computer_cards.remove(11)
                computer_cards.append(1)
                is_game_over = True
                
            draw_another_card = input("Do you you want to draw another card? Type y for yes and n for no: ")
            if draw_another_card == "n":
                is_game_over = True
            elif draw_another_card == "y":
                user_cards.append(deal_card())
                repeat()
   
calculate_score(user_cards, computer_cards)