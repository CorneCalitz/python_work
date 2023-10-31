class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


    def search(self, value):
    	if self.val == value:
    		return 'Value exists'

    	elif value < self.val:
    		if self.left:
    			return self.left.search(value)
    		else:
    			return 'Value was not found.'    

    	else:
    		if self.right:
    			return self.right.search(value)
    		else:
    			return 'Value was not found.'

def inorder(root):

    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + ", ", end='')
        # Traverse right
        inorder(root.right)


def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + ", ", end='')


def preorder(root):

    if root:
        # Traverse root
        print(str(root.val) + ", ", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)

	
def response_get():
		flag1 = True

		while flag1:
			try:
				response = int(input('Input response\n>>> '))
				if response < 1 or response > 3:
					print('Please input a number from 1 to 3')
				else:
					flag1 = False

			except ValueError:
				print('Please input a number.')

		return response 


print('1 Populate the tree with at least 8 nodes (items)')
print('2 Search for an item')
print('3 EXIT')

flag2 = False

while True:

	response = response_get()
	
	if response == 1:
		print('Populated tree with 8 nodes')
		root = Node(40)
		root.left = Node(30)
		root.right = Node(60)
		root.left.left = Node(20)
		root.left.right = Node(38)
		root.left.left.left = Node(8)
		root.left.left.right = Node(25)
		root.right.left = Node(50)
		root.right.right = Node(70)

		print("Inorder traversal ")
		inorder(root)

		print("\nPreorder traversal ")
		preorder(root)

		print("\nPostorder traversal ")
		postorder(root)

		flag2 = True


	elif response == 2 and flag2 == True:
		print('Search for an item')
		item = int(input('>>> '))
		print(root.search(item))

	elif response == 2 and flag2 == False:
		print("You first have to populate the tree with values.")
		
		
	elif response == 3:
		exit('Exiting...')

	else:
		print('How did you get this message?')