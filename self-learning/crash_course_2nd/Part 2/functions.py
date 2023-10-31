def greet(username): # parameter being used within the function
	print(f'Hello {username}')


greet('John') # argument being called


# Poisitional arguments
'''When you call a function, Python must match each argument in the
function call with a parameter in the function definition. The simplest
way to do this is based on the order of the arguments provided. Values
matched up this way are called positional arguments.'''

def describe_pet(pet_name='henry', animal_type='dog'): # Parameter using a defualt value
	print(f'\nI have a {animal_type}')
	print(f"My {animal_type}'s name is {pet_name.title()}.")

# The order of the function arguments are important
describe_pet('harry','hamster')
describe_pet('odie','dog')

# Keyword arguments
describe_pet(pet_name='garfield', animal_type='cat')

# Call using no arguments and relying on defualt values
describe_pet()

def get_formatted_name(first_name, last_name, middle_name=''):
	'''Return a full name, neatly formatted'''
	# Optional function call using a return
	# Optional since not everyone has a middle name

	if middle_name:
		full_name = f'\n{first_name} {middle_name} {last_name}'
	else:
		full_name = f'\n{first_name} {last_name}'
	return full_name.title()


print(get_formatted_name('jimi','hendrix'))
print(get_formatted_name('john','hooker','lee'))

def build_person(fname, lname, age=None):
	person  = {'first':fname, 'last':lname}
	if age:
		person['age'] = age
	return person

man = build_person('john','conner', age=50)
print(man)
man = build_person('winston','churchill')
print(man)
print()

# Formatting a list using a function
def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f'Printing model: {current_design}')
		completed_models.append(current_design)


def show_completed_models(completed_models):
	print('\nThe following models have been printed:')
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['robot','phone case', 'bottle']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
# the list becomes empty
# If we want to keep the original values from the unprinted list we can send a copy as an argument
# We do this by slicing the list

unprinted_designs = ['robot','phone case', 'bottle']
completed_models = []

print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
# this method should be used sparingly since working with large lists can be cumbersone
# on memory and it will become even worse if you use copies of large lists

# Function relying on arbitary number of arguments
# Single * asterisk before a parameter is going to collect the argument as a tuple
def make_pizza(size,*toppings):
	print(f"\nMaking a size {size} pizza with the following toppings:")
	for topping in toppings:
		print(topping)

make_pizza(12,'pepporoni')
make_pizza(14,'mushrooms','green peppers','cheese')

# Double asterisk collects the arguments as a dictionary
def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein', location='princeton',field='physics')

print(user_profile)


def sandwich_order(*args):
	print('Sandwich order:')
	for topping in args:
		print(f'\t{topping}')


sandwich_order('Cheese','Mayo','Ham')
sandwich_order('Cheese','Bread')

def car_information(manufacturer, model_name, **car_info):
	car_info['manufacturer'] = manufacturer
	car_info['model_name'] = model_name
	return car_info

print(car_information('BMW', 'M4', colour='green', type='A'))








