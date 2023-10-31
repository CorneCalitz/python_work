fName = "john"
lName = "conner"
fullName = f'{fName.title()} {lName.title()}'
message = f'Stupid {fullName}!'
print(message)

language = ' python'
print(language.lstrip())

l = 'python '
print(l.lstrip())

x = ' boom '
print(x.strip())

message =  'He said, "Someone\'s Pachinko machine rocketed into the sky during the explosion."'
print(message)

string = '123456789'
for i in range(len(string)):
	print(i)
	print(string[i],string[i-len(string)+1])