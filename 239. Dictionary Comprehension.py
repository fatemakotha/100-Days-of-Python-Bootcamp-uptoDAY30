#Create a dictionary using Dictionary comprehension:
#Example 1
import random
names = ["Kotha", "Cutu", "Sheela", "Mummum"]

#new_dic = [new_key:new_value for items in list if test *********
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores) #{'Kotha': 2, 'Cutu': 87, 'Sheela': 100, 'Mummum': 29}