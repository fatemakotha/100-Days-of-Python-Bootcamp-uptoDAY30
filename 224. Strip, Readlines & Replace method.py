#READLINE / READLINES:
# Returns all lines in the file, as a list where each line is an item in the list object:
f = open("demofile.txt", "r")
print(f.readlines())

# Does not return the next line if the total number of returned bytes are more than 33:
f = open("demofile.txt", "r")
print(f.readlines(33))


#REPLACE:
# Replace the word "bananas":
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)


#STRIP
# Remove spaces at the beginning and at the end of the string:
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")