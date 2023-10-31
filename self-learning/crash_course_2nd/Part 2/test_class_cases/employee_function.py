class Employee:
	"""Represent an employee with a salary"""
	def __init__(self, first_name, last_name, salary):
		"""Initiator"""
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary

	def give_raise(self, raise_= 5000):
		"""Gives employee a raise"""
		self.salary += raise_

	def show(self):
		"""print the employee's information"""
		print(f'{self.first_name} {self.last_name} | R{self.salary}')


