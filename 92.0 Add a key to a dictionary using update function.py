#Write a Python script to add a key to a dictionary
sample_dictionary = {0: 10, 1: 20}
sample_dictionary[2] = 30
print(sample_dictionary) #prints: {0: 10, 1: 20, 2: 30}

#...............OR...............

#Use the update function:
d = {0:10, 1:20}
d.update({2:30})
print(d) #prints: {0: 10, 1: 20, 2: 30}