#Every year that is divisible by 4 is a LEAP year
    #EXCEPT every year tnat is divisible by 100 which is NOT LEAP
        #UNLESS the year is divisible by 400 which is a LEAP YEAR




year = int(input("Input the year you want to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print ("Leap")
        else:
            print("Not leap")
    else:
        print("Leap")
else:
    print("Not leap")