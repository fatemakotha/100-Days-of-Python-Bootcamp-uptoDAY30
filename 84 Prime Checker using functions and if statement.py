#Prime Number checker:
def prime_checker(number):
    if number % 1 == 0 and number % number == 0:
        if number % 2 == 0:
            print(f"{n} is a Not a Prime Number")
        else:
            print(f"{n} is a Prime Number")
   


n = int(input("Check this number: ")) 
prime_checker(number=n)
#when input is 8
#prints:
# Check this number: 8
# 8 is a Not a Prime Number

#when input is 5
#prints:
# Check this number: 5
# 5 is a Prime Number
