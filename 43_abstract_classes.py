# prevents a user from creating object of that class (ghost class)
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

class Motorcycle(Vehicle):
    # if no go method error
    def go(self):
        print("You ride the motorcycle")

# vehicle = Vehicle() # not allowed using abstract class
car = Car()
motorcycle = Motorcycle()

vehicle.go()
car.go()



