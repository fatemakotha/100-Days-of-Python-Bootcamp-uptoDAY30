def my_function():
  # for i in range(1, 20): #won't work as range is upto 20 which means 19 starting from 0
  for i in range(1, 21): #so instead we write this line
    if i == 20:
      print("You got it")
my_function()