my_age = input("Input your age:")
age_as_integer = int(my_age)

years_left = 90 - age_as_integer
remaining_days = years_left * 365
remaining_weeks = years_left * 52
remaining_months = years_left * 12

print(f"You have {remaining_days} days, {remaining_weeks} weeks, {remaining_months} months")