#FIND THE HIGHEST SCORE
#Input: 78 65 89 86 55 91 64 89
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)): #converting each item in list to an integer
  student_scores[n] = int(student_scores[n]) #converting each item in list to an integer
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:   #checks each score against another
        highest_score = score #assigns the highest score to highest_score
    
print(f"The hightest score is: {highest_score}")