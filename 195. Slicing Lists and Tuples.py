#Slicing:
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5]) #prints: ['c', 'd', 'e']
print(piano_keys[2:]) #prints: ['c', 'd', 'e', 'f', 'g']
print(piano_keys[:5]) #prints: ['a', 'b', 'c', 'd', 'e']
print(piano_keys[2:5:2]) #start:end:step #prints: ['c', 'e']
print(piano_keys[::2]) #start:end:step #prints: ['a', 'c', 'e', 'g']
print(piano_keys[::-1]) #start:end:step #prints: ['g', 'f', 'e', 'd', 'c', 'b', 'a']

piano_tuple = ("do","re", "mi", "ki", "mi", "na", "wa" )
print(piano_tuple[2:5]) #prints: ('mi', 'ki', 'mi')
print(piano_tuple[2:]) #prints: ('mi', 'ki', 'mi', 'na', 'wa')
print(piano_tuple[:5]) #prints: ('do', 're', 'mi', 'ki', 'mi')
print(piano_tuple[2:5:2]) #prints: ('mi', 'mi')
print(piano_tuple[::2]) #prints: ('do', 'mi', 'mi', 'wa')
print(piano_tuple[::-1]) #prints: ('wa', 'na', 'mi', 'ki', 'mi', 're', 'do')