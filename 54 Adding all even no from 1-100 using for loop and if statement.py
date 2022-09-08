#ADD ALL EVEN NUMBERS FROM 1-100
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number #addes each number to the previous ones
print(total) #prints: 5050



print(".....OR METHOD 2........")



total = 0
for number in range(2, 101, 2): # *** Here it starts adding numbers from 2 i.e. 2+4+5+6+8.....+100
    if number % 2 == 0:
        total += number #addes each number to the previous ones
print(total) #prints: 5050