#NORMAL FUNCTION:
def add(n1, n2):
    sum = n1 + n2
    print(sum)
    
add(2, 3) #which means n1=2 and n2=3
#PRINTS: 5

#.............................................................

#FUNCTIONS WITH UNLIMITED ARGUEMENTS:
def add(*args): #The asterisk means UNLIMITED ARGUMENTS ****
    print(args[0]) #the argument at index 0 is 2
    #PRINTS: 2
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(2, 3, 4) #takes in as many arguements as needed
#PTINTS: 9