#use range(), if and elif
print("Welcome to FizzBuzz!")
for number in range(1,101):#range is between 1 and 101, not including 101
    if number % 3 == 0 and number % 5 == 0:#if number is divisible by 3 and five, replace number by "FizzBuzz"
        number = "FizzBuzz"
        print(number)
    elif number % 3 == 0:#if number is divisible by 3, replace number by "Fizz"
        number = "Fizz"
        print(number)
    elif number % 5 == 0:#if number is divisible by 5 replace number by "Buzz"
        number = "Buzz"
        print(number)
    else: #if none of the above conditions apply, then print the original number
        print(number)