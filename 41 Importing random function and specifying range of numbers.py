import random # to use the random function we need to import it

#print a random integer between 100 t0 200
random_integer = random.randint(100,200)# the computer will choose a number between 100-200
print(random_integer)

#print any random float 

random_float = random.random()
print(random_float) #prints: anything in the range 0.00000000 to 0.99999999

new = random_float * 5 #if multiplied by 5 it gives a random number thats between 0.00000000 - 4.99999999

print(new)