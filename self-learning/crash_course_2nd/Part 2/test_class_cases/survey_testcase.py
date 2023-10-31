import unittest
from survey import AnonymousSurvey
'''
Different types of assertions that can be tested for
 - assertEqual(a, b)		Verify that a == b
 - assertNotEqual(a, b)		Verify that a != b
 - assertTrue(x)			verify that x is True
 - assertFalse(x)			verify that x is False
 - assertIn(item, list)		verify that item is in list
 - assertNotIn(item, list)	verify that item is not in list
'''



class TestAnonymousSurvey(unittest.TestCase):
	'''Tests for the class AnonymousSurvey'''

	# setUp method is ran before every method starting with test
	# This method creates instances of any class which you want to test
	def setUp(self):
		'''Create a survey and set of responses for use in all test methods.'''
		question = 'First game you ever completed?'
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['God of War', 'Uncharted 3', 'Metal Gear Solid']

	def test_store_single_response(self):
		'''Test that a single response is stored properly.'''
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		'''Test that 3 individual responses are stored properly'''
		for response in self.responses:
			self.my_survey.store_response(response)

		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
	unittest.main()


