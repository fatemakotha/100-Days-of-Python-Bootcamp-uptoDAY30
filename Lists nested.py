dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
#how to divide them into fruits and vegetables?
#METHOD 1
#we can make two seperate lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]


#or we can use METHOD 2 "NESTED LIST"

dirty_dozen = [fruits, vegetables]#this gives 2 lists[[dsd, asdas, sds],[sdsd, sda, asd]]
print(dirty_dozen)