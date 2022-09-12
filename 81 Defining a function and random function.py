import random

names = ["X", "Y", "Z"]
name = random.choice(names)
def greet():
    print(f"Hello {name}")
    print("How do you do?")
    print("Isn't the weather nice today? ")
greet()
#prints :
# Hello Y or X or Z in random order
# How do you do?
# Isn't the weather nice today? 