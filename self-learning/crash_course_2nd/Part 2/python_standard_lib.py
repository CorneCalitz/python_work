from random import randint
print(randint(1,10))

# This method chooses a random value from a list or tuple
from random import choice
players = ['charles','martina','michael','florence','hope']
first_up = choice(players)
print(first_up)

for i in range(10):
	print(randint(1,6))