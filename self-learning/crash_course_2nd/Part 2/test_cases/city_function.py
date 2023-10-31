def city_country(city, country, population=''):
	if population:
		line = f'{city} ({population}), {country}'
	else:
		line = f'{city}, {country}'
	return line.title()

