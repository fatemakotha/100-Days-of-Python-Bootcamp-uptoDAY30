print("Welcome to Pizza Delivery!")
size = input("Input your desired size: S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y o N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0 #consider the initial billl to be zero

if size == "S":
    bill += 15 #we add 15 to the initial bill which was 0
elif size == "M":
    bill += 20 #we add 20 to the initial bill which was 0
else:
    bill += 25 #we add 25 to the initial bill which was 0
    
if add_pepperoni == "Y":
 if size == "S":
     bill += 2
 else:
     bill += 3
    
if extra_cheese == "Y":
    bill += 1
print(f"Your final fill is {bill}.")