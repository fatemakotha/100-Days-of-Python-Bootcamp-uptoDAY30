

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3] #THIS IS A NESTED LIST
print(f"{row1}\n{row2}\n{row3}") #ADDING A LINE BETWEEN EACH ROW

position = input("Where do you want to put the treasure? ") # if you input 23 that mean horizontal 2 and verticle 3
#We need to convert the 2digit string "23" to ver and hori and convert them to integers
horizontal = int(position[0]) # we get hold of the 0th item in the string "2" as 0th postition in 23 is 2
vertical = int(position[1]) # we get hold of the 0th item in the string "3" as 1st position in 23 is 3



selected_row = map[vertical - 1] #vertical-1= 3-1 = 2, 2nd index in map is row3. Now row3 is selected
selected_row[horizontal - 1] #horizontal-1 = 2-1 = 1, we get the index one item from row3 which is what we will mark as "X"
selected_row[horizontal - 1] = "X" #changing that box to x
# prints:
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']
    




print(f"{row1}\n{row2}\n{row3}")