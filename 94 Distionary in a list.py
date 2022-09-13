travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, times_visited, cities_visited): # countries_visited, times_visited, cities_visited are the INPUTS this FUNCTION takes and their values are: "Russia", 2, ["Moscow", "Saint Petersburg"]
    new_country = {}
    new_country["country"] = country_visited #assigns "country" = "Russia"
    new_country["visits"] = times_visited #assigns "visits" = "2"
    new_country["cities"] = cities_visited #assigns "cities" = ["Moscow", "Saint Petersburg"]
    travel_log.append(new_country) #adds "Russia", 2, ["Moscow", "Saint Petersburg"] to the LIST of travel_log

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"]) #a function with 3 inputs
print(travel_log)
#prints:
# [{'country': 'France', 'visits': 12, 'cities': ['Paris', 'Lille', 'Dijon']}, {'country': 'Germany', 'visits': 5, 'cities': ['Berlin', 'Hamburg', 'Stuttgart']}, {'country': 'Russia', 'visits': 2, 'cities': ['Moscow', 'Saint Petersburg']}]