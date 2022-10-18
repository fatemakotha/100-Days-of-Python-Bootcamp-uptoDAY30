#CONDITIONAL LIST COMPREHENSION
#EXAMPLE 4: Make a new list that adds 1 to each item if item is > 2
numberss = [1, 2, 3, 4, 5, 6]
newww_list = [n + 1 for n in numberss if n > 2]
print(newww_list) #prints: [4, 5, 6, 7]

#EXAMPLE 5: prints name if it has less that 5 alophabets
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 5]
print(short_names) #prints: ['Alex', 'Beth', 'Dave']
