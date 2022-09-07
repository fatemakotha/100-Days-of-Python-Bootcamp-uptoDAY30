import random
names_string = input("Give me everybody's names, separated by a comma. ") # you can enter ANY number of names in the format abc, ddh, adas remember to use a space
names = names_string.split(", ")
print(len(names)) #gives 3

#Get the total no of items in list
no_of_items = len(names)

random_choice = random.randint(0, no_of_items - 1) #list starts with index 0 and last index

print(random_choice)#prints firrent integers

person_to_pay = names[random_choice] #HERE random_choice brings out the random int value and picks the name attached to it

print(person_to_pay)



# OR WE CAN DO THIS

import random
names_string = input("Give me everybody's names, separated by a comma. ") # you can enter ANY number of names in the format abc, ddh, adas remember to use a space
names = names_string.split(", ")
print(len(names)) #gives 3

person_to_pay = random.choice(names)

print(person_to_pay) #prints a random name