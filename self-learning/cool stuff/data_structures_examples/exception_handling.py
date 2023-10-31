y = 0
x = 1

if y != 0:
	ratio = x/y
else:
	print("Look before you leap.")


try:
	ratio = x/y
except ZeroDivisionError:
	print("It is always easier to ask for forgiveness than it is to get permission.")

"""The relative advantage of using a try-except structure is that the non-exceptional
case runs efficiently, without extraneous checks for the exceptional condition. However,
handling the exceptional case requires slightly more time when using a tryexcept
structure than with a standard conditional statement. For this reason, the
try-except clause is best used when there is reason to believe that the exceptional
case is relatively unlikely, or when it is prohibitively expensive to proactively evaluate
a condition to avoid the exception."""

try:
	fp = open('sample.txt')
except IOError as e:
	print('Unable to open the file: ', e)

age = -1

while age <=0:	# Initial invalid response
	try:
		age = int(input('Enter your age >>>'))
		if age <= 0:
			print('Age must be positive')
	except (ValueError, EOFError):
		print("Invalid response.")
		pass # instead of repsonse we can use pass to continue the while loop

age = -1

while age <=0:	# Initial invalid response
	try:
		age = int(input('Enter your age again >>>'))
		if age <= 0:
			print('Age must be positive')
	except ValueError:
		print("Invalid response.")
	except EOFError:
		print("Yikes")
		raise		# Re-raises this exception

	

