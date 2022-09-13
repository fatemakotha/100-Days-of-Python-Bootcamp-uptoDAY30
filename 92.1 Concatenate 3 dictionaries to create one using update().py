#Write a Python program to concatenate following dictionaries to create a new one using update()
dictionary_1={1:10, 2:20}
dictionary_2={3:30, 4:40}
dictionary_3={5:50,6:60}
concatenated_dic = {}
for d in (dictionary_1, dictionary_2, dictionary_3): concatenated_dic.update(d)
print(concatenated_dic) #prints: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}