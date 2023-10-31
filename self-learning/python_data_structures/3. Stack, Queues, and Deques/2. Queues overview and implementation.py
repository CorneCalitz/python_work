"""
A queue is an ordered collection of items where the addition of new items happens at the one end, called the 'rear', and
the removal of existing items occurs at the other end, called the 'front'. As an element enters teh queue it starts at
the rear and makes its way toward the front, waiting until the next element has been removed.

Recently added items in must wait at the end of the collection. The item that has been in the collection the longest is
at the front. This ordering principle is called FIFO, first-in first-out. (first come first served)

Think of a line at a movie or a checkout line at a grocery store.

Items added to the front are enqueued and items removed from the rear are dequeued.

"""

from IPython.display import Image

url = 'https://netmatze.files.wordpress.com/2014/08/queue.png'
Image(url)

"""
Queue operations

-Queue(): creates a new queue that is empty.
-enqueue(): adds a new items to the rear of the queue.
-dequeue(): removes the front item from the queue.
-isEmpty(): test to see whether the queue is empty.
-size: returns the number of items in the queue.

"""


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
print(q.size())
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
