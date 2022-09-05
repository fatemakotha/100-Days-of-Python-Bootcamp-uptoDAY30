print("Welcome to the tip calculator.")

bill = float(input("What is your total bill $?"))


tip = int(input("What percentage tip would you prefer to give? 10 12 or 15"))

people = int(input("How many people will split the people?"))

#Each person should pay = (bill/  no of people) * 1.12 if 12%
#For 10%, we use 1.12, for 12% 1.12, for 15% 1.15


bill_with_tip = tip / 100 * bill + bill #entire bill along with entire tip for all people together #/100 turns tip into 0.1, 0.2 or 1.15, this decimal no times the tip is the full tip. Then we add this tip that we calculated from the bill, to the actual bill

print(bill_with_tip)

each_person = bill_with_tip / people

each_person_as_integer = str(each_person)

print("Each person has to pay " + each_person_as_integer + "$")