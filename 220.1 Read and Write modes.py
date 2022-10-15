# We do not have to close this file as we used the "with" statement:
with open("my_file.txt", mode="r") as file: #By default the mode is set to READ ONLY, you CANNOT WRITE
    file.write("This is some randon text")

# We do not have to close this file as we used the "with" statement:
with open("my_file.txt", mode="w") as file: #mode set to WRITE
    file.write("This is some randon text") #all text in my file got replaced by "This is some randon text"