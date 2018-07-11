# Code adapted from Corey Shafer
# sets and dictionaries both use {}. To declare an empty set tho you need to use the set() fxn
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

del student['age']
phone = student.pop('phone')
print(student.get('phone', 'Not Found'))
print(student)

print(student.items())
print(student.values())

for key, value in  student.items():
    print(key, value)


