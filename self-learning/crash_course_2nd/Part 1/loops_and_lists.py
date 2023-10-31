for x in range(1,6):
	print(x)

# list function can be used to make lists
numbers = list(range(0,11,2))	# range can be used to make steps
print(numbers)

squares = []
for value in range(1,11):
	squares.append(value ** 2)

print(squares)

# same code as above instead as a list comprehension
# N.B.
squares = [value**2 for value in range(1,11)]
print(squares)

numbers = [value for value in range(1,11)]
print(numbers)


cubes = [num**3 for num in range(1,11)]
print(cubes)

# Slicing a list
print(cubes[2:4])
print(cubes[:4])
print(cubes[4:])
# Outputting items from the end of a list
print(cubes[-3:])

for cube in cubes[:3]:
	print(cube)

# Syntax for copying needs to use a slice since copying without a slice means that the list is still
# being referenced to. Any changes in one list will automatically occur in the other list.
copied_cubes = cubes[:]
print(copied_cubes)

cars = ["audi","BMW",'Mercedes','Nissan','Toyota',"Honda","Hyundai"]
print(f'First 3 items in list are {cars[:3]}')
mid = len(cars)//2
print(f'Middle 3 items in list are{cars[mid-1:-mid+1]}')
print(f'Last 3 items in the list are{cars[-3:]}')

my_pizza = ['Pineapple','Pepporoni','Cheese']
friend_pizza = my_pizza[:]
friend_pizza.append("Caribbean")
print(my_pizza)
print(friend_pizza)