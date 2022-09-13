# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

d=dict()
for x in range(1,16):
    d[x] = x**2 # when x is 2, 
                #d[2] = 2**2, 
                # 2 = 4
                #gives 2: 4
print(d)
#prints:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 
# 225}