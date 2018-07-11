# Code adapted from Corey Shafer
# Lists - can dynamically shrink grow or be changed - i.e. are mutable
print("____________________Lists__________________")
courses = ["History", "Math", "Physics", "CompSci"]
courses2 = ["Polotics", "Biology"]
nums = [1, 5, 2, 4, 3]
course_str = ', '.join(courses)
new_list = course_str.split(', ')  # Split up where you find a comma space and make a list
courses.append('Art')
courses.insert(0, 'Economics')
courses.extend(courses2)  # Adds the courses at the end to the original. Append will add the list itself.
courses.remove('Math')
poppedValue = courses.pop()  # Removes last value of a list - useful for lists ran like a queue


# To sort & reverse lists:
courses.reverse()
courses.sort(reverse=True)
sortedCourses = sorted(courses)
nums.sort(reverse=True)


print("Popped value: ", poppedValue)
print(courses)
print(courses[-1])  # Very useful to access last element as list can grow or shrink
print("Iterate", courses[0: 2])  # Cool way to print through indexes. First index is inclusive, second is not
print(courses[2:])  # This is known as slicing and will go until the end of the list
print(sortedCourses)
print(nums)
print(sum(nums))
print("Index of CompSci: ", courses.index("CompSci"))
print('Art' in courses)

for item in courses:
    print(item, end=", ")
print()
for index, course in enumerate(courses, start=1):
    print(index, course)

print(course_str)
print(new_list)

# Tuples - cannot be modified - i.e. immutable
print("____________________Tuples__________________")
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# Sets -Have no duplicates and if checking if something exists in a set is more efficient that lists or tuples
print("____________________Sets__________________")
coursesSet = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
coursesSet2 = {'History', 'Math', 'Art', 'Design'}
print(coursesSet)
print('Math' in coursesSet)  # The order of the set is random at runtime
print(coursesSet.intersection(coursesSet2))
print(coursesSet.difference(coursesSet2))
print(coursesSet.union(coursesSet2))



# Final point: Creating empty lists, tuples and sets
empty_list = []
empty_list2 = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}  # Not right! This is a dict
empty_set = set() # This is how it must be done!




