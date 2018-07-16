"""
Methods - function that is associated with a class, rather than fxns
Object is an instance of a class
Classes are blueprints for objects to use
Tutorial adapted from: Corey Schafer
"""
import datetime

class Employee:
	# Class variables are shared among all instances
	raise_amount = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + "@email.com"
		Employee.num_of_emps += 1

	def fullname(self):
		print('{} {}'.format(self.first, self.last))

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	# Class method when this @classmethod is placed over fxn
	@classmethod
	def set_raise_amt(cls, amount):
		# By doing this, setting raise_amount for all
		# objects and not just itself
		cls.raise_amount = amount

	# Class methods can be used as alternate structures
	@classmethod
	# Convention for these: starts with from_
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		# Return new employee object
		return cls(first, last, pay)

	# Syntax for decorators @.....
	# If not accessing the self variable, probs static method
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Sue', 'Smith', 60000)

# Class method insta passed, and changes raise amt for all
Employee.set_raise_amt(1.05)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# when we run this it gets transformed into:
# Employee.fullname(emp_1) and passes the instance of itself,
# this is why we need the self parameter as it holds the object
emp_1.fullname()

# Changes for all instances
Employee.raise_amount = 1.06

# Changes only for that specific instance
# but only if use .self If use .employee than changes for all 
emp_1.raise_amount = 1.07

print(emp_1.__dict__)
print("\n", Employee.__dict__)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Sue-Smith-90000'
emp_str_3 = 'Jimmy-Shoes-20000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

