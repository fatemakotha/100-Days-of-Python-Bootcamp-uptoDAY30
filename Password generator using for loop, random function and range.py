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
password = ""
#assume nr_letters = 4
for char in range(1, nr_letters + 1): #the range is 4, including 4, but if we use only nr_letters that does not include 4, thus we add 1, to make it include 4
    random_char = random.choice(letters)
    password += random_char #starts with nothing as password = "", then keeps adding letters as string oncatenation
print(password)

#assume nr_numbers = 2
for char in range(1, nr_numbers + 1): #the range is 2, including 4, but if we use only nr_letters that does not include 4, thus we add 1, to make it include 4
# *** THE CODE BELOW SIMPLIFIES WHAT WE DID FOR LETERS
    password += random.choice(numbers) #starts with nothing as password = "", then keeps adding letters as string oncatenation
print(password)


#assume nr_symbols = 2
for char in range(1, nr_symbols + 1): #the range starts from 0 and ends at 4, including 4, but if we use only nr_letters that does not include 4, thus we add 1, to make it include 4
 # ***THE CODE BELOW SIMPLIFIES WHAT WE DID FOR LETERS
    password += random.choice(symbols) #starts with nothing as password = "", then keeps adding letters as string oncatenation
print(password)

#prints:
# Welcome to the Python Password Generator!
# How many letters would you like in your password?
# 4
# How many symbols would you like?
# 2
# How many numbers would you like?
# 2
# sNea
# sNea94
# sNea94&)
