import math 

first_num = int(input("Enter the 1st number: ")) #input 8 here
operator = input("Chose the operator:\n +, -, * or /")
second_num = int(input("Enter the 2nd number: ")) #input 2 here

dic = {}
dic["first_num"] = first_num
dic["second_num"] = second_num
print(dic) #prints:  {'first_num': 5, 'second_num': 2}

if operator == "+":
    ans1 = dic["first_num"] + dic["second_num"] #targets first and second value from the dic
    print(ans1)
elif operator == "-":
    ans2 = dic["first_num"] - dic["second_num"] 
    print(ans2)
elif operator == "*":
    ans3 = dic["first_num"] * dic["second_num"]
    print(ans3)
elif operator == "/":
    ans4 = math.ceil(dic["first_num"] / dic["second_num"]) #if 1st no is 5 and 2nd no is 2, then when divided, the ans is 2.5 which is not a whole number. Thus we use math.ceil() to round the number up
    print(ans4)
else:
    print("sad")