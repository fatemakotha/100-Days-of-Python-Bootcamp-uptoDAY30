# CREATE NEW FILE: if the name specified does not have a file in that name, it will CREATE one!
with open("new_file.txt", mode="w") as file: #mode set to WRITE
    file.write("\nThis is some randon text") #all text in my file got replaced by "This is some randon text"