
#While loops:
number_of_hurdles = 6 #as there are 6 hurdles
while number_of_hurdles > 0: #when number_of_hurdles > 0, carry out the two lines below:
    number_of_hurdles -= 1# every time it loops, number_of_hurdles decreases by 1
    print(number_of_hurdles) #prints: 5, then 4, then 3, then 2, then 1, then 0
    
#niow that the while function is no more TRUE, as indentation has been removed, it prints the last value of number_of_hurdles, which we saw in the loop stopped at 0
print(number_of_hurdles) #prints: 0