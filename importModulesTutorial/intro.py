"""
Setting path using sys.path.append is ugly for the reason that you do not have the import statement at the top.
This can be rectified through the use of adding the path (of the modules folder) in environment variables.

In windows: computer > properties > advanced system settings > environment variables > New > Variable name : PYTHONPATH
Variable value: C:\\Users\\micha\\OneDrive\\Desktop\\modules (Unique based on where module folder is)
Note: Don't have double back slash in variable value, compiler gave out tho and I had to add them"""

import sys
#sys.path.append(r"C:\Users\micha\OneDrive\Desktop\modules")     # r in front converts to raw string
import my_module as mm
import random
import math
import calendar
import datetime
import os
import antigravity

# from my_module import find_index ---Is an alternative to import the fxn specificaly

courses = ['History', 'Math', 'Biology', 'Politics']

index = mm.find_index(courses, 'Math')
print("Index = ", index)
print(mm.test)
print(sys.path)

# Use of random library
random_course = random.choice(courses)
print(random_course)

# Use of math library
rads = math.radians(90)
print(math.sin(rads))

#Use of calendar and date library
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

print(os.getcwd())
print(os.__file__)