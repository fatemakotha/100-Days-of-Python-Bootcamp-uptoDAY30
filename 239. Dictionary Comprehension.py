#Create a dictionary using Dictionary comprehension:
#Example 1
import random
names = ["Kotha", "Cutu", "Sheela", "Mummum"]

#new_dic = [new_key:new_value for items in list if test *********
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores) #{'Kotha': 2, 'Cutu': 87, 'Sheela': 100, 'Mummum': 29}

#new_dic = [new_key:new_value for (key,value) in list if test *********
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students) #prints: {'Kotha': 67}