import random



#Functions with POSITIONAL ARGUMENT: ***
def greet_with(name, location): #it has 2 inputs, the name and the loaction
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet_with("Kotha", "Dhaka")
#prints:
# Hello Kotha
# What is it like in Dhaka?

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet_with(name="Kotha", location="Dhaka")
# prints:
# Hello Kotha
# What is it like in Dhaka?


#Functions with KEYWORD ARGUMENT: ***
greet_with(location="Dhaka", name="Kotha") #** name and location indexes are swapped but we still get correct answer 
#prints:
# Hello Kotha
# What is it like in Dhaka?