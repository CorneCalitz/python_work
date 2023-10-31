alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)


aliens = []

# populate the list with 30 aliens
for alien_number in range(30):
	new_alien = {
				'color':'green',
				'points':5,
				'speed':'slow'
				}
	aliens.append(new_alien)
print('')

# Alter only the first 5 aliens
for alien in aliens[:10]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
	
		

for alien in aliens[:8]:
	print(alien)

# you can store a list inside of a dict
favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
	if len(languages) == 1:
		print(f"\n{name.title()}'s favorite language is:")
		for language in languages:
			print(f"\t{language.title()}")

	else:
		print(f"\n{name.title()}'s favorite languages are:")
		for language in languages:
			print(f"\t{language.title()}")
print()


# You can nest a dict in another dict:

users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}

for username, user_info in users.items():
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}\n")


# Exercises -------------------

pet1 = {'type':'dog',
		'owner':'carl',
		'breed':'golden retriever'}

pet2 = {'type':'cat',
		'owner':'john',
		'breed':'garfield'}

pet3 = {'type':'bird',
		'owner':'samantha',
		'breed':'parrot'}

pets = [pet1, pet2, pet3]

for pet in pets:
	print(f'Pet information:\n\t{pet["type"].title()}\n\t{pet["owner"].title()}\n\t{pet["breed"].title()}\n')

fav_nums = {	'kyle': [1,2],
			'john':5,
			'henro': [6,3],
			'jake':[5,3],
			'rob': 6
			}

for name, fav_num in fav_nums.items():
	if type(fav_num) is int:
		print(f"{name.title()}'s favourite number is \n{fav_num}\n")

	else:
		print(f"{name.title()}'s favourite numbers are")
		for num in fav_num:
			print(f'{num}')
		print()

cities = 	{

			'new york': 
			{	
			'population':5000,
			'country':'United States',
			'fact':'it sucks here'
			},

			'london':
			{
			'population':4000,
			'country':'england',
			'fact':'knives out'
			}

			}

for city, facts in cities.items():
	print(city)
	print(facts)