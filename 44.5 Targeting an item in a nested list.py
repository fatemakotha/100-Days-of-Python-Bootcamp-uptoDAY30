row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

#target 8
input_row_col = input("Enter two digit number: ") #enter 10
#1=column index, 0=row index #this means we target "2" which is in the 1st index/column2 and 0th index/row1

horizontal = int(input_row_col[0]) #converting the 1 from 10 entered, into an int, gives 1
vertical = int(input_row_col[1])#converting the 0 from 10 entered, into an int, gives 0

selected_row = map[vertical] #value of vertical is 0, thus we pull 0th index in map which is row1
selected_row[horizontal] = "X" #now that row 1 has been picked, we put the value of horizontal which is 1, which gives the 1st element in row1 which is 2


print(f"{row1}\n{row2}\n{row3}")
#prints: 
# [1, 'X', 3]
# [4, 5, 6]
# [7, 8, 9]