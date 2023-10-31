import unittest
from employee_function import Employee

class TestEmployeeFunction(unittest.TestCase):

	def setUp(self):
		"""Creates the employee and sets up raise values"""
		self.test_emp = Employee('John', 'Conner', 10000)
		


	def test_give_defualt_raise(self):
		'''Test that the default raise works'''
		self.test_emp.give_raise()
		self.assertEqual(15000 ,self.test_emp.salary)


	def test_give_custom_raise(self):
		'''Test that the custom raise works'''
		self.test_emp.give_raise(1000)
		self.assertEqual(11000, self.test_emp.salary)

if __name__ == '__main__':
	unittest.main()