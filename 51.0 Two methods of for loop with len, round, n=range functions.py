#INPUT = 180 124 165 173 189 169 146


student_heights = input("Input a list of student heights ").split()

#CONVERTING EACH HEIGHT TO INTEGER
for n in range(0, len(student_heights)): #specifying the range which is index (0 to no of items by len)
  student_heights[n] = int(student_heights[n]) #we use n here as we used n in the prev line # puts n=0, n=1, up until n=len(student heights)
  
print(student_heights)
print(type(student_heights))#prints list

#FINDING TOTAL HEIGHT
total_height = sum(student_heights)#sum function adds the items in a list

#FINDING TOTAL NO OF STUDENTS
number_of_students = len(student_heights)
ave_height = round(total_height / number_of_students)#round function rounds up the answer
print(ave_height)#prints 164




print("...........OR METHOD 2.............")




student_heights = input("Input a list of student heights ").split()#splits the items in a list
for n in range(0, len(student_heights)): #specifying the range which is index (0 to no of items by len)

#CONVERTING EACH HEIGHT TO INTEGER
  student_heights[n] = int(student_heights[n]) #we use n here as we used n in the prev line # puts n=0, n=1, up until n=len(student heights)
print(student_heights)
print(type(student_heights))#prints list

#FINDING TOTAL HEIGHT
total_height = 0
for height in student_heights:#we replicate the "sum" function here #We assign each value to the variable height, i.e. height= 180, height =124 etc
    total_height += height #ADD EACH VALUE OF HEIGHT TO THE NEXT i.e. height=0+180+124...
print(total_height)

#FINDING TOTAL NO OF STUDENTS
number_of_students = 0 #assigned to 0
for students in student_heights:
    number_of_students += 1#we add 1 to number_of_students each time our for loop tuns
print(number_of_students)
ave_height = round(total_height / number_of_students)#round function rounds up the answer
print(ave_height)#prints 164