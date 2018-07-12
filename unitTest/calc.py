# Unit testing can show exactly what is broken.
# Tests do not run in order
# Generally write a test where it all passes, and when
# a new addition comes, can re-run tests.to ensure works
# Not the case in test-driven devlopment

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	if y == 0:
		raise ValueError("Cannot divide by zero!")
	return x / y