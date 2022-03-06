print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:#_______1
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5")
    elif age <= 18:
        print("Youth tickets are $7")
    else:
        print("Adult tickets are $12")
else:
    print("Sorry, you have to be taller to be able to ride.")#_______1