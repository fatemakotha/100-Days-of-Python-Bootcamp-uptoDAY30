#NESTED if /else
print("Welcome to the rollercoaster!")
height = int(input("Enter your height in m: "))

if height >=120:
    print("You can ride")
    age = int(input("Input your age: "))
    if age >= 18:
        print("$12")
    else:
        print ("$7")
        
else:
    print("Sorry,you did not reach desired height level")