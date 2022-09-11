z = 0 

while z < 3: #for z = 0 1 2 3  ----------------1
    if z == 0:
        print("z is",z)
        z += 1 #z becomes 0+1 = 1 and goes back to step -----------1
    elif z == 1:
        print("z is",z)
        z += 1 #z becomes 2 and goes back to step -----------1
    else:
        print("z is",z) #when z is 2
        z += 1 #here z becomes 3 and goes back to step -----------1
#prints: 
# z is 0
# z is 1
# z is 2