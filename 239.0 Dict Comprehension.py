#EXAMPLE 1 :
#Takes each letter in sentence and counts letters in word:
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list = sentence.split() #['What', 'is', 'the', 'Airspeed', 'Velocity', 'of', 'an', 'Unladen', 'Swallow?']
print(word_list)
result = {word:len(word) for word in word_list }
print(result) #{'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

#EXAMPLE 2 :
# Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius
# and converts it into degrees Fahrenheit.
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()} #**** dic.items() iterates through all key value pairs in a dic

print(weather_f) #prints: {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}