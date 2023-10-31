"""
A singly linked list is a collection of nodes that collectively form a linear sequence. Each node stores a reference to
an object that is an element of the sequence, as well as a reference to the next node.

First and last node of linked list are known as the head and tail of the list. Starting from the head node we can
traverse the linked list by following each node's reference until we reach the tail. The tail is the node that has None
as its next reference. Reference of a node can be viewed as a link or pointer; thus, the process of traversing a list is
known as link hopping or pointer hopping.

Each node represents an object stored in memory. Another object represents the linked list as a whole, and it should at
least store the reference to the head of the list. It is also not uncommon to store a reference to the tail, to avoid
needless traversals through the list. We should also consider storing the size of the list (number of nodes) in a
separate reference.
"""

from IPython.display import Image
url ='https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230726162542/Linked-List-Data-Structure.png'


class Node(object):

    def __init__(self, value):

        self.value = value
        self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c


"""
Pros of linked lists:

    -   Linked lists have constant-time insertions and deletions in any position, in comparison, arrays require O(n)
        time to do the same thing since elements need to be shifted after insertion or deletion.
    -   Linked list can continue to expand without having to specify their size ahead of time.
    -   Can be used to implement stack, queue, graph, hash map, etc.
    
Cons of linked lists:

    -   To access an element in a linked list, you need to take O(k) time to go from the head of the list to the kth
        element. Arrays have constant time operations to access elements in an array.
    -   Uses extra memory for storing pointers compared to arrays.
"""