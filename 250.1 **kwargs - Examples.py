#EX 1:
# What is the output of this code?
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(1, 2) #PRINTS: 1 2 yes please! 0

#........................................................

#EX 2
# What is the output of this code?
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(toast='nah', spam=4, eggs=2) #PRINTS: 4 2 nah 0

#........................................................

#EX 3:
# What is the output of the code below?
def test(*args):
    print(args)
 
test(1,2,3,5)
#PRINTS: (1, 2, 3, 4)
#args is a tuple, hence it will print the parenthesis ****

#........................................................

#EX 4:
# What is the output of the code below?
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)
#PRINTS: 4 (7, 3, 0) {"x": 10, "y": 64}
#4 is passed by position. 7,3,0 are collected into a tuple. x and y are in a keyword dictionary *****