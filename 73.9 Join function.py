#1
display = ["_", "_", "_","_", "_", "_"]
print(display) #prints: ['_', '_', '_', '_', '_', '_']

#2
print(f"The joined list is: {' '.join(display)}") #joins the items in a list using space in between
#prints: The joined list is: _ _ _ _ _ _

#3
print(f"{','.join(display)}") #joins the items in a list using a comma in between
#prints: _,_,_,_,_,_

#4
my_list = ("John", "Peter", "Vicky")
x = "# ".join(my_list) #joins the list using a # and a space in between
print(x) #prints: #John# Peter# Vicky

#5
my_list = ("John", "Peter", "Vicky")
x = "".join(my_list) #joins the list using nothing in between
print(x) #prints: JohnPeterVicky