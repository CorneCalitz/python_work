def fibonacci(x):
	if x < 2:
		return x
	else:
		return fibonacci(x - 1) + fibonacci(x - 2)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(10))