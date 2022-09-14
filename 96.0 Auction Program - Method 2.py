
end = False
thisdict = {}

while not end:
    name = input("What is your name?: ")
    the_bid= int(input("What is your bid?: $"))
    more_entry = input("yes or no")
    result = 0
 
    if more_entry == "yes":
        thisdict[name] = the_bid #equivalent to += in a list
        print(thisdict) #{'kk': 3, 'cutu': 999}
        
    elif more_entry == "no":
        end = True
        max = max(thisdict.values())
        print(max)
        
        
        
        

        
        
        
        
        
    else:
        print("FINISHED")