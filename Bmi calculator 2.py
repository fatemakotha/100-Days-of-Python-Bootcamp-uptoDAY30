
height = int(input("Enter height in m: "))
weight = int(input("Enter weight in kg: "))
bmi = round(weight / height ** 2)

if bmi < 18.5:#under 18.5
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:#uover 18 but below 25
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:#over 25 but below 30
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:#over 30 but below 35
    print(f"Your bmi is {bmi}, you are obese.")
else:#avobe 35
    print(f"Your bmi is {bmi}, you are clinically obese.")