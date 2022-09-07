# create a list
numbers = [2, 3, 5, 2, 11, 2, 7]

# check the count of 2
# numbers.count(2) does not work, it has to be stored into another variable
count = numbers.count(2)

print('Count of 2:', count)

# Output: Count of 2: 3





states = ["Newyork", "California", "Texas", "Miami"] 
new = states.count("Texas")
print(new) #prints 1


#INCORRECT
states = ["Newyork", "California", "Texas", "Miami"] 
new = states.count(0)
print(new) #prints 0