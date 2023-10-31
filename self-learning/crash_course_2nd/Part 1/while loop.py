# Moving items from one list to another
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop(0)

	print(f'Verifying user: {current_user.title()}')
	confirmed_users.append(current_user)

print('\nConfirmed users:')
for user in confirmed_users:
	print(f'\t{user.title()}')

# Removing all instances of a specific value from a list
pets = ['dog','cat','parrot','dog','cat','cat','hamster','parrot']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)

# Filling a dictionary with input

response = {}

polling_active = True

while polling_active:
	name = input('\nWhat is your name?')
	mountain = input("Which mountain would you like to climb someday?")

	response[name] = mountain

	repeat = input('Anotha one (y/n)')

	if repeat == 'n':
		polling_active = False

text = 'Polling results'
print(f'{text:-^20}')
for name, mountain in response.items():
	print(f'{name} would like to climb {mountain}')

	
