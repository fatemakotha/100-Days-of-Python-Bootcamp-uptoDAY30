# Fix the Errors
# age = input("How old are you?") #cannot print because age is an STRING and the 18 is an integer.
age = int(input("How old are you?"))
if age > 18:
# print("You can drive at age {age}.") #no indentation before print statement
    print("You can drive at age {age}.") #prints: You can drive at age {age}. This is because we did NOT USE an f-string
    print(f"You can drive at age {age}.") #prints: You can drive at age 22.