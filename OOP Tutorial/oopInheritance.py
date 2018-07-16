# Tutorial adapted from: Corey Schafer

class Employee:
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + "@email.com"

	def fullname(self):
		print('{} {}'.format(self.first, self.last))

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

# Inherits from the employee class
# Has all the same attributes, constructors
# Uses method-resolution order to chain through the
# inheritance order of constructors and what not till it finds
# what is needed
class Developer(Employee):
	raise_amount = 1.10

	def __init__(self, first, last, pay, prog_lang):
		# Constructor chaining
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):
	# Never want to pass mutable objects like lists or dicts as argumnets
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('--->', end=" ")
			emp.fullname()


dev_1 = Developer('Corey', 'Schafer',50000, 'python')
dev_2 = Developer('Sue', 'Smith', 60000, 'java')

mgr_1 = Manager('Jack', 'Wan', 90000, [dev_1])
print(mgr_1.email)

print(isinstance(mgr_1, Manager))

print(issubclass(Manager, Employee))
