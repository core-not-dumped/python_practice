from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

# print(Car.wheels) # possible
# Car.wheels = 2 # can change class variable

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print(car_2.wheels)

car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()



