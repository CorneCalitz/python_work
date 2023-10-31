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


class Battery:

	def __init__(self, battery_size=75):
		self.battery_size = battery_size

	def describe_battery(self):
		print(f'The car has a {self.battery_size}--kWh battery')


class ElectricCar(Car):

	def __init__(self, make , model, year):
		
		super(). __init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank(self):
		print('This car has no gas tank')



