first_num = int(input("Enter the 2st number: ")) 
second_num = int(input("Enter the 2nd number: "))
operator = input("Chose the operator:\n +, -, * or /")

dic = {}
dic["first_num"] = first_num
dic["second_num"] = second_num
print(dic) #prints:  {'first_num': 5, 'second_num': 2}

if operator == "+":
    ans1 = dic["first_num"] + dic["second_num"] #targets first and second value from the dic
    print(ans1)