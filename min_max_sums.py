#!/bin/python3

"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
"""

def miniMaxSum(arr):
    max = min = arr[0]
    min_index = max_index = max_sum = min_sum =  0
    for i, n in enumerate(arr):
        if max > n:
            max = n
            max_index = i
        if min < n:
            min = n
            min_index = i
            
    # Calculate the max sum
    for i, n in enumerate(arr):
        if i == min_index:
            continue
        else:
            max_sum += n
            
    # Calculate the min sum
    for i, n in enumerate(arr):
        if i == max_index:
            continue
        else:
            min_sum += n
    
    print("{0} {1}".format(max_sum, min_sum))
    
        
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
