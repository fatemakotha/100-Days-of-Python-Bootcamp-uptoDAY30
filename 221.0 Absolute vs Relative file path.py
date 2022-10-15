#Opening a file using file path

#ABSOLUTE FILE PATH:
with open("C:/Users/fatem/OneDrive/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)


#RELATIVE FILE PATH:
with open("../../../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)