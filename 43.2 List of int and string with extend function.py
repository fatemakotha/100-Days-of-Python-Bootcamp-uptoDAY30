# create a list
states = ["Newyork", "California", "Texas", "Miami"] #LIST 1
# create another list
letters = ["A", "B", "C"] #LIST 2

#extend function to add two lists
states.extend(letters)
print(states) #prints ['Newyork', 'California', 'Texas', 'Miami', 'A', 'B', 'C'] ***HERE THE ORDER IS LIST 1 AND THEN LIST 2





# create a list
prime_numbers = [2, 3, 5] #LIST 1

# create another list
numbers = [1, 4] #LIST 2

# add all elements of prime_numbers to numbers
numbers.extend(prime_numbers)


print('List after extend():', numbers)

# Output: List after extend(): [1, 4, 2, 3, 5] *** HERE THE LIST IS IN AUTO ORDER