#Using while loop, if statement and str() function; iterate through the list and if there is a 100, print it with its index number. i.e.: "There is a 100 at index no: 5"






lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
#Type your code here.

i = 0
while i < len(lst): #-----1
    if lst[i] == 100: #first i=0, then i=1,then 2 3 4 ........till length of list which in this case is 14
                      #and if lst[0]=100 then prints the command below, if not, goes back to -----1
        print("There is a 100 at index no: " + str(i))
    i = i+1 #adds 1 to i every time 