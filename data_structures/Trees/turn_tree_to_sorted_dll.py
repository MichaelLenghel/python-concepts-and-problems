class Node:
	def __init__(self, key):
		self.key = key
		self.previous = self.next = None

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

	# Insert in sorted order from a bst to X
	def insert_from_bst(self, tree, dll):
		if tree:
			self.insert_from_bst(tree.left, dll)
			dll.insert_to_dll(tree.key)
			self.insert_from_bst(tree.right, dll)
		else:
			return

class DLL:
	def __init__(self):
		self.tail = self.head = None

	def insert_to_dll(self, val):
		new_node = Node(val)
		if not self.tail and not self.head:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.previous = self.tail
			self.tail.next = new_node
			self.tail = new_node


	def display_ll(self):
		current = self.head
		while current:
			print(current.key, end="")
			if current.next:
				print(end=", ")
			current = current.next

root = None
tree = BinaryTree()


root = tree.insert(root, 3)
root = tree.insert(root, 5)
root = tree.insert(root, 4)
root = tree.insert(root, 7)
root = tree.insert(root, 2)
root = tree.insert(root, 1)

# Will insert all values from bst to linkedlist in sortedorder
dll = DLL()
ddl_tail = tree.insert_from_bst(root, dll)
dll.display_ll()