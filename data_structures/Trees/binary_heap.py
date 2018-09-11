# Enqueue and dequeue is O(log N)`\
# Using a complete binary tree (Where are levels contain max amount of nodes)
# Min heap

class BinHeap:
	def __init__(self):
		self.heap_list = [0]
		self.current_size = 0

	def insert(self, item):
		self.heap_list.append(item)
		self.current_size += 1
		self.sift_up(self.current_size)

	def sift_up(self, i):
		while i // 2 > 0:
			if self.heap_list[i] < self.heap_list[i // 2]:
				# Swap the elements
				self.heap_list[i], self.heap_list[i // 2] = \
				self.heap_list[i // 2],  self.heap_list[i]
			i = i // 2

	def del_min(self):
		# Will be element at top
		retval = self.heap_list[1]
		self.heap_list[1] = self.heap_list[self.current_size]
		self.current_size -= 1
		self.heap_list.pop()
		self.sift_down(1)
		return retval

	def sift_down(self, i):
		while i * 2 <= self.current_size:

			mc = self.min_child(i)
			if self.heap_list[i] > self.heap_list[mc]:
				# Swap the elements
				self.heap_list[i], self.heap_list[mc] = \
				self.heap_list[mc],  self.heap_list[i]
				i = mc

	def min_child(self, i):
		if i * 2 + 1 > self.current_size:
			return i * 2
		else:
			if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
				return i * 2
			else:
				return i * 2 + 1

	def is_empty(self):
		pass

	def size(self):
		pass

	def show_heap(self):
		for i, x in enumerate(self.heap_list):
			if x != 0:
				print(x, end="")
			if i < self.current_size and i != 0:
				print(end=", ")

	# O(N) if create from list as don't need to worry about branches at the bottom since they have no children
	def build_heap(self, alist):
		i = len(alist) // 2
		self.current_size = len(alist)
		self.heap_list = [0] + alist[:]
		while i > 0:
			self.sift_down(i)
			i = i - 1
		


bin_heap = BinHeap()
bin_heap.insert(10)
bin_heap.insert(5)
bin_heap.insert(4)
bin_heap.insert(1)
bin_heap.insert(20)
bin_heap.show_heap()
bin_heap.del_min()
print("\nRemoving min val: ")
bin_heap.show_heap()

bin_heap_list = BinHeap()

li = [9, 6, 5, 2, 3]
bin_heap_list.build_heap(li)

print("List heap: ")
bin_heap_list.show_heap()
