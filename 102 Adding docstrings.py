#Adding docstrings
def format_name(f_name, l_name):
    """Take the names and convert them to 
    title case""" #the doctring goes after the name of the function
    if f_name == "" or l_name == "":
        return f"You did not input one of the names" 
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}" 
    
print(format_name(input("What is your first name?"), input("What is your last name?"))) #function is being called in this line