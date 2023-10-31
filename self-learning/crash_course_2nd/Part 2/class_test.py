class Dog:

	# A function that is part of a class is called a method
	# __init__ method is called automatically whenever the class is set.
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(self.name, 'decided to sit')

	def roll_over(self):
		print(self.name, 'rolled over')


my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Jameson', 7)
your_dog.sit()


class Car:

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0

	def get_description(self):
		long_name = f'{self.year} {self.make} {self.model}'
		return long_name.title()

	def read_odometer(self):
		print(f'This car has {self.odometer} miles on it.')

	def update_odometer(self, mileage):
		if mileage >= self.odometer:
			self.odometer = mileage
		else:
			print('Cannot rollback odometer')
	def add_miles(self, miles):
		self.odometer += miles

	def fill_gas_tank(self):
		print("Gas tank is full")



new_car = Car('audi','a4',2019)
print(new_car.get_description())
# Change the value directly
new_car.odometer = 23
new_car.read_odometer()

# Change value using a method
new_car.update_odometer(100)
new_car.read_odometer()
new_car.add_miles(12)
new_car.read_odometer()


''' CLASS INHERITANCE '''

# Sometimes adding to many attributes describing one thing to a class can lead to clutter
# You can create seperate classes describing attributes in another class
# Take for instance the battery from the electric car.
class Battery:

	def __init__(self, battery_size=75):
		self.battery_size = battery_size

	def describe_battery(self):
		print(f'The car has a {self.battery_size}--kWh battery')


# Creates a child class
class ElectricCar(Car):

	def __init__(self, make , model, year):
		# Initialize varaibles of the parent class
		# Parent class = superclass
		# Child class = subclass
		super(). __init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank(self):
		# you can override the methods from the parent class
		print('This car has no gas tank')

# Parent class must be part of the current file
my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_description())

my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()












