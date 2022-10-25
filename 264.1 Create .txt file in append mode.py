            with open("data.txt", "a") as data_file: #opens in append mode and creates the file names info.txt as there is no file of that name here
                data_file.write(f"{website} | {email}| {password}\n")
                website_entry.delete(0, END) #CLEARS EVERYTHING FROM 0TH INDEX TO LAST IN WEBSITE TEXTBOX
                password_entry.delete(0, END) #CLEARS EVERYTHING FROM 0TH INDEX TO LAST IN PASSWORD TEXTBOX

#******The write method overwrites the content in a text file while the append method appends text to the file.******