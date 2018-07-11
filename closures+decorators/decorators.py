# Code adapted from Corey Shafer ->https://www.youtube.com/watch?v=FsAPt_9Bf3U

""" 
 Decorators - A function that takes another function as an argument
 adds functionality (with code before that function is executed) and returns the function as variable, all without altering the function
 that was passed as the argument.

 Can also use classes as decorators rather than functions
 """

def decorator_function(original_funciton):
	# *args, **kwargs allow us to use an number of positional arguments
	def wrapper_function(*args, **kwargs):
		print('Wrapper executed this before {}'.format(original_funciton.__name__))
		# Return the function we passed and set the variable
		return original_funciton(*args, **kwargs)
	return wrapper_function


# with this '@decorator_function', when fxn is ran
# executes what's before the wrapper_function first! Basicaly applies decorator
# Especially useful since decorator_function not ran now
# as when calling original decorated_display()
@decorator_function # decorator_functions are more common, but can use decorator_class
def display():
	print('Display function ran')

@decorator_function 
def display_info(name, age):
	print('display_info ran with arguments ({}, {})'.format(name, age))

# Pass in display function to this decorated fxn
decorated_display = decorator_function(display)


# decorated_display_info() class object
display_info('John', 25)

# decorated_display() function
display()