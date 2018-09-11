class BinaryTree:
	def __init__(self, key = None):
		self.key = key
		self.left = self.right = None
		self.counter = 0

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
			print("\ncounter = ", self.counter, end="")
			self.counter+= 1
			return -1
		else:
			self.counter+= 1
			return 1 + max(self.get_height(root.left), self.get_height(root.right))

	def bfs(self, root):
		queue = [root] if root else []
		while queue:
			node = queue.pop()
			print(node.key, end=" ")

			if node.left: queue.insert(0, node.left)
			if node.right: queue.insert(0, node.right)

	def dfs(self, root):
		print(root.key, end=", ")
		if root.left:
			self.dfs(root.left)
		if root.right:
			self.dfs(root.right)


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
