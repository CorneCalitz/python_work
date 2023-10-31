try:
	print(5/0)
except ZeroDivisionError:
	print('You cannnot. Period.')

filename = 'alice.txt'

try:
	with open(filename) as f:
		contents = f.read()

except FileNotFoundError:
	print(f'File {filename} does not exist')


# How to split and count words found in a file
title = 'Alice in Wonderland'
print(title.split())

# Working with multiple files is as simple as creating a function which opens the files
def count_words(filename):
	try:
		with open(filepath,'r') as f:
			contents = f.read()

	except FileNotFoundError:
		# Failing silently
		pass
	else:

		words = contents.split()
		num_words = len(words)
		print(f'The file has about {num_words} words')

filepaths = ['text_files\\jou_ma.txt', 'text_files\\python.txt','text_files\\pi_digits.txt','Fake_file.txt']

for filepath in filepaths:
	count_words(filepath)



