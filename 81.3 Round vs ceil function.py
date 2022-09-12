# Description
# Math.ceil( ) computes the ceiling function—i.e., it returns the closest integer value that is greater than or equal to the function argument. Math.ceil( ) differs from Math.round( ) in that it always rounds up, rather than rounding up or down to the closest integer. Also note that Math.ceil( ) does not round negative numbers to larger negative numbers; it rounds them up toward zero.

# Example using math.ceil
import math
a = Math.ceil(1.99);   #// Result is 2.0, rounds to the larger number
b = Math.ceil(1.01);   #// Result is 2.0, rounds to the larger number
c = Math.ceil(1.0);    #// Result is 1.0
d = Math.ceil(-1.99);  #// Result is -1.0 *** does not round negative numbers to larger negative, it rounds them up toward zero.

#Example using round
a = round(1.99);   #// Result is 2, rounds to the larger number
b = round(1.01);   #// Result is 1, rounds to the smaller number
c = round(1.0);    #// Result is 1
d = round(-1.99);  #// Result is -2 *** rounds to the larger negative number

print(a, b, c, d)