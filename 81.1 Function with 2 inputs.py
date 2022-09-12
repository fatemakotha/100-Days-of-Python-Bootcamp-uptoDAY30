import random

def greet():
    print(f"Hello")
    print(f"How do you do?")
    print(f"Isn't the weather nice today? ")
greet() 

def greet_with_name(name): #funcion is greet_with_name() and inside () we create a variable "name"
    print(f"Hello {name}")
    print(f"How do you do? {name} ")
    
greet_with_name("Kotha") 


#Functions with more than 1 input:
def greet_with(name, location): #it has 2 inputs, the name and the loaction
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet_with("Kotha", "Dhaka") #value of PARAMETER1 named name is set to 1st value "Kotha" and value of PARAMETER2 named location is set to the 2nd value "Dhaka" ***THIS IS CALLED POSITIONAL ARGUEMENTS
#prints:
# Hello Kotha
# What is it like in Dhaka?