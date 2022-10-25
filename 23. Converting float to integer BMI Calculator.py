#BMI CALCULATOR
height = input("Enter the height in metres: ")
weight = input("Enter the weight in kilograms: ")

bmi =  int(weight) / ((float(height)) ** 2)
print(bmi) #ans is a float

#how do we convert this float BMI to a whole number?
#ans:
print(int(bmi))