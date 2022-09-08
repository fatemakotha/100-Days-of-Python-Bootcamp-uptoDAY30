#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = 0
for letter in letters:
    letter = random.choice(letters)
    letter1 = random.choice(letters)
    letter2 = random.choice(letters)
    letter3 = random.choice(letters)
print(letter,letter1,letter2,letter3)

number = 0
for number in numbers:
    number = random.choice(numbers)
    number1 = random.choice(numbers)
print(number, number1)

symbol = 0
for symbol in symbols:
    symbol = random.choice(symbols)
    symbol1 = random.choice(symbols)
print(symbol, symbol1)

password = (letter+letter1+letter2+letter3+number+number1+symbol+symbol1)
random_password = random.choice(password)
print(password) #prints Gziq87&) or MOUF77(+ etc. This is in the form 4letters, 2numbers and then 2symbols