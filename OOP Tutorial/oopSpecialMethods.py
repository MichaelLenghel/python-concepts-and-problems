# Tutorial adapted from: Corey Schafer

class Employee:
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + "@email.com"

	def fullname(self):
		return'{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Sue', 'Smith', 60000)


# Will add what we specified in the function
print(emp_1 + emp_2)

# Prints length of what we specified
print(len(emp_1))

print(emp_1)
# print(repr(emp_1)): Unambigoously logs or prints info for object. Should be basically able to copy and paste as constructor

# print(str(emp_1)): Displays readable info for end user
# print(int.__add__(1, 2)) -> Called when u add two numbers in a print
# print(str.__add__('a', 'b')) -> Called when u concat two strings in a print
