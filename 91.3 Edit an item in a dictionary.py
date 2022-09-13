#Dictionary
#i.e. Bug is the KEY, and the meaning is tha VALUE........EXAMPLE 1
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
#Add a new entry:.........EXAMPLE 2
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#Edit an item in a dictionary: ***
programming_dictionary["Bug"] = "ABC"
print(programming_dictionary) #prints: {'Bug': 'ABC', 'Function': 'A piece of code that you can easily call over and over again.', 'Loop': 'The action of doing something over and over again.'}

#but if:
programming_dictionary["new"] = "................"
print(programming_dictionary) #prints: {'Bug': 'ABC', 'Function': 'A piece of code that you can easily call over and over again.', 'Loop': 'The action of doing something over and over again.', 'new': '................'}