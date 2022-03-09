#LISTS EXAMPLE 1
states = ["Newyork", "California", "Texas", "Miami"] #list data structure newyork is the 
print(states)



#Change ITEMS ON LIST
states[1] = "XYZ" # California is changed to XYZ, as it was item no 1
print(states)

#ADD an item to the end list
states.append("Kothaland")
print(states)

#adding a list to the end of a list
states.extend(["Kland", "Yland", "Zland'"])
print(states)

#insert an item at given position i.e. position 3
states.insert(3, "Florida")
print(states)

#REMOVE AN ITEM
states.remove("Florida")
print(states)

#POP AN ITEM Remove the item at the given position in the list, and return it
states.pop(3)
print(states)

#REVERSE STATES
states.reverse()
print(states)








#INDEXING LISTS
print(states.index("Texas", 0,))#finds Texas bstarting at data 0
print(states.index("Texas", 0, 6))#finds Texas bstarting at data 0 and ending search at data 6



#EXAMPLE 2
fruit = ["banana", "apple", "orange"]
print(fruit)

#SORT
fruit.sort()#sorts list alphabetically
print(fruit)


fruit.clear()#clears the entire list
print(fruit)