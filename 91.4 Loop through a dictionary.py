#Dictionary
#i.e. Bug is the KEY, and the meaning is tha VALUE........EXAMPLE 1
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
#Add a new entry:.........EXAMPLE 2
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)



#HOW TO LOOP THROUGH A DICTIONARY:
for key in programming_dictionary:
    print(key)
    #prints:
    # Bug
    # Function
    # Loop  ***ONLY prints the key
    
print("NEXT EXAMPLE\n") #...............................................

#INSTEAD, to print our the key and value, we do this:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    #prints:
    # Bug
    # An error in a program that prevents the program from running as expected.
    # Function
    # A piece of code that you can easily call over and over again.
    # Loop
    # The action of doing something over and over again. 