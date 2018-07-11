# Code adapted from Corey Shafer
# A closure allows a variable to hold the functions object reference with the varible that was passed to it initally. This variable
# called freely with parameters, but remembering what happened in the initall function call when the variable was transformed
# to a funciton

# A closure closes over variables in a function in it's own environment. This is very useful as it's a way of storing the  stuff that
# normally becomes random access memory from a function  

def outer_finc(msg):
	message = msg

	def inner_func():
		print(message)

	return inner_func()

outter_func()

#Returns the inner_func(). my_func is now a function
hi_func = outer_func('hi')
hello_func = outer_func('Hello')

print(hi_func.__name__) #This will print the name of the function that it is storing

hi_func()
hello_func()

# Inner function has access to inner methods

