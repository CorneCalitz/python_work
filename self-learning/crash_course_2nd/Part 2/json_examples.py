import json

numbers = [2, 2 ,1, 4 ,6 ,7, 10]

filename = 'json_files\\numbers.json'
with open(filename, 'w') as f:
	json.dump(numbers, f)

with open(filename) as f:
	numbers_from_file = json.load(f)

print(numbers_from_file)


filename = 'text_files\\username.json'




try:
	with open(filename) as f:
		username = json.load(f)

except FileNotFoundError:
	username = input('What is your name?' )
	with open(filename, 'w') as f:
		json.dump(username,f)
		print(f'We will remember you when you come back, {username}.')

else:
	print(f'Welcome back, {username}.')




