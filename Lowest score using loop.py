student_scores = input("Input a list of student scores ").split()#
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

#input 2 3 1 5 
lowest_score = student_scores[0]#here lowest score is student_scores value number 0, which is 2
for score in student_scores:
    if lowest_score > score:
       lowest_score = score
print(lowest_score)