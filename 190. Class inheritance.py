class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal): #command to INHERIT from class named animal
    def __init__(self):
        super().__init__() #command to INHERIT from class named animal

    def breathe(self): #we want breathe() to have the same functionality but in a little different way
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
# ***calls the breathe() from superclass and prints Inhale, exhale.
#*** adds to the functionality of breathe() superclass and prints

nemo.breathe() #prints: Inhale, exhale.
                      # doing this underwater. 