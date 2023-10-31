# Queue works on the principle of “First-in, first-out”.

# Populate queue with 5 items
def queue_populate():
    data = []
    data.append(99)
    data.append(70)
    data.append(65)
    data.append(45)
    data.append(80)
    return data


# Remove 1st item from queue
def remove_item(data):
    return data.pop(0)


# View queue
def view_queue():
    print(queue)


print("Choose the following")
print("1. Populate queue with 5 items (marks)")
print("2. View queue")
print("3. Remove an item from queue")
print("4. Exit")

queue = []

while True:
    number = input("Option >>>")
    if number == "1":
        queue = queue_populate()
    elif number == "2":
        view_queue()
    elif number == "3":
        remove_item(queue)
    elif number == "4":
        exit()
    else:
        print("Choose a number 1,2 or 3")
    print("Command executed")

