#***The pop() method removes the item at the given index from the list and returns the removed item.


# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# remove the element at index 2
removed_element = prime_numbers.pop(2)

print('Removed Element:', removed_element) # prints Removed Element: 5
print('Updated List:', prime_numbers) #prints # Updated List: [2, 3, 7]





#does not work using index number***
# states = ["Newyork", "California", "Texas", "Miami"] 
# removed_state = states.pop(3)
# print('Removed Element:', removed_states) # prints Removed Element: 5
# print('Updated List:', states)

states = ["Newyork", "California", "Texas", "Miami"] 
removed_state = states.pop(3)

print('Removed Element:', "Texas") # prints Removed Element: Texas
print('Updated List:', states) #prints Updated List: ['Newyork', 'California', 'Texas']