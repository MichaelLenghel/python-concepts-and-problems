class Deque:
	def __init__(self):
		self.items = []

	def add_front(self, item):
		self.items.append(item)

	def add_rear(self, item):
		self.items.insert(0, item)

	def remove_front(self):
		if self.size() == 0:
			print("Must be at least one element in the list")
			return
		else:
			return self.items.pop()

	def remove_rear(self):
		if self.size() == 0:
			print("Must be at least one element in the list")
			return
		else:
			return self.items.pop(0)

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)

if __name__ == '__main__':
	q = Deque()
	q.add_front('hello')
	q.add_front('world')
	print(q.items)
	print(q.remove_rear())
	print(q.remove_front())
	print(q.items)