#Opening a file using file path
with open("C:/Users/fatem/OneDrive/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)