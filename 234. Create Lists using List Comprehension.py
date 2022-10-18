#Creating List using FOR LOOP:
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    new_num = n + 1
    new_list.append(new_num)
print(new_list) #prints: [2, 3, 4]

#..............OR.........

#Creating List using LIST COMPREHENSION:
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list) #prints: [2, 3, 4]
