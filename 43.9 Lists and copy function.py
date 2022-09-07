#***TThe copy() method returns a shallow copy of the list.

# mixed list
prime_numbers = [2, 3, 5]

# copying a list
numbers = prime_numbers.copy()


print('Copied List:', numbers)

# Output: Copied List: [2, 3, 5]




#does not work using index number***
states = ["Newyork", "California", "Texas", "Miami"] 
states.copy()
print(states) #prints: ['Newyork', 'California', 'Texas', 'Miami']