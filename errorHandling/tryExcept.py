# Goal of try, except block: catches which type of errors occurs and way to getaround them

try:
    f = open('testfile.txt')
    if f.name == 'testfile.txt':
        raise Exception
    var = 1
except FileNotFoundError as e:
    print("No go", e)
except Exception as e:
    print("Error!")
else:
    # Code that runs if try didn't run an exception
    print(f.read())
    f.close()
finally:
    # Runs no matter what happens.
    print("Executing finally...")