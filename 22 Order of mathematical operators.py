a = float(123.9)
print(type(a))
#prints: <class 'float'>

print(str(70) + str(99))
#prints: 7099

print(type(6 / 3))
#prints <class 'float'>

# PEMDAS(The order in which operators work)
# Starts with()
# then does **
# then does */
# and lastly +-

print(3 * (3 + 3) / 3 - 3) 
#Heres how it works
print(3 * (6) / 3 - 3) #does the (3+3) in parenthesis first
print(18 / 3 - 3) #then does the *
print(6.0 - 3) #then does the /
print(3.0) #then does the -