"""
A stack is an ordered collection of items where the addition of new items and the removal of existing items always takes
place at the same end. End is referred to as the 'top' and the opposite of the top is known as the 'base'
Items stored closer to the base of the stack have been in the stack for the longest period of time. The most recently
added item is the one that gets removed first.

Ordering principle known as LIFO, last-in first-out.
Newer items are near the top and older items are near the base.
"""

from IPython.display import Image
url ='https://upload.wikimedia.org/wikipedia/commons/b/b4/Lifo_stack.png'

Image(url)

"""
Items are 'pushed' into the base and 'popped' out. Stacks are used to reverse the order of items. The order of insertion
is the reverse order of removal.

Examples of stacks is your web browser stacking webpages as you traverse them. The top is the current webpage you are on
The back button 'pops' the current webpage(url) from the stack and allows you to go back to the previous webpage in the 
base of the stack.
"""

"""
Stack operations

-Stack(): creates an empty stack.
-push(item): adds a new item to the top of the stack.
-pop(): removes the top item from the stack.
-peek(): returns the top item from the stack.
-isEmpty(): tests to see whether the stack is empty.
-size(): return the numbers of the items

"""

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

s = Stack()
print(s.isEmpty())
s.push(1)
s.push('two')
print(s.peek())
s.push(2)
print(s.size())
s.pop()
s.pop()
print(s.size())
s.pop()
print(s.isEmpty())


