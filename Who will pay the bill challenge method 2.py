import random



names_string = input("Give me the names, seperated by commas.")
names = names_string.split(",")#splitting input to a LIST



print(names[0])# name at position 0 is the first name on the list
num_items = len(names)# finds the number of names on the list which is 3




random_choice = random.randint(0, num_items - 1)#starting from position 0 and ending at 2 as(num_items - 1 = 3 -1 = 2)
person = names[random_choice]
print(f"Person who will buy the meal today is {person}")