student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [55, 76, 98]
}

#ITERATE OVER DICTIONARIES:
for (key, value) in student_dict.items():
    print(key)
    #prints:
    # student
    # score
    print(value)
    # prints:
    # ['Angela', 'James', 'Lily']
    # [55, 76, 98]

#ITERATE OVER DATAFRAME:
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
#prints:
#   student  score
# 0  Angela     55
# 1   James     76
# 2    Lily     98

#Loop through DATAFRAME: (loops through columns) **
for (key, value) in student_data_frame.items():
    print(key) #prints only keys
    print(value) #prints only values

#LOOP THROUGH EACH ROW OF A DATA FRAME:(loops through each row)
for (index, row) in student_data_frame.iterrows(): #row is the given name 
    # print(index) #prints
    # 0
    # 1
    # 2
    # print(row)  # prints
    # student
    # Angela
    # score
    # 55
    # Name: 0, dtype: object
    # student
    # James
    # score
    # 76
    # Name: 1, dtype: object
    # student
    # Lily
    # score
    # 98
    # Name: 2, dtype:
    # print(row.student) #prints:
    # Angela
    # James
    # Lily
    # print(row.score) #prints:
    # 55
    # 76
    # 98
    if row.student == "Angela":
        print(row.score) #prints: 56 ** which is the score for Angela