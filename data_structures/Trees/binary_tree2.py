class BinaryTree:
	def __init__(self, key = None):
		self.key = key
		self.left = self.right = None
		self.counter = 0
		self.tree_vals = []

	def insert(self, root, key):
		if root == None:
			root = BinaryTree(key)
		else:
			if key <= root.key:
				cur = self.insert(root.left, key)
				root.left = cur
			else:
				cur = self.insert(root.right, key)
				root.right = cur
		return root


	def delete(self, key):
		pass

	def get_height(self, root):
		
		if root is None:
			return -1
		else:
			return 1 + max(self.get_height(root.left), self.get_height(root.right))

	def bfs(self, root):
		queue = [root] if root else []
		while queue:
			node = queue.pop()
			print(node.key, end=" ")

			if node.left: queue.insert(0, node.left)
			if node.right: queue.insert(0, node.right)

	# Uses inorder traversal
	def sort(self, root):
		if root.left:
			self.sort(root.left)
		print(root.key, end=", ")
		if root.right:
			self.sort(root.right)

	# Uses preorder traversal
	def dfs(self, root):
		print(root.key, end=", ")
		if root.left:
			self.dfs(root.left)
		if root.right:
			self.dfs(root.right)

	# Given a binary tree
	# check if a binary search tree
	def val_bst(self, root):
		if root.left:
			if root.key > root.left.key:
				print("broke")
				return False
			self.val_bst(root.left)
		if root.right:
			if root.key < root.left.key:
				return False
			self.val_bst(root.right)
		return True


	def inorder_binary_check(self, tree):
		if tree:
			self.inorder_binary_check(tree.left)
			self.tree_vals.append(tree.key)
			self.inorder_binary_check(tree.right)
		return self.tree_vals == sorted(self.tree_vals)


root = None
tree = BinaryTree()

root = tree.insert(root, 3)
root = tree.insert(root, 5)
root = tree.insert(root, 4)
root = tree.insert(root, 7)
root = tree.insert(root, 2)
root = tree.insert(root, 1)

print("Breath first search traversal: ")
tree.bfs(root)
print("\nDepth first search traversal: ")
tree.dfs(root)
print("\nHeight of tree is: {}".format(tree.get_height(root)))

if tree.inorder_binary_check(root):
	print("Is a binary search tree")
else:
	print("Not a binary search tree")

print("Binary tree sorted: ")
tree.sort(root)

# if tree.val_bst(root):
# 	print("Is a binary search tree")
# else:
# 	print("Not a binary search tree")
