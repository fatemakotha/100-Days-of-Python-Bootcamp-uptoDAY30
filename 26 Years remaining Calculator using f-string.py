# How long do we have till we turn 90 and die?

age = int(input("What is your age?"))
age_as_int = int(age) #converts str to int
years_left = 90 - age_as_int 

days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 52

print(f"You have {months_left} months, {weeks_left} weeks, and {days_left} days left to live")

YearsToLive = age / 12
print(YearsToLive)