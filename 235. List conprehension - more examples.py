#Write a List Comprehension to create a new list called squared_numbers.
# This new list should contain every number in the list numbers but each number should be squared
#EXAMPLE 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)


#EXAMPLE 2:
#file1.txt has some numbers in it
#file2.txt has some numbers in it
#we want to print the common numbers in the 2 files
import csv
with open("file1.txt") as file1:
    file_1_data = file1.readlines()
    print(file_1_data)
with open("file2.txt") as file2:
    file_2_data = file2.readlines()
    print(file_2_data)

result = [int(num) for num in file_1_data if num in file_2_data]
print(result)