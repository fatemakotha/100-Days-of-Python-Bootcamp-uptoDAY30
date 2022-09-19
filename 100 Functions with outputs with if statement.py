def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return f"You did not input one of the names" #printed when either the first or last name is not given by the user
    #** In this case the next lines of the code which turns the words to TITLE, are not executed,
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}" # *** return means this is the end of a function and any code written after is will not run
    
print(format_name(input("What is your first name?"), input("What is your last name?")))