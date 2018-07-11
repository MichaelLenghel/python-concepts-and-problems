# Code adapted from Corey Shafer
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Rather than doing a for each loop and appending to the list, this is a comprehension
my_list = [n for n in nums]

print(my_list)

# For the same thing, but multipling each value by itself:
my_list = [n*n for n in nums]
print(my_list)

# Using a map + lambda-> Doesn't read well at all. Use comprehensions
# my_list = map(lambda n: n*n, nums) 
# print(my_list)

#This time: I want 'n' for each 'n' in nums if 'n' is even
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '01234'
my_list = [(letter, num) for letter in 'abcd' for num in range(0, 4)]
print(my_list)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(list(zip(names, heroes)))

# my_dict = {}
# for names, heroes in zip(names, heroes):
# 	my_dict[names] = heroes
# print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heroes) if name != "Peter"}
print(my_dict)

# Remember: Sets have unique values
nums = [1,1,1,1,1, 2, 5, 7, 2, 9, 4, 8, 4]
my_set = set()
for n in nums:
	my_set.add(n)
print(my_set)

my_set = {n for n in nums}
print(my_set)

# generator Expressions:

