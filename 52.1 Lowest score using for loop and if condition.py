#FIND THE LOWEST SCORE
#Input: 78 65 89 86 55 91 64 89
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)): #converting each item in list to an integer
  student_scores[n] = int(student_scores[n]) #converting each item in list to an integer
print(student_scores)

lowest_score = student_scores[0] #u***nlike the highest score where we assigned highest_score = 0, here we assign lowest_score to the first score
for score in student_scores:
    if score < lowest_score:   #checks each score against another
        lowest_score = score #assigns the highest score to highest_score
    
print(f"The lowest score is: {lowest_score}")