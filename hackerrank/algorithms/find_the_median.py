#!/bin/python3
# https://www.hackerrank.com/challenges/find-the-median

import sys
import math
def findTheMedian(n, arr):
    # Complete this function
    arr.sort()
    mid = n/2
    ceil = math.ceil(mid)
    floor = math.ceil(mid+0.45)
    return (arr[ceil-1] + arr[floor-1])/2

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
result = findTheMedian(n, arr)
print(result)