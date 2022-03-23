student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total_height =  sum(student_heights)
num_of_students = len(student_heights)
avg_height = round(total_height / num_of_students)
print(avg_height)