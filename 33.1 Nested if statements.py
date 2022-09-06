number = float(input("Enter a number:"))

if number >= 1500 and number <= 2700:
    if number % 7 == 0 and number % 5 == 0:
            print("Yes")
    else:
            print("No")
else:
    print("No")
    
#If you enter 2 which is outside the range it prints No
#If yoy print 2577 which is in the range and divisible by 5 and 7 it prints Yes