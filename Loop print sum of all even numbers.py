#Print sum of all even numbers
total = 0
for number in range(2, 101, 2):
    total += number#this will add every number in the given range, starting from 2 to 100
    print(total)#2+3+4+5+...+100, giving us 2 6 12 ...2550
print(total)#as the indentation is removed it only prints 2500


#OR
total2 = 0
for number in range(1,101):
    if number % 2 == 0:
     total2 += number
print(total)#prints 2500