def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month == 2: #this line runs if it is a leap year
#   if is_leap(2022) and month == February
#   if True and month == February
      return 29 #it returns the value 29 days
  return month_days[month - 1] # This line runs if NOT LEAP YEAR #user inputs 1-12 but computer starts from 0, thus the -1
      
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)