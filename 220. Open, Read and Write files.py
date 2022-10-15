file = open("my_file.txt") #OPENING THE FILE named: my_file.txt
contents = file.read() #READING THE FILE

print(contents) #prints: Hello, my name is Kotha.

#I have modified and added a new line to my file:

print(contents)
#prints:
# Hello, my name is Kotha.
# I love hot chocolate

file.close() #**CLOSING TH FILE

print(contents) #even after the file is closed, it can access whats inside
#prints: 
# Hello, my name is Kotha.
# 
# I love hot chocolate