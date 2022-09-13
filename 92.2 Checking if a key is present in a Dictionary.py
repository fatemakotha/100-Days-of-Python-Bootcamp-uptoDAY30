#Write a Python program to check whether a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#REMEMBER the keys are: 1 2 3 4 5 and 6
def is_key_present():
  x = int(input("Input a value for x: "))    
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present()