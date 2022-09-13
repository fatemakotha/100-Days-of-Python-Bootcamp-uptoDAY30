#Dictionary
#i.e. Bug is the KEY, and the meaning is tha VALUE........EXAMPLE 1
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
#what if we wanted to retrieve an item from the dictionary:
#to fetch the word "Bug" from the dictionary:
print(programming_dictionary["Bug"]) #prints: An error in a program that prevents the program

#Add a new entry:.........EXAMPLE 2
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)
#prints:
# {'Bug': 'An error in a program that prevents the program from running as expected.', 'Function': 'A piece of code that you can easily call over and over again.', 'Loop': 'The action of doing something over and over again.'}