# Assigned key value pairs
alien_0 = {'color':'green', 'points': 5}
print(alien_0['color'])
print(alien_0)

# Adding new key-value pairs
alien_0['x-pos'] = 0
alien_0['y-pos'] = 25
print(alien_0)

# Modifying a value in dict
alien_0['color'] = 'yellow'
print(alien_0['color'])

# Deleted permanently
del alien_0['points']
print(alien_0)

# .get method allows you to get a key value and set a message if that key value does not exits
point_value = alien_0.get('points','No point value assinged')
print(point_value)
colour = alien_0.get('color','no color')
print(colour)

user = {
		'id':1,
		'name':'john',
		'age': 12
		}

# Loop for a dictionary [Method .items call a list of key-value pairs]
for key, value in user.items():
	print(f'\nKey:{key}')
	print(f'Value:{value}')

# .keys method return only the key values as a list
for key in user.keys():
	print(key)

# .values return only the values as a list
print(user.values())

favourite_languages = {
						'john':'python',
						'sarah':'ruby',
						'handre':'C++',
						'fanie':'C++'}
friends = ['handre', 'john']

for name in favourite_languages.keys():
	print(f"Hello {name.title()}")
	if name in friends:
		language = favourite_languages[name]	# Uses the name of the key to get the paired key value
		print(f"Thank for taking my poll {name.title()}. I see you love {language}")

print('\n')

# can use the sorted function to sort the values
# the set method can also be applied to weed out any repeated values from the dict
for lang in set(sorted(favourite_languages.values(), reverse=True)):
	print(lang.title())

print('')

rivers = {
		'egypt':'nile',
		'namibia':'orange river',
		'mississipi river':'united states',
		'river thames':'england'
		}

for river in rivers.values():
	print(river.title())
print('')
for country in rivers:
	print(country.title())

print('')
poll_takers = ['henro','corne','jan','handre','john']

for taker in poll_takers:
	if taker in favourite_languages.keys():
		print(f"Thank you for responding {taker.title()}.")
	else:
		print(f'Please take the poll {taker.title()}.')


