import unittest
from city_function import city_country 

class CityCountryTestCase(unittest.TestCase):
	'''Tests the city_country.py function'''

	def test_city_country(self):
		'''Do a country like 'Berlin, Russia' '''
		formatted_line = city_country('Berlin', 'Russia')
		self.assertEqual(formatted_line,'Berlin, Russia')

	def test_city_country_population(self):
		formatted_line = city_country('Berlin','Russia', 14500)
		self.assertEqual(formatted_line,'Berlin (14500), Russia')

if __name__ == '__main__':
	unittest.main()

