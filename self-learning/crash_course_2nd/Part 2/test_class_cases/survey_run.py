from survey import AnonymousSurvey

# Define question and instantiate the object
question = 'First game you ever completed?'
my_survey = AnonymousSurvey(question)

# Show question and store responses
my_survey.show_question()
print('Enter q to quit')

while True:
	response = input('Game: ')
	if response == 'q':
		break
	my_survey.store_response(response)

# Show survey results
print('\nThanks for participating.')
my_survey.show_results()
