# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.


#CLASS name: Vehicle
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
#OBJECT name: modelX, modelY and modelZ
modelX = Vehicle(240, 18) 
print(modelX.max_speed, modelX.mileage) #prints: 240 18

modelY = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage) #prints: 240 18

modelZ = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage) #prints: 240 18