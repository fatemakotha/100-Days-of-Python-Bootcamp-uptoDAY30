#EX------------1
a = 13.949999988079071
print(a)
#prints: 13.94999998807907
print("%.2f" % a)
#prints: 13.95
print(round(a,2))
#prints: 13.95

print("%.2f" % round(a, 2))
# #prints: 13.95

print("{:.2f}".format(a))
# #prints: 13.95

print("{:.2f}".format(round(a, 2)))
# #prints: 13.95

print("{:.15f}".format(round(a, 2)))
#prints: 13.949999999999999

# #......................................................

#EX---------2
import math

a = math.ceil(29.785)
print(a) #prints: 30

b = round(29.785)
print(b) #prints: 30

x = format(math.pi, '.12g')  # give 12 significant digits
print(x)
#prints: 1'3.14159265359'

y = format(math.pi, '.2f')   # give 2 digits after the point
print(y)
#prints: 1'3.14'

z = repr(math.pi)

print(z)
#prints: 1'3.141592653589793'