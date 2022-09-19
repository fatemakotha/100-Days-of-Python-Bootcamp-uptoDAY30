#  Write a Python function to sum all the numbers in a list
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

entry = input("Enter the numbers seperated by a space: ").split()
print(entry)

for number in range(0, len(entry)):
    entry[number] = int(entry[number])
total = 0
for x in entry:
    total += x
print(total)

#.........OR...................................

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))
