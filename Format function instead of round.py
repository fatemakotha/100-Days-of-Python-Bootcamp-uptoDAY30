print("Welcome to the tip calculator.")

bill = float(input("What is your total bill $?"))


tip = int(input("What percentage tip would you prefer to give? 10 12 or 15"))

people = int(input("How many people will split the people?"))

#Each person should pay = (bill/  no of people) * 1.12 if 12%
#For 10%, we use 1.12, for 12% 1.12, for 15% 1.15


bill_with_tip = tip / 100 * bill + bill #entire bill along with entire tip for all people together

print(bill_with_tip)

each_person = float(bill_with_tip / people)

#**** We now round up the float, using round, or format function
amount = round(each_person, 2)
#or
amount = "{:.2f}".format(each_person)



each_person_as_integer = str(each_person)

print("Each person has to pay " + each_person_as_integer + "$")