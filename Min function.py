
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

#lets say our input was 1 2 3 4
print(min(student_scores))#prints 1. which is the minimum among the inputs