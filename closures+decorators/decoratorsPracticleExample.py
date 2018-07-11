# Code adapted from Corey Shafer
# Keep track of how many times a function was called
# Decorators most often used in logging

# Decorators are used a lot for working with third class libraries, routing
# Most confusing thing is keep track of all wrappers and whatnot
import time
from functools import wraps

def my_logger(orig_func):
	import logging
	# Matches name of original function
	logging.basicConfig(filename='({}.log'.format(orig_func.__name__), level=logging.INFO)

	# Preserves name of original function. Useful when chaining or stacking
	# decorators like done below, as order of exeuction wont mess up by returning the wrong names
	@wraps(orig_func)
	def wrapper(*args, **kwargs):
		logging.info(
			'ran with args: {}. and kwargs: {}'.format(args, kwargs))
		return orig_func(*args, **kwargs)

	return wrapper

def my_timer(orig_func):
	import time

	@wraps(orig_func)
	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = orig_func(*args, **kwargs)
		t2 = time.time() - t1
		print('{} ran in: {} sec'.format(orig_func.__name__, t2))
	return wrapper

@my_logger
@my_timer
def display_info(name, age):
	time.sleep(1)
	print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Hank', 30)