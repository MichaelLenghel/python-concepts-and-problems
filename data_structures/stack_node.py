class Node:
	def __init__(self, item = None):
		self.item = item
		self.next = None

class Stack:
	def __init__(self):
		self.head = None

	def push(self, item):
		if self.head is None:
			self.head = Node(item)
		else:
			new_node = Node(item) 
			new_node.next = self.head
			self.head = new_node

	def pop(self):
		if self.is_empty():
			print("Must have at least one element in the stack to pop")
			return
		else:
			data = self.head.item
			self.head = self.head.next
			return data

	def is_empty(self):
		return self.head.next == None

	def show(self):
		new_head = Node()
		new_head = self.head
		while new_head != None:
			print(new_head.item, "-->", end=" ")
			new_head = new_head.next
		print("None")

s = Stack()
s.push(10)
s.push(15)
s.push(25)
s.show()
print(s.pop())
s.show()