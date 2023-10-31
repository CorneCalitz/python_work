def addition():
	num1 = 0
	while True:
		try:
			num2 =int(input(f'Please input a number to add to {num1}.\n>>>'))
			num1 += num2

		except ValueError:
			print('You cannot add a string value to an integer value. Baka!')

		else:
			print(f' = {num1}')

def make_files():
	filename = 'dogs.txt'
	try:
		with open(f'text_files\\{filename}','w') as f:
			f.write('Jason\n')
			f.write('Parker\n')
			f.write('Fiona\n')

	except FileNotFoundError:
		print(f'File {filename} could not be made')

	else:
		print(f'File {filename} made successfully')

	filename = 'cats.txt'
	try:
		with open(f'text_files\\{filename}','w') as f:
			f.write('Mewto\n')
			f.write('Nibbles\n')
			f.write('Klepto\n')

	except FileNotFoundError:
		print(f'File {filename} could not be made')

	else:
		print(f'File {filename} made successfully')

def read_files(filename, filepath):
	try:
		with open(filepath, 'r') as f:
			lines = f.readlines()

	except FileNotFoundError:
		print(f'\n{filename} does not exist')

	else:
		print(f'\n{filename} contents')
		for line in lines:
			print(f'\t{line.rstrip()}')

make_files()
read_files('dogs.txt','text_files\\dogs.txt')
read_files('cats.txt','text_files\\cats.txt')