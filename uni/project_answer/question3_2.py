class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.element = item

def inorder(tree):

    if tree:
        inorder(tree.left)
        print(str(tree.element), end=' ')
        inorder(tree.right)

def preorder(tree):

    if tree:
        print(str(tree.element), end=' ')
        preorder(tree.left)
        preorder(tree.right)


tree = Node('E')
tree.left = Node('X')
tree.right = Node('N')
tree.left.left = Node('A')
tree.left.right = Node('U')
tree.left.left.left = Node('M')
tree.left.left.right = Node('F')


print("Inorder traversal yields:")
inorder(tree)

print("\n\nPreorder traversal yields:")
preorder(tree)



