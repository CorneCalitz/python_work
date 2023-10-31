names = ['Cale','Johan','John']
print(names[0])
print(f'Greetings {names[1]}')

names[0] = 'Gabe'
print(names)

names.append('Cale')
print(names)

del names[1]
print(names)

# Pop can be used to get a variable
popped_name = names.pop(0)
print(names)
print(popped_name)

# Remove does not get a variable in return
names.remove('Cale')
print(names)


# Sorting a list
print("\n===================\n")
alphabet = ['z','a','b','y','e','d']
print(alphabet)
alphabet.sort()
print(alphabet)
alphabet.sort(reverse=True)
print(alphabet)

# list it reset
alphabet = ['z','a','b','y','e','d']

# sorted method is temporary
print('Temp sort:',sorted(alphabet,reverse=True))
print('Original:', alphabet)

# Reverse method which reverses the original order of a list
number = [1,2,3,10,5]
number.reverse()
print(number)