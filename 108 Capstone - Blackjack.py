import random #imports the random function

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """Pick a random card from the deck"""
    card = random.choice(cards)
    return card