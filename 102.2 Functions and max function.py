# Python function to find the Max of three numbers
def max_number(num_one, num_two, num_three):
    """Function that finds the max number"""
    first = int(num_one)
    second = int(num_two)
    third = int(num_three)
    list = max(first, second, third) #max function finds the highest value
    print(list)
    
    
max_number(input("Enter first number: "), input("Enter second number: "), input("Enter third number: "))

#.................OR...............................

def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
    # return max_of_two( x, max_of_two( 6, -5) )
    # return max_of_two( x, 6 )
    # return max_of_two( 3, 6 )
    # return max_of_two( 6 )
print(max_of_three(input("Enter x"), input("Enter y"), input("Enter z")))