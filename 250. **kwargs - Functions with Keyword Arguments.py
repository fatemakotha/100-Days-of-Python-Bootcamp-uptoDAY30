#FUNCTIONS with KEYWORD ARGUEMENTS:
def calculate(n, **kwargs): #adds KEYWORD ARGUMENTS and THEIR values as a DICTIONARY  **
   print(kwargs) #PRINTS: {'add': 3, 'multiply': 5}
   for key, value in kwargs.items():
       # print(key)
       # print(value)
       #PRINTS:
       # add
       # 3
       # multiply
       # 5
       n += kwargs["add"]
       n *= kwargs["multiply"]
       print(n)
       
    
calculate(2, add=3, multiply=5) #PRINTS: 25 because n is given a value of 2, and 2+=3  is 5 and 5*=5 is 25