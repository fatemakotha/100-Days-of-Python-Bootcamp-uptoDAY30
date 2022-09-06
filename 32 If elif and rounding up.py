height = float(input("Enter height in m: "))
weight = float(input("Enter weight in kg: "))

print(height)
print(weight)

bmi = round(weight / height ** 2)
print(bmi)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
    
elif bmi == 18.5 or bmi < 25:#we can also write just bmi < 25 because 18.5 is more then 18.5 and below 25
    print(f"Your bmi is {bmi}, you are normal")
elif bmi == 25 or bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi == 30 or bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
    
else:
    print(f"Your bmi is {bmi}, you are clinically obese")