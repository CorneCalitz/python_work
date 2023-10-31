"""
A deque, known as a double-ended queue, is an ordered collection of items similar to the queue. It has two ends, a front
and a rear, and items remain positioned in teh collection. New items can either be added at the front or the rear. Items
can also be removed from the front or the rear.

Dequeues can assume the characteristics of stacks and queues, but it is up to you to decide how data is removed or added
in this data structure.

"""

from IPython.display import Image
Image('http://www.codeproject.com/KB/recipes/669131/deque.png')

"""
Deque operations

-Deque(): creates a new deque that is empty.
-addFront(item): adds a new item to the front of the deque.
-addRear(item): adds a new item to the rear of of the deque.
-removeFront(): removes the front item from the deque.
-removeRear(): removes the rear item from the deque.
-isEmpty(): tests to see whether the deque is empty.
-size(): returns the number of items in the deque.

"""

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


d = Deque()
d.addFront('hello')
d.addRear('world')
print(d.size())
print(d.removeFront() + ' ' +  d.removeRear())
print(d.size())
