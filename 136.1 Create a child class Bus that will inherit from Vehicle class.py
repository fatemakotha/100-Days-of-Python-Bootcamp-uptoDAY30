# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

#CLASS: Vehicle
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
#CHILD CLASS: Bus
class Bus(Vehicle):
    pass

#OBJECT: School_bus
School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)