class BinaryTree:
	def __init__(self, key):
		self.key = key
		self.right = None
		self.left = None


	def insert_left(self, item):
		if self.left == None:
			self.left = BinaryTree(item)
		else:
			t = BinaryTree(item)
			t.left = self.left
			self.left = t

	def insert_right(self, item):
		if self.right == None:
			self.right = BinaryTree(item)
		else:
			t = BinaryTree(item)
			t.right = self.right
			self.right = t

	def get_right(self):
		return self.right

	def get_left(self):
		return self.left

	def set_root_val(self, val):
		self.key = val

	def get_root_val(self):
		return self.key

	# Method of preorder
	# def preorder(self):
	# 	print(self.key)

	# 	if self.left:
	# 		self.left.preorder()
	# 	if self.right:
	# 		self.right.preorder()

# Get root value first
# Equivalent to a depth first search (Stack)
def preorder(tree):
	if tree:
		print(tree.get_root_val())
		preorder(tree.get_left())
		preorder(tree.get_right())

# Get root value last
# Used for deleting values from a tree
def postorder(tree):
	if tree:
		postorder(tree.get_left())
		postorder(tree.get_right())
		print(tree.get_root_val())

# Get root vlaue in the middle
# Equivalent to sorting a binary search tree
def inorder(tree):
	if tree:
		inorder(tree.get_left())
		print(tree.get_root_val())
		inorder(tree.get_right())


r = BinaryTree('a')
r.insert_left('b')
r.insert_right('c')
r.insert_left('d')
r.insert_right('e')
r.insert_left('g')


print("Preorder traversal: ")
preorder(r)
print("Postorder traversal: ")
postorder(r)
print("Inorder traversal: ")
inorder(r)