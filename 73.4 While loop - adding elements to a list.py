#  Adding elements to a list using while loop
myList = []
i = 0

while len(myList) < 4 :
    myList.append(i)
    i += 1 # starts with i = 0 then 1 2 3 and stops at 4
  
print(myList)
#prints:
# [0, 1, 2, 3]