def outer_function(a, b): #if a = 5 and b = 10
    def inner_function(c, d): #inner function takes inputs from outer function, thus c = 5 and d = 10
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)