"""
In a doubly linked list, each node contains references to both the next and previous nodes. This allows for
traversal in both forward and backward directions, but it requires additional memory for the backward reference.
"""

url = "https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/03/DLL1.png"


class DoublyLinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None


a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

b.prev_node = a
a.next_node = b

b.next_node = c
c.prev_node = b
