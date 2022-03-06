year = int(input("Which year do you want to check? "))

if year % 4 == 0:#____________ 1
    if year % 100 == 0:#_________ 
        if year % 400 == 0:#__________ 3
            print("Leap")
        else:
            print("Not Leap")# if year % 400 not == 0 Not Leap #__________ 3
    else:
        print("Leap year")#if year % 100 not == 0 #_________ 2
else:
        print("Not Leap year")# if year % 4 not == 0 Not LEAP#_____________1