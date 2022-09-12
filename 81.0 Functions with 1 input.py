import random

def greet():
    print(f"Hello")
    print(f"How do you do?")
    print(f"Isn't the weather nice today? ")
greet() 
#prints:
# Hello
# How do you do?
# Isn't the weather nice today? 

def greet_with_name(name): #funcion is greet_with_name() and inside () we create a variable "name"
    print(f"Hello {name}")
    print(f"How do you do? {name} ")
    
greet_with_name("Kotha") #this assignes "Kotha" to the variable name
# prints:
# Hello Kotha
# How do you do? Kotha 

#*** HERE greet_with_name is the PARAMETER and "Kotha" is the ARGUEMENT
#*** PARAMETER is the name of the data being passed into the function greet_with_name, AND the ARGUEMENT is the value of the data, which is "Kotha"