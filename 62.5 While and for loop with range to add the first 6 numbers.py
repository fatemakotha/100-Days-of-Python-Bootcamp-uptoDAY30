summation = 1+2+3+4+5+6
print(summation) #prints: 21

#.....OR......

num = 6
sum = 0  
   # use while loop to iterate un till zero  
while(num > 0):  
    sum += num  
    num -= 1  
print("The sum is",sum) #prints: The sum is 21

#.....OR......
 
sum = 0
for number in range(7): #range is 0 to 6
    sum += number
print(sum) #prints 21

#.....OR......
  
n = int(input("Enter number")) #enter 6
sum = 0
# loop from 1 to n
for num in range(1, n + 1, 1): #starting from 1 ending at n+1 and steps of 1
    sum += num
print("Sum of first ", n, "numbers is: ", sum) #prints: Sum of first  6 numbers is:  21