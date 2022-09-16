def format_name(f_name, l_name): #f_name and l_name are the PARAMETERS or INOUTS
    formatted_f_name = f_name.title() #title function converts the first letter of every wordto uppercase and the rest to lowercase
    formatted_l_name = l_name.title()
    print(f" {formatted_f_name} and {formatted_l_name}")
    
format_name("angela", "KoThA")
#prints:
# Angela and Kotha