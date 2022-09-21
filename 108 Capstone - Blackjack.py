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