
temp_list = data["temp"].tolist() #converts a SERIESs into a list
print(temp_list)

#Calculating AVERAGE TEMPERATURE:
total_temp = 0
for each_temp in temp_list:
    total_temp += int(each_temp)
avg_temp = total_temp / len(temp_list)
print(avg_temp) #prints: 17.428571428571427

#OR:
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp) #prints: 17.428571428571427

#OR:
avg_temp = data["temp"].mean()
print(avg_temp) #prints: 17.428571428571427