from car import Car, ElectricCar


car = Car('audi','a4',2019)
print(car.get_description())

e_car = ElectricCar('tesla','model s',2020)
print(e_car.get_description())
e_car.battery.describe_battery()

# you can also import a module into another module that needs importing
# For example, we could split the car and electric car modules into seperate modules
# Since the electric car is dependant on the car module you would have to import the
# car module into the electricCar module.