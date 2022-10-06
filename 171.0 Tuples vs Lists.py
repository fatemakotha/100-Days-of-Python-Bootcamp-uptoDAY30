# Difference between LIST and TUPLE:
#Value of Tuples CANNOT be changed **

my_tuple = (1, 3, 4)
print(my_tuple[0]) #prints: 1
print(my_tuple[1]) #prints: 3
print(my_tuple[2]) #prints: 4

print(len(my_tuple))

my_tuple[2] = 3
print(my_tuple) #ERROR