#Dictionary
#i.e. Bug is the KEY, and the meaninf is tha VALUE
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}
#what if we wanted to retrieve an item from the dictionary:
#to fetch the word "Bug" from the dictionary:
print(programming_dictionary["Bug"]) #prints: An error in a program that prevents the program from running as expected.
    #spell the KEY correctly to fetch it
    
#.........................................................................................

#Example of wWRONG code:
programming_dictionary = {
    Bug: "An error in a program that prevents the program from running as expected.", #NO "" in Bug means it won't run
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}
print(programming_dictionary[Bug]) # NO "" in Bug means it won't run
#.......................................................................................

#another example: ***
programming_dictionary = {
    123: "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}
print(programming_dictionary[123]) #prints: An error in a program that prevents the program from running as expected.