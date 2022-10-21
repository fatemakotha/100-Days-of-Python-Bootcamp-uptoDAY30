import turtle

kim = turtle.Turtle()

#The line below will give an error because it need the agrument of what to write:
# kim.write() 

kim.write("hello", align = "center", font=("Arial", 80, "bold"))

#align and font are optional arguements! **
#you can use there default value:
kim.write("dfdf")
#OR you can assign a vaklue
kim.write("hello", align = "center", font=("Arial", 80, "bold"))