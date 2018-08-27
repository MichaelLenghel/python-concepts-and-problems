class Node:
	def __init__(self, item):
		self.item = item
		self.next = None

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	def enqueue(self, item):
		if self.head is None:
			self.head = Node(item)
			self.tail = Node(item)
		else:
			new_node = Node(item)
			# Make reference to next element if node deleted
			if self.head.next == None:
				self.head.next = new_node
			self.tail.next = new_node
			self.tail = new_node

	def dequeue(self):
		if self.is_empty():
			print("Must have at least one element in the queue to dequeue")
			return
		else:
			ele = self.head.item
			self.head = self.head.next
			return ele

	def is_empty(self):
		return self.head == None

	def show(self):
		temp_head = self.head
		print()
		while temp_head != None:
			print(temp_head.item)
			temp_head = temp_head.next

q = Queue()
while True:
	print('enqueue <value>')
	print('dequeue')
	print('quit')
	do = input('Pick an option above ').split()

	operation = do[0].strip().lower()
	if operation == 'enqueue':
		q.enqueue(int(do[1]))
	elif operation == 'dequeue':
		q.dequeue()
	elif operation == 'quit':
		print("Quiting...")
		break
	else:
		print("Invalid operation entered, try again")
	q.show()