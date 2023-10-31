# \\ is an escape sequence
filepath = 'text_files\\pi_digits.txt'

# All files must be opened first
#When the with block finishes executing the file closes
with open(filepath)  as file_object:
	contents = file_object.read()

# The read function creates an extra blank line at the end of the file
# You remove it using the strip function
print(contents.rstrip())

print('')

with open(filepath) as file_object:
# This is how you print line for line
	for line in file_object:
		print(line.rstrip())

print('')


with open(filepath) as file_object:
	# You can also 
	lines = file_object.readlines()

print(lines)
for line in lines:
	print(line.rstrip())

print('')
pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

with open('text_files\\pi_1mil.txt') as file:
	lines = file.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print(f'{pi_string[:52]}...')
print(len(pi_string))

birthday = '200402'
if birthday in pi_string:
	print('yes')
else:
	print('no')

print('')
with open('text_files\\python.txt') as file:
	lines = file.readlines()


for line in lines:
	line = line.replace('Python', 'C')
	line = line.replace('python', 'C')
	print(line.rstrip())


# Reading and writing to a file are done using several modes.
# read mode (r) write mode (w) append mode (a) read and write mode (r+).
# Write mode will override any text that which pre-exists in a file.
filename = 'text_files\\programming.txt'

with open(filename, 'w') as file:
	file.write("Rather die living your own life than to succeed in living someone else's.\n")
	file.write("Only an exceptional man is allowed to overstep the boundaries of the law.\n")

with open(filename, 'r') as file:
	print(file.read())

with open(filename, 'a') as file:
	file.write('Watson! What is the meaning of this!\n')

with open(filename, 'r') as file:
	print(file.read())





