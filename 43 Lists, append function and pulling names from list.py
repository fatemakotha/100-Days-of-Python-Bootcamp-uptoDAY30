#LISTS
states = ["Newyork", "California", "Texas", "Miami"] #list data structure newyork is the first data, california is second
print(states[0]) #trying to pull out the first piece of data

print(states[2])#ans is Texas

#***INCASE OF COMMING BACKWARDS:
print(states[-1])#data number 1 from the back is MIAMI")

states[1] = ["ABD"]
print(states) #prints ['Newyork', ['ABD'], 'Texas', 'Miami']

#adding a name to the end of the list
states.append("KOTHA LAND")
print(states) #Prints ['Newyork', ['ABD'], 'Texas', 'Miami', 'KOTHA LAND']