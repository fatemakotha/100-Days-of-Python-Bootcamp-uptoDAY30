#Using loop to calculate the highest score
student_scores = input("Input a list of student scores ").split()#gets a string of numbers separated by spaces from the user and splits the string at whitespaces
for n in range(0, len(student_scores)):#here the range starts from 0 and ends at the number of heights given i.e. 5
  student_scores[n] = int(student_scores[n])#converts each of the resulting strings to a number
print(student_scores)

# print(min(student_scores))
#input 3 2 4 6 
h_score = 0
for score in student_scores:
    score > h_score#first runs 3 > 0 true, 2 > 3 false, 4 > 3 true and then 6 > 4 true
    h_score = score # == means checking a condition, = means it is equal to
print(f"The Highest score is: {h_score}")