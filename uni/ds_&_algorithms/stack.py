# Stack works on the principle of “Last-in, first-out”.


# Populate stack with 5 items
def stack_populate():
    data = []
    data.append(90)
    data.append(75)
    data.append(57)
    data.append(85)
    data.append(40)
    return data


# Remove item from stack
def remove_item(data):
    return data.pop()


# View stack
def view_stack():
    print(stack)


print("Choose the following")
print("1. Populate stack with 5 items (marks)")
print("2. View stack")
print("3. Remove an item from stack")

stack = []

while True:
    number = input("Option >>>")
    if number == "1":
        stack = stack_populate()
    elif number == "2":
        view_stack()
    elif number == "3":
        remove_item(stack)
    else:
        print("Choose a number 1,2 or 3")
    print("Command executed")












