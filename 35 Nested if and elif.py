# Small pizza = 15
# Medium pizza = 20
# Large pizza - 25

# Pepperoni for small pizza = 2
# Pepperoni for farge pizza = 3

# Extra cheese for any size pizza = 1

print("Welcome to Pizza Delivery!")
size = input("Input your desired size: S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y o N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0 #consider the initial billl to be zero

#task one is to ask for the size #NOT NESTED
if size == "S":
    bill += 15 #we add 15 to the initial bill which was 0
elif size == "M":
    bill += 20 #we add 20 to the initial bill which was 0
else:
    bill += 25 #we add 25 to the initial bill which was 0

#task 2 is to ask whether they want pepperoni #NOT NESTED
if add_pepperoni == "Y":
 if size == "S": #nested
     bill += 2 #adds 2 dollars to the bill #nested
 else: #nested
     bill += 3 #adss 3 dollars to the bill #nested

#task 3 is to ask if they want extra cheese #NOT NESTED
if extra_cheese == "Y":
    bill += 1
#last task is to show the final bill #NOT NESTED
print(f"Your final fill is {bill}.")