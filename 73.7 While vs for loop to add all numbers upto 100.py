#Write a while loop that adds all the numbers up to 100 (inclusive).

total= 0

for number in range(101):
    total += number
    print(number)
    



#..........OR.......



counter = 0 #starts with 0 1 2 3 .....100
total = 0 #starts with 0

while counter <= 100: #when 0 <= 100, when 1 <= 100
    total += counter #total = 0, total = 0+1 = 1
    counter += 1 #now counter becomes 1+1=2


print(total)