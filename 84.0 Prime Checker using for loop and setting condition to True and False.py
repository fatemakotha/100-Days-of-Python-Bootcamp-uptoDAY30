#Prime Number checker:
def prime_checker(number):
#if number = 7, we want to check 7/2 = ?, 7/3 = ?, ......7/7 = ? 

    is_prime = True #set to True
    for i in range(2, number): #range starts from two and ends at i, if i is 7, range ends at 6
        if number % i == 0:
            is_prime = False #if divisible then set to False
    if is_prime: #if True
        print("It is a prime number")
    else:
        print("Not a prime number")
   


n = int(input("Check this number: ")) 
prime_checker(number=n)