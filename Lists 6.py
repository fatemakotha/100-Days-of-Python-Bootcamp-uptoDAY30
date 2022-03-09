states = ["A", "B", "C", "D"]
num_of_states = len(states)#which gives us 4
print(num_of_states)

#if we try to find the last item on list using print(states[4]) we get an error because the fifth item on the list in on the index number 3
#what we do instead is:

print(states[num_of_states - 1]) #this gives us "D" as that is the last state