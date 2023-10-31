from name_function import get_formatted_name


print('Enter q at any time to quit.')
while True:
	first = input('\nfirst name:')
	if first == 'q':
		break
	last = input('\nlast name:')
	if last == 'q':
		break

	name = get_formatted_name(first, last)
	print(f'\n---> {name}')

# Module unittest from Python standard library provides tools for testing code.
# unit test verifies that one specific aspect of a function's behaviour is correct.
# a test case is a collection of unit tests that together prove that a function behaves as it's supposed to
