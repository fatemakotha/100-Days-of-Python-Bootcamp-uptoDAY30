from tkinter import messagebox

#POP UP BOX:
messagebox.showinfo(title="OOPS!", message="Please don't keep any fields empty") #shows a tile and a message, and gives an "okay" button for user to click

messagebox.askokcancel(title=website, message="Hi") #shows a tile and a message, and gives "okay" and "cancel"  button for user to click

#____________________________________________________

#DELETE:
website_entry.delete(0, END) #CLEARS EVERYTHING FROM 0TH INDEX TO LAST IN WEBSITE TEXTBOX

#____________________________________________________

import pyperclip
pyperclip.copy(password) #insert the text we want to copy, which in this case is the password

#____________________________________________________


