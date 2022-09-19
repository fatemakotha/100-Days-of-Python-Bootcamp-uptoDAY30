# Without running the code below, what do you think will be printed in the console?

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 
print(add(2, multiply(5, divide(8, 4))))
#prints: 12
#8 / 4 = 2
# 2 * 5 = 10
# 10 + 2 = 12