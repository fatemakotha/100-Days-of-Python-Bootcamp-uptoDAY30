# We have to count how many times t,r,u,e,l,o,v,e appears in the names

print("Welcome to the Love Calculator! ")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined_name = name1 + name2
lower_case_name = combined_name.lower()#this .lower makes the capital letter change to lowercase

t = lower_case_name.count("t") #the answer to how many times "t" appears in the name is an integer
r = lower_case_name.count("r") #the answer here is an integer
u = lower_case_name.count("u") #the answer here is an integer
e = lower_case_name.count("e") #the answer here is an integer

true = t + r + u + e #ans of how many times t,r,u and e is found is added and ans is an integer

l = lower_case_name.count("l") #the answer to how many times "l" appears in the name is an integer
o = lower_case_name.count("o") #the answer here is an integer
v = lower_case_name.count("v") #the answer here is an integer
e = lower_case_name.count("e") #the answer here is an integer

love = l + o + v + e ##ans of how many times l,o,v and e is found is added and ans is an integer

#lets say true=8 and love=2, we need to convert them back to strings to get 82 or it will be added as integers and give 10!
love_score = str(true) + str(love)#adds the ans of tru and love as strings

int_love_score = int(love_score) #concerts the love_score from string to integer for if/else____1

if (int_love_score < 10) or (int_love_score > 90): #introduction to or function in if/else
    print(f"Your love_score is {int_love_score}, you go together like mentos and pepsi")#____1
elif (int_love_score >= 40) and (int_love_score <= 50):#____1
    print(f"Your love_score is {int_love_score}, you are alright together")
else:#____1
    print(f"Your love_score is {int_love_score}.")