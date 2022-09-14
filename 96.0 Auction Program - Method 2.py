
end = False
thisdict = {}

while not end:
    name = input("What is your name?: ")
    the_bid= int(input("What is your bid?: $"))
    more_entry = input("yes or no")
    
    
    if more_entry == "yes":
        thisdict[name] = the_bid #equivalent to += in a list
        print(thisdict)
        
    elif more_entry == "no":
        end = True
        winner = thisdic.max()
        print("No more entries")
        
    else:
        print("FINISHED")