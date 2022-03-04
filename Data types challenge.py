#Split the input number of two digits and find their addition
#if your input number is 32, the output should be 3+2, which is 5
number = input("Type a two digit number")
print(type(number))

first_digit = number[0]
second_digit = number[1]


#METHOD 1:  addition = int(first_digit) + int(second_unit)

#OR METHOD 2:
conv_first_digit = int(first_digit)
conv_second_digit = int(second_digit)



addition = conv_first_digit + conv_second_digit
print(addition)

