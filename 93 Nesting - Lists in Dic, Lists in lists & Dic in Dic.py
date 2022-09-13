# {
#     Key: [List],
#     Key: {Dictionary}
# ) #This is a LIST and a DICTIONARY nested in another DICTIONARY


#NESTING
#Nesting in a LIST:
["A", "B", ["C", "D"]] # 1 list inside another list

#......................................................................................


capitals = {
    "France": "Paris",
    "Bangladesh": "Dhaka",
}
#if we want to NEST a LIST in a DICTIONARY:
travel_log = {
    "France": ["Paris", "Lille", "Dijon"], # 1 KEY 3 VALUES
    "Bangladesh": ["Dhaka", "Barisal", "Chittagong"],
}
print(travel_log)
#prints:
# {'France': ['Paris', 'Lille', 'Dijon'], 'Bangladesh': ['Dhaka', 'Barisal', 'Chittagong']}

#...................................................................................


#if we want to NEST a DICTIONARY IN A DICTIONARY
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}, # 1 KEY 3 VALUES
    "Bangladesh": {"cities_visited": ["Dhaka", "Barisal", "Chittagong"]},
}
print(travel_log)
#prints:
# 'France': {'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visits': 12}, 'Bangladesh': {'cities_visited': ['Dhaka', 'Barisal', 'Chittagong']}}