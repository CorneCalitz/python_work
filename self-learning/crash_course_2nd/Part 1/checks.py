list_ = [1,4,5,3]
if 1 in list_:
	print("Yes")
else:
	print("no")

alpha = ['x','a','b','g']
if 'h' in alpha:
	print("Yes")
else:
	print("no")

# N.B. You can check an entire list this way
if 'a' in alpha:
	print('y')

if 'h' not in alpha:
	print('true')

letter = 'x'

if letter in alpha:
	print('True')


toppings = ['mushroom','cheese','peppers']
for topping in toppings:
	if topping == 'peppers':
		print("No peppers, sorry.")

	else:
		print("Adding ",topping)

print('\n Finished making your pizza')


# Checks for an empty list
toppings = []
if toppings:
	print(toppings)

else :
	print("\nReally, no toppings?")

available_toppings = ('mushroom','cheese','peppers')
requested_toppings = ['mushroom','french fries']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f'\nAdding {requested_topping}.')

	else:
		print(f'Sorry, we do not have {requested_topping}.')

print("\n---------Admin code----------")
users = ["john","admin",'sam','user','cory']

if users:
	for user in users:
		if user == 'admin':
			print(f'Hello {user.title()}, would you like to see a status report.')
		else:
			print(f'Hello {user.title()}, thank you for logging in.')

else:
	print("We need more users.")

print("\n---------Username code----------")
current_users = ['ADMIN','USER1','JOHN','USER2']
new_users = ['user3','user1']


for new_user in new_users:
	if new_user.upper() in current_users:
		print(f'Username "{new_user}" already in use. Please use a different username.')
	else:
		print(f'Username "{new_user}" is available.')

numbers = list(range(1,10))

for number in numbers:
	if number == 1:
		print(f'{number}st')
	elif number == 2:
		print(f'{number}nd')
	elif number == 3:
		print(f'{number}rd')
	else:
		print(f'{number}th')












