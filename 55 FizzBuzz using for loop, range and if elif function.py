#When a number is divisible by 3, it should print "Fizz" instead of the number
#When a number is divisible by 5, it should print "Buzz" instead of the number
#When a number is divisible by 3 and 5, it should print "Fizz Buzz" instead of the number
#Numbers should be 1-20 

total = 0
for number in range(1, 21):
    if number % 3 == 0 and number % 5 == 0: # *** This statement goes first because otherwise it will check for if number % 3 == 0 or number % 5 == 0 and print "Fizz" or "Buzz" and there will be nothing left for to check for if number % 3 and number % 5 == 00 which will give "Fizz Buzz"
        number = ("Fizz Buzz")
        print(number)
    elif number % 5 == 0:
        number = ("Buzz")
        print(number)
    elif number % 3 == 0: 
        number = ("Fizz")
        print(number)
    else: 
        print(number)
        
#prints
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# Fizz Buzz
# 16
# 17
# Fizz
# 19
# Buzz