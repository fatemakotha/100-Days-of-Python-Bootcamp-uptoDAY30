student_scores = {
  "Hermione": 99,
  "Ron": 78,
  "Harry": 81, 
  "Draco": 74,
  "Neville": 62,
} #THIS IS A DICTIONARY

#TODO-1: Create an empty dictionary called student_grades.
#How to start with an EMPTY Dictionary:
student_grades = {} #another dictionary

for student in student_scores:
    score = student_scores[student] #score is a new variable
    # score = student_scores[Hermione]
    # score = 99
    if score > 90: #if 99 > 90
        student_grades[student] = "Outstanding!" #as 99 > 90, student_grades[Hermione] is set to "Outstanding!"
                                                 #the KEY stays same, BUT the VALUE is changed from 99 to "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "FAIL"

print(student_grades)
#PRINTS:
# {'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding!', 'Draco': 'Acceptable', 'Neville': 'FAIL'}  