# Play Computer
year = int(input("What's your year of birth?")) #produces an error if we type 1994 **
if year >= 1980 and year < 1994:
  print("You are a millenial.")
# elif year > 1994: #this line makes the error. It has to be set to >=
elif year >= 1994:
  print("You are a Gen Z.")
#Now if you type in 1994 it prints: "You are a Gen Z."