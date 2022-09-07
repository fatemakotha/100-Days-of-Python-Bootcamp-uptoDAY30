#given string
string1=("Python is great")
print(string1.split()) 
#prints ['Python', 'is', 'great']


#Given string
string1=("This is Python")
string1=string1.split()
#applying list method to the individual elements of the list string1
list1=list(map(list,string1))
print(list1)
#prints:[['T', 'h', 'i', 's'], ['i', 's'], ['P', 'y', 't', 'h', 'o', 'n']]



#given string
string1=("AskPython")
#type-casting the string into list using list()
print(list(string1))
#prints ['A', 's', 'k', 'P', 'y', 't', 'h', 'o', 'n']


#given string
string1=("abc,def,ghi")
#spliting string1 into list with ',' as the parameter
print(string1.split(','))
#prints: ['abc', 'def', 'ghi']