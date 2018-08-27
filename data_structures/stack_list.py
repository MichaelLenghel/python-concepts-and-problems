# Stacks can be used to reverse the order of items. E.g. 1,2,3,4,5 insertd and result is: 5,4,3,2,1. By popping wwe start from 5
# Every website has a backbutton, this is a stack to remember which website u last visited.

class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if self.size() == 0:
			print("Must be at least one element in the list")
			return
		else:
			print(self.items.pop())

	def peek(self):
		return self.items[len(self.items) - 1]

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)


if __name__ == '__main__':
	s = Stack()
	print(s.is_empty())
	s.push(1)
	s.push("two")
	s.push(True)
	print(s.peek())
	print(s.items)
	s.pop()