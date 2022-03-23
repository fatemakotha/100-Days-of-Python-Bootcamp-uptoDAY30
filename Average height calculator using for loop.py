#DO NOT USE len() or sum()
student_heights = input("Input a list of student heights ").split()#gets a string of numbers separated by spaces from the user and splits the string at whitespaces
for n in range(0, len(student_heights)):#here the range starts from 0 and ends at the number of heights given i.e. 5
  student_heights[n] = int(student_heights[n])#converts each of the resulting strings to a number

#sums the heights of all students and prints the total heigh
total_height =  0
for height in student_heights:
    total_height += height #total_height = total_height + height
print(total_height)# for input 1 2 3 4 it prints 10 

#counts how much students there are, and prints the number
num_of_students = 0
for student in student_heights:
    num_of_students += 1 #num_of_students = num_of_students + student
print(num_of_students)

avg_height = round(total_height / num_of_students)
print(avg_height)