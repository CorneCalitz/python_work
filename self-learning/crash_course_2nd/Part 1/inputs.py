# Example of amulti line string
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!\n")

# Modulus operator
# x % y: y divided by x giving the remainder of the division

num = int(input("Enter a number and ill tell you if its even or odd:\n>>>"))

if num % 10 == 0:
	print("Even")
else:
	print("Odd")

num = int(input("Number to check if it is a multiple of ten:\n>>>"))

if num % 10 == 0:
	print("Multiple of ten")
else:
	print("Not multiple of ten")
