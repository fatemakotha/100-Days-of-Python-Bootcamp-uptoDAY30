

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️*"]
map = [row1, row2, row3] #THIS IS A NESTED LIST
print(f"{row1}\n{row2}\n{row3}") #ADDING A LINE BETWEEN EACH ROW

position = input("Where do you want to put the treasure? ") # if you input 23 that mean horizontal 2 and verticle 3
#We need to convert the 2digit string "23" to ver and hori and convert them to integers
horizontal = int(position[0]) # we get hold of the 0th item in the string "2" as 0th postition in 23 is 2
vertical = int(position[1]) # we get hold of the 0th item in the string "3" as 1st position in 23 is 3

print(map[3 -1]) #because in python range srates at 0, in this case range is 0-2
#OR 
print(map[vertical -1])#print the row I have selected

selected_row = map[vertical - 1]
selected_row[horizontal - 1] #selected row at the position horizontal -1
selected_row[horizontal - 1] = "X" #changing that box to x
# prints:
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️*']
    




print(f"{row1}\n{row2}\n{row3}")