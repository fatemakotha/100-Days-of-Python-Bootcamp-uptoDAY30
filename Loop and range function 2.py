#using range() in for loop
total = 0
for number in range(1, 101):
    total += number#this will add every number in the given range, starting from 0 to 100
    print(total)#1+2+3+4+5+...+100, giving us 1 3 6 ...5050
print(total)#as th indentation is removed it only prints 5050