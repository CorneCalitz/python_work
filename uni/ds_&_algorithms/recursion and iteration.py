# Example of recursion

def factorial_recursive(n):
	if n==0:
		return 1
	else: 
		return n * factorial_recursive(n-1)

print(factorial_recursive(5))



# Example of iteration

def factorial_iteration(f):
	product = 1
	for i in range(f):
		product = product * (i+1)

	return product

print(factorial_iteration(5))

