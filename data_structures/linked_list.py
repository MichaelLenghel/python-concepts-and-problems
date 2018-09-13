class Node:
	def __init__(self, item):
		self.item = item
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, item):
		# Insert into linked list without sorting (Each new element  at end): 
		# new_node = Node(item)
		# if self.head is None:
		# 	self.head = new_node
		# 	self.tail = new_node
		# else:
		# 	self.tail.next = new_node
		# 	self.tail = new_node

		# Insert in sorted order
		new_node = Node(item)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			previous = None
			current = self.head
			while current:
				if new_node.item < current.item:
					break
				previous = current
				current = current.next

			# Insert at the head of the list
			if not previous:
				new_node.next = self.head
				self.head = new_node
			# Insert at the end of the list
			elif not current:
				self.tail.next = new_node
				self.tail = new_node
			# Insert in middle
			else:
				previous.next = new_node
				new_node.next = current


	def delete(self, item):

		if self.is_empty():
			print("Must have at least one element in the linkedlist to delete")
			return
		else:
			# Removing from the end of a linked list:
			previous_node = None
			current_node = self.head

			while current_node:
				if current_node.item == item:
					break
				previous_node = current_node
				current_node = current_node.next
			# Else executes if loop terminates normally and no value found
			else:
				print("\n", item, " not found in the list", sep="")
				return

			# Means we are deleting the first element
			if previous_node == None:
				# Removing from start of a linked list
				ele = self.head.item
				self.head = self.head.next
			else:
				ele = current_node.item
				previous_node.next = current_node.next
			return ele


	def is_empty(self):
		return self.head == None

	def show(self):
		temp_head = self.head
		print()
		while temp_head != None:
			print(temp_head.item, end="")
			if temp_head.next:
				print(end=", ")
			temp_head = temp_head.next


if __name__ == '__main__':
	ll = LinkedList()

	
	ll.insert(15)
	ll.insert(25)
	ll.insert(10)
	ll.insert(30)
	ll.insert(11)

	print("Initial list: ") 
	ll.show()

	print("\ndeleted" , ll.delete(25))
	ll.show()
	print("\ndeleted" , ll.delete(18))
	ll.show()
	print("\ndeleted" , ll.delete(10))
	ll.show()
	print("\ndeleted" , ll.delete(15))
	ll.show()
	print("\ndeleted" , ll.delete(1))
	ll.show()
	print("\ndeleted" , ll.delete(11))
	ll.show()