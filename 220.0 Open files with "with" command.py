
#We do not have to close this file as we used the "with" statement: 
with open("my_file.txt") as file: #OPENING THE FILE named: my_file.txt and naming it file
    contents = file.read() #READING THE FILE
    print(contents) #prints: Hello, my name is Kotha.
    print(contents)
    #Modified thw file:
    print(contents) #even after the file is closed, it can access whats inside