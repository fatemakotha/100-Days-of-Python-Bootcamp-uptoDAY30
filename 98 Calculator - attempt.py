first_num = int(input("Enter the 2st number: ")) #input 8 here
second_num = int(input("Enter the 2nd number: ")) #input 2 here
operator = input("Chose the operator:\n +, -, * or /")

dic = {}
dic["first_num"] = first_num
dic["second_num"] = second_num
print(dic) #prints:  {'first_num': 5, 'second_num': 2}

if operator == "+":
    ans1 = dic["first_num"] + dic["second_num"] #targets first and second value from the dic
    print(ans1)
elif operator == "-":
    print("minus")
elif operator == "*":
    print("multiply")
elif operator == "-":
    print("divide")
else: