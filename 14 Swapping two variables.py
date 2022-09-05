# Python program to swap two variables

x = input("x: ")
y = input("y: ")

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print("x is :" + x)
print("y is :" + y)

# prints:

# x: 5
# y: 6
# x is :6
# y is :5