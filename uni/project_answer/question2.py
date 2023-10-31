class ArrayStack:

    def __init__(self, name):
        self.data = []
        self.name = name

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0
            
    def push(self, element):
        # At new element to top of stack
        self.data.append(element)

    def top(self):
        # Return element at top of stack
        if self.is_empty():
            raise 'Stack is empty'
        return self.data[-1]

    def pop(self):
        # Remove and return element at the top of stack
        if self.is_empty():
            raise 'Stack is empty'
        return self.data.pop()

    
def transfer_stack(stack_from, stack_to):
    # This function will transfer the stack to another stack following the last-in, first-out principle
    # Take not that it will also alter the data found in the current object's stack
    print(f'{stack_from.name} : {stack_from.data}')
    print(f'Length of {stack_from.name} before the transfer: {stack_from.__len__()}')
    print(f'{stack_to.name} : {stack_to.data}')
    print(f'Length of {stack_to.name} before the transfer: {stack_to.__len__()}')
    print(f'Item at the top of {stack_from.name} : {stack_from.top()}')

    temp1 = stack_from.data
    temp2 = stack_to.data
    stack_to.data = []
    stack_from.data = []

    for i in range(temp1.__len__()):
        stack_to.push(temp1.pop())

    for i in range(temp2.__len__()):
        stack_from.push(temp2.pop())

    print('\nThe transfer was done successfully\n')
    print(f'Item at the top of {stack_to.name} : {stack_to.top()}')
    print(f'Length of {stack_from.name} after transfer: {stack_from.__len__()}')
    print(f'Length of {stack_to.name} after transfer: {stack_to.__len__()}')
    print(f'{stack_to.name} after transfer : {stack_to.data}')
    print(f'{stack_from.name} after transfer: {stack_from.data}')


# Creation of stack S
S = ArrayStack('Stack S')
S.push(10)
S.push(25)
S.push(15)
S.push(7)

# Creation of stack T
T = ArrayStack('Stack T')

# stack S --> stack T | initial stack T --> stack S
transfer_stack(stack_from=S, stack_to=T)
















    








