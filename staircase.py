#!/bin/python3

# Complete the staircase function below.
def staircase(n):
    counter = 1
    for i in range(0, n):
        # Spaces leading to the hastags
        for j in range(0, n - i - 1):
            print(end=" ")
        for k in range(0, counter):
             print("#", end="")
        print(end="\n")
        counter += 1
        
if __name__ == '__main__':
    n = int(input("Enter a number\n"))

    staircase(n)