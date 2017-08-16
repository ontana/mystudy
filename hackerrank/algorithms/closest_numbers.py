#!/bin/python3
# https://www.hackerrank.com/challenges/closest-numbers

import sys

def closetNumbers(n, arr):
    # Complete this function
    arr.sort()
    lowestDiff = arr[1] - arr[0]
    res = [arr[0], arr[1]]
    for i in range(1, n - 1):
    	diff = arr[i+1] - arr[i]
    	if diff < lowestDiff:
    		lowestDiff = diff
    		res = [arr[i], arr[i+1]]
    	elif diff == lowestDiff:
    		res.append(arr[i])
    		res.append(arr[i+1])
    return res

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
result = closetNumbers(n, arr)
print(*result)