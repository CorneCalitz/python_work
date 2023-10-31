available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
recipe = {"flour": 500, "eggs": 200, "sugar": 2000}

available_from_recipe = {}

for key, value in available.items():
	print(key)
	print(value)
	if key in recipe.keys():
		available_from_recipe[key] = value


available_from_recipe = sorted(available_from_recipe.items())

print(sorted(recipe.items()))

print(recipe)




