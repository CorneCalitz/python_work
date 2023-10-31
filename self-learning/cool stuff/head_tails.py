import random

enter = input("Press ENTER to flip the coin\n")

num = random.randint(1,2)
if num == 1:
	print("Heads!\nWilliam wins")
else:
	print("Tails\nCorne wins")