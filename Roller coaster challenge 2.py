print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:#_______1
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
        
    pic = input("Do you want a picture? Y or N.")
    if pic == "Y": #add $3 to their bill
        bill += 3 # this means bill= bill + 3
        
        print(f"You final bill is {bill}.")
        
    
else:
    print("Sorry, you have to be taller to be able to ride.")#_______1