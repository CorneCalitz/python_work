class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
# Compare the new value with the parent node
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data

# Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()


while True:
	print('1. Populate tree with 5 items')
	print('2. View the tree inorder')
	print('3. View the tree preorder')
	print('4. View the tree postorder')
	print('5. EXIT')

	response = int(input("\n>>>"))
	if response == 1:
		root = Node('Food')
		root.insert('Cheese')
		root.insert('Bread')
		root.insert('Steak')
		root.insert('Tuna')
		root.insert('Chicken')


	elif response == 2:
		view_list()
		print('Marks viewed\n')

	elif response == 3:
		sort_asc()
		print('Marks sorted in ascending order\n')

	elif response == 4:
		sort_desc()
		print('Marks sorted in descending order\n')

	elif response == 5:
		exit()

	else:
		print("Please choose a number in the range of 1 to 5\n")





