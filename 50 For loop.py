#A loop allows us to execute the same line of codes, multiple times
fruits = ["Apple", "Peach", "Pear"]
#to access all items in this list individually and print it out one by one then we would use a "for" loop.
#then we give a name to a single term
for fruit in fruits:
    print(fruit)#prints the value of each of these fruit variables #we are executing the print statement 3 times
    #prints
    # Apple
    # Peach
    # Pear
    #This loop is taking a list of fruits and assigning a variable named fruit to each of them
    #So the 1st time it runs, fruit = Apple, the 2nd time fruit = Peach and 3rd time fruit = Pear
    print(fruit + " " + "Pie")
    #prints:
    # Apple
    # Apple Pie
    # Peach
    # Peach Pie
    # Pear
    # Pear Pie 
    
    # ***ALL OF THIS IS EXECUTED AS IT IS INSIDE THE for LOOP
    