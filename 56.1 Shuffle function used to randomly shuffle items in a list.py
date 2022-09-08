import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist) #shuffle function ONLY works for lists

print(mylist)
#prints:
# ['banana', 'apple', 'cherry'] or
# ['apple', 'cherry', 'banana'] or 
# ['cherry', 'apple', 'banana'] and so on





# ***shuffle function does not work in a string
import random

mylist = ["asdfsd"]
random.shuffle(mylist) #shuffle function ONLY works for lists

print(mylist)
#prints:
# ['asdfsd']