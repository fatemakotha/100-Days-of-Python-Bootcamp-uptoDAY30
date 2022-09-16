import math #imported math
def calculation(): #defined the actions for calculation
    first_num = int(input("Enter the 1st number: ")) #input 8 here
    operator = input("Chose the operator:\n +, -, * or /: ") # + - * / are all strings here
    second_num = int(input("Enter the 2nd number: ")) #input 2 here
    
    dic = {} #created an empty dictionary
    dic["first_num"] = first_num #created 1st item in dic
    dic["second_num"] = second_num #created 2nd item in dic
    print(f"The dictionary created is: \n {dic}") #{'first_num': 8, 'second_num': 2} 
    
    if operator == "+": #if operator is + then do addition
        ans1 = dic["first_num"] + dic["second_num"] #targets first and second value from the dic
        print(ans1)
    elif operator == "-": #if operator is - then do subtraction
        ans2 = dic["first_num"] - dic["second_num"] 
        print(ans2)
    elif operator == "*": #if operator is * then do multiplication
        ans3 = dic["first_num"] * dic["second_num"]
        print(ans3)
    elif operator == "/": #if operator is / then do division
        ans4 = math.ceil(dic["first_num"] / dic["second_num"]) #if 1st no is 5 and 2nd no is 2, then when divided, the ans is 2.5 which is not a whole number. Thus we use math.ceil() to round the number up
        print(ans4)
    else:
        print(f"There is no operator here as: {operator}")
calculation()
cont_inue = input("Do you wish to go again? Type yes or no: ").lower() # .lower() changes the input string to lowercase
end = False #end is set to False
while not end: #which means while not False = while true, run the loop below:
    if cont_inue == "yes":
        calculation() #if cont_inue == "yes" then call the calculation() function
        cont_inue = input("Do you wish to go again? Type yes or no: ").lower() #then ask if the user wants to go again # .lower() changes the  input string to lowercase
    elif cont_inue == "no": #if cont_inue == "no" then set end = True which stops the WHILE LOOP 
        end = True
        print("Thanks for using my CALCULATOR ❤️") #and prints this
    else:
        end = True
        print("You did not type yes or no!")
