# Code adapted from Corey Shafer
"""Note: generators are more performat because they don't hold 
all the values at the same time! Way better in memory, altho execution
will be a bit slower"""

def square_numbers(nums):
	for i in nums:
		# yield makes this a generator
		# Returns one result at a time
		yield(i * i)

my_nums = square_numbers([1, 2, 3, 4, 5])

# Alternative list comprehension my_nums = [x*x for x in [1, 2, 3, 4, 5]]
# and my_nums = (x*x for x in [1, 2, 3, 4, 5]) with circular brackets we are using a generator
for num in my_nums:
	print(next(my_nums))