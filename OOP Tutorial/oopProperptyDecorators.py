class Employee:

	def __init__(self, first, last):
		self.first = first
		self.last = last

	# Allows us to access this like a variable
	# Useful when need to change setting a variable
	# with a setter and don't want to need to change
	# main code
	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(" ")
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print(' Delete Name!')
		self.first = None
		self.last = None


emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'

# Uses the setter to parse the names and set them
emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# Runs deleter function
del emp_1.fullname