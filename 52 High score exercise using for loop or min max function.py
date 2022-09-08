#FIND THE HIGHEST SCORE
#Input: 78 65 89 86 55 91 64 89
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)): #converting each item in list to an integer
  student_scores[n] = int(student_scores[n]) #converting each item in list to an integer
print(student_scores)
print(max(student_scores)) #prints: 91
print(min(student_scores)) #prints: 55

#But we don't want to use the max or min function
print("..........METHOD 2.........")