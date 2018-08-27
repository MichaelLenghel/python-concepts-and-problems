class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		if self.size() == 0:
			print("Must be at least one element in the list")
			return
		else:
			return self.items.pop()

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)

if __name__ == '__main__':
	q = Queue()
	q.enqueue(1)
	q.enqueue("two")
	q.enqueue(True)
	print(q.items)
	print(q.dequeue())
	print(q.items)
