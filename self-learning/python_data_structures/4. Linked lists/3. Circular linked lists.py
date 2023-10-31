"""
The circular linked list is a linked list where all nodes are connected to form a circle. In a circular linked
list, the first node and the last node are connected to each other which forms a circle. There is no NULL at the end.

You can create singly and doubly circular linked lists, but it has to be known that circular lists are can become very
complicated when used to implement other data structures.

Pros of circular linked lists:

    -   Any node can be the starting point. We just need to stop traversing once we visit the starting point again.
    -   Perfect for applications that repeatedly go around the list. Exp. Multiple applications running on a PC
"""

singly_circular = "https://media.geeksforgeeks.org/wp-content/uploads/20220817185024/CircularSinglyLinkedList-660x172.png"
doubly_circular = "https://media.geeksforgeeks.org/wp-content/uploads/20220817185057/Circulardoublylinkedlist-660x155.png"


class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


one = Node(3)
two = Node(5)
three = Node(9)

one.next = two
two.next = three
three.next = one

# insertion
zero = Node(1)
zero.next = one
three.next = zero
