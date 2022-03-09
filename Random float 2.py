import random # to use the random function we need to import it

#0.00000000 - 0.99999999
random_float = random.random()# prints a float between 0 and 1

#how to get number between 0-5?
random_float_zero_to_five = random_float * 5#0.00000000 - 4.99999999 NOT INCLUDING 5!!
print(random_float_zero_to_five)