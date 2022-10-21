import tkinter
import turtle

my_window = tkinter.Tk() #created a window
my_window.title("My First GUI prog") #changes the title of the window
my_window.minsize(width=500, height=300) #changes the size of the window

#Creating a LABEL:

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold")) #font is a Tuple #PRINTS: I am a Label
#If I want to change my_lable's text:
my_label["text"] = "NEW TEXT" #PRINTS: NEW TEXT
my_label.config(text="NEW TEXT") #PRINTS: NEW TEXT

#in pack() the default values are already set as a DICTIONARY, so if we want to change that we can specify that certain input:
my_label.pack(side="top") #pust the label at the center top of screen. without the pack() method, LABEL won't appear on screen


#Creating a BUTTON:
#Getting the button to work:
def button_clicked():
    print("I got clicked")
    my_label.config(text="I got clicked") #changes the text of the label when button is clicked
    new_text = my_input.get()
    my_label.config(text=new_text)  # changes the text of the label when something is typed inside the box

my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button.pack() #prints a rectangular button on screen


#ENTRY component: #opens a space for user to type something in ***
my_input = tkinter.Entry(width=10) #changes width of box
my_input.pack()







my_window.mainloop() #will keep the window open. This is a loop lie: while True. HAS TO BE AT THE END OF THE PROGRAM **