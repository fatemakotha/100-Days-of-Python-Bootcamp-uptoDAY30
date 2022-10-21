
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
#SCENARIO 1:
my_car = Car(make="Toyota", model="Axio") #set the inputs manually
print(my_car.model) #prints: Axio
print((my_car.make)) #Toyota

#SCENARIO 2:
my_car = Car(make="Toyota") #set the inputs manually
print(my_car.model)
print((my_car.make))
#prints: my_car = Car(make="Toyota", model=) #set the inputs manually
        # SyntaxError: invalid syntax
        #BECAUSE WE DID NOT SPECIFY "model"

#SCENARIO 3:
my_car = Car(make="Toyota", model="") #set the inputs manually
print(my_car.model) #prints: Axio
print((my_car.make)) #prints: Toyota
#NO ERROR AS model is set to an empty string ""

#SCENARIO 4:
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_new_car = Car(make="Toyota") #model NOT SPECIFIED BUT STILL NO ERROR as we used the get() method **
print(my_new_car.model) #prints: NONE